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


@dataclass
class ResponseFormat:
    """
    (Future reference)
    """

    type: Literal["json_object", "text"]
    """
    (Future reference)
    Type of response.
    """
    json_schema: Optional[Dict[str, Any]] = None
    """
    (Future reference)
    JSON schema to guide `json_object` response.
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
    model: Optional[Literal["mistral-7b-instruct"]] = "mistral-7b-instruct"
    """
    (Future reference)
    Selected model.
    """
    response_format: Optional[ResponseFormat] = None
    """
    (Future reference)
    Format of the response.
    """
    temperature: Optional[int] = 4
    """
    (Future reference)
    Sampling temperature to use. Higher values make the output more random, lower values make the output more deterministic.
    """
    max_tokens: Optional[int] = 800
    """
    (Future reference)
    Maximum number of tokens to generate.
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
    model: Optional[Literal["mistral-7b-instruct"]] = "mistral-7b-instruct"
    """
    (Future reference)
    Selected model.
    """
    response_format: Optional[ResponseFormat] = None
    """
    (Future reference)
    Format of the response.
    """
    temperature: Optional[int] = 4
    """
    (Future reference)
    Sampling temperature to use. Higher values make the output more random, lower values make the output more deterministic.
    """
    max_tokens: Optional[int] = 800
    """
    (Future reference)
    Maximum number of tokens to generate.
    """


@dataclass
class FutureGenerateTextOut:
    """
    (Future reference)
    """

    text: Optional[str] = None
    """
    (Future reference)
    Text response.
    """
    json_object: Optional[Dict[str, Any]] = None
    """
    (Future reference)
    JSON response.
    """


@dataclass
class FutureMultiGenerateTextOut:
    """
    (Future reference)
    """

    choices: List[FutureGenerateTextOut]


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
    image_uris: Optional[List[str]] = None
    """
    (Future reference)
    Image prompts.
    """
    model: Optional[Literal["firellava-13b"]] = "firellava-13b"
    """
    (Future reference)
    Selected model.
    """
    temperature: Optional[int] = 4
    """
    (Future reference)
    Sampling temperature to use. Higher values make the output more random, lower values make the output more deterministic.
    """
    max_tokens: Optional[int] = 800
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
class FutureGenerateImageIn:
    """
    (Future reference)
    """

    prompt: str
    """
    (Future reference)
    Text prompt.
    """
    image_prompt_uri: Optional[str] = None
    """
    (Future reference)
    Image prompt.
    """
    model: Optional[Literal["stablediffusion-xl"]] = "stablediffusion-xl"
    """
    (Future reference)
    Selected model.
    """
    image_influence: Optional[float] = 5
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
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](/docs/file-stores). If unset, the image data will be returned as a base64-encoded string.
    """
    width: Optional[int] = None
    """
    (Future reference)
    Width of output image, in pixels.
    """
    height: Optional[int] = None
    """
    (Future reference)
    Height of output image, in pixels.
    """
    seed: Optional[int] = None
    """
    (Future reference)
    Seed for deterministic generation. Default is a random seed.
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
    seed: int
    """
    (Future reference)
    The random noise seed used for generation.
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
    image_prompt_uri: Optional[str] = None
    """
    (Future reference)
    Image prompt.
    """
    model: Optional[Literal["stablediffusion-xl"]] = "stablediffusion-xl"
    """
    (Future reference)
    Selected model.
    """
    image_influence: Optional[float] = 5
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
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](/docs/file-stores). If unset, the image data will be returned as a base64-encoded string.
    """
    width: Optional[int] = None
    """
    (Future reference)
    Width of output image, in pixels.
    """
    height: Optional[int] = None
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
class FutureMultiGenerateImageOut:
    """
    (Future reference)
    """

    outputs: List[FutureGenerateImageOut]


