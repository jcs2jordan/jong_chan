# 로또 완성본

from random import randint


def generate_numbers(n):
    numbers = []
    while len(numbers) < n:
        new_number = randint(1, 45)
        if new_number not in numbers:
            numbers.append(new_number)
    return numbers


def draw_winning_numbers():
    # 코드를 작성하세요.
    winning_numbers = generate_numbers(7)
    return sorted(winning_numbers[:6]) + winning_numbers[6:]


def count_matching_numbers(list_1, list_2):
    # 코드를 작성하세요.

    same_numbers = list(set(list_1).intersection(list_2))
    return len(same_numbers)


def check(numbers, winning_numbers):
    # 코드를 작성하세요.
    if count_matching_numbers(numbers, winning_numbers[0:6]) == 6:
        return 100000000
    elif count_matching_numbers(numbers, winning_numbers[0:6]) == 5 and count_matching_numbers(numbers, winning_numbers[6:]) == 1:
        return 50000000
    elif count_matching_numbers(numbers, winning_numbers[0:6]) == 5:
        return 1000000
    elif count_matching_numbers(numbers, winning_numbers[0:6]) == 4:
        return 50000
    elif count_matching_numbers(numbers, winning_numbers[0:6]) == 3:
        return 5000
    else:

        return 0