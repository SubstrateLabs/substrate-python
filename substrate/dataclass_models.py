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
    type: Literal["api_error", "invalid_request_error"]
    """
    The type of error returned.
    """
    message: str
    """
    A message providing more details about the error.
    """


@dataclass
class ResponseFormat:
    type: Literal["json_object", "text"]
    """
    Type of response.
    """
    json_schema: Optional[Dict[str, Any]] = None
    """
    JSON schema to guide `json_object` response.
    """


@dataclass
class GenerateTextIn:
    prompt: str
    """
    Input prompt.
    """
    model: Optional[Literal["mistral-7b-instruct"]] = "mistral-7b-instruct"
    """
    Selected model.
    """
    response_format: Optional[ResponseFormat] = None
    """
    Format of the response.
    """
    temperature: Optional[int] = 4
    """
    Sampling temperature to use. Higher values make the output more random, lower values make the output more deterministic.
    """
    max_tokens: Optional[int] = 800
    """
    Maximum number of tokens to generate.
    """


@dataclass
class MultiGenerateTextIn:
    prompt: str
    """
    Input prompt.
    """
    num_choices: int
    """
    Number of choices to generate.
    """
    model: Optional[Literal["mistral-7b-instruct"]] = "mistral-7b-instruct"
    """
    Selected model.
    """
    response_format: Optional[ResponseFormat] = None
    """
    Format of the response.
    """
    temperature: Optional[int] = 4
    """
    Sampling temperature to use. Higher values make the output more random, lower values make the output more deterministic.
    """
    max_tokens: Optional[int] = 800
    """
    Maximum number of tokens to generate.
    """


@dataclass
class GenerateTextOut:
    text: Optional[str] = None
    """
    Text response.
    """
    json_object: Optional[Dict[str, Any]] = None
    """
    JSON response.
    """


@dataclass
class MultiGenerateTextOut:
    choices: List[GenerateTextOut]


@dataclass
class GenerateTextVisionIn:
    prompt: str
    """
    Text prompt.
    """
    image_uris: Optional[List[str]] = None
    """
    Image prompts.
    """
    model: Optional[Literal["firellava-13b"]] = "firellava-13b"
    """
    Selected model.
    """
    temperature: Optional[int] = 4
    """
    Sampling temperature to use. Higher values make the output more random, lower values make the output more deterministic.
    """
    max_tokens: Optional[int] = 800
    """
    Maximum number of tokens to generate.
    """


@dataclass
class GenerateTextVisionOut:
    text: str
    """
    Text response.
    """


@dataclass
class GenerateImageIn:
    prompt: str
    """
    Text prompt.
    """
    image_prompt_uri: Optional[str] = None
    """
    Image prompt.
    """
    model: Optional[Literal["stablediffusion-xl"]] = "stablediffusion-xl"
    """
    Selected model.
    """
    image_influence: Optional[float] = 5
    """
    Controls the influence of the image prompt on the generated output.
    """
    negative_prompt: Optional[str] = None
    """
    Negative input prompt.
    """
    store: Optional[str] = None
    """
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](/docs/file-stores). If unset, the image data will be returned as a base64-encoded string.
    """
    width: Optional[int] = None
    """
    Width of output image, in pixels.
    """
    height: Optional[int] = None
    """
    Height of output image, in pixels.
    """
    seed: Optional[int] = None
    """
    Seed for deterministic generation. Default is a random seed.
    """


@dataclass
class GenerateImageOut:
    image_uri: str
    """
    Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """
    seed: int
    """
    The random noise seed used for generation.
    """


@dataclass
class MultiGenerateImageIn:
    prompt: str
    """
    Text prompt.
    """
    num_images: int
    """
    Number of images to generate.
    """
    image_prompt_uri: Optional[str] = None
    """
    Image prompt.
    """
    model: Optional[Literal["stablediffusion-xl"]] = "stablediffusion-xl"
    """
    Selected model.
    """
    image_influence: Optional[float] = 5
    """
    Controls the influence of the image prompt on the generated output.
    """
    negative_prompt: Optional[str] = None
    """
    Negative input prompt.
    """
    store: Optional[str] = None
    """
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](/docs/file-stores). If unset, the image data will be returned as a base64-encoded string.
    """
    width: Optional[int] = None
    """
    Width of output image, in pixels.
    """
    height: Optional[int] = None
    """
    Height of output image, in pixels.
    """
    seeds: Optional[List[int]] = None
    """
    Random noise seeds. Default is random seeds for each generation.
    """


