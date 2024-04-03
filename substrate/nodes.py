"""
꩜ Substrate
@GENERATED FILE
20240403.20240403
"""

from .substrate import SubstrateResponse
from .core.corenode import CoreNode
from .dataclass_models import (
    CLIPOut,
    JinaV2Out,
    FillMaskOut,
    EmbedTextOut,
    EmbedImageOut,
    Firellava13BOut,
    GenerateJSONOut,
    GenerateTextOut,
    UpscaleImageOut,
    GenerateImageOut,
    DetectSegmentsOut,
    GenerateSpeechOut,
    MultiEmbedTextOut,
    MultiEmbedImageOut,
    TranscribeMediaOut,
    RemoveBackgroundOut,
    Mistral7BInstructOut,
    MultiGenerateJSONOut,
    MultiGenerateTextOut,
    StableDiffusionXLOut,
    GenerateTextVisionOut,
    MultiGenerateImageOut,
    GenerativeEditImageOut,
    MultiGenerativeEditImageOut,
    StableDiffusionXLInpaintOut,
    StableDiffusionXLIPAdapterOut,
    StableDiffusionXLControlNetOut,
)
from .typeddict_models import (
    CLIPIn,
    JinaV2In,
    FillMaskIn,
    EmbedTextIn,
    EmbedImageIn,
    Firellava13BIn,
    GenerateJSONIn,
    GenerateTextIn,
    UpscaleImageIn,
    GenerateImageIn,
    DetectSegmentsIn,
    GenerateSpeechIn,
    MultiEmbedTextIn,
    MultiEmbedImageIn,
    TranscribeMediaIn,
    RemoveBackgroundIn,
    Mistral7BInstructIn,
    MultiGenerateJSONIn,
    MultiGenerateTextIn,
    StableDiffusionXLIn,
    GenerateTextVisionIn,
    MultiGenerateImageIn,
    GenerativeEditImageIn,
    MultiGenerativeEditImageIn,
    StableDiffusionXLInpaintIn,
    StableDiffusionXLIPAdapterIn,
    StableDiffusionXLControlNetIn,
)
from .future_dataclass_models import (
    FutureCLIPOut,
    FutureJinaV2Out,
    FutureFillMaskOut,
    FutureEmbedTextOut,
    FutureEmbedImageOut,
    FutureFirellava13BOut,
    FutureGenerateJSONOut,
    FutureGenerateTextOut,
    FutureUpscaleImageOut,
    FutureGenerateImageOut,
    FutureDetectSegmentsOut,
    FutureGenerateSpeechOut,
    FutureMultiEmbedTextOut,
    FutureMultiEmbedImageOut,
    FutureTranscribeMediaOut,
    FutureRemoveBackgroundOut,
    FutureMistral7BInstructOut,
    FutureMultiGenerateJSONOut,
    FutureMultiGenerateTextOut,
    FutureStableDiffusionXLOut,
    FutureGenerateTextVisionOut,
    FutureMultiGenerateImageOut,
    FutureGenerativeEditImageOut,
    FutureMultiGenerativeEditImageOut,
    FutureStableDiffusionXLInpaintOut,
    FutureStableDiffusionXLIPAdapterOut,
    FutureStableDiffusionXLControlNetOut,
)


