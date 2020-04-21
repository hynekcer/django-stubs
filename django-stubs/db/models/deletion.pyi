from typing import Any, Callable, Iterable, Optional, Union, Collection, Type

from django.db.models.base import Model

from django.db import IntegrityError
from django.db.models.fields import Field
from django.db.models.options import Options
from django.db.models.query import QuerySet

def CASCADE(collector: Collector, field: Field, sub_objs: QuerySet, using: str) -> None: ...
def SET_NULL(collector: Collector, field: Field, sub_objs: QuerySet, using: str) -> None: ...
def SET_DEFAULT(collector: Collector, field: Field, sub_objs: QuerySet, using: str) -> None: ...
def DO_NOTHING(collector: Collector, field: Field, sub_objs: QuerySet, using: str) -> None: ...
def PROTECT(collector: Collector, field: Field, sub_objs: QuerySet, using: str) -> None: ...
def SET(value: Any) -> Callable[[Collector, Field, QuerySet, str], None]: ...
def get_candidate_relations_to_delete(opts: Options) -> Iterable[Field]: ...

class ProtectedError(IntegrityError): ...

class Collector:
    def __init__(self, using: str) -> None: ...
    def collect(
        self,
        objs: Collection[Optional[Model]],
        source: Optional[Type[Model]] = ...,
        source_attr: Optional[str] = ...,
        **kwargs: Any
    ) -> None: ...
    def can_fast_delete(self, objs: Union[Model, Iterable[Model]], from_field: Optional[Field] = ...) -> bool: ...