@dataclass
class MultiGenerateImageOut:
    outputs: List[GenerateImageOut]


@dataclass
class ControlledGenerateImageIn:
    image_uri: str
    """
    Input image.
    """
    control_method: Literal["edge", "depth", "illusion"]
    """
    Strategy to control generation using the input image.
    """
    prompt: str
    """
    Text prompt.
    """
    output_resolution: Optional[int] = 1024
    """
    Resolution of the output image, in pixels.
    """
    model: Optional[Literal["stablediffusion-xl"]] = "stablediffusion-xl"
    """
    Selected model.
    """
    negative_prompt: Optional[str] = None
    """
    Negative input prompt.
    """
    store: Optional[str] = None
    """
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](/docs/file-stores). If unset, the image data will be returned as a base64-encoded string.
    """
    image_influence: Optional[float] = 9
    """
    Controls the influence of the input image on the generated output.
    """
    seed: Optional[int] = None
    """
    Seed for deterministic generation. Default is a random seed.
    """


@dataclass
class ControlledGenerateImageOut:
    image_uri: str
    """
    Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """
    seed: int
    """
    The random noise seed used for generation.
    """


@dataclass
class MultiControlledGenerateImageIn:
    image_uri: str
    """
    Input image.
    """
    control_method: Literal["edge", "depth", "illusion"]
    """
    Strategy to control generation using the input image.
    """
    prompt: str
    """
    Text prompt.
    """
    num_images: int
    """
    Number of images to generate.
    """
    output_resolution: Optional[int] = 1024
    """
    Resolution of the output image, in pixels.
    """
    model: Optional[Literal["stablediffusion-xl"]] = "stablediffusion-xl"
    """
    Selected model.
    """
    negative_prompt: Optional[str] = None
    """
    Negative input prompt.
    """
    store: Optional[str] = None
    """
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](/docs/file-stores). If unset, the image data will be returned as a base64-encoded string.
    """
    image_influence: Optional[float] = 9
    """
    Controls the influence of the input image on the generated output.
    """
    seeds: Optional[List[int]] = None
    """
    Random noise seeds. Default is random seeds for each generation.
    """


@dataclass
class MultiControlledGenerateImageOut:
    outputs: List[ControlledGenerateImageOut]


@dataclass
class GenerativeEditImageIn:
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
    image_prompt_uri: Optional[str] = None
    """
    Image prompt.
    """
    output_resolution: Optional[int] = 1024
    """
    Resolution of the output image, in pixels.
    """
    model: Optional[Literal["stablediffusion-xl"]] = "stablediffusion-xl"
    """
    Selected model.
    """
    strength: Optional[float] = 8
    """
    Controls the strength of the generation process.
    """
    image_prompt_influence: Optional[float] = 5
    """
    Controls the influence of the image prompt on the generated output.
    """
    negative_prompt: Optional[str] = None
    """
    Negative input prompt.
    """
    store: Optional[str] = None
    """
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](/docs/file-stores). If unset, the image data will be returned as a base64-encoded string.
    """
    seed: Optional[int] = None
    """
    Seed for deterministic generation. Default is a random seed.
    """


@dataclass
class GenerativeEditImageOut:
    image_uri: str
    """
    Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """
    seed: int
    """
    The random noise seed used for generation.
    """


