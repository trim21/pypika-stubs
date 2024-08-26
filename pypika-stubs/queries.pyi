from _typeshed import Incomplete
from pypika.enums import (
    Dialects as Dialects,
    JoinType as JoinType,
    ReferenceOption as ReferenceOption,
    SetOperation as SetOperation,
)
from pypika.terms import (
    ArithmeticExpression as ArithmeticExpression,
    Criterion as Criterion,
    EmptyCriterion as EmptyCriterion,
    Field as Field,
    Function as Function,
    Index as Index,
    Node as Node,
    PeriodCriterion as PeriodCriterion,
    Rollup as Rollup,
    Star as Star,
    Term as Term,
    Tuple as Tuple,
    ValueWrapper as ValueWrapper,
)
from pypika.utils import (
    JoinException as JoinException,
    QueryException as QueryException,
    RollupException as RollupException,
    SetOperationException as SetOperationException,
    builder as builder,
    format_alias_sql as format_alias_sql,
    format_quotes as format_quotes,
    ignore_copy as ignore_copy,
)
from typing import Any, Sequence

class Selectable(Node):
    alias: Incomplete
    def __init__(self, alias: str) -> None: ...
    def as_(self, alias: str) -> Selectable: ...
    def field(self, name: str) -> Field: ...
    @property
    def star(self) -> Star: ...
    def __getattr__(self, name: str) -> Field: ...
    def __getitem__(self, name: str) -> Field: ...
    def get_table_name(self) -> str: ...

class AliasedQuery(Selectable):
    name: Incomplete
    query: Incomplete
    def __init__(self, name: str, query: Selectable | None = None) -> None: ...
    def get_sql(self, **kwargs: Any) -> str: ...
    def __eq__(self, other: AliasedQuery) -> bool: ...
    def __hash__(self) -> int: ...

class Schema:
    def __init__(self, name: str, parent: Schema | None = None) -> None: ...
    def __eq__(self, other: Schema) -> bool: ...
    def __ne__(self, other: Schema) -> bool: ...
    def __getattr__(self, item: str) -> Table: ...
    def get_sql(self, quote_char: str | None = None, **kwargs: Any) -> str: ...

class Database(Schema):
    def __getattr__(self, item: str) -> Schema: ...

class Table(Selectable):
    def __init__(
            self,
            name: str,
            schema: Schema | str | None = None,
            alias: str | None = None,
            query_cls: type['Query'] | None = None,
    ) -> None: ...
    def get_table_name(self) -> str: ...
    def get_sql(self, **kwargs: Any) -> str: ...
    def for_(self, temporal_criterion: Criterion) -> Table: ...
    def for_portion(self, period_criterion: PeriodCriterion) -> Table: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...
    def select(self, *terms: int | float | str | bool | Term | Field) -> QueryBuilder: ...
    def update(self) -> QueryBuilder: ...
    def insert(self, *terms: int | float | str | bool | Term | Field) -> QueryBuilder: ...

def make_tables(*names: tuple[str, str] | str, **kwargs: Any) -> list[Table]: ...

class Column:
    name: Incomplete
    type: Incomplete
    nullable: Incomplete
    default: Incomplete
    def __init__(
            self,
            column_name: str,
            column_type: str | None = None,
            nullable: bool | None = None,
            default: Any | Term | None = None,
    ) -> None: ...
    def get_name_sql(self, **kwargs: Any) -> str: ...
    def get_sql(self, **kwargs: Any) -> str: ...

def make_columns(*names: tuple[str, str] | str) -> list[Column]: ...

class PeriodFor:
    name: Incomplete
    start_column: Incomplete
    end_column: Incomplete
    def __init__(self, name: str, start_column: str | Column, end_column: str | Column) -> None: ...
    def get_sql(self, **kwargs: Any) -> str: ...

_TableT = Table

