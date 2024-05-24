import os
import sys
from pathlib import Path


class Test:
    def test_basic(self):
        # add parent dir to sys.path to make 'substrate' importable
        parent_dir = Path(__file__).resolve().parent.parent.parent.parent
        sys.path.insert(0, str(parent_dir))

        api_key = os.environ.get("SUBSTRATE_API_KEY")
        if api_key is None:
            raise EnvironmentError("No SUBSTRATE_API_KEY set")

        from substrate import Substrate, GenerateText

        substrate = Substrate(api_key=api_key)

        story = GenerateText(prompt="tell me a story", max_tokens=8)
        response = substrate.run(story)

        summary_out = response.get(story)
        assert len(summary_out.text) > 0
