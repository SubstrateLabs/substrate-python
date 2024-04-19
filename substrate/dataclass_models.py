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
    type: Literal["api_error", "invalid_request_error"]
    """
    The type of error returned.
    """
    message: str
    """
    A message providing more details about the error.
    """
    request_id: Optional[str] = None
    """
    A unique identifier for the request.
    """


@dataclass
class GenerateTextIn:
    prompt: str
    """
    Input prompt.
    """
    temperature: float = 0.4
    """
    Sampling temperature to use. Higher values make the output more random, lower values make the output more deterministic.
    """
    max_tokens: Optional[int] = None
    """
    Maximum number of tokens to generate.
    """
    node: Literal["Mistral7BInstruct"] = "Mistral7BInstruct"
    """
    Selected node.
    """


@dataclass
class GenerateTextOut:
    text: str
    """
    Text response.
    """


@dataclass
class GenerateJSONIn:
    prompt: str
    """
    Input prompt.
    """
    json_schema: Dict[str, Any]
    """
    JSON schema to guide `json_object` response.
    """
    temperature: float = 0.4
    """
    Sampling temperature to use. Higher values make the output more random, lower values make the output more deterministic.
    """
    max_tokens: Optional[int] = None
    """
    Maximum number of tokens to generate.
    """
    node: Literal["Mistral7BInstruct"] = "Mistral7BInstruct"
    """
    Selected node.
    """


@dataclass
class GenerateJSONOut:
    json_object: Dict[str, Any]
    """
    JSON response.
    """


@dataclass
class MultiGenerateTextIn:
    prompt: Optional[str] = None
    """
    Input prompt.
    """
    batch_prompts: Optional[List[str]] = None
    """
    Batch input prompts.
    """
    num_choices: int = 1
    """
    Number of choices to generate.
    """
    temperature: float = 0.4
    """
    Sampling temperature to use. Higher values make the output more random, lower values make the output more deterministic.
    """
    max_tokens: Optional[int] = None
    """
    Maximum number of tokens to generate.
    """
    node: Literal["Mistral7BInstruct"] = "Mistral7BInstruct"
    """
    Selected node.
    """


@dataclass
class MultiGenerateTextOutput:
    choices: List[GenerateTextOut]
    """
    Response choices.
    """


@dataclass
class MultiGenerateTextOut:
    outputs: List[MultiGenerateTextOutput]
    """
    A single output for `prompt`, or multiple outputs for `batch_prompts`.
    """


@dataclass
class MultiGenerateJSONIn:
    json_schema: Dict[str, Any]
    """
    JSON schema to guide `json_object` response.
    """
    prompt: Optional[str] = None
    """
    Input prompt.
    """
    batch_prompts: Optional[List[str]] = None
    """
    Batch input prompts.
    """
    num_choices: int = 2
    """
    Number of choices to generate.
    """
    temperature: float = 0.4
    """
    Sampling temperature to use. Higher values make the output more random, lower values make the output more deterministic.
    """
    max_tokens: Optional[int] = None
    """
    Maximum number of tokens to generate.
    """
    node: Literal["Mistral7BInstruct"] = "Mistral7BInstruct"
    """
    Selected node.
    """


@dataclass
class MultiGenerateJSONOutput:
    choices: List[GenerateJSONOut]
    """
    Response choices.
    """


@dataclass
class MultiGenerateJSONOut:
    outputs: List[MultiGenerateJSONOutput]
    """
    A single output for `prompt`, or multiple outputs for `batch_prompts`.
    """


@dataclass
class Mistral7BInstructIn:
    prompt: Optional[str] = None
    """
    Input prompt.
    """
    num_choices: int = 1
    """
    Number of choices to generate.
    """
    json_schema: Optional[Dict[str, Any]] = None
    """
    JSON schema to guide response.
    """
    batch_prompts: Optional[List[str]] = None
    """
    Batch input prompts.
    """
    temperature: Optional[float] = None
    """
    Sampling temperature to use. Higher values make the output more random, lower values make the output more deterministic.
    """
    max_tokens: Optional[int] = None
    """
    Maximum number of tokens to generate.
    """


