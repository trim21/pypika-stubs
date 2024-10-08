from _typeshed import Incomplete
from typing import Any

from pypika import Field as Field
from pypika.enums import SqlTypes as SqlTypes
from pypika.terms import (
    AggregateFunction as AggregateFunction,
    Function as Function,
    LiteralValue as LiteralValue,
    Star as Star,
    Term,
)
from pypika.utils import builder as builder

class DistinctOptionFunction(AggregateFunction):
    def __init__(self, name: str, *args: Any, **kwargs: Any) -> None: ...
    def get_function_sql(self, **kwargs: Any) -> str: ...
    def distinct(self) -> None: ...

class Count(DistinctOptionFunction):
    def __init__(self, param: str | Field, alias: str | None = None) -> None: ...

class Sum(DistinctOptionFunction):
    def __init__(self, term: str | Field | Term, alias: str | None = None) -> None: ...

class Avg(AggregateFunction):
    def __init__(self, term: str | Field | Term, alias: str | None = None) -> None: ...

class Min(AggregateFunction):
    def __init__(self, term: str | Field | Term, alias: str | None = None) -> None: ...

class Max(AggregateFunction):
    def __init__(self, term: str | Field | Term, alias: str | None = None) -> None: ...

class Std(AggregateFunction):
    def __init__(self, term: str | Field | Term, alias: str | None = None) -> None: ...

class StdDev(AggregateFunction):
    def __init__(self, term: str | Field | Term, alias: str | None = None) -> None: ...

class Abs(AggregateFunction):
    def __init__(self, term: str | Field | Term, alias: str | None = None) -> None: ...

class First(AggregateFunction):
    def __init__(self, term: str | Field | Term, alias: str | None = None) -> None: ...

class Last(AggregateFunction):
    def __init__(self, term: str | Field | Term, alias: str | None = None) -> None: ...

class Sqrt(Function):
    def __init__(self, term: str | Field | Term, alias: str | None = None) -> None: ...

class Floor(Function):
    def __init__(self, term: str | Field | Term, alias: str | None = None) -> None: ...

class ApproximatePercentile(AggregateFunction):
    percentile: float
    def __init__(
        self, term: str | Field | Term, percentile: float, alias: str | None = None
    ) -> None: ...
    def get_special_params_sql(self, **kwargs: Any) -> str: ...

class Cast(Function):
    as_type: str
    def __init__(
        self, term: str | Field | Term, as_type: str, alias: str | None = None
    ) -> None: ...
    def get_special_params_sql(self, **kwargs: Any) -> str: ...

class Convert(Function):
    encoding: str
    def __init__(
        self, term: str | Field | Term, encoding: str, alias: str | None = None
    ) -> None: ...
    def get_special_params_sql(self, **kwargs: Any) -> str: ...

class ToChar(Function):
    def __init__(
        self, term: str | Field | Term, as_type: str, alias: str | None = None
    ) -> None: ...

class Signed(Cast):
    def __init__(self, term: str | Field, alias: str | None = None) -> None: ...

class Unsigned(Cast):
    def __init__(self, term: str | Field, alias: str | None = None) -> None: ...

class Date(Function):
    def __init__(self, term: str | Field, alias: str | None = None) -> None: ...

class DateDiff(Function):
    def __init__(
        self,
        interval: float,
        start_date: Incomplete,
        end_date: Incomplete,
        alias: str | None = None,
    ) -> None: ...

class TimeDiff(Function):
    def __init__(
        self, start_time: Incomplete, end_time: Incomplete, alias: str | None = None
    ) -> None: ...

class DateAdd(Function):
    def __init__(
        self,
        date_part: Incomplete,
        interval: Incomplete,
        term: str,
        alias: str | None = None,
    ) -> None: ...

class ToDate(Function):
    def __init__(
        self, value: Incomplete, format_mask: Incomplete, alias: str | None = None
    ) -> None: ...

class Timestamp(Function):
    def __init__(self, term: str | Field, alias: str | None = None) -> None: ...

class TimestampAdd(Function):
    def __init__(
        self,
        date_part: Incomplete,
        interval: Incomplete,
        term: str,
        alias: str | None = None,
    ) -> None: ...

class Ascii(Function):
    def __init__(self, term: str | Field, alias: str | None = None) -> None: ...

class NullIf(Function):
    def __init__(
        self, term: str | Field | Term, condition: Incomplete, **kwargs: Any
    ) -> None: ...

class Bin(Function):
    def __init__(self, term: str | Field, alias: str | None = None) -> None: ...

class Concat(Function):
    def __init__(self, *terms: str | Field | Term, **kwargs: Any) -> None: ...

class Insert(Function):
    def __init__(
        self,
        term: str | Field | Term,
        start: int,
        stop: int,
        subterm: str,
        alias: str | None = None,
    ) -> None: ...

class Length(Function):
    def __init__(self, term: str | Field, alias: str | None = None) -> None: ...

class Upper(Function):
    def __init__(self, term: str | Field, alias: str | None = None) -> None: ...

class Lower(Function):
    def __init__(self, term: str | Field, alias: str | None = None) -> None: ...

class Substring(Function):
    def __init__(
        self, term: str | Field | Term, start: int, stop: int, alias: str | None = None
    ) -> None: ...

class Reverse(Function):
    def __init__(self, term: str | Field | Term, alias: str | None = None) -> None: ...

class Trim(Function):
    def __init__(self, term: str | Field | Term, alias: str | None = None) -> None: ...

class SplitPart(Function):
    def __init__(
        self,
        term: str | Field | Term,
        delimiter: Incomplete,
        index: Incomplete,
        alias: str | None = None,
    ) -> None: ...

class RegexpMatches(Function):
    def __init__(
        self,
        term: str | Field | Term,
        pattern: Incomplete,
        modifiers: Incomplete | None = None,
        alias: str | None = None,
    ) -> None: ...

class RegexpLike(Function):
    def __init__(
        self,
        term: str | Field | Term,
        pattern: Incomplete,
        modifiers: Incomplete | None = None,
        alias: str | None = None,
    ) -> None: ...

class Replace(Function):
    def __init__(
        self,
        term: str | Field | Term,
        find_string: str,
        replace_with: str,
        alias: str | None = None,
    ) -> None: ...

class Now(Function):
    def __init__(self, alias: str | None = None) -> None: ...

class UtcTimestamp(Function):
    def __init__(self, alias: str | None = None) -> None: ...

class CurTimestamp(Function):
    def __init__(self, alias: str | None = None) -> None: ...
    def get_function_sql(self, **kwargs: Any) -> str: ...

class CurDate(Function):
    def __init__(self, alias: str | None = None) -> None: ...

class CurTime(Function):
    def __init__(self, alias: str | None = None) -> None: ...

class Extract(Function):
    field: Field
    def __init__(
        self, date_part: str, field: Field, alias: str | None = None
    ) -> None: ...
    def get_special_params_sql(self, **kwargs: Any) -> str: ...

class IsNull(Function):
    def __init__(self, term: str | Field, alias: str | None = None) -> None: ...

class Coalesce(Function):
    def __init__(
        self, term: str | Field | Term, *default_values: Any, **kwargs: Any
    ) -> None: ...

class IfNull(Function):
    def __init__(
        self, condition: str, term: str | Field | Term, **kwargs: Any
    ) -> None: ...

class NVL(Function):
    def __init__(self, condition: str, term: str, alias: str | None = None) -> None: ...
