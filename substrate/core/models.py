"""
꩜ Substrate
@generated file
(using datamodel-codegen)
"""


from __future__ import annotations

from typing import Any, Dict, List, Optional
from typing_extensions import Literal, Annotated

from pydantic import Extra, Field, BaseModel


class ErrorOut(BaseModel):
    class Config:
        extra = Extra.allow

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


class GenerateTextIn(BaseModel):
    class Config:
        extra = Extra.allow

    prompt: str
    """
    Input prompt.
    """
    temperature: Annotated[float, Field(ge=0.0, le=1.0)] = 0.4
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


class GenerateTextOut(BaseModel):
    class Config:
        extra = Extra.allow

    text: Optional[str] = None
    """
    Text response.
    """


class GenerateJSONIn(BaseModel):
    class Config:
        extra = Extra.allow

    prompt: str
    """
    Input prompt.
    """
    json_schema: Dict[str, Any]
    """
    JSON schema to guide `json_object` response.
    """
    temperature: Annotated[float, Field(ge=0.0, le=1.0)] = 0.4
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


class GenerateJSONOut(BaseModel):
    class Config:
        extra = Extra.allow

    json_object: Optional[Dict[str, Any]] = None
    """
    JSON response.
    """


class MultiGenerateTextIn(BaseModel):
    class Config:
        extra = Extra.allow

    prompt: str
    """
    Input prompt.
    """
    num_choices: Annotated[int, Field(ge=1)]
    """
    Number of choices to generate.
    """
    temperature: Annotated[float, Field(ge=0.0, le=1.0)] = 0.4
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


class MultiGenerateTextOut(BaseModel):
    class Config:
        extra = Extra.allow

    choices: List[GenerateTextOut]
    """
    Response choices.
    """


class MultiGenerateJSONIn(BaseModel):
    class Config:
        extra = Extra.allow

    prompt: str
    """
    Input prompt.
    """
    json_schema: Dict[str, Any]
    """
    JSON schema to guide `json_object` response.
    """
    num_choices: Annotated[int, Field(ge=1)]
    """
    Number of choices to generate.
    """
    temperature: Annotated[float, Field(ge=0.0, le=1.0)] = 0.4
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


class MultiGenerateJSONOut(BaseModel):
    class Config:
        extra = Extra.allow

    choices: List[GenerateJSONOut]
    """
    Response choices.
    """


class Mistral7BInstructIn(BaseModel):
    class Config:
        extra = Extra.allow

    prompt: str
    """
    Input prompt.
    """
    num_choices: int
    """
    Number of choices to generate.
    """
    json_schema: Optional[Dict[str, Any]] = None
    """
    JSON schema to guide response.
    """
    temperature: Annotated[Optional[float], Field(ge=0.0, le=1.0)] = None
    """
    Sampling temperature to use. Higher values make the output more random, lower values make the output more deterministic.
    """
    max_tokens: Optional[int] = None
    """
    Maximum number of tokens to generate.
    """


class Mistral7BInstructChoice(BaseModel):
    class Config:
        extra = Extra.allow

    text: Optional[str] = None
    """
    Text response, if `json_schema` was not provided.
    """
    json_object: Optional[Dict[str, Any]] = None
    """
    JSON response, if `json_schema` was provided.
    """


class Mistral7BInstructOut(BaseModel):
    class Config:
        extra = Extra.allow

    choices: List[Mistral7BInstructChoice]
    """
    Response choices.
    """


class GenerateTextVisionIn(BaseModel):
    class Config:
        extra = Extra.allow

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


class GenerateTextVisionOut(BaseModel):
    class Config:
        extra = Extra.allow

    text: str
    """
    Text response.
    """


class Firellava13BIn(BaseModel):
    class Config:
        extra = Extra.allow

    prompt: str
    """
    Text prompt.
    """
    image_uris: List[str]
    """
    Image prompts.
    """
    temperature: Annotated[Optional[float], Field(ge=0.0)] = None
    """
    Sampling temperature to use. Higher values make the output more random, lower values make the output more deterministic.
    """
    max_tokens: int = 800
    """
    Maximum number of tokens to generate.
    """


