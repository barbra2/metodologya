import random

GAME_RULES = "What number is missing in the progression?"


def generate_geometric_progression(start, ratio, length):
    return [start * (ratio ** i) for i in range(length)]


def generate_question():
    start = random.randint(1, 10)
    ratio = random.randint(2, 5)
    length = random.randint(5, 10)
    progression = generate_geometric_progression(start, ratio, length)
    hidden_index = random.randint(0, length - 1)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = ".."
    question = " ".join(map(str, progression))
    return question, correct_answer