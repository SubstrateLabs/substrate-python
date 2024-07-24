"""
֍ Substrate
generated file
"""


from __future__ import annotations

from typing import Any, Dict, List
from typing_extensions import Literal, TypedDict, NotRequired


class ErrorOut(TypedDict):
    type: NotRequired[Literal["api_error", "invalid_request_error", "dependency_error"]]
    """
    The type of error returned.
    """
    message: NotRequired[str]
    """
    A message providing more details about the error.
    """
    status_code: NotRequired[int]
    """
    The HTTP status code for the error.
    """


class ExperimentalIn(TypedDict):
    name: NotRequired[str]
    """
    Identifier.
    """
    args: NotRequired[Dict[str, Any]]
    """
    Arguments.
    """
    timeout: NotRequired[int]
    """
    Timeout in seconds.
    """


class ExperimentalOut(TypedDict):
    output: NotRequired[Dict[str, Any]]
    """
    Response.
    """


class BoxIn(TypedDict):
    value: NotRequired[Any]
    """
    Values to box.
    """


class BoxOut(TypedDict):
    value: NotRequired[Any]
    """
    The evaluated result.
    """


class IfIn(TypedDict):
    condition: NotRequired[bool]
    """
    Condition.
    """
    value_if_true: NotRequired[Any]
    """
    Result when condition is true.
    """
    value_if_false: NotRequired[Any]
    """
    Result when condition is false.
    """


class IfOut(TypedDict):
    result: NotRequired[Any]
    """
    Result. Null if `value_if_false` is not provided and `condition` is false.
    """


class RunPythonIn(TypedDict):
    pkl_function: NotRequired[str]
    """
    Pickled function.
    """
    kwargs: NotRequired[Dict[str, Any]]
    """
    Keyword arguments to your function.
    """
    python_version: NotRequired[str]
    """
    Python version.
    """
    pip_install: NotRequired[List[str]]
    """
    Python packages to install. You must import them in your code.
    """


class RunPythonOut(TypedDict):
    output: NotRequired[Any]
    """
    Return value of your function.
    """
    pkl_output: NotRequired[str]
    """
    Pickled return value.
    """
    stdout: NotRequired[str]
    """
    Everything printed to stdout while running your code.
    """
    stderr: NotRequired[str]
    """
    Contents of stderr if your code did not run successfully.
    """


class ComputeTextIn(TypedDict):
    prompt: NotRequired[str]
    """
    Input prompt.
    """
    image_uris: NotRequired[List[str]]
    """
    Image prompts.
    """
    temperature: NotRequired[float]
    """
    Sampling temperature to use. Higher values make the output more random, lower values make the output more deterministic.
    """
    max_tokens: NotRequired[int]
    """
    Maximum number of tokens to generate.
    """
    model: NotRequired[
        Literal[
            "Mistral7BInstruct",
            "Mixtral8x7BInstruct",
            "Llama3Instruct8B",
            "Llama3Instruct70B",
            "Firellava13B",
            "gpt-4o",
            "gpt-4o-mini",
            "claude-3-5-sonnet-20240620",
        ]
    ]
    """
    Selected model. `Firellava13B` is automatically selected when `image_uris` is provided.
    """


class ComputeTextOut(TypedDict):
    text: NotRequired[str]
    """
    Text response.
    """


class ComputeJSONIn(TypedDict):
    prompt: NotRequired[str]
    """
    Input prompt.
    """
    json_schema: NotRequired[Dict[str, Any]]
    """
    JSON schema to guide `json_object` response.
    """
    temperature: NotRequired[float]
    """
    Sampling temperature to use. Higher values make the output more random, lower values make the output more deterministic.
    """
    max_tokens: NotRequired[int]
    """
    Maximum number of tokens to generate.
    """
    model: NotRequired[Literal["Mistral7BInstruct", "Mixtral8x7BInstruct", "Llama3Instruct8B"]]
    """
    Selected model.
    """


class ComputeJSONOut(TypedDict):
    json_object: NotRequired[Dict[str, Any]]
    """
    JSON response.
    """
    text: NotRequired[str]
    """
    If the model output could not be parsed to JSON, this is the raw text output.
    """