class GenerateText(CoreNode):
    """
    Generate text using a language model.

    https://substrate.run/library#GenerateText
    """

    def __init__(self, args: GenerateTextIn):
        """
        Input arguments: `prompt`, `temperature` (optional), `max_tokens` (optional), `node` (optional)

        Output fields: `future.text` (optional)

        https://substrate.run/library#GenerateText
        """
        super().__init__(**args)
        self.node = "GenerateText"

    def output(self, response: SubstrateResponse) -> GenerateTextOut:
        """
        Retrieve this node's output from a response.

        Output fields: `future.text` (optional)

        https://substrate.run/library#GenerateText
        """
        klass = GenerateTextOut
        json = response.api_response.json
        if json and json.get("data"):
            data = json["data"]
            node_id = self.id
            if data.get(self.id):
                return klass(**data[self.id])
        raise ValueError(f"Node {self.id} not found in response")

    @property
    def future(self) -> FutureGenerateTextOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.text` (optional)

        https://substrate.run/library#GenerateText
        """
        return super().future  # type: ignore


class MultiGenerateText(CoreNode):
    """
    Generate multiple text choices using a language model.

    https://substrate.run/library#MultiGenerateText
    """

    def __init__(self, args: MultiGenerateTextIn):
        """
        Input arguments: `prompt`, `num_choices`, `temperature` (optional), `max_tokens` (optional), `node` (optional)

        Output fields: `future.choices`

        https://substrate.run/library#MultiGenerateText
        """
        super().__init__(**args)
        self.node = "MultiGenerateText"

    def output(self, response: SubstrateResponse) -> MultiGenerateTextOut:
        """
        Retrieve this node's output from a response.

        Output fields: `future.choices`

        https://substrate.run/library#MultiGenerateText
        """
        klass = MultiGenerateTextOut
        json = response.api_response.json
        if json and json.get("data"):
            data = json["data"]
            node_id = self.id
            if data.get(self.id):
                return klass(**data[self.id])
        raise ValueError(f"Node {self.id} not found in response")

    @property
    def future(self) -> FutureMultiGenerateTextOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.choices`

        https://substrate.run/library#MultiGenerateText
        """
        return super().future  # type: ignore


class GenerateJSON(CoreNode):
    """
    Generate JSON using a language model.

    https://substrate.run/library#GenerateJSON
    """

    def __init__(self, args: GenerateJSONIn):
        """
        Input arguments: `prompt`, `json_schema`, `temperature` (optional), `max_tokens` (optional), `node` (optional)

        Output fields: `future.json_object` (optional)

        https://substrate.run/library#GenerateJSON
        """
        super().__init__(**args)
        self.node = "GenerateJSON"

    def output(self, response: SubstrateResponse) -> GenerateJSONOut:
        """
        Retrieve this node's output from a response.

        Output fields: `future.json_object` (optional)

        https://substrate.run/library#GenerateJSON
        """
        klass = GenerateJSONOut
        json = response.api_response.json
        if json and json.get("data"):
            data = json["data"]
            node_id = self.id
            if data.get(self.id):
                return klass(**data[self.id])
        raise ValueError(f"Node {self.id} not found in response")

    @property
    def future(self) -> FutureGenerateJSONOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.json_object` (optional)

        https://substrate.run/library#GenerateJSON
        """
        return super().future  # type: ignore


class MultiGenerateJSON(CoreNode):
    """
    Generate multiple JSON choices using a language model.

    https://substrate.run/library#MultiGenerateJSON
    """

    def __init__(self, args: MultiGenerateJSONIn):
        """
        Input arguments: `prompt`, `json_schema`, `num_choices`, `temperature` (optional), `max_tokens` (optional), `node` (optional)

        Output fields: `future.choices`

        https://substrate.run/library#MultiGenerateJSON
        """
        super().__init__(**args)
        self.node = "MultiGenerateJSON"

    def output(self, response: SubstrateResponse) -> MultiGenerateJSONOut:
        """
        Retrieve this node's output from a response.

        Output fields: `future.choices`

        https://substrate.run/library#MultiGenerateJSON
        """
        klass = MultiGenerateJSONOut
        json = response.api_response.json
        if json and json.get("data"):
            data = json["data"]
            node_id = self.id
            if data.get(self.id):
                return klass(**data[self.id])
        raise ValueError(f"Node {self.id} not found in response")

    @property
    def future(self) -> FutureMultiGenerateJSONOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.choices`

        https://substrate.run/library#MultiGenerateJSON
        """
        return super().future  # type: ignore


class GenerateTextVision(CoreNode):
    """
    Generate text with image input.

    https://substrate.run/library#GenerateTextVision
    """

    def __init__(self, args: GenerateTextVisionIn):
        """
        Input arguments: `prompt`, `image_uris`, `temperature` (optional), `max_tokens` (optional), `node` (optional)

        Output fields: `future.text`

        https://substrate.run/library#GenerateTextVision
        """
        super().__init__(**args)
        self.node = "GenerateTextVision"

    def output(self, response: SubstrateResponse) -> GenerateTextVisionOut:
        """
        Retrieve this node's output from a response.

        Output fields: `future.text`

        https://substrate.run/library#GenerateTextVision
        """
        klass = GenerateTextVisionOut
        json = response.api_response.json
        if json and json.get("data"):
            data = json["data"]
            node_id = self.id
            if data.get(self.id):
                return klass(**data[self.id])
        raise ValueError(f"Node {self.id} not found in response")

    @property
    def future(self) -> FutureGenerateTextVisionOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.text`

        https://substrate.run/library#GenerateTextVision
        """
        return super().future  # type: ignore


class Mistral7BInstruct(CoreNode):
    """
    Generate text using Mistral 7B Instruct.

    https://substrate.run/library#Mistral7BInstruct
    """

    def __init__(self, args: Mistral7BInstructIn):
        """
        Input arguments: `prompt`, `num_choices`, `json_schema` (optional), `temperature` (optional), `max_tokens` (optional)

        Output fields: `future.choices`

        https://substrate.run/library#Mistral7BInstruct
        """
        super().__init__(**args)
        self.node = "Mistral7BInstruct"

    def output(self, response: SubstrateResponse) -> Mistral7BInstructOut:
        """
        Retrieve this node's output from a response.

        Output fields: `future.choices`

        https://substrate.run/library#Mistral7BInstruct
        """
        klass = Mistral7BInstructOut
        json = response.api_response.json
        if json and json.get("data"):
            data = json["data"]
            node_id = self.id
            if data.get(self.id):
                return klass(**data[self.id])
        raise ValueError(f"Node {self.id} not found in response")

    @property
    def future(self) -> FutureMistral7BInstructOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.choices`

        https://substrate.run/library#Mistral7BInstruct
        """
        return super().future  # type: ignore


