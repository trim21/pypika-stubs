import re
from pypika.enums import (
    Arithmetic as Arithmetic,
    Boolean as Boolean,
    Comparator as Comparator,
    Dialects as Dialects,
    Equality as Equality,
    JSONOperators as JSONOperators,
    Matching as Matching,
    Order as Order,
)
from pypika.queries import QueryBuilder as QueryBuilder, Selectable as Selectable, Table as Table, Schema
from pypika.utils import (
    CaseException as CaseException,
    FunctionException as FunctionException,
    builder as builder,
    format_alias_sql as format_alias_sql,
    format_quotes as format_quotes,
    ignore_copy as ignore_copy,
    resolve_is_aggregate as resolve_is_aggregate,
)
from typing import Any, Iterable, Iterator, Sequence, TypeVar, ClassVar

NodeT = TypeVar('NodeT', bound='Node')

class Node:
    is_aggregate: bool | Node

    def nodes_(self) -> Iterator[NodeT]: ...
    def find_(self, type: type[NodeT]) -> list[NodeT]: ...

class Term(Node):
    is_aggregate: bool
    alias: str | Node

    def __init__(self, alias: str | None = None) -> None: ...
    def as_(self, alias: str) -> Term: ...
    @property
    def tables_(self) -> set[Table]: ...
    def fields_(self) -> set[Field]: ...
    @staticmethod
    def wrap_constant(
            val: Any, wrapper_cls: type['Term'] | None = None
    ) -> ValueError | NodeT | LiteralValue | Array | Tuple | ValueWrapper: ...
    @staticmethod
    def wrap_json(
            val: Term | QueryBuilder | Interval | None | str | int | bool,
            wrapper_cls: type[Term] | None = None,
    ) -> Term | QueryBuilder | Interval | NullValue | ValueWrapper | JSON: ...
    def replace_table(self, current_table: Table | None, new_table: Table | None) -> Term: ...
    def eq(self, other: Any) -> BasicCriterion: ...
    def isnull(self) -> NullCriterion: ...
    def notnull(self) -> Not: ...
    def isnotnull(self) -> NotNullCriterion: ...
    def bitwiseand(self, value: int) -> BitwiseAndCriterion: ...
    def gt(self, other: Any) -> BasicCriterion: ...
    def gte(self, other: Any) -> BasicCriterion: ...
    def lt(self, other: Any) -> BasicCriterion: ...
    def lte(self, other: Any) -> BasicCriterion: ...
    def ne(self, other: Any) -> BasicCriterion: ...
    def glob(self, expr: str) -> BasicCriterion: ...
    def like(self, expr: str) -> BasicCriterion: ...
    def not_like(self, expr: str) -> BasicCriterion: ...
    def ilike(self, expr: str) -> BasicCriterion: ...
    def not_ilike(self, expr: str) -> BasicCriterion: ...
    def rlike(self, expr: str) -> BasicCriterion: ...
    def regex(self, pattern: str) -> BasicCriterion: ...
    def regexp(self, pattern: str) -> BasicCriterion: ...
    def between(self, lower: Any, upper: Any) -> BetweenCriterion: ...
    def from_to(self, start: Any, end: Any) -> PeriodCriterion: ...
    def as_of(self, expr: str) -> BasicCriterion: ...
    def all_(self) -> All: ...
    def isin(self, arg: list | tuple | set | frozenset | Term) -> ContainsCriterion: ...
    def notin(self, arg: list | tuple | set | frozenset | Term) -> ContainsCriterion: ...
    def bin_regex(self, pattern: str) -> BasicCriterion: ...
    def negate(self) -> Not: ...
    def lshift(self, other: Any) -> ArithmeticExpression: ...
    def rshift(self, other: Any) -> ArithmeticExpression: ...
    def __invert__(self) -> Not: ...
    def __pos__(self) -> Term: ...
    def __neg__(self) -> Negative: ...
    def __add__(self, other: Any) -> ArithmeticExpression: ...
    def __sub__(self, other: Any) -> ArithmeticExpression: ...
    def __mul__(self, other: Any) -> ArithmeticExpression: ...
    def __truediv__(self, other: Any) -> ArithmeticExpression: ...
    def __pow__(self, other: Any) -> Pow: ...
    def __mod__(self, other: Any) -> Mod: ...
    def __radd__(self, other: Any) -> ArithmeticExpression: ...
    def __rsub__(self, other: Any) -> ArithmeticExpression: ...
    def __rmul__(self, other: Any) -> ArithmeticExpression: ...
    def __rtruediv__(self, other: Any) -> ArithmeticExpression: ...
    def __lshift__(self, other: Any) -> ArithmeticExpression: ...
    def __rshift__(self, other: Any) -> ArithmeticExpression: ...
    def __rlshift__(self, other: Any) -> ArithmeticExpression: ...
    def __rrshift__(self, other: Any) -> ArithmeticExpression: ...
    def __eq__(self, other: Any) -> BasicCriterion: ...
    def __ne__(self, other: Any) -> BasicCriterion: ...
    def __gt__(self, other: Any) -> BasicCriterion: ...
    def __ge__(self, other: Any) -> BasicCriterion: ...
    def __lt__(self, other: Any) -> BasicCriterion: ...
    def __le__(self, other: Any) -> BasicCriterion: ...
    def __getitem__(self, item: slice) -> BetweenCriterion: ...
    def __hash__(self) -> int: ...
    def get_sql(self, **kwargs: Any) -> str: ...

