"""
֍ Substrate
generated file
"""


from __future__ import annotations

from typing import Any, Dict, List, Optional
from typing_extensions import Literal, Annotated

from pydantic import Extra, Field, BaseModel


class ErrorOut(BaseModel):
    class Config:
        extra = Extra.allow

    type: Literal["api_error", "invalid_request_error", "dependency_error"]
    """
    The type of error returned.
    """
    message: str
    """
    A message providing more details about the error.
    """
    status_code: int = 500
    """
    The HTTP status code for the error.
    """


class ExperimentalIn(BaseModel):
    class Config:
        extra = Extra.allow

    name: str
    """
    Identifier.
    """
    args: Dict[str, Any]
    """
    Arguments.
    """
    timeout: int = 60
    """
    Timeout in seconds.
    """


class ExperimentalOut(BaseModel):
    class Config:
        extra = Extra.allow

    output: Dict[str, Any]
    """
    Response.
    """


class BoxIn(BaseModel):
    class Config:
        extra = Extra.allow

    value: Any
    """
    Values to box.
    """


class BoxOut(BaseModel):
    class Config:
        extra = Extra.allow

    value: Any
    """
    The evaluated result.
    """


class IfIn(BaseModel):
    class Config:
        extra = Extra.allow

    condition: bool
    """
    Condition.
    """
    value_if_true: Any
    """
    Result when condition is true.
    """
    value_if_false: Optional[Any] = None
    """
    Result when condition is false.
    """


class IfOut(BaseModel):
    class Config:
        extra = Extra.allow

    result: Any
    """
    Result. Null if `value_if_false` is not provided and `condition` is false.
    """


class RunPythonIn(BaseModel):
    class Config:
        extra = Extra.allow

    pkl_function: Optional[str] = None
    """
    Pickled function.
    """
    kwargs: Dict[str, Any]
    """
    Keyword arguments to your function.
    """
    python_version: Optional[str] = None
    """
    Python version.
    """
    pip_install: Optional[List[str]] = None
    """
    Python packages to install. You must import them in your code.
    """


class RunPythonOut(BaseModel):
    class Config:
        extra = Extra.allow

    output: Optional[Any] = None
    """
    Return value of your function.
    """
    pkl_output: Optional[str] = None
    """
    Pickled return value.
    """
    stdout: str
    """
    Everything printed to stdout while running your code.
    """
    stderr: str
    """
    Contents of stderr if your code did not run successfully.
    """


class ComputeTextIn(BaseModel):
    class Config:
        extra = Extra.allow

    prompt: str
    """
    Input prompt.
    """
    image_uris: Optional[List[str]] = None
    """
    Image prompts.
    """
    temperature: Annotated[float, Field(ge=0.0, le=1.0)] = 0.4
    """
    Sampling temperature to use. Higher values make the output more random, lower values make the output more deterministic.
    """
    max_tokens: Optional[int] = None
    """
    Maximum number of tokens to generate.
    """
    model: Literal[
        "Mistral7BInstruct",
        "Mixtral8x7BInstruct",
        "Llama3Instruct8B",
        "Llama3Instruct70B",
        "Firellava13B",
        "gpt-4o",
        "gpt-4o-mini",
        "claude-3-5-sonnet-20240620",
    ] = "Llama3Instruct8B"
    """
    Selected model. `Firellava13B` is automatically selected when `image_uris` is provided.
    """


class ComputeTextOut(BaseModel):
    class Config:
        extra = Extra.allow

    text: str
    """
    Text response.
    """


class ComputeJSONIn(BaseModel):
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
    model: Literal["Mistral7BInstruct", "Mixtral8x7BInstruct", "Llama3Instruct8B"] = "Llama3Instruct8B"
    """
    Selected model.
    """


class ComputeJSONOut(BaseModel):
    class Config:
        extra = Extra.allow

    json_object: Optional[Dict[str, Any]] = None
    """
    JSON response.
    """
    text: Optional[str] = None
    """
    If the model output could not be parsed to JSON, this is the raw text output.
    """


