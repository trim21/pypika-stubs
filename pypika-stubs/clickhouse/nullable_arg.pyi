from binascii import Incomplete

from pypika.terms import Function as Function, Term

class IfNull(Function):
    def __init__(
        self, term: str | Term, alt: Incomplete, **kwargs: Incomplete
    ) -> None: ...