class Parameter(Term):
    is_aggregate: bool
    placeholder: str | int

    def __init__(self, placeholder: str | int) -> None: ...
    def get_sql(self, **kwargs: Any) -> str: ...

class QmarkParameter(Parameter):
    def __init__(self) -> None: ...
    def get_sql(self, **kwargs: Any) -> str: ...

class NumericParameter(Parameter):
    def get_sql(self, **kwargs: Any) -> str: ...

class NamedParameter(Parameter):
    def get_sql(self, **kwargs: Any) -> str: ...

class FormatParameter(Parameter):
    def __init__(self) -> None: ...
    def get_sql(self, **kwargs: Any) -> str: ...

class PyformatParameter(Parameter):
    def get_sql(self, **kwargs: Any) -> str: ...

class Negative(Term):
    term: Term

    def __init__(self, term: Term) -> None: ...
    @property
    def is_aggregate(self) -> bool | None: ...
    def get_sql(self, **kwargs: Any) -> str: ...

class ValueWrapper(Term):
    is_aggregate: bool
    value: Any

    def __init__(self, value: Any, alias: str | None = None) -> None: ...
    def get_value_sql(self, **kwargs: Any) -> str: ...
    @classmethod
    def get_formatted_value(cls, value: Any, **kwargs: Any) -> str: ...
    def get_sql(self, quote_char: str | None = None, secondary_quote_char: str = "'", **kwargs: Any) -> str: ...

class JSON(Term):
    table: str | None
    value: Any

    def __init__(self, value: Any = None, alias: str | None = None) -> None: ...
    def get_sql(self, secondary_quote_char: str = "'", **kwargs: Any) -> str: ...
    def get_json_value(self, key_or_index: str | int) -> BasicCriterion: ...
    def get_text_value(self, key_or_index: str | int) -> BasicCriterion: ...
    def get_path_json_value(self, path_json: str) -> BasicCriterion: ...
    def get_path_text_value(self, path_json: str) -> BasicCriterion: ...
    def has_key(self, other: Any) -> BasicCriterion: ...
    def contains(self, other: Any) -> BasicCriterion: ...
    def contained_by(self, other: Any) -> BasicCriterion: ...
    def has_keys(self, other: Iterable) -> BasicCriterion: ...
    def has_any_keys(self, other: Iterable) -> BasicCriterion: ...

class Values(Term):
    field: Field

    def __init__(self, field: str | Field) -> None: ...
    def get_sql(self, quote_char: str | None = None, **kwargs: Any) -> str: ...

class LiteralValue(Term):
    def __init__(self, value: Any, alias: str | None = None) -> None: ...
    def get_sql(self, **kwargs: Any) -> str: ...

class NullValue(LiteralValue):
    def __init__(self, alias: str | None = None) -> None: ...

