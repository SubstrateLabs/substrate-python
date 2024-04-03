"""
꩜ Substrate
@generated file
(using datamodel-codegen)
"""


from __future__ import annotations

from typing import Any, Dict, List
from typing_extensions import Literal, TypedDict, NotRequired


class ErrorOut(TypedDict):
    type: NotRequired[Literal["api_error", "invalid_request_error"]]
    """
    The type of error returned.
    """
    message: NotRequired[str]
    """
    A message providing more details about the error.
    """


class GenerateTextIn(TypedDict):
    prompt: NotRequired[str]
    """
    Input prompt.
    """
    temperature: NotRequired[int]
    """
    (Optional) Sampling temperature to use. Higher values make the output more random, lower values make the output more deterministic.
    """
    max_tokens: NotRequired[int]
    """
    (Optional) Maximum number of tokens to generate.
    """
    node: NotRequired[Literal["Mistral7BInstruct"]]
    """
    (Optional) Selected node.
    """


class GenerateTextOut(TypedDict):
    text: NotRequired[str]
    """
    (Optional) Text response.
    """


class GenerateJSONIn(TypedDict):
    prompt: NotRequired[str]
    """
    Input prompt.
    """
    json_schema: NotRequired[Dict[str, Any]]
    """
    JSON schema to guide `json_object` response.
    """
    temperature: NotRequired[int]
    """
    (Optional) Sampling temperature to use. Higher values make the output more random, lower values make the output more deterministic.
    """
    max_tokens: NotRequired[int]
    """
    (Optional) Maximum number of tokens to generate.
    """
    node: NotRequired[Literal["Mistral7BInstruct"]]
    """
    (Optional) Selected node.
    """


class GenerateJSONOut(TypedDict):
    json_object: NotRequired[Dict[str, Any]]
    """
    (Optional) JSON response.
    """


class MultiGenerateTextIn(TypedDict):
    prompt: NotRequired[str]
    """
    Input prompt.
    """
    num_choices: NotRequired[int]
    """
    Number of choices to generate.
    """
    temperature: NotRequired[int]
    """
    (Optional) Sampling temperature to use. Higher values make the output more random, lower values make the output more deterministic.
    """
    max_tokens: NotRequired[int]
    """
    (Optional) Maximum number of tokens to generate.
    """
    node: NotRequired[Literal["Mistral7BInstruct"]]
    """
    (Optional) Selected node.
    """


class MultiGenerateTextOut(TypedDict):
    choices: NotRequired[List[GenerateTextOut]]


class MultiGenerateJSONIn(TypedDict):
    prompt: NotRequired[str]
    """
    Input prompt.
    """
    json_schema: NotRequired[Dict[str, Any]]
    """
    JSON schema to guide `json_object` response.
    """
    num_choices: NotRequired[int]
    """
    Number of choices to generate.
    """
    temperature: NotRequired[int]
    """
    (Optional) Sampling temperature to use. Higher values make the output more random, lower values make the output more deterministic.
    """
    max_tokens: NotRequired[int]
    """
    (Optional) Maximum number of tokens to generate.
    """
    node: NotRequired[Literal["Mistral7BInstruct"]]
    """
    (Optional) Selected node.
    """


class MultiGenerateJSONOut(TypedDict):
    choices: NotRequired[List[GenerateJSONOut]]


class Mistral7BInstructIn(TypedDict):
    prompt: NotRequired[str]
    """
    Input prompt.
    """
    num_choices: NotRequired[int]
    """
    Number of choices to generate.
    """
    json_schema: NotRequired[Dict[str, Any]]
    """
    (Optional) JSON schema to guide response.
    """
    temperature: NotRequired[float]
    """
    (Optional) Sampling temperature to use. Higher values make the output more random, lower values make the output more deterministic.
    """
    max_tokens: NotRequired[int]
    """
    (Optional) Maximum number of tokens to generate.
    """


class Mistral7BInstructChoice(TypedDict):
    text: NotRequired[str]
    """
    (Optional) Text response, if `json_schema` was not provided.
    """
    json_object: NotRequired[Dict[str, Any]]
    """
    (Optional) JSON response, if `json_schema` was provided.
    """