class Firellava13BOut(BaseModel):
    class Config:
        extra = Extra.allow

    text: str
    """
    Text response.
    """


class GenerateImageIn(BaseModel):
    class Config:
        extra = Extra.allow

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


class GenerateImageOut(BaseModel):
    class Config:
        extra = Extra.allow

    image_uri: str
    """
    Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """


class MultiGenerateImageIn(BaseModel):
    class Config:
        extra = Extra.allow

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


class MultiGenerateImageOut(BaseModel):
    class Config:
        extra = Extra.allow

    outputs: List[GenerateImageOut]
    """
    Generated images.
    """


class StableDiffusionXLIn(BaseModel):
    class Config:
        extra = Extra.allow

    prompt: str
    """
    Text prompt.
    """
    negative_prompt: Optional[str] = None
    """
    Negative input prompt.
    """
    steps: Optional[int] = None
    """
    Number of diffusion steps.
    """
    num_images: int
    """
    Number of images to generate.
    """
    store: Optional[str] = None
    """
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](/docs/file-stores). If unset, the image data will be returned as a base64-encoded string.
    """
    height: Optional[int] = None
    """
    Height of output image, in pixels.
    """
    width: Optional[int] = None
    """
    Width of output image, in pixels.
    """
    seeds: Optional[List[int]] = None
    """
    Seeds for deterministic generation. Default is a random seed.
    """
    guidance_scale: Annotated[float, Field(ge=0.0)] = 5
    """
    Higher values adhere to the text prompt more strongly, typically at the expense of image quality.
    """


class StableDiffusionImage(BaseModel):
    class Config:
        extra = Extra.allow

    image_uri: str
    """
    Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """
    seed: int
    """
    The random noise seed used for generation.
    """


class StableDiffusionXLOut(BaseModel):
    class Config:
        extra = Extra.allow

    outputs: List[StableDiffusionImage]
    """
    Generated images.
    """


class StableDiffusionXLLightningIn(BaseModel):
    class Config:
        extra = Extra.allow

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
    height: Optional[int] = None
    """
    Height of output image, in pixels.
    """
    width: Optional[int] = None
    """
    Width of output image, in pixels.
    """
    seeds: Optional[List[int]] = None
    """
    Seeds for deterministic generation. Default is a random seed.
    """


class StableDiffusionXLLightningOut(BaseModel):
    class Config:
        extra = Extra.allow

    outputs: List[StableDiffusionImage]
    """
    Generated images.
    """


class StableDiffusionXLIPAdapterIn(BaseModel):
    class Config:
        extra = Extra.allow

    prompt: str
    """
    Text prompt.
    """
    image_prompt_uri: Optional[str] = None
    """
    Image prompt.
    """
    num_images: int
    """
    Number of images to generate.
    """
    ip_adapter_scale: Annotated[Optional[float], Field(ge=0.0)] = None
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
    width: Optional[int] = None
    """
    Width of output image, in pixels.
    """
    height: Optional[int] = None
    """
    Height of output image, in pixels.
    """
    seeds: Optional[List[int]] = None
    """
    Random noise seeds. Default is random seeds for each generation.
    """


class StableDiffusionXLIPAdapterOut(BaseModel):
    class Config:
        extra = Extra.allow

    outputs: List[StableDiffusionImage]
    """
    Generated images.
    """


class StableDiffusionXLControlNetIn(BaseModel):
    class Config:
        extra = Extra.allow

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
    conditioning_scale: Annotated[Optional[float], Field(ge=0.0)] = None
    """
    Controls the influence of the input image on the generated output.
    """
    seeds: Optional[List[int]] = None
    """
    Random noise seeds. Default is random seeds for each generation.
    """


class StableDiffusionXLControlNetOut(BaseModel):
    class Config:
        extra = Extra.allow

    outputs: List[StableDiffusionImage]
    """
    Generated images.
    """


class GenerativeEditImageIn(BaseModel):
    class Config:
        extra = Extra.allow

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


class GenerativeEditImageOut(BaseModel):
    class Config:
        extra = Extra.allow

    image_uri: str
    """
    Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """


class MultiGenerativeEditImageIn(BaseModel):
    class Config:
        extra = Extra.allow

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
    Mask image that controls which pixels are edited (inpainting). If unset, the entire image is edited (image-to-image).
    """
    num_images: int
    """
    Number of images to generate.
    """
    store: Optional[str] = None
    """
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](/docs/file-stores). If unset, the image data will be returned as a base64-encoded string.
    """
    node: Literal["StableDiffusionXLInpaint"] = "StableDiffusionXLInpaint"
    """
    Selected node.
    """


class MultiGenerativeEditImageOut(BaseModel):
    class Config:
        extra = Extra.allow

    outputs: List[GenerativeEditImageOut]
    """
    Generated images.
    """


class StableDiffusionXLInpaintIn(BaseModel):
    class Config:
        extra = Extra.allow

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
    Mask image that controls which pixels are edited (inpainting). If unset, the entire image is edited (image-to-image).
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
    strength: Annotated[float, Field(ge=0.0, le=1.0)] = 1
    """
    Controls the strength of the generation process.
    """
    seeds: Optional[List[int]] = None
    """
    Random noise seeds. Default is random seeds for each generation.
    """


class StableDiffusionXLInpaintOut(BaseModel):
    class Config:
        extra = Extra.allow

    outputs: List[StableDiffusionImage]
    """
    Generated images.
    """


class BoundingBox(BaseModel):
    class Config:
        extra = Extra.allow

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


class Point(BaseModel):
    class Config:
        extra = Extra.allow

    x: int
    """
    X position.
    """
    y: int
    """
    Y position.
    """


class FillMaskIn(BaseModel):
    class Config:
        extra = Extra.allow

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


class FillMaskOut(BaseModel):
    class Config:
        extra = Extra.allow

    image_uri: str
    """
    Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """


class BigLaMaIn(BaseModel):
    class Config:
        extra = Extra.allow

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


class BigLaMaOut(BaseModel):
    class Config:
        extra = Extra.allow

    image_uri: str
    """
    Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """


class RemoveBackgroundIn(BaseModel):
    class Config:
        extra = Extra.allow

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


class RemoveBackgroundOut(BaseModel):
    class Config:
        extra = Extra.allow

    image_uri: str
    """
    Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """


class DISISNetIn(BaseModel):
    class Config:
        extra = Extra.allow

    image_uri: str
    """
    Input image.
    """
    store: Optional[str] = None
    """
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](/docs/file-stores). If unset, the image data will be returned as a base64-encoded string.
    """


class DISISNetOut(BaseModel):
    class Config:
        extra = Extra.allow

    image_uri: str
    """
    Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """


class UpscaleImageIn(BaseModel):
    class Config:
        extra = Extra.allow

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


class UpscaleImageOut(BaseModel):
    class Config:
        extra = Extra.allow

    image_uri: str
    """
    Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """


class RealESRGANIn(BaseModel):
    class Config:
        extra = Extra.allow

    image_uri: str
    """
    Input image.
    """
    store: Optional[str] = None
    """
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](/docs/file-stores). If unset, the image data will be returned as a base64-encoded string.
    """


class RealESRGANOut(BaseModel):
    class Config:
        extra = Extra.allow

    image_uri: str
    """
    Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """


class SegmentUnderPointIn(BaseModel):
    class Config:
        extra = Extra.allow

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


class SegmentUnderPointOut(BaseModel):
    class Config:
        extra = Extra.allow

    mask_image_uri: str
    """
    Detected segments in 'mask image' format. Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """


class SegmentAnythingIn(BaseModel):
    class Config:
        extra = Extra.allow

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


class SegmentAnythingOut(BaseModel):
    class Config:
        extra = Extra.allow

    mask_image_uri: str
    """
    Detected segments in 'mask image' format. Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """


class TranscribeMediaIn(BaseModel):
    class Config:
        extra = Extra.allow

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


class TranscribedWord(BaseModel):
    class Config:
        extra = Extra.allow

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


class TranscribedSegment(BaseModel):
    class Config:
        extra = Extra.allow

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


class ChapterMarker(BaseModel):
    class Config:
        extra = Extra.allow

    title: str
    """
    Chapter title.
    """
    start: float
    """
    Start time of chapter, in seconds.
    """


class TranscribeMediaOut(BaseModel):
    class Config:
        extra = Extra.allow

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


class GenerateSpeechIn(BaseModel):
    class Config:
        extra = Extra.allow

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


class GenerateSpeechOut(BaseModel):
    class Config:
        extra = Extra.allow

    audio_uri: str
    """
    Base 64-encoded WAV audio bytes, or a hosted audio url if `store` is provided.
    """


class XTTSV2In(BaseModel):
    class Config:
        extra = Extra.allow

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


class XTTSV2Out(BaseModel):
    class Config:
        extra = Extra.allow

    audio_uri: str
    """
    Base 64-encoded WAV audio bytes, or a hosted audio url if `store` is provided.
    """


class Embedding(BaseModel):
    class Config:
        extra = Extra.allow

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


class EmbedTextIn(BaseModel):
    class Config:
        extra = Extra.allow

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


class EmbedTextOut(BaseModel):
    class Config:
        extra = Extra.allow

    embedding: Embedding
    """
    Generated embedding.
    """


class EmbedTextItem(BaseModel):
    class Config:
        extra = Extra.allow

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


class MultiEmbedTextIn(BaseModel):
    class Config:
        extra = Extra.allow

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


class MultiEmbedTextOut(BaseModel):
    class Config:
        extra = Extra.allow

    embeddings: List[Embedding]
    """
    Generated embeddings.
    """


class JinaV2In(BaseModel):
    class Config:
        extra = Extra.allow

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


class JinaV2Out(BaseModel):
    class Config:
        extra = Extra.allow

    embeddings: List[Embedding]
    """
    Generated embeddings.
    """


class EmbedImageIn(BaseModel):
    class Config:
        extra = Extra.allow

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


class EmbedImageOut(BaseModel):
    class Config:
        extra = Extra.allow

    embedding: Embedding
    """
    Generated embedding.
    """


class EmbedImageItem(BaseModel):
    class Config:
        extra = Extra.allow

    image_uri: str
    """
    Image to embed.
    """
    doc_id: Optional[str] = None
    """
    Vector store document ID. Ignored if `store` is unset.
    """


class EmbedTextOrImageItem(BaseModel):
    class Config:
        extra = Extra.allow

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


class MultiEmbedImageIn(BaseModel):
    class Config:
        extra = Extra.allow

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


class MultiEmbedImageOut(BaseModel):
    class Config:
        extra = Extra.allow

    embeddings: List[Embedding]
    """
    Generated embeddings.
    """


class CLIPIn(BaseModel):
    class Config:
        extra = Extra.allow

    items: List[EmbedTextOrImageItem]
    """
    Items to embed.
    """
    embedded_metadata_keys: Optional[List[str]] = None
    """
    Choose keys from `metadata` to embed with text, when embedding and storing text documents.
    """
    store: Optional[str] = None
    """
    [Vector store](/docs/vector-stores) identifier.
    """


class CLIPOut(BaseModel):
    class Config:
        extra = Extra.allow

    embeddings: List[Embedding]
    """
    Generated embeddings.
    """


class CreateVectorStoreIn(BaseModel):
    class Config:
        extra = Extra.allow

    name: Annotated[str, Field(max_length=63, min_length=1)]
    """
    Vector store name.
    """
    model: Literal["jina-v2", "clip"]
    """
    Selected embedding model
    """
    m: Annotated[int, Field(ge=1, le=64)] = 16
    """
    The max number of connections per layer for the index.
    """
    ef_construction: Annotated[int, Field(ge=1, le=128)] = 64
    """
    The size of the dynamic candidate list for constructing the index graph.
    """
    metric: Literal["cosine", "l2", "inner"] = "inner"
    """
    The distance metric to construct the index with.
    """


class CreateVectorStoreOut(BaseModel):
    class Config:
        extra = Extra.allow

    name: Annotated[str, Field(max_length=63, min_length=1)]
    """
    Vector store name.
    """
    model: Literal["jina-v2", "clip"]
    """
    Selected embedding model
    """
    m: Annotated[int, Field(ge=1, le=64)]
    """
    The max number of connections per layer for the index.
    """
    ef_construction: Annotated[int, Field(ge=1, le=128)]
    """
    The size of the dynamic candidate list for constructing the index graph.
    """
    metric: Literal["cosine", "l2", "inner"]
    """
    The distance metric to construct the index with.
    """


class ListVectorStoresIn(BaseModel):
    pass

    class Config:
        extra = Extra.allow


class ListVectorStoresOut(BaseModel):
    class Config:
        extra = Extra.allow

    stores: Optional[List[CreateVectorStoreOut]] = None
    """
    List of vector stores.
    """


class DeleteVectorStoreIn(BaseModel):
    class Config:
        extra = Extra.allow

    name: str
    """
    Vector store name.
    """
    model: Literal["jina-v2", "clip"]
    """
    Selected embedding model
    """


class DeleteVectorStoreOut(BaseModel):
    class Config:
        extra = Extra.allow

    name: str
    """
    Vector store name.
    """
    model: Literal["jina-v2", "clip"]
    """
    Selected embedding model
    """


class Vector(BaseModel):
    """
    Canonical representation of document with embedding vector.
    """

    class Config:
        extra = Extra.allow

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


class FetchVectorsIn(BaseModel):
    class Config:
        extra = Extra.allow

    name: str
    """
    Vector store name.
    """
    model: Literal["jina-v2", "clip"]
    """
    Selected embedding model
    """
    ids: Annotated[List[str], Field(max_items=100)]
    """
    Document IDs to retrieve.
    """


class FetchVectorsOut(BaseModel):
    class Config:
        extra = Extra.allow

    vectors: List[Vector]
    """
    Retrieved vectors.
    """


class UpdateVectorsOut(BaseModel):
    class Config:
        extra = Extra.allow

    count: int
    """
    Number of vectors modified.
    """


class DeleteVectorsOut(BaseModel):
    class Config:
        extra = Extra.allow

    count: int
    """
    Number of vectors modified.
    """


class UpdateVectorParams(BaseModel):
    class Config:
        extra = Extra.allow

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


class UpdateVectorsIn(BaseModel):
    class Config:
        extra = Extra.allow

    name: str
    """
    Vector store name.
    """
    model: Literal["jina-v2", "clip"]
    """
    Selected embedding model
    """
    vectors: Annotated[List[UpdateVectorParams], Field(max_items=100)]
    """
    Vectors to upsert.
    """


class DeleteVectorsIn(BaseModel):
    class Config:
        extra = Extra.allow

    name: str
    """
    Vector store name.
    """
    model: Literal["jina-v2", "clip"]
    """
    Selected embedding model
    """
    ids: Annotated[List[str], Field(max_items=100)]
    """
    Document IDs to delete.
    """


class QueryVectorStoreIn(BaseModel):
    class Config:
        extra = Extra.allow

    name: str
    """
    Vector store to query against.
    """
    model: Literal["jina-v2", "clip"]
    """
    Selected embedding model
    """
    query_ids: Optional[List[str]] = None
    """
    Document IDs to use for the query.
    """
    query_image_uris: Optional[List[str]] = None
    """
    Image URIs to embed and use for the query.
    """
    query_vectors: Optional[List[List[float]]] = None
    """
    Vector to use for the query.
    """
    query_strings: Optional[List[str]] = None
    """
    Texts to embed and use for the query.
    """
    top_k: Annotated[int, Field(ge=1, le=1000)] = 10
    """
    Number of results to return.
    """
    ef_search: Annotated[int, Field(ge=1, le=1000)] = 40
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


class VectorStoreQueryResult(BaseModel):
    class Config:
        extra = Extra.allow

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


class QueryVectorStoreOut(BaseModel):
    class Config:
        extra = Extra.allow

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
    Selected embedding model
    """
    metric: Optional[Literal["cosine", "l2", "inner"]] = None
    """
    The distance metric used for the query.
    """
