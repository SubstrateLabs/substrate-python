"""
꩜ Substrate
@GENERATED FILE
20240502.20240502
"""

from .core.models import (
    CLIPOut,
    JinaV2Out,
    XTTSV2Out,
    RunCodeOut,
    FillMaskOut,
    EmbedTextOut,
    EmbedImageOut,
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
    Llama3Instruct8BOut,
    QueryVectorStoreOut,
    RemoveBackgroundOut,
    BatchGenerateJSONOut,
    BatchGenerateTextOut,
    CreateVectorStoreOut,
    DeleteVectorStoreOut,
    Llama3Instruct70BOut,
    Mistral7BInstructOut,
    MultiGenerateJSONOut,
    MultiGenerateTextOut,
    SegmentUnderPointOut,
    StableDiffusionXLOut,
    GenerateTextVisionOut,
    MultiGenerateImageOut,
    GenerativeEditImageOut,
    Mixtral8x7BInstructOut,
    MultiGenerativeEditImageOut,
    StableDiffusionXLInpaintOut,
    StableDiffusionXLIPAdapterOut,
    StableDiffusionXLLightningOut,
    StableDiffusionXLControlNetOut,
)
from .core.corenode import CoreNode
from .typeddict_models import (
    CLIPIn,
    JinaV2In,
    XTTSV2In,
    RunCodeIn,
    FillMaskIn,
    EmbedTextIn,
    EmbedImageIn,
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
    Llama3Instruct8BIn,
    QueryVectorStoreIn,
    RemoveBackgroundIn,
    BatchGenerateJSONIn,
    BatchGenerateTextIn,
    CreateVectorStoreIn,
    DeleteVectorStoreIn,
    Llama3Instruct70BIn,
    Mistral7BInstructIn,
    MultiGenerateJSONIn,
    MultiGenerateTextIn,
    SegmentUnderPointIn,
    StableDiffusionXLIn,
    GenerateTextVisionIn,
    MultiGenerateImageIn,
    GenerativeEditImageIn,
    Mixtral8x7BInstructIn,
    MultiGenerativeEditImageIn,
    StableDiffusionXLInpaintIn,
    StableDiffusionXLIPAdapterIn,
    StableDiffusionXLLightningIn,
    StableDiffusionXLControlNetIn,
)
from .future_dataclass_models import (
    FutureCLIPOut,
    FutureJinaV2Out,
    FutureXTTSV2Out,
    FutureRunCodeOut,
    FutureFillMaskOut,
    FutureEmbedTextOut,
    FutureEmbedImageOut,
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
    FutureLlama3Instruct8BOut,
    FutureQueryVectorStoreOut,
    FutureRemoveBackgroundOut,
    FutureBatchGenerateJSONOut,
    FutureBatchGenerateTextOut,
    FutureCreateVectorStoreOut,
    FutureDeleteVectorStoreOut,
    FutureLlama3Instruct70BOut,
    FutureMistral7BInstructOut,
    FutureMultiGenerateJSONOut,
    FutureMultiGenerateTextOut,
    FutureSegmentUnderPointOut,
    FutureStableDiffusionXLOut,
    FutureGenerateTextVisionOut,
    FutureMultiGenerateImageOut,
    FutureGenerativeEditImageOut,
    FutureMixtral8x7BInstructOut,
    FutureMultiGenerativeEditImageOut,
    FutureStableDiffusionXLInpaintOut,
    FutureStableDiffusionXLIPAdapterOut,
    FutureStableDiffusionXLLightningOut,
    FutureStableDiffusionXLControlNetOut,
)


class RunCode(CoreNode[RunCodeOut]):
    """
    Evaluate code using a code interpreter.

    https://substrate.run/library#RunCode
    """

    def __init__(self, args: RunCodeIn, hide: bool = False):
        """
        Input arguments: `code`, `args` (optional), `language` (optional)

        Output fields: `future.output` (optional), `future.json_output`, `future.error` (optional)

        https://substrate.run/library#RunCode
        """
        super().__init__(hide=hide, out_type=RunCodeOut, **args)
        self.node = "RunCode"

    @property
    def future(self) -> FutureRunCodeOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.output` (optional), `future.json_output`, `future.error` (optional)

        https://substrate.run/library#RunCode
        """
        return super().future  # type: ignore


class GenerateText(CoreNode[GenerateTextOut]):
    """
    Generate text using a language model.

    https://substrate.run/library#GenerateText
    """

    def __init__(self, args: GenerateTextIn, hide: bool = False):
        """
        Input arguments: `prompt`, `temperature` (optional), `max_tokens` (optional), `node` (optional)

        Output fields: `future.text`

        https://substrate.run/library#GenerateText
        """
        super().__init__(hide=hide, out_type=GenerateTextOut, **args)
        self.node = "GenerateText"

    @property
    def future(self) -> FutureGenerateTextOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.text`

        https://substrate.run/library#GenerateText
        """
        return super().future  # type: ignore


class MultiGenerateText(CoreNode[MultiGenerateTextOut]):
    """
    Generate multiple text choices using a language model.

    https://substrate.run/library#MultiGenerateText
    """

    def __init__(self, args: MultiGenerateTextIn, hide: bool = False):
        """
        Input arguments: `prompt`, `num_choices`, `temperature` (optional), `max_tokens` (optional), `node` (optional)

        Output fields: `future.choices`

        https://substrate.run/library#MultiGenerateText
        """
        super().__init__(hide=hide, out_type=MultiGenerateTextOut, **args)
        self.node = "MultiGenerateText"

    @property
    def future(self) -> FutureMultiGenerateTextOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.choices`

        https://substrate.run/library#MultiGenerateText
        """
        return super().future  # type: ignore