class Firellava13B(CoreNode):
    """
    Generate text with image input using FireLLaVA 13B.

    https://substrate.run/library#Firellava13B
    """

    def __init__(self, args: Firellava13BIn):
        """
        Input arguments: `prompt`, `image_uris`, `temperature` (optional), `max_tokens` (optional)

        Output fields: `future.text`

        https://substrate.run/library#Firellava13B
        """
        super().__init__(**args)
        self.node = "Firellava13B"

    def output(self, response: SubstrateResponse) -> Firellava13BOut:
        """
        Retrieve this node's output from a response.

        Output fields: `future.text`

        https://substrate.run/library#Firellava13B
        """
        klass = Firellava13BOut
        json = response.api_response.json
        if json and json.get("data"):
            data = json["data"]
            node_id = self.id
            if data.get(self.id):
                return klass(**data[self.id])
        raise ValueError(f"Node {self.id} not found in response")

    @property
    def future(self) -> FutureFirellava13BOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.text`

        https://substrate.run/library#Firellava13B
        """
        return super().future  # type: ignore


class GenerateImage(CoreNode):
    """
    Generate an image.

    https://substrate.run/library#GenerateImage
    """

    def __init__(self, args: GenerateImageIn):
        """
        Input arguments: `prompt`, `store` (optional), `node` (optional)

        Output fields: `future.image_uri`

        https://substrate.run/library#GenerateImage
        """
        super().__init__(**args)
        self.node = "GenerateImage"

    def output(self, response: SubstrateResponse) -> GenerateImageOut:
        """
        Retrieve this node's output from a response.

        Output fields: `future.image_uri`

        https://substrate.run/library#GenerateImage
        """
        klass = GenerateImageOut
        json = response.api_response.json
        if json and json.get("data"):
            data = json["data"]
            node_id = self.id
            if data.get(self.id):
                return klass(**data[self.id])
        raise ValueError(f"Node {self.id} not found in response")

    @property
    def future(self) -> FutureGenerateImageOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.image_uri`

        https://substrate.run/library#GenerateImage
        """
        return super().future  # type: ignore


class MultiGenerateImage(CoreNode):
    """
    Generate multiple images.

    https://substrate.run/library#MultiGenerateImage
    """

    def __init__(self, args: MultiGenerateImageIn):
        """
        Input arguments: `prompt`, `num_images`, `store` (optional), `node` (optional)

        Output fields: `future.outputs`

        https://substrate.run/library#MultiGenerateImage
        """
        super().__init__(**args)
        self.node = "MultiGenerateImage"

    def output(self, response: SubstrateResponse) -> MultiGenerateImageOut:
        """
        Retrieve this node's output from a response.

        Output fields: `future.outputs`

        https://substrate.run/library#MultiGenerateImage
        """
        klass = MultiGenerateImageOut
        json = response.api_response.json
        if json and json.get("data"):
            data = json["data"]
            node_id = self.id
            if data.get(self.id):
                return klass(**data[self.id])
        raise ValueError(f"Node {self.id} not found in response")

    @property
    def future(self) -> FutureMultiGenerateImageOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.outputs`

        https://substrate.run/library#MultiGenerateImage
        """
        return super().future  # type: ignore


