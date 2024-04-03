"""
꩜ Substrate
@generated file
(using datamodel-codegen)
"""


from __future__ import annotations

from typing import Any, Dict, List, Optional
from dataclasses import dataclass
from typing_extensions import Literal


@dataclass
class ErrorOut:
    """
    (Future reference)
    """

    type: Literal["api_error", "invalid_request_error"]
    """
    (Future reference)
    The type of error returned.
    """
    message: str
    """
    (Future reference)
    A message providing more details about the error.
    """


@dataclass
class FutureGenerateTextIn:
    """
    (Future reference)
    """

    prompt: str
    """
    (Future reference)
    Input prompt.
    """
    temperature: Optional[int] = 4
    """
    (Future reference)
    Sampling temperature to use. Higher values make the output more random, lower values make the output more deterministic.
    """
    max_tokens: Optional[int] = None
    """
    (Future reference)
    Maximum number of tokens to generate.
    """
    node: Optional[Literal["Mistral7BInstruct"]] = "Mistral7BInstruct"
    """
    (Future reference)
    Selected node.
    """


@dataclass
class FutureGenerateTextOut:
    """
    (Future reference)
    """

    text: Optional[str] = None
    """
    (Future reference)
    Text response.
    """


@dataclass
class FutureGenerateJSONIn:
    """
    (Future reference)
    """

    prompt: str
    """
    (Future reference)
    Input prompt.
    """
    json_schema: Dict[str, Any]
    """
    (Future reference)
    JSON schema to guide `json_object` response.
    """
    temperature: Optional[int] = 4
    """
    (Future reference)
    Sampling temperature to use. Higher values make the output more random, lower values make the output more deterministic.
    """
    max_tokens: Optional[int] = None
    """
    (Future reference)
    Maximum number of tokens to generate.
    """
    node: Optional[Literal["Mistral7BInstruct"]] = "Mistral7BInstruct"
    """
    (Future reference)
    Selected node.
    """


@dataclass
class FutureGenerateJSONOut:
    """
    (Future reference)
    """

    json_object: Optional[Dict[str, Any]] = None
    """
    (Future reference)
    JSON response.
    """


@dataclass
class FutureMultiGenerateTextIn:
    """
    (Future reference)
    """

    prompt: str
    """
    (Future reference)
    Input prompt.
    """
    num_choices: int
    """
    (Future reference)
    Number of choices to generate.
    """
    temperature: Optional[int] = 4
    """
    (Future reference)
    Sampling temperature to use. Higher values make the output more random, lower values make the output more deterministic.
    """
    max_tokens: Optional[int] = None
    """
    (Future reference)
    Maximum number of tokens to generate.
    """
    node: Optional[Literal["Mistral7BInstruct"]] = "Mistral7BInstruct"
    """
    (Future reference)
    Selected node.
    """


@dataclass
class FutureMultiGenerateTextOut:
    """
    (Future reference)
    """

    choices: List[FutureGenerateTextOut]


@dataclass
class FutureMultiGenerateJSONIn:
    """
    (Future reference)
    """

    prompt: str
    """
    (Future reference)
    Input prompt.
    """
    json_schema: Dict[str, Any]
    """
    (Future reference)
    JSON schema to guide `json_object` response.
    """
    num_choices: int
    """
    (Future reference)
    Number of choices to generate.
    """
    temperature: Optional[int] = 4
    """
    (Future reference)
    Sampling temperature to use. Higher values make the output more random, lower values make the output more deterministic.
    """
    max_tokens: Optional[int] = None
    """
    (Future reference)
    Maximum number of tokens to generate.
    """
    node: Optional[Literal["Mistral7BInstruct"]] = "Mistral7BInstruct"
    """
    (Future reference)
    Selected node.
    """


@dataclass
class FutureMultiGenerateJSONOut:
    """
    (Future reference)
    """

    choices: List[FutureGenerateJSONOut]


