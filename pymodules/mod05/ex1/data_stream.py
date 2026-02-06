#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any


class DataStream(ABC):
    def __init__(self, stream_id: str):
        self.stream_id = stream_id
        self.count = 0

    @abstractmethod
    def process_batch(self, data_batch: list[Any]) -> str:
        pass

    def filter_data(
        self, data_batch: list[Any], criteria: str | None = None
    ) -> list[Any]:
        return data_batch

    def get_stats(self) -> dict[str, str | int]:
        return {"stream_id": self.stream_id, "count": self.count}


class SensorStream(DataStream):
    def process_batch(self, data_batch: list[Any]) -> str:
        temps = [x for x in data_batch if isinstance(x, (int, float))]
        self.count += len(temps)
        avg = sum(temps) / len(temps)
        return f"Sensor: {len(temps)} readings, avg={avg}"


class TransactionStream(DataStream):
    def process_batch(self, data_batch: list[Any]) -> str:
        values = [x for x in data_batch if isinstance(x, int)]
        self.count += len(values)
        return f"Transactions: {len(values)} ops, net={sum(values)}"


class EventStream(DataStream):
    def process_batch(self, data_batch: list[Any]) -> str:
        errors = [x for x in data_batch if x == "error"]
        self.count += len(data_batch)
        return f"Events: {len(data_batch)}, errors={len(errors)}"


class StreamProcessor:
    def handle(self, stream: DataStream, batch: list[Any]) -> str:
        return stream.process_batch(batch)


if __name__ == "__main__":
    streams = [
        SensorStream("S1"),
        TransactionStream("T1"),
        EventStream("E1"),
    ]

    batches = [
        [22.5, 23.0],
        [100, -50, 25],
        ["login", "error", "logout"],
    ]

    manager = StreamProcessor()

    for s, b in zip(streams, batches, strict=False):
        print(manager.handle(s, b))