class MultiComputeTextIn(TypedDict):
    prompt: NotRequired[str]
    """
    Input prompt.
    """
    num_choices: NotRequired[int]
    """
    Number of choices to generate.
    """
    temperature: NotRequired[float]
    """
    Sampling temperature to use. Higher values make the output more random, lower values make the output more deterministic.
    """
    max_tokens: NotRequired[int]
    """
    Maximum number of tokens to generate.
    """
    model: NotRequired[
        Literal[
            "Mistral7BInstruct",
            "Mixtral8x7BInstruct",
            "Llama3Instruct8B",
            "Llama3Instruct70B",
        ]
    ]
    """
    Selected model.
    """


class MultiComputeTextOut(TypedDict):
    choices: NotRequired[List[ComputeTextOut]]
    """
    Response choices.
    """


class BatchComputeTextIn(TypedDict):
    prompts: NotRequired[List[str]]
    """
    Batch input prompts.
    """
    temperature: NotRequired[float]
    """
    Sampling temperature to use. Higher values make the output more random, lower values make the output more deterministic.
    """
    max_tokens: NotRequired[int]
    """
    Maximum number of tokens to generate.
    """
    model: NotRequired[Literal["Mistral7BInstruct", "Llama3Instruct8B"]]
    """
    Selected model.
    """


class BatchComputeTextOut(TypedDict):
    outputs: NotRequired[List[ComputeTextOut]]
    """
    Batch outputs.
    """


class MultiComputeJSONIn(TypedDict):
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
    temperature: NotRequired[float]
    """
    Sampling temperature to use. Higher values make the output more random, lower values make the output more deterministic.
    """
    max_tokens: NotRequired[int]
    """
    Maximum number of tokens to generate.
    """
    model: NotRequired[Literal["Mistral7BInstruct", "Mixtral8x7BInstruct", "Llama3Instruct8B"]]
    """
    Selected model.
    """


class MultiComputeJSONOut(TypedDict):
    choices: NotRequired[List[ComputeJSONOut]]
    """
    Response choices.
    """


class BatchComputeJSONIn(TypedDict):
    prompts: NotRequired[List[str]]
    """
    Batch input prompts.
    """
    json_schema: NotRequired[Dict[str, Any]]
    """
    JSON schema to guide `json_object` response.
    """
    temperature: NotRequired[float]
    """
    Sampling temperature to use. Higher values make the output more random, lower values make the output more deterministic.
    """
    max_tokens: NotRequired[int]
    """
    Maximum number of tokens to generate.
    """
    model: NotRequired[Literal["Mistral7BInstruct", "Llama3Instruct8B"]]
    """
    Selected model.
    """


class BatchComputeJSONOut(TypedDict):
    outputs: NotRequired[List[ComputeJSONOut]]
    """
    Batch outputs.
    """


class Mistral7BInstructIn(TypedDict):
    prompt: NotRequired[str]
    """
    Input prompt.
    """
    system_prompt: NotRequired[str]
    """
    System prompt.
    """
    num_choices: NotRequired[int]
    """
    Number of choices to generate.
    """
    json_schema: NotRequired[Dict[str, Any]]
    """
    JSON schema to guide response.
    """
    temperature: NotRequired[float]
    """
    Higher values make the output more random, lower values make the output more deterministic.
    """
    frequency_penalty: NotRequired[float]
    """
    Higher values decrease the likelihood of repeating previous tokens.
    """
    repetition_penalty: NotRequired[float]
    """
    Higher values decrease the likelihood of repeated sequences.
    """
    presence_penalty: NotRequired[float]
    """
    Higher values increase the likelihood of new topics appearing.
    """
    top_p: NotRequired[float]
    """
    Probability below which less likely tokens are filtered out.
    """
    max_tokens: NotRequired[int]
    """
    Maximum number of tokens to generate.
    """


class Mistral7BInstructChoice(TypedDict):
    text: NotRequired[str]
    """
    Text response, if `json_schema` was not provided.
    """
    json_object: NotRequired[Dict[str, Any]]
    """
    JSON response, if `json_schema` was provided.
    """