@dataclass
class FutureMistral7BInstructIn:
    """
    (Future reference)
    """

    prompt: str
    """
    (Future reference)
    Input prompt.
    """
    num_choices: int
    """
    (Future reference)
    Number of choices to generate.
    """
    json_schema: Optional[Dict[str, Any]] = None
    """
    (Future reference)
    JSON schema to guide response.
    """
    temperature: Optional[float] = None
    """
    (Future reference)
    Sampling temperature to use. Higher values make the output more random, lower values make the output more deterministic.
    """
    max_tokens: Optional[int] = None
    """
    (Future reference)
    Maximum number of tokens to generate.
    """


@dataclass
class Mistral7BInstructChoice:
    """
    (Future reference)
    """

    text: Optional[str] = None
    """
    (Future reference)
    Text response, if `json_schema` was not provided.
    """
    json_object: Optional[Dict[str, Any]] = None
    """
    (Future reference)
    JSON response, if `json_schema` was provided.
    """


@dataclass
class FutureMistral7BInstructOut:
    """
    (Future reference)
    """

    choices: List[Mistral7BInstructChoice]


@dataclass
class FutureGenerateTextVisionIn:
    """
    (Future reference)
    """

    prompt: str
    """
    (Future reference)
    Text prompt.
    """
    image_uris: List[str]
    """
    (Future reference)
    Image prompts.
    """
    temperature: Optional[int] = 4
    """
    (Future reference)
    Sampling temperature to use. Higher values make the output more random, lower values make the output more deterministic.
    """
    max_tokens: Optional[int] = 800
    """
    (Future reference)
    Maximum number of tokens to generate.
    """
    node: Optional[Literal["Firellava13B"]] = "Firellava13B"
    """
    (Future reference)
    Selected node.
    """


@dataclass
class FutureGenerateTextVisionOut:
    """
    (Future reference)
    """

    text: str
    """
    (Future reference)
    Text response.
    """


@dataclass
class FutureFirellava13BIn:
    """
    (Future reference)
    """

    prompt: str
    """
    (Future reference)
    Text prompt.
    """
    image_uris: List[str]
    """
    (Future reference)
    Image prompts.
    """
    temperature: Optional[float] = None
    """
    (Future reference)
    Sampling temperature to use. Higher values make the output more random, lower values make the output more deterministic.
    """
    max_tokens: Optional[int] = 800
    """
    (Future reference)
    Maximum number of tokens to generate.
    """


@dataclass
class FutureFirellava13BOut:
    """
    (Future reference)
    """

    text: str
    """
    (Future reference)
    Text response.
    """


@dataclass
class FutureGenerateImageIn:
    """
    (Future reference)
    """

    prompt: str
    """
    (Future reference)
    Text prompt.
    """
    store: Optional[str] = None
    """
    (Future reference)
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](/docs/file-stores). If unset, the image data will be returned as a base64-encoded string.
    """
    node: Optional[Literal["StableDiffusionXL"]] = "StableDiffusionXL"
    """
    (Future reference)
    Selected node.
    """


@dataclass
class FutureGenerateImageOut:
    """
    (Future reference)
    """

    image_uri: str
    """
    (Future reference)
    Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """


@dataclass
class FutureMultiGenerateImageIn:
    """
    (Future reference)
    """

    prompt: str
    """
    (Future reference)
    Text prompt.
    """
    num_images: int
    """
    (Future reference)
    Number of images to generate.
    """
    store: Optional[str] = None
    """
    (Future reference)
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](/docs/file-stores). If unset, the image data will be returned as a base64-encoded string.
    """
    node: Optional[Literal["StableDiffusionXL"]] = "StableDiffusionXL"
    """
    (Future reference)
    Selected node.
    """


@dataclass
class FutureMultiGenerateImageOut:
    """
    (Future reference)
    """

    outputs: List[FutureGenerateImageOut]


@dataclass
class FutureStableDiffusionXLIn:
    """
    (Future reference)
    """

    prompt: str
    """
    (Future reference)
    Text prompt.
    """
    negative_prompt: Optional[str] = None
    """
    (Future reference)
    Negative input prompt.
    """
    steps: Optional[int] = None
    """
    (Future reference)
    Number of diffusion steps.
    """
    num_images: Optional[int] = None
    """
    (Future reference)
    Number of images to generate.
    """
    store: Optional[str] = None
    """
    (Future reference)
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](/docs/file-stores). If unset, the image data will be returned as a base64-encoded string.
    """
    height: Optional[int] = None
    """
    (Future reference)
    Height of output image, in pixels.
    """
    width: Optional[int] = None
    """
    (Future reference)
    Width of output image, in pixels.
    """
    seeds: Optional[int] = None
    """
    (Future reference)
    Seeds for deterministic generation. Default is a random seed.
    """
    guidance_scale: Optional[float] = 5
    """
    (Future reference)
    Higher values adhere to the text prompt more strongly, typically at the expense of image quality.
    """


