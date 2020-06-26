# -*- coding: utf-8 -*-

"""Implementations of various knowledge graph embedding models."""

from typing import Mapping, Set, Type, Union

from .base import EntityEmbeddingModel, EntityRelationEmbeddingModel, Model, MultimodalModel
from .multimodal import ComplExLiteral, DistMultLiteral
from .unimodal import (
    ComplEx,
    ConvE,
    ConvKB,
    DistMult,
    ERMLP,
    ERMLPE,
    HolE,
    KG2E,
    NTN,
    ProjE,
    RESCAL,
    RGCN,
    RotatE,
    SimplE,
    StructuredEmbedding,
    TransD,
    TransE,
    TransH,
    TransR,
    TuckER,
    UnstructuredModel,
)
from ..utils import get_cls, normalize_string

__all__ = [
    'ComplEx',
    'ComplExLiteral',
    'ConvE',
    'ConvKB',
    'DistMult',
    'DistMultLiteral',
    'ERMLP',
    'ERMLPE',
    'HolE',
    'KG2E',
    'NTN',
    'ProjE',
    'RESCAL',
    'RGCN',
    'RotatE',
    'SimplE',
    'StructuredEmbedding',
    'TransD',
    'TransE',
    'TransH',
    'TransR',
    'TuckER',
    'UnstructuredModel',
    'models',
    'get_model_cls',
]


def _recur(c):
    for sc in c.__subclasses__():
        yield sc
        yield from _recur(sc)


_MODELS: Set[Type[Model]] = {
    cls
    for cls in _recur(Model)
    if cls not in {Model, MultimodalModel, EntityRelationEmbeddingModel, EntityEmbeddingModel}
}

#: A mapping of models' names to their implementations
models: Mapping[str, Type[Model]] = {
    normalize_string(cls.__name__): cls
    for cls in _MODELS
}


def get_model_cls(query: Union[str, Type[Model]]) -> Type[Model]:
    """Look up a model class by name (case/punctuation insensitive) in :data:`pykeen.models.models`.

    :param query: The name of the model (case insensitive, punctuation insensitive).
    :return: The model class
    """
    return get_cls(
        query,
        base=Model,
        lookup_dict=models,
    )
