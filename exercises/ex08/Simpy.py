"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730483098"


class Simpy:
    """Simplified version of NumPy."""
    values: list[float]

    def __init__(self, vs: list[float]):
        """Constructor definition for initialization of attributes."""
        self.values = vs

    def __str__(self) -> str:
        """Produce a str representation of a Simpy object for humans."""
        return(f"Simpy({self.values})")

    def fill(self, filler: float, amount: int) -> None:
        """Fills a Simpy's values with a specific number of repeating values."""
        i: int = 0
        while i < amount:
            if i >= len(self.values):
                self.values.append(filler)
            else:
                self.values[i] = filler
            i += 1
        if len(self.values) > amount:
            while len(self.values) != amount:
                self.values.pop(amount)

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Operator overload for addition."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for val in self.values:
                result.values.append(val + rhs)
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.values.append(self.values[i] + rhs.values[i])
                i += 1
        return result

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Operator overload for exponentiation."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for val in self.values:
                result.values.append(val ** rhs)
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.values.append(self.values[i] ** rhs.values[i])
                i += 1
        return result

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Operator overload for equality that returns a mask."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for val in self.values:
                result.append(val == rhs)
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.append(self.values[i] == rhs.values[i])
                i += 1
        return result

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Operator overload for greater than that returns a mask."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for val in self.values:
                result.append(val > rhs)
            return result
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.append(self.values[i] > rhs.values[i])
                i += 1
        return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Operator overloading for subscription notation."""
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            assert len(self.values) == len(rhs)
            result: Simpy = Simpy([])
            i: int = 0
            while i < len(rhs):
                if rhs[i]:
                    result.values.append(self.values[i])
                i += 1
            return result

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fill in a Simpy's values attribute with a range of values."""
        self.values = []
        assert step != 0.0
        if step > 0.0:
            next_value: float = start
            while next_value < stop:
                self.values.append(next_value)
                next_value += step
        else:
            next_value: float = start
            while next_value > stop:
                self.values.append(next_value)
                next_value += step

    def sum(self) -> float:
        """Compute and return the sum of all items in the values attribute."""
        return sum(self.values)