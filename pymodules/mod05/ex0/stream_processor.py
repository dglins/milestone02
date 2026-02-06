#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return isinstance(data, list) and all(
            isinstance(x, (int, float)) for x in data
        )

    def process(self, data: Any) -> str:
        if not self.validate(data):
            return "Invalid numeric data"

        total = sum(data)
        avg = total / len(data)

        return f"Processed {len(data)} numeric values, sum={total}, avg={avg}"


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return isinstance(data, str)

    def process(self, data: Any) -> str:
        if not self.validate(data):
            return "Invalid text data"

        chars = len(data)
        words = len(data.split())

        return f"Processed text: {chars} characters, {words} words"


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return isinstance(data, str)

    def process(self, data: Any) -> str:
        if not self.validate(data):
            return "Invalid log entry"

        level, _, msg = data.partition(":")
        return f"[{level}] {level} level detected: {msg.strip()}"


if __name__ == "__main__":
    processors: list[DataProcessor] = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor(),
    ]

    samples = [
        [1, 2, 3],
        "Hello Nexus",
        "INFO: System ready",
    ]

    for p, s in zip(processors, samples, strict=False):
        try:
            result = p.process(s)
            print(p.format_output(result))
        except Exception as e:
            print("Error:", e)