@dataclass
class FutureControlledGenerateImageIn:
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
    output_resolution: Optional[int] = 1024
    """
    (Future reference)
    Resolution of the output image, in pixels.
    """
    model: Optional[Literal["stablediffusion-xl"]] = "stablediffusion-xl"
    """
    (Future reference)
    Selected model.
    """
    negative_prompt: Optional[str] = None
    """
    (Future reference)
    Negative input prompt.
    """
    store: Optional[str] = None
    """
    (Future reference)
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](/docs/file-stores). If unset, the image data will be returned as a base64-encoded string.
    """
    image_influence: Optional[float] = 9
    """
    (Future reference)
    Controls the influence of the input image on the generated output.
    """
    seed: Optional[int] = None
    """
    (Future reference)
    Seed for deterministic generation. Default is a random seed.
    """


@dataclass
class FutureControlledGenerateImageOut:
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
class FutureMultiControlledGenerateImageIn:
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
    output_resolution: Optional[int] = 1024
    """
    (Future reference)
    Resolution of the output image, in pixels.
    """
    model: Optional[Literal["stablediffusion-xl"]] = "stablediffusion-xl"
    """
    (Future reference)
    Selected model.
    """
    negative_prompt: Optional[str] = None
    """
    (Future reference)
    Negative input prompt.
    """
    store: Optional[str] = None
    """
    (Future reference)
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](/docs/file-stores). If unset, the image data will be returned as a base64-encoded string.
    """
    image_influence: Optional[float] = 9
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
class FutureMultiControlledGenerateImageOut:
    """
    (Future reference)
    """

    outputs: List[FutureControlledGenerateImageOut]


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
    image_prompt_uri: Optional[str] = None
    """
    (Future reference)
    Image prompt.
    """
    output_resolution: Optional[int] = 1024
    """
    (Future reference)
    Resolution of the output image, in pixels.
    """
    model: Optional[Literal["stablediffusion-xl"]] = "stablediffusion-xl"
    """
    (Future reference)
    Selected model.
    """
    strength: Optional[float] = 8
    """
    (Future reference)
    Controls the strength of the generation process.
    """
    image_prompt_influence: Optional[float] = 5
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
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](/docs/file-stores). If unset, the image data will be returned as a base64-encoded string.
    """
    seed: Optional[int] = None
    """
    (Future reference)
    Seed for deterministic generation. Default is a random seed.
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
    seed: int
    """
    (Future reference)
    The random noise seed used for generation.
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
    image_prompt_uri: Optional[str] = None
    """
    (Future reference)
    Image prompt.
    """
    output_resolution: Optional[int] = 1024
    """
    (Future reference)
    Resolution of the output image, in pixels.
    """
    model: Optional[Literal["stablediffusion-xl"]] = "stablediffusion-xl"
    """
    (Future reference)
    Selected model.
    """
    negative_prompt: Optional[str] = None
    """
    (Future reference)
    Negative input prompt.
    """
    store: Optional[str] = None
    """
    (Future reference)
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](/docs/file-stores). If unset, the image data will be returned as a base64-encoded string.
    """
    strength: Optional[float] = 8
    """
    (Future reference)
    Controls the strength of the generation process.
    """
    image_prompt_influence: Optional[float] = 5
    """
    (Future reference)
    Controls the influence of the image prompt on the generated output.
    """
    seeds: Optional[List[int]] = None
    """
    (Future reference)
    Random noise seeds. Default is random seeds for each generation.
    """


@dataclass
class FutureMultiGenerativeEditImageOut:
    """
    (Future reference)
    """

    outputs: List[FutureGenerativeEditImageOut]


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
    model: Optional[Literal["big-lama"]] = "big-lama"
    """
    (Future reference)
    Selected model.
    """
    store: Optional[str] = None
    """
    (Future reference)
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](/docs/file-stores). If unset, the image data will be returned as a base64-encoded string.
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
class FutureRemoveBackgroundIn:
    """
    (Future reference)
    """

    image_uri: str
    """
    (Future reference)
    Input image.
    """
    return_mask: Optional[bool] = None
    """
    (Future reference)
    Return a mask image instead of the original content.
    """
    background_color: Optional[str] = None
    """
    (Future reference)
    Hex value background color. Transparent if unset.
    """
    model: Optional[Literal["isnet"]] = "isnet"
    """
    (Future reference)
    Selected model.
    """
    store: Optional[str] = None
    """
    (Future reference)
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](/docs/file-stores). If unset, the image data will be returned as a base64-encoded string.
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
class FutureUpscaleImageIn:
    """
    (Future reference)
    """

    image_uri: str
    """
    (Future reference)
    Input image.
    """
    model: Optional[Literal["real-esrgan-x4"]] = "real-esrgan-x4"
    """
    (Future reference)
    Selected model.
    """
    store: Optional[str] = None
    """
    (Future reference)
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](/docs/file-stores). If unset, the image data will be returned as a base64-encoded string.
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
class FutureDetectSegmentsIn:
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
    Point prompts, to detect a segment under the point. One of `point_prompt` or `box_prompt` must be set.
    """
    box_prompts: Optional[List[BoundingBox]] = None
    """
    (Future reference)
    Box prompts, to detect a segment within the bounding box. One of `point_prompt` or `box_prompt` must be set.
    """
    model: Optional[Literal["segment-anything"]] = "segment-anything"
    """
    (Future reference)
    Selected model.
    """
    store: Optional[str] = None
    """
    (Future reference)
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](/docs/file-stores). If unset, the image data will be returned as a base64-encoded string.
    """


@dataclass
class FutureDetectSegmentsOut:
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
    language: Optional[str] = "en"
    """
    (Future reference)
    Language of input audio in [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes) format.
    """
    segment: Optional[bool] = False
    """
    (Future reference)
    Segment the text into sentences with approximate timestamps.
    """
    align: Optional[bool] = False
    """
    (Future reference)
    Align transcription to produce more accurate sentence-level timestamps and word-level timestamps. An array of word segments will be included in each sentence segment.
    """
    diarize: Optional[bool] = False
    """
    (Future reference)
    Identify speakers for each segment. Speaker IDs will be included in each segment.
    """
    suggest_chapters: Optional[bool] = False
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
    audio_uri: Optional[str] = None
    """
    (Future reference)
    Reference audio used to synthesize the speaker. If unset, a default speaker voice will be used.
    """
    language: Optional[str] = "en"
    """
    (Future reference)
    Language of input text. Supported languages: `en, de, fr, es, it, pt, pl, zh, ar, cs, ru, nl, tr, hu, ko`.
    """
    store: Optional[str] = None
    """
    (Future reference)
    Use "hosted" to return an audio URL hosted on Substrate. You can also provide a URL to a registered [file store](/docs/file-stores). If unset, the audio data will be returned as a base64-encoded string.
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
class Embedding:
    """
    (Future reference)
    """

    vector: List[float]
    """
    (Future reference)
    Embedding vector.
    """
    document_id: Optional[str] = None
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
    model: Optional[Literal["jina-v2", "clip"]] = "jina-v2"
    """
    (Future reference)
    Selected model.
    """
    store: Optional[str] = None
    """
    (Future reference)
    [Vector store](/docs/vector-stores) identifier.
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
    document_id: Optional[str] = None
    """
    (Future reference)
    Vector store document ID. Ignored if `store` is unset.
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
    document_id: Optional[str] = None
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
    model: Optional[Literal["jina-v2", "clip"]] = "jina-v2"
    """
    (Future reference)
    Selected model.
    """
    store: Optional[str] = None
    """
    (Future reference)
    [Vector store](/docs/vector-stores) identifier.
    """
    embedded_metadata_keys: Optional[List[str]] = None
    """
    (Future reference)
    Choose keys from `metadata` to embed with text.
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
class FutureEmbedImageIn:
    """
    (Future reference)
    """

    image_uri: str
    """
    (Future reference)
    Image to embed.
    """
    model: Optional[Literal["clip"]] = "clip"
    """
    (Future reference)
    Selected model.
    """
    store: Optional[str] = None
    """
    (Future reference)
    [Vector store](/docs/vector-stores) identifier.
    """
    document_id: Optional[str] = None
    """
    (Future reference)
    Vector store document ID. Ignored if `store` is unset.
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
    document_id: Optional[str] = None
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
    store: Optional[str] = None
    """
    (Future reference)
    [Vector store](/docs/vector-stores) identifier.
    """
    model: Optional[Literal["clip"]] = "clip"
    """
    (Future reference)
    Selected model.
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
class VectorStoreParams:
    """
    (Future reference)
    Fields describing a vector store and its associated index.
    """

    name: str
    """
    (Future reference)
    Vector store name.
    """
    model: Literal["jina-v2", "clip"]
    """
    (Future reference)
    Selected embedding model
    """
    m: Optional[int] = 16
    """
    (Future reference)
    The max number of connections per layer for the index.
    """
    ef_construction: Optional[int] = 64
    """
    (Future reference)
    The size of the dynamic candidate list for constructing the index graph.
    """
    metric: Optional[Literal["cosine", "l2", "inner"]] = "inner"
    """
    (Future reference)
    The distance metric to construct the index with.
    """


@dataclass
class DeleteVectorStoreParams:
    """
    (Future reference)
    """

    name: str
    """
    (Future reference)
    Vector store name.
    """
    model: Literal["jina-v2", "clip"]
    """
    (Future reference)
    Selected embedding model
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
class GetVectorsParams:
    """
    (Future reference)
    """

    name: str
    """
    (Future reference)
    Vector store name.
    """
    model: Literal["jina-v2", "clip"]
    """
    (Future reference)
    Selected embedding model
    """
    ids: List[str]
    """
    (Future reference)
    Document IDs to retrieve.
    """


