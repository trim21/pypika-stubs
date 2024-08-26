from _typeshed import Incomplete
from typing import Any

from pypika.terms import Field as Field, Function as Function
from pypika.utils import format_alias_sql as format_alias_sql

class ToString(Function):
    def __init__(self, name: str | Field, alias: str | None = None) -> None: ...

class ToFixedString(Function):
    alias: str | None
    name: str
    schema: str | None
    args: tuple[Any, ...]
    def __init__(
        self,
        field: str | Field,
        length: int,
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

class ToInt8(Function):
    def __init__(self, name: str | Field, alias: str | None = None) -> None: ...

class ToInt16(Function):
    def __init__(self, name: str | Field, alias: str | None = None) -> None: ...

class ToInt32(Function):
    def __init__(self, name: str | Field, alias: str | None = None) -> None: ...

class ToInt64(Function):
    def __init__(self, name: str | Field, alias: str | None = None) -> None: ...

class ToUInt8(Function):
    def __init__(self, name: str | Field, alias: str | None = None) -> None: ...

class ToUInt16(Function):
    def __init__(self, name: str | Field, alias: str | None = None) -> None: ...

class ToUInt32(Function):
    def __init__(self, name: str | Field, alias: str | None = None) -> None: ...

class ToUInt64(Function):
    def __init__(self, name: str | Field, alias: str | None = None) -> None: ...

class ToFloat32(Function):
    def __init__(self, name: str | Field, alias: str | None = None) -> None: ...

class ToFloat64(Function):
    def __init__(self, name: str | Field, alias: str | None = None) -> None: ...

class ToDate(Function):
    def __init__(self, name: str | Field, alias: str | None = None) -> None: ...

class ToDateTime(Function):
    def __init__(self, name: str | Field, alias: str | None = None) -> None: ...