class Mistral7BInstructOut(TypedDict):
    choices: NotRequired[List[Mistral7BInstructChoice]]
    """
    Response choices.
    """


class Mixtral8x7BInstructIn(TypedDict):
    prompt: NotRequired[str]
    """
    Input prompt.
    """
    system_prompt: NotRequired[str]
    """
    System prompt.
    """
    num_choices: NotRequired[int]
    """
    Number of choices to generate.
    """
    json_schema: NotRequired[Dict[str, Any]]
    """
    JSON schema to guide response.
    """
    temperature: NotRequired[float]
    """
    Higher values make the output more random, lower values make the output more deterministic.
    """
    frequency_penalty: NotRequired[float]
    """
    Higher values decrease the likelihood of repeating previous tokens.
    """
    repetition_penalty: NotRequired[float]
    """
    Higher values decrease the likelihood of repeated sequences.
    """
    presence_penalty: NotRequired[float]
    """
    Higher values increase the likelihood of new topics appearing.
    """
    top_p: NotRequired[float]
    """
    Probability below which less likely tokens are filtered out.
    """
    max_tokens: NotRequired[int]
    """
    Maximum number of tokens to generate.
    """


class Mixtral8x7BChoice(TypedDict):
    text: NotRequired[str]
    """
    Text response, if `json_schema` was not provided.
    """
    json_object: NotRequired[Dict[str, Any]]
    """
    JSON response, if `json_schema` was provided.
    """


class Mixtral8x7BInstructOut(TypedDict):
    choices: NotRequired[List[Mixtral8x7BChoice]]
    """
    Response choices.
    """


class Llama3Instruct8BIn(TypedDict):
    prompt: NotRequired[str]
    """
    Input prompt.
    """
    system_prompt: NotRequired[str]
    """
    System prompt.
    """
    num_choices: NotRequired[int]
    """
    Number of choices to generate.
    """
    temperature: NotRequired[float]
    """
    Higher values make the output more random, lower values make the output more deterministic.
    """
    frequency_penalty: NotRequired[float]
    """
    Higher values decrease the likelihood of repeating previous tokens.
    """
    repetition_penalty: NotRequired[float]
    """
    Higher values decrease the likelihood of repeated sequences.
    """
    presence_penalty: NotRequired[float]
    """
    Higher values increase the likelihood of new topics appearing.
    """
    top_p: NotRequired[float]
    """
    Probability below which less likely tokens are filtered out.
    """
    max_tokens: NotRequired[int]
    """
    Maximum number of tokens to generate.
    """
    json_schema: NotRequired[Dict[str, Any]]
    """
    JSON schema to guide response.
    """


class Llama3Instruct8BChoice(TypedDict):
    text: NotRequired[str]
    """
    Text response.
    """
    json_object: NotRequired[Dict[str, Any]]
    """
    JSON response, if `json_schema` was provided.
    """


class Llama3Instruct8BOut(TypedDict):
    choices: NotRequired[List[Llama3Instruct8BChoice]]
    """
    Response choices.
    """


class Llama3Instruct70BIn(TypedDict):
    prompt: NotRequired[str]
    """
    Input prompt.
    """
    system_prompt: NotRequired[str]
    """
    System prompt.
    """
    num_choices: NotRequired[int]
    """
    Number of choices to generate.
    """
    temperature: NotRequired[float]
    """
    Higher values make the output more random, lower values make the output more deterministic.
    """
    frequency_penalty: NotRequired[float]
    """
    Higher values decrease the likelihood of repeating previous tokens.
    """
    repetition_penalty: NotRequired[float]
    """
    Higher values decrease the likelihood of repeated sequences.
    """
    presence_penalty: NotRequired[float]
    """
    Higher values increase the likelihood of new topics appearing.
    """
    top_p: NotRequired[float]
    """
    Probability below which less likely tokens are filtered out.
    """
    max_tokens: NotRequired[int]
    """
    Maximum number of tokens to generate.
    """


class Llama3Instruct70BChoice(TypedDict):
    text: NotRequired[str]
    """
    Text response.
    """


