#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any


def pretty_data(data: Any) -> str:
    if isinstance(data, str):
        return f"\"{data}\""
    return str(data)


class DataProcessor(ABC):
    name: str = "Generic Processor"

    @abstractmethod
    def process(self, data: Any) -> str:
        raise NotImplementedError

    @abstractmethod
    def validate(self, data: Any) -> bool:
        raise NotImplementedError

    # STANDARD OUTPUT
    def format_output(self, data: Any) -> str:
        result = self.process(data)
        validation = (
            f"{self.name.split()[0]} data verified"
            if self.validate(data)
            else "Invalid data"
        )

        return (
            f"\nInitializing {self.name}...\n"
            f"Processing data: {pretty_data(data)}\n"
            f"Validation: {validation}\n"
            f"Output: {result}"
        )

    # POLYMORPHIC OUTPUT
    def format_result(self, data: Any, prefix: str) -> str:
        return f"{prefix}: {self.process(data)}"


class NumericProcessor(DataProcessor):
    name = "Numeric Processor"

    def validate(self, data: Any) -> bool:
        return isinstance(data, list)

    def process(self, data: Any) -> str:
        if not self.validate(data):
            return "Invalid numeric data."

        try:
            if len(data) == 0:
                raise ValueError("Empty list.")

            total = sum(data)
            avg = total / len(data)

        except (TypeError, ValueError, ZeroDivisionError) as e:
            return f"Numeric processing error: {e}"

        return f"Processed {len(data)} numeric values, sum={total}, avg={avg}"


class TextProcessor(DataProcessor):
    name = "Text Processor"

    def validate(self, data: Any) -> bool:
        return isinstance(data, str)

    def process(self, data: Any) -> str:
        if not self.validate(data):
            return "Invalid text data."

        try:
            chars = len(data)
            words = len(data.split())

        except Exception as e:
            return f"Text processing error: {e}"

        return f"Processed text: {chars} characters, {words} words"


class LogProcessor(DataProcessor):
    name = "Log Processor"

    def validate(self, data: Any) -> bool:
        return isinstance(data, str) and ":" in data

    def process(self, data: Any) -> str:
        if not self.validate(data):
            return "Invalid log entry."

        try:
            level, _, msg = data.partition(":")
            level = level.strip().upper()
            msg = msg.strip()

        except Exception as e:
            return f"Log parsing error: {e}"

        if level == "ERROR":
            return f"[ALERT] ERROR level detected: {msg}"

        return f"[{level}] {level} level detected: {msg}"


# =========================
# Execution helpers
# =========================

def run_standard(processors: DataProcessor, samples: list[Any]) -> str:
    return "\n".join(
        p.format_output(s)
        for p, s in zip(processors, samples, strict=False)
    )


def run_polymorphic(processors: DataProcessor, samples: list[Any]) -> str:
    lines = ["Processing multiple data types through same interface..."]
    lines.extend(
        p.format_result(s, f"Result {i}")
        for i, (p, s) in enumerate(zip(processors, samples,
                                       strict=False), start=1)
    )
    return "\n".join(lines)


if __name__ == "__main__":
    processors = [NumericProcessor(), TextProcessor(), LogProcessor()]

    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    print(
        run_standard(
            processors,
            [[1, 2, 3, 4, 5], "Hello Nexus World",
             "ERROR: Connection timeout"],
        )
    )

    print("\n=== Polymorphic Processing Demo ===\n")
    print(
        run_polymorphic(
            processors,
            [[1, 2, 3], "Hello Nexus", "INFO: System ready"],
        )
    )

    print("\nFoundation systems online. Nexus ready for advanced streams.")