class GenerativeEditImage(CoreNode):
    """
    Edit an image using image generation.

    https://substrate.run/library#GenerativeEditImage
    """

    def __init__(self, args: GenerativeEditImageIn):
        """
        Input arguments: `image_uri`, `prompt`, `mask_image_uri` (optional), `store` (optional), `node` (optional)

        Output fields: `future.image_uri`

        https://substrate.run/library#GenerativeEditImage
        """
        super().__init__(**args)
        self.node = "GenerativeEditImage"

    def output(self, response: SubstrateResponse) -> GenerativeEditImageOut:
        """
        Retrieve this node's output from a response.

        Output fields: `future.image_uri`

        https://substrate.run/library#GenerativeEditImage
        """
        klass = GenerativeEditImageOut
        json = response.api_response.json
        if json and json.get("data"):
            data = json["data"]
            node_id = self.id
            if data.get(self.id):
                return klass(**data[self.id])
        raise ValueError(f"Node {self.id} not found in response")

    @property
    def future(self) -> FutureGenerativeEditImageOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.image_uri`

        https://substrate.run/library#GenerativeEditImage
        """
        return super().future  # type: ignore


class MultiGenerativeEditImage(CoreNode):
    """
    Edit multiple images using image generation.

    https://substrate.run/library#MultiGenerativeEditImage
    """

    def __init__(self, args: MultiGenerativeEditImageIn):
        """
        Input arguments: `image_uri`, `prompt`, `mask_image_uri` (optional), `num_images`, `store` (optional), `node` (optional)

        Output fields: `future.outputs`

        https://substrate.run/library#MultiGenerativeEditImage
        """
        super().__init__(**args)
        self.node = "MultiGenerativeEditImage"

    def output(self, response: SubstrateResponse) -> MultiGenerativeEditImageOut:
        """
        Retrieve this node's output from a response.

        Output fields: `future.outputs`

        https://substrate.run/library#MultiGenerativeEditImage
        """
        klass = MultiGenerativeEditImageOut
        json = response.api_response.json
        if json and json.get("data"):
            data = json["data"]
            node_id = self.id
            if data.get(self.id):
                return klass(**data[self.id])
        raise ValueError(f"Node {self.id} not found in response")

    @property
    def future(self) -> FutureMultiGenerativeEditImageOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.outputs`

        https://substrate.run/library#MultiGenerativeEditImage
        """
        return super().future  # type: ignore


class StableDiffusionXL(CoreNode):
    """
    Generate an image using Stable Diffusion XL.

    https://substrate.run/library#StableDiffusionXL
    """

    def __init__(self, args: StableDiffusionXLIn):
        """
        Input arguments: `prompt`, `negative_prompt` (optional), `steps` (optional), `num_images` (optional), `store` (optional), `height` (optional), `width` (optional), `seeds` (optional), `guidance_scale` (optional)

        Output fields: `future.outputs`

        https://substrate.run/library#StableDiffusionXL
        """
        super().__init__(**args)
        self.node = "StableDiffusionXL"

    def output(self, response: SubstrateResponse) -> StableDiffusionXLOut:
        """
        Retrieve this node's output from a response.

        Output fields: `future.outputs`

        https://substrate.run/library#StableDiffusionXL
        """
        klass = StableDiffusionXLOut
        json = response.api_response.json
        if json and json.get("data"):
            data = json["data"]
            node_id = self.id
            if data.get(self.id):
                return klass(**data[self.id])
        raise ValueError(f"Node {self.id} not found in response")

    @property
    def future(self) -> FutureStableDiffusionXLOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.outputs`

        https://substrate.run/library#StableDiffusionXL
        """
        return super().future  # type: ignore


