from dataclasses import dataclass


@dataclass
class Rectangle:
    # TODO: Propose data format to hold rectangle information

    def contains(self, other: "Rectangle") -> bool:
        # TODO: Implement
        raise NotImplementedError

    def intersect(self, other: "Rectangle") -> bool:
        # TODO: Implement
        raise NotImplementedError
