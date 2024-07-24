"""
𐃏 Substrate
@GENERATED FILE
"""
from __future__ import annotations

import warnings

from .substrate import SubstrateResponse
from .core.corenode import CoreNode

# filter pydantic v2 deprecation warnings
with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    from .core.models import (
        IfOut,
        BoxOut,
        CLIPOut,
        JinaV2Out,
        EmbedTextOut,
        RunPythonOut,
        EmbedImageOut,
        EraseImageOut,
        ComputeJSONOut,
        ComputeTextOut,
        ExperimentalOut,
        FetchVectorsOut,
        Firellava13BOut,
        InpaintImageOut,
        UpscaleImageOut,
        DeleteVectorsOut,
        GenerateImageOut,
        SplitDocumentOut,
        UpdateVectorsOut,
        GenerateSpeechOut,
        MultiEmbedTextOut,
        MultiEmbedImageOut,
        SegmentAnythingOut,
        BatchComputeJSONOut,
        BatchComputeTextOut,
        ListVectorStoresOut,
        Llama3Instruct8BOut,
        MultiComputeJSONOut,
        MultiComputeTextOut,
        QueryVectorStoreOut,
        RemoveBackgroundOut,
        TranscribeSpeechOut,
        DeleteVectorStoreOut,
        Llama3Instruct70BOut,
        Mistral7BInstructOut,
        MultiInpaintImageOut,
        SegmentUnderPointOut,
        MultiGenerateImageOut,
        Mixtral8x7BInstructOut,
        FindOrCreateVectorStoreOut,
        StableDiffusionXLInpaintOut,
        StableDiffusionXLLightningOut,
        StableDiffusionXLControlNetOut,
    )
from typing import Any, Dict, List, Optional
from dataclasses import dataclass
from typing_extensions import Literal

from .future_dataclass_models import (
    FutureIfOut,
    FutureBoxOut,
    FutureCLIPOut,
    FutureJinaV2Out,
    FutureEmbedTextOut,
    FutureRunPythonOut,
    FutureEmbedImageOut,
    FutureEraseImageOut,
    FutureComputeJSONOut,
    FutureComputeTextOut,
    FutureExperimentalOut,
    FutureFetchVectorsOut,
    FutureFirellava13BOut,
    FutureInpaintImageOut,
    FutureUpscaleImageOut,
    FutureDeleteVectorsOut,
    FutureGenerateImageOut,
    FutureSplitDocumentOut,
    FutureUpdateVectorsOut,
    FutureGenerateSpeechOut,
    FutureMultiEmbedTextOut,
    FutureMultiEmbedImageOut,
    FutureSegmentAnythingOut,
    FutureBatchComputeJSONOut,
    FutureBatchComputeTextOut,
    FutureListVectorStoresOut,
    FutureLlama3Instruct8BOut,
    FutureMultiComputeJSONOut,
    FutureMultiComputeTextOut,
    FutureQueryVectorStoreOut,
    FutureRemoveBackgroundOut,
    FutureTranscribeSpeechOut,
    FutureDeleteVectorStoreOut,
    FutureLlama3Instruct70BOut,
    FutureMistral7BInstructOut,
    FutureMultiInpaintImageOut,
    FutureSegmentUnderPointOut,
    FutureMultiGenerateImageOut,
    FutureMixtral8x7BInstructOut,
    FutureFindOrCreateVectorStoreOut,
    FutureStableDiffusionXLInpaintOut,
    FutureStableDiffusionXLLightningOut,
    FutureStableDiffusionXLControlNetOut,
)


class Experimental(CoreNode[ExperimentalOut]):
    """https://substrate.run/nodes#Experimental"""

    def __init__(
        self,
        name: str,
        args: Dict[str, Any],
        timeout: int = 60,
        hide: bool = False,
        **kwargs,
    ):
        """
        Args:
            name: Identifier.
            args: Arguments.
            timeout: Timeout in seconds.

        https://substrate.run/nodes#Experimental
        """
        super().__init__(
            name=name,
            args=args,
            timeout=timeout,
            hide=hide,
            out_type=ExperimentalOut,
            **kwargs,
        )
        self.node = "Experimental"

    @property
    def future(self) -> FutureExperimentalOut:  # type: ignore
        """
        Future reference to this node's output.

        https://substrate.run/nodes#Experimental
        """
        return super().future  # type: ignore


class Box(CoreNode[BoxOut]):
    """https://substrate.run/nodes#Box"""

    def __init__(self, value: Any, hide: bool = False, **kwargs):
        """
        Args:
            value: Values to box.

        https://substrate.run/nodes#Box
        """
        super().__init__(value=value, hide=hide, out_type=BoxOut, **kwargs)
        self.node = "Box"

    @property
    def future(self) -> FutureBoxOut:  # type: ignore
        """
        Future reference to this node's output.

        https://substrate.run/nodes#Box
        """
        return super().future  # type: ignore


class If(CoreNode[IfOut]):
    """https://substrate.run/nodes#If"""

    def __init__(
        self,
        condition: bool,
        value_if_true: Any,
        value_if_false: Optional[Any] = None,
        hide: bool = False,
        **kwargs,
    ):
        """
        Args:
            condition: Condition.
            value_if_true: Result when condition is true.
            value_if_false: Result when condition is false.

        https://substrate.run/nodes#If
        """
        super().__init__(
            condition=condition,
            value_if_true=value_if_true,
            value_if_false=value_if_false,
            hide=hide,
            out_type=IfOut,
            **kwargs,
        )
        self.node = "If"

    @property
    def future(self) -> FutureIfOut:  # type: ignore
        """
        Future reference to this node's output.

        https://substrate.run/nodes#If
        """
        return super().future  # type: ignore


class ComputeText(CoreNode[ComputeTextOut]):
    """https://substrate.run/nodes#ComputeText"""

    def __init__(
        self,
        prompt: str,
        image_uris: Optional[List[str]] = None,
        temperature: float = 0.4,
        max_tokens: Optional[int] = None,
        model: Literal[
            "Mistral7BInstruct",
            "Mixtral8x7BInstruct",
            "Llama3Instruct8B",
            "Llama3Instruct70B",
            "Firellava13B",
            "gpt-4o",
            "gpt-4o-mini",
            "claude-3-5-sonnet-20240620",
        ] = "Llama3Instruct8B",
        hide: bool = False,
        **kwargs,
    ):
        """
        Args:
            prompt: Input prompt.
            image_uris: Image prompts.
            temperature: Sampling temperature to use. Higher values make the output more random, lower values make the output more deterministic.
            max_tokens: Maximum number of tokens to generate.
            model: Selected model. `Firellava13B` is automatically selected when `image_uris` is provided.

        https://substrate.run/nodes#ComputeText
        """
        super().__init__(
            prompt=prompt,
            image_uris=image_uris,
            temperature=temperature,
            max_tokens=max_tokens,
            model=model,
            hide=hide,
            out_type=ComputeTextOut,
            **kwargs,
        )
        self.node = "ComputeText"

    @property
    def future(self) -> FutureComputeTextOut:  # type: ignore
        """
        Future reference to this node's output.

        https://substrate.run/nodes#ComputeText
        """
        return super().future  # type: ignore