@dataclass
class StableDiffusionImage:
    """
    (Future reference)
    """

    image_uri: str
    """
    (Future reference)
    Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """
    seed: int
    """
    (Future reference)
    The random noise seed used for generation.
    """


@dataclass
class FutureStableDiffusionXLOut:
    """
    (Future reference)
    """

    outputs: List[StableDiffusionImage]


@dataclass
class FutureStableDiffusionXLIPAdapterIn:
    """
    (Future reference)
    """

    prompt: str
    """
    (Future reference)
    Text prompt.
    """
    num_images: int
    """
    (Future reference)
    Number of images to generate.
    """
    image_prompt_uri: Optional[str] = None
    """
    (Future reference)
    Image prompt.
    """
    ip_adapter_scale: Optional[float] = None
    """
    (Future reference)
    Controls the influence of the image prompt on the generated output.
    """
    negative_prompt: Optional[str] = None
    """
    (Future reference)
    Negative input prompt.
    """
    store: Optional[str] = None
    """
    (Future reference)
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](/docs/file-stores). If unset, the image data will be returned as a base64-encoded string.
    """
    width: Optional[int] = None
    """
    (Future reference)
    Width of output image, in pixels.
    """
    height: Optional[int] = None
    """
    (Future reference)
    Height of output image, in pixels.
    """
    seeds: Optional[List[int]] = None
    """
    (Future reference)
    Random noise seeds. Default is random seeds for each generation.
    """


@dataclass
class FutureStableDiffusionXLIPAdapterOut:
    """
    (Future reference)
    """

    outputs: List[StableDiffusionImage]


@dataclass
class FutureStableDiffusionXLControlNetIn:
    """
    (Future reference)
    """

    image_uri: str
    """
    (Future reference)
    Input image.
    """
    control_method: Literal["edge", "depth", "illusion"]
    """
    (Future reference)
    Strategy to control generation using the input image.
    """
    prompt: str
    """
    (Future reference)
    Text prompt.
    """
    num_images: int
    """
    (Future reference)
    Number of images to generate.
    """
    output_resolution: Optional[int] = 1024
    """
    (Future reference)
    Resolution of the output image, in pixels.
    """
    negative_prompt: Optional[str] = None
    """
    (Future reference)
    Negative input prompt.
    """
    store: Optional[str] = None
    """
    (Future reference)
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](/docs/file-stores). If unset, the image data will be returned as a base64-encoded string.
    """
    conditioning_scale: Optional[float] = None
    """
    (Future reference)
    Controls the influence of the input image on the generated output.
    """
    seeds: Optional[List[int]] = None
    """
    (Future reference)
    Random noise seeds. Default is random seeds for each generation.
    """


@dataclass
class FutureStableDiffusionXLControlNetOut:
    """
    (Future reference)
    """

    outputs: List[StableDiffusionImage]


@dataclass
class FutureGenerativeEditImageIn:
    """
    (Future reference)
    """

    image_uri: str
    """
    (Future reference)
    Original image.
    """
    prompt: str
    """
    (Future reference)
    Text prompt.
    """
    mask_image_uri: Optional[str] = None
    """
    (Future reference)
    Mask image that controls which pixels are inpainted. If unset, the entire image is edited (image-to-image).
    """
    store: Optional[str] = None
    """
    (Future reference)
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](/docs/file-stores). If unset, the image data will be returned as a base64-encoded string.
    """
    node: Optional[Literal["StableDiffusionXLInpaint"]] = "StableDiffusionXLInpaint"
    """
    (Future reference)
    Selected node.
    """


@dataclass
class FutureGenerativeEditImageOut:
    """
    (Future reference)
    """

    image_uri: str
    """
    (Future reference)
    Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """


