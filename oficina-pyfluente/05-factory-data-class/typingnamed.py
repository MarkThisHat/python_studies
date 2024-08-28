import typing

Coordinate = typing.NamedTuple('Coordinate', [('lat', float), ('lon', float)])
print(issubclass(Coordinate, tuple))

print(typing.get_type_hints(Coordinate))
