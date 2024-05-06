"""
꩜ Substrate
@generated file
(using datamodel-codegen)
"""


from __future__ import annotations

from typing import Any, Dict, List, Optional
from typing_extensions import Literal, Annotated

from pydantic import Field, BaseModel


class ErrorOut(BaseModel):
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


class RunCodeIn(BaseModel):
    code: str
    """
    Code to execute.
    """
    args: Optional[List[str]] = None
    """
    List of command line arguments.
    """
    language: Literal["python", "typescript", "javascript"] = "python"
    """
    Interpreter to use.
    """


class RunCodeOut(BaseModel):
    output: Optional[str] = None
    """
    Contents of `stdout` after executing the code.
    """
    json_output: Dict[str, Any]
    """
    `output` as parsed JSON. Print serialized json to `stdout` to receive JSON.
    """
    error: Optional[str] = None
    """
    Contents of `stderr` after executing the code.
    """


class GenerateTextIn(BaseModel):
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
    node: Literal[
        "Mistral7BInstruct",
        "Mixtral8x7BInstruct",
        "Llama3Instruct8B",
        "Llama3Instruct70B",
    ] = "Mistral7BInstruct"
    """
    Selected node.
    """


class GenerateTextOut(BaseModel):
    text: str
    """
    Text response.
    """


class GenerateJSONIn(BaseModel):
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
    node: Literal["Mistral7BInstruct", "Mixtral8x7BInstruct"] = "Mistral7BInstruct"
    """
    Selected node.
    """


class GenerateJSONOut(BaseModel):
    json_object: Dict[str, Any]
    """
    JSON response.
    """


class MultiGenerateTextIn(BaseModel):
    prompt: str
    """
    Input prompt.
    """
    num_choices: Annotated[int, Field(ge=1, le=8)]
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
    node: Literal[
        "Mistral7BInstruct",
        "Mixtral8x7BInstruct",
        "Llama3Instruct8B",
        "Llama3Instruct70B",
    ] = "Mistral7BInstruct"
    """
    Selected node.
    """


class MultiGenerateTextOut(BaseModel):
    choices: List[GenerateTextOut]
    """
    Response choices.
    """


class BatchGenerateTextIn(BaseModel):
    prompts: List[str]
    """
    Batch input prompts.
    """
    temperature: Annotated[float, Field(ge=0.0, le=1.0)] = 0.4
    """
    Sampling temperature to use. Higher values make the output more random, lower values make the output more deterministic.
    """
    max_tokens: Optional[int] = None
    """
    Maximum number of tokens to generate.
    """


class BatchGenerateTextOut(BaseModel):
    outputs: List[GenerateTextOut]
    """
    Batch outputs.
    """


class MultiGenerateJSONIn(BaseModel):
    prompt: str
    """
    Input prompt.
    """
    json_schema: Dict[str, Any]
    """
    JSON schema to guide `json_object` response.
    """
    num_choices: Annotated[int, Field(ge=1, le=8)]
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
    node: Literal["Mistral7BInstruct", "Mixtral8x7BInstruct"] = "Mistral7BInstruct"
    """
    Selected node.
    """


class MultiGenerateJSONOut(BaseModel):
    choices: List[GenerateJSONOut]
    """
    Response choices.
    """


