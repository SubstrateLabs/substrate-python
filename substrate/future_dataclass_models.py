"""
֍ Substrate
generated file
"""


from __future__ import annotations

from typing import Any, Dict, List, Optional
from dataclasses import dataclass
from typing_extensions import Literal


@dataclass
class ErrorOut:
    """
    Future reference to ErrorOut
    """

    type: Literal["api_error", "invalid_request_error", "dependency_error"]
    """
    (Future reference)
    The type of error returned.
    """
    message: str
    """
    (Future reference)
    A message providing more details about the error.
    """
    status_code: int = 500
    """
    (Future reference)
    The HTTP status code for the error.
    """


@dataclass
class FutureExperimentalIn:
    """
    Future reference to FutureExperimentalIn
    """

    name: str
    """
    (Future reference)
    Identifier.
    """
    args: Dict[str, Any]
    """
    (Future reference)
    Arguments.
    """
    timeout: int = 60
    """
    (Future reference)
    Timeout in seconds.
    """


@dataclass
class FutureExperimentalOut:
    """
    Future reference to FutureExperimentalOut
    """

    output: Dict[str, Any]
    """
    (Future reference)
    Response.
    """


@dataclass
class FutureBoxIn:
    """
    Future reference to FutureBoxIn
    """

    value: Any
    """
    (Future reference)
    Values to box.
    """


@dataclass
class FutureBoxOut:
    """
    Future reference to FutureBoxOut
    """

    value: Any
    """
    (Future reference)
    The evaluated result.
    """


@dataclass
class FutureIfIn:
    """
    Future reference to FutureIfIn
    """

    condition: bool
    """
    (Future reference)
    Condition.
    """
    value_if_true: Any
    """
    (Future reference)
    Result when condition is true.
    """
    value_if_false: Optional[Any] = None
    """
    (Future reference)
    Result when condition is false.
    """


@dataclass
class FutureIfOut:
    """
    Future reference to FutureIfOut
    """

    result: Any
    """
    (Future reference)
    Result. Null if `value_if_false` is not provided and `condition` is false.
    """


@dataclass
class FutureRunPythonIn:
    """
    Future reference to FutureRunPythonIn
    """

    kwargs: Dict[str, Any]
    """
    (Future reference)
    Keyword arguments to your function.
    """
    pkl_function: Optional[str] = None
    """
    (Future reference)
    Pickled function.
    """
    python_version: Optional[str] = None
    """
    (Future reference)
    Python version.
    """
    pip_install: Optional[List[str]] = None
    """
    (Future reference)
    Python packages to install. You must import them in your code.
    """


@dataclass
class FutureRunPythonOut:
    """
    Future reference to FutureRunPythonOut
    """

    stdout: str
    """
    (Future reference)
    Everything printed to stdout while running your code.
    """
    stderr: str
    """
    (Future reference)
    Contents of stderr if your code did not run successfully.
    """
    output: Optional[Any] = None
    """
    (Future reference)
    Return value of your function.
    """
    pkl_output: Optional[str] = None
    """
    (Future reference)
    Pickled return value.
    """


@dataclass
class FutureComputeTextIn:
    """
    Future reference to FutureComputeTextIn
    """

    prompt: str
    """
    (Future reference)
    Input prompt.
    """
    image_uris: Optional[List[str]] = None
    """
    (Future reference)
    Image prompts.
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
    (Future reference)
    Selected model. `Firellava13B` is automatically selected when `image_uris` is provided.
    """


@dataclass
class FutureComputeTextOut:
    """
    Future reference to FutureComputeTextOut
    """

    text: str
    """
    (Future reference)
    Text response.
    """