@dataclass
class MultiGenerativeEditImageIn:
    image_uri: str
    """
    Original image.
    """
    prompt: str
    """
    Text prompt.
    """
    num_images: int
    """
    Number of images to generate.
    """
    mask_image_uri: Optional[str] = None
    """
    Mask image that controls which pixels are edited (inpainting). If unset, the entire image is edited (image-to-image).
    """
    image_prompt_uri: Optional[str] = None
    """
    Image prompt.
    """
    output_resolution: Optional[int] = 1024
    """
    Resolution of the output image, in pixels.
    """
    model: Optional[Literal["stablediffusion-xl"]] = "stablediffusion-xl"
    """
    Selected model.
    """
    negative_prompt: Optional[str] = None
    """
    Negative input prompt.
    """
    store: Optional[str] = None
    """
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](/docs/file-stores). If unset, the image data will be returned as a base64-encoded string.
    """
    strength: Optional[float] = 8
    """
    Controls the strength of the generation process.
    """
    image_prompt_influence: Optional[float] = 5
    """
    Controls the influence of the image prompt on the generated output.
    """
    seeds: Optional[List[int]] = None
    """
    Random noise seeds. Default is random seeds for each generation.
    """


@dataclass
class MultiGenerativeEditImageOut:
    outputs: List[GenerativeEditImageOut]


@dataclass
class BoundingBox:
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


@dataclass
class Point:
    x: int
    """
    X position.
    """
    y: int
    """
    Y position.
    """


@dataclass
class FillMaskIn:
    image_uri: str
    """
    Input image.
    """
    mask_image_uri: str
    """
    Mask image that controls which pixels are inpainted.
    """
    model: Optional[Literal["big-lama"]] = "big-lama"
    """
    Selected model.
    """
    store: Optional[str] = None
    """
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](/docs/file-stores). If unset, the image data will be returned as a base64-encoded string.
    """


@dataclass
class FillMaskOut:
    image_uri: str
    """
    Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """


@dataclass
class RemoveBackgroundIn:
    image_uri: str
    """
    Input image.
    """
    return_mask: Optional[bool] = None
    """
    Return a mask image instead of the original content.
    """
    background_color: Optional[str] = None
    """
    Hex value background color. Transparent if unset.
    """
    model: Optional[Literal["isnet"]] = "isnet"
    """
    Selected model.
    """
    store: Optional[str] = None
    """
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](/docs/file-stores). If unset, the image data will be returned as a base64-encoded string.
    """


@dataclass
class RemoveBackgroundOut:
    image_uri: str
    """
    Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """


@dataclass
class UpscaleImageIn:
    image_uri: str
    """
    Input image.
    """
    model: Optional[Literal["real-esrgan-x4"]] = "real-esrgan-x4"
    """
    Selected model.
    """
    store: Optional[str] = None
    """
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](/docs/file-stores). If unset, the image data will be returned as a base64-encoded string.
    """


@dataclass
class UpscaleImageOut:
    image_uri: str
    """
    Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """


@dataclass
class DetectSegmentsIn:
    image_uri: str
    """
    Input image.
    """
    point_prompts: Optional[List[Point]] = None
    """
    Point prompts, to detect a segment under the point. One of `point_prompt` or `box_prompt` must be set.
    """
    box_prompts: Optional[List[BoundingBox]] = None
    """
    Box prompts, to detect a segment within the bounding box. One of `point_prompt` or `box_prompt` must be set.
    """
    model: Optional[Literal["segment-anything"]] = "segment-anything"
    """
    Selected model.
    """
    store: Optional[str] = None
    """
    Use "hosted" to return an image URL hosted on Substrate. You can also provide a URL to a registered [file store](/docs/file-stores). If unset, the image data will be returned as a base64-encoded string.
    """


@dataclass
class DetectSegmentsOut:
    mask_image_uri: str
    """
    Detected segments in 'mask image' format. Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """


@dataclass
class TranscribeMediaIn:
    audio_uri: str
    """
    Input audio.
    """
    prompt: Optional[str] = None
    """
    Prompt to guide model on the content and context of input audio.
    """
    language: Optional[str] = "en"
    """
    Language of input audio in [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes) format.
    """
    segment: Optional[bool] = False
    """
    Segment the text into sentences with approximate timestamps.
    """
    align: Optional[bool] = False
    """
    Align transcription to produce more accurate sentence-level timestamps and word-level timestamps. An array of word segments will be included in each sentence segment.
    """
    diarize: Optional[bool] = False
    """
    Identify speakers for each segment. Speaker IDs will be included in each segment.
    """
    suggest_chapters: Optional[bool] = False
    """
    Suggest automatic chapter markers.
    """