@dataclass
class FutureMultiGenerativeEditImageIn:
    """
    (Future reference)
    """

    image_uri: str
    """
    (Future reference)
    Original image.
    """
    prompt: str
    """
    (Future reference)
    Text prompt.
    """
    num_images: int
    """
    (Future reference)
    Number of images to generate.
    """
    mask_image_uri: Optional[str] = None
    """
    (Future reference)
    Mask image that controls which pixels are edited (inpainting). If unset, the entire image is edited (image-to-image).
    """
    store: Optional[str] = None
    """
    (Future reference)
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](/docs/file-stores). If unset, the image data will be returned as a base64-encoded string.
    """
    node: Optional[Literal["StableDiffusionXLInpaint"]] = "StableDiffusionXLInpaint"
    """
    (Future reference)
    Selected node.
    """


@dataclass
class FutureMultiGenerativeEditImageOut:
    """
    (Future reference)
    """

    outputs: List[FutureGenerativeEditImageOut]


@dataclass
class FutureStableDiffusionXLInpaintIn:
    """
    (Future reference)
    """

    image_uri: str
    """
    (Future reference)
    Original image.
    """
    prompt: str
    """
    (Future reference)
    Text prompt.
    """
    num_images: int
    """
    (Future reference)
    Number of images to generate.
    """
    mask_image_uri: Optional[str] = None
    """
    (Future reference)
    Mask image that controls which pixels are edited (inpainting). If unset, the entire image is edited (image-to-image).
    """
    output_resolution: Optional[int] = 1024
    """
    (Future reference)
    Resolution of the output image, in pixels.
    """
    negative_prompt: Optional[str] = None
    """
    (Future reference)
    Negative input prompt.
    """
    store: Optional[str] = None
    """
    (Future reference)
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](/docs/file-stores). If unset, the image data will be returned as a base64-encoded string.
    """
    strength: Optional[float] = 0.5
    """
    (Future reference)
    Controls the strength of the generation process.
    """
    seeds: Optional[List[int]] = None
    """
    (Future reference)
    Random noise seeds. Default is random seeds for each generation.
    """


@dataclass
class FutureStableDiffusionXLInpaintOut:
    """
    (Future reference)
    """

    outputs: List[StableDiffusionImage]


@dataclass
class BoundingBox:
    """
    (Future reference)
    """

    x1: float
    """
    (Future reference)
    Top left corner x.
    """
    y1: float
    """
    (Future reference)
    Top left corner y.
    """
    x2: float
    """
    (Future reference)
    Bottom right corner x.
    """
    y2: float
    """
    (Future reference)
    Bottom right corner y.
    """


@dataclass
class Point:
    """
    (Future reference)
    """

    x: int
    """
    (Future reference)
    X position.
    """
    y: int
    """
    (Future reference)
    Y position.
    """


@dataclass
class FutureFillMaskIn:
    """
    (Future reference)
    """

    image_uri: str
    """
    (Future reference)
    Input image.
    """
    mask_image_uri: str
    """
    (Future reference)
    Mask image that controls which pixels are inpainted.
    """
    model: Optional[Literal["big-lama"]] = "big-lama"
    """
    (Future reference)
    Selected model.
    """
    store: Optional[str] = None
    """
    (Future reference)
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](/docs/file-stores). If unset, the image data will be returned as a base64-encoded string.
    """


@dataclass
class FutureFillMaskOut:
    """
    (Future reference)
    """

    image_uri: str
    """
    (Future reference)
    Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """


@dataclass
class FutureRemoveBackgroundIn:
    """
    (Future reference)
    """

    image_uri: str
    """
    (Future reference)
    Input image.
    """
    return_mask: Optional[bool] = None
    """
    (Future reference)
    Return a mask image instead of the original content.
    """
    background_color: Optional[str] = None
    """
    (Future reference)
    Hex value background color. Transparent if unset.
    """
    model: Optional[Literal["isnet"]] = "isnet"
    """
    (Future reference)
    Selected model.
    """
    store: Optional[str] = None
    """
    (Future reference)
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](/docs/file-stores). If unset, the image data will be returned as a base64-encoded string.
    """


