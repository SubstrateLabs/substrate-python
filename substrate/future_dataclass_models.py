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
    request_id: Optional[str] = None
    """
    (Future reference)
    A unique identifier for the request.
    """


@dataclass
class FutureRunCodeIn:
    """
    (Future reference)
    """

    code: str
    """
    (Future reference)
    Code to execute.
    """
    args: Optional[List[str]] = None
    """
    (Future reference)
    List of command line arguments.
    """
    language: Literal["python", "typescript", "javascript"] = "python"
    """
    (Future reference)
    Interpreter to use.
    """


@dataclass
class FutureRunCodeOut:
    """
    (Future reference)
    """

    json_output: Dict[str, Any]
    """
    (Future reference)
    `output` as parsed JSON. Print serialized json to `stdout` to receive JSON.
    """
    output: Optional[str] = None
    """
    (Future reference)
    Contents of `stdout` after executing the code.
    """
    error: Optional[str] = None
    """
    (Future reference)
    Contents of `stderr` after executing the code.
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
    temperature: float = 0.4
    """
    (Future reference)
    Sampling temperature to use. Higher values make the output more random, lower values make the output more deterministic.
    """
    max_tokens: Optional[int] = None
    """
    (Future reference)
    Maximum number of tokens to generate.
    """
    node: Literal[
        "Mistral7BInstruct",
        "Mixtral8x7BInstruct",
        "Llama3Instruct8B",
        "Llama3Instruct70B",
    ] = "Mistral7BInstruct"
    """
    (Future reference)
    Selected node.
    """


@dataclass
class FutureGenerateTextOut:
    """
    (Future reference)
    """

    text: str
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
    temperature: float = 0.4
    """
    (Future reference)
    Sampling temperature to use. Higher values make the output more random, lower values make the output more deterministic.
    """
    max_tokens: Optional[int] = None
    """
    (Future reference)
    Maximum number of tokens to generate.
    """
    node: Literal["Mistral7BInstruct", "Mixtral8x7BInstruct"] = "Mistral7BInstruct"
    """
    (Future reference)
    Selected node.
    """


@dataclass
class FutureGenerateJSONOut:
    """
    (Future reference)
    """

    json_object: Dict[str, Any]
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
    temperature: float = 0.4
    """
    (Future reference)
    Sampling temperature to use. Higher values make the output more random, lower values make the output more deterministic.
    """
    max_tokens: Optional[int] = None
    """
    (Future reference)
    Maximum number of tokens to generate.
    """
    node: Literal[
        "Mistral7BInstruct",
        "Mixtral8x7BInstruct",
        "Llama3Instruct8B",
        "Llama3Instruct70B",
    ] = "Mistral7BInstruct"
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
    """
    (Future reference)
    Response choices.
    """


@dataclass
class FutureBatchGenerateTextIn:
    """
    (Future reference)
    """

    prompts: List[str]
    """
    (Future reference)
    Batch input prompts.
    """
    temperature: float = 0.4
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
class FutureBatchGenerateTextOut:
    """
    (Future reference)
    """

    outputs: List[FutureGenerateTextOut]
    """
    (Future reference)
    Batch outputs.
    """


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
    temperature: float = 0.4
    """
    (Future reference)
    Sampling temperature to use. Higher values make the output more random, lower values make the output more deterministic.
    """
    max_tokens: Optional[int] = None
    """
    (Future reference)
    Maximum number of tokens to generate.
    """
    node: Literal["Mistral7BInstruct", "Mixtral8x7BInstruct"] = "Mistral7BInstruct"
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
    """
    (Future reference)
    Response choices.
    """


@dataclass
class FutureBatchGenerateJSONIn:
    """
    (Future reference)
    """

    prompts: List[str]
    """
    (Future reference)
    Batch input prompts.
    """
    json_schema: Dict[str, Any]
    """
    (Future reference)
    JSON schema to guide `json_object` response.
    """
    temperature: float = 0.4
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
class FutureBatchGenerateJSONOut:
    """
    (Future reference)
    """

    outputs: List[FutureGenerateJSONOut]
    """
    (Future reference)
    Batch outputs.
    """


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
    num_choices: int = 1
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
    """
    (Future reference)
    Response choices.
    """


@dataclass
class FutureMixtral8x7BInstructIn:
    """
    (Future reference)
    """

    prompt: str
    """
    (Future reference)
    Input prompt.
    """
    num_choices: int = 1
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
class Mixtral8x7BChoice:
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
class FutureMixtral8x7BInstructOut:
    """
    (Future reference)
    """

    choices: List[Mixtral8x7BChoice]
    """
    (Future reference)
    Response choices.
    """


@dataclass
class FutureLlama3Instruct8BIn:
    """
    (Future reference)
    """

    prompt: str
    """
    (Future reference)
    Input prompt.
    """
    num_choices: int = 1
    """
    (Future reference)
    Number of choices to generate.
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
class Llama3Instruct8BChoice:
    """
    (Future reference)
    """

    text: Optional[str] = None
    """
    (Future reference)
    Text response.
    """