@dataclass
class TranscribedWord:
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


@dataclass
class TranscribedSegment:
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


@dataclass
class ChapterMarker:
    title: str
    """
    Chapter title.
    """
    start: float
    """
    Start time of chapter, in seconds.
    """


@dataclass
class TranscribeMediaOut:
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


@dataclass
class GenerateSpeechIn:
    text: str
    """
    Input text.
    """
    audio_uri: Optional[str] = None
    """
    Reference audio used to synthesize the speaker. If unset, a default speaker voice will be used.
    """
    language: Optional[str] = "en"
    """
    Language of input text. Supported languages: `en, de, fr, es, it, pt, pl, zh, ar, cs, ru, nl, tr, hu, ko`.
    """
    store: Optional[str] = None
    """
    Use "hosted" to return an audio URL hosted on Substrate. You can also provide a URL to a registered [file store](/docs/file-stores). If unset, the audio data will be returned as a base64-encoded string.
    """


@dataclass
class GenerateSpeechOut:
    audio_uri: str
    """
    Base 64-encoded WAV audio bytes, or a hosted audio url if `store` is provided.
    """


@dataclass
class Embedding:
    vector: List[float]
    """
    Embedding vector.
    """
    document_id: Optional[str] = None
    """
    Vector store document ID.
    """
    metadata: Optional[Dict[str, Any]] = None
    """
    Vector store document metadata.
    """


@dataclass
class EmbedTextIn:
    text: str
    """
    Text to embed.
    """
    model: Optional[Literal["jina-v2", "clip"]] = "jina-v2"
    """
    Selected model.
    """
    store: Optional[str] = None
    """
    [Vector store](/docs/vector-stores) identifier.
    """
    metadata: Optional[Dict[str, Any]] = None
    """
    Metadata that can be used to query the vector store. Ignored if `store` is unset.
    """
    embedded_metadata_keys: Optional[List[str]] = None
    """
    Choose keys from `metadata` to embed with text.
    """
    document_id: Optional[str] = None
    """
    Vector store document ID. Ignored if `store` is unset.
    """


@dataclass
class EmbedTextOut:
    embedding: Embedding
    """
    Generated embedding.
    """


@dataclass
class EmbedTextItem:
    text: str
    """
    Text to embed.
    """
    metadata: Optional[Dict[str, Any]] = None
    """
    Metadata that can be used to query the vector store. Ignored if `store` is unset.
    """
    document_id: Optional[str] = None
    """
    Vector store document ID. Ignored if `store` is unset.
    """


@dataclass
class MultiEmbedTextIn:
    items: List[EmbedTextItem]
    """
    Items to embed.
    """
    model: Optional[Literal["jina-v2", "clip"]] = "jina-v2"
    """
    Selected model.
    """
    store: Optional[str] = None
    """
    [Vector store](/docs/vector-stores) identifier.
    """
    embedded_metadata_keys: Optional[List[str]] = None
    """
    Choose keys from `metadata` to embed with text.
    """


@dataclass
class MultiEmbedTextOut:
    embeddings: List[Embedding]
    """
    Generated embeddings.
    """


@dataclass
class EmbedImageIn:
    image_uri: str
    """
    Image to embed.
    """
    model: Optional[Literal["clip"]] = "clip"
    """
    Selected model.
    """
    store: Optional[str] = None
    """
    [Vector store](/docs/vector-stores) identifier.
    """
    document_id: Optional[str] = None
    """
    Vector store document ID. Ignored if `store` is unset.
    """


@dataclass
class EmbedImageOut:
    embedding: Embedding
    """
    Generated embedding.
    """