class Mistral7BInstructOut(TypedDict):
    choices: NotRequired[List[Mistral7BInstructChoice]]


class GenerateTextVisionIn(TypedDict):
    prompt: NotRequired[str]
    """
    Text prompt.
    """
    image_uris: NotRequired[List[str]]
    """
    Image prompts.
    """
    temperature: NotRequired[int]
    """
    (Optional) Sampling temperature to use. Higher values make the output more random, lower values make the output more deterministic.
    """
    max_tokens: NotRequired[int]
    """
    (Optional) Maximum number of tokens to generate.
    """
    node: NotRequired[Literal["Firellava13B"]]
    """
    (Optional) Selected node.
    """


class GenerateTextVisionOut(TypedDict):
    text: NotRequired[str]
    """
    Text response.
    """


class Firellava13BIn(TypedDict):
    prompt: NotRequired[str]
    """
    Text prompt.
    """
    image_uris: NotRequired[List[str]]
    """
    Image prompts.
    """
    temperature: NotRequired[float]
    """
    (Optional) Sampling temperature to use. Higher values make the output more random, lower values make the output more deterministic.
    """
    max_tokens: NotRequired[int]
    """
    (Optional) Maximum number of tokens to generate.
    """


class Firellava13BOut(TypedDict):
    text: NotRequired[str]
    """
    Text response.
    """


class GenerateImageIn(TypedDict):
    prompt: NotRequired[str]
    """
    Text prompt.
    """
    store: NotRequired[str]
    """
    (Optional) Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](/docs/file-stores). If unset, the image data will be returned as a base64-encoded string.
    """
    node: NotRequired[Literal["StableDiffusionXL"]]
    """
    (Optional) Selected node.
    """


class GenerateImageOut(TypedDict):
    image_uri: NotRequired[str]
    """
    Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """


class MultiGenerateImageIn(TypedDict):
    prompt: NotRequired[str]
    """
    Text prompt.
    """
    num_images: NotRequired[int]
    """
    Number of images to generate.
    """
    store: NotRequired[str]
    """
    (Optional) Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](/docs/file-stores). If unset, the image data will be returned as a base64-encoded string.
    """
    node: NotRequired[Literal["StableDiffusionXL"]]
    """
    (Optional) Selected node.
    """


class MultiGenerateImageOut(TypedDict):
    outputs: NotRequired[List[GenerateImageOut]]


class StableDiffusionXLIn(TypedDict):
    prompt: NotRequired[str]
    """
    Text prompt.
    """
    negative_prompt: NotRequired[str]
    """
    (Optional) Negative input prompt.
    """
    steps: NotRequired[int]
    """
    (Optional) Number of diffusion steps.
    """
    num_images: NotRequired[int]
    """
    (Optional) Number of images to generate.
    """
    store: NotRequired[str]
    """
    (Optional) Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](/docs/file-stores). If unset, the image data will be returned as a base64-encoded string.
    """
    height: NotRequired[int]
    """
    (Optional) Height of output image, in pixels.
    """
    width: NotRequired[int]
    """
    (Optional) Width of output image, in pixels.
    """
    seeds: NotRequired[int]
    """
    (Optional) Seeds for deterministic generation. Default is a random seed.
    """
    guidance_scale: NotRequired[float]
    """
    (Optional) Higher values adhere to the text prompt more strongly, typically at the expense of image quality.
    """


class StableDiffusionImage(TypedDict):
    image_uri: NotRequired[str]
    """
    Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """
    seed: NotRequired[int]
    """
    The random noise seed used for generation.
    """


class StableDiffusionXLOut(TypedDict):
    outputs: NotRequired[List[StableDiffusionImage]]


