from random import randint


def generate_numbers(n):
    numbers = []
    while len(numbers) < n:
        new_number = randint(1, 45)
        if new_number not in numbers:
            numbers.append(new_number)
    return numbers
    


print(generate_numbers(7)) # 확인용

        
    # 코드를 작성하세요.