class BatchGenerateJSONIn(BaseModel):
    prompts: List[str]
    """
    Batch input prompts.
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


class BatchGenerateJSONOut(BaseModel):
    outputs: List[GenerateJSONOut]
    """
    Batch outputs.
    """


class Mistral7BInstructIn(BaseModel):
    prompt: str
    """
    Input prompt.
    """
    num_choices: Annotated[int, Field(ge=1, le=8)] = 1
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
    text: Optional[str] = None
    """
    Text response, if `json_schema` was not provided.
    """
    json_object: Optional[Dict[str, Any]] = None
    """
    JSON response, if `json_schema` was provided.
    """


class Mistral7BInstructOut(BaseModel):
    choices: List[Mistral7BInstructChoice]
    """
    Response choices.
    """


class Mixtral8x7BInstructIn(BaseModel):
    prompt: str
    """
    Input prompt.
    """
    num_choices: Annotated[int, Field(ge=1, le=8)] = 1
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


class Mixtral8x7BChoice(BaseModel):
    text: Optional[str] = None
    """
    Text response, if `json_schema` was not provided.
    """
    json_object: Optional[Dict[str, Any]] = None
    """
    JSON response, if `json_schema` was provided.
    """


class Mixtral8x7BInstructOut(BaseModel):
    choices: List[Mixtral8x7BChoice]
    """
    Response choices.
    """


class Llama3Instruct8BIn(BaseModel):
    prompt: str
    """
    Input prompt.
    """
    num_choices: Annotated[int, Field(ge=1, le=8)] = 1
    """
    Number of choices to generate.
    """
    temperature: Annotated[Optional[float], Field(ge=0.0, le=1.0)] = None
    """
    Sampling temperature to use. Higher values make the output more random, lower values make the output more deterministic.
    """
    max_tokens: Optional[int] = None
    """
    Maximum number of tokens to generate.
    """


class Llama3Instruct8BChoice(BaseModel):
    text: Optional[str] = None
    """
    Text response.
    """


class Llama3Instruct8BOut(BaseModel):
    choices: List[Llama3Instruct8BChoice]
    """
    Response choices.
    """


class Llama3Instruct70BIn(BaseModel):
    prompt: str
    """
    Input prompt.
    """
    num_choices: Annotated[int, Field(ge=1, le=8)] = 1
    """
    Number of choices to generate.
    """
    temperature: Annotated[Optional[float], Field(ge=0.0, le=1.0)] = None
    """
    Sampling temperature to use. Higher values make the output more random, lower values make the output more deterministic.
    """
    max_tokens: Optional[int] = None
    """
    Maximum number of tokens to generate.
    """


class Llama3Instruct70BChoice(BaseModel):
    text: Optional[str] = None
    """
    Text response.
    """


class Llama3Instruct70BOut(BaseModel):
    choices: List[Llama3Instruct70BChoice]
    """
    Response choices.
    """


class GenerateTextVisionIn(BaseModel):
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


class GenerateTextVisionOut(BaseModel):
    text: str
    """
    Text response.
    """


class Firellava13BIn(BaseModel):
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


class Firellava13BOut(BaseModel):
    text: str
    """
    Text response.
    """


class GenerateImageIn(BaseModel):
    prompt: str
    """
    Text prompt.
    """
    store: Optional[str] = None
    """
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://guides.substrate.run/guides/external-file-storage). If unset, the image data will be returned as a base64-encoded string.
    """


class GenerateImageOut(BaseModel):
    image_uri: str
    """
    Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """


class MultiGenerateImageIn(BaseModel):
    prompt: str
    """
    Text prompt.
    """
    num_images: Annotated[int, Field(ge=1, le=8)]
    """
    Number of images to generate.
    """
    store: Optional[str] = None
    """
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://guides.substrate.run/guides/external-file-storage). If unset, the image data will be returned as a base64-encoded string.
    """


class MultiGenerateImageOut(BaseModel):
    outputs: List[GenerateImageOut]
    """
    Generated images.
    """


class StableDiffusionXLIn(BaseModel):
    prompt: str
    """
    Text prompt.
    """
    negative_prompt: Optional[str] = None
    """
    Negative input prompt.
    """
    steps: Annotated[int, Field(ge=0, le=150)] = 30
    """
    Number of diffusion steps.
    """
    num_images: Annotated[int, Field(ge=1, le=8)]
    """
    Number of images to generate.
    """
    store: Optional[str] = None
    """
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://guides.substrate.run/guides/external-file-storage). If unset, the image data will be returned as a base64-encoded string.
    """
    height: Annotated[int, Field(ge=256, le=1536)] = 1024
    """
    Height of output image, in pixels.
    """
    width: Annotated[int, Field(ge=256, le=1536)] = 1024
    """
    Width of output image, in pixels.
    """
    seeds: Optional[List[int]] = None
    """
    Seeds for deterministic generation. Default is a random seed.
    """
    guidance_scale: Annotated[float, Field(ge=0.0, le=30.0)] = 7
    """
    Higher values adhere to the text prompt more strongly, typically at the expense of image quality.
    """


class StableDiffusionImage(BaseModel):
    image_uri: str
    """
    Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """
    seed: int
    """
    The random noise seed used for generation.
    """


class StableDiffusionXLOut(BaseModel):
    outputs: List[StableDiffusionImage]
    """
    Generated images.
    """


class StableDiffusionXLLightningIn(BaseModel):
    prompt: str
    """
    Text prompt.
    """
    negative_prompt: Optional[str] = None
    """
    Negative input prompt.
    """
    num_images: Annotated[int, Field(ge=1, le=8)] = 1
    """
    Number of images to generate.
    """
    store: Optional[str] = None
    """
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://guides.substrate.run/guides/external-file-storage). If unset, the image data will be returned as a base64-encoded string.
    """
    height: Annotated[int, Field(ge=256, le=1536)] = 1024
    """
    Height of output image, in pixels.
    """
    width: Annotated[int, Field(ge=256, le=1536)] = 1024
    """
    Width of output image, in pixels.
    """
    seeds: Optional[List[int]] = None
    """
    Seeds for deterministic generation. Default is a random seed.
    """


class StableDiffusionXLLightningOut(BaseModel):
    outputs: List[StableDiffusionImage]
    """
    Generated images.
    """


class StableDiffusionXLIPAdapterIn(BaseModel):
    prompt: str
    """
    Text prompt.
    """
    image_prompt_uri: Optional[str] = None
    """
    Image prompt.
    """
    num_images: Annotated[int, Field(ge=1, le=8)]
    """
    Number of images to generate.
    """
    ip_adapter_scale: Annotated[float, Field(ge=0.0, le=1.0)] = 0.5
    """
    Controls the influence of the image prompt on the generated output.
    """
    negative_prompt: Optional[str] = None
    """
    Negative input prompt.
    """
    store: Optional[str] = None
    """
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://guides.substrate.run/guides/external-file-storage). If unset, the image data will be returned as a base64-encoded string.
    """
    width: Annotated[int, Field(ge=640, le=1536)] = 1024
    """
    Width of output image, in pixels.
    """
    height: Annotated[int, Field(ge=640, le=1536)] = 1024
    """
    Height of output image, in pixels.
    """
    seeds: Optional[List[int]] = None
    """
    Random noise seeds. Default is random seeds for each generation.
    """


class StableDiffusionXLIPAdapterOut(BaseModel):
    outputs: List[StableDiffusionImage]
    """
    Generated images.
    """


class StableDiffusionXLControlNetIn(BaseModel):
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
    num_images: Annotated[int, Field(ge=1, le=8)]
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
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://guides.substrate.run/guides/external-file-storage). If unset, the image data will be returned as a base64-encoded string.
    """
    conditioning_scale: Annotated[float, Field(ge=0.0, le=1.0)] = 0.5
    """
    Controls the influence of the input image on the generated output.
    """
    seeds: Optional[List[int]] = None
    """
    Random noise seeds. Default is random seeds for each generation.
    """