class SystemTimeValue(LiteralValue):
    def __init__(self, alias: str | None = None) -> None: ...

class Criterion(Term):
    def __and__(self, other: Any) -> ComplexCriterion: ...
    def __or__(self, other: Any) -> ComplexCriterion: ...
    def __xor__(self, other: Any) -> ComplexCriterion: ...
    @staticmethod
    def any(terms: Iterable[Term] = ()) -> EmptyCriterion: ...
    @staticmethod
    def all(terms: Iterable[Any] = ()) -> EmptyCriterion: ...
    def get_sql(self) -> str: ...

class EmptyCriterion(Criterion):
    is_aggregate: bool
    tables_: ClassVar[set[Any]]

    def fields_(self) -> set['Field']: ...
    def __and__(self, other: Any) -> Any: ...
    def __or__(self, other: Any) -> Any: ...
    def __xor__(self, other: Any) -> Any: ...
    def __invert__(self) -> Any: ...

class Field(Criterion, JSON):
    name: str
    table: Table | Selectable

    def __init__(self, name: str, alias: str | None = None, table: str | Selectable | None = None) -> None: ...
    def nodes_(self) -> Iterator[NodeT]: ...
    def replace_table(self, current_table: Table | None, new_table: Table | None) -> Field: ...
    def get_sql(self, **kwargs: Any) -> str: ...

class Index(Term):
    name: str

    def __init__(self, name: str, alias: str | None = None) -> None: ...
    def get_sql(self, quote_char: str | None = None, **kwargs: Any) -> str: ...

class Star(Field):
    def __init__(self, table: str | Selectable | None = None) -> None: ...
    def nodes_(self) -> Iterator[NodeT]: ...
    def get_sql(
            self, with_alias: bool = False, with_namespace: bool = False, quote_char: str | None = None, **kwargs: Any
    ) -> str: ...

class Tuple(Criterion):
    values: list[Any]

    def __init__(self, *values: Any) -> None: ...
    def nodes_(self) -> Iterator[NodeT]: ...
    def get_sql(self, **kwargs: Any) -> str: ...
    @property
    def is_aggregate(self) -> bool: ...
    def replace_table(self, current_table: Table | None, new_table: Table | None) -> Tuple: ...

class Array(Tuple):
    def get_sql(self, **kwargs: Any) -> str: ...

class Bracket(Tuple):
    def __init__(self, term: Any) -> None: ...

class NestedCriterion(Criterion):
    left: Any
    comparator: Comparator
    nested_comparator: ComplexCriterion
    right: Any
    nested: Any

    def __init__(
            self,
            comparator: Comparator,
            nested_comparator: ComplexCriterion,
            left: Any,
            right: Any,
            nested: Any,
            alias: str | None = None,
    ) -> None: ...
    def nodes_(self) -> Iterator[NodeT]: ...
    @property
    def is_aggregate(self) -> bool | None: ...
    def replace_table(self, current_table: Table | None, new_table: Table | None) -> NestedCriterion: ...
    def get_sql(self, with_alias: bool = False, **kwargs: Any) -> str: ...

class BasicCriterion(Criterion):
    comparator: Comparator
    left: Term
    right: Term

    def __init__(self, comparator: Comparator, left: Term, right: Term, alias: str | None = None) -> None: ...
    def nodes_(self) -> Iterator[NodeT]: ...
    @property
    def is_aggregate(self) -> bool | None: ...
    def replace_table(self, current_table: Table | None, new_table: Table | None) -> BasicCriterion: ...
    def get_sql(self, quote_char: str = '"', with_alias: bool = False, **kwargs: Any) -> str: ...

class ContainsCriterion(Criterion):
    term: Term
    container: Term

    def __init__(self, term: Term, container: Term, alias: str | None = None) -> None: ...
    def nodes_(self) -> Iterator[NodeT]: ...
    @property
    def is_aggregate(self) -> bool | None: ...
    def replace_table(self, current_table: Table | None, new_table: Table | None) -> ContainsCriterion: ...
    def get_sql(self, subquery: Any = None, **kwargs: Any) -> str: ...
    def negate(self) -> ContainsCriterion: ...