class StableDiffusionXLIPAdapterIn(TypedDict):
    prompt: NotRequired[str]
    """
    Text prompt.
    """
    image_prompt_uri: NotRequired[str]
    """
    (Optional) Image prompt.
    """
    num_images: NotRequired[int]
    """
    Number of images to generate.
    """
    ip_adapter_scale: NotRequired[float]
    """
    (Optional) Controls the influence of the image prompt on the generated output.
    """
    negative_prompt: NotRequired[str]
    """
    (Optional) Negative input prompt.
    """
    store: NotRequired[str]
    """
    (Optional) Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](/docs/file-stores). If unset, the image data will be returned as a base64-encoded string.
    """
    width: NotRequired[int]
    """
    (Optional) Width of output image, in pixels.
    """
    height: NotRequired[int]
    """
    (Optional) Height of output image, in pixels.
    """
    seeds: NotRequired[List[int]]
    """
    (Optional) Random noise seeds. Default is random seeds for each generation.
    """


class StableDiffusionXLIPAdapterOut(TypedDict):
    outputs: NotRequired[List[StableDiffusionImage]]


class StableDiffusionXLControlNetIn(TypedDict):
    image_uri: NotRequired[str]
    """
    Input image.
    """
    control_method: NotRequired[Literal["edge", "depth", "illusion"]]
    """
    Strategy to control generation using the input image.
    """
    prompt: NotRequired[str]
    """
    Text prompt.
    """
    num_images: NotRequired[int]
    """
    Number of images to generate.
    """
    output_resolution: NotRequired[int]
    """
    (Optional) Resolution of the output image, in pixels.
    """
    negative_prompt: NotRequired[str]
    """
    (Optional) Negative input prompt.
    """
    store: NotRequired[str]
    """
    (Optional) Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](/docs/file-stores). If unset, the image data will be returned as a base64-encoded string.
    """
    conditioning_scale: NotRequired[float]
    """
    (Optional) Controls the influence of the input image on the generated output.
    """
    seeds: NotRequired[List[int]]
    """
    (Optional) Random noise seeds. Default is random seeds for each generation.
    """


class StableDiffusionXLControlNetOut(TypedDict):
    outputs: NotRequired[List[StableDiffusionImage]]


class GenerativeEditImageIn(TypedDict):
    image_uri: NotRequired[str]
    """
    Original image.
    """
    prompt: NotRequired[str]
    """
    Text prompt.
    """
    mask_image_uri: NotRequired[str]
    """
    (Optional) Mask image that controls which pixels are inpainted. If unset, the entire image is edited (image-to-image).
    """
    store: NotRequired[str]
    """
    (Optional) Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](/docs/file-stores). If unset, the image data will be returned as a base64-encoded string.
    """
    node: NotRequired[Literal["StableDiffusionXLInpaint"]]
    """
    (Optional) Selected node.
    """


class GenerativeEditImageOut(TypedDict):
    image_uri: NotRequired[str]
    """
    Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """


class MultiGenerativeEditImageIn(TypedDict):
    image_uri: NotRequired[str]
    """
    Original image.
    """
    prompt: NotRequired[str]
    """
    Text prompt.
    """
    mask_image_uri: NotRequired[str]
    """
    (Optional) Mask image that controls which pixels are edited (inpainting). If unset, the entire image is edited (image-to-image).
    """
    num_images: NotRequired[int]
    """
    Number of images to generate.
    """
    store: NotRequired[str]
    """
    (Optional) Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](/docs/file-stores). If unset, the image data will be returned as a base64-encoded string.
    """
    node: NotRequired[Literal["StableDiffusionXLInpaint"]]
    """
    (Optional) Selected node.
    """


class MultiGenerativeEditImageOut(TypedDict):
    outputs: NotRequired[List[GenerativeEditImageOut]]


class StableDiffusionXLInpaintIn(TypedDict):
    image_uri: NotRequired[str]
    """
    Original image.
    """
    prompt: NotRequired[str]
    """
    Text prompt.
    """
    mask_image_uri: NotRequired[str]
    """
    (Optional) Mask image that controls which pixels are edited (inpainting). If unset, the entire image is edited (image-to-image).
    """
    num_images: NotRequired[int]
    """
    Number of images to generate.
    """
    output_resolution: NotRequired[int]
    """
    (Optional) Resolution of the output image, in pixels.
    """
    negative_prompt: NotRequired[str]
    """
    (Optional) Negative input prompt.
    """
    store: NotRequired[str]
    """
    (Optional) Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](/docs/file-stores). If unset, the image data will be returned as a base64-encoded string.
    """
    strength: NotRequired[float]
    """
    (Optional) Controls the strength of the generation process.
    """
    seeds: NotRequired[List[int]]
    """
    (Optional) Random noise seeds. Default is random seeds for each generation.
    """