class MultiComputeTextIn(BaseModel):
    class Config:
        extra = Extra.allow

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
    model: Literal[
        "Mistral7BInstruct",
        "Mixtral8x7BInstruct",
        "Llama3Instruct8B",
        "Llama3Instruct70B",
    ] = "Llama3Instruct8B"
    """
    Selected model.
    """


class MultiComputeTextOut(BaseModel):
    class Config:
        extra = Extra.allow

    choices: List[ComputeTextOut]
    """
    Response choices.
    """


class BatchComputeTextIn(BaseModel):
    class Config:
        extra = Extra.allow

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
    model: Literal["Mistral7BInstruct", "Llama3Instruct8B"] = "Llama3Instruct8B"
    """
    Selected model.
    """


class BatchComputeTextOut(BaseModel):
    class Config:
        extra = Extra.allow

    outputs: List[ComputeTextOut]
    """
    Batch outputs.
    """


class MultiComputeJSONIn(BaseModel):
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
    model: Literal["Mistral7BInstruct", "Mixtral8x7BInstruct", "Llama3Instruct8B"] = "Llama3Instruct8B"
    """
    Selected model.
    """


class MultiComputeJSONOut(BaseModel):
    class Config:
        extra = Extra.allow

    choices: List[ComputeJSONOut]
    """
    Response choices.
    """


class BatchComputeJSONIn(BaseModel):
    class Config:
        extra = Extra.allow

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
    model: Literal["Mistral7BInstruct", "Llama3Instruct8B"] = "Llama3Instruct8B"
    """
    Selected model.
    """


class BatchComputeJSONOut(BaseModel):
    class Config:
        extra = Extra.allow

    outputs: List[ComputeJSONOut]
    """
    Batch outputs.
    """