class ComputeJSON(CoreNode[ComputeJSONOut]):
    """https://substrate.run/nodes#ComputeJSON"""

    def __init__(
        self,
        prompt: str,
        json_schema: Dict[str, Any],
        temperature: float = 0.4,
        max_tokens: Optional[int] = None,
        model: Literal["Mistral7BInstruct", "Mixtral8x7BInstruct", "Llama3Instruct8B"] = "Llama3Instruct8B",
        hide: bool = False,
        **kwargs,
    ):
        """
        Args:
            prompt: Input prompt.
            json_schema: JSON schema to guide `json_object` response.
            temperature: Sampling temperature to use. Higher values make the output more random, lower values make the output more deterministic.
            max_tokens: Maximum number of tokens to generate.
            model: Selected model.

        https://substrate.run/nodes#ComputeJSON
        """
        super().__init__(
            prompt=prompt,
            json_schema=json_schema,
            temperature=temperature,
            max_tokens=max_tokens,
            model=model,
            hide=hide,
            out_type=ComputeJSONOut,
            **kwargs,
        )
        self.node = "ComputeJSON"

    @property
    def future(self) -> FutureComputeJSONOut:  # type: ignore
        """
        Future reference to this node's output.

        https://substrate.run/nodes#ComputeJSON
        """
        return super().future  # type: ignore


class MultiComputeText(CoreNode[MultiComputeTextOut]):
    """https://substrate.run/nodes#MultiComputeText"""

    def __init__(
        self,
        prompt: str,
        num_choices: int,
        temperature: float = 0.4,
        max_tokens: Optional[int] = None,
        model: Literal[
            "Mistral7BInstruct",
            "Mixtral8x7BInstruct",
            "Llama3Instruct8B",
            "Llama3Instruct70B",
        ] = "Llama3Instruct8B",
        hide: bool = False,
        **kwargs,
    ):
        """
        Args:
            prompt: Input prompt.
            num_choices: Number of choices to generate.
            temperature: Sampling temperature to use. Higher values make the output more random, lower values make the output more deterministic.
            max_tokens: Maximum number of tokens to generate.
            model: Selected model.

        https://substrate.run/nodes#MultiComputeText
        """
        super().__init__(
            prompt=prompt,
            num_choices=num_choices,
            temperature=temperature,
            max_tokens=max_tokens,
            model=model,
            hide=hide,
            out_type=MultiComputeTextOut,
            **kwargs,
        )
        self.node = "MultiComputeText"

    @property
    def future(self) -> FutureMultiComputeTextOut:  # type: ignore
        """
        Future reference to this node's output.

        https://substrate.run/nodes#MultiComputeText
        """
        return super().future  # type: ignore


class BatchComputeText(CoreNode[BatchComputeTextOut]):
    """https://substrate.run/nodes#BatchComputeText"""

    def __init__(
        self,
        prompts: List[str],
        temperature: float = 0.4,
        max_tokens: Optional[int] = None,
        model: Literal["Mistral7BInstruct", "Llama3Instruct8B"] = "Llama3Instruct8B",
        hide: bool = False,
        **kwargs,
    ):
        """
        Args:
            prompts: Batch input prompts.
            temperature: Sampling temperature to use. Higher values make the output more random, lower values make the output more deterministic.
            max_tokens: Maximum number of tokens to generate.
            model: Selected model.

        https://substrate.run/nodes#BatchComputeText
        """
        super().__init__(
            prompts=prompts,
            temperature=temperature,
            max_tokens=max_tokens,
            model=model,
            hide=hide,
            out_type=BatchComputeTextOut,
            **kwargs,
        )
        self.node = "BatchComputeText"

    @property
    def future(self) -> FutureBatchComputeTextOut:  # type: ignore
        """
        Future reference to this node's output.

        https://substrate.run/nodes#BatchComputeText
        """
        return super().future  # type: ignore


class MultiComputeJSON(CoreNode[MultiComputeJSONOut]):
    """https://substrate.run/nodes#MultiComputeJSON"""

    def __init__(
        self,
        prompt: str,
        json_schema: Dict[str, Any],
        num_choices: int,
        temperature: float = 0.4,
        max_tokens: Optional[int] = None,
        model: Literal["Mistral7BInstruct", "Mixtral8x7BInstruct", "Llama3Instruct8B"] = "Llama3Instruct8B",
        hide: bool = False,
        **kwargs,
    ):
        """
        Args:
            prompt: Input prompt.
            json_schema: JSON schema to guide `json_object` response.
            num_choices: Number of choices to generate.
            temperature: Sampling temperature to use. Higher values make the output more random, lower values make the output more deterministic.
            max_tokens: Maximum number of tokens to generate.
            model: Selected model.

        https://substrate.run/nodes#MultiComputeJSON
        """
        super().__init__(
            prompt=prompt,
            json_schema=json_schema,
            num_choices=num_choices,
            temperature=temperature,
            max_tokens=max_tokens,
            model=model,
            hide=hide,
            out_type=MultiComputeJSONOut,
            **kwargs,
        )
        self.node = "MultiComputeJSON"

    @property
    def future(self) -> FutureMultiComputeJSONOut:  # type: ignore
        """
        Future reference to this node's output.

        https://substrate.run/nodes#MultiComputeJSON
        """
        return super().future  # type: ignore


class BatchComputeJSON(CoreNode[BatchComputeJSONOut]):
    """https://substrate.run/nodes#BatchComputeJSON"""

    def __init__(
        self,
        prompts: List[str],
        json_schema: Dict[str, Any],
        temperature: float = 0.4,
        max_tokens: Optional[int] = None,
        model: Literal["Mistral7BInstruct", "Llama3Instruct8B"] = "Llama3Instruct8B",
        hide: bool = False,
        **kwargs,
    ):
        """
        Args:
            prompts: Batch input prompts.
            json_schema: JSON schema to guide `json_object` response.
            temperature: Sampling temperature to use. Higher values make the output more random, lower values make the output more deterministic.
            max_tokens: Maximum number of tokens to generate.
            model: Selected model.

        https://substrate.run/nodes#BatchComputeJSON
        """
        super().__init__(
            prompts=prompts,
            json_schema=json_schema,
            temperature=temperature,
            max_tokens=max_tokens,
            model=model,
            hide=hide,
            out_type=BatchComputeJSONOut,
            **kwargs,
        )
        self.node = "BatchComputeJSON"

    @property
    def future(self) -> FutureBatchComputeJSONOut:  # type: ignore
        """
        Future reference to this node's output.

        https://substrate.run/nodes#BatchComputeJSON
        """
        return super().future  # type: ignore