class StableDiffusionXLInpaintOut(TypedDict):
    outputs: NotRequired[List[StableDiffusionImage]]


class BoundingBox(TypedDict):
    x1: NotRequired[float]
    """
    Top left corner x.
    """
    y1: NotRequired[float]
    """
    Top left corner y.
    """
    x2: NotRequired[float]
    """
    Bottom right corner x.
    """
    y2: NotRequired[float]
    """
    Bottom right corner y.
    """


class Point(TypedDict):
    x: NotRequired[int]
    """
    X position.
    """
    y: NotRequired[int]
    """
    Y position.
    """


class FillMaskIn(TypedDict):
    image_uri: NotRequired[str]
    """
    Input image.
    """
    mask_image_uri: NotRequired[str]
    """
    Mask image that controls which pixels are inpainted.
    """
    model: NotRequired[Literal["big-lama"]]
    """
    (Optional) Selected model.
    """
    store: NotRequired[str]
    """
    (Optional) Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](/docs/file-stores). If unset, the image data will be returned as a base64-encoded string.
    """


class FillMaskOut(TypedDict):
    image_uri: NotRequired[str]
    """
    Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """


class RemoveBackgroundIn(TypedDict):
    image_uri: NotRequired[str]
    """
    Input image.
    """
    return_mask: NotRequired[bool]
    """
    (Optional) Return a mask image instead of the original content.
    """
    background_color: NotRequired[str]
    """
    (Optional) Hex value background color. Transparent if unset.
    """
    model: NotRequired[Literal["isnet"]]
    """
    (Optional) Selected model.
    """
    store: NotRequired[str]
    """
    (Optional) Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](/docs/file-stores). If unset, the image data will be returned as a base64-encoded string.
    """


class RemoveBackgroundOut(TypedDict):
    image_uri: NotRequired[str]
    """
    Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """


class UpscaleImageIn(TypedDict):
    image_uri: NotRequired[str]
    """
    Input image.
    """
    model: NotRequired[Literal["real-esrgan-x4"]]
    """
    (Optional) Selected model.
    """
    store: NotRequired[str]
    """
    (Optional) Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](/docs/file-stores). If unset, the image data will be returned as a base64-encoded string.
    """


class UpscaleImageOut(TypedDict):
    image_uri: NotRequired[str]
    """
    Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """


class DetectSegmentsIn(TypedDict):
    image_uri: NotRequired[str]
    """
    Input image.
    """
    point_prompts: NotRequired[List[Point]]
    """
    (Optional) Point prompts, to detect a segment under the point. One of `point_prompts` or `box_prompts` must be set.
    """
    box_prompts: NotRequired[List[BoundingBox]]
    """
    (Optional) Box prompts, to detect a segment within the bounding box. One of `point_prompts` or `box_prompts` must be set.
    """
    model: NotRequired[Literal["segment-anything"]]
    """
    (Optional) Selected model.
    """
    store: NotRequired[str]
    """
    (Optional) Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](/docs/file-stores). If unset, the image data will be returned as a base64-encoded string.
    """


class DetectSegmentsOut(TypedDict):
    mask_image_uri: NotRequired[str]
    """
    Detected segments in 'mask image' format. Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """


class TranscribeMediaIn(TypedDict):
    audio_uri: NotRequired[str]
    """
    Input audio.
    """
    prompt: NotRequired[str]
    """
    (Optional) Prompt to guide model on the content and context of input audio.
    """
    language: NotRequired[str]
    """
    (Optional) Language of input audio in [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes) format.
    """
    segment: NotRequired[bool]
    """
    (Optional) Segment the text into sentences with approximate timestamps.
    """
    align: NotRequired[bool]
    """
    (Optional) Align transcription to produce more accurate sentence-level timestamps and word-level timestamps. An array of word segments will be included in each sentence segment.
    """
    diarize: NotRequired[bool]
    """
    (Optional) Identify speakers for each segment. Speaker IDs will be included in each segment.
    """
    suggest_chapters: NotRequired[bool]
    """
    (Optional) Suggest automatic chapter markers.
    """


