#!/usr/bin/env python3

import sys


def ft_score_analytics(args: list[str]) -> None:
    print("=== Player Score Analytics ===")

    if len(args) < 2:
        print(
            "No scores provided. "
            "Usage: python3 ft_score_analytics.py <score1> <score2> ..."
        )
        return

    try:
        scores: list[int] = [int(arg) for arg in args[1:]]
    except ValueError:
        print("oops, I typed 'banana' instead of '1000'")
        return

    total_players: int = len(scores)
    total_score: int = sum(scores)
    average_score: float = total_score / total_players
    high_score: int = max(scores)
    low_score: int = min(scores)
    score_range: int = high_score - low_score

    print(f"""
Scores processed: {scores}
Total players: {total_players}
Total score: {total_score}
Average score: {average_score:.2f}
High score: {high_score}
Low score: {low_score}
Score range: {score_range}
""")


if __name__ == "__main__":
    ft_score_analytics(sys.argv)