class Mistral7BInstruct(CoreNode[Mistral7BInstructOut]):
    """https://substrate.run/nodes#Mistral7BInstruct"""

    def __init__(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        num_choices: int = 1,
        json_schema: Optional[Dict[str, Any]] = None,
        temperature: Optional[float] = None,
        frequency_penalty: float = 0.0,
        repetition_penalty: float = 1.0,
        presence_penalty: float = 1.1,
        top_p: float = 0.95,
        max_tokens: Optional[int] = None,
        hide: bool = False,
        **kwargs,
    ):
        """
        Args:
            prompt: Input prompt.
            system_prompt: System prompt.
            num_choices: Number of choices to generate.
            json_schema: JSON schema to guide response.
            temperature: Higher values make the output more random, lower values make the output more deterministic.
            frequency_penalty: Higher values decrease the likelihood of repeating previous tokens.
            repetition_penalty: Higher values decrease the likelihood of repeated sequences.
            presence_penalty: Higher values increase the likelihood of new topics appearing.
            top_p: Probability below which less likely tokens are filtered out.
            max_tokens: Maximum number of tokens to generate.

        https://substrate.run/nodes#Mistral7BInstruct
        """
        super().__init__(
            prompt=prompt,
            system_prompt=system_prompt,
            num_choices=num_choices,
            json_schema=json_schema,
            temperature=temperature,
            frequency_penalty=frequency_penalty,
            repetition_penalty=repetition_penalty,
            presence_penalty=presence_penalty,
            top_p=top_p,
            max_tokens=max_tokens,
            hide=hide,
            out_type=Mistral7BInstructOut,
            **kwargs,
        )
        self.node = "Mistral7BInstruct"

    @property
    def future(self) -> FutureMistral7BInstructOut:  # type: ignore
        """
        Future reference to this node's output.

        https://substrate.run/nodes#Mistral7BInstruct
        """
        return super().future  # type: ignore


class Mixtral8x7BInstruct(CoreNode[Mixtral8x7BInstructOut]):
    """https://substrate.run/nodes#Mixtral8x7BInstruct"""

    def __init__(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        num_choices: int = 1,
        json_schema: Optional[Dict[str, Any]] = None,
        temperature: Optional[float] = None,
        frequency_penalty: float = 0.0,
        repetition_penalty: float = 1.0,
        presence_penalty: float = 1.1,
        top_p: float = 0.95,
        max_tokens: Optional[int] = None,
        hide: bool = False,
        **kwargs,
    ):
        """
        Args:
            prompt: Input prompt.
            system_prompt: System prompt.
            num_choices: Number of choices to generate.
            json_schema: JSON schema to guide response.
            temperature: Higher values make the output more random, lower values make the output more deterministic.
            frequency_penalty: Higher values decrease the likelihood of repeating previous tokens.
            repetition_penalty: Higher values decrease the likelihood of repeated sequences.
            presence_penalty: Higher values increase the likelihood of new topics appearing.
            top_p: Probability below which less likely tokens are filtered out.
            max_tokens: Maximum number of tokens to generate.

        https://substrate.run/nodes#Mixtral8x7BInstruct
        """
        super().__init__(
            prompt=prompt,
            system_prompt=system_prompt,
            num_choices=num_choices,
            json_schema=json_schema,
            temperature=temperature,
            frequency_penalty=frequency_penalty,
            repetition_penalty=repetition_penalty,
            presence_penalty=presence_penalty,
            top_p=top_p,
            max_tokens=max_tokens,
            hide=hide,
            out_type=Mixtral8x7BInstructOut,
            **kwargs,
        )
        self.node = "Mixtral8x7BInstruct"

    @property
    def future(self) -> FutureMixtral8x7BInstructOut:  # type: ignore
        """
        Future reference to this node's output.

        https://substrate.run/nodes#Mixtral8x7BInstruct
        """
        return super().future  # type: ignore


class Llama3Instruct8B(CoreNode[Llama3Instruct8BOut]):
    """https://substrate.run/nodes#Llama3Instruct8B"""

    def __init__(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        num_choices: int = 1,
        temperature: Optional[float] = None,
        frequency_penalty: float = 0.0,
        repetition_penalty: float = 1.0,
        presence_penalty: float = 1.1,
        top_p: float = 0.95,
        max_tokens: Optional[int] = None,
        json_schema: Optional[Dict[str, Any]] = None,
        hide: bool = False,
        **kwargs,
    ):
        """
        Args:
            prompt: Input prompt.
            system_prompt: System prompt.
            num_choices: Number of choices to generate.
            temperature: Higher values make the output more random, lower values make the output more deterministic.
            frequency_penalty: Higher values decrease the likelihood of repeating previous tokens.
            repetition_penalty: Higher values decrease the likelihood of repeated sequences.
            presence_penalty: Higher values increase the likelihood of new topics appearing.
            top_p: Probability below which less likely tokens are filtered out.
            max_tokens: Maximum number of tokens to generate.
            json_schema: JSON schema to guide response.

        https://substrate.run/nodes#Llama3Instruct8B
        """
        super().__init__(
            prompt=prompt,
            system_prompt=system_prompt,
            num_choices=num_choices,
            temperature=temperature,
            frequency_penalty=frequency_penalty,
            repetition_penalty=repetition_penalty,
            presence_penalty=presence_penalty,
            top_p=top_p,
            max_tokens=max_tokens,
            json_schema=json_schema,
            hide=hide,
            out_type=Llama3Instruct8BOut,
            **kwargs,
        )
        self.node = "Llama3Instruct8B"

    @property
    def future(self) -> FutureLlama3Instruct8BOut:  # type: ignore
        """
        Future reference to this node's output.

        https://substrate.run/nodes#Llama3Instruct8B
        """
        return super().future  # type: ignore


class Llama3Instruct70B(CoreNode[Llama3Instruct70BOut]):
    """https://substrate.run/nodes#Llama3Instruct70B"""

    def __init__(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        num_choices: int = 1,
        temperature: Optional[float] = None,
        frequency_penalty: float = 0.0,
        repetition_penalty: float = 1.0,
        presence_penalty: float = 1.1,
        top_p: float = 0.95,
        max_tokens: Optional[int] = None,
        hide: bool = False,
        **kwargs,
    ):
        """
        Args:
            prompt: Input prompt.
            system_prompt: System prompt.
            num_choices: Number of choices to generate.
            temperature: Higher values make the output more random, lower values make the output more deterministic.
            frequency_penalty: Higher values decrease the likelihood of repeating previous tokens.
            repetition_penalty: Higher values decrease the likelihood of repeated sequences.
            presence_penalty: Higher values increase the likelihood of new topics appearing.
            top_p: Probability below which less likely tokens are filtered out.
            max_tokens: Maximum number of tokens to generate.

        https://substrate.run/nodes#Llama3Instruct70B
        """
        super().__init__(
            prompt=prompt,
            system_prompt=system_prompt,
            num_choices=num_choices,
            temperature=temperature,
            frequency_penalty=frequency_penalty,
            repetition_penalty=repetition_penalty,
            presence_penalty=presence_penalty,
            top_p=top_p,
            max_tokens=max_tokens,
            hide=hide,
            out_type=Llama3Instruct70BOut,
            **kwargs,
        )
        self.node = "Llama3Instruct70B"

    @property
    def future(self) -> FutureLlama3Instruct70BOut:  # type: ignore
        """
        Future reference to this node's output.

        https://substrate.run/nodes#Llama3Instruct70B
        """
        return super().future  # type: ignore