class Mistral7BInstructIn(BaseModel):
    class Config:
        extra = Extra.allow

    prompt: str
    """
    Input prompt.
    """
    system_prompt: Optional[str] = None
    """
    System prompt.
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
    Higher values make the output more random, lower values make the output more deterministic.
    """
    frequency_penalty: Annotated[float, Field(ge=-2.0, le=2.0)] = 0.0
    """
    Higher values decrease the likelihood of repeating previous tokens.
    """
    repetition_penalty: Annotated[float, Field(ge=-2.0, le=2.0)] = 1.0
    """
    Higher values decrease the likelihood of repeated sequences.
    """
    presence_penalty: Annotated[float, Field(ge=-2.0, le=2.0)] = 1.1
    """
    Higher values increase the likelihood of new topics appearing.
    """
    top_p: Annotated[float, Field(ge=0.0, le=1.0)] = 0.95
    """
    Probability below which less likely tokens are filtered out.
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


class Mixtral8x7BInstructIn(BaseModel):
    class Config:
        extra = Extra.allow

    prompt: str
    """
    Input prompt.
    """
    system_prompt: Optional[str] = None
    """
    System prompt.
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
    Higher values make the output more random, lower values make the output more deterministic.
    """
    frequency_penalty: Annotated[float, Field(ge=-2.0, le=2.0)] = 0.0
    """
    Higher values decrease the likelihood of repeating previous tokens.
    """
    repetition_penalty: Annotated[float, Field(ge=-2.0, le=2.0)] = 1.0
    """
    Higher values decrease the likelihood of repeated sequences.
    """
    presence_penalty: Annotated[float, Field(ge=-2.0, le=2.0)] = 1.1
    """
    Higher values increase the likelihood of new topics appearing.
    """
    top_p: Annotated[float, Field(ge=0.0, le=1.0)] = 0.95
    """
    Probability below which less likely tokens are filtered out.
    """
    max_tokens: Optional[int] = None
    """
    Maximum number of tokens to generate.
    """


class Mixtral8x7BChoice(BaseModel):
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


class Mixtral8x7BInstructOut(BaseModel):
    class Config:
        extra = Extra.allow

    choices: List[Mixtral8x7BChoice]
    """
    Response choices.
    """


class Llama3Instruct8BIn(BaseModel):
    class Config:
        extra = Extra.allow

    prompt: str
    """
    Input prompt.
    """
    system_prompt: Optional[str] = None
    """
    System prompt.
    """
    num_choices: Annotated[int, Field(ge=1, le=8)] = 1
    """
    Number of choices to generate.
    """
    temperature: Annotated[Optional[float], Field(ge=0.0, le=1.0)] = None
    """
    Higher values make the output more random, lower values make the output more deterministic.
    """
    frequency_penalty: Annotated[float, Field(ge=-2.0, le=2.0)] = 0.0
    """
    Higher values decrease the likelihood of repeating previous tokens.
    """
    repetition_penalty: Annotated[float, Field(ge=-2.0, le=2.0)] = 1.0
    """
    Higher values decrease the likelihood of repeated sequences.
    """
    presence_penalty: Annotated[float, Field(ge=-2.0, le=2.0)] = 1.1
    """
    Higher values increase the likelihood of new topics appearing.
    """
    top_p: Annotated[float, Field(ge=0.0, le=1.0)] = 0.95
    """
    Probability below which less likely tokens are filtered out.
    """
    max_tokens: Optional[int] = None
    """
    Maximum number of tokens to generate.
    """
    json_schema: Optional[Dict[str, Any]] = None
    """
    JSON schema to guide response.
    """


class Llama3Instruct8BChoice(BaseModel):
    class Config:
        extra = Extra.allow

    text: Optional[str] = None
    """
    Text response.
    """
    json_object: Optional[Dict[str, Any]] = None
    """
    JSON response, if `json_schema` was provided.
    """


class Llama3Instruct8BOut(BaseModel):
    class Config:
        extra = Extra.allow

    choices: List[Llama3Instruct8BChoice]
    """
    Response choices.
    """


class Llama3Instruct70BIn(BaseModel):
    class Config:
        extra = Extra.allow

    prompt: str
    """
    Input prompt.
    """
    system_prompt: Optional[str] = None
    """
    System prompt.
    """
    num_choices: Annotated[int, Field(ge=1, le=8)] = 1
    """
    Number of choices to generate.
    """
    temperature: Annotated[Optional[float], Field(ge=0.0, le=1.0)] = None
    """
    Higher values make the output more random, lower values make the output more deterministic.
    """
    frequency_penalty: Annotated[float, Field(ge=-2.0, le=2.0)] = 0.0
    """
    Higher values decrease the likelihood of repeating previous tokens.
    """
    repetition_penalty: Annotated[float, Field(ge=-2.0, le=2.0)] = 1.0
    """
    Higher values decrease the likelihood of repeated sequences.
    """
    presence_penalty: Annotated[float, Field(ge=-2.0, le=2.0)] = 1.1
    """
    Higher values increase the likelihood of new topics appearing.
    """
    top_p: Annotated[float, Field(ge=0.0, le=1.0)] = 0.95
    """
    Probability below which less likely tokens are filtered out.
    """
    max_tokens: Optional[int] = None
    """
    Maximum number of tokens to generate.
    """


class Llama3Instruct70BChoice(BaseModel):
    class Config:
        extra = Extra.allow

    text: Optional[str] = None
    """
    Text response.
    """


class Llama3Instruct70BOut(BaseModel):
    class Config:
        extra = Extra.allow

    choices: List[Llama3Instruct70BChoice]
    """
    Response choices.
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
    max_tokens: Optional[int] = None
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
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://docs.substrate.run/reference/external-files). If unset, the image data will be returned as a base64-encoded string.
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
    num_images: Annotated[int, Field(ge=1, le=8)]
    """
    Number of images to generate.
    """
    store: Optional[str] = None
    """
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://docs.substrate.run/reference/external-files). If unset, the image data will be returned as a base64-encoded string.
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
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://docs.substrate.run/reference/external-files). If unset, the image data will be returned as a base64-encoded string.
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
    num_images: Annotated[int, Field(ge=1, le=8)] = 1
    """
    Number of images to generate.
    """
    store: Optional[str] = None
    """
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://docs.substrate.run/reference/external-files). If unset, the image data will be returned as a base64-encoded string.
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
    image_prompt_uri: str
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
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://docs.substrate.run/reference/external-files). If unset, the image data will be returned as a base64-encoded string.
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
    control_method: Literal["edge", "depth", "illusion", "tile"]
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
    output_resolution: Annotated[int, Field(ge=512, le=2048)] = 1024
    """
    Resolution of the output image, in pixels.
    """
    negative_prompt: Optional[str] = None
    """
    Negative input prompt.
    """
    store: Optional[str] = None
    """
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://docs.substrate.run/reference/external-files). If unset, the image data will be returned as a base64-encoded string.
    """
    conditioning_scale: Annotated[float, Field(ge=0.0, le=1.0)] = 0.5
    """
    Controls the influence of the input image on the generated output.
    """
    strength: Annotated[float, Field(ge=0.0, le=1.0)] = 0.5
    """
    Controls how much to transform the input image.
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


class InpaintImageIn(BaseModel):
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
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://docs.substrate.run/reference/external-files). If unset, the image data will be returned as a base64-encoded string.
    """