@dataclass
class GetVectorsResponse:
    """
    (Future reference)
    """

    vectors: List[Vector]
    """
    (Future reference)
    Retrieved vectors.
    """


@dataclass
class VectorUpdateCountResponse:
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
    Document to update.
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
class UpdateVectorsParams:
    """
    (Future reference)
    """

    name: str
    """
    (Future reference)
    Vector store name.
    """
    model: Literal["jina-v2", "clip"]
    """
    (Future reference)
    Selected embedding model
    """
    vectors: List[UpdateVectorParams]
    """
    (Future reference)
    Vectors to upsert.
    """


@dataclass
class DeleteVectorsParams:
    """
    (Future reference)
    """

    name: str
    """
    (Future reference)
    Vector store name.
    """
    model: Literal["jina-v2", "clip"]
    """
    (Future reference)
    Selected embedding model
    """
    ids: List[str]
    """
    (Future reference)
    Document IDs to delete.
    """


@dataclass
class QueryVectorStoreParams:
    """
    (Future reference)
    """

    name: str
    """
    (Future reference)
    Vector store to query against.
    """
    model: Literal["jina-v2", "clip"]
    """
    (Future reference)
    Selected embedding model
    """
    query_ids: Optional[List[str]] = None
    """
    (Future reference)
    Document IDs to use for the query.
    """
    query_image_uris: Optional[List[str]] = None
    """
    (Future reference)
    Image URIs to embed and use for the query.
    """
    query_vectors: Optional[List[List[float]]] = None
    """
    (Future reference)
    Vector to use for the query.
    """
    query_strings: Optional[List[str]] = None
    """
    (Future reference)
    Texts to embed and use for the query.
    """
    top_k: Optional[int] = 10
    """
    (Future reference)
    Number of results to return.
    """
    ef_search: Optional[int] = 40
    """
    (Future reference)
    The size of the dynamic candidate list for searching the index graph.
    """
    include_values: Optional[bool] = False
    """
    (Future reference)
    Include the values of the vectors in the response.
    """
    include_metadata: Optional[bool] = False
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
class QueryVectorStoreResponse:
    """
    (Future reference)
    """

    results: List[List[VectorStoreQueryResult]]
    """
    (Future reference)
    Query results.
    """
    name: Optional[str] = None
    """
    (Future reference)
    Vector store name.
    """
    model: Optional[Literal["jina-v2", "clip"]] = None
    """
    (Future reference)
    Selected embedding model
    """
    metric: Optional[Literal["cosine", "l2", "inner"]] = None
    """
    (Future reference)
    The distance metric used for the query.
    """
