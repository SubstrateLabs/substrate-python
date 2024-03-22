"""
꩜ Substrate
@GENERATED FILE
20240315.20240321
"""

from .substrate import SubstrateResponse
from .core.corenode import CoreNode
from .dataclass_models import (
    FillMaskOut,
    EmbedTextOut,
    EmbedImageOut,
    GenerateTextOut,
    UpscaleImageOut,
    GenerateImageOut,
    DetectSegmentsOut,
    GenerateSpeechOut,
    MultiEmbedTextOut,
    MultiEmbedImageOut,
    TranscribeMediaOut,
    RemoveBackgroundOut,
    MultiGenerateTextOut,
    GenerateTextVisionOut,
    MultiGenerateImageOut,
    GenerativeEditImageOut,
    ControlledGenerateImageOut,
    MultiGenerativeEditImageOut,
    MultiControlledGenerateImageOut,
)
from .typeddict_models import (
    FillMaskIn,
    EmbedTextIn,
    EmbedImageIn,
    GenerateTextIn,
    UpscaleImageIn,
    GenerateImageIn,
    DetectSegmentsIn,
    GenerateSpeechIn,
    MultiEmbedTextIn,
    MultiEmbedImageIn,
    TranscribeMediaIn,
    RemoveBackgroundIn,
    MultiGenerateTextIn,
    GenerateTextVisionIn,
    MultiGenerateImageIn,
    GenerativeEditImageIn,
    ControlledGenerateImageIn,
    MultiGenerativeEditImageIn,
    MultiControlledGenerateImageIn,
)
from .future_dataclass_models import (
    FutureFillMaskOut,
    FutureEmbedTextOut,
    FutureEmbedImageOut,
    FutureGenerateTextOut,
    FutureUpscaleImageOut,
    FutureGenerateImageOut,
    FutureDetectSegmentsOut,
    FutureGenerateSpeechOut,
    FutureMultiEmbedTextOut,
    FutureMultiEmbedImageOut,
    FutureTranscribeMediaOut,
    FutureRemoveBackgroundOut,
    FutureMultiGenerateTextOut,
    FutureGenerateTextVisionOut,
    FutureMultiGenerateImageOut,
    FutureGenerativeEditImageOut,
    FutureControlledGenerateImageOut,
    FutureMultiGenerativeEditImageOut,
    FutureMultiControlledGenerateImageOut,
)


class GenerateText(CoreNode):
    """
    Generate text using a language model.

    https://substrate.run/library#GenerateText
    """

    def __init__(self, args: GenerateTextIn):
        """
        Input arguments: `prompt`, `model` (optional), `response_format` (optional), `temperature` (optional), `max_tokens` (optional)

        Output fields: `future.text` (optional), `future.json_object` (optional)

        https://substrate.run/library#GenerateText
        """
        super().__init__(**args)
        self.node = "GenerateText"

    def output(self, response: SubstrateResponse) -> GenerateTextOut:
        """
        Retrieve this node's output from a response.

        Output fields: `future.text` (optional), `future.json_object` (optional)

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

        Output fields: `future.text` (optional), `future.json_object` (optional)

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
        Input arguments: `prompt`, `num_choices`, `model` (optional), `response_format` (optional), `temperature` (optional), `max_tokens` (optional)

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


class GenerateTextVision(CoreNode):
    """
    Generate text by prompting with text and images using a vision-language model.

    https://substrate.run/library#GenerateTextVision
    """

    def __init__(self, args: GenerateTextVisionIn):
        """
        Input arguments: `prompt`, `image_uris` (optional), `model` (optional), `temperature` (optional), `max_tokens` (optional)

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


class GenerateImage(CoreNode):
    """
    Generate an image.

    https://substrate.run/library#GenerateImage
    """

    def __init__(self, args: GenerateImageIn):
        """
        Input arguments: `prompt`, `image_prompt_uri` (optional), `model` (optional), `image_influence` (optional), `negative_prompt` (optional), `store` (optional), `width` (optional), `height` (optional), `seed` (optional)

        Output fields: `future.image_uri`, `future.seed`

        https://substrate.run/library#GenerateImage
        """
        super().__init__(**args)
        self.node = "GenerateImage"

    def output(self, response: SubstrateResponse) -> GenerateImageOut:
        """
        Retrieve this node's output from a response.

        Output fields: `future.image_uri`, `future.seed`

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

        Output fields: `future.image_uri`, `future.seed`

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
        Input arguments: `prompt`, `image_prompt_uri` (optional), `num_images`, `model` (optional), `image_influence` (optional), `negative_prompt` (optional), `store` (optional), `width` (optional), `height` (optional), `seeds` (optional)

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


class ControlledGenerateImage(CoreNode):
    """
    Generate an image with generation controlled by an input image.

    https://substrate.run/library#ControlledGenerateImage
    """

    def __init__(self, args: ControlledGenerateImageIn):
        """
        Input arguments: `image_uri`, `control_method`, `prompt`, `output_resolution` (optional), `model` (optional), `negative_prompt` (optional), `store` (optional), `image_influence` (optional), `seed` (optional)

        Output fields: `future.image_uri`, `future.seed`

        https://substrate.run/library#ControlledGenerateImage
        """
        super().__init__(**args)
        self.node = "ControlledGenerateImage"

    def output(self, response: SubstrateResponse) -> ControlledGenerateImageOut:
        """
        Retrieve this node's output from a response.

        Output fields: `future.image_uri`, `future.seed`

        https://substrate.run/library#ControlledGenerateImage
        """
        klass = ControlledGenerateImageOut
        json = response.api_response.json
        if json and json.get("data"):
            data = json["data"]
            node_id = self.id
            if data.get(self.id):
                return klass(**data[self.id])
        raise ValueError(f"Node {self.id} not found in response")

    @property
    def future(self) -> FutureControlledGenerateImageOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.image_uri`, `future.seed`

        https://substrate.run/library#ControlledGenerateImage
        """
        return super().future  # type: ignore