@dataclass
class FutureComputeJSONIn:
    """
    Future reference to FutureComputeJSONIn
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
    model: Literal["Mistral7BInstruct", "Mixtral8x7BInstruct", "Llama3Instruct8B"] = "Llama3Instruct8B"
    """
    (Future reference)
    Selected model.
    """


@dataclass
class FutureComputeJSONOut:
    """
    Future reference to FutureComputeJSONOut
    """

    json_object: Optional[Dict[str, Any]] = None
    """
    (Future reference)
    JSON response.
    """
    text: Optional[str] = None
    """
    (Future reference)
    If the model output could not be parsed to JSON, this is the raw text output.
    """


@dataclass
class FutureMultiComputeTextIn:
    """
    Future reference to FutureMultiComputeTextIn
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
    model: Literal[
        "Mistral7BInstruct",
        "Mixtral8x7BInstruct",
        "Llama3Instruct8B",
        "Llama3Instruct70B",
    ] = "Llama3Instruct8B"
    """
    (Future reference)
    Selected model.
    """


@dataclass
class FutureMultiComputeTextOut:
    """
    Future reference to FutureMultiComputeTextOut
    """

    choices: List[FutureComputeTextOut]
    """
    (Future reference)
    Response choices.
    """


@dataclass
class FutureBatchComputeTextIn:
    """
    Future reference to FutureBatchComputeTextIn
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
    model: Literal["Mistral7BInstruct", "Llama3Instruct8B"] = "Llama3Instruct8B"
    """
    (Future reference)
    Selected model.
    """


@dataclass
class FutureBatchComputeTextOut:
    """
    Future reference to FutureBatchComputeTextOut
    """

    outputs: List[FutureComputeTextOut]
    """
    (Future reference)
    Batch outputs.
    """


@dataclass
class FutureMultiComputeJSONIn:
    """
    Future reference to FutureMultiComputeJSONIn
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
    model: Literal["Mistral7BInstruct", "Mixtral8x7BInstruct", "Llama3Instruct8B"] = "Llama3Instruct8B"
    """
    (Future reference)
    Selected model.
    """


@dataclass
class FutureMultiComputeJSONOut:
    """
    Future reference to FutureMultiComputeJSONOut
    """

    choices: List[FutureComputeJSONOut]
    """
    (Future reference)
    Response choices.
    """