class InpaintImageOut(BaseModel):
    class Config:
        extra = Extra.allow

    image_uri: str
    """
    Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """


class MultiInpaintImageIn(BaseModel):
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
    num_images: Annotated[int, Field(ge=1, le=8)]
    """
    Number of images to generate.
    """
    store: Optional[str] = None
    """
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://docs.substrate.run/reference/external-files). If unset, the image data will be returned as a base64-encoded string.
    """


class MultiInpaintImageOut(BaseModel):
    class Config:
        extra = Extra.allow

    outputs: List[InpaintImageOut]
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
    num_images: Annotated[int, Field(ge=1, le=8)]
    """
    Number of images to generate.
    """
    output_resolution: Annotated[int, Field(ge=512, le=2048)] = 1024
    """
    Resolution of the output image, in pixels.
    """
    negative_prompt: Optional[str] = None
    """
    Negative input prompt.
    """
    store: Optional[str] = None
    """
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://docs.substrate.run/reference/external-files). If unset, the image data will be returned as a base64-encoded string.
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


class EraseImageIn(BaseModel):
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
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://docs.substrate.run/reference/external-files). If unset, the image data will be returned as a base64-encoded string.
    """


class EraseImageOut(BaseModel):
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
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://docs.substrate.run/reference/external-files). If unset, the image data will be returned as a base64-encoded string.
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
    invert_mask: bool = False
    """
    Invert the mask image. Only takes effect if `return_mask` is true.
    """
    background_color: Optional[str] = None
    """
    Hex value background color. Transparent if unset.
    """
    store: Optional[str] = None
    """
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://docs.substrate.run/reference/external-files). If unset, the image data will be returned as a base64-encoded string.
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
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://docs.substrate.run/reference/external-files). If unset, the image data will be returned as a base64-encoded string.
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

    prompt: Optional[str] = None
    """
    Prompt to guide model on the content of image to upscale.
    """
    image_uri: str
    """
    Input image.
    """
    output_resolution: Annotated[int, Field(ge=512, le=2048)] = 1024
    """
    Resolution of the output image, in pixels.
    """
    store: Optional[str] = None
    """
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://docs.substrate.run/reference/external-files). If unset, the image data will be returned as a base64-encoded string.
    """


class UpscaleImageOut(BaseModel):
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
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://docs.substrate.run/reference/external-files). If unset, the image data will be returned as a base64-encoded string.
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
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://docs.substrate.run/reference/external-files). If unset, the image data will be returned as a base64-encoded string.
    """


class SegmentAnythingOut(BaseModel):
    class Config:
        extra = Extra.allow

    mask_image_uri: str
    """
    Detected segments in 'mask image' format. Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """


class TranscribeSpeechIn(BaseModel):
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