class StableDiffusionXLInpaint(CoreNode):
    """
    Inpaint an image using Stable Diffusion XL.

    https://substrate.run/library#StableDiffusionXLInpaint
    """

    def __init__(self, args: StableDiffusionXLInpaintIn):
        """
        Input arguments: `image_uri`, `prompt`, `mask_image_uri` (optional), `num_images`, `output_resolution` (optional), `negative_prompt` (optional), `store` (optional), `strength` (optional), `seeds` (optional)

        Output fields: `future.outputs`

        https://substrate.run/library#StableDiffusionXLInpaint
        """
        super().__init__(**args)
        self.node = "StableDiffusionXLInpaint"

    def output(self, response: SubstrateResponse) -> StableDiffusionXLInpaintOut:
        """
        Retrieve this node's output from a response.

        Output fields: `future.outputs`

        https://substrate.run/library#StableDiffusionXLInpaint
        """
        klass = StableDiffusionXLInpaintOut
        json = response.api_response.json
        if json and json.get("data"):
            data = json["data"]
            node_id = self.id
            if data.get(self.id):
                return klass(**data[self.id])
        raise ValueError(f"Node {self.id} not found in response")

    @property
    def future(self) -> FutureStableDiffusionXLInpaintOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.outputs`

        https://substrate.run/library#StableDiffusionXLInpaint
        """
        return super().future  # type: ignore


class StableDiffusionXLIPAdapter(CoreNode):
    """
    Generate an image using Stable Diffusion XL with an image prompt.

    https://substrate.run/library#StableDiffusionXLIPAdapter
    """

    def __init__(self, args: StableDiffusionXLIPAdapterIn):
        """
        Input arguments: `prompt`, `image_prompt_uri` (optional), `num_images`, `ip_adapter_scale` (optional), `negative_prompt` (optional), `store` (optional), `width` (optional), `height` (optional), `seeds` (optional)

        Output fields: `future.outputs`

        https://substrate.run/library#StableDiffusionXLIPAdapter
        """
        super().__init__(**args)
        self.node = "StableDiffusionXLIPAdapter"

    def output(self, response: SubstrateResponse) -> StableDiffusionXLIPAdapterOut:
        """
        Retrieve this node's output from a response.

        Output fields: `future.outputs`

        https://substrate.run/library#StableDiffusionXLIPAdapter
        """
        klass = StableDiffusionXLIPAdapterOut
        json = response.api_response.json
        if json and json.get("data"):
            data = json["data"]
            node_id = self.id
            if data.get(self.id):
                return klass(**data[self.id])
        raise ValueError(f"Node {self.id} not found in response")

    @property
    def future(self) -> FutureStableDiffusionXLIPAdapterOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.outputs`

        https://substrate.run/library#StableDiffusionXLIPAdapter
        """
        return super().future  # type: ignore


class StableDiffusionXLControlNet(CoreNode):
    """
    Generate an image using Stable Diffusion XL structuring generation with an input image.

    https://substrate.run/library#StableDiffusionXLControlNet
    """

    def __init__(self, args: StableDiffusionXLControlNetIn):
        """
        Input arguments: `image_uri`, `control_method`, `prompt`, `num_images`, `output_resolution` (optional), `negative_prompt` (optional), `store` (optional), `conditioning_scale` (optional), `seeds` (optional)

        Output fields: `future.outputs`

        https://substrate.run/library#StableDiffusionXLControlNet
        """
        super().__init__(**args)
        self.node = "StableDiffusionXLControlNet"

    def output(self, response: SubstrateResponse) -> StableDiffusionXLControlNetOut:
        """
        Retrieve this node's output from a response.

        Output fields: `future.outputs`

        https://substrate.run/library#StableDiffusionXLControlNet
        """
        klass = StableDiffusionXLControlNetOut
        json = response.api_response.json
        if json and json.get("data"):
            data = json["data"]
            node_id = self.id
            if data.get(self.id):
                return klass(**data[self.id])
        raise ValueError(f"Node {self.id} not found in response")

    @property
    def future(self) -> FutureStableDiffusionXLControlNetOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.outputs`

        https://substrate.run/library#StableDiffusionXLControlNet
        """
        return super().future  # type: ignore


