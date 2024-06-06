from typing import List


def process_numbers(numbers: List[int]) -> List[int]:
    return [x * 2 for x in numbers]


my_numbers = [1, 2, 3, 4, 5]
doubled_numbers = process_numbers(my_numbers)
print(doubled_numbers)
