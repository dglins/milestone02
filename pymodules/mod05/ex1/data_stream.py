#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Union


class DataStream(ABC):
    def __init__(
        self, stream_id: str, stream_type: str, stream_uses: List[str]
    ):
        self.stream_id = stream_id
        self.stream_type = stream_type
        self.stream_uses = tuple(stream_uses)
        self.processed_batches = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        raise NotImplementedError

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria is None:
            return list(data_batch)
        return [item for item in data_batch if criteria in str(item)]

    def get_stats(self) -> Dict[str, Union[str, int]]:
        return {
            "stream_id": self.stream_id,
            "processed_batches": self.processed_batches,
        }


class SensorStream(DataStream):
    DEFAULT_ID = "SENSOR_001"
    DEFAULT_TYPE = "Environmental Data"
    DEFAULT_USES = ("temp", "humidity", "pressure")

    def __init__(self, stream_id: str = DEFAULT_ID):
        super().__init__(
            stream_id=stream_id,
            stream_type=self.DEFAULT_TYPE,
            stream_uses=self.DEFAULT_USES,
        )

    def process_batch(self, data_batch: List[Any]) -> str:
        values: List[float] = []
        for item in data_batch:
            s = str(item).strip()

            parts = s.split(":")
            if len(parts) < 2:
                continue

            last = parts[-1]
            try:
                values.append(float(last))
            except ValueError:
                continue

        if not values:
            return "Sensor processing error (no numeric readings found)."

        avg = sum(values) / len(values)
        self.processed_batches += 1
        return (
            f"Sensor analysis: {len(values)} readings processed, "
            f"avg temp: {avg:.1f}°C"
        )


class TransactionStream(DataStream):
    DEFAULT_ID = "TRANS_001"
    DEFAULT_TYPE = "Financial Data"
    DEFAULT_USES = ("buy", "sell")

    def __init__(self, stream_id: str = DEFAULT_ID):
        super().__init__(
            stream_id=stream_id,
            stream_type=self.DEFAULT_TYPE,
            stream_uses=self.DEFAULT_USES,
        )

    def process_batch(self, data_batch: List[Any]) -> str:
        amounts: List[float] = []
        buy_total = 0.0
        sell_total = 0.0

        for item in data_batch:
            s = str(item).strip()
            if ":" not in s:
                continue

            action, raw = s.split(":", 1)
            action = action.strip().lower()
            raw = raw.strip()

            try:
                value = float(raw)
            except ValueError:
                continue

            amounts.append(value)
            if action == "buy":
                buy_total += value
            elif action == "sell":
                sell_total += value

        if not amounts:
            return (
                "Transaction processing error (no numeric transactions found)."
            )

        net = sell_total - buy_total
        self.processed_batches += 1
        sign = "+" if net >= 0 else ""
        return (
            f"Transaction analysis: {len(amounts)} operations, "
            f"net flow: {sign}{net:.0f} units"
        )


class EventStream(DataStream):
    DEFAULT_ID = "EVENT_001"
    DEFAULT_TYPE = "System Events"
    DEFAULT_USES = ("login", "error", "logout")

    def __init__(self, stream_id: str = DEFAULT_ID):
        super().__init__(
            stream_id=stream_id,
            stream_type=self.DEFAULT_TYPE,
            stream_uses=self.DEFAULT_USES,
        )

    def process_batch(self, data_batch: List[Any]) -> str:
        counts: Dict[str, int] = {}
        total = 0

        for item in data_batch:
            evt = str(item).strip().lower()
            if not evt:
                continue
            counts[evt] = counts.get(evt, 0) + 1
            total += 1

        if total == 0:
            return "Event processing error (empty batch)."

        self.processed_batches += 1

        errors = counts.get("error", 0)
        error_word = "error" if errors == 1 else "errors"
        return (
            f"Event analysis: {total} events, {errors} {error_word} detected"
        )


class StreamProcessor:
    def __init__(self, streams: List[DataStream]):
        self.streams_by_id = {s.stream_id: s for s in streams}

    def execute(self, batch_map: Dict[str, List[Any]]) -> Dict[str, str]:
        """
        batch_map: { "SENSOR_001", "TRANS_001", "EVENT_001" }
        """
        results: Dict[str, str] = {}

        for stream_id, batch in batch_map.items():
            stream = self.streams_by_id.get(stream_id)
            if stream is None:
                results[stream_id] = (
                    "Unknown stream_id (no registered stream)."
                )
                continue

            results[stream_id] = stream.process_batch(batch)

        return results


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    print()

    sensor_batch = ["temp:22.5", "humidity:65", "pressure:1013"]
    transaction_batch = ["buy:100", "sell:150", "buy:75"]
    event_batch = ["login", "error", "logout"]

    # Sensor Stream
    print("Initializing Sensor Stream...")
    s = SensorStream()
    print(f"Stream ID: {s.stream_id}, Type: {s.stream_type}")
    print(f"Processing sensor batch: {sensor_batch}")
    print(s.process_batch(sensor_batch))
    print()

    # Transaction Stream
    print("Initializing Transaction Stream...")
    t = TransactionStream()
    print(f"Stream ID: {t.stream_id}, Type: {t.stream_type}")
    print(f"Processing transaction batch: {transaction_batch}")
    print(t.process_batch(transaction_batch))
    print()

    # Event Stream
    print("Initializing Event Stream...")
    e = EventStream()
    print(f"Stream ID: {e.stream_id}, Type: {e.stream_type}")
    print(f"Processing event batch: {event_batch}")
    print(e.process_batch(event_batch))
    print()

    # Polymorphic Processing
    print("=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")
    print()

    streams = (s, t, e)
    processor = StreamProcessor(streams)

    mixed_batches = {
        "Batch 1": {
            "SENSOR_001": ["temp:30.0", "temp:28.0"],
            "TRANS_001": ["buy:100", "sell:40", "buy:25", "sell:10"],
            "EVENT_001": ["login", "error", "logout"],
        }
    }

    for batch_name, batch_map in mixed_batches.items():
        print(f"{batch_name} Results:")
        results = processor.execute(batch_map)

        # Count readings/operations/events
        sensor_count = len(batch_map.get("SENSOR_001", []))
        trans_count = len(batch_map.get("TRANS_001", []))
        event_count = len(batch_map.get("EVENT_001", []))

        print(f"- Sensor data: {sensor_count} readings processed")
        print(f"- Transaction data: {trans_count} operations processed")
        print(f"- Event data: {event_count} events processed")
        print()

    # Filtering
    filter_criteria = {
        "sensor": "ALERT",
        "transaction": "buy:1000",
        "event": "error",
    }

    sensor_alerts_batch = [
        "ALERT:temp:45.0",
        "temp:22.0",
        "ALERT:pressure:1100",
        "humidity:60",
    ]
    large_transaction_batch = ["buy:1000", "sell:150", "buy:75", "buy:1000"]
    event_noise_batch = ["login", "error", "logout", "error"]

    filtered_sensors = s.filter_data(
        sensor_alerts_batch, filter_criteria["sensor"]
    )
    filtered_transactions = t.filter_data(
        large_transaction_batch, filter_criteria["transaction"]
    )

    print("Stream filtering active: High-priority data only")
    print(
        f"Filtered results: {len(filtered_sensors)} critical sensor alerts, "
        f"{len(filtered_transactions)} large transaction"
    )
    print()
    print("All streams processed successfully. Nexus throughput optimal.")
