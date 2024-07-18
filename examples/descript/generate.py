import os

import sys
import json
from substrate import Substrate, TranscribeSpeech

current_dir = os.path.dirname(os.path.abspath(__file__))
api_key = os.environ.get("SUBSTRATE_API_KEY")
substrate = Substrate(api_key=api_key, timeout=60 * 5)
sample = "https://media.substrate.run/my-dinner-andre.m4a"
audio_uri = sys.argv[1] if len(sys.argv) > 1 else sample
outfile = sys.argv[2] if len(sys.argv) > 2 else "descript.html"


def main():
    transcribe = TranscribeSpeech(audio_uri=audio_uri, segment=True, align=True, _cache_age=60 * 60 * 24 * 7)
    result = substrate.run(transcribe)
    transcript = result.get(transcribe)
    segments = [s.dict() for s in transcript.segments]

    with open(os.path.join(current_dir, "index.html"), "r") as f:
        html_template = f.read()
    html = html_template.replace('"{{ segments }}"', json.dumps(segments, indent=2)).replace(
        "{{ audioUrl }}", audio_uri
    )
    with open(outfile, "w") as f:
        f.write(html)


if __name__ == "__main__":
    main()
    print(f"꩜ Done. View by running `open {outfile}`")
