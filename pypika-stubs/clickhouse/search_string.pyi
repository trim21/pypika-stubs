import abc
from _typeshed import Incomplete
from typing import Any

from pypika.terms import Function as Function, Field
from pypika.utils import format_alias_sql as format_alias_sql

class _AbstractSearchString(Function, metaclass=abc.ABCMeta):
    def __init__(
        self, name: str | Field, pattern: str, alias: str | None = None
    ) -> None: ...
    @classmethod
    @abc.abstractmethod
    def clickhouse_function(cls) -> str: ...
    def get_sql(
        self,
        with_alias: bool = False,
        with_namespace: bool = False,
        quote_char: Incomplete | None = None,
        dialect: Incomplete | None = None,
        **kwargs: Any,
    ) -> str: ...

class Match(_AbstractSearchString):
    @classmethod
    def clickhouse_function(cls) -> str: ...

class Like(_AbstractSearchString):
    @classmethod
    def clickhouse_function(cls) -> str: ...

class NotLike(_AbstractSearchString):
    @classmethod
    def clickhouse_function(cls) -> str: ...

class _AbstractMultiSearchString(Function, metaclass=abc.ABCMeta):
    def __init__(
        self, name: str | Field, patterns: list, alias: str | None = None
    ) -> None: ...
    @classmethod
    @abc.abstractmethod
    def clickhouse_function(cls) -> str: ...
    def get_sql(
        self,
        with_alias: bool = False,
        with_namespace: bool = False,
        quote_char: Incomplete | None = None,
        dialect: Incomplete | None = None,
        **kwargs: Any,
    ) -> str: ...

class MultiSearchAny(_AbstractMultiSearchString):
    @classmethod
    def clickhouse_function(cls) -> str: ...

class MultiMatchAny(_AbstractMultiSearchString):
    @classmethod
    def clickhouse_function(cls) -> str: ...
