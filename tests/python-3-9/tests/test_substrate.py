import sys
from pathlib import Path

import pytest
from pydantic import BaseModel

# add parent dir to sys.path to make 'substrate' importable
parent_dir = Path(__file__).resolve().parent.parent.parent.parent
sys.path.insert(0, str(parent_dir))

from substrate import Substrate
from substrate.core.corenode import CoreNode


class MockOutput(BaseModel):
    y: str


@pytest.mark.unit
class TestSubstrate:
    def test_serialize(self):
        a = CoreNode(x="y", out_type=MockOutput)
        b = CoreNode(x=a.future.y, out_type=MockOutput)
        c = CoreNode(x=b.future.y, out_type=MockOutput)

        # when the nodes are explicitly passed in
        result = Substrate.serialize(a, b, c)

        node_ids = sorted([d["id"] for d in result["nodes"]])
        assert node_ids == [a.id, b.id, c.id]
        assert len(result["futures"]) == 2

        # when the terminal node are passed in
        result = Substrate.serialize(c)

        node_ids = sorted([d["id"] for d in result["nodes"]])
        assert node_ids == [a.id, b.id, c.id]
        assert len(result["futures"]) == 2

    def test_serialize_with_depends_list(self):
        a = CoreNode(x="x", out_type=MockOutput)
        a.id = "a"
        b = CoreNode(x="x", out_type=MockOutput, _depends=[a])
        b.id = "b"
        c = CoreNode(x="x", out_type=MockOutput, _depends=[a, b])
        c.id = "c"

        # when nodes are connected via _depends, `edges` should be populated correctly
        edges = Substrate.serialize(a, b, c).get("edges")
        assert len(edges) == 3
        assert ["a", "b", {}] in edges
        assert ["a", "c", {}] in edges
        assert ["b", "c", {}] in edges