class TranscribedWord(TypedDict):
    word: NotRequired[str]
    """
    Text of word.
    """
    start: NotRequired[float]
    """
    (Optional) Start time of word, in seconds.
    """
    end: NotRequired[float]
    """
    (Optional) End time of word, in seconds.
    """
    speaker: NotRequired[str]
    """
    (Optional) ID of speaker, if `diarize` is enabled.
    """


class TranscribedSegment(TypedDict):
    text: NotRequired[str]
    """
    Text of segment.
    """
    start: NotRequired[float]
    """
    Start time of segment, in seconds.
    """
    end: NotRequired[float]
    """
    End time of segment, in seconds.
    """
    speaker: NotRequired[str]
    """
    (Optional) ID of speaker, if `diarize` is enabled.
    """
    words: NotRequired[List[TranscribedWord]]
    """
    (Optional) Aligned words, if `align` is enabled.
    """


class ChapterMarker(TypedDict):
    title: NotRequired[str]
    """
    Chapter title.
    """
    start: NotRequired[float]
    """
    Start time of chapter, in seconds.
    """


class TranscribeMediaOut(TypedDict):
    text: NotRequired[str]
    """
    Transcribed text.
    """
    segments: NotRequired[List[TranscribedSegment]]
    """
    (Optional) Transcribed segments, if `segment` is enabled.
    """
    chapters: NotRequired[List[ChapterMarker]]
    """
    (Optional) Chapter markers, if `suggest_chapters` is enabled.
    """


class GenerateSpeechIn(TypedDict):
    text: NotRequired[str]
    """
    Input text.
    """
    audio_uri: NotRequired[str]
    """
    (Optional) Reference audio used to synthesize the speaker. If unset, a default speaker voice will be used.
    """
    language: NotRequired[str]
    """
    (Optional) Language of input text. Supported languages: `en, de, fr, es, it, pt, pl, zh, ar, cs, ru, nl, tr, hu, ko`.
    """
    store: NotRequired[str]
    """
    (Optional) Use "hosted" to return an audio URL hosted on Substrate. You can also provide a URL to a registered [file store](/docs/file-stores). If unset, the audio data will be returned as a base64-encoded string.
    """


class GenerateSpeechOut(TypedDict):
    audio_uri: NotRequired[str]
    """
    Base 64-encoded WAV audio bytes, or a hosted audio url if `store` is provided.
    """


class Embedding(TypedDict):
    vector: NotRequired[List[float]]
    """
    Embedding vector.
    """
    doc_id: NotRequired[str]
    """
    (Optional) Vector store document ID.
    """
    metadata: NotRequired[Dict[str, Any]]
    """
    (Optional) Vector store document metadata.
    """


class EmbedTextIn(TypedDict):
    text: NotRequired[str]
    """
    Text to embed.
    """
    store: NotRequired[str]
    """
    (Optional) [Vector store](/docs/vector-stores) identifier.
    """
    metadata: NotRequired[Dict[str, Any]]
    """
    (Optional) Metadata that can be used to query the vector store. Ignored if `store` is unset.
    """
    embedded_metadata_keys: NotRequired[List[str]]
    """
    (Optional) Choose keys from `metadata` to embed with text.
    """
    doc_id: NotRequired[str]
    """
    (Optional) Vector store document ID. Ignored if `store` is unset.
    """
    node: NotRequired[Literal["JinaV2", "CLIP"]]
    """
    (Optional) Selected node.
    """


class EmbedTextOut(TypedDict):
    embedding: NotRequired[Embedding]
    """
    Generated embedding.
    """


class EmbedTextItem(TypedDict):
    text: NotRequired[str]
    """
    Text to embed.
    """
    metadata: NotRequired[Dict[str, Any]]
    """
    (Optional) Metadata that can be used to query the vector store. Ignored if `store` is unset.
    """
    doc_id: NotRequired[str]
    """
    (Optional) Vector store document ID. Ignored if `store` is unset.
    """