@dataclass
class FutureBatchComputeJSONIn:
    """
    Future reference to FutureBatchComputeJSONIn
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
    model: Literal["Mistral7BInstruct", "Llama3Instruct8B"] = "Llama3Instruct8B"
    """
    (Future reference)
    Selected model.
    """


@dataclass
class FutureBatchComputeJSONOut:
    """
    Future reference to FutureBatchComputeJSONOut
    """

    outputs: List[FutureComputeJSONOut]
    """
    (Future reference)
    Batch outputs.
    """


@dataclass
class FutureMistral7BInstructIn:
    """
    Future reference to FutureMistral7BInstructIn
    """

    prompt: str
    """
    (Future reference)
    Input prompt.
    """
    system_prompt: Optional[str] = None
    """
    (Future reference)
    System prompt.
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
    Higher values make the output more random, lower values make the output more deterministic.
    """
    frequency_penalty: float = 0.0
    """
    (Future reference)
    Higher values decrease the likelihood of repeating previous tokens.
    """
    repetition_penalty: float = 1.0
    """
    (Future reference)
    Higher values decrease the likelihood of repeated sequences.
    """
    presence_penalty: float = 1.1
    """
    (Future reference)
    Higher values increase the likelihood of new topics appearing.
    """
    top_p: float = 0.95
    """
    (Future reference)
    Probability below which less likely tokens are filtered out.
    """
    max_tokens: Optional[int] = None
    """
    (Future reference)
    Maximum number of tokens to generate.
    """


@dataclass
class Mistral7BInstructChoice:
    """
    Future reference to Mistral7BInstructChoice
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
    Future reference to FutureMistral7BInstructOut
    """

    choices: List[Mistral7BInstructChoice]
    """
    (Future reference)
    Response choices.
    """


@dataclass
class FutureMixtral8x7BInstructIn:
    """
    Future reference to FutureMixtral8x7BInstructIn
    """

    prompt: str
    """
    (Future reference)
    Input prompt.
    """
    system_prompt: Optional[str] = None
    """
    (Future reference)
    System prompt.
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
    Higher values make the output more random, lower values make the output more deterministic.
    """
    frequency_penalty: float = 0.0
    """
    (Future reference)
    Higher values decrease the likelihood of repeating previous tokens.
    """
    repetition_penalty: float = 1.0
    """
    (Future reference)
    Higher values decrease the likelihood of repeated sequences.
    """
    presence_penalty: float = 1.1
    """
    (Future reference)
    Higher values increase the likelihood of new topics appearing.
    """
    top_p: float = 0.95
    """
    (Future reference)
    Probability below which less likely tokens are filtered out.
    """
    max_tokens: Optional[int] = None
    """
    (Future reference)
    Maximum number of tokens to generate.
    """


@dataclass
class Mixtral8x7BChoice:
    """
    Future reference to Mixtral8x7BChoice
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
    Future reference to FutureMixtral8x7BInstructOut
    """

    choices: List[Mixtral8x7BChoice]
    """
    (Future reference)
    Response choices.
    """


@dataclass
class FutureLlama3Instruct8BIn:
    """
    Future reference to FutureLlama3Instruct8BIn
    """

    prompt: str
    """
    (Future reference)
    Input prompt.
    """
    system_prompt: Optional[str] = None
    """
    (Future reference)
    System prompt.
    """
    num_choices: int = 1
    """
    (Future reference)
    Number of choices to generate.
    """
    temperature: Optional[float] = None
    """
    (Future reference)
    Higher values make the output more random, lower values make the output more deterministic.
    """
    frequency_penalty: float = 0.0
    """
    (Future reference)
    Higher values decrease the likelihood of repeating previous tokens.
    """
    repetition_penalty: float = 1.0
    """
    (Future reference)
    Higher values decrease the likelihood of repeated sequences.
    """
    presence_penalty: float = 1.1
    """
    (Future reference)
    Higher values increase the likelihood of new topics appearing.
    """
    top_p: float = 0.95
    """
    (Future reference)
    Probability below which less likely tokens are filtered out.
    """
    max_tokens: Optional[int] = None
    """
    (Future reference)
    Maximum number of tokens to generate.
    """
    json_schema: Optional[Dict[str, Any]] = None
    """
    (Future reference)
    JSON schema to guide response.
    """


@dataclass
class Llama3Instruct8BChoice:
    """
    Future reference to Llama3Instruct8BChoice
    """

    text: Optional[str] = None
    """
    (Future reference)
    Text response.
    """
    json_object: Optional[Dict[str, Any]] = None
    """
    (Future reference)
    JSON response, if `json_schema` was provided.
    """


@dataclass
class FutureLlama3Instruct8BOut:
    """
    Future reference to FutureLlama3Instruct8BOut
    """

    choices: List[Llama3Instruct8BChoice]
    """
    (Future reference)
    Response choices.
    """


@dataclass
class FutureLlama3Instruct70BIn:
    """
    Future reference to FutureLlama3Instruct70BIn
    """

    prompt: str
    """
    (Future reference)
    Input prompt.
    """
    system_prompt: Optional[str] = None
    """
    (Future reference)
    System prompt.
    """
    num_choices: int = 1
    """
    (Future reference)
    Number of choices to generate.
    """
    temperature: Optional[float] = None
    """
    (Future reference)
    Higher values make the output more random, lower values make the output more deterministic.
    """
    frequency_penalty: float = 0.0
    """
    (Future reference)
    Higher values decrease the likelihood of repeating previous tokens.
    """
    repetition_penalty: float = 1.0
    """
    (Future reference)
    Higher values decrease the likelihood of repeated sequences.
    """
    presence_penalty: float = 1.1
    """
    (Future reference)
    Higher values increase the likelihood of new topics appearing.
    """
    top_p: float = 0.95
    """
    (Future reference)
    Probability below which less likely tokens are filtered out.
    """
    max_tokens: Optional[int] = None
    """
    (Future reference)
    Maximum number of tokens to generate.
    """


@dataclass
class Llama3Instruct70BChoice:
    """
    Future reference to Llama3Instruct70BChoice
    """

    text: Optional[str] = None
    """
    (Future reference)
    Text response.
    """


@dataclass
class FutureLlama3Instruct70BOut:
    """
    Future reference to FutureLlama3Instruct70BOut
    """

    choices: List[Llama3Instruct70BChoice]
    """
    (Future reference)
    Response choices.
    """


@dataclass
class FutureFirellava13BIn:
    """
    Future reference to FutureFirellava13BIn
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
    max_tokens: Optional[int] = None
    """
    (Future reference)
    Maximum number of tokens to generate.
    """


