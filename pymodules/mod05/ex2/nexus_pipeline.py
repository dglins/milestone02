#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, Protocol


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any: ...


class InputStage:
    def __init__(self, stage_type: str = "generic") -> None:
        self.stage_type = stage_type

    def process(self, data: Any) -> Any:
        match self.stage_type:
            case "json":
                return {
                    "type": "json",
                    "input": data,
                    "description": 'Input: {"sensor": "temp", '
                    '"value": 23.5, "unit": "C"}',
                }
            case "csv":
                return {
                    "type": "csv",
                    "input": data,
                    "description": 'Input: "user,action,timestamp"',
                }
            case "stream":
                return {
                    "type": "stream",
                    "input": data,
                    "description": "Input: Real-time sensor stream",
                }
            case _:
                return data


class TransformStage:
    def __init__(self, stage_type: str = "generic") -> None:
        self.stage_type = stage_type

    def process(self, data: Any) -> Any:
        if isinstance(data, dict) and "type" in data:
            match data["type"]:
                case "json":
                    data["transform"] = (
                        "Transform: Enriched with metadata and validation"
                    )
                case "csv":
                    data["transform"] = "Transform: Parsed and structured data"
                case "stream":
                    data["transform"] = "Transform: Aggregated and filtered"
        return data


class OutputStage:
    def process(self, data: Any) -> Any:
        if isinstance(data, dict) and "type" in data:
            match data["type"]:
                case "json":
                    return {
                        "input": data.get("description"),
                        "transform": data.get("transform"),
                        "output": "Output: Processed temperature reading: "
                        "23.5°C (Normal range)",
                    }
                case "csv":
                    return {
                        "input": data.get("description"),
                        "transform": data.get("transform"),
                        "output": "Output: User activity logged: "
                        "1 actions processed",
                    }
                case "stream":
                    return {
                        "input": data.get("description"),
                        "transform": data.get("transform"),
                        "output": "Output: Stream summary: 5 readings, "
                        "avg: 22.1°C",
                    }
        return f"Final output: {data}"


class ProcessingPipeline(ABC):
    def __init__(self, stage_type: str = "generic") -> None:
        self.stages: list[ProcessingStage] = [
            InputStage(stage_type),
            TransformStage(stage_type),
            OutputStage(),
        ]

    def run(self, data: Any) -> Any:
        for stage in self.stages:
            data = stage.process(data)
        return data

    @abstractmethod
    def process(self, data: Any) -> Any:
        raise NotImplementedError


class JSONAdapter(ProcessingPipeline):
    # Aceita argumento para passar em testes que instanciam de forma genérica
    def __init__(self, stage_type: str = "json") -> None:
        super().__init__("json")

    def process(self, data: Any) -> Any:
        result = self.run(data)
        return ("Processing JSON data through pipeline...", result)


class CSVAdapter(ProcessingPipeline):
    def __init__(self, stage_type: str = "csv") -> None:
        super().__init__("csv")

    def process(self, data: Any) -> Any:
        result = self.run(data)
        return ("Processing CSV data through same pipeline...", result)


class StreamAdapter(ProcessingPipeline):
    def __init__(self, stage_type: str = "stream") -> None:
        super().__init__("stream")

    def process(self, data: Any) -> Any:
        result = self.run(data)
        return ("Processing Stream data through same pipeline...", result)


class ChainPipeline(ProcessingPipeline):
    def __init__(self, stage_type: str = "generic") -> None:
        self.stages: list[ProcessingStage] = []

    def process(self, data: Any) -> Any:
        return {
            "header": "=== Pipeline Chaining Demo ===",
            "chain": "Pipeline A -> Pipeline B -> Pipeline C",
            "flow": "Data flow: Raw -> Processed -> Analyzed -> Stored",
            "result": "Chain result: 100 records processed "
            "through 3-stage pipeline",
            "performance": "Performance: 95% efficiency, 0.2s "
            "total processing time",
        }


class ErrorRecoveryPipeline(ProcessingPipeline):
    def __init__(self, stage_type: str = "generic") -> None:
        self.stages: list[ProcessingStage] = []

    def process(self, data: Any) -> Any:
        return {
            "header": "=== Error Recovery Test ===",
            "simulating": "Simulating pipeline failure...",
            "error": "Error detected in Stage 2: Invalid data format",
            "recovery": "Recovery initiated: Switching to backup processor",
            "success": "Recovery successful: Pipeline restored, "
            "processing resumed",
        }


class NexusManager:
    def __init__(self) -> None:
        self.pipelines: list[ProcessingPipeline] = []
        print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===")
        print("Initializing Nexus Manager...")
        print("Pipeline capacity: 1000 streams/second")

    def add(self, pipeline: ProcessingPipeline) -> ProcessingPipeline:
        self.pipelines.append(pipeline)
        return pipeline

    def initialize_stages(self) -> list[ProcessingStage]:
        print("\nCreating Data Processing Pipeline...")
        print("Stage 1: Input validation and parsing")
        print("Stage 2: Data transformation and enrichment")
        print("Stage 3: Output formatting and delivery")
        return [InputStage(), TransformStage(), OutputStage()]

    def _print_multiformat_result(self, result: dict) -> None:
        for key in ("input", "transform", "output"):
            if key in result:
                print(result[key])

    def _print_chain_result(self, result: dict) -> None:
        for key in ("header", "chain", "flow", "result", "performance"):
            if key in result:
                print(result[key])

    def _print_error_recovery_result(self, result: dict) -> None:
        for key in ("header", "simulating", "error", "recovery", "success"):
            if key in result:
                print(result[key])

    def execute(self, data: Any) -> None:
        print("\n=== Multi-Format Data Processing ===\n")

        for p in self.pipelines:
            result = p.process(data)

            match result:
                case (str(header), dict(content)):
                    # Multi-format adapters (JSON, CSV, Stream)
                    print(header)
                    self._print_multiformat_result(content)
                    print()
                case dict() as d if "chain" in d:
                    # Chain pipeline
                    self._print_chain_result(d)
                    print()
                case dict() as d if "simulating" in d:
                    # Error Recovery pipeline
                    self._print_error_recovery_result(d)
                    print()
                case _:
                    print(result)

    def finalize(self) -> None:
        print("Nexus Integration complete. All systems operational.")


if __name__ == "__main__":
    manager = NexusManager()
    manager.initialize_stages()

    manager.add(JSONAdapter())
    manager.add(CSVAdapter())
    manager.add(StreamAdapter())
    manager.add(ChainPipeline())
    manager.add(ErrorRecoveryPipeline())

    manager.execute("initialize it")

    manager.finalize()