@dataclass
class FutureRemoveBackgroundOut:
    """
    (Future reference)
    """

    image_uri: str
    """
    (Future reference)
    Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """


@dataclass
class FutureUpscaleImageIn:
    """
    (Future reference)
    """

    image_uri: str
    """
    (Future reference)
    Input image.
    """
    model: Optional[Literal["real-esrgan-x4"]] = "real-esrgan-x4"
    """
    (Future reference)
    Selected model.
    """
    store: Optional[str] = None
    """
    (Future reference)
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](/docs/file-stores). If unset, the image data will be returned as a base64-encoded string.
    """


@dataclass
class FutureUpscaleImageOut:
    """
    (Future reference)
    """

    image_uri: str
    """
    (Future reference)
    Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """


@dataclass
class FutureDetectSegmentsIn:
    """
    (Future reference)
    """

    image_uri: str
    """
    (Future reference)
    Input image.
    """
    point_prompts: Optional[List[Point]] = None
    """
    (Future reference)
    Point prompts, to detect a segment under the point. One of `point_prompts` or `box_prompts` must be set.
    """
    box_prompts: Optional[List[BoundingBox]] = None
    """
    (Future reference)
    Box prompts, to detect a segment within the bounding box. One of `point_prompts` or `box_prompts` must be set.
    """
    model: Optional[Literal["segment-anything"]] = "segment-anything"
    """
    (Future reference)
    Selected model.
    """
    store: Optional[str] = None
    """
    (Future reference)
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](/docs/file-stores). If unset, the image data will be returned as a base64-encoded string.
    """


@dataclass
class FutureDetectSegmentsOut:
    """
    (Future reference)
    """

    mask_image_uri: str
    """
    (Future reference)
    Detected segments in 'mask image' format. Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """


@dataclass
class FutureTranscribeMediaIn:
    """
    (Future reference)
    """

    audio_uri: str
    """
    (Future reference)
    Input audio.
    """
    prompt: Optional[str] = None
    """
    (Future reference)
    Prompt to guide model on the content and context of input audio.
    """
    language: Optional[str] = "en"
    """
    (Future reference)
    Language of input audio in [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes) format.
    """
    segment: Optional[bool] = False
    """
    (Future reference)
    Segment the text into sentences with approximate timestamps.
    """
    align: Optional[bool] = False
    """
    (Future reference)
    Align transcription to produce more accurate sentence-level timestamps and word-level timestamps. An array of word segments will be included in each sentence segment.
    """
    diarize: Optional[bool] = False
    """
    (Future reference)
    Identify speakers for each segment. Speaker IDs will be included in each segment.
    """
    suggest_chapters: Optional[bool] = False
    """
    (Future reference)
    Suggest automatic chapter markers.
    """


@dataclass
class TranscribedWord:
    """
    (Future reference)
    """

    word: str
    """
    (Future reference)
    Text of word.
    """
    start: Optional[float] = None
    """
    (Future reference)
    Start time of word, in seconds.
    """
    end: Optional[float] = None
    """
    (Future reference)
    End time of word, in seconds.
    """
    speaker: Optional[str] = None
    """
    (Future reference)
    ID of speaker, if `diarize` is enabled.
    """


@dataclass
class TranscribedSegment:
    """
    (Future reference)
    """

    text: str
    """
    (Future reference)
    Text of segment.
    """
    start: float
    """
    (Future reference)
    Start time of segment, in seconds.
    """
    end: float
    """
    (Future reference)
    End time of segment, in seconds.
    """
    speaker: Optional[str] = None
    """
    (Future reference)
    ID of speaker, if `diarize` is enabled.
    """
    words: Optional[List[TranscribedWord]] = None
    """
    (Future reference)
    Aligned words, if `align` is enabled.
    """


@dataclass
class ChapterMarker:
    """
    (Future reference)
    """

    title: str
    """
    (Future reference)
    Chapter title.
    """
    start: float
    """
    (Future reference)
    Start time of chapter, in seconds.
    """


@dataclass
class FutureTranscribeMediaOut:
    """
    (Future reference)
    """

    text: str
    """
    (Future reference)
    Transcribed text.
    """
    segments: Optional[List[TranscribedSegment]] = None
    """
    (Future reference)
    Transcribed segments, if `segment` is enabled.
    """
    chapters: Optional[List[ChapterMarker]] = None
    """
    (Future reference)
    Chapter markers, if `suggest_chapters` is enabled.
    """