class FillMask(CoreNode):
    """
    Edit an image with a generative model.

    https://substrate.run/library#FillMask
    """

    def __init__(self, args: FillMaskIn):
        """
        Input arguments: `image_uri`, `mask_image_uri`, `model` (optional), `store` (optional)

        Output fields: `future.image_uri`

        https://substrate.run/library#FillMask
        """
        super().__init__(**args)
        self.node = "FillMask"

    def output(self, response: SubstrateResponse) -> FillMaskOut:
        """
        Retrieve this node's output from a response.

        Output fields: `future.image_uri`

        https://substrate.run/library#FillMask
        """
        klass = FillMaskOut
        json = response.api_response.json
        if json and json.get("data"):
            data = json["data"]
            node_id = self.id
            if data.get(self.id):
                return klass(**data[self.id])
        raise ValueError(f"Node {self.id} not found in response")

    @property
    def future(self) -> FutureFillMaskOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.image_uri`

        https://substrate.run/library#FillMask
        """
        return super().future  # type: ignore


class UpscaleImage(CoreNode):
    """
    Upscale an image.

    https://substrate.run/library#UpscaleImage
    """

    def __init__(self, args: UpscaleImageIn):
        """
        Input arguments: `image_uri`, `model` (optional), `store` (optional)

        Output fields: `future.image_uri`

        https://substrate.run/library#UpscaleImage
        """
        super().__init__(**args)
        self.node = "UpscaleImage"

    def output(self, response: SubstrateResponse) -> UpscaleImageOut:
        """
        Retrieve this node's output from a response.

        Output fields: `future.image_uri`

        https://substrate.run/library#UpscaleImage
        """
        klass = UpscaleImageOut
        json = response.api_response.json
        if json and json.get("data"):
            data = json["data"]
            node_id = self.id
            if data.get(self.id):
                return klass(**data[self.id])
        raise ValueError(f"Node {self.id} not found in response")

    @property
    def future(self) -> FutureUpscaleImageOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.image_uri`

        https://substrate.run/library#UpscaleImage
        """
        return super().future  # type: ignore


class RemoveBackground(CoreNode):
    """
    Remove the background from an image, with the option to return the foreground as a mask.

    https://substrate.run/library#RemoveBackground
    """

    def __init__(self, args: RemoveBackgroundIn):
        """
        Input arguments: `image_uri`, `return_mask` (optional), `background_color` (optional), `model` (optional), `store` (optional)

        Output fields: `future.image_uri`

        https://substrate.run/library#RemoveBackground
        """
        super().__init__(**args)
        self.node = "RemoveBackground"

    def output(self, response: SubstrateResponse) -> RemoveBackgroundOut:
        """
        Retrieve this node's output from a response.

        Output fields: `future.image_uri`

        https://substrate.run/library#RemoveBackground
        """
        klass = RemoveBackgroundOut
        json = response.api_response.json
        if json and json.get("data"):
            data = json["data"]
            node_id = self.id
            if data.get(self.id):
                return klass(**data[self.id])
        raise ValueError(f"Node {self.id} not found in response")

    @property
    def future(self) -> FutureRemoveBackgroundOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.image_uri`

        https://substrate.run/library#RemoveBackground
        """
        return super().future  # type: ignore