class MultiEmbedTextIn(TypedDict):
    items: NotRequired[List[EmbedTextItem]]
    """
    Items to embed.
    """
    store: NotRequired[str]
    """
    (Optional) [Vector store](/docs/vector-stores) identifier.
    """
    embedded_metadata_keys: NotRequired[List[str]]
    """
    (Optional) Choose keys from `metadata` to embed with text.
    """
    node: NotRequired[Literal["JinaV2", "CLIP"]]
    """
    (Optional) Selected node.
    """


class MultiEmbedTextOut(TypedDict):
    embeddings: NotRequired[List[Embedding]]
    """
    Generated embeddings.
    """


class JinaV2In(TypedDict):
    items: NotRequired[List[EmbedTextItem]]
    """
    Items to embed.
    """
    store: NotRequired[str]
    """
    (Optional) [Vector store](/docs/vector-stores) identifier.
    """
    embedded_metadata_keys: NotRequired[List[str]]
    """
    (Optional) Choose keys from `metadata` to embed with text.
    """


class JinaV2Out(TypedDict):
    embeddings: NotRequired[List[Embedding]]
    """
    Generated embeddings.
    """


class EmbedImageIn(TypedDict):
    image_uri: NotRequired[str]
    """
    Image to embed.
    """
    store: NotRequired[str]
    """
    (Optional) [Vector store](/docs/vector-stores) identifier.
    """
    doc_id: NotRequired[str]
    """
    (Optional) Vector store document ID. Ignored if `store` is unset.
    """
    node: NotRequired[Literal["CLIP"]]
    """
    (Optional) Selected node.
    """


class EmbedImageOut(TypedDict):
    embedding: NotRequired[Embedding]
    """
    Generated embedding.
    """


class EmbedImageItem(TypedDict):
    image_uri: NotRequired[str]
    """
    Image to embed.
    """
    doc_id: NotRequired[str]
    """
    (Optional) Vector store document ID. Ignored if `store` is unset.
    """


class EmbedTextOrImageItem(TypedDict):
    image_uri: NotRequired[str]
    """
    (Optional) Image to embed.
    """
    text: NotRequired[str]
    """
    (Optional) Text to embed.
    """
    metadata: NotRequired[Dict[str, Any]]
    """
    (Optional) Metadata that can be used to query the vector store. Ignored if `store` is unset.
    """
    doc_id: NotRequired[str]
    """
    (Optional) Vector store document ID. Ignored if `store` is unset.
    """


class MultiEmbedImageIn(TypedDict):
    items: NotRequired[List[EmbedImageItem]]
    """
    Items to embed.
    """
    store: NotRequired[str]
    """
    (Optional) [Vector store](/docs/vector-stores) identifier.
    """
    node: NotRequired[Literal["CLIP"]]
    """
    (Optional) Selected node.
    """


class MultiEmbedImageOut(TypedDict):
    embeddings: NotRequired[List[Embedding]]
    """
    Generated embeddings.
    """


class CLIPIn(TypedDict):
    items: NotRequired[List[EmbedTextOrImageItem]]
    """
    Items to embed.
    """
    embedded_metadata_keys: NotRequired[List[str]]
    """
    (Optional) Choose keys from `metadata` to embed with text, when embedding and storing text documents.
    """
    store: NotRequired[str]
    """
    (Optional) [Vector store](/docs/vector-stores) identifier.
    """


class CLIPOut(TypedDict):
    embeddings: NotRequired[List[Embedding]]
    """
    Generated embeddings.
    """


class VectorStoreParams(TypedDict):
    name: NotRequired[str]
    """
    Vector store name.
    """
    model: NotRequired[Literal["jina-v2", "clip"]]
    """
    Selected embedding model
    """
    m: NotRequired[int]
    """
    (Optional) The max number of connections per layer for the index.
    """
    ef_construction: NotRequired[int]
    """
    (Optional) The size of the dynamic candidate list for constructing the index graph.
    """
    metric: NotRequired[Literal["cosine", "l2", "inner"]]
    """
    (Optional) The distance metric to construct the index with.
    """