class Llama3Instruct70BOut(TypedDict):
    choices: NotRequired[List[Llama3Instruct70BChoice]]
    """
    Response choices.
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
    max_tokens: NotRequired[int]
    """
    Maximum number of tokens to generate.
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
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://docs.substrate.run/reference/external-files). If unset, the image data will be returned as a base64-encoded string.
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
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://docs.substrate.run/reference/external-files). If unset, the image data will be returned as a base64-encoded string.
    """


class MultiGenerateImageOut(TypedDict):
    outputs: NotRequired[List[GenerateImageOut]]
    """
    Generated images.
    """


class StableDiffusionXLIn(TypedDict):
    prompt: NotRequired[str]
    """
    Text prompt.
    """
    negative_prompt: NotRequired[str]
    """
    Negative input prompt.
    """
    steps: NotRequired[int]
    """
    Number of diffusion steps.
    """
    num_images: NotRequired[int]
    """
    Number of images to generate.
    """
    store: NotRequired[str]
    """
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://docs.substrate.run/reference/external-files). If unset, the image data will be returned as a base64-encoded string.
    """
    height: NotRequired[int]
    """
    Height of output image, in pixels.
    """
    width: NotRequired[int]
    """
    Width of output image, in pixels.
    """
    seeds: NotRequired[List[int]]
    """
    Seeds for deterministic generation. Default is a random seed.
    """
    guidance_scale: NotRequired[float]
    """
    Higher values adhere to the text prompt more strongly, typically at the expense of image quality.
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
    """
    Generated images.
    """


class StableDiffusionXLLightningIn(TypedDict):
    prompt: NotRequired[str]
    """
    Text prompt.
    """
    negative_prompt: NotRequired[str]
    """
    Negative input prompt.
    """
    num_images: NotRequired[int]
    """
    Number of images to generate.
    """
    store: NotRequired[str]
    """
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://docs.substrate.run/reference/external-files). If unset, the image data will be returned as a base64-encoded string.
    """
    height: NotRequired[int]
    """
    Height of output image, in pixels.
    """
    width: NotRequired[int]
    """
    Width of output image, in pixels.
    """
    seeds: NotRequired[List[int]]
    """
    Seeds for deterministic generation. Default is a random seed.
    """


class StableDiffusionXLLightningOut(TypedDict):
    outputs: NotRequired[List[StableDiffusionImage]]
    """
    Generated images.
    """


class StableDiffusionXLIPAdapterIn(TypedDict):
    prompt: NotRequired[str]
    """
    Text prompt.
    """
    image_prompt_uri: NotRequired[str]
    """
    Image prompt.
    """
    num_images: NotRequired[int]
    """
    Number of images to generate.
    """
    ip_adapter_scale: NotRequired[float]
    """
    Controls the influence of the image prompt on the generated output.
    """
    negative_prompt: NotRequired[str]
    """
    Negative input prompt.
    """
    store: NotRequired[str]
    """
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://docs.substrate.run/reference/external-files). If unset, the image data will be returned as a base64-encoded string.
    """
    width: NotRequired[int]
    """
    Width of output image, in pixels.
    """
    height: NotRequired[int]
    """
    Height of output image, in pixels.
    """
    seeds: NotRequired[List[int]]
    """
    Random noise seeds. Default is random seeds for each generation.
    """


class StableDiffusionXLIPAdapterOut(TypedDict):
    outputs: NotRequired[List[StableDiffusionImage]]
    """
    Generated images.
    """


class StableDiffusionXLControlNetIn(TypedDict):
    image_uri: NotRequired[str]
    """
    Input image.
    """
    control_method: NotRequired[Literal["edge", "depth", "illusion", "tile"]]
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
    Resolution of the output image, in pixels.
    """
    negative_prompt: NotRequired[str]
    """
    Negative input prompt.
    """
    store: NotRequired[str]
    """
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://docs.substrate.run/reference/external-files). If unset, the image data will be returned as a base64-encoded string.
    """
    conditioning_scale: NotRequired[float]
    """
    Controls the influence of the input image on the generated output.
    """
    strength: NotRequired[float]
    """
    Controls how much to transform the input image.
    """
    seeds: NotRequired[List[int]]
    """
    Random noise seeds. Default is random seeds for each generation.
    """


class StableDiffusionXLControlNetOut(TypedDict):
    outputs: NotRequired[List[StableDiffusionImage]]
    """
    Generated images.
    """


class InpaintImageIn(TypedDict):
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
    Mask image that controls which pixels are inpainted. If unset, the entire image is edited (image-to-image).
    """
    store: NotRequired[str]
    """
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://docs.substrate.run/reference/external-files). If unset, the image data will be returned as a base64-encoded string.
    """