class Query:
    @classmethod
    def from_(cls, table: Selectable | str, **kwargs: Any) -> QueryBuilder: ...
    @classmethod
    def create_table(cls, table: str | Table) -> CreateQueryBuilder: ...
    @classmethod
    def create_index(cls, index: str | Index) -> CreateIndexBuilder: ...
    @classmethod
    def drop_database(cls, database: Database | Table) -> DropQueryBuilder: ...
    @classmethod
    def drop_table(cls, table: str | Table) -> DropQueryBuilder: ...
    @classmethod
    def drop_user(cls, user: str) -> DropQueryBuilder: ...
    @classmethod
    def drop_view(cls, view: str) -> DropQueryBuilder: ...
    @classmethod
    def drop_index(cls, index: str | Index) -> DropQueryBuilder: ...
    @classmethod
    def into(cls, table: Table | str, **kwargs: Any) -> QueryBuilder: ...
    @classmethod
    def with_(cls, table: str | Selectable, name: str, **kwargs: Any) -> QueryBuilder: ...
    @classmethod
    def select(cls, *terms: int | float | str | bool | Term, **kwargs: Any) -> QueryBuilder: ...
    @classmethod
    def update(cls, table: str | Table, **kwargs: Any) -> QueryBuilder: ...
    @classmethod
    def Tables(cls, *names: tuple[str, str] | str, **kwargs: Any) -> list[Table]: ...
    @classmethod
    def Table(cls, table_name: str, **kwargs: Any) -> _TableT: ...

class _SetOperation(Selectable, Term):
    base_query: QueryBuilder
    def __init__(
            self,
            base_query: QueryBuilder,
            set_operation_query: QueryBuilder,
            set_operation: SetOperation,
            alias: str | None = None,
            wrapper_cls: type[ValueWrapper] = ...,
    ) -> None: ...
    def orderby(self, *fields: Field, **kwargs: Any) -> _SetOperation: ...
    def limit(self, limit: int) -> _SetOperation: ...
    def offset(self, offset: int) -> _SetOperation: ...
    def union(self, other: Selectable) -> _SetOperation: ...
    def union_all(self, other: Selectable) -> _SetOperation: ...
    def intersect(self, other: Selectable) -> _SetOperation: ...
    def except_of(self, other: Selectable) -> _SetOperation: ...
    def minus(self, other: Selectable) -> _SetOperation: ...
    def __add__(self, other: Selectable) -> _SetOperation: ...
    def __mul__(self, other: Selectable) -> _SetOperation: ...
    def __sub__(self, other: QueryBuilder) -> _SetOperation: ...
    def get_sql(self, with_alias: bool = False, subquery: bool = False, **kwargs: Any) -> str: ...

