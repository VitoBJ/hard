import random

def find_pairs(first_number):
    pairs = []
    for i in range(2, 21):
        for j in range(2, 21):
            if i != first_number and j != first_number:
                pair_sum = i + j
                if pair_sum != 0 and first_number % pair_sum == 0:
                    pairs.append((i, j))
    return pairs
first_number = random.randint(3, 20)
print(f"Первое число: {first_number}")
result = find_pairs(first_number)
print("Пары чисел, сумма которых делит первое число:")
for pair in result:
    print(pair)