@dataclass
class Mistral7BInstructChoice:
    text: Optional[str] = None
    """
    Text response, if `json_schema` was not provided.
    """
    json_object: Optional[Dict[str, Any]] = None
    """
    JSON response, if `json_schema` was provided.
    """


@dataclass
class Mistral7BInstructOutput:
    choices: List[Mistral7BInstructChoice]
    """
    Response choices.
    """


@dataclass
class Mistral7BInstructOut:
    outputs: List[Mistral7BInstructOutput]
    """
    A single output for `prompt`, or multiple outputs for `batch_prompts`.
    """


@dataclass
class GenerateTextVisionIn:
    prompt: str
    """
    Text prompt.
    """
    image_uris: List[str]
    """
    Image prompts.
    """
    max_tokens: int = 800
    """
    Maximum number of tokens to generate.
    """
    node: Literal["Firellava13B"] = "Firellava13B"
    """
    Selected node.
    """


@dataclass
class GenerateTextVisionOut:
    text: str
    """
    Text response.
    """


@dataclass
class Firellava13BIn:
    prompt: str
    """
    Text prompt.
    """
    image_uris: List[str]
    """
    Image prompts.
    """
    max_tokens: int = 800
    """
    Maximum number of tokens to generate.
    """


@dataclass
class Firellava13BOut:
    text: str
    """
    Text response.
    """


@dataclass
class GenerateImageIn:
    prompt: str
    """
    Text prompt.
    """
    store: Optional[str] = None
    """
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](/docs/file-stores). If unset, the image data will be returned as a base64-encoded string.
    """
    node: Literal["StableDiffusionXL"] = "StableDiffusionXL"
    """
    Selected node.
    """


@dataclass
class GenerateImageOut:
    image_uri: str
    """
    Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """


@dataclass
class MultiGenerateImageIn:
    prompt: str
    """
    Text prompt.
    """
    num_images: int
    """
    Number of images to generate.
    """
    store: Optional[str] = None
    """
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](/docs/file-stores). If unset, the image data will be returned as a base64-encoded string.
    """
    node: Literal["StableDiffusionXL"] = "StableDiffusionXL"
    """
    Selected node.
    """


@dataclass
class MultiGenerateImageOut:
    outputs: List[GenerateImageOut]
    """
    Generated images.
    """


@dataclass
class StableDiffusionXLIn:
    prompt: str
    """
    Text prompt.
    """
    num_images: int
    """
    Number of images to generate.
    """
    negative_prompt: Optional[str] = None
    """
    Negative input prompt.
    """
    steps: int = 30
    """
    Number of diffusion steps.
    """
    store: Optional[str] = None
    """
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](/docs/file-stores). If unset, the image data will be returned as a base64-encoded string.
    """
    height: int = 1024
    """
    Height of output image, in pixels.
    """
    width: int = 1024
    """
    Width of output image, in pixels.
    """
    seeds: Optional[List[int]] = None
    """
    Seeds for deterministic generation. Default is a random seed.
    """
    guidance_scale: float = 7
    """
    Higher values adhere to the text prompt more strongly, typically at the expense of image quality.
    """


@dataclass
class StableDiffusionImage:
    image_uri: str
    """
    Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """
    seed: int
    """
    The random noise seed used for generation.
    """


@dataclass
class StableDiffusionXLOut:
    outputs: List[StableDiffusionImage]
    """
    Generated images.
    """


@dataclass
class StableDiffusionXLLightningIn:
    prompt: str
    """
    Text prompt.
    """
    negative_prompt: Optional[str] = None
    """
    Negative input prompt.
    """
    num_images: int = 1
    """
    Number of images to generate.
    """
    store: Optional[str] = None
    """
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](/docs/file-stores). If unset, the image data will be returned as a base64-encoded string.
    """
    height: int = 1024
    """
    Height of output image, in pixels.
    """
    width: int = 1024
    """
    Width of output image, in pixels.
    """
    seeds: Optional[List[int]] = None
    """
    Seeds for deterministic generation. Default is a random seed.
    """


@dataclass
class StableDiffusionXLLightningOut:
    outputs: List[StableDiffusionImage]
    """
    Generated images.
    """