class ExistsCriterion(Criterion):
    container: QueryBuilder

    def __init__(self, container: QueryBuilder, alias: str | None = None) -> None: ...
    def get_sql(self, **kwargs: Any) -> str: ...
    def negate(self): ...

class RangeCriterion(Criterion):
    term: Term
    start: Any
    end: Any

    def __init__(self, term: Term, start: Any, end: Any, alias: str | None = None) -> None: ...
    def nodes_(self) -> Iterator[NodeT]: ...
    @property
    def is_aggregate(self) -> bool | None: ...

class BetweenCriterion(RangeCriterion):
    def replace_table(self, current_table: Table | None, new_table: Table | None) -> BetweenCriterion: ...
    def get_sql(self, **kwargs: Any) -> str: ...

class PeriodCriterion(RangeCriterion):
    def get_sql(self, **kwargs: Any) -> str: ...

class BitwiseAndCriterion(Criterion):
    term: Term
    value: Any

    def __init__(self, term: Term, value: Any, alias: str | None = None) -> None: ...
    def nodes_(self) -> Iterator[NodeT]: ...
    def replace_table(self, current_table: Table | None, new_table: Table | None) -> BitwiseAndCriterion: ...
    def get_sql(self, **kwargs: Any) -> str: ...

class NullCriterion(Criterion):
    term: Term

    def __init__(self, term: Term, alias: str | None = None) -> None: ...
    def nodes_(self) -> Iterator[NodeT]: ...
    def replace_table(self, current_table: Table | None, new_table: Table | None) -> NullCriterion: ...
    def get_sql(self, with_alias: bool = False, **kwargs: Any) -> str: ...

class NotNullCriterion(NullCriterion):
    def get_sql(self, with_alias: bool = False, **kwargs: Any) -> str: ...

class ComplexCriterion(BasicCriterion):
    def get_sql(self, subcriterion: bool = False, **kwargs: Any) -> str: ...
    def needs_brackets(self, term: Term) -> bool: ...

class ArithmeticExpression(Term):
    add_order: ClassVar[list[Arithmetic]]
    operator: Arithmetic
    left: Any
    right: Any

    def __init__(self, operator: Arithmetic, left: Any, right: Any, alias: str | None = None) -> None: ...
    def nodes_(self) -> Iterator[NodeT]: ...
    @property
    def is_aggregate(self) -> bool | None: ...
    def replace_table(self, current_table: Table | None, new_table: Table | None) -> ArithmeticExpression: ...
    def left_needs_parens(self, curr_op: str | None, left_op: str | None) -> bool: ...
    def right_needs_parens(self, curr_op: str | None, right_op: str | None) -> bool: ...
    def get_sql(self, with_alias: bool = False, **kwargs: Any) -> str: ...

class Case(Criterion):
    def __init__(self, alias: str | None = None) -> None: ...
    def nodes_(self) -> Iterator[NodeT]: ...
    @property
    def is_aggregate(self) -> bool | None: ...
    def when(self, criterion: Any, term: Any) -> Case: ...
    def replace_table(self, current_table: Table | None, new_table: Table | None) -> Case: ...
    def else_(self, term: Any) -> Case: ...
    def get_sql(self, with_alias: bool = False, **kwargs: Any) -> str: ...

class Not(Criterion):
    term: Term

    def __init__(self, term: Term, alias: str | None = None) -> None: ...
    def nodes_(self) -> Iterator[NodeT]: ...
    def get_sql(self, **kwargs: Any) -> str: ...
    def __getattr__(self, name: str) -> Any: ...
    def replace_table(self, current_table: Table | None, new_table: Table | None) -> Not: ...

class All(Criterion):
    term: Term

    def __init__(self, term: Term, alias: str | None = None) -> None: ...
    def nodes_(self) -> Iterator[NodeT]: ...
    def get_sql(self, **kwargs: Any) -> str: ...

class CustomFunction:
    name: str
    params: Sequence | None

    def __init__(self, name: str, params: Sequence | None = None) -> None: ...
    def __call__(self, *args: Any, **kwargs: Any) -> Function: ...