class DetectSegments(CoreNode):
    """
    Detect segments in an image given point(s) or bounding box(es).

    https://substrate.run/library#DetectSegments
    """

    def __init__(self, args: DetectSegmentsIn):
        """
        Input arguments: `image_uri`, `point_prompts` (optional), `box_prompts` (optional), `model` (optional), `store` (optional)

        Output fields: `future.mask_image_uri`

        https://substrate.run/library#DetectSegments
        """
        super().__init__(**args)
        self.node = "DetectSegments"

    def output(self, response: SubstrateResponse) -> DetectSegmentsOut:
        """
        Retrieve this node's output from a response.

        Output fields: `future.mask_image_uri`

        https://substrate.run/library#DetectSegments
        """
        klass = DetectSegmentsOut
        json = response.api_response.json
        if json and json.get("data"):
            data = json["data"]
            node_id = self.id
            if data.get(self.id):
                return klass(**data[self.id])
        raise ValueError(f"Node {self.id} not found in response")

    @property
    def future(self) -> FutureDetectSegmentsOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.mask_image_uri`

        https://substrate.run/library#DetectSegments
        """
        return super().future  # type: ignore


class TranscribeMedia(CoreNode):
    """
    Transcribe speech in an audio or video file.

    https://substrate.run/library#TranscribeMedia
    """

    def __init__(self, args: TranscribeMediaIn):
        """
        Input arguments: `audio_uri`, `prompt` (optional), `language` (optional), `segment` (optional), `align` (optional), `diarize` (optional), `suggest_chapters` (optional)

        Output fields: `future.text`, `future.segments` (optional), `future.chapters` (optional)

        https://substrate.run/library#TranscribeMedia
        """
        super().__init__(**args)
        self.node = "TranscribeMedia"

    def output(self, response: SubstrateResponse) -> TranscribeMediaOut:
        """
        Retrieve this node's output from a response.

        Output fields: `future.text`, `future.segments` (optional), `future.chapters` (optional)

        https://substrate.run/library#TranscribeMedia
        """
        klass = TranscribeMediaOut
        json = response.api_response.json
        if json and json.get("data"):
            data = json["data"]
            node_id = self.id
            if data.get(self.id):
                return klass(**data[self.id])
        raise ValueError(f"Node {self.id} not found in response")

    @property
    def future(self) -> FutureTranscribeMediaOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.text`, `future.segments` (optional), `future.chapters` (optional)

        https://substrate.run/library#TranscribeMedia
        """
        return super().future  # type: ignore


class GenerateSpeech(CoreNode):
    """
    Generate speech from text.

    https://substrate.run/library#GenerateSpeech
    """

    def __init__(self, args: GenerateSpeechIn):
        """
        Input arguments: `text`, `audio_uri` (optional), `language` (optional), `store` (optional)

        Output fields: `future.audio_uri`

        https://substrate.run/library#GenerateSpeech
        """
        super().__init__(**args)
        self.node = "GenerateSpeech"

    def output(self, response: SubstrateResponse) -> GenerateSpeechOut:
        """
        Retrieve this node's output from a response.

        Output fields: `future.audio_uri`

        https://substrate.run/library#GenerateSpeech
        """
        klass = GenerateSpeechOut
        json = response.api_response.json
        if json and json.get("data"):
            data = json["data"]
            node_id = self.id
            if data.get(self.id):
                return klass(**data[self.id])
        raise ValueError(f"Node {self.id} not found in response")

    @property
    def future(self) -> FutureGenerateSpeechOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.audio_uri`

        https://substrate.run/library#GenerateSpeech
        """
        return super().future  # type: ignore


class EmbedText(CoreNode):
    """
    Generate embedding for a text document.

    https://substrate.run/library#EmbedText
    """

    def __init__(self, args: EmbedTextIn):
        """
        Input arguments: `text`, `store` (optional), `metadata` (optional), `embedded_metadata_keys` (optional), `doc_id` (optional), `node` (optional)

        Output fields: `future.embedding`

        https://substrate.run/library#EmbedText
        """
        super().__init__(**args)
        self.node = "EmbedText"

    def output(self, response: SubstrateResponse) -> EmbedTextOut:
        """
        Retrieve this node's output from a response.

        Output fields: `future.embedding`

        https://substrate.run/library#EmbedText
        """
        klass = EmbedTextOut
        json = response.api_response.json
        if json and json.get("data"):
            data = json["data"]
            node_id = self.id
            if data.get(self.id):
                return klass(**data[self.id])
        raise ValueError(f"Node {self.id} not found in response")

    @property
    def future(self) -> FutureEmbedTextOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.embedding`

        https://substrate.run/library#EmbedText
        """
        return super().future  # type: ignore


class MultiEmbedText(CoreNode):
    """
    Generate embeddings for multiple text documents.

    https://substrate.run/library#MultiEmbedText
    """

    def __init__(self, args: MultiEmbedTextIn):
        """
        Input arguments: `items`, `store` (optional), `embedded_metadata_keys` (optional), `node` (optional)

        Output fields: `future.embeddings`

        https://substrate.run/library#MultiEmbedText
        """
        super().__init__(**args)
        self.node = "MultiEmbedText"

    def output(self, response: SubstrateResponse) -> MultiEmbedTextOut:
        """
        Retrieve this node's output from a response.

        Output fields: `future.embeddings`

        https://substrate.run/library#MultiEmbedText
        """
        klass = MultiEmbedTextOut
        json = response.api_response.json
        if json and json.get("data"):
            data = json["data"]
            node_id = self.id
            if data.get(self.id):
                return klass(**data[self.id])
        raise ValueError(f"Node {self.id} not found in response")

    @property
    def future(self) -> FutureMultiEmbedTextOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.embeddings`

        https://substrate.run/library#MultiEmbedText
        """
        return super().future  # type: ignore


class EmbedImage(CoreNode):
    """
    Generate embedding for an image.

    https://substrate.run/library#EmbedImage
    """

    def __init__(self, args: EmbedImageIn):
        """
        Input arguments: `image_uri`, `store` (optional), `doc_id` (optional), `node` (optional)

        Output fields: `future.embedding`

        https://substrate.run/library#EmbedImage
        """
        super().__init__(**args)
        self.node = "EmbedImage"

    def output(self, response: SubstrateResponse) -> EmbedImageOut:
        """
        Retrieve this node's output from a response.

        Output fields: `future.embedding`

        https://substrate.run/library#EmbedImage
        """
        klass = EmbedImageOut
        json = response.api_response.json
        if json and json.get("data"):
            data = json["data"]
            node_id = self.id
            if data.get(self.id):
                return klass(**data[self.id])
        raise ValueError(f"Node {self.id} not found in response")

    @property
    def future(self) -> FutureEmbedImageOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.embedding`

        https://substrate.run/library#EmbedImage
        """
        return super().future  # type: ignore


