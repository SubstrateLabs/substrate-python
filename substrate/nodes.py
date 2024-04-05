"""
꩜ Substrate
@GENERATED FILE
20240405.20240405
"""

from .substrate import SubstrateResponse
from .core.corenode import CoreNode
from .dataclass_models import (
    CLIPOut,
    JinaV2Out,
    XTTSV2Out,
    BigLaMaOut,
    DISISNetOut,
    FillMaskOut,
    EmbedTextOut,
    EmbedImageOut,
    RealESRGANOut,
    FetchVectorsOut,
    Firellava13BOut,
    GenerateJSONOut,
    GenerateTextOut,
    UpscaleImageOut,
    DeleteVectorsOut,
    GenerateImageOut,
    UpdateVectorsOut,
    GenerateSpeechOut,
    MultiEmbedTextOut,
    MultiEmbedImageOut,
    SegmentAnythingOut,
    TranscribeMediaOut,
    ListVectorStoresOut,
    QueryVectorStoreOut,
    RemoveBackgroundOut,
    CreateVectorStoreOut,
    DeleteVectorStoreOut,
    Mistral7BInstructOut,
    MultiGenerateJSONOut,
    MultiGenerateTextOut,
    SegmentUnderPointOut,
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
    XTTSV2In,
    BigLaMaIn,
    DISISNetIn,
    FillMaskIn,
    EmbedTextIn,
    EmbedImageIn,
    RealESRGANIn,
    FetchVectorsIn,
    Firellava13BIn,
    GenerateJSONIn,
    GenerateTextIn,
    UpscaleImageIn,
    DeleteVectorsIn,
    GenerateImageIn,
    UpdateVectorsIn,
    GenerateSpeechIn,
    MultiEmbedTextIn,
    MultiEmbedImageIn,
    SegmentAnythingIn,
    TranscribeMediaIn,
    ListVectorStoresIn,
    QueryVectorStoreIn,
    RemoveBackgroundIn,
    CreateVectorStoreIn,
    DeleteVectorStoreIn,
    Mistral7BInstructIn,
    MultiGenerateJSONIn,
    MultiGenerateTextIn,
    SegmentUnderPointIn,
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
    FutureXTTSV2Out,
    FutureBigLaMaOut,
    FutureDISISNetOut,
    FutureFillMaskOut,
    FutureEmbedTextOut,
    FutureEmbedImageOut,
    FutureRealESRGANOut,
    FutureFetchVectorsOut,
    FutureFirellava13BOut,
    FutureGenerateJSONOut,
    FutureGenerateTextOut,
    FutureUpscaleImageOut,
    FutureDeleteVectorsOut,
    FutureGenerateImageOut,
    FutureUpdateVectorsOut,
    FutureGenerateSpeechOut,
    FutureMultiEmbedTextOut,
    FutureMultiEmbedImageOut,
    FutureSegmentAnythingOut,
    FutureTranscribeMediaOut,
    FutureListVectorStoresOut,
    FutureQueryVectorStoreOut,
    FutureRemoveBackgroundOut,
    FutureCreateVectorStoreOut,
    FutureDeleteVectorStoreOut,
    FutureMistral7BInstructOut,
    FutureMultiGenerateJSONOut,
    FutureMultiGenerateTextOut,
    FutureSegmentUnderPointOut,
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
    Generate text using [Mistral 7B Instruct](https://mistral.ai/news/announcing-mistral-7b).

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
    Generate text with image input using [FireLLaVA 13B](https://fireworks.ai/blog/firellava-the-first-commercially-permissive-oss-llava-model).

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
    Generate an image using [Stable Diffusion XL](https://arxiv.org/abs/2307.01952).

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
    Edit an image using [Stable Diffusion XL](https://arxiv.org/abs/2307.01952). Supports inpainting (edit part of the image with a mask) and image-to-image (edit the full image).

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
    Generate an image with an image prompt, using Stable Diffusion XL with [IP-Adapter](https://arxiv.org/abs/2308.06721).

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
    Generate an image with generation structured by an input image, using Stable Diffusion XL with [ControlNet](https://arxiv.org/abs/2302.05543).

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
    Fill (inpaint) part of an image, e.g. to 'remove' an object.

    https://substrate.run/library#FillMask
    """

    def __init__(self, args: FillMaskIn):
        """
        Input arguments: `image_uri`, `mask_image_uri`, `store` (optional), `node` (optional)

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


class BigLaMa(CoreNode):
    """
    Inpaint a mask using [LaMa](https://github.com/advimman/lama).

    https://substrate.run/library#BigLaMa
    """

    def __init__(self, args: BigLaMaIn):
        """
        Input arguments: `image_uri`, `mask_image_uri`, `store` (optional)

        Output fields: `future.image_uri`

        https://substrate.run/library#BigLaMa
        """
        super().__init__(**args)
        self.node = "BigLaMa"

    def output(self, response: SubstrateResponse) -> BigLaMaOut:
        """
        Retrieve this node's output from a response.

        Output fields: `future.image_uri`

        https://substrate.run/library#BigLaMa
        """
        klass = BigLaMaOut
        json = response.api_response.json
        if json and json.get("data"):
            data = json["data"]
            node_id = self.id
            if data.get(self.id):
                return klass(**data[self.id])
        raise ValueError(f"Node {self.id} not found in response")

    @property
    def future(self) -> FutureBigLaMaOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.image_uri`

        https://substrate.run/library#BigLaMa
        """
        return super().future  # type: ignore


class UpscaleImage(CoreNode):
    """
    Upscale an image.

    https://substrate.run/library#UpscaleImage
    """

    def __init__(self, args: UpscaleImageIn):
        """
        Input arguments: `image_uri`, `store` (optional), `node` (optional)

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


class RealESRGAN(CoreNode):
    """
    Upscale an image using [RealESRGAN](https://github.com/xinntao/Real-ESRGAN).

    https://substrate.run/library#RealESRGAN
    """

    def __init__(self, args: RealESRGANIn):
        """
        Input arguments: `image_uri`, `model` (optional), `store` (optional)

        Output fields: `future.image_uri`

        https://substrate.run/library#RealESRGAN
        """
        super().__init__(**args)
        self.node = "RealESRGAN"

    def output(self, response: SubstrateResponse) -> RealESRGANOut:
        """
        Retrieve this node's output from a response.

        Output fields: `future.image_uri`

        https://substrate.run/library#RealESRGAN
        """
        klass = RealESRGANOut
        json = response.api_response.json
        if json and json.get("data"):
            data = json["data"]
            node_id = self.id
            if data.get(self.id):
                return klass(**data[self.id])
        raise ValueError(f"Node {self.id} not found in response")

    @property
    def future(self) -> FutureRealESRGANOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.image_uri`

        https://substrate.run/library#RealESRGAN
        """
        return super().future  # type: ignore


class RemoveBackground(CoreNode):
    """
    Remove the background from an image, with the option to return the foreground as a mask.

    https://substrate.run/library#RemoveBackground
    """

    def __init__(self, args: RemoveBackgroundIn):
        """
        Input arguments: `image_uri`, `return_mask` (optional), `background_color` (optional), `store` (optional), `node` (optional)

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


class DISISNet(CoreNode):
    """
    Segment an image using [DIS IS-Net](https://github.com/xuebinqin/DIS).

    https://substrate.run/library#DISISNet
    """

    def __init__(self, args: DISISNetIn):
        """
        Input arguments: `image_uri`, `return_mask` (optional), `background_color` (optional), `store` (optional)

        Output fields: `future.image_uri`

        https://substrate.run/library#DISISNet
        """
        super().__init__(**args)
        self.node = "DISISNet"

    def output(self, response: SubstrateResponse) -> DISISNetOut:
        """
        Retrieve this node's output from a response.

        Output fields: `future.image_uri`

        https://substrate.run/library#DISISNet
        """
        klass = DISISNetOut
        json = response.api_response.json
        if json and json.get("data"):
            data = json["data"]
            node_id = self.id
            if data.get(self.id):
                return klass(**data[self.id])
        raise ValueError(f"Node {self.id} not found in response")

    @property
    def future(self) -> FutureDISISNetOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.image_uri`

        https://substrate.run/library#DISISNet
        """
        return super().future  # type: ignore


class SegmentUnderPoint(CoreNode):
    """
    Segment an image under a point and return the segment.

    https://substrate.run/library#SegmentUnderPoint
    """

    def __init__(self, args: SegmentUnderPointIn):
        """
        Input arguments: `image_uri`, `point`, `store` (optional), `node` (optional)

        Output fields: `future.mask_image_uri`

        https://substrate.run/library#SegmentUnderPoint
        """
        super().__init__(**args)
        self.node = "SegmentUnderPoint"

    def output(self, response: SubstrateResponse) -> SegmentUnderPointOut:
        """
        Retrieve this node's output from a response.

        Output fields: `future.mask_image_uri`

        https://substrate.run/library#SegmentUnderPoint
        """
        klass = SegmentUnderPointOut
        json = response.api_response.json
        if json and json.get("data"):
            data = json["data"]
            node_id = self.id
            if data.get(self.id):
                return klass(**data[self.id])
        raise ValueError(f"Node {self.id} not found in response")

    @property
    def future(self) -> FutureSegmentUnderPointOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.mask_image_uri`

        https://substrate.run/library#SegmentUnderPoint
        """
        return super().future  # type: ignore


class SegmentAnything(CoreNode):
    """
    Segment an image using [SegmentAnything](https://github.com/facebookresearch/segment-anything).

    https://substrate.run/library#SegmentAnything
    """

    def __init__(self, args: SegmentAnythingIn):
        """
        Input arguments: `image_uri`, `point_prompts` (optional), `box_prompts` (optional), `store` (optional)

        Output fields: `future.mask_image_uri`

        https://substrate.run/library#SegmentAnything
        """
        super().__init__(**args)
        self.node = "SegmentAnything"

    def output(self, response: SubstrateResponse) -> SegmentAnythingOut:
        """
        Retrieve this node's output from a response.

        Output fields: `future.mask_image_uri`

        https://substrate.run/library#SegmentAnything
        """
        klass = SegmentAnythingOut
        json = response.api_response.json
        if json and json.get("data"):
            data = json["data"]
            node_id = self.id
            if data.get(self.id):
                return klass(**data[self.id])
        raise ValueError(f"Node {self.id} not found in response")

    @property
    def future(self) -> FutureSegmentAnythingOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.mask_image_uri`

        https://substrate.run/library#SegmentAnything
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
        Input arguments: `text`, `store` (optional), `node` (optional)

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


class XTTSV2(CoreNode):
    """
    Generate speech from text using [XTTS v2](https://docs.coqui.ai/en/latest/models/xtts.html).

    https://substrate.run/library#XTTSV2
    """

    def __init__(self, args: XTTSV2In):
        """
        Input arguments: `text`, `audio_uri` (optional), `language` (optional), `store` (optional)

        Output fields: `future.audio_uri`

        https://substrate.run/library#XTTSV2
        """
        super().__init__(**args)
        self.node = "XTTSV2"

    def output(self, response: SubstrateResponse) -> XTTSV2Out:
        """
        Retrieve this node's output from a response.

        Output fields: `future.audio_uri`

        https://substrate.run/library#XTTSV2
        """
        klass = XTTSV2Out
        json = response.api_response.json
        if json and json.get("data"):
            data = json["data"]
            node_id = self.id
            if data.get(self.id):
                return klass(**data[self.id])
        raise ValueError(f"Node {self.id} not found in response")

    @property
    def future(self) -> FutureXTTSV2Out:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.audio_uri`

        https://substrate.run/library#XTTSV2
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
    Generate embeddings for multiple text documents using [Jina Embeddings 2](https://arxiv.org/abs/2310.19923).

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
    Generate embeddings for text or images using [CLIP](https://openai.com/research/clip).

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


class CreateVectorStore(CoreNode):
    """
    Create a vector store for storing and querying embeddings.

    https://substrate.run/library#CreateVectorStore
    """

    def __init__(self, args: CreateVectorStoreIn):
        """
        Input arguments: `name`, `model`, `m` (optional), `ef_construction` (optional), `metric` (optional)

        Output fields: `future.name`, `future.model`, `future.m`, `future.ef_construction`, `future.metric`

        https://substrate.run/library#CreateVectorStore
        """
        super().__init__(**args)
        self.node = "CreateVectorStore"

    def output(self, response: SubstrateResponse) -> CreateVectorStoreOut:
        """
        Retrieve this node's output from a response.

        Output fields: `future.name`, `future.model`, `future.m`, `future.ef_construction`, `future.metric`

        https://substrate.run/library#CreateVectorStore
        """
        klass = CreateVectorStoreOut
        json = response.api_response.json
        if json and json.get("data"):
            data = json["data"]
            node_id = self.id
            if data.get(self.id):
                return klass(**data[self.id])
        raise ValueError(f"Node {self.id} not found in response")

    @property
    def future(self) -> FutureCreateVectorStoreOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.name`, `future.model`, `future.m`, `future.ef_construction`, `future.metric`

        https://substrate.run/library#CreateVectorStore
        """
        return super().future  # type: ignore


class ListVectorStores(CoreNode):
    """
    List all vector stores.

    https://substrate.run/library#ListVectorStores
    """

    def __init__(self, args: ListVectorStoresIn):
        """
        Input arguments:

        Output fields: `future.stores` (optional)

        https://substrate.run/library#ListVectorStores
        """
        super().__init__(**args)
        self.node = "ListVectorStores"

    def output(self, response: SubstrateResponse) -> ListVectorStoresOut:
        """
        Retrieve this node's output from a response.

        Output fields: `future.stores` (optional)

        https://substrate.run/library#ListVectorStores
        """
        klass = ListVectorStoresOut
        json = response.api_response.json
        if json and json.get("data"):
            data = json["data"]
            node_id = self.id
            if data.get(self.id):
                return klass(**data[self.id])
        raise ValueError(f"Node {self.id} not found in response")

    @property
    def future(self) -> FutureListVectorStoresOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.stores` (optional)

        https://substrate.run/library#ListVectorStores
        """
        return super().future  # type: ignore


class DeleteVectorStore(CoreNode):
    """
    Delete a vector store.

    https://substrate.run/library#DeleteVectorStore
    """

    def __init__(self, args: DeleteVectorStoreIn):
        """
        Input arguments: `name`, `model`

        Output fields: `future.name`, `future.model`

        https://substrate.run/library#DeleteVectorStore
        """
        super().__init__(**args)
        self.node = "DeleteVectorStore"

    def output(self, response: SubstrateResponse) -> DeleteVectorStoreOut:
        """
        Retrieve this node's output from a response.

        Output fields: `future.name`, `future.model`

        https://substrate.run/library#DeleteVectorStore
        """
        klass = DeleteVectorStoreOut
        json = response.api_response.json
        if json and json.get("data"):
            data = json["data"]
            node_id = self.id
            if data.get(self.id):
                return klass(**data[self.id])
        raise ValueError(f"Node {self.id} not found in response")

    @property
    def future(self) -> FutureDeleteVectorStoreOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.name`, `future.model`

        https://substrate.run/library#DeleteVectorStore
        """
        return super().future  # type: ignore


class QueryVectorStore(CoreNode):
    """
    Query a vector store for similar vectors.

    https://substrate.run/library#QueryVectorStore
    """

    def __init__(self, args: QueryVectorStoreIn):
        """
        Input arguments: `name`, `model`, `query_ids` (optional), `query_image_uris` (optional), `query_vectors` (optional), `query_strings` (optional), `top_k` (optional), `ef_search` (optional), `include_values` (optional), `include_metadata` (optional), `filters` (optional)

        Output fields: `future.results`, `future.name` (optional), `future.model` (optional), `future.metric` (optional)

        https://substrate.run/library#QueryVectorStore
        """
        super().__init__(**args)
        self.node = "QueryVectorStore"

    def output(self, response: SubstrateResponse) -> QueryVectorStoreOut:
        """
        Retrieve this node's output from a response.

        Output fields: `future.results`, `future.name` (optional), `future.model` (optional), `future.metric` (optional)

        https://substrate.run/library#QueryVectorStore
        """
        klass = QueryVectorStoreOut
        json = response.api_response.json
        if json and json.get("data"):
            data = json["data"]
            node_id = self.id
            if data.get(self.id):
                return klass(**data[self.id])
        raise ValueError(f"Node {self.id} not found in response")

    @property
    def future(self) -> FutureQueryVectorStoreOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.results`, `future.name` (optional), `future.model` (optional), `future.metric` (optional)

        https://substrate.run/library#QueryVectorStore
        """
        return super().future  # type: ignore


class FetchVectors(CoreNode):
    """
    Fetch vectors from a vector store.

    https://substrate.run/library#FetchVectors
    """

    def __init__(self, args: FetchVectorsIn):
        """
        Input arguments: `name`, `model`, `ids`

        Output fields: `future.vectors`

        https://substrate.run/library#FetchVectors
        """
        super().__init__(**args)
        self.node = "FetchVectors"

    def output(self, response: SubstrateResponse) -> FetchVectorsOut:
        """
        Retrieve this node's output from a response.

        Output fields: `future.vectors`

        https://substrate.run/library#FetchVectors
        """
        klass = FetchVectorsOut
        json = response.api_response.json
        if json and json.get("data"):
            data = json["data"]
            node_id = self.id
            if data.get(self.id):
                return klass(**data[self.id])
        raise ValueError(f"Node {self.id} not found in response")

    @property
    def future(self) -> FutureFetchVectorsOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.vectors`

        https://substrate.run/library#FetchVectors
        """
        return super().future  # type: ignore


class UpdateVectors(CoreNode):
    """
    Update vectors in a vector store.

    https://substrate.run/library#UpdateVectors
    """

    def __init__(self, args: UpdateVectorsIn):
        """
        Input arguments: `name`, `model`, `vectors`

        Output fields: `future.count`

        https://substrate.run/library#UpdateVectors
        """
        super().__init__(**args)
        self.node = "UpdateVectors"

    def output(self, response: SubstrateResponse) -> UpdateVectorsOut:
        """
        Retrieve this node's output from a response.

        Output fields: `future.count`

        https://substrate.run/library#UpdateVectors
        """
        klass = UpdateVectorsOut
        json = response.api_response.json
        if json and json.get("data"):
            data = json["data"]
            node_id = self.id
            if data.get(self.id):
                return klass(**data[self.id])
        raise ValueError(f"Node {self.id} not found in response")

    @property
    def future(self) -> FutureUpdateVectorsOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.count`

        https://substrate.run/library#UpdateVectors
        """
        return super().future  # type: ignore


class DeleteVectors(CoreNode):
    """
    Delete vectors in a vector store.

    https://substrate.run/library#DeleteVectors
    """

    def __init__(self, args: DeleteVectorsIn):
        """
        Input arguments: `name`, `model`, `ids`

        Output fields: `future.count`

        https://substrate.run/library#DeleteVectors
        """
        super().__init__(**args)
        self.node = "DeleteVectors"

    def output(self, response: SubstrateResponse) -> DeleteVectorsOut:
        """
        Retrieve this node's output from a response.

        Output fields: `future.count`

        https://substrate.run/library#DeleteVectors
        """
        klass = DeleteVectorsOut
        json = response.api_response.json
        if json and json.get("data"):
            data = json["data"]
            node_id = self.id
            if data.get(self.id):
                return klass(**data[self.id])
        raise ValueError(f"Node {self.id} not found in response")

    @property
    def future(self) -> FutureDeleteVectorsOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.count`

        https://substrate.run/library#DeleteVectors
        """
        return super().future  # type: ignore