@dataclass
class FutureGenerateSpeechIn:
    """
    (Future reference)
    """

    text: str
    """
    (Future reference)
    Input text.
    """
    audio_uri: Optional[str] = None
    """
    (Future reference)
    Reference audio used to synthesize the speaker. If unset, a default speaker voice will be used.
    """
    language: Optional[str] = "en"
    """
    (Future reference)
    Language of input text. Supported languages: `en, de, fr, es, it, pt, pl, zh, ar, cs, ru, nl, tr, hu, ko`.
    """
    store: Optional[str] = None
    """
    (Future reference)
    Use "hosted" to return an audio URL hosted on Substrate. You can also provide a URL to a registered [file store](/docs/file-stores). If unset, the audio data will be returned as a base64-encoded string.
    """


@dataclass
class FutureGenerateSpeechOut:
    """
    (Future reference)
    """

    audio_uri: str
    """
    (Future reference)
    Base 64-encoded WAV audio bytes, or a hosted audio url if `store` is provided.
    """


@dataclass
class Embedding:
    """
    (Future reference)
    """

    vector: List[float]
    """
    (Future reference)
    Embedding vector.
    """
    doc_id: Optional[str] = None
    """
    (Future reference)
    Vector store document ID.
    """
    metadata: Optional[Dict[str, Any]] = None
    """
    (Future reference)
    Vector store document metadata.
    """


@dataclass
class FutureEmbedTextIn:
    """
    (Future reference)
    """

    text: str
    """
    (Future reference)
    Text to embed.
    """
    store: Optional[str] = None
    """
    (Future reference)
    [Vector store](/docs/vector-stores) identifier.
    """
    metadata: Optional[Dict[str, Any]] = None
    """
    (Future reference)
    Metadata that can be used to query the vector store. Ignored if `store` is unset.
    """
    embedded_metadata_keys: Optional[List[str]] = None
    """
    (Future reference)
    Choose keys from `metadata` to embed with text.
    """
    doc_id: Optional[str] = None
    """
    (Future reference)
    Vector store document ID. Ignored if `store` is unset.
    """
    node: Optional[Literal["JinaV2", "CLIP"]] = "JinaV2"
    """
    (Future reference)
    Selected node.
    """


@dataclass
class FutureEmbedTextOut:
    """
    (Future reference)
    """

    embedding: Embedding
    """
    (Future reference)
    Generated embedding.
    """


@dataclass
class EmbedTextItem:
    """
    (Future reference)
    """

    text: str
    """
    (Future reference)
    Text to embed.
    """
    metadata: Optional[Dict[str, Any]] = None
    """
    (Future reference)
    Metadata that can be used to query the vector store. Ignored if `store` is unset.
    """
    doc_id: Optional[str] = None
    """
    (Future reference)
    Vector store document ID. Ignored if `store` is unset.
    """


@dataclass
class FutureMultiEmbedTextIn:
    """
    (Future reference)
    """

    items: List[EmbedTextItem]
    """
    (Future reference)
    Items to embed.
    """
    store: Optional[str] = None
    """
    (Future reference)
    [Vector store](/docs/vector-stores) identifier.
    """
    embedded_metadata_keys: Optional[List[str]] = None
    """
    (Future reference)
    Choose keys from `metadata` to embed with text.
    """
    node: Optional[Literal["JinaV2", "CLIP"]] = "JinaV2"
    """
    (Future reference)
    Selected node.
    """


@dataclass
class FutureMultiEmbedTextOut:
    """
    (Future reference)
    """

    embeddings: List[Embedding]
    """
    (Future reference)
    Generated embeddings.
    """


@dataclass
class FutureJinaV2In:
    """
    (Future reference)
    """

    items: List[EmbedTextItem]
    """
    (Future reference)
    Items to embed.
    """
    store: Optional[str] = None
    """
    (Future reference)
    [Vector store](/docs/vector-stores) identifier.
    """
    embedded_metadata_keys: Optional[List[str]] = None
    """
    (Future reference)
    Choose keys from `metadata` to embed with text.
    """