class Firellava13B(CoreNode[Firellava13BOut]):
    """https://substrate.run/nodes#Firellava13B"""

    def __init__(
        self,
        prompt: str,
        image_uris: List[str],
        max_tokens: Optional[int] = None,
        hide: bool = False,
        **kwargs,
    ):
        """
        Args:
            prompt: Text prompt.
            image_uris: Image prompts.
            max_tokens: Maximum number of tokens to generate.

        https://substrate.run/nodes#Firellava13B
        """
        super().__init__(
            prompt=prompt,
            image_uris=image_uris,
            max_tokens=max_tokens,
            hide=hide,
            out_type=Firellava13BOut,
            **kwargs,
        )
        self.node = "Firellava13B"

    @property
    def future(self) -> FutureFirellava13BOut:  # type: ignore
        """
        Future reference to this node's output.

        https://substrate.run/nodes#Firellava13B
        """
        return super().future  # type: ignore


class GenerateImage(CoreNode[GenerateImageOut]):
    """https://substrate.run/nodes#GenerateImage"""

    def __init__(self, prompt: str, store: Optional[str] = None, hide: bool = False, **kwargs):
        """
        Args:
            prompt: Text prompt.
            store: Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://docs.substrate.run/reference/external-files). If unset, the image data will be returned as a base64-encoded string.

        https://substrate.run/nodes#GenerateImage
        """
        super().__init__(prompt=prompt, store=store, hide=hide, out_type=GenerateImageOut, **kwargs)
        self.node = "GenerateImage"

    @property
    def future(self) -> FutureGenerateImageOut:  # type: ignore
        """
        Future reference to this node's output.

        https://substrate.run/nodes#GenerateImage
        """
        return super().future  # type: ignore


class MultiGenerateImage(CoreNode[MultiGenerateImageOut]):
    """https://substrate.run/nodes#MultiGenerateImage"""

    def __init__(
        self,
        prompt: str,
        num_images: int,
        store: Optional[str] = None,
        hide: bool = False,
        **kwargs,
    ):
        """
        Args:
            prompt: Text prompt.
            num_images: Number of images to generate.
            store: Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://docs.substrate.run/reference/external-files). If unset, the image data will be returned as a base64-encoded string.

        https://substrate.run/nodes#MultiGenerateImage
        """
        super().__init__(
            prompt=prompt,
            num_images=num_images,
            store=store,
            hide=hide,
            out_type=MultiGenerateImageOut,
            **kwargs,
        )
        self.node = "MultiGenerateImage"

    @property
    def future(self) -> FutureMultiGenerateImageOut:  # type: ignore
        """
        Future reference to this node's output.

        https://substrate.run/nodes#MultiGenerateImage
        """
        return super().future  # type: ignore


class StableDiffusionXLLightning(CoreNode[StableDiffusionXLLightningOut]):
    """https://substrate.run/nodes#StableDiffusionXLLightning"""

    def __init__(
        self,
        prompt: str,
        negative_prompt: Optional[str] = None,
        num_images: int = 1,
        store: Optional[str] = None,
        height: int = 1024,
        width: int = 1024,
        seeds: Optional[List[int]] = None,
        hide: bool = False,
        **kwargs,
    ):
        """
        Args:
            prompt: Text prompt.
            negative_prompt: Negative input prompt.
            num_images: Number of images to generate.
            store: Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://docs.substrate.run/reference/external-files). If unset, the image data will be returned as a base64-encoded string.
            height: Height of output image, in pixels.
            width: Width of output image, in pixels.
            seeds: Seeds for deterministic generation. Default is a random seed.

        https://substrate.run/nodes#StableDiffusionXLLightning
        """
        super().__init__(
            prompt=prompt,
            negative_prompt=negative_prompt,
            num_images=num_images,
            store=store,
            height=height,
            width=width,
            seeds=seeds,
            hide=hide,
            out_type=StableDiffusionXLLightningOut,
            **kwargs,
        )
        self.node = "StableDiffusionXLLightning"

    @property
    def future(self) -> FutureStableDiffusionXLLightningOut:  # type: ignore
        """
        Future reference to this node's output.

        https://substrate.run/nodes#StableDiffusionXLLightning
        """
        return super().future  # type: ignore


class StableDiffusionXLControlNet(CoreNode[StableDiffusionXLControlNetOut]):
    """https://substrate.run/nodes#StableDiffusionXLControlNet"""

    def __init__(
        self,
        image_uri: str,
        control_method: Literal["edge", "depth", "illusion", "tile"],
        prompt: str,
        num_images: int,
        output_resolution: int = 1024,
        negative_prompt: Optional[str] = None,
        store: Optional[str] = None,
        conditioning_scale: float = 0.5,
        strength: float = 0.5,
        seeds: Optional[List[int]] = None,
        hide: bool = False,
        **kwargs,
    ):
        """
        Args:
            image_uri: Input image.
            control_method: Strategy to control generation using the input image.
            prompt: Text prompt.
            num_images: Number of images to generate.
            output_resolution: Resolution of the output image, in pixels.
            negative_prompt: Negative input prompt.
            store: Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://docs.substrate.run/reference/external-files). If unset, the image data will be returned as a base64-encoded string.
            conditioning_scale: Controls the influence of the input image on the generated output.
            strength: Controls how much to transform the input image.
            seeds: Random noise seeds. Default is random seeds for each generation.

        https://substrate.run/nodes#StableDiffusionXLControlNet
        """
        super().__init__(
            image_uri=image_uri,
            control_method=control_method,
            prompt=prompt,
            num_images=num_images,
            output_resolution=output_resolution,
            negative_prompt=negative_prompt,
            store=store,
            conditioning_scale=conditioning_scale,
            strength=strength,
            seeds=seeds,
            hide=hide,
            out_type=StableDiffusionXLControlNetOut,
            **kwargs,
        )
        self.node = "StableDiffusionXLControlNet"

    @property
    def future(self) -> FutureStableDiffusionXLControlNetOut:  # type: ignore
        """
        Future reference to this node's output.

        https://substrate.run/nodes#StableDiffusionXLControlNet
        """
        return super().future  # type: ignore