class QueryBuilder(Selectable, Term):
    QUOTE_CHAR: str
    SECONDARY_QUOTE_CHAR: str
    ALIAS_QUOTE_CHAR: Incomplete
    QUERY_ALIAS_QUOTE_CHAR: Incomplete
    QUERY_CLS = Query
    dialect: Incomplete
    as_keyword: Incomplete
    wrap_set_operation_queries: Incomplete
    immutable: Incomplete
    def __init__(
            self,
            dialect: Dialects | None = None,
            wrap_set_operation_queries: bool = True,
            wrapper_cls: type[ValueWrapper] = ...,
            immutable: bool = True,
            as_keyword: bool = False,
    ) -> None: ...
    def __copy__(self) -> QueryBuilder: ...
    def from_(self, selectable: Selectable | Query | str) -> QueryBuilder: ...
    def replace_table(self, current_table: Table | None, new_table: Table | None) -> QueryBuilder: ...
    def with_(self, selectable: Selectable, name: str) -> QueryBuilder: ...
    def into(self, table: str | Table) -> QueryBuilder: ...
    def select(self, *terms: Any) -> QueryBuilder: ...
    def delete(self) -> QueryBuilder: ...
    def update(self, table: str | Table) -> QueryBuilder: ...
    def columns(self, *terms: Any) -> QueryBuilder: ...
    def insert(self, *terms: Any) -> QueryBuilder: ...
    def replace(self, *terms: Any) -> QueryBuilder: ...
    def force_index(self, term: str | Index, *terms: str | Index) -> QueryBuilder: ...
    def use_index(self, term: str | Index, *terms: str | Index) -> QueryBuilder: ...
    def distinct(self) -> QueryBuilder: ...
    def for_update(self) -> QueryBuilder: ...
    def ignore(self) -> QueryBuilder: ...
    def prewhere(self, criterion: Criterion) -> QueryBuilder: ...
    def where(self, criterion: Term | EmptyCriterion) -> QueryBuilder: ...
    def having(self, criterion: Term | EmptyCriterion) -> QueryBuilder: ...
    def groupby(self, *terms: str | int | Term) -> QueryBuilder: ...
    def with_totals(self) -> QueryBuilder: ...
    def rollup(self, *terms: list | tuple | set | Term, **kwargs: Any) -> QueryBuilder: ...
    def orderby(self, *fields: Any, **kwargs: Any) -> QueryBuilder: ...
    def join(self, item: Table | QueryBuilder | AliasedQuery | Selectable, how: JoinType = ...) -> Joiner: ...
    def inner_join(self, item: Table | QueryBuilder | AliasedQuery) -> Joiner: ...
    def left_join(self, item: Table | QueryBuilder | AliasedQuery) -> Joiner: ...
    def left_outer_join(self, item: Table | QueryBuilder | AliasedQuery) -> Joiner: ...
    def right_join(self, item: Table | QueryBuilder | AliasedQuery) -> Joiner: ...
    def right_outer_join(self, item: Table | QueryBuilder | AliasedQuery) -> Joiner: ...
    def outer_join(self, item: Table | QueryBuilder | AliasedQuery) -> Joiner: ...
    def full_outer_join(self, item: Table | QueryBuilder | AliasedQuery) -> Joiner: ...
    def cross_join(self, item: Table | QueryBuilder | AliasedQuery) -> Joiner: ...
    def hash_join(self, item: Table | QueryBuilder | AliasedQuery) -> Joiner: ...
    def limit(self, limit: int) -> QueryBuilder: ...
    def offset(self, offset: int) -> QueryBuilder: ...
    def union(self, other: QueryBuilder) -> _SetOperation: ...
    def union_all(self, other: QueryBuilder) -> _SetOperation: ...
    def intersect(self, other: QueryBuilder) -> _SetOperation: ...
    def except_of(self, other: QueryBuilder) -> _SetOperation: ...
    def minus(self, other: QueryBuilder) -> _SetOperation: ...
    def set(self, field: Field | str, value: Any) -> QueryBuilder: ...
    def __add__(self, other: QueryBuilder) -> _SetOperation: ...
    def __mul__(self, other: QueryBuilder) -> _SetOperation: ...
    def __sub__(self, other: QueryBuilder) -> _SetOperation: ...
    def slice(self, slice: slice) -> QueryBuilder: ...
    def __getitem__(self, item: Any) -> QueryBuilder | Field: ...
    def fields_(self) -> list[Field]: ...
    def do_join(self, join: Join) -> None: ...
    def is_joined(self, table: Table) -> bool: ...
    def __eq__(self, other: QueryBuilder) -> bool: ...
    def __ne__(self, other: QueryBuilder) -> bool: ...
    def __hash__(self) -> int: ...
    def get_sql(self, with_alias: bool = False, subquery: bool = False, **kwargs: Any) -> str: ...
    def pipe(self, func: Incomplete, *args: Any, **kwargs: Any) -> Incomplete: ...

class Joiner:
    query: Incomplete
    item: Incomplete
    how: Incomplete
    type_label: Incomplete
    def __init__(
            self, query: QueryBuilder, item: Table | QueryBuilder | AliasedQuery, how: JoinType, type_label: str
    ) -> None: ...
    def on(self, criterion: Criterion | None, collate: str | None = None) -> QueryBuilder: ...
    def on_field(self, *fields: Any) -> QueryBuilder: ...
    def using(self, *fields: Any) -> QueryBuilder: ...
    def cross(self) -> QueryBuilder: ...