@dataclass
class FutureLlama3Instruct8BOut:
    """
    (Future reference)
    """

    choices: List[Llama3Instruct8BChoice]
    """
    (Future reference)
    Response choices.
    """


@dataclass
class FutureLlama3Instruct70BIn:
    """
    (Future reference)
    """

    prompt: str
    """
    (Future reference)
    Input prompt.
    """
    num_choices: int = 1
    """
    (Future reference)
    Number of choices to generate.
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
class Llama3Instruct70BChoice:
    """
    (Future reference)
    """

    text: Optional[str] = None
    """
    (Future reference)
    Text response.
    """


@dataclass
class FutureLlama3Instruct70BOut:
    """
    (Future reference)
    """

    choices: List[Llama3Instruct70BChoice]
    """
    (Future reference)
    Response choices.
    """


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
    max_tokens: int = 800
    """
    (Future reference)
    Maximum number of tokens to generate.
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
    max_tokens: int = 800
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
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://guides.substrate.run/guides/external-file-storage). If unset, the image data will be returned as a base64-encoded string.
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
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://guides.substrate.run/guides/external-file-storage). If unset, the image data will be returned as a base64-encoded string.
    """


@dataclass
class FutureMultiGenerateImageOut:
    """
    (Future reference)
    """

    outputs: List[FutureGenerateImageOut]
    """
    (Future reference)
    Generated images.
    """


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
    num_images: int
    """
    (Future reference)
    Number of images to generate.
    """
    negative_prompt: Optional[str] = None
    """
    (Future reference)
    Negative input prompt.
    """
    steps: int = 30
    """
    (Future reference)
    Number of diffusion steps.
    """
    store: Optional[str] = None
    """
    (Future reference)
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://guides.substrate.run/guides/external-file-storage). If unset, the image data will be returned as a base64-encoded string.
    """
    height: int = 1024
    """
    (Future reference)
    Height of output image, in pixels.
    """
    width: int = 1024
    """
    (Future reference)
    Width of output image, in pixels.
    """
    seeds: Optional[List[int]] = None
    """
    (Future reference)
    Seeds for deterministic generation. Default is a random seed.
    """
    guidance_scale: float = 7
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
    """
    (Future reference)
    Generated images.
    """


@dataclass
class FutureStableDiffusionXLLightningIn:
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
    num_images: int = 1
    """
    (Future reference)
    Number of images to generate.
    """
    store: Optional[str] = None
    """
    (Future reference)
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://guides.substrate.run/guides/external-file-storage). If unset, the image data will be returned as a base64-encoded string.
    """
    height: int = 1024
    """
    (Future reference)
    Height of output image, in pixels.
    """
    width: int = 1024
    """
    (Future reference)
    Width of output image, in pixels.
    """
    seeds: Optional[List[int]] = None
    """
    (Future reference)
    Seeds for deterministic generation. Default is a random seed.
    """


@dataclass
class FutureStableDiffusionXLLightningOut:
    """
    (Future reference)
    """

    outputs: List[StableDiffusionImage]
    """
    (Future reference)
    Generated images.
    """


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
    ip_adapter_scale: float = 0.5
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
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://guides.substrate.run/guides/external-file-storage). If unset, the image data will be returned as a base64-encoded string.
    """
    width: int = 1024
    """
    (Future reference)
    Width of output image, in pixels.
    """
    height: int = 1024
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
    """
    (Future reference)
    Generated images.
    """


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
    output_resolution: int = 1024
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
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://guides.substrate.run/guides/external-file-storage). If unset, the image data will be returned as a base64-encoded string.
    """
    conditioning_scale: float = 0.5
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
    """
    (Future reference)
    Generated images.
    """


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
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://guides.substrate.run/guides/external-file-storage). If unset, the image data will be returned as a base64-encoded string.
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
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://guides.substrate.run/guides/external-file-storage). If unset, the image data will be returned as a base64-encoded string.
    """