@dataclass
class FutureFirellava13BOut:
    """
    Future reference to FutureFirellava13BOut
    """

    text: str
    """
    (Future reference)
    Text response.
    """


@dataclass
class FutureGenerateImageIn:
    """
    Future reference to FutureGenerateImageIn
    """

    prompt: str
    """
    (Future reference)
    Text prompt.
    """
    store: Optional[str] = None
    """
    (Future reference)
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://docs.substrate.run/reference/external-files). If unset, the image data will be returned as a base64-encoded string.
    """


@dataclass
class FutureGenerateImageOut:
    """
    Future reference to FutureGenerateImageOut
    """

    image_uri: str
    """
    (Future reference)
    Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """


@dataclass
class FutureMultiGenerateImageIn:
    """
    Future reference to FutureMultiGenerateImageIn
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
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://docs.substrate.run/reference/external-files). If unset, the image data will be returned as a base64-encoded string.
    """


@dataclass
class FutureMultiGenerateImageOut:
    """
    Future reference to FutureMultiGenerateImageOut
    """

    outputs: List[FutureGenerateImageOut]
    """
    (Future reference)
    Generated images.
    """


@dataclass
class FutureStableDiffusionXLIn:
    """
    Future reference to FutureStableDiffusionXLIn
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
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://docs.substrate.run/reference/external-files). If unset, the image data will be returned as a base64-encoded string.
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
    Future reference to StableDiffusionImage
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
    Future reference to FutureStableDiffusionXLOut
    """

    outputs: List[StableDiffusionImage]
    """
    (Future reference)
    Generated images.
    """


@dataclass
class FutureStableDiffusionXLLightningIn:
    """
    Future reference to FutureStableDiffusionXLLightningIn
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
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://docs.substrate.run/reference/external-files). If unset, the image data will be returned as a base64-encoded string.
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
    Future reference to FutureStableDiffusionXLLightningOut
    """

    outputs: List[StableDiffusionImage]
    """
    (Future reference)
    Generated images.
    """


@dataclass
class FutureStableDiffusionXLIPAdapterIn:
    """
    Future reference to FutureStableDiffusionXLIPAdapterIn
    """

    prompt: str
    """
    (Future reference)
    Text prompt.
    """
    image_prompt_uri: str
    """
    (Future reference)
    Image prompt.
    """
    num_images: int
    """
    (Future reference)
    Number of images to generate.
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
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://docs.substrate.run/reference/external-files). If unset, the image data will be returned as a base64-encoded string.
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
    Future reference to FutureStableDiffusionXLIPAdapterOut
    """

    outputs: List[StableDiffusionImage]
    """
    (Future reference)
    Generated images.
    """