class InpaintImage(CoreNode[InpaintImageOut]):
    """https://substrate.run/nodes#InpaintImage"""

    def __init__(
        self,
        image_uri: str,
        prompt: str,
        mask_image_uri: Optional[str] = None,
        store: Optional[str] = None,
        hide: bool = False,
        **kwargs,
    ):
        """
        Args:
            image_uri: Original image.
            prompt: Text prompt.
            mask_image_uri: Mask image that controls which pixels are inpainted. If unset, the entire image is edited (image-to-image).
            store: Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://docs.substrate.run/reference/external-files). If unset, the image data will be returned as a base64-encoded string.

        https://substrate.run/nodes#InpaintImage
        """
        super().__init__(
            image_uri=image_uri,
            prompt=prompt,
            mask_image_uri=mask_image_uri,
            store=store,
            hide=hide,
            out_type=InpaintImageOut,
            **kwargs,
        )
        self.node = "InpaintImage"

    @property
    def future(self) -> FutureInpaintImageOut:  # type: ignore
        """
        Future reference to this node's output.

        https://substrate.run/nodes#InpaintImage
        """
        return super().future  # type: ignore


class MultiInpaintImage(CoreNode[MultiInpaintImageOut]):
    """https://substrate.run/nodes#MultiInpaintImage"""

    def __init__(
        self,
        image_uri: str,
        prompt: str,
        num_images: int,
        mask_image_uri: Optional[str] = None,
        store: Optional[str] = None,
        hide: bool = False,
        **kwargs,
    ):
        """
        Args:
            image_uri: Original image.
            prompt: Text prompt.
            num_images: Number of images to generate.
            mask_image_uri: Mask image that controls which pixels are edited (inpainting). If unset, the entire image is edited (image-to-image).
            store: Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://docs.substrate.run/reference/external-files). If unset, the image data will be returned as a base64-encoded string.

        https://substrate.run/nodes#MultiInpaintImage
        """
        super().__init__(
            image_uri=image_uri,
            prompt=prompt,
            num_images=num_images,
            mask_image_uri=mask_image_uri,
            store=store,
            hide=hide,
            out_type=MultiInpaintImageOut,
            **kwargs,
        )
        self.node = "MultiInpaintImage"

    @property
    def future(self) -> FutureMultiInpaintImageOut:  # type: ignore
        """
        Future reference to this node's output.

        https://substrate.run/nodes#MultiInpaintImage
        """
        return super().future  # type: ignore


class StableDiffusionXLInpaint(CoreNode[StableDiffusionXLInpaintOut]):
    """https://substrate.run/nodes#StableDiffusionXLInpaint"""

    def __init__(
        self,
        image_uri: str,
        prompt: str,
        num_images: int,
        mask_image_uri: Optional[str] = None,
        output_resolution: int = 1024,
        negative_prompt: Optional[str] = None,
        store: Optional[str] = None,
        strength: float = 0.8,
        seeds: Optional[List[int]] = None,
        hide: bool = False,
        **kwargs,
    ):
        """
        Args:
            image_uri: Original image.
            prompt: Text prompt.
            num_images: Number of images to generate.
            mask_image_uri: Mask image that controls which pixels are edited (inpainting). If unset, the entire image is edited (image-to-image).
            output_resolution: Resolution of the output image, in pixels.
            negative_prompt: Negative input prompt.
            store: Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://docs.substrate.run/reference/external-files). If unset, the image data will be returned as a base64-encoded string.
            strength: Controls the strength of the generation process.
            seeds: Random noise seeds. Default is random seeds for each generation.

        https://substrate.run/nodes#StableDiffusionXLInpaint
        """
        super().__init__(
            image_uri=image_uri,
            prompt=prompt,
            num_images=num_images,
            mask_image_uri=mask_image_uri,
            output_resolution=output_resolution,
            negative_prompt=negative_prompt,
            store=store,
            strength=strength,
            seeds=seeds,
            hide=hide,
            out_type=StableDiffusionXLInpaintOut,
            **kwargs,
        )
        self.node = "StableDiffusionXLInpaint"

    @property
    def future(self) -> FutureStableDiffusionXLInpaintOut:  # type: ignore
        """
        Future reference to this node's output.

        https://substrate.run/nodes#StableDiffusionXLInpaint
        """
        return super().future  # type: ignore


class EraseImage(CoreNode[EraseImageOut]):
    """https://substrate.run/nodes#EraseImage"""

    def __init__(
        self,
        image_uri: str,
        mask_image_uri: str,
        store: Optional[str] = None,
        hide: bool = False,
        **kwargs,
    ):
        """
        Args:
            image_uri: Input image.
            mask_image_uri: Mask image that controls which pixels are inpainted.
            store: Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://docs.substrate.run/reference/external-files). If unset, the image data will be returned as a base64-encoded string.

        https://substrate.run/nodes#EraseImage
        """
        super().__init__(
            image_uri=image_uri,
            mask_image_uri=mask_image_uri,
            store=store,
            hide=hide,
            out_type=EraseImageOut,
            **kwargs,
        )
        self.node = "EraseImage"

    @property
    def future(self) -> FutureEraseImageOut:  # type: ignore
        """
        Future reference to this node's output.

        https://substrate.run/nodes#EraseImage
        """
        return super().future  # type: ignore


class RemoveBackground(CoreNode[RemoveBackgroundOut]):
    """https://substrate.run/nodes#RemoveBackground"""

    def __init__(
        self,
        image_uri: str,
        return_mask: bool = False,
        invert_mask: bool = False,
        background_color: Optional[str] = None,
        store: Optional[str] = None,
        hide: bool = False,
        **kwargs,
    ):
        """
        Args:
            image_uri: Input image.
            return_mask: Return a mask image instead of the original content.
            invert_mask: Invert the mask image. Only takes effect if `return_mask` is true.
            background_color: Hex value background color. Transparent if unset.
            store: Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://docs.substrate.run/reference/external-files). If unset, the image data will be returned as a base64-encoded string.

        https://substrate.run/nodes#RemoveBackground
        """
        super().__init__(
            image_uri=image_uri,
            return_mask=return_mask,
            invert_mask=invert_mask,
            background_color=background_color,
            store=store,
            hide=hide,
            out_type=RemoveBackgroundOut,
            **kwargs,
        )
        self.node = "RemoveBackground"

    @property
    def future(self) -> FutureRemoveBackgroundOut:  # type: ignore
        """
        Future reference to this node's output.

        https://substrate.run/nodes#RemoveBackground
        """
        return super().future  # type: ignore