@dataclass
class FutureMultiGenerativeEditImageOut:
    """
    (Future reference)
    """

    outputs: List[FutureGenerativeEditImageOut]
    """
    (Future reference)
    Generated images.
    """


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
    output_resolution: int = 1024
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
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://guides.substrate.run/guides/external-file-storage). If unset, the image data will be returned as a base64-encoded string.
    """
    strength: float = 0.8
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
    """
    (Future reference)
    Generated images.
    """


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
    store: Optional[str] = None
    """
    (Future reference)
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://guides.substrate.run/guides/external-file-storage). If unset, the image data will be returned as a base64-encoded string.
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
class FutureBigLaMaIn:
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
    store: Optional[str] = None
    """
    (Future reference)
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://guides.substrate.run/guides/external-file-storage). If unset, the image data will be returned as a base64-encoded string.
    """


@dataclass
class FutureBigLaMaOut:
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
    return_mask: bool = False
    """
    (Future reference)
    Return a mask image instead of the original content.
    """
    background_color: Optional[str] = None
    """
    (Future reference)
    Hex value background color. Transparent if unset.
    """
    store: Optional[str] = None
    """
    (Future reference)
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://guides.substrate.run/guides/external-file-storage). If unset, the image data will be returned as a base64-encoded string.
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
class FutureDISISNetIn:
    """
    (Future reference)
    """

    image_uri: str
    """
    (Future reference)
    Input image.
    """
    store: Optional[str] = None
    """
    (Future reference)
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://guides.substrate.run/guides/external-file-storage). If unset, the image data will be returned as a base64-encoded string.
    """


@dataclass
class FutureDISISNetOut:
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
    store: Optional[str] = None
    """
    (Future reference)
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://guides.substrate.run/guides/external-file-storage). If unset, the image data will be returned as a base64-encoded string.
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
class FutureRealESRGANIn:
    """
    (Future reference)
    """

    image_uri: str
    """
    (Future reference)
    Input image.
    """
    store: Optional[str] = None
    """
    (Future reference)
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://guides.substrate.run/guides/external-file-storage). If unset, the image data will be returned as a base64-encoded string.
    """


@dataclass
class FutureRealESRGANOut:
    """
    (Future reference)
    """

    image_uri: str
    """
    (Future reference)
    Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """


@dataclass
class FutureSegmentUnderPointIn:
    """
    (Future reference)
    """

    image_uri: str
    """
    (Future reference)
    Input image.
    """
    point: Point
    """
    (Future reference)
    Point prompt.
    """
    store: Optional[str] = None
    """
    (Future reference)
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://guides.substrate.run/guides/external-file-storage). If unset, the image data will be returned as a base64-encoded string.
    """


@dataclass
class FutureSegmentUnderPointOut:
    """
    (Future reference)
    """

    mask_image_uri: str
    """
    (Future reference)
    Detected segments in 'mask image' format. Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """


@dataclass
class FutureSegmentAnythingIn:
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
    store: Optional[str] = None
    """
    (Future reference)
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://guides.substrate.run/guides/external-file-storage). If unset, the image data will be returned as a base64-encoded string.
    """


