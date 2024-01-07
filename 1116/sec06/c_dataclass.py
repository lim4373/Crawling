from  dataclasses import *
#__init__  / __repr__


@dataclass
class Person:
    name :str
    age :int

##################################################
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
C = make_dataclass('C',
                   [('x', int),
                     'y',
                    ('z', int, field(default=5))],
                   namespace={'add_one': lambda self: self.x + 1}, )


if __name__ == '__main__':
     c=C(10,'python')  # C(x=10, y='python', z = 5 )
     print(c.x)
     print(c.add_one())
     print(c)