@dataclass
class StableDiffusionXLIPAdapterIn:
    prompt: str
    """
    Text prompt.
    """
    num_images: int
    """
    Number of images to generate.
    """
    image_prompt_uri: Optional[str] = None
    """
    Image prompt.
    """
    ip_adapter_scale: float = 0.5
    """
    Controls the influence of the image prompt on the generated output.
    """
    negative_prompt: Optional[str] = None
    """
    Negative input prompt.
    """
    store: Optional[str] = None
    """
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](/docs/file-stores). If unset, the image data will be returned as a base64-encoded string.
    """
    width: int = 1024
    """
    Width of output image, in pixels.
    """
    height: int = 1024
    """
    Height of output image, in pixels.
    """
    seeds: Optional[List[int]] = None
    """
    Random noise seeds. Default is random seeds for each generation.
    """


@dataclass
class StableDiffusionXLIPAdapterOut:
    outputs: List[StableDiffusionImage]
    """
    Generated images.
    """


@dataclass
class StableDiffusionXLControlNetIn:
    image_uri: str
    """
    Input image.
    """
    control_method: Literal["edge", "depth", "illusion"]
    """
    Strategy to control generation using the input image.
    """
    prompt: str
    """
    Text prompt.
    """
    num_images: int
    """
    Number of images to generate.
    """
    output_resolution: int = 1024
    """
    Resolution of the output image, in pixels.
    """
    negative_prompt: Optional[str] = None
    """
    Negative input prompt.
    """
    store: Optional[str] = None
    """
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](/docs/file-stores). If unset, the image data will be returned as a base64-encoded string.
    """
    conditioning_scale: float = 0.5
    """
    Controls the influence of the input image on the generated output.
    """
    seeds: Optional[List[int]] = None
    """
    Random noise seeds. Default is random seeds for each generation.
    """


@dataclass
class StableDiffusionXLControlNetOut:
    outputs: List[StableDiffusionImage]
    """
    Generated images.
    """


@dataclass
class GenerativeEditImageIn:
    image_uri: str
    """
    Original image.
    """
    prompt: str
    """
    Text prompt.
    """
    mask_image_uri: Optional[str] = None
    """
    Mask image that controls which pixels are inpainted. If unset, the entire image is edited (image-to-image).
    """
    store: Optional[str] = None
    """
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](/docs/file-stores). If unset, the image data will be returned as a base64-encoded string.
    """
    node: Literal["StableDiffusionXLInpaint"] = "StableDiffusionXLInpaint"
    """
    Selected node.
    """


@dataclass
class GenerativeEditImageOut:
    image_uri: str
    """
    Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """


@dataclass
class MultiGenerativeEditImageIn:
    image_uri: str
    """
    Original image.
    """
    prompt: str
    """
    Text prompt.
    """
    num_images: int
    """
    Number of images to generate.
    """
    mask_image_uri: Optional[str] = None
    """
    Mask image that controls which pixels are edited (inpainting). If unset, the entire image is edited (image-to-image).
    """
    store: Optional[str] = None
    """
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](/docs/file-stores). If unset, the image data will be returned as a base64-encoded string.
    """
    node: Literal["StableDiffusionXLInpaint"] = "StableDiffusionXLInpaint"
    """
    Selected node.
    """


@dataclass
class MultiGenerativeEditImageOut:
    outputs: List[GenerativeEditImageOut]
    """
    Generated images.
    """


@dataclass
class StableDiffusionXLInpaintIn:
    image_uri: str
    """
    Original image.
    """
    prompt: str
    """
    Text prompt.
    """
    num_images: int
    """
    Number of images to generate.
    """
    mask_image_uri: Optional[str] = None
    """
    Mask image that controls which pixels are edited (inpainting). If unset, the entire image is edited (image-to-image).
    """
    output_resolution: int = 1024
    """
    Resolution of the output image, in pixels.
    """
    negative_prompt: Optional[str] = None
    """
    Negative input prompt.
    """
    store: Optional[str] = None
    """
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](/docs/file-stores). If unset, the image data will be returned as a base64-encoded string.
    """
    strength: float = 0.8
    """
    Controls the strength of the generation process.
    """
    seeds: Optional[List[int]] = None
    """
    Random noise seeds. Default is random seeds for each generation.
    """


@dataclass
class StableDiffusionXLInpaintOut:
    outputs: List[StableDiffusionImage]
    """
    Generated images.
    """