@dataclass
class FutureSegmentAnythingOut:
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
    language: str = "en"
    """
    (Future reference)
    Language of input audio in [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes) format.
    """
    segment: bool = False
    """
    (Future reference)
    Segment the text into sentences with approximate timestamps.
    """
    align: bool = False
    """
    (Future reference)
    Align transcription to produce more accurate sentence-level timestamps and word-level timestamps. An array of word segments will be included in each sentence segment.
    """
    diarize: bool = False
    """
    (Future reference)
    Identify speakers for each segment. Speaker IDs will be included in each segment.
    """
    suggest_chapters: bool = False
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
    store: Optional[str] = None
    """
    (Future reference)
    Use "hosted" to return an audio URL hosted on Substrate. You can also provide a URL to a registered [file store](https://guides.substrate.run/guides/external-file-storage). If unset, the audio data will be returned as a base64-encoded string.
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
class FutureXTTSV2In:
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
    language: str = "en"
    """
    (Future reference)
    Language of input text. Supported languages: `en, de, fr, es, it, pt, pl, zh, ar, cs, ru, nl, tr, hu, ko`.
    """
    store: Optional[str] = None
    """
    (Future reference)
    Use "hosted" to return an audio URL hosted on Substrate. You can also provide a URL to a registered [file store](https://guides.substrate.run/guides/external-file-storage). If unset, the audio data will be returned as a base64-encoded string.
    """


@dataclass
class FutureXTTSV2Out:
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
    collection_name: Optional[str] = None
    """
    (Future reference)
    Vector store name.
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
    model: Literal["jina-v2", "clip"] = "jina-v2"
    """
    (Future reference)
    Selected embedding model.
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
    collection_name: Optional[str] = None
    """
    (Future reference)
    Vector store name.
    """
    embedded_metadata_keys: Optional[List[str]] = None
    """
    (Future reference)
    Choose keys from `metadata` to embed with text.
    """
    model: Literal["jina-v2", "clip"] = "jina-v2"
    """
    (Future reference)
    Selected embedding model.
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
    collection_name: Optional[str] = None
    """
    (Future reference)
    Vector store name.
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
    collection_name: Optional[str] = None
    """
    (Future reference)
    Vector store name.
    """
    doc_id: Optional[str] = None
    """
    (Future reference)
    Vector store document ID. Ignored if `store` is unset.
    """
    model: Literal["clip"] = "clip"
    """
    (Future reference)
    Selected embedding model.
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
    collection_name: Optional[str] = None
    """
    (Future reference)
    Vector store name.
    """
    model: Literal["clip"] = "clip"
    """
    (Future reference)
    Selected embedding model.
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
    collection_name: Optional[str] = None
    """
    (Future reference)
    Vector store name.
    """
    embedded_metadata_keys: Optional[List[str]] = None
    """
    (Future reference)
    Choose keys from `metadata` to embed with text. Only applies to text items.
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
class FutureCreateVectorStoreIn:
    """
    (Future reference)
    """

    collection_name: str
    """
    (Future reference)
    Vector store name.
    """
    model: Literal["jina-v2", "clip"]
    """
    (Future reference)
    Selected embedding model.
    """
    m: int = 16
    """
    (Future reference)
    The max number of connections per layer for the index.
    """
    ef_construction: int = 64
    """
    (Future reference)
    The size of the dynamic candidate list for constructing the index graph.
    """
    metric: Literal["cosine", "l2", "inner"] = "inner"
    """
    (Future reference)
    The distance metric to construct the index with.
    """


@dataclass
class FutureCreateVectorStoreOut:
    """
    (Future reference)
    """

    collection_name: str
    """
    (Future reference)
    Vector store name.
    """
    model: Literal["jina-v2", "clip"]
    """
    (Future reference)
    Selected embedding model.
    """
    m: int
    """
    (Future reference)
    The max number of connections per layer for the index.
    """
    ef_construction: int
    """
    (Future reference)
    The size of the dynamic candidate list for constructing the index graph.
    """
    metric: Literal["cosine", "l2", "inner"]
    """
    (Future reference)
    The distance metric to construct the index with.
    """


@dataclass
class FutureListVectorStoresIn:
    """
    (Future reference)
    """

    pass


@dataclass
class FutureListVectorStoresOut:
    """
    (Future reference)
    """

    items: Optional[List[FutureCreateVectorStoreOut]] = None
    """
    (Future reference)
    List of vector stores.
    """


@dataclass
class FutureDeleteVectorStoreIn:
    """
    (Future reference)
    """

    collection_name: str
    """
    (Future reference)
    Vector store name.
    """
    model: Literal["jina-v2", "clip"]
    """
    (Future reference)
    Selected embedding model.
    """


@dataclass
class FutureDeleteVectorStoreOut:
    """
    (Future reference)
    """

    collection_name: str
    """
    (Future reference)
    Vector store name.
    """
    model: Literal["jina-v2", "clip"]
    """
    (Future reference)
    Selected embedding model.
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
class FutureFetchVectorsIn:
    """
    (Future reference)
    """

    collection_name: str
    """
    (Future reference)
    Vector store name.
    """
    model: Literal["jina-v2", "clip"]
    """
    (Future reference)
    Selected embedding model.
    """
    ids: List[str]
    """
    (Future reference)
    Document IDs to retrieve.
    """


@dataclass
class FutureFetchVectorsOut:
    """
    (Future reference)
    """

    vectors: List[Vector]
    """
    (Future reference)
    Retrieved vectors.
    """


@dataclass
class FutureUpdateVectorsOut:
    """
    (Future reference)
    """

    count: int
    """
    (Future reference)
    Number of vectors modified.
    """


@dataclass
class FutureDeleteVectorsOut:
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
class FutureUpdateVectorsIn:
    """
    (Future reference)
    """

    collection_name: str
    """
    (Future reference)
    Vector store name.
    """
    model: Literal["jina-v2", "clip"]
    """
    (Future reference)
    Selected embedding model.
    """
    vectors: List[UpdateVectorParams]
    """
    (Future reference)
    Vectors to upsert.
    """


@dataclass
class FutureDeleteVectorsIn:
    """
    (Future reference)
    """

    collection_name: str
    """
    (Future reference)
    Vector store name.
    """
    model: Literal["jina-v2", "clip"]
    """
    (Future reference)
    Selected embedding model.
    """
    ids: List[str]
    """
    (Future reference)
    Document IDs to delete.
    """


@dataclass
class FutureQueryVectorStoreIn:
    """
    (Future reference)
    """

    collection_name: str
    """
    (Future reference)
    Vector store to query against.
    """
    model: Literal["jina-v2", "clip"]
    """
    (Future reference)
    Selected embedding model.
    """
    query_strings: Optional[List[str]] = None
    """
    (Future reference)
    Texts to embed and use for the query.
    """
    query_image_uris: Optional[List[str]] = None
    """
    (Future reference)
    Image URIs to embed and use for the query.
    """
    query_vectors: Optional[List[List[float]]] = None
    """
    (Future reference)
    Vectors to use for the query.
    """
    query_ids: Optional[List[str]] = None
    """
    (Future reference)
    Document IDs to use for the query.
    """
    top_k: int = 10
    """
    (Future reference)
    Number of results to return.
    """
    ef_search: int = 40
    """
    (Future reference)
    The size of the dynamic candidate list for searching the index graph.
    """
    include_values: bool = False
    """
    (Future reference)
    Include the values of the vectors in the response.
    """
    include_metadata: bool = False
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
class FutureQueryVectorStoreOut:
    """
    (Future reference)
    """

    results: List[List[VectorStoreQueryResult]]
    """
    (Future reference)
    Query results.
    """
    collection_name: Optional[str] = None
    """
    (Future reference)
    Vector store name.
    """
    model: Optional[Literal["jina-v2", "clip"]] = None
    """
    (Future reference)
    Selected embedding model.
    """
    metric: Optional[Literal["cosine", "l2", "inner"]] = None
    """
    (Future reference)
    The distance metric used for the query.
    """