class UpscaleImage(CoreNode[UpscaleImageOut]):
    """https://substrate.run/nodes#UpscaleImage"""

    def __init__(
        self,
        image_uri: str,
        prompt: Optional[str] = None,
        output_resolution: int = 1024,
        store: Optional[str] = None,
        hide: bool = False,
        **kwargs,
    ):
        """
        Args:
            image_uri: Input image.
            prompt: Prompt to guide model on the content of image to upscale.
            output_resolution: Resolution of the output image, in pixels.
            store: Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://docs.substrate.run/reference/external-files). If unset, the image data will be returned as a base64-encoded string.

        https://substrate.run/nodes#UpscaleImage
        """
        super().__init__(
            image_uri=image_uri,
            prompt=prompt,
            output_resolution=output_resolution,
            store=store,
            hide=hide,
            out_type=UpscaleImageOut,
            **kwargs,
        )
        self.node = "UpscaleImage"

    @property
    def future(self) -> FutureUpscaleImageOut:  # type: ignore
        """
        Future reference to this node's output.

        https://substrate.run/nodes#UpscaleImage
        """
        return super().future  # type: ignore


class SegmentUnderPoint(CoreNode[SegmentUnderPointOut]):
    """https://substrate.run/nodes#SegmentUnderPoint"""

    def __init__(
        self,
        image_uri: str,
        point: Point,
        store: Optional[str] = None,
        hide: bool = False,
        **kwargs,
    ):
        """
        Args:
            image_uri: Input image.
            point: Point prompt.
            store: Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://docs.substrate.run/reference/external-files). If unset, the image data will be returned as a base64-encoded string.

        https://substrate.run/nodes#SegmentUnderPoint
        """
        super().__init__(
            image_uri=image_uri,
            point=point,
            store=store,
            hide=hide,
            out_type=SegmentUnderPointOut,
            **kwargs,
        )
        self.node = "SegmentUnderPoint"

    @property
    def future(self) -> FutureSegmentUnderPointOut:  # type: ignore
        """
        Future reference to this node's output.

        https://substrate.run/nodes#SegmentUnderPoint
        """
        return super().future  # type: ignore


class SegmentAnything(CoreNode[SegmentAnythingOut]):
    """https://substrate.run/nodes#SegmentAnything"""

    def __init__(
        self,
        image_uri: str,
        point_prompts: Optional[List[Point]] = None,
        box_prompts: Optional[List[BoundingBox]] = None,
        store: Optional[str] = None,
        hide: bool = False,
        **kwargs,
    ):
        """
        Args:
            image_uri: Input image.
            point_prompts: Point prompts, to detect a segment under the point. One of `point_prompts` or `box_prompts` must be set.
            box_prompts: Box prompts, to detect a segment within the bounding box. One of `point_prompts` or `box_prompts` must be set.
            store: Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](https://docs.substrate.run/reference/external-files). If unset, the image data will be returned as a base64-encoded string.

        https://substrate.run/nodes#SegmentAnything
        """
        super().__init__(
            image_uri=image_uri,
            point_prompts=point_prompts,
            box_prompts=box_prompts,
            store=store,
            hide=hide,
            out_type=SegmentAnythingOut,
            **kwargs,
        )
        self.node = "SegmentAnything"

    @property
    def future(self) -> FutureSegmentAnythingOut:  # type: ignore
        """
        Future reference to this node's output.

        https://substrate.run/nodes#SegmentAnything
        """
        return super().future  # type: ignore


class TranscribeSpeech(CoreNode[TranscribeSpeechOut]):
    """https://substrate.run/nodes#TranscribeSpeech"""

    def __init__(
        self,
        audio_uri: str,
        prompt: Optional[str] = None,
        language: str = "en",
        segment: bool = False,
        align: bool = False,
        diarize: bool = False,
        suggest_chapters: bool = False,
        hide: bool = False,
        **kwargs,
    ):
        """
        Args:
            audio_uri: Input audio.
            prompt: Prompt to guide model on the content and context of input audio.
            language: Language of input audio in [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes) format.
            segment: Segment the text into sentences with approximate timestamps.
            align: Align transcription to produce more accurate sentence-level timestamps and word-level timestamps. An array of word segments will be included in each sentence segment.
            diarize: Identify speakers for each segment. Speaker IDs will be included in each segment.
            suggest_chapters: Suggest automatic chapter markers.

        https://substrate.run/nodes#TranscribeSpeech
        """
        super().__init__(
            audio_uri=audio_uri,
            prompt=prompt,
            language=language,
            segment=segment,
            align=align,
            diarize=diarize,
            suggest_chapters=suggest_chapters,
            hide=hide,
            out_type=TranscribeSpeechOut,
            **kwargs,
        )
        self.node = "TranscribeSpeech"

    @property
    def future(self) -> FutureTranscribeSpeechOut:  # type: ignore
        """
        Future reference to this node's output.

        https://substrate.run/nodes#TranscribeSpeech
        """
        return super().future  # type: ignore


class GenerateSpeech(CoreNode[GenerateSpeechOut]):
    """https://substrate.run/nodes#GenerateSpeech"""

    def __init__(self, text: str, store: Optional[str] = None, hide: bool = False, **kwargs):
        """
        Args:
            text: Input text.
            store: Use "hosted" to return an audio URL hosted on Substrate. You can also provide a URL to a registered [file store](https://docs.substrate.run/reference/external-files). If unset, the audio data will be returned as a base64-encoded string.

        https://substrate.run/nodes#GenerateSpeech
        """
        super().__init__(text=text, store=store, hide=hide, out_type=GenerateSpeechOut, **kwargs)
        self.node = "GenerateSpeech"

    @property
    def future(self) -> FutureGenerateSpeechOut:  # type: ignore
        """
        Future reference to this node's output.

        https://substrate.run/nodes#GenerateSpeech
        """
        return super().future  # type: ignore


class EmbedText(CoreNode[EmbedTextOut]):
    """https://substrate.run/nodes#EmbedText"""

    def __init__(
        self,
        text: str,
        collection_name: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        embedded_metadata_keys: Optional[List[str]] = None,
        doc_id: Optional[str] = None,
        model: Literal["jina-v2", "clip"] = "jina-v2",
        hide: bool = False,
        **kwargs,
    ):
        """
        Args:
            text: Text to embed.
            collection_name: Vector store name.
            metadata: Metadata that can be used to query the vector store. Ignored if `collection_name` is unset.
            embedded_metadata_keys: Choose keys from `metadata` to embed with text.
            doc_id: Vector store document ID. Ignored if `store` is unset.
            model: Selected embedding model.

        https://substrate.run/nodes#EmbedText
        """
        super().__init__(
            text=text,
            collection_name=collection_name,
            metadata=metadata,
            embedded_metadata_keys=embedded_metadata_keys,
            doc_id=doc_id,
            model=model,
            hide=hide,
            out_type=EmbedTextOut,
            **kwargs,
        )
        self.node = "EmbedText"

    @property
    def future(self) -> FutureEmbedTextOut:  # type: ignore
        """
        Future reference to this node's output.

        https://substrate.run/nodes#EmbedText
        """
        return super().future  # type: ignore


