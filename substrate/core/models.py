"""
꩜ Substrate
@generated file
(using datamodel-codegen)
"""


from __future__ import annotations

from typing import Any, Dict, List, Optional
from typing_extensions import Literal, Annotated

from pydantic import Extra, Field, BaseModel


class ErrorOut(BaseModel):
    class Config:
        extra = Extra.allow

    type: Literal["api_error", "invalid_request_error"]
    """
    The type of error returned.
    """
    message: str
    """
    A message providing more details about the error.
    """


class ResponseFormat(BaseModel):
    class Config:
        extra = Extra.allow

    type: Literal["json_object", "text"]
    """
    Type of response.
    """
    json_schema: Optional[Dict[str, Any]] = None
    """
    JSON schema to guide `json_object` response.
    """


class GenerateTextIn(BaseModel):
    class Config:
        extra = Extra.allow

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
    temperature: Annotated[Optional[int], Field(ge=1, le=10)] = 4
    """
    Sampling temperature to use. Higher values make the output more random, lower values make the output more deterministic.
    """
    max_tokens: Optional[int] = 800
    """
    Maximum number of tokens to generate.
    """


class MultiGenerateTextIn(BaseModel):
    class Config:
        extra = Extra.allow

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
    temperature: Annotated[Optional[int], Field(ge=1, le=10)] = 4
    """
    Sampling temperature to use. Higher values make the output more random, lower values make the output more deterministic.
    """
    max_tokens: Optional[int] = 800
    """
    Maximum number of tokens to generate.
    """


class GenerateTextOut(BaseModel):
    class Config:
        extra = Extra.allow

    text: Optional[str] = None
    """
    Text response.
    """
    json_object: Optional[Dict[str, Any]] = None
    """
    JSON response.
    """


class MultiGenerateTextOut(BaseModel):
    class Config:
        extra = Extra.allow

    choices: List[GenerateTextOut]


class GenerateTextVisionIn(BaseModel):
    class Config:
        extra = Extra.allow

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
    temperature: Annotated[Optional[int], Field(ge=1, le=10)] = 4
    """
    Sampling temperature to use. Higher values make the output more random, lower values make the output more deterministic.
    """
    max_tokens: Optional[int] = 800
    """
    Maximum number of tokens to generate.
    """


class GenerateTextVisionOut(BaseModel):
    class Config:
        extra = Extra.allow

    text: str
    """
    Text response.
    """


class GenerateImageIn(BaseModel):
    class Config:
        extra = Extra.allow

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
    image_influence: Annotated[Optional[float], Field(ge=0.0, le=10.0)] = 5
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


class GenerateImageOut(BaseModel):
    class Config:
        extra = Extra.allow

    image_uri: str
    """
    Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """
    seed: int
    """
    The random noise seed used for generation.
    """


class MultiGenerateImageIn(BaseModel):
    class Config:
        extra = Extra.allow

    prompt: str
    """
    Text prompt.
    """
    image_prompt_uri: Optional[str] = None
    """
    Image prompt.
    """
    num_images: int
    """
    Number of images to generate.
    """
    model: Optional[Literal["stablediffusion-xl"]] = "stablediffusion-xl"
    """
    Selected model.
    """
    image_influence: Annotated[Optional[float], Field(ge=0.0, le=10.0)] = 5
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


class MultiGenerateImageOut(BaseModel):
    class Config:
        extra = Extra.allow

    outputs: List[GenerateImageOut]


class ControlledGenerateImageIn(BaseModel):
    class Config:
        extra = Extra.allow

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
    image_influence: Annotated[Optional[float], Field(ge=0.0, le=10.0)] = 9
    """
    Controls the influence of the input image on the generated output.
    """
    seed: Optional[int] = None
    """
    Seed for deterministic generation. Default is a random seed.
    """


class ControlledGenerateImageOut(BaseModel):
    class Config:
        extra = Extra.allow

    image_uri: str
    """
    Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """
    seed: int
    """
    The random noise seed used for generation.
    """


class MultiControlledGenerateImageIn(BaseModel):
    class Config:
        extra = Extra.allow

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
    image_influence: Annotated[Optional[float], Field(ge=0.0, le=10.0)] = 9
    """
    Controls the influence of the input image on the generated output.
    """
    seeds: Optional[List[int]] = None
    """
    Random noise seeds. Default is random seeds for each generation.
    """


