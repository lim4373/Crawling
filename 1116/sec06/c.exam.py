'''
def make_dataclass(cls_name: str,
                   fields: Iterable[str | tuple[str, type] | tuple[str, type, Field]],
                   *,
                   bases: tuple[type, ...] = ...,
                   namespace: dict[str, Any] | None = ...,
                   init: bool = ...,
                   repr: bool = ...,
                   eq: bool = ...,
                   order: bool = ...,
                   unsafe_hash: bool = ...,
                   frozen: bool = ...) -> type
'''

class C :
    def __init__(self):