class InpaintImageOut(TypedDict):
    image_uri: NotRequired[str]
    """
    Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """


class MultiInpaintImageIn(TypedDict):
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
    Mask image that controls which pixels are edited (inpainting). If unset, the entire image is edited (image-to-image).
    """
    num_images: NotRequired[int]
    """
    Number of images to generate.
    """
    store: NotRequired[str]
    """
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://docs.substrate.run/reference/external-files). If unset, the image data will be returned as a base64-encoded string.
    """


class MultiInpaintImageOut(TypedDict):
    outputs: NotRequired[List[InpaintImageOut]]
    """
    Generated images.
    """


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
    Mask image that controls which pixels are edited (inpainting). If unset, the entire image is edited (image-to-image).
    """
    num_images: NotRequired[int]
    """
    Number of images to generate.
    """
    output_resolution: NotRequired[int]
    """
    Resolution of the output image, in pixels.
    """
    negative_prompt: NotRequired[str]
    """
    Negative input prompt.
    """
    store: NotRequired[str]
    """
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://docs.substrate.run/reference/external-files). If unset, the image data will be returned as a base64-encoded string.
    """
    strength: NotRequired[float]
    """
    Controls the strength of the generation process.
    """
    seeds: NotRequired[List[int]]
    """
    Random noise seeds. Default is random seeds for each generation.
    """


class StableDiffusionXLInpaintOut(TypedDict):
    outputs: NotRequired[List[StableDiffusionImage]]
    """
    Generated images.
    """


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


class EraseImageIn(TypedDict):
    image_uri: NotRequired[str]
    """
    Input image.
    """
    mask_image_uri: NotRequired[str]
    """
    Mask image that controls which pixels are inpainted.
    """
    store: NotRequired[str]
    """
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://docs.substrate.run/reference/external-files). If unset, the image data will be returned as a base64-encoded string.
    """


class EraseImageOut(TypedDict):
    image_uri: NotRequired[str]
    """
    Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """


class BigLaMaIn(TypedDict):
    image_uri: NotRequired[str]
    """
    Input image.
    """
    mask_image_uri: NotRequired[str]
    """
    Mask image that controls which pixels are inpainted.
    """
    store: NotRequired[str]
    """
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://docs.substrate.run/reference/external-files). If unset, the image data will be returned as a base64-encoded string.
    """