class MultiEmbedText(CoreNode[MultiEmbedTextOut]):
    """https://substrate.run/nodes#MultiEmbedText"""

    def __init__(
        self,
        items: List[EmbedTextItem],
        collection_name: Optional[str] = None,
        embedded_metadata_keys: Optional[List[str]] = None,
        model: Literal["jina-v2", "clip"] = "jina-v2",
        hide: bool = False,
        **kwargs,
    ):
        """
        Args:
            items: Items to embed.
            collection_name: Vector store name.
            embedded_metadata_keys: Choose keys from `metadata` to embed with text.
            model: Selected embedding model.

        https://substrate.run/nodes#MultiEmbedText
        """
        super().__init__(
            items=items,
            collection_name=collection_name,
            embedded_metadata_keys=embedded_metadata_keys,
            model=model,
            hide=hide,
            out_type=MultiEmbedTextOut,
            **kwargs,
        )
        self.node = "MultiEmbedText"

    @property
    def future(self) -> FutureMultiEmbedTextOut:  # type: ignore
        """
        Future reference to this node's output.

        https://substrate.run/nodes#MultiEmbedText
        """
        return super().future  # type: ignore


class JinaV2(CoreNode[JinaV2Out]):
    """https://substrate.run/nodes#JinaV2"""

    def __init__(
        self,
        items: List[EmbedTextItem],
        collection_name: Optional[str] = None,
        embedded_metadata_keys: Optional[List[str]] = None,
        hide: bool = False,
        **kwargs,
    ):
        """
        Args:
            items: Items to embed.
            collection_name: Vector store name.
            embedded_metadata_keys: Choose keys from `metadata` to embed with text.

        https://substrate.run/nodes#JinaV2
        """
        super().__init__(
            items=items,
            collection_name=collection_name,
            embedded_metadata_keys=embedded_metadata_keys,
            hide=hide,
            out_type=JinaV2Out,
            **kwargs,
        )
        self.node = "JinaV2"

    @property
    def future(self) -> FutureJinaV2Out:  # type: ignore
        """
        Future reference to this node's output.

        https://substrate.run/nodes#JinaV2
        """
        return super().future  # type: ignore


class EmbedImage(CoreNode[EmbedImageOut]):
    """https://substrate.run/nodes#EmbedImage"""

    def __init__(
        self,
        image_uri: str,
        collection_name: Optional[str] = None,
        doc_id: Optional[str] = None,
        model: Literal["clip"] = "clip",
        hide: bool = False,
        **kwargs,
    ):
        """
        Args:
            image_uri: Image to embed.
            collection_name: Vector store name.
            doc_id: Vector store document ID. Ignored if `collection_name` is unset.
            model: Selected embedding model.

        https://substrate.run/nodes#EmbedImage
        """
        super().__init__(
            image_uri=image_uri,
            collection_name=collection_name,
            doc_id=doc_id,
            model=model,
            hide=hide,
            out_type=EmbedImageOut,
            **kwargs,
        )
        self.node = "EmbedImage"

    @property
    def future(self) -> FutureEmbedImageOut:  # type: ignore
        """
        Future reference to this node's output.

        https://substrate.run/nodes#EmbedImage
        """
        return super().future  # type: ignore


class MultiEmbedImage(CoreNode[MultiEmbedImageOut]):
    """https://substrate.run/nodes#MultiEmbedImage"""

    def __init__(
        self,
        items: List[EmbedImageItem],
        collection_name: Optional[str] = None,
        model: Literal["clip"] = "clip",
        hide: bool = False,
        **kwargs,
    ):
        """
        Args:
            items: Items to embed.
            collection_name: Vector store name.
            model: Selected embedding model.

        https://substrate.run/nodes#MultiEmbedImage
        """
        super().__init__(
            items=items,
            collection_name=collection_name,
            model=model,
            hide=hide,
            out_type=MultiEmbedImageOut,
            **kwargs,
        )
        self.node = "MultiEmbedImage"

    @property
    def future(self) -> FutureMultiEmbedImageOut:  # type: ignore
        """
        Future reference to this node's output.

        https://substrate.run/nodes#MultiEmbedImage
        """
        return super().future  # type: ignore


class CLIP(CoreNode[CLIPOut]):
    """https://substrate.run/nodes#CLIP"""

    def __init__(
        self,
        items: List[EmbedTextOrImageItem],
        collection_name: Optional[str] = None,
        embedded_metadata_keys: Optional[List[str]] = None,
        hide: bool = False,
        **kwargs,
    ):
        """
        Args:
            items: Items to embed.
            collection_name: Vector store name.
            embedded_metadata_keys: Choose keys from `metadata` to embed with text. Only applies to text items.

        https://substrate.run/nodes#CLIP
        """
        super().__init__(
            items=items,
            collection_name=collection_name,
            embedded_metadata_keys=embedded_metadata_keys,
            hide=hide,
            out_type=CLIPOut,
            **kwargs,
        )
        self.node = "CLIP"

    @property
    def future(self) -> FutureCLIPOut:  # type: ignore
        """
        Future reference to this node's output.

        https://substrate.run/nodes#CLIP
        """
        return super().future  # type: ignore


class FindOrCreateVectorStore(CoreNode[FindOrCreateVectorStoreOut]):
    """https://substrate.run/nodes#FindOrCreateVectorStore"""

    def __init__(
        self,
        collection_name: str,
        model: Literal["jina-v2", "clip"],
        hide: bool = False,
        **kwargs,
    ):
        """
        Args:
            collection_name: Vector store name.
            model: Selected embedding model.

        https://substrate.run/nodes#FindOrCreateVectorStore
        """
        super().__init__(
            collection_name=collection_name,
            model=model,
            hide=hide,
            out_type=FindOrCreateVectorStoreOut,
            **kwargs,
        )
        self.node = "FindOrCreateVectorStore"

    @property
    def future(self) -> FutureFindOrCreateVectorStoreOut:  # type: ignore
        """
        Future reference to this node's output.

        https://substrate.run/nodes#FindOrCreateVectorStore
        """
        return super().future  # type: ignore


class ListVectorStores(CoreNode[ListVectorStoresOut]):
    """https://substrate.run/nodes#ListVectorStores"""

    def __init__(self, hide: bool = False, **kwargs):
        """
        Args:

        https://substrate.run/nodes#ListVectorStores
        """
        super().__init__(hide=hide, out_type=ListVectorStoresOut, **kwargs)
        self.node = "ListVectorStores"

    @property
    def future(self) -> FutureListVectorStoresOut:  # type: ignore
        """
        Future reference to this node's output.

        https://substrate.run/nodes#ListVectorStores
        """
        return super().future  # type: ignore


