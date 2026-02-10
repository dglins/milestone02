#!/usr/bin/env python3

import time


class StreamWizard:
    def event_generator(self, count: int, offset: int = 0):
        """Gera eventos de jogo sob demanda."""
        actions: list[str] = ["killed monster", "found treasure", "leveled up"]
        players: list[str] = ["alice", "bob", "charlie", "david", "eve"]
        for i in range(1, count + 1):
            idx: int = i + offset
            level: int = int(i % (count / idx)) * 7
            player: str = players[idx % len(players)]
            action: str = actions[idx % len(actions)]
            yield {"id": i, "player": player, "level": level, "action": action}

    def fibonacci_gen(self, n: int):
        """Gerador da sequência de Fibonacci."""
        a, b = 0, 1
        for _ in range(n):
            yield a
            a, b = b, a + b

    def is_prime(self, n: int) -> bool:
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def prime_gen(self, count: int):
        """Gerador de números primos."""
        num = 2
        found = 0
        while found < count:
            if self.is_prime(num):
                yield num
                found += 1
            num += 1


def process_stream(count: int = 1000):
    wizard = StreamWizard()
    print("=== Game Data Stream Processor ===")
    print()
    print(f"Processing {count} game events...")
    print()

    high_level_count = 0
    treasure_count = 0
    levelup_count = 0

    start_time = time.time()

    for event in wizard.event_generator(count, 20):
        if event["id"] <= 3:
            print(
                f"Event {event['id']}: Player {event['player']} "
                f"(level {event['level']}) {event['action']}"
            )

        if event["level"] >= 10:
            high_level_count += 1
        if event["action"] == "found treasure":
            treasure_count += 1
        elif event["action"] == "leveled up":
            levelup_count += 1

    end_time = time.time()

    print("...")
    print()
    print("=== Stream Analytics ===")
    print(f"Total events processed: {count}")
    print(f"High-level players (10+): {high_level_count}")
    print(f"Treasure events: {treasure_count}")
    print(f"Level-up events: {levelup_count}")
    print()
    print("Memory usage: Constant (streaming)")
    print(f"Processing time: {end_time - start_time:.3f} seconds")
    print()
    print("\n=== Generator Demonstration ===")
    fib_list = [str(n) for n in wizard.fibonacci_gen(10)]
    print(f"Fibonacci sequence (first 10): {', '.join(fib_list)}")

    prime_list = [str(n) for n in wizard.prime_gen(5)]
    print(f"Prime numbers (first 5): {', '.join(prime_list)}")


if __name__ == "__main__":
    process_stream()