@dataclass
class FutureStableDiffusionXLControlNetIn:
    """
    Future reference to FutureStableDiffusionXLControlNetIn
    """

    image_uri: str
    """
    (Future reference)
    Input image.
    """
    control_method: Literal["edge", "depth", "illusion", "tile"]
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
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://docs.substrate.run/reference/external-files). If unset, the image data will be returned as a base64-encoded string.
    """
    conditioning_scale: float = 0.5
    """
    (Future reference)
    Controls the influence of the input image on the generated output.
    """
    strength: float = 0.5
    """
    (Future reference)
    Controls how much to transform the input image.
    """
    seeds: Optional[List[int]] = None
    """
    (Future reference)
    Random noise seeds. Default is random seeds for each generation.
    """


@dataclass
class FutureStableDiffusionXLControlNetOut:
    """
    Future reference to FutureStableDiffusionXLControlNetOut
    """

    outputs: List[StableDiffusionImage]
    """
    (Future reference)
    Generated images.
    """


@dataclass
class FutureInpaintImageIn:
    """
    Future reference to FutureInpaintImageIn
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
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://docs.substrate.run/reference/external-files). If unset, the image data will be returned as a base64-encoded string.
    """


@dataclass
class FutureInpaintImageOut:
    """
    Future reference to FutureInpaintImageOut
    """

    image_uri: str
    """
    (Future reference)
    Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """


@dataclass
class FutureMultiInpaintImageIn:
    """
    Future reference to FutureMultiInpaintImageIn
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
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://docs.substrate.run/reference/external-files). If unset, the image data will be returned as a base64-encoded string.
    """


@dataclass
class FutureMultiInpaintImageOut:
    """
    Future reference to FutureMultiInpaintImageOut
    """

    outputs: List[FutureInpaintImageOut]
    """
    (Future reference)
    Generated images.
    """


@dataclass
class FutureStableDiffusionXLInpaintIn:
    """
    Future reference to FutureStableDiffusionXLInpaintIn
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
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://docs.substrate.run/reference/external-files). If unset, the image data will be returned as a base64-encoded string.
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
    Future reference to FutureStableDiffusionXLInpaintOut
    """

    outputs: List[StableDiffusionImage]
    """
    (Future reference)
    Generated images.
    """


@dataclass
class BoundingBox:
    """
    Future reference to BoundingBox
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
    Future reference to Point
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
class FutureEraseImageIn:
    """
    Future reference to FutureEraseImageIn
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
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://docs.substrate.run/reference/external-files). If unset, the image data will be returned as a base64-encoded string.
    """


@dataclass
class FutureEraseImageOut:
    """
    Future reference to FutureEraseImageOut
    """

    image_uri: str
    """
    (Future reference)
    Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """


@dataclass
class FutureBigLaMaIn:
    """
    Future reference to FutureBigLaMaIn
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
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://docs.substrate.run/reference/external-files). If unset, the image data will be returned as a base64-encoded string.
    """


@dataclass
class FutureBigLaMaOut:
    """
    Future reference to FutureBigLaMaOut
    """

    image_uri: str
    """
    (Future reference)
    Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """


@dataclass
class FutureRemoveBackgroundIn:
    """
    Future reference to FutureRemoveBackgroundIn
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
    invert_mask: bool = False
    """
    (Future reference)
    Invert the mask image. Only takes effect if `return_mask` is true.
    """
    background_color: Optional[str] = None
    """
    (Future reference)
    Hex value background color. Transparent if unset.
    """
    store: Optional[str] = None
    """
    (Future reference)
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://docs.substrate.run/reference/external-files). If unset, the image data will be returned as a base64-encoded string.
    """


@dataclass
class FutureRemoveBackgroundOut:
    """
    Future reference to FutureRemoveBackgroundOut
    """

    image_uri: str
    """
    (Future reference)
    Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """


@dataclass
class FutureDISISNetIn:
    """
    Future reference to FutureDISISNetIn
    """

    image_uri: str
    """
    (Future reference)
    Input image.
    """
    store: Optional[str] = None
    """
    (Future reference)
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://docs.substrate.run/reference/external-files). If unset, the image data will be returned as a base64-encoded string.
    """


@dataclass
class FutureDISISNetOut:
    """
    Future reference to FutureDISISNetOut
    """

    image_uri: str
    """
    (Future reference)
    Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """


@dataclass
class FutureUpscaleImageIn:
    """
    Future reference to FutureUpscaleImageIn
    """

    image_uri: str
    """
    (Future reference)
    Input image.
    """
    prompt: Optional[str] = None
    """
    (Future reference)
    Prompt to guide model on the content of image to upscale.
    """
    output_resolution: int = 1024
    """
    (Future reference)
    Resolution of the output image, in pixels.
    """
    store: Optional[str] = None
    """
    (Future reference)
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://docs.substrate.run/reference/external-files). If unset, the image data will be returned as a base64-encoded string.
    """


@dataclass
class FutureUpscaleImageOut:
    """
    Future reference to FutureUpscaleImageOut
    """

    image_uri: str
    """
    (Future reference)
    Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """


@dataclass
class FutureSegmentUnderPointIn:
    """
    Future reference to FutureSegmentUnderPointIn
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
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://docs.substrate.run/reference/external-files). If unset, the image data will be returned as a base64-encoded string.
    """


@dataclass
class FutureSegmentUnderPointOut:
    """
    Future reference to FutureSegmentUnderPointOut
    """

    mask_image_uri: str
    """
    (Future reference)
    Detected segments in 'mask image' format. Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """


@dataclass
class FutureSegmentAnythingIn:
    """
    Future reference to FutureSegmentAnythingIn
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
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://docs.substrate.run/reference/external-files). If unset, the image data will be returned as a base64-encoded string.
    """


@dataclass
class FutureSegmentAnythingOut:
    """
    Future reference to FutureSegmentAnythingOut
    """

    mask_image_uri: str
    """
    (Future reference)
    Detected segments in 'mask image' format. Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """


@dataclass
class FutureTranscribeSpeechIn:
    """
    Future reference to FutureTranscribeSpeechIn
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
    Future reference to TranscribedWord
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
    Future reference to TranscribedSegment
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
    Future reference to ChapterMarker
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
class FutureTranscribeSpeechOut:
    """
    Future reference to FutureTranscribeSpeechOut
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
    Future reference to FutureGenerateSpeechIn
    """

    text: str
    """
    (Future reference)
    Input text.
    """
    store: Optional[str] = None
    """
    (Future reference)
    Use "hosted" to return an audio URL hosted on Substrate. You can also provide a URL to a registered [file store](https://docs.substrate.run/reference/external-files). If unset, the audio data will be returned as a base64-encoded string.
    """