class BatchGenerateText(CoreNode[BatchGenerateTextOut]):
    """
    Generate text for multiple prompts in batch using a language model.

    https://substrate.run/library#BatchGenerateText
    """

    def __init__(self, args: BatchGenerateTextIn, hide: bool = False):
        """
        Input arguments: `prompts`, `temperature` (optional), `max_tokens` (optional)

        Output fields: `future.outputs`

        https://substrate.run/library#BatchGenerateText
        """
        super().__init__(hide=hide, out_type=BatchGenerateTextOut, **args)
        self.node = "BatchGenerateText"

    @property
    def future(self) -> FutureBatchGenerateTextOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.outputs`

        https://substrate.run/library#BatchGenerateText
        """
        return super().future  # type: ignore


class BatchGenerateJSON(CoreNode[BatchGenerateJSONOut]):
    """
    Generate JSON for multiple prompts in batch using a language model.

    https://substrate.run/library#BatchGenerateJSON
    """

    def __init__(self, args: BatchGenerateJSONIn, hide: bool = False):
        """
        Input arguments: `prompts`, `json_schema`, `temperature` (optional), `max_tokens` (optional)

        Output fields: `future.outputs`

        https://substrate.run/library#BatchGenerateJSON
        """
        super().__init__(hide=hide, out_type=BatchGenerateJSONOut, **args)
        self.node = "BatchGenerateJSON"

    @property
    def future(self) -> FutureBatchGenerateJSONOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.outputs`

        https://substrate.run/library#BatchGenerateJSON
        """
        return super().future  # type: ignore


class GenerateJSON(CoreNode[GenerateJSONOut]):
    """
    Generate JSON using a language model.

    https://substrate.run/library#GenerateJSON
    """

    def __init__(self, args: GenerateJSONIn, hide: bool = False):
        """
        Input arguments: `prompt`, `json_schema`, `temperature` (optional), `max_tokens` (optional), `node` (optional)

        Output fields: `future.json_object`

        https://substrate.run/library#GenerateJSON
        """
        super().__init__(hide=hide, out_type=GenerateJSONOut, **args)
        self.node = "GenerateJSON"

    @property
    def future(self) -> FutureGenerateJSONOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.json_object`

        https://substrate.run/library#GenerateJSON
        """
        return super().future  # type: ignore


