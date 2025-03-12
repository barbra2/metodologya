import math
import random

GAME_RULES = "Find the smallest common multiple of given numbers."


def gcd(a, b):
    return math.gcd(a, b)


def lcm(a, b):
    return a * b // gcd(a, b)


def lcm_three(a, b, c):
    return lcm(lcm(a, b), c)


def generate_question():
    numbers = [random.randint(1, 100) for _ in range(3)]
    correct_answer = lcm_three(*numbers)
    question = " ".join(map(str, numbers))
    return question, correct_answer