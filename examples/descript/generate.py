# import os
# import json
#
# api_key = os.environ.get("SUBSTRATE_API_KEY")
# if api_key is None:
#     raise EnvironmentError("No SUBSTRATE_API_KEY set")
#
# from substrate import (
#     Substrate,
#     GenerateImage,
#     RemoveBackground,
#     EraseImage,
#     InpaintImage,
# )
#
# substrate = Substrate(api_key=api_key, timeout=60 * 5)
# prompt = "by edward hopper, a red leather wing chair in an open room, pillars, amazing painting composition"
# image = GenerateImage(prompt=prompt, negative_prompt="photo realistic", _cache_age=1000)
# fg = RemoveBackground(image_uri=image.future.image_uri)
# mask = RemoveBackground(
#     image_uri=image.future.image_uri,
#     return_mask=True,
# )
# bg = EraseImage(
#     image_uri=image.future.image_uri,
#     mask_image_uri=mask.future.image_uri,
# )
# bg_prompt = "by edward hopper, an empty room with pillars, amazing painting composition"
# inpaint = InpaintImage(image_uri=bg.future.image_uri, prompt=bg_prompt, store="hosted")
# result = substrate.run(inpaint)
# viz = Substrate.visualize(inpaint)
# os.system(f"open {viz}")
#
# print(json.dumps(result.json, indent=2))


# #!/usr/bin/env -S npx ts-node --transpileOnly
# import fs from "fs";
# import { Substrate, TranscribeSpeech } from "substrate";
# import { currentDir } from "./util";
#
# const sample = "https://media.substrate.run/my-dinner-andre.m4a"; // NB: this is a ~2hr long file
# const substrate = new Substrate({ apiKey: process.env["SUBSTRATE_API_KEY"] });
#
# const audio_uri = process.argv[2] || sample;
# const outfile = process.argv[3] || "descript.html";
# async function main() {
#   const transcribe = new TranscribeSpeech(
#     { audio_uri, segment: true, align: true },
#     { cache_age: 60 * 60 * 24 * 7 },
#   );
#   const res = await substrate.run(transcribe);
#   const transcript = res.get(transcribe);
#
#   const htmlTemplate = fs.readFileSync(`${currentDir}/index.html`, "utf8");
#   const html = htmlTemplate
#     .replace('"{{ segments }}"', JSON.stringify(transcript.segments, null, 2))
#     .replace("{{ audioUrl }}", audio_uri);
#   fs.writeFileSync(outfile, html);
# }
#
# main().then(() => console.log(`꩜ Done. View by running \`open ${outfile}\``));