class MultiGenerateJSON(CoreNode[MultiGenerateJSONOut]):
    """
    Generate multiple JSON choices using a language model.

    https://substrate.run/library#MultiGenerateJSON
    """

    def __init__(self, args: MultiGenerateJSONIn, hide: bool = False):
        """
        Input arguments: `prompt`, `json_schema`, `num_choices`, `temperature` (optional), `max_tokens` (optional), `node` (optional)

        Output fields: `future.choices`

        https://substrate.run/library#MultiGenerateJSON
        """
        super().__init__(hide=hide, out_type=MultiGenerateJSONOut, **args)
        self.node = "MultiGenerateJSON"

    @property
    def future(self) -> FutureMultiGenerateJSONOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.choices`

        https://substrate.run/library#MultiGenerateJSON
        """
        return super().future  # type: ignore


class GenerateTextVision(CoreNode[GenerateTextVisionOut]):
    """
    Generate text with image input.

    https://substrate.run/library#GenerateTextVision
    """

    def __init__(self, args: GenerateTextVisionIn, hide: bool = False):
        """
        Input arguments: `prompt`, `image_uris`, `max_tokens` (optional)

        Output fields: `future.text`

        https://substrate.run/library#GenerateTextVision
        """
        super().__init__(hide=hide, out_type=GenerateTextVisionOut, **args)
        self.node = "GenerateTextVision"

    @property
    def future(self) -> FutureGenerateTextVisionOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.text`

        https://substrate.run/library#GenerateTextVision
        """
        return super().future  # type: ignore


class Mistral7BInstruct(CoreNode[Mistral7BInstructOut]):
    """
    Generate text using [Mistral 7B Instruct](https://mistral.ai/news/announcing-mistral-7b).

    https://substrate.run/library#Mistral7BInstruct
    """

    def __init__(self, args: Mistral7BInstructIn, hide: bool = False):
        """
        Input arguments: `prompt`, `num_choices` (optional), `json_schema` (optional), `temperature` (optional), `max_tokens` (optional)

        Output fields: `future.choices`

        https://substrate.run/library#Mistral7BInstruct
        """
        super().__init__(hide=hide, out_type=Mistral7BInstructOut, **args)
        self.node = "Mistral7BInstruct"

    @property
    def future(self) -> FutureMistral7BInstructOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.choices`

        https://substrate.run/library#Mistral7BInstruct
        """
        return super().future  # type: ignore


class Mixtral8x7BInstruct(CoreNode[Mixtral8x7BInstructOut]):
    """
    Generate text using instruct-tuned [Mixtral 8x7B](https://mistral.ai/news/mixtral-of-experts/).

    https://substrate.run/library#Mixtral8x7BInstruct
    """

    def __init__(self, args: Mixtral8x7BInstructIn, hide: bool = False):
        """
        Input arguments: `prompt`, `num_choices` (optional), `json_schema` (optional), `temperature` (optional), `max_tokens` (optional)

        Output fields: `future.choices`

        https://substrate.run/library#Mixtral8x7BInstruct
        """
        super().__init__(hide=hide, out_type=Mixtral8x7BInstructOut, **args)
        self.node = "Mixtral8x7BInstruct"

    @property
    def future(self) -> FutureMixtral8x7BInstructOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.choices`

        https://substrate.run/library#Mixtral8x7BInstruct
        """
        return super().future  # type: ignore


class Llama3Instruct8B(CoreNode[Llama3Instruct8BOut]):
    """
    Generate text using instruct-tuned [Llama 3 8B](https://llama.meta.com/llama3/).

    https://substrate.run/library#Llama3Instruct8B
    """

    def __init__(self, args: Llama3Instruct8BIn, hide: bool = False):
        """
        Input arguments: `prompt`, `num_choices` (optional), `temperature` (optional), `max_tokens` (optional)

        Output fields: `future.choices`

        https://substrate.run/library#Llama3Instruct8B
        """
        super().__init__(hide=hide, out_type=Llama3Instruct8BOut, **args)
        self.node = "Llama3Instruct8B"

    @property
    def future(self) -> FutureLlama3Instruct8BOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.choices`

        https://substrate.run/library#Llama3Instruct8B
        """
        return super().future  # type: ignore


class Llama3Instruct70B(CoreNode[Llama3Instruct70BOut]):
    """
    Generate text using instruct-tuned [Llama 3 70B](https://llama.meta.com/llama3/).

    https://substrate.run/library#Llama3Instruct70B
    """

    def __init__(self, args: Llama3Instruct70BIn, hide: bool = False):
        """
        Input arguments: `prompt`, `num_choices` (optional), `temperature` (optional), `max_tokens` (optional)

        Output fields: `future.choices`

        https://substrate.run/library#Llama3Instruct70B
        """
        super().__init__(hide=hide, out_type=Llama3Instruct70BOut, **args)
        self.node = "Llama3Instruct70B"

    @property
    def future(self) -> FutureLlama3Instruct70BOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.choices`

        https://substrate.run/library#Llama3Instruct70B
        """
        return super().future  # type: ignore


class Firellava13B(CoreNode[Firellava13BOut]):
    """
    Generate text with image input using [FireLLaVA 13B](https://fireworks.ai/blog/firellava-the-first-commercially-permissive-oss-llava-model).

    https://substrate.run/library#Firellava13B
    """

    def __init__(self, args: Firellava13BIn, hide: bool = False):
        """
        Input arguments: `prompt`, `image_uris`, `max_tokens` (optional)

        Output fields: `future.text`

        https://substrate.run/library#Firellava13B
        """
        super().__init__(hide=hide, out_type=Firellava13BOut, **args)
        self.node = "Firellava13B"

    @property
    def future(self) -> FutureFirellava13BOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.text`

        https://substrate.run/library#Firellava13B
        """
        return super().future  # type: ignore


class GenerateImage(CoreNode[GenerateImageOut]):
    """
    Generate an image.

    https://substrate.run/library#GenerateImage
    """

    def __init__(self, args: GenerateImageIn, hide: bool = False):
        """
        Input arguments: `prompt`, `store` (optional)

        Output fields: `future.image_uri`

        https://substrate.run/library#GenerateImage
        """
        super().__init__(hide=hide, out_type=GenerateImageOut, **args)
        self.node = "GenerateImage"

    @property
    def future(self) -> FutureGenerateImageOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.image_uri`

        https://substrate.run/library#GenerateImage
        """
        return super().future  # type: ignore


class MultiGenerateImage(CoreNode[MultiGenerateImageOut]):
    """
    Generate multiple images.

    https://substrate.run/library#MultiGenerateImage
    """

    def __init__(self, args: MultiGenerateImageIn, hide: bool = False):
        """
        Input arguments: `prompt`, `num_images`, `store` (optional)

        Output fields: `future.outputs`

        https://substrate.run/library#MultiGenerateImage
        """
        super().__init__(hide=hide, out_type=MultiGenerateImageOut, **args)
        self.node = "MultiGenerateImage"

    @property
    def future(self) -> FutureMultiGenerateImageOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.outputs`

        https://substrate.run/library#MultiGenerateImage
        """
        return super().future  # type: ignore


class GenerativeEditImage(CoreNode[GenerativeEditImageOut]):
    """
    Edit an image using image generation.

    https://substrate.run/library#GenerativeEditImage
    """

    def __init__(self, args: GenerativeEditImageIn, hide: bool = False):
        """
        Input arguments: `image_uri`, `prompt`, `mask_image_uri` (optional), `store` (optional)

        Output fields: `future.image_uri`

        https://substrate.run/library#GenerativeEditImage
        """
        super().__init__(hide=hide, out_type=GenerativeEditImageOut, **args)
        self.node = "GenerativeEditImage"

    @property
    def future(self) -> FutureGenerativeEditImageOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.image_uri`

        https://substrate.run/library#GenerativeEditImage
        """
        return super().future  # type: ignore


class MultiGenerativeEditImage(CoreNode[MultiGenerativeEditImageOut]):
    """
    Edit multiple images using image generation.

    https://substrate.run/library#MultiGenerativeEditImage
    """

    def __init__(self, args: MultiGenerativeEditImageIn, hide: bool = False):
        """
        Input arguments: `image_uri`, `prompt`, `mask_image_uri` (optional), `num_images`, `store` (optional)

        Output fields: `future.outputs`

        https://substrate.run/library#MultiGenerativeEditImage
        """
        super().__init__(hide=hide, out_type=MultiGenerativeEditImageOut, **args)
        self.node = "MultiGenerativeEditImage"

    @property
    def future(self) -> FutureMultiGenerativeEditImageOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.outputs`

        https://substrate.run/library#MultiGenerativeEditImage
        """
        return super().future  # type: ignore


class StableDiffusionXL(CoreNode[StableDiffusionXLOut]):
    """
    Generate an image using [Stable Diffusion XL](https://arxiv.org/abs/2307.01952).

    https://substrate.run/library#StableDiffusionXL
    """

    def __init__(self, args: StableDiffusionXLIn, hide: bool = False):
        """
        Input arguments: `prompt`, `negative_prompt` (optional), `steps` (optional), `num_images`, `store` (optional), `height` (optional), `width` (optional), `seeds` (optional), `guidance_scale` (optional)

        Output fields: `future.outputs`

        https://substrate.run/library#StableDiffusionXL
        """
        super().__init__(hide=hide, out_type=StableDiffusionXLOut, **args)
        self.node = "StableDiffusionXL"

    @property
    def future(self) -> FutureStableDiffusionXLOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.outputs`

        https://substrate.run/library#StableDiffusionXL
        """
        return super().future  # type: ignore


class StableDiffusionXLLightning(CoreNode[StableDiffusionXLLightningOut]):
    """
    Generate an image using [Stable Diffusion XL Lightning](https://arxiv.org/abs/2402.13929).

    https://substrate.run/library#StableDiffusionXLLightning
    """

    def __init__(self, args: StableDiffusionXLLightningIn, hide: bool = False):
        """
        Input arguments: `prompt`, `negative_prompt` (optional), `num_images` (optional), `store` (optional), `height` (optional), `width` (optional), `seeds` (optional)

        Output fields: `future.outputs`

        https://substrate.run/library#StableDiffusionXLLightning
        """
        super().__init__(hide=hide, out_type=StableDiffusionXLLightningOut, **args)
        self.node = "StableDiffusionXLLightning"

    @property
    def future(self) -> FutureStableDiffusionXLLightningOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.outputs`

        https://substrate.run/library#StableDiffusionXLLightning
        """
        return super().future  # type: ignore


class StableDiffusionXLInpaint(CoreNode[StableDiffusionXLInpaintOut]):
    """
    Edit an image using [Stable Diffusion XL](https://arxiv.org/abs/2307.01952). Supports inpainting (edit part of the image with a mask) and image-to-image (edit the full image).

    https://substrate.run/library#StableDiffusionXLInpaint
    """

    def __init__(self, args: StableDiffusionXLInpaintIn, hide: bool = False):
        """
        Input arguments: `image_uri`, `prompt`, `mask_image_uri` (optional), `num_images`, `output_resolution` (optional), `negative_prompt` (optional), `store` (optional), `strength` (optional), `seeds` (optional)

        Output fields: `future.outputs`

        https://substrate.run/library#StableDiffusionXLInpaint
        """
        super().__init__(hide=hide, out_type=StableDiffusionXLInpaintOut, **args)
        self.node = "StableDiffusionXLInpaint"

    @property
    def future(self) -> FutureStableDiffusionXLInpaintOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.outputs`

        https://substrate.run/library#StableDiffusionXLInpaint
        """
        return super().future  # type: ignore


class StableDiffusionXLControlNet(CoreNode[StableDiffusionXLControlNetOut]):
    """
    Generate an image with generation structured by an input image, using Stable Diffusion XL with [ControlNet](https://arxiv.org/abs/2302.05543).

    https://substrate.run/library#StableDiffusionXLControlNet
    """

    def __init__(self, args: StableDiffusionXLControlNetIn, hide: bool = False):
        """
        Input arguments: `image_uri`, `control_method`, `prompt`, `num_images`, `output_resolution` (optional), `negative_prompt` (optional), `store` (optional), `conditioning_scale` (optional), `seeds` (optional)

        Output fields: `future.outputs`

        https://substrate.run/library#StableDiffusionXLControlNet
        """
        super().__init__(hide=hide, out_type=StableDiffusionXLControlNetOut, **args)
        self.node = "StableDiffusionXLControlNet"

    @property
    def future(self) -> FutureStableDiffusionXLControlNetOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.outputs`

        https://substrate.run/library#StableDiffusionXLControlNet
        """
        return super().future  # type: ignore


class StableDiffusionXLIPAdapter(CoreNode[StableDiffusionXLIPAdapterOut]):
    """
    Generate an image with an image prompt, using Stable Diffusion XL with [IP-Adapter](https://arxiv.org/abs/2308.06721).

    https://substrate.run/library#StableDiffusionXLIPAdapter
    """

    def __init__(self, args: StableDiffusionXLIPAdapterIn, hide: bool = False):
        """
        Input arguments: `prompt`, `image_prompt_uri` (optional), `num_images`, `ip_adapter_scale` (optional), `negative_prompt` (optional), `store` (optional), `width` (optional), `height` (optional), `seeds` (optional)

        Output fields: `future.outputs`

        https://substrate.run/library#StableDiffusionXLIPAdapter
        """
        super().__init__(hide=hide, out_type=StableDiffusionXLIPAdapterOut, **args)
        self.node = "StableDiffusionXLIPAdapter"

    @property
    def future(self) -> FutureStableDiffusionXLIPAdapterOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.outputs`

        https://substrate.run/library#StableDiffusionXLIPAdapter
        """
        return super().future  # type: ignore


class TranscribeMedia(CoreNode[TranscribeMediaOut]):
    """
    Transcribe speech in an audio or video file.

    https://substrate.run/library#TranscribeMedia
    """

    def __init__(self, args: TranscribeMediaIn, hide: bool = False):
        """
        Input arguments: `audio_uri`, `prompt` (optional), `language` (optional), `segment` (optional), `align` (optional), `diarize` (optional), `suggest_chapters` (optional)

        Output fields: `future.text`, `future.segments` (optional), `future.chapters` (optional)

        https://substrate.run/library#TranscribeMedia
        """
        super().__init__(hide=hide, out_type=TranscribeMediaOut, **args)
        self.node = "TranscribeMedia"

    @property
    def future(self) -> FutureTranscribeMediaOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.text`, `future.segments` (optional), `future.chapters` (optional)

        https://substrate.run/library#TranscribeMedia
        """
        return super().future  # type: ignore


class GenerateSpeech(CoreNode[GenerateSpeechOut]):
    """
    Generate speech from text.

    https://substrate.run/library#GenerateSpeech
    """

    def __init__(self, args: GenerateSpeechIn, hide: bool = False):
        """
        Input arguments: `text`, `store` (optional)

        Output fields: `future.audio_uri`

        https://substrate.run/library#GenerateSpeech
        """
        super().__init__(hide=hide, out_type=GenerateSpeechOut, **args)
        self.node = "GenerateSpeech"

    @property
    def future(self) -> FutureGenerateSpeechOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.audio_uri`

        https://substrate.run/library#GenerateSpeech
        """
        return super().future  # type: ignore


class XTTSV2(CoreNode[XTTSV2Out]):
    """
    Generate speech from text using [XTTS v2](https://docs.coqui.ai/en/latest/models/xtts.html).

    https://substrate.run/library#XTTSV2
    """

    def __init__(self, args: XTTSV2In, hide: bool = False):
        """
        Input arguments: `text`, `audio_uri` (optional), `language` (optional), `store` (optional)

        Output fields: `future.audio_uri`

        https://substrate.run/library#XTTSV2
        """
        super().__init__(hide=hide, out_type=XTTSV2Out, **args)
        self.node = "XTTSV2"

    @property
    def future(self) -> FutureXTTSV2Out:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.audio_uri`

        https://substrate.run/library#XTTSV2
        """
        return super().future  # type: ignore


class RemoveBackground(CoreNode[RemoveBackgroundOut]):
    """
    Remove the background from an image, with the option to return the foreground as a mask.

    https://substrate.run/library#RemoveBackground
    """

    def __init__(self, args: RemoveBackgroundIn, hide: bool = False):
        """
        Input arguments: `image_uri`, `return_mask` (optional), `background_color` (optional), `store` (optional)

        Output fields: `future.image_uri`

        https://substrate.run/library#RemoveBackground
        """
        super().__init__(hide=hide, out_type=RemoveBackgroundOut, **args)
        self.node = "RemoveBackground"

    @property
    def future(self) -> FutureRemoveBackgroundOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.image_uri`

        https://substrate.run/library#RemoveBackground
        """
        return super().future  # type: ignore


class FillMask(CoreNode[FillMaskOut]):
    """
    Fill (inpaint) part of an image, e.g. to 'remove' an object.

    https://substrate.run/library#FillMask
    """

    def __init__(self, args: FillMaskIn, hide: bool = False):
        """
        Input arguments: `image_uri`, `mask_image_uri`, `store` (optional)

        Output fields: `future.image_uri`

        https://substrate.run/library#FillMask
        """
        super().__init__(hide=hide, out_type=FillMaskOut, **args)
        self.node = "FillMask"

    @property
    def future(self) -> FutureFillMaskOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.image_uri`

        https://substrate.run/library#FillMask
        """
        return super().future  # type: ignore


class UpscaleImage(CoreNode[UpscaleImageOut]):
    """
    Upscale an image.

    https://substrate.run/library#UpscaleImage
    """

    def __init__(self, args: UpscaleImageIn, hide: bool = False):
        """
        Input arguments: `image_uri`, `store` (optional)

        Output fields: `future.image_uri`

        https://substrate.run/library#UpscaleImage
        """
        super().__init__(hide=hide, out_type=UpscaleImageOut, **args)
        self.node = "UpscaleImage"

    @property
    def future(self) -> FutureUpscaleImageOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.image_uri`

        https://substrate.run/library#UpscaleImage
        """
        return super().future  # type: ignore


class SegmentUnderPoint(CoreNode[SegmentUnderPointOut]):
    """
    Segment an image under a point and return the segment.

    https://substrate.run/library#SegmentUnderPoint
    """

    def __init__(self, args: SegmentUnderPointIn, hide: bool = False):
        """
        Input arguments: `image_uri`, `point`, `store` (optional)

        Output fields: `future.mask_image_uri`

        https://substrate.run/library#SegmentUnderPoint
        """
        super().__init__(hide=hide, out_type=SegmentUnderPointOut, **args)
        self.node = "SegmentUnderPoint"

    @property
    def future(self) -> FutureSegmentUnderPointOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.mask_image_uri`

        https://substrate.run/library#SegmentUnderPoint
        """
        return super().future  # type: ignore


class SegmentAnything(CoreNode[SegmentAnythingOut]):
    """
    Segment an image using [SegmentAnything](https://github.com/facebookresearch/segment-anything).

    https://substrate.run/library#SegmentAnything
    """

    def __init__(self, args: SegmentAnythingIn, hide: bool = False):
        """
        Input arguments: `image_uri`, `point_prompts` (optional), `box_prompts` (optional), `store` (optional)

        Output fields: `future.mask_image_uri`

        https://substrate.run/library#SegmentAnything
        """
        super().__init__(hide=hide, out_type=SegmentAnythingOut, **args)
        self.node = "SegmentAnything"

    @property
    def future(self) -> FutureSegmentAnythingOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.mask_image_uri`

        https://substrate.run/library#SegmentAnything
        """
        return super().future  # type: ignore


class EmbedText(CoreNode[EmbedTextOut]):
    """
    Generate embedding for a text document.

    https://substrate.run/library#EmbedText
    """

    def __init__(self, args: EmbedTextIn, hide: bool = False):
        """
        Input arguments: `text`, `collection_name` (optional), `metadata` (optional), `embedded_metadata_keys` (optional), `doc_id` (optional), `model` (optional)

        Output fields: `future.embedding`

        https://substrate.run/library#EmbedText
        """
        super().__init__(hide=hide, out_type=EmbedTextOut, **args)
        self.node = "EmbedText"

    @property
    def future(self) -> FutureEmbedTextOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.embedding`

        https://substrate.run/library#EmbedText
        """
        return super().future  # type: ignore


class MultiEmbedText(CoreNode[MultiEmbedTextOut]):
    """
    Generate embeddings for multiple text documents.

    https://substrate.run/library#MultiEmbedText
    """

    def __init__(self, args: MultiEmbedTextIn, hide: bool = False):
        """
        Input arguments: `items`, `collection_name` (optional), `embedded_metadata_keys` (optional), `model` (optional)

        Output fields: `future.embeddings`

        https://substrate.run/library#MultiEmbedText
        """
        super().__init__(hide=hide, out_type=MultiEmbedTextOut, **args)
        self.node = "MultiEmbedText"

    @property
    def future(self) -> FutureMultiEmbedTextOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.embeddings`

        https://substrate.run/library#MultiEmbedText
        """
        return super().future  # type: ignore


class EmbedImage(CoreNode[EmbedImageOut]):
    """
    Generate embedding for an image.

    https://substrate.run/library#EmbedImage
    """

    def __init__(self, args: EmbedImageIn, hide: bool = False):
        """
        Input arguments: `image_uri`, `collection_name` (optional), `doc_id` (optional), `model` (optional)

        Output fields: `future.embedding`

        https://substrate.run/library#EmbedImage
        """
        super().__init__(hide=hide, out_type=EmbedImageOut, **args)
        self.node = "EmbedImage"

    @property
    def future(self) -> FutureEmbedImageOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.embedding`

        https://substrate.run/library#EmbedImage
        """
        return super().future  # type: ignore


class MultiEmbedImage(CoreNode[MultiEmbedImageOut]):
    """
    Generate embeddings for multiple images.

    https://substrate.run/library#MultiEmbedImage
    """

    def __init__(self, args: MultiEmbedImageIn, hide: bool = False):
        """
        Input arguments: `items`, `collection_name` (optional), `model` (optional)

        Output fields: `future.embeddings`

        https://substrate.run/library#MultiEmbedImage
        """
        super().__init__(hide=hide, out_type=MultiEmbedImageOut, **args)
        self.node = "MultiEmbedImage"

    @property
    def future(self) -> FutureMultiEmbedImageOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.embeddings`

        https://substrate.run/library#MultiEmbedImage
        """
        return super().future  # type: ignore


class JinaV2(CoreNode[JinaV2Out]):
    """
    Generate embeddings for multiple text documents using [Jina Embeddings 2](https://arxiv.org/abs/2310.19923).

    https://substrate.run/library#JinaV2
    """

    def __init__(self, args: JinaV2In, hide: bool = False):
        """
        Input arguments: `items`, `collection_name` (optional), `embedded_metadata_keys` (optional)

        Output fields: `future.embeddings`

        https://substrate.run/library#JinaV2
        """
        super().__init__(hide=hide, out_type=JinaV2Out, **args)
        self.node = "JinaV2"

    @property
    def future(self) -> FutureJinaV2Out:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.embeddings`

        https://substrate.run/library#JinaV2
        """
        return super().future  # type: ignore


class CLIP(CoreNode[CLIPOut]):
    """
    Generate embeddings for text or images using [CLIP](https://openai.com/research/clip).

    https://substrate.run/library#CLIP
    """

    def __init__(self, args: CLIPIn, hide: bool = False):
        """
        Input arguments: `items`, `collection_name` (optional), `embedded_metadata_keys` (optional)

        Output fields: `future.embeddings`

        https://substrate.run/library#CLIP
        """
        super().__init__(hide=hide, out_type=CLIPOut, **args)
        self.node = "CLIP"

    @property
    def future(self) -> FutureCLIPOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.embeddings`

        https://substrate.run/library#CLIP
        """
        return super().future  # type: ignore


class CreateVectorStore(CoreNode[CreateVectorStoreOut]):
    """
    Create a vector store for storing and querying embeddings.

    https://substrate.run/library#CreateVectorStore
    """

    def __init__(self, args: CreateVectorStoreIn, hide: bool = False):
        """
        Input arguments: `collection_name`, `model`, `m` (optional), `ef_construction` (optional), `metric` (optional)

        Output fields: `future.collection_name`, `future.model`, `future.m`, `future.ef_construction`, `future.metric`

        https://substrate.run/library#CreateVectorStore
        """
        super().__init__(hide=hide, out_type=CreateVectorStoreOut, **args)
        self.node = "CreateVectorStore"

    @property
    def future(self) -> FutureCreateVectorStoreOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.collection_name`, `future.model`, `future.m`, `future.ef_construction`, `future.metric`

        https://substrate.run/library#CreateVectorStore
        """
        return super().future  # type: ignore


class ListVectorStores(CoreNode[ListVectorStoresOut]):
    """
    List all vector stores.

    https://substrate.run/library#ListVectorStores
    """

    def __init__(self, args: ListVectorStoresIn, hide: bool = False):
        """
        Input arguments:

        Output fields: `future.items` (optional)

        https://substrate.run/library#ListVectorStores
        """
        super().__init__(hide=hide, out_type=ListVectorStoresOut, **args)
        self.node = "ListVectorStores"

    @property
    def future(self) -> FutureListVectorStoresOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.items` (optional)

        https://substrate.run/library#ListVectorStores
        """
        return super().future  # type: ignore


class DeleteVectorStore(CoreNode[DeleteVectorStoreOut]):
    """
    Delete a vector store.

    https://substrate.run/library#DeleteVectorStore
    """

    def __init__(self, args: DeleteVectorStoreIn, hide: bool = False):
        """
        Input arguments: `collection_name`, `model`

        Output fields: `future.collection_name`, `future.model`

        https://substrate.run/library#DeleteVectorStore
        """
        super().__init__(hide=hide, out_type=DeleteVectorStoreOut, **args)
        self.node = "DeleteVectorStore"

    @property
    def future(self) -> FutureDeleteVectorStoreOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.collection_name`, `future.model`

        https://substrate.run/library#DeleteVectorStore
        """
        return super().future  # type: ignore


class QueryVectorStore(CoreNode[QueryVectorStoreOut]):
    """
    Query a vector store for similar vectors.

    https://substrate.run/library#QueryVectorStore
    """

    def __init__(self, args: QueryVectorStoreIn, hide: bool = False):
        """
        Input arguments: `collection_name`, `model`, `query_strings` (optional), `query_image_uris` (optional), `query_vectors` (optional), `query_ids` (optional), `top_k` (optional), `ef_search` (optional), `include_values` (optional), `include_metadata` (optional), `filters` (optional)

        Output fields: `future.results`, `future.collection_name` (optional), `future.model` (optional), `future.metric` (optional)

        https://substrate.run/library#QueryVectorStore
        """
        super().__init__(hide=hide, out_type=QueryVectorStoreOut, **args)
        self.node = "QueryVectorStore"

    @property
    def future(self) -> FutureQueryVectorStoreOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.results`, `future.collection_name` (optional), `future.model` (optional), `future.metric` (optional)

        https://substrate.run/library#QueryVectorStore
        """
        return super().future  # type: ignore


class FetchVectors(CoreNode[FetchVectorsOut]):
    """
    Fetch vectors from a vector store.

    https://substrate.run/library#FetchVectors
    """

    def __init__(self, args: FetchVectorsIn, hide: bool = False):
        """
        Input arguments: `collection_name`, `model`, `ids`

        Output fields: `future.vectors`

        https://substrate.run/library#FetchVectors
        """
        super().__init__(hide=hide, out_type=FetchVectorsOut, **args)
        self.node = "FetchVectors"

    @property
    def future(self) -> FutureFetchVectorsOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.vectors`

        https://substrate.run/library#FetchVectors
        """
        return super().future  # type: ignore


class UpdateVectors(CoreNode[UpdateVectorsOut]):
    """
    Update vectors in a vector store.

    https://substrate.run/library#UpdateVectors
    """

    def __init__(self, args: UpdateVectorsIn, hide: bool = False):
        """
        Input arguments: `collection_name`, `model`, `vectors`

        Output fields: `future.count`

        https://substrate.run/library#UpdateVectors
        """
        super().__init__(hide=hide, out_type=UpdateVectorsOut, **args)
        self.node = "UpdateVectors"

    @property
    def future(self) -> FutureUpdateVectorsOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.count`

        https://substrate.run/library#UpdateVectors
        """
        return super().future  # type: ignore


class DeleteVectors(CoreNode[DeleteVectorsOut]):
    """
    Delete vectors in a vector store.

    https://substrate.run/library#DeleteVectors
    """

    def __init__(self, args: DeleteVectorsIn, hide: bool = False):
        """
        Input arguments: `collection_name`, `model`, `ids`

        Output fields: `future.count`

        https://substrate.run/library#DeleteVectors
        """
        super().__init__(hide=hide, out_type=DeleteVectorsOut, **args)
        self.node = "DeleteVectors"

    @property
    def future(self) -> FutureDeleteVectorsOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.count`

        https://substrate.run/library#DeleteVectors
        """
        return super().future  # type: ignore