@dataclass
class BoundingBox:
    x1: float
    """
    Top left corner x.
    """
    y1: float
    """
    Top left corner y.
    """
    x2: float
    """
    Bottom right corner x.
    """
    y2: float
    """
    Bottom right corner y.
    """


@dataclass
class Point:
    x: int
    """
    X position.
    """
    y: int
    """
    Y position.
    """


@dataclass
class FillMaskIn:
    image_uri: str
    """
    Input image.
    """
    mask_image_uri: str
    """
    Mask image that controls which pixels are inpainted.
    """
    store: Optional[str] = None
    """
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](/docs/file-stores). If unset, the image data will be returned as a base64-encoded string.
    """
    node: Literal["BigLaMa"] = "BigLaMa"
    """
    Selected node.
    """


@dataclass
class FillMaskOut:
    image_uri: str
    """
    Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """


@dataclass
class BigLaMaIn:
    image_uri: str
    """
    Input image.
    """
    mask_image_uri: str
    """
    Mask image that controls which pixels are inpainted.
    """
    store: Optional[str] = None
    """
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](/docs/file-stores). If unset, the image data will be returned as a base64-encoded string.
    """


@dataclass
class BigLaMaOut:
    image_uri: str
    """
    Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """


@dataclass
class RemoveBackgroundIn:
    image_uri: str
    """
    Input image.
    """
    return_mask: bool = False
    """
    Return a mask image instead of the original content.
    """
    background_color: Optional[str] = None
    """
    Hex value background color. Transparent if unset.
    """
    store: Optional[str] = None
    """
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](/docs/file-stores). If unset, the image data will be returned as a base64-encoded string.
    """
    node: Literal["DISISNet"] = "DISISNet"
    """
    Selected node.
    """


@dataclass
class RemoveBackgroundOut:
    image_uri: str
    """
    Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """


@dataclass
class DISISNetIn:
    image_uri: str
    """
    Input image.
    """
    store: Optional[str] = None
    """
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](/docs/file-stores). If unset, the image data will be returned as a base64-encoded string.
    """


@dataclass
class DISISNetOut:
    image_uri: str
    """
    Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """


@dataclass
class UpscaleImageIn:
    image_uri: str
    """
    Input image.
    """
    store: Optional[str] = None
    """
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](/docs/file-stores). If unset, the image data will be returned as a base64-encoded string.
    """
    node: Literal["RealESRGAN"] = "RealESRGAN"
    """
    Selected node.
    """


@dataclass
class UpscaleImageOut:
    image_uri: str
    """
    Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """


@dataclass
class RealESRGANIn:
    image_uri: str
    """
    Input image.
    """
    store: Optional[str] = None
    """
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](/docs/file-stores). If unset, the image data will be returned as a base64-encoded string.
    """


@dataclass
class RealESRGANOut:
    image_uri: str
    """
    Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """


@dataclass
class SegmentUnderPointIn:
    image_uri: str
    """
    Input image.
    """
    point: Point
    """
    Point prompt.
    """
    store: Optional[str] = None
    """
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](/docs/file-stores). If unset, the image data will be returned as a base64-encoded string.
    """
    node: Literal["SegmentAnything"] = "SegmentAnything"
    """
    Selected node.
    """


@dataclass
class SegmentUnderPointOut:
    mask_image_uri: str
    """
    Detected segments in 'mask image' format. Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """


@dataclass
class SegmentAnythingIn:
    image_uri: str
    """
    Input image.
    """
    point_prompts: Optional[List[Point]] = None
    """
    Point prompts, to detect a segment under the point. One of `point_prompts` or `box_prompts` must be set.
    """
    box_prompts: Optional[List[BoundingBox]] = None
    """
    Box prompts, to detect a segment within the bounding box. One of `point_prompts` or `box_prompts` must be set.
    """
    store: Optional[str] = None
    """
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](/docs/file-stores). If unset, the image data will be returned as a base64-encoded string.
    """


@dataclass
class SegmentAnythingOut:
    mask_image_uri: str
    """
    Detected segments in 'mask image' format. Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """


@dataclass
class TranscribeMediaIn:
    audio_uri: str
    """
    Input audio.
    """
    prompt: Optional[str] = None
    """
    Prompt to guide model on the content and context of input audio.
    """
    language: str = "en"
    """
    Language of input audio in [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes) format.
    """
    segment: bool = False
    """
    Segment the text into sentences with approximate timestamps.
    """
    align: bool = False
    """
    Align transcription to produce more accurate sentence-level timestamps and word-level timestamps. An array of word segments will be included in each sentence segment.
    """
    diarize: bool = False
    """
    Identify speakers for each segment. Speaker IDs will be included in each segment.
    """
    suggest_chapters: bool = False
    """
    Suggest automatic chapter markers.
    """


@dataclass
class TranscribedWord:
    word: str
    """
    Text of word.
    """
    start: Optional[float] = None
    """
    Start time of word, in seconds.
    """
    end: Optional[float] = None
    """
    End time of word, in seconds.
    """
    speaker: Optional[str] = None
    """
    ID of speaker, if `diarize` is enabled.
    """


@dataclass
class TranscribedSegment:
    text: str
    """
    Text of segment.
    """
    start: float
    """
    Start time of segment, in seconds.
    """
    end: float
    """
    End time of segment, in seconds.
    """
    speaker: Optional[str] = None
    """
    ID of speaker, if `diarize` is enabled.
    """
    words: Optional[List[TranscribedWord]] = None
    """
    Aligned words, if `align` is enabled.
    """


@dataclass
class ChapterMarker:
    title: str
    """
    Chapter title.
    """
    start: float
    """
    Start time of chapter, in seconds.
    """


@dataclass
class TranscribeMediaOut:
    text: str
    """
    Transcribed text.
    """
    segments: Optional[List[TranscribedSegment]] = None
    """
    Transcribed segments, if `segment` is enabled.
    """
    chapters: Optional[List[ChapterMarker]] = None
    """
    Chapter markers, if `suggest_chapters` is enabled.
    """


@dataclass
class GenerateSpeechIn:
    text: str
    """
    Input text.
    """
    store: Optional[str] = None
    """
    Use "hosted" to return an audio URL hosted on Substrate. You can also provide a URL to a registered [file store](/docs/file-stores). If unset, the audio data will be returned as a base64-encoded string.
    """
    node: Literal["XTTSV2"] = "XTTSV2"
    """
    Selected node.
    """


@dataclass
class GenerateSpeechOut:
    audio_uri: str
    """
    Base 64-encoded WAV audio bytes, or a hosted audio url if `store` is provided.
    """


@dataclass
class XTTSV2In:
    text: str
    """
    Input text.
    """
    audio_uri: Optional[str] = None
    """
    Reference audio used to synthesize the speaker. If unset, a default speaker voice will be used.
    """
    language: str = "en"
    """
    Language of input text. Supported languages: `en, de, fr, es, it, pt, pl, zh, ar, cs, ru, nl, tr, hu, ko`.
    """
    store: Optional[str] = None
    """
    Use "hosted" to return an audio URL hosted on Substrate. You can also provide a URL to a registered [file store](/docs/file-stores). If unset, the audio data will be returned as a base64-encoded string.
    """


@dataclass
class XTTSV2Out:
    audio_uri: str
    """
    Base 64-encoded WAV audio bytes, or a hosted audio url if `store` is provided.
    """


@dataclass
class Embedding:
    vector: List[float]
    """
    Embedding vector.
    """
    doc_id: Optional[str] = None
    """
    Vector store document ID.
    """
    metadata: Optional[Dict[str, Any]] = None
    """
    Vector store document metadata.
    """


@dataclass
class EmbedTextIn:
    text: str
    """
    Text to embed.
    """
    store: Optional[str] = None
    """
    [Vector store](/docs/vector-stores) identifier.
    """
    metadata: Optional[Dict[str, Any]] = None
    """
    Metadata that can be used to query the vector store. Ignored if `store` is unset.
    """
    embedded_metadata_keys: Optional[List[str]] = None
    """
    Choose keys from `metadata` to embed with text.
    """
    doc_id: Optional[str] = None
    """
    Vector store document ID. Ignored if `store` is unset.
    """
    node: Literal["JinaV2", "CLIP"] = "JinaV2"
    """
    Selected node.
    """