class StableDiffusionXLControlNetOut(BaseModel):
    outputs: List[StableDiffusionImage]
    """
    Generated images.
    """


class GenerativeEditImageIn(BaseModel):
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
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://guides.substrate.run/guides/external-file-storage). If unset, the image data will be returned as a base64-encoded string.
    """


class GenerativeEditImageOut(BaseModel):
    image_uri: str
    """
    Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """


class MultiGenerativeEditImageIn(BaseModel):
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
    num_images: Annotated[int, Field(ge=1, le=8)]
    """
    Number of images to generate.
    """
    store: Optional[str] = None
    """
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://guides.substrate.run/guides/external-file-storage). If unset, the image data will be returned as a base64-encoded string.
    """


class MultiGenerativeEditImageOut(BaseModel):
    outputs: List[GenerativeEditImageOut]
    """
    Generated images.
    """


class StableDiffusionXLInpaintIn(BaseModel):
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
    num_images: Annotated[int, Field(ge=1, le=8)]
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
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://guides.substrate.run/guides/external-file-storage). If unset, the image data will be returned as a base64-encoded string.
    """
    strength: Annotated[float, Field(ge=0.0, le=1.0)] = 0.8
    """
    Controls the strength of the generation process.
    """
    seeds: Optional[List[int]] = None
    """
    Random noise seeds. Default is random seeds for each generation.
    """


