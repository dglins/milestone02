#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, List, Protocol
import time


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any: ...


class InputStage:
    def process(self, data: Any) -> Any:
        return data


class TransformStage:
    def process(self, data: Any) -> Any:
        return {"payload": data, "timestamp": time.time()}


class OutputStage:
    def process(self, data: Any) -> Any:
        return f"Final output: {data}"


class ProcessingPipeline(ABC):
    def __init__(self):
        self.stages: List[ProcessingStage] = [
            InputStage(),
            TransformStage(),
            OutputStage(),
        ]

    def run(self, data: Any) -> Any:
        for stage in self.stages:
            data = stage.process(data)
        return data

    @abstractmethod
    def process(self, data: Any) -> Any:
        pass


class JSONAdapter(ProcessingPipeline):
    def process(self, data: Any) -> Any:
        return self.run(data)


class CSVAdapter(ProcessingPipeline):
    def process(self, data: Any) -> Any:
        return self.run(data)


class StreamAdapter(ProcessingPipeline):
    def process(self, data: Any) -> Any:
        return self.run(data)


class NexusManager:
    def __init__(self):
        self.pipelines: List[ProcessingPipeline] = []

    def add(self, pipeline: ProcessingPipeline):
        self.pipelines.append(pipeline)

    def execute(self, data: Any):
        for p in self.pipelines:
            print(p.process(data))


if __name__ == "__main__":
    manager = NexusManager()

    manager.add(JSONAdapter())
    manager.add(CSVAdapter())
    manager.add(StreamAdapter())

    manager.execute({"sensor": "temp", "value": 22})