@dataclass
class EmbedTextOut:
    embedding: Embedding
    """
    Generated embedding.
    """


@dataclass
class EmbedTextItem:
    text: str
    """
    Text to embed.
    """
    metadata: Optional[Dict[str, Any]] = None
    """
    Metadata that can be used to query the vector store. Ignored if `store` is unset.
    """
    doc_id: Optional[str] = None
    """
    Vector store document ID. Ignored if `store` is unset.
    """


@dataclass
class MultiEmbedTextIn:
    items: List[EmbedTextItem]
    """
    Items to embed.
    """
    store: Optional[str] = None
    """
    [Vector store](/docs/vector-stores) identifier.
    """
    embedded_metadata_keys: Optional[List[str]] = None
    """
    Choose keys from `metadata` to embed with text.
    """
    node: Literal["JinaV2", "CLIP"] = "JinaV2"
    """
    Selected node.
    """


@dataclass
class MultiEmbedTextOut:
    embeddings: List[Embedding]
    """
    Generated embeddings.
    """


@dataclass
class JinaV2In:
    items: List[EmbedTextItem]
    """
    Items to embed.
    """
    store: Optional[str] = None
    """
    [Vector store](/docs/vector-stores) identifier.
    """
    embedded_metadata_keys: Optional[List[str]] = None
    """
    Choose keys from `metadata` to embed with text.
    """


@dataclass
class JinaV2Out:
    embeddings: List[Embedding]
    """
    Generated embeddings.
    """


@dataclass
class EmbedImageIn:
    image_uri: str
    """
    Image to embed.
    """
    store: Optional[str] = None
    """
    [Vector store](/docs/vector-stores) identifier.
    """
    doc_id: Optional[str] = None
    """
    Vector store document ID. Ignored if `store` is unset.
    """
    node: Literal["CLIP"] = "CLIP"
    """
    Selected node.
    """


@dataclass
class EmbedImageOut:
    embedding: Embedding
    """
    Generated embedding.
    """


@dataclass
class EmbedImageItem:
    image_uri: str
    """
    Image to embed.
    """
    doc_id: Optional[str] = None
    """
    Vector store document ID. Ignored if `store` is unset.
    """


@dataclass
class EmbedTextOrImageItem:
    image_uri: Optional[str] = None
    """
    Image to embed.
    """
    text: Optional[str] = None
    """
    Text to embed.
    """
    metadata: Optional[Dict[str, Any]] = None
    """
    Metadata that can be used to query the vector store. Ignored if `store` is unset.
    """
    doc_id: Optional[str] = None
    """
    Vector store document ID. Ignored if `store` is unset.
    """


@dataclass
class MultiEmbedImageIn:
    items: List[EmbedImageItem]
    """
    Items to embed.
    """
    store: Optional[str] = None
    """
    [Vector store](/docs/vector-stores) identifier.
    """
    node: Literal["CLIP"] = "CLIP"
    """
    Selected node.
    """


@dataclass
class MultiEmbedImageOut:
    embeddings: List[Embedding]
    """
    Generated embeddings.
    """


@dataclass
class CLIPIn:
    items: List[EmbedTextOrImageItem]
    """
    Items to embed.
    """
    store: Optional[str] = None
    """
    [Vector store](/docs/vector-stores) identifier.
    """


@dataclass
class CLIPOut:
    embeddings: List[Embedding]
    """
    Generated embeddings.
    """


@dataclass
class CreateVectorStoreIn:
    name: str
    """
    Vector store name.
    """
    model: Literal["jina-v2", "clip"]
    """
    Selected embedding model.
    """
    m: int = 16
    """
    The max number of connections per layer for the index.
    """
    ef_construction: int = 64
    """
    The size of the dynamic candidate list for constructing the index graph.
    """
    metric: Literal["cosine", "l2", "inner"] = "inner"
    """
    The distance metric to construct the index with.
    """


@dataclass
class CreateVectorStoreOut:
    name: str
    """
    Vector store name.
    """
    model: Literal["jina-v2", "clip"]
    """
    Selected embedding model.
    """
    m: int
    """
    The max number of connections per layer for the index.
    """
    ef_construction: int
    """
    The size of the dynamic candidate list for constructing the index graph.
    """
    metric: Literal["cosine", "l2", "inner"]
    """
    The distance metric to construct the index with.
    """