@dataclass
class FutureGenerateSpeechOut:
    """
    Future reference to FutureGenerateSpeechOut
    """

    audio_uri: str
    """
    (Future reference)
    Base 64-encoded WAV audio bytes, or a hosted audio url if `store` is provided.
    """


@dataclass
class FutureXTTSV2In:
    """
    Future reference to FutureXTTSV2In
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
    Use "hosted" to return an audio URL hosted on Substrate. You can also provide a URL to a registered [file store](https://docs.substrate.run/reference/external-files). If unset, the audio data will be returned as a base64-encoded string.
    """


@dataclass
class FutureXTTSV2Out:
    """
    Future reference to FutureXTTSV2Out
    """

    audio_uri: str
    """
    (Future reference)
    Base 64-encoded WAV audio bytes, or a hosted audio url if `store` is provided.
    """


@dataclass
class Embedding:
    """
    Future reference to Embedding
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
    Future reference to FutureEmbedTextIn
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
    Metadata that can be used to query the vector store. Ignored if `collection_name` is unset.
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
    Future reference to FutureEmbedTextOut
    """

    embedding: Embedding
    """
    (Future reference)
    Generated embedding.
    """


@dataclass
class EmbedTextItem:
    """
    Future reference to EmbedTextItem
    """

    text: str
    """
    (Future reference)
    Text to embed.
    """
    metadata: Optional[Dict[str, Any]] = None
    """
    (Future reference)
    Metadata that can be used to query the vector store. Ignored if `collection_name` is unset.
    """
    doc_id: Optional[str] = None
    """
    (Future reference)
    Vector store document ID. Ignored if `collection_name` is unset.
    """


@dataclass
class FutureMultiEmbedTextIn:
    """
    Future reference to FutureMultiEmbedTextIn
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
    Future reference to FutureMultiEmbedTextOut
    """

    embeddings: List[Embedding]
    """
    (Future reference)
    Generated embeddings.
    """


@dataclass
class FutureJinaV2In:
    """
    Future reference to FutureJinaV2In
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
    Future reference to FutureJinaV2Out
    """

    embeddings: List[Embedding]
    """
    (Future reference)
    Generated embeddings.
    """


@dataclass
class FutureEmbedImageIn:
    """
    Future reference to FutureEmbedImageIn
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
    Vector store document ID. Ignored if `collection_name` is unset.
    """
    model: Literal["clip"] = "clip"
    """
    (Future reference)
    Selected embedding model.
    """


@dataclass
class FutureEmbedImageOut:
    """
    Future reference to FutureEmbedImageOut
    """

    embedding: Embedding
    """
    (Future reference)
    Generated embedding.
    """