class BigLaMaOut(TypedDict):
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
    Return a mask image instead of the original content.
    """
    invert_mask: NotRequired[bool]
    """
    Invert the mask image. Only takes effect if `return_mask` is true.
    """
    background_color: NotRequired[str]
    """
    Hex value background color. Transparent if unset.
    """
    store: NotRequired[str]
    """
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://docs.substrate.run/reference/external-files). If unset, the image data will be returned as a base64-encoded string.
    """


class RemoveBackgroundOut(TypedDict):
    image_uri: NotRequired[str]
    """
    Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """


class DISISNetIn(TypedDict):
    image_uri: NotRequired[str]
    """
    Input image.
    """
    store: NotRequired[str]
    """
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://docs.substrate.run/reference/external-files). If unset, the image data will be returned as a base64-encoded string.
    """


class DISISNetOut(TypedDict):
    image_uri: NotRequired[str]
    """
    Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """


class UpscaleImageIn(TypedDict):
    prompt: NotRequired[str]
    """
    Prompt to guide model on the content of image to upscale.
    """
    image_uri: NotRequired[str]
    """
    Input image.
    """
    output_resolution: NotRequired[int]
    """
    Resolution of the output image, in pixels.
    """
    store: NotRequired[str]
    """
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://docs.substrate.run/reference/external-files). If unset, the image data will be returned as a base64-encoded string.
    """


class UpscaleImageOut(TypedDict):
    image_uri: NotRequired[str]
    """
    Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """


class SegmentUnderPointIn(TypedDict):
    image_uri: NotRequired[str]
    """
    Input image.
    """
    point: NotRequired[Point]
    """
    Point prompt.
    """
    store: NotRequired[str]
    """
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://docs.substrate.run/reference/external-files). If unset, the image data will be returned as a base64-encoded string.
    """


class SegmentUnderPointOut(TypedDict):
    mask_image_uri: NotRequired[str]
    """
    Detected segments in 'mask image' format. Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """


class SegmentAnythingIn(TypedDict):
    image_uri: NotRequired[str]
    """
    Input image.
    """
    point_prompts: NotRequired[List[Point]]
    """
    Point prompts, to detect a segment under the point. One of `point_prompts` or `box_prompts` must be set.
    """
    box_prompts: NotRequired[List[BoundingBox]]
    """
    Box prompts, to detect a segment within the bounding box. One of `point_prompts` or `box_prompts` must be set.
    """
    store: NotRequired[str]
    """
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://docs.substrate.run/reference/external-files). If unset, the image data will be returned as a base64-encoded string.
    """


class SegmentAnythingOut(TypedDict):
    mask_image_uri: NotRequired[str]
    """
    Detected segments in 'mask image' format. Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """


class TranscribeSpeechIn(TypedDict):
    audio_uri: NotRequired[str]
    """
    Input audio.
    """
    prompt: NotRequired[str]
    """
    Prompt to guide model on the content and context of input audio.
    """
    language: NotRequired[str]
    """
    Language of input audio in [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes) format.
    """
    segment: NotRequired[bool]
    """
    Segment the text into sentences with approximate timestamps.
    """
    align: NotRequired[bool]
    """
    Align transcription to produce more accurate sentence-level timestamps and word-level timestamps. An array of word segments will be included in each sentence segment.
    """
    diarize: NotRequired[bool]
    """
    Identify speakers for each segment. Speaker IDs will be included in each segment.
    """
    suggest_chapters: NotRequired[bool]
    """
    Suggest automatic chapter markers.
    """


class TranscribedWord(TypedDict):
    word: NotRequired[str]
    """
    Text of word.
    """
    start: NotRequired[float]
    """
    Start time of word, in seconds.
    """
    end: NotRequired[float]
    """
    End time of word, in seconds.
    """
    speaker: NotRequired[str]
    """
    ID of speaker, if `diarize` is enabled.
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
    ID of speaker, if `diarize` is enabled.
    """
    words: NotRequired[List[TranscribedWord]]
    """
    Aligned words, if `align` is enabled.
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


class TranscribeSpeechOut(TypedDict):
    text: NotRequired[str]
    """
    Transcribed text.
    """
    segments: NotRequired[List[TranscribedSegment]]
    """
    Transcribed segments, if `segment` is enabled.
    """
    chapters: NotRequired[List[ChapterMarker]]
    """
    Chapter markers, if `suggest_chapters` is enabled.
    """


class GenerateSpeechIn(TypedDict):
    text: NotRequired[str]
    """
    Input text.
    """
    store: NotRequired[str]
    """
    Use "hosted" to return an audio URL hosted on Substrate. You can also provide a URL to a registered [file store](https://docs.substrate.run/reference/external-files). If unset, the audio data will be returned as a base64-encoded string.
    """


class GenerateSpeechOut(TypedDict):
    audio_uri: NotRequired[str]
    """
    Base 64-encoded WAV audio bytes, or a hosted audio url if `store` is provided.
    """


class XTTSV2In(TypedDict):
    text: NotRequired[str]
    """
    Input text.
    """
    audio_uri: NotRequired[str]
    """
    Reference audio used to synthesize the speaker. If unset, a default speaker voice will be used.
    """
    language: NotRequired[str]
    """
    Language of input text. Supported languages: `en, de, fr, es, it, pt, pl, zh, ar, cs, ru, nl, tr, hu, ko`.
    """
    store: NotRequired[str]
    """
    Use "hosted" to return an audio URL hosted on Substrate. You can also provide a URL to a registered [file store](https://docs.substrate.run/reference/external-files). If unset, the audio data will be returned as a base64-encoded string.
    """


