import os
import sys
import json
from substrate import ComputeJSON, sb, Substrate, TranscribeSpeech
from util import current_dir, list_chapters, proposed_schema, timestamped_schema, timestamp_prompt


api_key = os.environ.get("SUBSTRATE_API_KEY")
substrate = Substrate(api_key=api_key)

sample = "https://media.substrate.run/federer-dartmouth.m4a"
audio_uri = sys.argv[1] if len(sys.argv) > 1 else sample
outfile = sys.argv[2] if len(sys.argv) > 2 else "descript.html"

opts = {"_cache_age": 60 * 60 * 24 * 7}


def main():
    transcribe = TranscribeSpeech(audio_uri=audio_uri, segment=True, align=True, **opts)
    chapters = ComputeJSON(
        prompt=sb.concat(list_chapters, "\n\nTRANSCRIPT:\n\n", transcribe.future.text),
        json_schema=proposed_schema,
        model="Mixtral8x7BInstruct",
        **opts,
    )
    timestamps = ComputeJSON(
        prompt=sb.concat(
            timestamp_prompt,
            "SECTIONS: ",
            sb.jq(chapters.future.json_object, ".chapters | @json"),
            "\n\nTRANSCRIPT:\n\n",
            transcribe.future.text,
        ),
        json_schema=timestamped_schema,
        model="Mixtral8x7BInstruct",
        **opts,
    )

    res = substrate.run(transcribe, chapters, timestamps)
    transcript = res.get(transcribe)
    segments = [s.dict() for s in transcript.segments]
    timestamped_chapters = res.get(timestamps).json_object.get("chapters")

    with open(os.path.join(current_dir, "index.html"), "r") as f:
        html_template = f.read()

    html = (
        html_template.replace('"{{ segments }}"', json.dumps(segments, indent=2))
        .replace('"{{ chapters }}"', json.dumps(timestamped_chapters, indent=2))
        .replace("{{ audioUrl }}", audio_uri)
    )

    with open(outfile, "w") as f:
        f.write(html)


if __name__ == "__main__":
    main()
    print(f"꩜ Done. View by running `open {outfile}`")