class MultiControlledGenerateImageOut(BaseModel):
    class Config:
        extra = Extra.allow

    outputs: List[ControlledGenerateImageOut]


class GenerativeEditImageIn(BaseModel):
    class Config:
        extra = Extra.allow

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
    strength: Annotated[Optional[float], Field(ge=0.0, le=10.0)] = 8
    """
    Controls the strength of the generation process.
    """
    image_prompt_influence: Annotated[Optional[float], Field(ge=0.0, le=10.0)] = 5
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


class GenerativeEditImageOut(BaseModel):
    class Config:
        extra = Extra.allow

    image_uri: str
    """
    Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """
    seed: int
    """
    The random noise seed used for generation.
    """


class MultiGenerativeEditImageIn(BaseModel):
    class Config:
        extra = Extra.allow

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
    Mask image that controls which pixels are edited (inpainting). If unset, the entire image is edited (image-to-image).
    """
    image_prompt_uri: Optional[str] = None
    """
    Image prompt.
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
    strength: Annotated[Optional[float], Field(ge=0.0, le=10.0)] = 8
    """
    Controls the strength of the generation process.
    """
    image_prompt_influence: Annotated[Optional[float], Field(ge=0.0, le=10.0)] = 5
    """
    Controls the influence of the image prompt on the generated output.
    """
    seeds: Optional[List[int]] = None
    """
    Random noise seeds. Default is random seeds for each generation.
    """


class MultiGenerativeEditImageOut(BaseModel):
    class Config:
        extra = Extra.allow

    outputs: List[GenerativeEditImageOut]


class BoundingBox(BaseModel):
    class Config:
        extra = Extra.allow

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


class Point(BaseModel):
    class Config:
        extra = Extra.allow

    x: int
    """
    X position.
    """
    y: int
    """
    Y position.
    """


class FillMaskIn(BaseModel):
    class Config:
        extra = Extra.allow

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


class FillMaskOut(BaseModel):
    class Config:
        extra = Extra.allow

    image_uri: str
    """
    Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """


class RemoveBackgroundIn(BaseModel):
    class Config:
        extra = Extra.allow

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


class RemoveBackgroundOut(BaseModel):
    class Config:
        extra = Extra.allow

    image_uri: str
    """
    Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """


class UpscaleImageIn(BaseModel):
    class Config:
        extra = Extra.allow

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


class UpscaleImageOut(BaseModel):
    class Config:
        extra = Extra.allow

    image_uri: str
    """
    Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """


class DetectSegmentsIn(BaseModel):
    class Config:
        extra = Extra.allow

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


class DetectSegmentsOut(BaseModel):
    class Config:
        extra = Extra.allow

    mask_image_uri: str
    """
    Detected segments in 'mask image' format. Base 64-encoded JPEG image bytes, or a hosted image url if `store` is provided.
    """


class TranscribeMediaIn(BaseModel):
    class Config:
        extra = Extra.allow

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


class TranscribedWord(BaseModel):
    class Config:
        extra = Extra.allow

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


class TranscribedSegment(BaseModel):
    class Config:
        extra = Extra.allow

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


class ChapterMarker(BaseModel):
    class Config:
        extra = Extra.allow

    title: str
    """
    Chapter title.
    """
    start: float
    """
    Start time of chapter, in seconds.
    """


class TranscribeMediaOut(BaseModel):
    class Config:
        extra = Extra.allow

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


class GenerateSpeechIn(BaseModel):
    class Config:
        extra = Extra.allow

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


class GenerateSpeechOut(BaseModel):
    class Config:
        extra = Extra.allow

    audio_uri: str
    """
    Base 64-encoded WAV audio bytes, or a hosted audio url if `store` is provided.
    """


class Embedding(BaseModel):
    class Config:
        extra = Extra.allow

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


class EmbedTextIn(BaseModel):
    class Config:
        extra = Extra.allow

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


class EmbedTextOut(BaseModel):
    class Config:
        extra = Extra.allow

    embedding: Embedding
    """
    Generated embedding.
    """