class DeleteVectorStoreParams(TypedDict):
    name: NotRequired[str]
    """
    Vector store name.
    """
    model: NotRequired[Literal["jina-v2", "clip"]]
    """
    Selected embedding model
    """


class Vector(TypedDict):
    """
    Canonical representation of document with embedding vector.
    """

    id: NotRequired[str]
    """
    Document ID.
    """
    vector: NotRequired[List[float]]
    """
    Embedding vector.
    """
    metadata: NotRequired[Dict[str, Any]]
    """
    Document metadata.
    """


class GetVectorsParams(TypedDict):
    name: NotRequired[str]
    """
    Vector store name.
    """
    model: NotRequired[Literal["jina-v2", "clip"]]
    """
    Selected embedding model
    """
    ids: NotRequired[List[str]]
    """
    Document IDs to retrieve.
    """


class GetVectorsResponse(TypedDict):
    vectors: NotRequired[List[Vector]]
    """
    Retrieved vectors.
    """


class VectorUpdateCountResponse(TypedDict):
    count: NotRequired[int]
    """
    Number of vectors modified.
    """


class UpdateVectorParams(TypedDict):
    """
    Document to update.
    """

    id: NotRequired[str]
    """
    Document ID.
    """
    vector: NotRequired[List[float]]
    """
    (Optional) Embedding vector.
    """
    metadata: NotRequired[Dict[str, Any]]
    """
    (Optional) Document metadata.
    """


class UpdateVectorsParams(TypedDict):
    name: NotRequired[str]
    """
    Vector store name.
    """
    model: NotRequired[Literal["jina-v2", "clip"]]
    """
    Selected embedding model
    """
    vectors: NotRequired[List[UpdateVectorParams]]
    """
    Vectors to upsert.
    """


class DeleteVectorsParams(TypedDict):
    name: NotRequired[str]
    """
    Vector store name.
    """
    model: NotRequired[Literal["jina-v2", "clip"]]
    """
    Selected embedding model
    """
    ids: NotRequired[List[str]]
    """
    Document IDs to delete.
    """


class QueryVectorStoreParams(TypedDict):
    name: NotRequired[str]
    """
    Vector store to query against.
    """
    model: NotRequired[Literal["jina-v2", "clip"]]
    """
    Selected embedding model
    """
    query_ids: NotRequired[List[str]]
    """
    (Optional) Document IDs to use for the query.
    """
    query_image_uris: NotRequired[List[str]]
    """
    (Optional) Image URIs to embed and use for the query.
    """
    query_vectors: NotRequired[List[List[float]]]
    """
    (Optional) Vector to use for the query.
    """
    query_strings: NotRequired[List[str]]
    """
    (Optional) Texts to embed and use for the query.
    """
    top_k: NotRequired[int]
    """
    (Optional) Number of results to return.
    """
    ef_search: NotRequired[int]
    """
    (Optional) The size of the dynamic candidate list for searching the index graph.
    """
    include_values: NotRequired[bool]
    """
    (Optional) Include the values of the vectors in the response.
    """
    include_metadata: NotRequired[bool]
    """
    (Optional) Include the metadata of the vectors in the response.
    """
    filters: NotRequired[Dict[str, Any]]
    """
    (Optional) Filter metadata by key-value pairs.
    """


class VectorStoreQueryResult(TypedDict):
    id: NotRequired[str]
    """
    Document ID.
    """
    distance: NotRequired[float]
    """
    Similarity score.
    """
    vector: NotRequired[List[float]]
    """
    (Optional) Embedding vector.
    """
    metadata: NotRequired[Dict[str, Any]]
    """
    (Optional) Document metadata.
    """


class QueryVectorStoreResponse(TypedDict):
    results: NotRequired[List[List[VectorStoreQueryResult]]]
    """
    Query results.
    """
    name: NotRequired[str]
    """
    (Optional) Vector store name.
    """
    model: NotRequired[Literal["jina-v2", "clip"]]
    """
    (Optional) Selected embedding model
    """
    metric: NotRequired[Literal["cosine", "l2", "inner"]]
    """
    (Optional) The distance metric used for the query.
    """