class XTTSV2Out(TypedDict):
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
    Vector store document ID.
    """
    metadata: NotRequired[Dict[str, Any]]
    """
    Vector store document metadata.
    """


class EmbedTextIn(TypedDict):
    text: NotRequired[str]
    """
    Text to embed.
    """
    collection_name: NotRequired[str]
    """
    Vector store name.
    """
    metadata: NotRequired[Dict[str, Any]]
    """
    Metadata that can be used to query the vector store. Ignored if `collection_name` is unset.
    """
    embedded_metadata_keys: NotRequired[List[str]]
    """
    Choose keys from `metadata` to embed with text.
    """
    doc_id: NotRequired[str]
    """
    Vector store document ID. Ignored if `store` is unset.
    """
    model: NotRequired[Literal["jina-v2", "clip"]]
    """
    Selected embedding model.
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
    Metadata that can be used to query the vector store. Ignored if `collection_name` is unset.
    """
    doc_id: NotRequired[str]
    """
    Vector store document ID. Ignored if `collection_name` is unset.
    """


class MultiEmbedTextIn(TypedDict):
    items: NotRequired[List[EmbedTextItem]]
    """
    Items to embed.
    """
    collection_name: NotRequired[str]
    """
    Vector store name.
    """
    embedded_metadata_keys: NotRequired[List[str]]
    """
    Choose keys from `metadata` to embed with text.
    """
    model: NotRequired[Literal["jina-v2", "clip"]]
    """
    Selected embedding model.
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
    collection_name: NotRequired[str]
    """
    Vector store name.
    """
    embedded_metadata_keys: NotRequired[List[str]]
    """
    Choose keys from `metadata` to embed with text.
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
    collection_name: NotRequired[str]
    """
    Vector store name.
    """
    doc_id: NotRequired[str]
    """
    Vector store document ID. Ignored if `collection_name` is unset.
    """
    model: NotRequired[Literal["clip"]]
    """
    Selected embedding model.
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
    Vector store document ID. Ignored if `collection_name` is unset.
    """


class EmbedTextOrImageItem(TypedDict):
    image_uri: NotRequired[str]
    """
    Image to embed.
    """
    text: NotRequired[str]
    """
    Text to embed.
    """
    metadata: NotRequired[Dict[str, Any]]
    """
    Metadata that can be used to query the vector store. Ignored if `collection_name` is unset.
    """
    doc_id: NotRequired[str]
    """
    Vector store document ID. Ignored if `collection_name` is unset.
    """


class MultiEmbedImageIn(TypedDict):
    items: NotRequired[List[EmbedImageItem]]
    """
    Items to embed.
    """
    collection_name: NotRequired[str]
    """
    Vector store name.
    """
    model: NotRequired[Literal["clip"]]
    """
    Selected embedding model.
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
    collection_name: NotRequired[str]
    """
    Vector store name.
    """
    embedded_metadata_keys: NotRequired[List[str]]
    """
    Choose keys from `metadata` to embed with text. Only applies to text items.
    """


class CLIPOut(TypedDict):
    embeddings: NotRequired[List[Embedding]]
    """
    Generated embeddings.
    """


class FindOrCreateVectorStoreIn(TypedDict):
    collection_name: NotRequired[str]
    """
    Vector store name.
    """
    model: NotRequired[Literal["jina-v2", "clip"]]
    """
    Selected embedding model.
    """


class FindOrCreateVectorStoreOut(TypedDict):
    collection_name: NotRequired[str]
    """
    Vector store name.
    """
    model: NotRequired[Literal["jina-v2", "clip"]]
    """
    Selected embedding model.
    """
    num_leaves: NotRequired[int]
    """
    Number of leaves in the vector store.
    """


class ListVectorStoresIn(TypedDict):
    pass


class ListVectorStoresOut(TypedDict):
    items: NotRequired[List[FindOrCreateVectorStoreOut]]
    """
    List of vector stores.
    """