@dataclass
class FutureJinaV2Out:
    """
    (Future reference)
    """

    embeddings: List[Embedding]
    """
    (Future reference)
    Generated embeddings.
    """


@dataclass
class FutureEmbedImageIn:
    """
    (Future reference)
    """

    image_uri: str
    """
    (Future reference)
    Image to embed.
    """
    store: Optional[str] = None
    """
    (Future reference)
    [Vector store](/docs/vector-stores) identifier.
    """
    doc_id: Optional[str] = None
    """
    (Future reference)
    Vector store document ID. Ignored if `store` is unset.
    """
    node: Optional[Literal["CLIP"]] = "CLIP"
    """
    (Future reference)
    Selected node.
    """


@dataclass
class FutureEmbedImageOut:
    """
    (Future reference)
    """

    embedding: Embedding
    """
    (Future reference)
    Generated embedding.
    """


@dataclass
class EmbedImageItem:
    """
    (Future reference)
    """

    image_uri: str
    """
    (Future reference)
    Image to embed.
    """
    doc_id: Optional[str] = None
    """
    (Future reference)
    Vector store document ID. Ignored if `store` is unset.
    """


@dataclass
class EmbedTextOrImageItem:
    """
    (Future reference)
    """

    image_uri: Optional[str] = None
    """
    (Future reference)
    Image to embed.
    """
    text: Optional[str] = None
    """
    (Future reference)
    Text to embed.
    """
    metadata: Optional[Dict[str, Any]] = None
    """
    (Future reference)
    Metadata that can be used to query the vector store. Ignored if `store` is unset.
    """
    doc_id: Optional[str] = None
    """
    (Future reference)
    Vector store document ID. Ignored if `store` is unset.
    """


@dataclass
class FutureMultiEmbedImageIn:
    """
    (Future reference)
    """

    items: List[EmbedImageItem]
    """
    (Future reference)
    Items to embed.
    """
    store: Optional[str] = None
    """
    (Future reference)
    [Vector store](/docs/vector-stores) identifier.
    """
    node: Optional[Literal["CLIP"]] = "CLIP"
    """
    (Future reference)
    Selected node.
    """


@dataclass
class FutureMultiEmbedImageOut:
    """
    (Future reference)
    """

    embeddings: List[Embedding]
    """
    (Future reference)
    Generated embeddings.
    """


@dataclass
class FutureCLIPIn:
    """
    (Future reference)
    """

    items: List[EmbedTextOrImageItem]
    """
    (Future reference)
    Items to embed.
    """
    embedded_metadata_keys: Optional[List[str]] = None
    """
    (Future reference)
    Choose keys from `metadata` to embed with text, when embedding and storing text documents.
    """
    store: Optional[str] = None
    """
    (Future reference)
    [Vector store](/docs/vector-stores) identifier.
    """


@dataclass
class FutureCLIPOut:
    """
    (Future reference)
    """

    embeddings: List[Embedding]
    """
    (Future reference)
    Generated embeddings.
    """


@dataclass
class VectorStoreParams:
    """
    (Future reference)
    """

    name: str
    """
    (Future reference)
    Vector store name.
    """
    model: Literal["jina-v2", "clip"]
    """
    (Future reference)
    Selected embedding model
    """
    m: Optional[int] = 16
    """
    (Future reference)
    The max number of connections per layer for the index.
    """
    ef_construction: Optional[int] = 64
    """
    (Future reference)
    The size of the dynamic candidate list for constructing the index graph.
    """
    metric: Optional[Literal["cosine", "l2", "inner"]] = "inner"
    """
    (Future reference)
    The distance metric to construct the index with.
    """


@dataclass
class DeleteVectorStoreParams:
    """
    (Future reference)
    """

    name: str
    """
    (Future reference)
    Vector store name.
    """
    model: Literal["jina-v2", "clip"]
    """
    (Future reference)
    Selected embedding model
    """


@dataclass
class Vector:
    """
    (Future reference)
    Canonical representation of document with embedding vector.
    """

    id: str
    """
    (Future reference)
    Document ID.
    """
    vector: List[float]
    """
    (Future reference)
    Embedding vector.
    """
    metadata: Dict[str, Any]
    """
    (Future reference)
    Document metadata.
    """


