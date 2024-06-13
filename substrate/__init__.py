"""
𐃏 Substrate Python SDK

20240612.20240612
"""

import warnings

import pydantic

if pydantic.VERSION.startswith("2"):
    warnings.filterwarnings("ignore", category=pydantic.warnings.PydanticDeprecatedSince20)

from .nodes import (
    CLIP,
    JinaV2,
    EmbedText,
    EmbedImage,
    EraseImage,
    Experimental,
    FetchVectors,
    Firellava13B,
    GenerateJSON,
    GenerateText,
    InpaintImage,
    UpscaleImage,
    DeleteVectors,
    GenerateImage,
    UpdateVectors,
    GenerateSpeech,
    MultiEmbedText,
    MultiEmbedImage,
    SegmentAnything,
    ListVectorStores,
    Llama3Instruct8B,
    QueryVectorStore,
    RemoveBackground,
    TranscribeSpeech,
    BatchGenerateJSON,
    BatchGenerateText,
    DeleteVectorStore,
    Llama3Instruct70B,
    Mistral7BInstruct,
    MultiGenerateJSON,
    MultiGenerateText,
    MultiInpaintImage,
    SegmentUnderPoint,
    MultiGenerateImage,
    Mixtral8x7BInstruct,
    FindOrCreateVectorStore,
    StableDiffusionXLInpaint,
    StableDiffusionXLLightning,
    StableDiffusionXLControlNet,
)
from .core.sb import sb
from ._version import __version__
from .substrate import Substrate, SubstrateResponse
from .run_python import RunPython

__all__ = [
    "__version__",
    "SubstrateResponse",
    "sb",
    "Substrate",
    "Experimental",
    "RunPython",
    "GenerateText",
    "MultiGenerateText",
    "BatchGenerateText",
    "BatchGenerateJSON",
    "GenerateJSON",
    "MultiGenerateJSON",
    "Mistral7BInstruct",
    "Mixtral8x7BInstruct",
    "Llama3Instruct8B",
    "Llama3Instruct70B",
    "Firellava13B",
    "GenerateImage",
    "MultiGenerateImage",
    "InpaintImage",
    "MultiInpaintImage",
    "StableDiffusionXLLightning",
    "StableDiffusionXLInpaint",
    "StableDiffusionXLControlNet",
    "TranscribeSpeech",
    "GenerateSpeech",
    "RemoveBackground",
    "EraseImage",
    "UpscaleImage",
    "SegmentUnderPoint",
    "SegmentAnything",
    "EmbedText",
    "MultiEmbedText",
    "EmbedImage",
    "MultiEmbedImage",
    "JinaV2",
    "CLIP",
    "FindOrCreateVectorStore",
    "ListVectorStores",
    "DeleteVectorStore",
    "QueryVectorStore",
    "FetchVectors",
    "UpdateVectors",
    "DeleteVectors",
]