class DeleteVectorStoreIn(TypedDict):
    collection_name: NotRequired[str]
    """
    Vector store name.
    """
    model: NotRequired[Literal["jina-v2", "clip"]]
    """
    Selected embedding model.
    """


class DeleteVectorStoreOut(TypedDict):
    collection_name: NotRequired[str]
    """
    Vector store name.
    """
    model: NotRequired[Literal["jina-v2", "clip"]]
    """
    Selected embedding model.
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


class FetchVectorsIn(TypedDict):
    collection_name: NotRequired[str]
    """
    Vector store name.
    """
    model: NotRequired[Literal["jina-v2", "clip"]]
    """
    Selected embedding model.
    """
    ids: NotRequired[List[str]]
    """
    Document IDs to retrieve.
    """


class FetchVectorsOut(TypedDict):
    vectors: NotRequired[List[Vector]]
    """
    Retrieved vectors.
    """


class UpdateVectorsOut(TypedDict):
    count: NotRequired[int]
    """
    Number of vectors modified.
    """


class DeleteVectorsOut(TypedDict):
    count: NotRequired[int]
    """
    Number of vectors modified.
    """


class UpdateVectorParams(TypedDict):
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


class UpdateVectorsIn(TypedDict):
    collection_name: NotRequired[str]
    """
    Vector store name.
    """
    model: NotRequired[Literal["jina-v2", "clip"]]
    """
    Selected embedding model.
    """
    vectors: NotRequired[List[UpdateVectorParams]]
    """
    Vectors to upsert.
    """


class DeleteVectorsIn(TypedDict):
    collection_name: NotRequired[str]
    """
    Vector store name.
    """
    model: NotRequired[Literal["jina-v2", "clip"]]
    """
    Selected embedding model.
    """
    ids: NotRequired[List[str]]
    """
    Document IDs to delete.
    """


class QueryVectorStoreIn(TypedDict):
    collection_name: NotRequired[str]
    """
    Vector store to query against.
    """
    model: NotRequired[Literal["jina-v2", "clip"]]
    """
    Selected embedding model.
    """
    query_strings: NotRequired[List[str]]
    """
    Texts to embed and use for the query.
    """
    query_image_uris: NotRequired[List[str]]
    """
    Image URIs to embed and use for the query.
    """
    query_vectors: NotRequired[List[List[float]]]
    """
    Vectors to use for the query.
    """
    query_ids: NotRequired[List[str]]
    """
    Document IDs to use for the query.
    """
    top_k: NotRequired[int]
    """
    Number of results to return.
    """
    ef_search: NotRequired[int]
    """
    The size of the dynamic candidate list for searching the index graph.
    """
    num_leaves_to_search: NotRequired[int]
    """
    The number of leaves in the index tree to search.
    """
    include_values: NotRequired[bool]
    """
    Include the values of the vectors in the response.
    """
    include_metadata: NotRequired[bool]
    """
    Include the metadata of the vectors in the response.
    """
    filters: NotRequired[Dict[str, Any]]
    """
    Filter metadata by key-value pairs.
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
    Embedding vector.
    """
    metadata: NotRequired[Dict[str, Any]]
    """
    Document metadata.
    """


class QueryVectorStoreOut(TypedDict):
    results: NotRequired[List[List[VectorStoreQueryResult]]]
    """
    Query results.
    """
    collection_name: NotRequired[str]
    """
    Vector store name.
    """
    model: NotRequired[Literal["jina-v2", "clip"]]
    """
    Selected embedding model.
    """


class SplitDocumentIn(TypedDict):
    uri: NotRequired[str]
    """
    URI of the document.
    """
    doc_id: NotRequired[str]
    """
    Document ID.
    """
    metadata: NotRequired[Dict[str, Any]]
    """
    Document metadata.
    """
    chunk_size: NotRequired[int]
    """
    Maximum number of units per chunk. Defaults to 1024 tokens for text or 40 lines for code.
    """
    chunk_overlap: NotRequired[int]
    """
    Number of units to overlap between chunks. Defaults to 200 tokens for text or 15 lines for code.
    """


class SplitDocumentOut(TypedDict):
    items: NotRequired[List[EmbedTextItem]]
    """
    Document chunks
    """