@dataclass
class GetVectorsParams:
    """
    (Future reference)
    """

    name: str
    """
    (Future reference)
    Vector store name.
    """
    model: Literal["jina-v2", "clip"]
    """
    (Future reference)
    Selected embedding model
    """
    ids: List[str]
    """
    (Future reference)
    Document IDs to retrieve.
    """


@dataclass
class GetVectorsResponse:
    """
    (Future reference)
    """

    vectors: List[Vector]
    """
    (Future reference)
    Retrieved vectors.
    """


@dataclass
class VectorUpdateCountResponse:
    """
    (Future reference)
    """

    count: int
    """
    (Future reference)
    Number of vectors modified.
    """


@dataclass
class UpdateVectorParams:
    """
    (Future reference)
    Document to update.
    """

    id: str
    """
    (Future reference)
    Document ID.
    """
    vector: Optional[List[float]] = None
    """
    (Future reference)
    Embedding vector.
    """
    metadata: Optional[Dict[str, Any]] = None
    """
    (Future reference)
    Document metadata.
    """


@dataclass
class UpdateVectorsParams:
    """
    (Future reference)
    """

    name: str
    """
    (Future reference)
    Vector store name.
    """
    model: Literal["jina-v2", "clip"]
    """
    (Future reference)
    Selected embedding model
    """
    vectors: List[UpdateVectorParams]
    """
    (Future reference)
    Vectors to upsert.
    """


@dataclass
class DeleteVectorsParams:
    """
    (Future reference)
    """

    name: str
    """
    (Future reference)
    Vector store name.
    """
    model: Literal["jina-v2", "clip"]
    """
    (Future reference)
    Selected embedding model
    """
    ids: List[str]
    """
    (Future reference)
    Document IDs to delete.
    """


@dataclass
class QueryVectorStoreParams:
    """
    (Future reference)
    """

    name: str
    """
    (Future reference)
    Vector store to query against.
    """
    model: Literal["jina-v2", "clip"]
    """
    (Future reference)
    Selected embedding model
    """
    query_ids: Optional[List[str]] = None
    """
    (Future reference)
    Document IDs to use for the query.
    """
    query_image_uris: Optional[List[str]] = None
    """
    (Future reference)
    Image URIs to embed and use for the query.
    """
    query_vectors: Optional[List[List[float]]] = None
    """
    (Future reference)
    Vector to use for the query.
    """
    query_strings: Optional[List[str]] = None
    """
    (Future reference)
    Texts to embed and use for the query.
    """
    top_k: Optional[int] = 10
    """
    (Future reference)
    Number of results to return.
    """
    ef_search: Optional[int] = 40
    """
    (Future reference)
    The size of the dynamic candidate list for searching the index graph.
    """
    include_values: Optional[bool] = False
    """
    (Future reference)
    Include the values of the vectors in the response.
    """
    include_metadata: Optional[bool] = False
    """
    (Future reference)
    Include the metadata of the vectors in the response.
    """
    filters: Optional[Dict[str, Any]] = None
    """
    (Future reference)
    Filter metadata by key-value pairs.
    """


@dataclass
class VectorStoreQueryResult:
    """
    (Future reference)
    """

    id: str
    """
    (Future reference)
    Document ID.
    """
    distance: float
    """
    (Future reference)
    Similarity score.
    """
    vector: Optional[List[float]] = None
    """
    (Future reference)
    Embedding vector.
    """
    metadata: Optional[Dict[str, Any]] = None
    """
    (Future reference)
    Document metadata.
    """


@dataclass
class QueryVectorStoreResponse:
    """
    (Future reference)
    """

    results: List[List[VectorStoreQueryResult]]
    """
    (Future reference)
    Query results.
    """
    name: Optional[str] = None
    """
    (Future reference)
    Vector store name.
    """
    model: Optional[Literal["jina-v2", "clip"]] = None
    """
    (Future reference)
    Selected embedding model
    """
    metric: Optional[Literal["cosine", "l2", "inner"]] = None
    """
    (Future reference)
    The distance metric used for the query.
    """
