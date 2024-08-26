from typing import Any

from pypika.terms import (
    AnalyticFunction as AnalyticFunction,
    IgnoreNullsAnalyticFunction as IgnoreNullsAnalyticFunction,
    WindowFrameAnalyticFunction as WindowFrameAnalyticFunction, Field, Term,
)

class Preceding(WindowFrameAnalyticFunction.Edge):
    modifier: str

class Following(WindowFrameAnalyticFunction.Edge):
    modifier: str

CURRENT_ROW: str

class Rank(AnalyticFunction):
    def __init__(self, **kwargs: Any) -> None: ...

class DenseRank(AnalyticFunction):
    def __init__(self, **kwargs: Any) -> None: ...

class RowNumber(AnalyticFunction):
    def __init__(self, **kwargs: Any) -> None: ...

class NTile(AnalyticFunction):
    def __init__(self, term: str | Field | Term, **kwargs: Any) -> None: ...

class FirstValue(WindowFrameAnalyticFunction, IgnoreNullsAnalyticFunction):
    def __init__(self, *terms: str | Field | Term, **kwargs: Any) -> None: ...

class LastValue(WindowFrameAnalyticFunction, IgnoreNullsAnalyticFunction):
    def __init__(self, *terms: str | Field | Term, **kwargs: Any) -> None: ...

class Median(AnalyticFunction):
    def __init__(self, term: str | Field | Term, **kwargs: Any) -> None: ...

class Avg(WindowFrameAnalyticFunction):
    def __init__(self, term: str | Field | Term, **kwargs: Any) -> None: ...

class StdDev(WindowFrameAnalyticFunction):
    def __init__(self, term: str | Field | Term, **kwargs: Any) -> None: ...

class StdDevPop(WindowFrameAnalyticFunction):
    def __init__(self, term: str | Field | Term, **kwargs: Any) -> None: ...

class StdDevSamp(WindowFrameAnalyticFunction):
    def __init__(self, term: str | Field | Term, **kwargs: Any) -> None: ...

class Variance(WindowFrameAnalyticFunction):
    def __init__(self, term: str | Field | Term, **kwargs: Any) -> None: ...

class VarPop(WindowFrameAnalyticFunction):
    def __init__(self, term: str | Field | Term, **kwargs: Any) -> None: ...

class VarSamp(WindowFrameAnalyticFunction):
    def __init__(self, term: str | Field | Term, **kwargs: Any) -> None: ...

class Count(WindowFrameAnalyticFunction):
    def __init__(self, term: str | Field | Term, **kwargs: Any) -> None: ...

class Sum(WindowFrameAnalyticFunction):
    def __init__(self, term: str | Field | Term, **kwargs: Any) -> None: ...

class Max(WindowFrameAnalyticFunction):
    def __init__(self, term: str | Field | Term, **kwargs: Any) -> None: ...

class Min(WindowFrameAnalyticFunction):
    def __init__(self, term: str | Field | Term, **kwargs: Any) -> None: ...

class Lag(AnalyticFunction):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

class Lead(AnalyticFunction):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