class DeleteVectorStore(CoreNode[DeleteVectorStoreOut]):
    """https://substrate.run/nodes#DeleteVectorStore"""

    def __init__(
        self,
        collection_name: str,
        model: Literal["jina-v2", "clip"],
        hide: bool = False,
        **kwargs,
    ):
        """
        Args:
            collection_name: Vector store name.
            model: Selected embedding model.

        https://substrate.run/nodes#DeleteVectorStore
        """
        super().__init__(
            collection_name=collection_name,
            model=model,
            hide=hide,
            out_type=DeleteVectorStoreOut,
            **kwargs,
        )
        self.node = "DeleteVectorStore"

    @property
    def future(self) -> FutureDeleteVectorStoreOut:  # type: ignore
        """
        Future reference to this node's output.

        https://substrate.run/nodes#DeleteVectorStore
        """
        return super().future  # type: ignore


class FetchVectors(CoreNode[FetchVectorsOut]):
    """https://substrate.run/nodes#FetchVectors"""

    def __init__(
        self,
        collection_name: str,
        model: Literal["jina-v2", "clip"],
        ids: List[str],
        hide: bool = False,
        **kwargs,
    ):
        """
        Args:
            collection_name: Vector store name.
            model: Selected embedding model.
            ids: Document IDs to retrieve.

        https://substrate.run/nodes#FetchVectors
        """
        super().__init__(
            collection_name=collection_name,
            model=model,
            ids=ids,
            hide=hide,
            out_type=FetchVectorsOut,
            **kwargs,
        )
        self.node = "FetchVectors"

    @property
    def future(self) -> FutureFetchVectorsOut:  # type: ignore
        """
        Future reference to this node's output.

        https://substrate.run/nodes#FetchVectors
        """
        return super().future  # type: ignore


class UpdateVectors(CoreNode[UpdateVectorsOut]):
    """https://substrate.run/nodes#UpdateVectors"""

    def __init__(
        self,
        collection_name: str,
        model: Literal["jina-v2", "clip"],
        vectors: List[UpdateVectorParams],
        hide: bool = False,
        **kwargs,
    ):
        """
        Args:
            collection_name: Vector store name.
            model: Selected embedding model.
            vectors: Vectors to upsert.

        https://substrate.run/nodes#UpdateVectors
        """
        super().__init__(
            collection_name=collection_name,
            model=model,
            vectors=vectors,
            hide=hide,
            out_type=UpdateVectorsOut,
            **kwargs,
        )
        self.node = "UpdateVectors"

    @property
    def future(self) -> FutureUpdateVectorsOut:  # type: ignore
        """
        Future reference to this node's output.

        https://substrate.run/nodes#UpdateVectors
        """
        return super().future  # type: ignore


class DeleteVectors(CoreNode[DeleteVectorsOut]):
    """https://substrate.run/nodes#DeleteVectors"""

    def __init__(
        self,
        collection_name: str,
        model: Literal["jina-v2", "clip"],
        ids: List[str],
        hide: bool = False,
        **kwargs,
    ):
        """
        Args:
            collection_name: Vector store name.
            model: Selected embedding model.
            ids: Document IDs to delete.

        https://substrate.run/nodes#DeleteVectors
        """
        super().__init__(
            collection_name=collection_name,
            model=model,
            ids=ids,
            hide=hide,
            out_type=DeleteVectorsOut,
            **kwargs,
        )
        self.node = "DeleteVectors"

    @property
    def future(self) -> FutureDeleteVectorsOut:  # type: ignore
        """
        Future reference to this node's output.

        https://substrate.run/nodes#DeleteVectors
        """
        return super().future  # type: ignore


class QueryVectorStore(CoreNode[QueryVectorStoreOut]):
    """https://substrate.run/nodes#QueryVectorStore"""

    def __init__(
        self,
        collection_name: str,
        model: Literal["jina-v2", "clip"],
        query_strings: Optional[List[str]] = None,
        query_image_uris: Optional[List[str]] = None,
        query_vectors: Optional[List[List[float]]] = None,
        query_ids: Optional[List[str]] = None,
        top_k: int = 10,
        ef_search: int = 40,
        num_leaves_to_search: int = 40,
        include_values: bool = False,
        include_metadata: bool = False,
        filters: Optional[Dict[str, Any]] = None,
        hide: bool = False,
        **kwargs,
    ):
        """
        Args:
            collection_name: Vector store to query against.
            model: Selected embedding model.
            query_strings: Texts to embed and use for the query.
            query_image_uris: Image URIs to embed and use for the query.
            query_vectors: Vectors to use for the query.
            query_ids: Document IDs to use for the query.
            top_k: Number of results to return.
            ef_search: The size of the dynamic candidate list for searching the index graph.
            num_leaves_to_search: The number of leaves in the index tree to search.
            include_values: Include the values of the vectors in the response.
            include_metadata: Include the metadata of the vectors in the response.
            filters: Filter metadata by key-value pairs.

        https://substrate.run/nodes#QueryVectorStore
        """
        super().__init__(
            collection_name=collection_name,
            model=model,
            query_strings=query_strings,
            query_image_uris=query_image_uris,
            query_vectors=query_vectors,
            query_ids=query_ids,
            top_k=top_k,
            ef_search=ef_search,
            num_leaves_to_search=num_leaves_to_search,
            include_values=include_values,
            include_metadata=include_metadata,
            filters=filters,
            hide=hide,
            out_type=QueryVectorStoreOut,
            **kwargs,
        )
        self.node = "QueryVectorStore"

    @property
    def future(self) -> FutureQueryVectorStoreOut:  # type: ignore
        """
        Future reference to this node's output.

        https://substrate.run/nodes#QueryVectorStore
        """
        return super().future  # type: ignore


class SplitDocument(CoreNode[SplitDocumentOut]):
    """https://substrate.run/nodes#SplitDocument"""

    def __init__(
        self,
        uri: str,
        doc_id: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        chunk_size: Optional[int] = None,
        chunk_overlap: Optional[int] = None,
        hide: bool = False,
        **kwargs,
    ):
        """
        Args:
            uri: URI of the document.
            doc_id: Document ID.
            metadata: Document metadata.
            chunk_size: Maximum number of units per chunk. Defaults to 1024 tokens for text or 40 lines for code.
            chunk_overlap: Number of units to overlap between chunks. Defaults to 200 tokens for text or 15 lines for code.

        https://substrate.run/nodes#SplitDocument
        """
        super().__init__(
            uri=uri,
            doc_id=doc_id,
            metadata=metadata,
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            hide=hide,
            out_type=SplitDocumentOut,
            **kwargs,
        )
        self.node = "SplitDocument"

    @property
    def future(self) -> FutureSplitDocumentOut:  # type: ignore
        """
        Future reference to this node's output.

        https://substrate.run/nodes#SplitDocument
        """
        return super().future  # type: ignore
