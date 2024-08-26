from _typeshed import Incomplete

from pypika.terms import Function

class If(Function):
    def __init__(self, *conditions: Incomplete, **kwargs: Incomplete) -> None: ...

class MultiIf(Function):
    def __init__(self, *conditions: Incomplete, **kwargs: Incomplete) -> None: ...