@dataclass
class EmbedImageItem:
    image_uri: str
    """
    Image to embed.
    """
    document_id: Optional[str] = None
    """
    Vector store document ID. Ignored if `store` is unset.
    """


@dataclass
class MultiEmbedImageIn:
    items: List[EmbedImageItem]
    """
    Items to embed.
    """
    store: Optional[str] = None
    """
    [Vector store](/docs/vector-stores) identifier.
    """
    model: Optional[Literal["clip"]] = "clip"
    """
    Selected model.
    """


@dataclass
class MultiEmbedImageOut:
    embeddings: List[Embedding]
    """
    Generated embeddings.
    """


@dataclass
class VectorStoreParams:
    """
    Fields describing a vector store and its associated index.
    """

    name: str
    """
    Vector store name.
    """
    model: Literal["jina-v2", "clip"]
    """
    Selected embedding model
    """
    m: Optional[int] = 16
    """
    The max number of connections per layer for the index.
    """
    ef_construction: Optional[int] = 64
    """
    The size of the dynamic candidate list for constructing the index graph.
    """
    metric: Optional[Literal["cosine", "l2", "inner"]] = "inner"
    """
    The distance metric to construct the index with.
    """


@dataclass
class DeleteVectorStoreParams:
    name: str
    """
    Vector store name.
    """
    model: Literal["jina-v2", "clip"]
    """
    Selected embedding model
    """


@dataclass
class Vector:
    """
    Canonical representation of document with embedding vector.
    """

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


@dataclass
class GetVectorsParams:
    name: str
    """
    Vector store name.
    """
    model: Literal["jina-v2", "clip"]
    """
    Selected embedding model
    """
    ids: List[str]
    """
    Document IDs to retrieve.
    """


@dataclass
class GetVectorsResponse:
    vectors: List[Vector]
    """
    Retrieved vectors.
    """


@dataclass
class VectorUpdateCountResponse:
    count: int
    """
    Number of vectors modified.
    """


@dataclass
class UpdateVectorParams:
    """
    Document to update.
    """

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


@dataclass
class UpdateVectorsParams:
    name: str
    """
    Vector store name.
    """
    model: Literal["jina-v2", "clip"]
    """
    Selected embedding model
    """
    vectors: List[UpdateVectorParams]
    """
    Vectors to upsert.
    """


@dataclass
class DeleteVectorsParams:
    name: str
    """
    Vector store name.
    """
    model: Literal["jina-v2", "clip"]
    """
    Selected embedding model
    """
    ids: List[str]
    """
    Document IDs to delete.
    """


@dataclass
class QueryVectorStoreParams:
    name: str
    """
    Vector store to query against.
    """
    model: Literal["jina-v2", "clip"]
    """
    Selected embedding model
    """
    query_ids: Optional[List[str]] = None
    """
    Document IDs to use for the query.
    """
    query_image_uris: Optional[List[str]] = None
    """
    Image URIs to embed and use for the query.
    """
    query_vectors: Optional[List[List[float]]] = None
    """
    Vector to use for the query.
    """
    query_strings: Optional[List[str]] = None
    """
    Texts to embed and use for the query.
    """
    top_k: Optional[int] = 10
    """
    Number of results to return.
    """
    ef_search: Optional[int] = 40
    """
    The size of the dynamic candidate list for searching the index graph.
    """
    include_values: Optional[bool] = False
    """
    Include the values of the vectors in the response.
    """
    include_metadata: Optional[bool] = False
    """
    Include the metadata of the vectors in the response.
    """
    filters: Optional[Dict[str, Any]] = None
    """
    Filter metadata by key-value pairs.
    """


@dataclass
class VectorStoreQueryResult:
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


@dataclass
class QueryVectorStoreResponse:
    results: List[List[VectorStoreQueryResult]]
    """
    Query results.
    """
    name: Optional[str] = None
    """
    Vector store name.
    """
    model: Optional[Literal["jina-v2", "clip"]] = None
    """
    Selected embedding model
    """
    metric: Optional[Literal["cosine", "l2", "inner"]] = None
    """
    The distance metric used for the query.
    """