class TranscribeSpeechOut(BaseModel):
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
    Use "hosted" to return an audio URL hosted on Substrate. You can also provide a URL to a registered [file store](https://docs.substrate.run/reference/external-files). If unset, the audio data will be returned as a base64-encoded string.
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
    Use "hosted" to return an audio URL hosted on Substrate. You can also provide a URL to a registered [file store](https://docs.substrate.run/reference/external-files). If unset, the audio data will be returned as a base64-encoded string.
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
    collection_name: Optional[str] = None
    """
    Vector store name.
    """
    metadata: Optional[Dict[str, Any]] = None
    """
    Metadata that can be used to query the vector store. Ignored if `collection_name` is unset.
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
    Metadata that can be used to query the vector store. Ignored if `collection_name` is unset.
    """
    doc_id: Optional[str] = None
    """
    Vector store document ID. Ignored if `collection_name` is unset.
    """


class MultiEmbedTextIn(BaseModel):
    class Config:
        extra = Extra.allow

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
    collection_name: Optional[str] = None
    """
    Vector store name.
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
    collection_name: Optional[str] = None
    """
    Vector store name.
    """
    doc_id: Optional[str] = None
    """
    Vector store document ID. Ignored if `collection_name` is unset.
    """
    model: Literal["clip"] = "clip"
    """
    Selected embedding model.
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
    Vector store document ID. Ignored if `collection_name` is unset.
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
    Metadata that can be used to query the vector store. Ignored if `collection_name` is unset.
    """
    doc_id: Optional[str] = None
    """
    Vector store document ID. Ignored if `collection_name` is unset.
    """


class MultiEmbedImageIn(BaseModel):
    class Config:
        extra = Extra.allow

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
    collection_name: Optional[str] = None
    """
    Vector store name.
    """
    embedded_metadata_keys: Optional[List[str]] = None
    """
    Choose keys from `metadata` to embed with text. Only applies to text items.
    """


class CLIPOut(BaseModel):
    class Config:
        extra = Extra.allow

    embeddings: List[Embedding]
    """
    Generated embeddings.
    """


class FindOrCreateVectorStoreIn(BaseModel):
    class Config:
        extra = Extra.allow

    collection_name: Annotated[str, Field(max_length=63, min_length=1)]
    """
    Vector store name.
    """
    model: Literal["jina-v2", "clip"]
    """
    Selected embedding model.
    """


class FindOrCreateVectorStoreOut(BaseModel):
    class Config:
        extra = Extra.allow

    collection_name: Annotated[str, Field(max_length=63, min_length=1)]
    """
    Vector store name.
    """
    model: Literal["jina-v2", "clip"]
    """
    Selected embedding model.
    """
    num_leaves: Annotated[Optional[int], Field(ge=1)] = None
    """
    Number of leaves in the vector store.
    """


class ListVectorStoresIn(BaseModel):
    pass

    class Config:
        extra = Extra.allow


class ListVectorStoresOut(BaseModel):
    class Config:
        extra = Extra.allow

    items: Optional[List[FindOrCreateVectorStoreOut]] = None
    """
    List of vector stores.
    """


class DeleteVectorStoreIn(BaseModel):
    class Config:
        extra = Extra.allow

    collection_name: str
    """
    Vector store name.
    """
    model: Literal["jina-v2", "clip"]
    """
    Selected embedding model.
    """


class DeleteVectorStoreOut(BaseModel):
    class Config:
        extra = Extra.allow

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
    class Config:
        extra = Extra.allow

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
    class Config:
        extra = Extra.allow

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
    num_leaves_to_search: Annotated[int, Field(ge=1, le=1000)] = 40
    """
    The number of leaves in the index tree to search.
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
    collection_name: Optional[str] = None
    """
    Vector store name.
    """
    model: Optional[Literal["jina-v2", "clip"]] = None
    """
    Selected embedding model.
    """


class SplitDocumentIn(BaseModel):
    class Config:
        extra = Extra.allow

    uri: str
    """
    URI of the document.
    """
    doc_id: Optional[str] = None
    """
    Document ID.
    """
    metadata: Optional[Dict[str, Any]] = None
    """
    Document metadata.
    """
    chunk_size: Annotated[Optional[int], Field(ge=1)] = None
    """
    Maximum number of units per chunk. Defaults to 1024 tokens for text or 40 lines for code.
    """
    chunk_overlap: Annotated[Optional[int], Field(ge=0)] = None
    """
    Number of units to overlap between chunks. Defaults to 200 tokens for text or 15 lines for code.
    """


class SplitDocumentOut(BaseModel):
    class Config:
        extra = Extra.allow

    items: List[EmbedTextItem]
    """
    Document chunks
    """