@dataclass
class ListVectorStoresIn:
    pass


@dataclass
class ListVectorStoresOut:
    stores: Optional[List[CreateVectorStoreOut]] = None
    """
    List of vector stores.
    """


@dataclass
class DeleteVectorStoreIn:
    name: str
    """
    Vector store name.
    """
    model: Literal["jina-v2", "clip"]
    """
    Selected embedding model.
    """


@dataclass
class DeleteVectorStoreOut:
    name: str
    """
    Vector store name.
    """
    model: Literal["jina-v2", "clip"]
    """
    Selected embedding model.
    """


@dataclass
class Vector:
    """
    Canonical representation of document with embedding vector.
    """

    id: str
    """
    Document ID.
    """
    vector: List[float]
    """
    Embedding vector.
    """
    metadata: Dict[str, Any]
    """
    Document metadata.
    """


@dataclass
class FetchVectorsIn:
    name: str
    """
    Vector store name.
    """
    model: Literal["jina-v2", "clip"]
    """
    Selected embedding model.
    """
    ids: List[str]
    """
    Document IDs to retrieve.
    """


@dataclass
class FetchVectorsOut:
    vectors: List[Vector]
    """
    Retrieved vectors.
    """


@dataclass
class UpdateVectorsOut:
    count: int
    """
    Number of vectors modified.
    """


@dataclass
class DeleteVectorsOut:
    count: int
    """
    Number of vectors modified.
    """


@dataclass
class UpdateVectorParams:
    id: str
    """
    Document ID.
    """
    vector: Optional[List[float]] = None
    """
    Embedding vector.
    """
    metadata: Optional[Dict[str, Any]] = None
    """
    Document metadata.
    """


@dataclass
class UpdateVectorsIn:
    name: str
    """
    Vector store name.
    """
    model: Literal["jina-v2", "clip"]
    """
    Selected embedding model.
    """
    vectors: List[UpdateVectorParams]
    """
    Vectors to upsert.
    """


@dataclass
class DeleteVectorsIn:
    name: str
    """
    Vector store name.
    """
    model: Literal["jina-v2", "clip"]
    """
    Selected embedding model.
    """
    ids: List[str]
    """
    Document IDs to delete.
    """


@dataclass
class QueryVectorStoreIn:
    name: str
    """
    Vector store to query against.
    """
    model: Literal["jina-v2", "clip"]
    """
    Selected embedding model.
    """
    query_strings: Optional[List[str]] = None
    """
    Texts to embed and use for the query.
    """
    query_image_uris: Optional[List[str]] = None
    """
    Image URIs to embed and use for the query.
    """
    query_vectors: Optional[List[List[float]]] = None
    """
    Vectors to use for the query.
    """
    query_ids: Optional[List[str]] = None
    """
    Document IDs to use for the query.
    """
    top_k: int = 10
    """
    Number of results to return.
    """
    ef_search: int = 40
    """
    The size of the dynamic candidate list for searching the index graph.
    """
    include_values: bool = False
    """
    Include the values of the vectors in the response.
    """
    include_metadata: bool = False
    """
    Include the metadata of the vectors in the response.
    """
    filters: Optional[Dict[str, Any]] = None
    """
    Filter metadata by key-value pairs.
    """
    metric: Optional[Literal["cosine", "l2", "inner"]] = None
    """
    The distance metric used for the query. Defaults to the distance metric the vector store was created with.
    """


@dataclass
class VectorStoreQueryResult:
    id: str
    """
    Document ID.
    """
    distance: float
    """
    Similarity score.
    """
    vector: Optional[List[float]] = None
    """
    Embedding vector.
    """
    metadata: Optional[Dict[str, Any]] = None
    """
    Document metadata.
    """


@dataclass
class QueryVectorStoreOut:
    results: List[List[VectorStoreQueryResult]]
    """
    Query results.
    """
    name: Optional[str] = None
    """
    Vector store name.
    """
    model: Optional[Literal["jina-v2", "clip"]] = None
    """
    Selected embedding model.
    """
    metric: Optional[Literal["cosine", "l2", "inner"]] = None
    """
    The distance metric used for the query.
    """
