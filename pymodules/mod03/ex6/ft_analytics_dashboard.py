#!/usr/bin/env python3


def main():
    # --- Sample Raw Data ---
    raw_players = [
        {
            "name": "alice",
            "score": 2300,
            "achievements": ["first_blood", "level_10"],
            "region": "north",
        },
        {
            "name": "bob",
            "score": 1800,
            "achievements": ["level_10"],
            "region": "east",
        },
        {
            "name": "charlie",
            "score": 2150,
            "achievements": ["boss_slayer", "level_10", "marathoner"],
            "region": "north",
        },
        {
            "name": "diana",
            "score": 2050,
            "achievements": ["first_blood", "collector"],
            "region": "central",
        },
    ]

    print("=== Game Analytics Dashboard ===")

    # --- List Comprehensions: Transformation & Filtering ---
    # Goal: Extract names of high scorers and create a list of doubled scores
    high_scorers = [p["name"] for p in raw_players if p["score"] > 2000]
    doubled_scores = [p["score"] * 2 for p in raw_players]

    print("\n=== List Comprehension Examples ===")
    print(f"High scorers (>2000): {high_scorers}")
    print(f"Scores doubled: {doubled_scores}")

    # --- Dict Comprehensions: Mappings & Logic ---
    # Goal: Create quick lookups and categorize data
    player_scores = {p["name"]: p["score"] for p in raw_players}
    achievement_counts = {
        p["name"]: len(p["achievements"]) for p in raw_players
    }

    # Categorizing scores: High if > 2000, else Low
    score_categories = {
        p["name"]: "High" if p["score"] > 2000 else "Low" for p in raw_players
    }

    print("\n=== Dict Comprehension Examples ===")
    print(f"Player scores: {player_scores}")
    print(f"Achievement counts: {achievement_counts}")
    print(f"Score categories: {score_categories}")

    # --- Set Comprehensions: Deduplication ---
    # Goal: Extract unique values across the entire dataset
    unique_regions = {p["region"] for p in raw_players}
    # Nested comprehension trick to flatten all achievements
    # into one unique set
    unique_achievements = {
        medal for p in raw_players for medal in p["achievements"]
    }

    print("\n=== Set Comprehension Examples ===")
    print(f"Active regions: {unique_regions}")
    print(f"Unique achievements: {unique_achievements}")

    # --- Combined Analysis ---
    all_scores = [p["score"] for p in raw_players]
    avg_score = sum(all_scores) / len(all_scores)

    # Finding the top performer (the person with the max score)
    top_score = max(all_scores)
    top_performer = [
        p["name"] for p in raw_players if p["score"] == top_score
    ][0]

    print("\n=== Combined Analysis ===")
    print(f"Total players: {len(raw_players)}")
    print(f"Total unique achievements: {len(unique_achievements)}")
    print(f"Average score: {avg_score}")
    print(f"Top performer: {top_performer} ({top_score} points)")


if __name__ == "__main__":
    main()
