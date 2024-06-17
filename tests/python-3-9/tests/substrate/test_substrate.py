import pytest
from pydantic import BaseModel

from substrate.substrate import Substrate
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