class StableDiffusionXLInpaintOut(BaseModel):
    outputs: List[StableDiffusionImage]
    """
    Generated images.
    """


class BoundingBox(BaseModel):
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
    x: int
    """
    X position.
    """
    y: int
    """
    Y position.
    """


class FillMaskIn(BaseModel):
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
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://guides.substrate.run/guides/external-file-storage). If unset, the image data will be returned as a base64-encoded string.
    """


class FillMaskOut(BaseModel):
    image_uri: str
    """
    Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """


class BigLaMaIn(BaseModel):
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
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://guides.substrate.run/guides/external-file-storage). If unset, the image data will be returned as a base64-encoded string.
    """


class BigLaMaOut(BaseModel):
    image_uri: str
    """
    Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """


class RemoveBackgroundIn(BaseModel):
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
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://guides.substrate.run/guides/external-file-storage). If unset, the image data will be returned as a base64-encoded string.
    """


class RemoveBackgroundOut(BaseModel):
    image_uri: str
    """
    Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """


class DISISNetIn(BaseModel):
    image_uri: str
    """
    Input image.
    """
    store: Optional[str] = None
    """
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://guides.substrate.run/guides/external-file-storage). If unset, the image data will be returned as a base64-encoded string.
    """


class DISISNetOut(BaseModel):
    image_uri: str
    """
    Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """


class UpscaleImageIn(BaseModel):
    image_uri: str
    """
    Input image.
    """
    store: Optional[str] = None
    """
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://guides.substrate.run/guides/external-file-storage). If unset, the image data will be returned as a base64-encoded string.
    """


class UpscaleImageOut(BaseModel):
    image_uri: str
    """
    Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """


class RealESRGANIn(BaseModel):
    image_uri: str
    """
    Input image.
    """
    store: Optional[str] = None
    """
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://guides.substrate.run/guides/external-file-storage). If unset, the image data will be returned as a base64-encoded string.
    """


class RealESRGANOut(BaseModel):
    image_uri: str
    """
    Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """


class SegmentUnderPointIn(BaseModel):
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
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://guides.substrate.run/guides/external-file-storage). If unset, the image data will be returned as a base64-encoded string.
    """


class SegmentUnderPointOut(BaseModel):
    mask_image_uri: str
    """
    Detected segments in 'mask image' format. Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """


class SegmentAnythingIn(BaseModel):
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
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://guides.substrate.run/guides/external-file-storage). If unset, the image data will be returned as a base64-encoded string.
    """


class SegmentAnythingOut(BaseModel):
    mask_image_uri: str
    """
    Detected segments in 'mask image' format. Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """


class TranscribeMediaIn(BaseModel):
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
    title: str
    """
    Chapter title.
    """
    start: float
    """
    Start time of chapter, in seconds.
    """


class TranscribeMediaOut(BaseModel):
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
    text: str
    """
    Input text.
    """
    store: Optional[str] = None
    """
    Use "hosted" to return an audio URL hosted on Substrate. You can also provide a URL to a registered [file store](https://guides.substrate.run/guides/external-file-storage). If unset, the audio data will be returned as a base64-encoded string.
    """


class GenerateSpeechOut(BaseModel):
    audio_uri: str
    """
    Base 64-encoded WAV audio bytes, or a hosted audio url if `store` is provided.
    """


class XTTSV2In(BaseModel):
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
    Use "hosted" to return an audio URL hosted on Substrate. You can also provide a URL to a registered [file store](https://guides.substrate.run/guides/external-file-storage). If unset, the audio data will be returned as a base64-encoded string.
    """


class XTTSV2Out(BaseModel):
    audio_uri: str
    """
    Base 64-encoded WAV audio bytes, or a hosted audio url if `store` is provided.
    """


class Embedding(BaseModel):
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
    text: str
    """
    Text to embed.
    """
    collection_name: Optional[str] = None
    """
    Vector store name.
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
    model: Literal["jina-v2", "clip"] = "jina-v2"
    """
    Selected embedding model.
    """


class EmbedTextOut(BaseModel):
    embedding: Embedding
    """
    Generated embedding.
    """


class EmbedTextItem(BaseModel):
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
    items: List[EmbedTextItem]
    """
    Items to embed.
    """
    collection_name: Optional[str] = None
    """
    Vector store name.
    """
    embedded_metadata_keys: Optional[List[str]] = None
    """
    Choose keys from `metadata` to embed with text.
    """
    model: Literal["jina-v2", "clip"] = "jina-v2"
    """
    Selected embedding model.
    """


class MultiEmbedTextOut(BaseModel):
    embeddings: List[Embedding]
    """
    Generated embeddings.
    """


class JinaV2In(BaseModel):
    items: List[EmbedTextItem]
    """
    Items to embed.
    """
    collection_name: Optional[str] = None
    """
    Vector store name.
    """
    embedded_metadata_keys: Optional[List[str]] = None
    """
    Choose keys from `metadata` to embed with text.
    """


class JinaV2Out(BaseModel):
    embeddings: List[Embedding]
    """
    Generated embeddings.
    """


class EmbedImageIn(BaseModel):
    image_uri: str
    """
    Image to embed.
    """
    collection_name: Optional[str] = None
    """
    Vector store name.
    """
    doc_id: Optional[str] = None
    """
    Vector store document ID. Ignored if `store` is unset.
    """
    model: Literal["clip"] = "clip"
    """
    Selected embedding model.
    """


class EmbedImageOut(BaseModel):
    embedding: Embedding
    """
    Generated embedding.
    """


class EmbedImageItem(BaseModel):
    image_uri: str
    """
    Image to embed.
    """
    doc_id: Optional[str] = None
    """
    Vector store document ID. Ignored if `store` is unset.
    """


class EmbedTextOrImageItem(BaseModel):
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
    items: List[EmbedImageItem]
    """
    Items to embed.
    """
    collection_name: Optional[str] = None
    """
    Vector store name.
    """
    model: Literal["clip"] = "clip"
    """
    Selected embedding model.
    """


class MultiEmbedImageOut(BaseModel):
    embeddings: List[Embedding]
    """
    Generated embeddings.
    """


class CLIPIn(BaseModel):
    items: List[EmbedTextOrImageItem]
    """
    Items to embed.
    """
    collection_name: Optional[str] = None
    """
    Vector store name.
    """
    embedded_metadata_keys: Optional[List[str]] = None
    """
    Choose keys from `metadata` to embed with text. Only applies to text items.
    """


class CLIPOut(BaseModel):
    embeddings: List[Embedding]
    """
    Generated embeddings.
    """


class CreateVectorStoreIn(BaseModel):
    collection_name: Annotated[str, Field(max_length=63, min_length=1)]
    """
    Vector store name.
    """
    model: Literal["jina-v2", "clip"]
    """
    Selected embedding model.
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
    collection_name: Annotated[str, Field(max_length=63, min_length=1)]
    """
    Vector store name.
    """
    model: Literal["jina-v2", "clip"]
    """
    Selected embedding model.
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


class ListVectorStoresOut(BaseModel):
    items: Optional[List[CreateVectorStoreOut]] = None
    """
    List of vector stores.
    """


class DeleteVectorStoreIn(BaseModel):
    collection_name: str
    """
    Vector store name.
    """
    model: Literal["jina-v2", "clip"]
    """
    Selected embedding model.
    """


class DeleteVectorStoreOut(BaseModel):
    collection_name: str
    """
    Vector store name.
    """
    model: Literal["jina-v2", "clip"]
    """
    Selected embedding model.
    """


class Vector(BaseModel):
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


class FetchVectorsIn(BaseModel):
    collection_name: str
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


class FetchVectorsOut(BaseModel):
    vectors: List[Vector]
    """
    Retrieved vectors.
    """


class UpdateVectorsOut(BaseModel):
    count: int
    """
    Number of vectors modified.
    """


class DeleteVectorsOut(BaseModel):
    count: int
    """
    Number of vectors modified.
    """


class UpdateVectorParams(BaseModel):
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
    collection_name: str
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


class DeleteVectorsIn(BaseModel):
    collection_name: str
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


class QueryVectorStoreIn(BaseModel):
    collection_name: str
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


class VectorStoreQueryResult(BaseModel):
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
    results: List[List[VectorStoreQueryResult]]
    """
    Query results.
    """
    collection_name: Optional[str] = None
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
