#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        """Abstract method to process data."""
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Abstract method to validate data."""
        pass

    def format_output(self, result: str) -> str:
        """Default implementation to format processed data as a string."""
        return f"Formatted Output: {result}"


class NumericProcessor(DataProcessor):
    print("Initial numeric process...")

    def validate(self, data: Any) -> bool:
        """Validates if the data is an int or float."""
        print("validating...")
        return isinstance(data, (int, float))

    def process(self, data: Any) -> Any:
        """Converts valid numeric data to float and squares it, otherwise raises ValueError."""
        print("processing")
        if not self.validate(data):
            print(
                f"Invalid data type for NumericProcessor: {
                    type(data)
                }. Expected int or float."
            )
            return print("Can not build the process")
        return float(data) ** 2

    def format_output(self, result: Any) -> str:
        """Formats the processed numeric data to two decimal places."""
        if not isinstance(result, (int, float)):
            return (
                f"Numeric Result: Invalid processed data type {type(result)}"
            )
        return f"Numeric Result: {result:.2f}"


class TextProcessor(DataProcessor):
    ...


class LogProcessor(DataProcessor):
    ...


if __name__ == "__main__":
    test1 = 1234
    test2 = "oi aqui"
    processor = NumericProcessor()
    processor.process(test1)
    processor.process(test2)


"""
Required Methods (must be implemented in all classes):
◦ process(self, data: Any) -> str
◦ validate(self, data: Any) -> bool
◦ format_output(self, result: str) -> str
"""

"""
Required Implementation:
• Create a DataProcessor abstract base class using ABC and @abstractmethod
• Mark process() and validate() as abstract methods
• Provide a default implementation for format_output() that can be overridden
• Override abstract methods in subclasses to provide specialized behavior
• Demonstrate polymorphic usage by processing different data types through the
same interface
• Include proper error handling for invalid data
"""

"""
=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===

Initializing Numeric Processor...
Processing data: [1, 2, 3, 4, 5]
Validation: Numeric data verified
Output: Processed 5 numeric values, sum=15, avg=3.0

Initializing Text Processor...
Processing data: "Hello Nexus World"
Validation: Text data verified
Output: Processed text: 17 characters, 3 words

Initializing Log Processor...
Processing data: "ERROR: Connection timeout"
Validation: Log entry verified
Output: [ALERT] ERROR level detected: Connection timeout
=== Polymorphic Processing Demo ===
"""