class Function(Criterion):
    name: str
    args: Any
    schema: Schema | None

    def __init__(self, name: str, *args: Any, schema: Schema | None = None, **kwargs: Any) -> None: ...
    def nodes_(self) -> Iterator[NodeT]: ...
    @property
    def is_aggregate(self) -> bool | None: ...
    def replace_table(self, current_table: Table | None, new_table: Table | None) -> Function: ...
    def get_special_params_sql(self, **kwargs: Any) -> Any: ...
    @staticmethod
    def get_arg_sql(arg: Any, **kwargs: Any) -> str: ...
    def get_function_sql(self, **kwargs: Any) -> str: ...
    def get_sql(self, **kwargs: Any) -> str: ...

class AggregateFunction(Function):
    is_aggregate: bool

    def __init__(self, name: str, *args: Any, **kwargs: Any) -> None: ...
    def filter(self, *filters: Any) -> AnalyticFunction: ...
    def get_filter_sql(self, **kwargs: Any) -> str: ...
    def get_function_sql(self, **kwargs: Any) -> str: ...

class AnalyticFunction(AggregateFunction):
    is_aggregate: bool
    is_analytic: bool

    def __init__(self, name: str, *args: Any, **kwargs: Any) -> None: ...
    def over(self, *terms: Any) -> AnalyticFunction: ...
    def orderby(self, *terms: Any, **kwargs: Any) -> AnalyticFunction: ...
    def get_partition_sql(self, **kwargs: Any) -> str: ...
    def get_function_sql(self, **kwargs: Any) -> str: ...

class WindowFrameAnalyticFunction(AnalyticFunction):
    class Edge:
        value: str | int | None

        def __init__(self, value: str | int | None = None) -> None: ...

    frame: str | None
    bound: tuple[str, Edge | None] | None

    def __init__(self, name: str, *args: Any, **kwargs: Any) -> None: ...
    def rows(self, bound: str | Edge, and_bound: Edge | None = None) -> WindowFrameAnalyticFunction: ...
    def range(self, bound: str | Edge, and_bound: Edge | None = None) -> WindowFrameAnalyticFunction: ...
    def get_frame_sql(self) -> str: ...
    def get_partition_sql(self, **kwargs: Any) -> str: ...

class IgnoreNullsAnalyticFunction(AnalyticFunction):
    def __init__(self, name: str, *args: Any, **kwargs: Any) -> None: ...
    def ignore_nulls(self) -> IgnoreNullsAnalyticFunction: ...
    def get_special_params_sql(self, **kwargs: Any) -> str | None: ...

class Interval(Node):
    templates: ClassVar[dict[Dialects, str]]
    units: ClassVar[list[str]]
    labels: ClassVar[list[str]]
    trim_pattern: re.Pattern
    dialect: Dialects | None
    largest: str | None
    smallest: str | None
    is_negative: bool
    # quarters: int # this property may not exists at runtime, typing doesn't support this cast
    # weeks: int # this property may not exists at runtime, typing doesn't support this cast

    def __init__(
            self,
            years: int = 0,
            months: int = 0,
            days: int = 0,
            hours: int = 0,
            minutes: int = 0,
            seconds: int = 0,
            microseconds: int = 0,
            quarters: int = 0,
            weeks: int = 0,
            dialect: Dialects | None = None,
    ) -> None: ...
    def get_sql(self, **kwargs: Any) -> str: ...

class Pow(Function):
    def __init__(self, term: Term, exponent: float, alias: str | None = None) -> None: ...

class Mod(Function):
    def __init__(self, term: Term, modulus: float, alias: str | None = None) -> None: ...

class Rollup(Function):
    def __init__(self, *terms: Any) -> None: ...

class PseudoColumn(Term):
    name: str

    def __init__(self, name: str) -> None: ...
    def get_sql(self, **kwargs: Any) -> str: ...

class AtTimezone(Term):
    is_aggregate: bool
    field: Field
    zone: str
    interval: bool

    def __init__(
            self, field: Field | str, zone: str, interval: bool = False, alias: str | None = None
    ) -> None: ...
    def get_sql(self, **kwargs: Any) -> str: ...