class MultiEmbedImage(CoreNode):
    """
    Generate embeddings for multiple images.

    https://substrate.run/library#MultiEmbedImage
    """

    def __init__(self, args: MultiEmbedImageIn):
        """
        Input arguments: `items`, `store` (optional), `node` (optional)

        Output fields: `future.embeddings`

        https://substrate.run/library#MultiEmbedImage
        """
        super().__init__(**args)
        self.node = "MultiEmbedImage"

    def output(self, response: SubstrateResponse) -> MultiEmbedImageOut:
        """
        Retrieve this node's output from a response.

        Output fields: `future.embeddings`

        https://substrate.run/library#MultiEmbedImage
        """
        klass = MultiEmbedImageOut
        json = response.api_response.json
        if json and json.get("data"):
            data = json["data"]
            node_id = self.id
            if data.get(self.id):
                return klass(**data[self.id])
        raise ValueError(f"Node {self.id} not found in response")

    @property
    def future(self) -> FutureMultiEmbedImageOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.embeddings`

        https://substrate.run/library#MultiEmbedImage
        """
        return super().future  # type: ignore


class JinaV2(CoreNode):
    """
    Generate embeddings for multiple text documents using Jina V2.

    https://substrate.run/library#JinaV2
    """

    def __init__(self, args: JinaV2In):
        """
        Input arguments: `items`, `store` (optional), `embedded_metadata_keys` (optional)

        Output fields: `future.embeddings`

        https://substrate.run/library#JinaV2
        """
        super().__init__(**args)
        self.node = "JinaV2"

    def output(self, response: SubstrateResponse) -> JinaV2Out:
        """
        Retrieve this node's output from a response.

        Output fields: `future.embeddings`

        https://substrate.run/library#JinaV2
        """
        klass = JinaV2Out
        json = response.api_response.json
        if json and json.get("data"):
            data = json["data"]
            node_id = self.id
            if data.get(self.id):
                return klass(**data[self.id])
        raise ValueError(f"Node {self.id} not found in response")

    @property
    def future(self) -> FutureJinaV2Out:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.embeddings`

        https://substrate.run/library#JinaV2
        """
        return super().future  # type: ignore


class CLIP(CoreNode):
    """
    Generate embeddings for text or images using CLIP.

    https://substrate.run/library#CLIP
    """

    def __init__(self, args: CLIPIn):
        """
        Input arguments: `items`, `embedded_metadata_keys` (optional), `store` (optional)

        Output fields: `future.embeddings`

        https://substrate.run/library#CLIP
        """
        super().__init__(**args)
        self.node = "CLIP"

    def output(self, response: SubstrateResponse) -> CLIPOut:
        """
        Retrieve this node's output from a response.

        Output fields: `future.embeddings`

        https://substrate.run/library#CLIP
        """
        klass = CLIPOut
        json = response.api_response.json
        if json and json.get("data"):
            data = json["data"]
            node_id = self.id
            if data.get(self.id):
                return klass(**data[self.id])
        raise ValueError(f"Node {self.id} not found in response")

    @property
    def future(self) -> FutureCLIPOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.embeddings`

        https://substrate.run/library#CLIP
        """
        return super().future  # type: ignore
