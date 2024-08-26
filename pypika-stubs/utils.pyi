from typing import Any, Callable, TypeVar

class QueryException(Exception): ...
class GroupingException(Exception): ...
class CaseException(Exception): ...
class JoinException(Exception): ...
class SetOperationException(Exception): ...
class RollupException(Exception): ...
class DialectNotSupported(Exception): ...
class FunctionException(Exception): ...

C = TypeVar("C")

def builder(func: C) -> C: ...
def ignore_copy(func: Callable) -> Callable: ...
def resolve_is_aggregate(values: list[bool | None]) -> bool | None: ...
def format_quotes(value: Any, quote_char: str | None) -> str: ...
def format_alias_sql(
    sql: str,
    alias: str | None,
    quote_char: str | None = None,
    alias_quote_char: str | None = None,
    as_keyword: bool = False,
    **kwargs: Any,
) -> str: ...
def validate(
    *args: Any, exc: Exception | None = None, type: type | None = None
) -> None: ...
