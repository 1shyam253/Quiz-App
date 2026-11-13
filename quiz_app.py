#!/usr/bin/env python3
"""Quiz App - answer the questions and see your score at the end."""
import argparse
QUESTIONS = [
    ("What is the capital of France?", ["a) London", "b) Paris", "c) Rome", "d) Berlin"], "b"),
    ("Which language is this quiz written in?", ["a) Java", "b) C++", "c) Python", "d) Ruby"], "c"),
    ("What is 7 x 8?", ["a) 54", "b) 56", "c) 48", "d) 64"], "b"),
    ("Which planet is known as the Red Planet?", ["a) Venus", "b) Jupiter", "c) Saturn", "d) Mars"], "d"),
    ("What does HTML stand for?", ["a) HyperText Markup Language", "b) HighText Machine Language", "c) HyperText Markdown Language", "d) None of these"], "a"),
    ("Which data structure uses first-in, first-out?", ["a) Stack", "b) Queue", "c) Tree", "d) Graph"], "b"),
]

def run(answers=None):
    score = 0
    for i, (q, options, correct) in enumerate(QUESTIONS, 1):
        print(f"\nQ{i}. {q}")
        print("\n".join(options))
        ans = (answers[i-1] if answers is not None else input("Your answer (a/b/c/d): ")).strip().lower()
        if ans == correct: print("Correct!"); score += 1
        else: print(f"Wrong - the answer was {correct}.")
    print(f"\nYour score: {score}/{len(QUESTIONS)}")
    return score

def main():
    p = argparse.ArgumentParser(description="Quiz App")
    p.add_argument("--answers", help="Comma-separated answers, e.g. b,c,b,d,a,b (non-interactive)")
    args = p.parse_args()
    run(args.answers.split(",") if args.answers else None)

if __name__ == "__main__":
    main()
