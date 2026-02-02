from typing import Callable

def generator_numbers(text: str):
    for char in text.split()[1:-1]:
        try:
            yield float(char.strip()) 
        except ValueError:
            continue
                

def sum_profit(text: str, func: Callable):
    sum_number = 0
    
    for num in func(text):
        sum_number += num
    return sum_number

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")