_T = TypeVar("_T")

# The ``create_model`` decorator is defined by a library.
# This could be in a type stub or inline.
@typing.dataclass_transform()
def create_model(cls: Type[_T]) -> Type[_T]:
    cls.__init__ = ...
    cls.__eq__ = ...
    cls.__ne__ = ...
    return cls

"""
# The ``create_model`` decorator can now be used to create new model
# classes, like this:
@create_model
class CustomerModel:
    id: int
    name: str
"""