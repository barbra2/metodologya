import random


def generate_geometric_progression(start, ratio, length):

    """Генерирует геометрическую прогрессию."""
    return [start * (ratio ** i) for i in range(length)]


def hide_element(progression, index):

    """Скрывает элемент прогрессии по указанному индексу."""
    progression[index] = '..'
    return progression


def play_game():

    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("What number is missing in the progression?")
    
    correct_answers = 0
    while correct_answers < 3:
        # Генерируем случайные параметры прогрессии
        start = random.randint(1, 10)
        ratio = random.randint(2, 5)
        length = random.randint(5, 10)
        
        # Создаем прогрессию
        progression = generate_geometric_progression(start, ratio, length)
        
        # Выбираем случайный индекс для скрытия
        hidden_index = random.randint(0, length - 1)
        correct_answer = progression[hidden_index]
        
        # Скрываем элемент
        progression_with_hidden = hide_element(progression.copy(), hidden_index)
        
        # Показываем вопрос
        print(f"Question: {' '.join(map(str, progression_with_hidden))}")
        user_answer = int(input("Your answer: "))
        
        # Проверяем ответ
        if user_answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return
    
    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    play_game()