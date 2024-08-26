import abc
from _typeshed import Incomplete
from csv import Dialect
from typing import Any

from pypika.terms import Field as Field, Function as Function, Term as Term
from pypika.utils import format_alias_sql as format_alias_sql

class Array(Term):
    def __init__(
        self,
        values: list,
        converter_cls: Incomplete | None = None,
        converter_options: dict | None = None,
        alias: str | None = None,
    ) -> None: ...
    def get_sql(self) -> str: ...

class HasAny(Function):
    alias: str | None
    schema: str | None
    args: tuple[Any, ...]
    name: str
    def __init__(
        self,
        left_array: Array | Field,
        right_array: Array | Field,
        alias: str | None = None,
        schema: str | None = None,
    ) -> None: ...
    def get_sql(
        self,
        with_alias: bool = False,
        with_namespace: bool = False,
        quote_char: Incomplete | None = None,
        dialect: Incomplete | None = None,
        **kwargs: Any,
    ) -> str: ...

class _AbstractArrayFunction(Function, metaclass=abc.ABCMeta):
    schema: str | None
    alias: str | None
    name: str
    def __init__(
        self, array: Array | Field, alias: str | None = None, schema: str | None = None
    ) -> None: ...
    def get_sql(
        self,
        with_namespace: bool = False,
        quote_char: str | None = None,
        dialect: Dialect | None = None,
        **kwargs: Any,
    ) -> str: ...
    @classmethod
    @abc.abstractmethod
    def clickhouse_function(cls) -> str: ...

class NotEmpty(_AbstractArrayFunction):
    @classmethod
    def clickhouse_function(cls) -> str: ...

class Empty(_AbstractArrayFunction):
    @classmethod
    def clickhouse_function(cls) -> str: ...

class Length(_AbstractArrayFunction):
    @classmethod
    def clickhouse_function(cls) -> str: ...