@dataclass
class EmbedImageItem:
    """
    Future reference to EmbedImageItem
    """

    image_uri: str
    """
    (Future reference)
    Image to embed.
    """
    doc_id: Optional[str] = None
    """
    (Future reference)
    Vector store document ID. Ignored if `collection_name` is unset.
    """


@dataclass
class EmbedTextOrImageItem:
    """
    Future reference to EmbedTextOrImageItem
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
    Metadata that can be used to query the vector store. Ignored if `collection_name` is unset.
    """
    doc_id: Optional[str] = None
    """
    (Future reference)
    Vector store document ID. Ignored if `collection_name` is unset.
    """


@dataclass
class FutureMultiEmbedImageIn:
    """
    Future reference to FutureMultiEmbedImageIn
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
    Future reference to FutureMultiEmbedImageOut
    """

    embeddings: List[Embedding]
    """
    (Future reference)
    Generated embeddings.
    """


@dataclass
class FutureCLIPIn:
    """
    Future reference to FutureCLIPIn
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
    Future reference to FutureCLIPOut
    """

    embeddings: List[Embedding]
    """
    (Future reference)
    Generated embeddings.
    """


@dataclass
class FutureFindOrCreateVectorStoreIn:
    """
    Future reference to FutureFindOrCreateVectorStoreIn
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
class FutureFindOrCreateVectorStoreOut:
    """
    Future reference to FutureFindOrCreateVectorStoreOut
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
    num_leaves: Optional[int] = None
    """
    (Future reference)
    Number of leaves in the vector store.
    """


@dataclass
class FutureListVectorStoresIn:
    """
    Future reference to FutureListVectorStoresIn
    """

    pass


@dataclass
class FutureListVectorStoresOut:
    """
    Future reference to FutureListVectorStoresOut
    """

    items: Optional[List[FutureFindOrCreateVectorStoreOut]] = None
    """
    (Future reference)
    List of vector stores.
    """


@dataclass
class FutureDeleteVectorStoreIn:
    """
    Future reference to FutureDeleteVectorStoreIn
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
    Future reference to FutureDeleteVectorStoreOut
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
    Future reference to Vector
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
    Future reference to FutureFetchVectorsIn
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
    Future reference to FutureFetchVectorsOut
    """

    vectors: List[Vector]
    """
    (Future reference)
    Retrieved vectors.
    """


@dataclass
class FutureUpdateVectorsOut:
    """
    Future reference to FutureUpdateVectorsOut
    """

    count: int
    """
    (Future reference)
    Number of vectors modified.
    """


@dataclass
class FutureDeleteVectorsOut:
    """
    Future reference to FutureDeleteVectorsOut
    """

    count: int
    """
    (Future reference)
    Number of vectors modified.
    """


@dataclass
class UpdateVectorParams:
    """
    Future reference to UpdateVectorParams
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
    Future reference to FutureUpdateVectorsIn
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
    Future reference to FutureDeleteVectorsIn
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
    Future reference to FutureQueryVectorStoreIn
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
    num_leaves_to_search: int = 40
    """
    (Future reference)
    The number of leaves in the index tree to search.
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
    Future reference to VectorStoreQueryResult
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
    Future reference to FutureQueryVectorStoreOut
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


@dataclass
class FutureSplitDocumentIn:
    """
    Future reference to FutureSplitDocumentIn
    """

    uri: str
    """
    (Future reference)
    URI of the document.
    """
    doc_id: Optional[str] = None
    """
    (Future reference)
    Document ID.
    """
    metadata: Optional[Dict[str, Any]] = None
    """
    (Future reference)
    Document metadata.
    """
    chunk_size: Optional[int] = None
    """
    (Future reference)
    Maximum number of units per chunk. Defaults to 1024 tokens for text or 40 lines for code.
    """
    chunk_overlap: Optional[int] = None
    """
    (Future reference)
    Number of units to overlap between chunks. Defaults to 200 tokens for text or 15 lines for code.
    """


@dataclass
class FutureSplitDocumentOut:
    """
    Future reference to FutureSplitDocumentOut
    """

    items: List[EmbedTextItem]
    """
    (Future reference)
    Document chunks
    """