class MultiControlledGenerateImage(CoreNode):
    """
    Generate multiple image outputs with generation controlled by an input image.

    https://substrate.run/library#MultiControlledGenerateImage
    """

    def __init__(self, args: MultiControlledGenerateImageIn):
        """
        Input arguments: `image_uri`, `control_method`, `prompt`, `num_images`, `output_resolution` (optional), `model` (optional), `negative_prompt` (optional), `store` (optional), `image_influence` (optional), `seeds` (optional)

        Output fields: `future.outputs`

        https://substrate.run/library#MultiControlledGenerateImage
        """
        super().__init__(**args)
        self.node = "MultiControlledGenerateImage"

    def output(self, response: SubstrateResponse) -> MultiControlledGenerateImageOut:
        """
        Retrieve this node's output from a response.

        Output fields: `future.outputs`

        https://substrate.run/library#MultiControlledGenerateImage
        """
        klass = MultiControlledGenerateImageOut
        json = response.api_response.json
        if json and json.get("data"):
            data = json["data"]
            node_id = self.id
            if data.get(self.id):
                return klass(**data[self.id])
        raise ValueError(f"Node {self.id} not found in response")

    @property
    def future(self) -> FutureMultiControlledGenerateImageOut:  # type: ignore
        """
        Future reference to this node's output.

        Output fields: `future.outputs`

        https://substrate.run/library#MultiControlledGenerateImage
        """
        return super().future  # type: ignore


class GenerativeEditImage(CoreNode):
    """
    Edit an image with a generative model.

    https://substrate.run/library#GenerativeEditImage
    """

    def __init__(self, args: GenerativeEditImageIn):
        """
        Input arguments: `image_uri`, `prompt`, `mask_image_uri` (optional), `image_prompt_uri` (optional), `output_resolution` (optional), `model` (optional), `strength` (optional), `image_prompt_influence` (optional), `negative_prompt` (optional), `store` (optional), `seed` (optional)

        Output fields: `future.image_uri`, `future.seed`

        https://substrate.run/library#GenerativeEditImage
        """
        super().__init__(**args)
        self.node = "GenerativeEditImage"

    def output(self, response: SubstrateResponse) -> GenerativeEditImageOut:
        """
        Retrieve this node's output from a response.

        Output fields: `future.image_uri`, `future.seed`

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

        Output fields: `future.image_uri`, `future.seed`

        https://substrate.run/library#GenerativeEditImage
        """
        return super().future  # type: ignore


class MultiGenerativeEditImage(CoreNode):
    """
    Generate multiple image outputs modifying part of an image using a mask.

    https://substrate.run/library#MultiGenerativeEditImage
    """

    def __init__(self, args: MultiGenerativeEditImageIn):
        """
        Input arguments: `image_uri`, `prompt`, `mask_image_uri` (optional), `image_prompt_uri` (optional), `num_images`, `output_resolution` (optional), `model` (optional), `negative_prompt` (optional), `store` (optional), `strength` (optional), `image_prompt_influence` (optional), `seeds` (optional)

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
    Generate vector embedding for a text document.

    https://substrate.run/library#EmbedText
    """

    def __init__(self, args: EmbedTextIn):
        """
        Input arguments: `text`, `model` (optional), `store` (optional), `metadata` (optional), `embedded_metadata_keys` (optional), `document_id` (optional)

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
    Generate vector embeddings for multiple text documents.

    https://substrate.run/library#MultiEmbedText
    """

    def __init__(self, args: MultiEmbedTextIn):
        """
        Input arguments: `items`, `model` (optional), `store` (optional), `embedded_metadata_keys` (optional)

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
    Generate vector embedding for an image, and optionally store the embedding.

    https://substrate.run/library#EmbedImage
    """

    def __init__(self, args: EmbedImageIn):
        """
        Input arguments: `image_uri`, `model` (optional), `store` (optional), `document_id` (optional)

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
    Generate vector embeddings for multiple images, and optionally store the embeddings.

    https://substrate.run/library#MultiEmbedImage
    """

    def __init__(self, args: MultiEmbedImageIn):
        """
        Input arguments: `items`, `store` (optional), `model` (optional)

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