class Join:
    item: Incomplete
    how: Incomplete
    def __init__(self, item: Term, how: JoinType) -> None: ...
    def get_sql(self, **kwargs: Any) -> str: ...
    def validate(self, _from: Sequence[Table], _joins: Sequence[Table]) -> None: ...
    def replace_table(self, current_table: Table | None, new_table: Table | None) -> Join: ...

class JoinOn(Join):
    criterion: Incomplete
    collate: Incomplete
    def __init__(self, item: Term, how: JoinType, criteria: QueryBuilder, collate: str | None = None) -> None: ...
    def get_sql(self, **kwargs: Any) -> str: ...
    def validate(self, _from: Sequence[Table], _joins: Sequence[Table]) -> None: ...
    item: Incomplete
    def replace_table(self, current_table: Table | None, new_table: Table | None) -> JoinOn: ...

class JoinUsing(Join):
    fields: Incomplete
    def __init__(self, item: Term, how: JoinType, fields: Sequence[Field]) -> None: ...
    def get_sql(self, **kwargs: Any) -> str: ...
    def validate(self, _from: Sequence[Table], _joins: Sequence[Table]) -> None: ...
    item: Incomplete
    def replace_table(self, current_table: Table | None, new_table: Table | None) -> JoinUsing: ...

class CreateQueryBuilder:
    QUOTE_CHAR: str
    SECONDARY_QUOTE_CHAR: str
    ALIAS_QUOTE_CHAR: Incomplete
    QUERY_CLS = Query
    dialect: Incomplete
    def __init__(self, dialect: Dialects | None = None) -> None: ...
    def create_table(self, table: Table | str) -> CreateQueryBuilder: ...
    def temporary(self) -> CreateQueryBuilder: ...
    def unlogged(self) -> CreateQueryBuilder: ...
    def with_system_versioning(self) -> CreateQueryBuilder: ...
    def columns(self, *columns: str | tuple[str, str] | Column) -> CreateQueryBuilder: ...
    def period_for(self, name: str, start_column: str | Column, end_column: str | Column) -> CreateQueryBuilder: ...
    def unique(self, *columns: str | Column) -> CreateQueryBuilder: ...
    def primary_key(self, *columns: str | Column) -> CreateQueryBuilder: ...
    def foreign_key(
            self,
            columns: list[str | Column],
            reference_table: str | Table,
            reference_columns: list[str | Column],
            on_delete: ReferenceOption | None = None,
            on_update: ReferenceOption | None = None,
    ) -> CreateQueryBuilder: ...
    def as_select(self, query_builder: QueryBuilder) -> CreateQueryBuilder: ...
    def if_not_exists(self) -> CreateQueryBuilder: ...
    def get_sql(self, **kwargs: Any) -> str: ...

class CreateIndexBuilder:
    def __init__(self) -> None: ...
    def create_index(self, index: str | Index) -> CreateIndexBuilder: ...
    def columns(self, *columns: str | tuple[str, str] | Column) -> CreateIndexBuilder: ...
    def on(self, table: Table | str) -> CreateIndexBuilder: ...
    def where(self, criterion: Term | EmptyCriterion) -> CreateIndexBuilder: ...
    def unique(self) -> CreateIndexBuilder: ...
    def if_not_exists(self) -> CreateIndexBuilder: ...
    def get_sql(self) -> str: ...

class DropQueryBuilder:
    QUOTE_CHAR: str
    SECONDARY_QUOTE_CHAR: str
    ALIAS_QUOTE_CHAR: Incomplete
    QUERY_CLS = Query
    dialect: Incomplete
    def __init__(self, dialect: Dialects | None = None) -> None: ...
    def drop_database(self, database: Database | str) -> DropQueryBuilder: ...
    def drop_table(self, table: Table | str) -> DropQueryBuilder: ...
    def drop_user(self, user: str) -> DropQueryBuilder: ...
    def drop_view(self, view: str) -> DropQueryBuilder: ...
    def drop_index(self, index: str) -> DropQueryBuilder: ...
    def if_exists(self) -> DropQueryBuilder: ...
    def get_sql(self, **kwargs: Any) -> str: ...