class EmbedTextItem(BaseModel):
    class Config:
        extra = Extra.allow

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


class MultiEmbedTextIn(BaseModel):
    class Config:
        extra = Extra.allow

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


class MultiEmbedTextOut(BaseModel):
    class Config:
        extra = Extra.allow

    embeddings: List[Embedding]
    """
    Generated embeddings.
    """


class EmbedImageIn(BaseModel):
    class Config:
        extra = Extra.allow

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


class EmbedImageOut(BaseModel):
    class Config:
        extra = Extra.allow

    embedding: Embedding
    """
    Generated embedding.
    """


class EmbedImageItem(BaseModel):
    class Config:
        extra = Extra.allow

    image_uri: str
    """
    Image to embed.
    """
    document_id: Optional[str] = None
    """
    Vector store document ID. Ignored if `store` is unset.
    """


class MultiEmbedImageIn(BaseModel):
    class Config:
        extra = Extra.allow

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


class MultiEmbedImageOut(BaseModel):
    class Config:
        extra = Extra.allow

    embeddings: List[Embedding]
    """
    Generated embeddings.
    """


class VectorStoreParams(BaseModel):
    """
    Fields describing a vector store and its associated index.
    """

    class Config:
        extra = Extra.allow

    name: Annotated[str, Field(max_length=63, min_length=1)]
    """
    Vector store name.
    """
    model: Literal["jina-v2", "clip"]
    """
    Selected embedding model
    """
    m: Annotated[Optional[int], Field(ge=1, le=64)] = 16
    """
    The max number of connections per layer for the index.
    """
    ef_construction: Annotated[Optional[int], Field(ge=1, le=128)] = 64
    """
    The size of the dynamic candidate list for constructing the index graph.
    """
    metric: Optional[Literal["cosine", "l2", "inner"]] = "inner"
    """
    The distance metric to construct the index with.
    """


class DeleteVectorStoreParams(BaseModel):
    class Config:
        extra = Extra.allow

    name: str
    """
    Vector store name.
    """
    model: Literal["jina-v2", "clip"]
    """
    Selected embedding model
    """


class Vector(BaseModel):
    """
    Canonical representation of document with embedding vector.
    """

    class Config:
        extra = Extra.allow

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


class GetVectorsParams(BaseModel):
    class Config:
        extra = Extra.allow

    name: str
    """
    Vector store name.
    """
    model: Literal["jina-v2", "clip"]
    """
    Selected embedding model
    """
    ids: Annotated[List[str], Field(max_items=100)]
    """
    Document IDs to retrieve.
    """


class GetVectorsResponse(BaseModel):
    class Config:
        extra = Extra.allow

    vectors: List[Vector]
    """
    Retrieved vectors.
    """


class VectorUpdateCountResponse(BaseModel):
    class Config:
        extra = Extra.allow

    count: int
    """
    Number of vectors modified.
    """


class UpdateVectorParams(BaseModel):
    """
    Document to update.
    """

    class Config:
        extra = Extra.allow

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


class UpdateVectorsParams(BaseModel):
    class Config:
        extra = Extra.allow

    name: str
    """
    Vector store name.
    """
    model: Literal["jina-v2", "clip"]
    """
    Selected embedding model
    """
    vectors: Annotated[List[UpdateVectorParams], Field(max_items=100)]
    """
    Vectors to upsert.
    """


class DeleteVectorsParams(BaseModel):
    class Config:
        extra = Extra.allow

    name: str
    """
    Vector store name.
    """
    model: Literal["jina-v2", "clip"]
    """
    Selected embedding model
    """
    ids: Annotated[List[str], Field(max_items=100)]
    """
    Document IDs to delete.
    """


class QueryVectorStoreParams(BaseModel):
    class Config:
        extra = Extra.allow

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
    top_k: Annotated[Optional[int], Field(ge=1, le=1000)] = 10
    """
    Number of results to return.
    """
    ef_search: Annotated[Optional[int], Field(ge=1, le=1000)] = 40
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


class VectorStoreQueryResult(BaseModel):
    class Config:
        extra = Extra.allow

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


class QueryVectorStoreResponse(BaseModel):
    class Config:
        extra = Extra.allow

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
