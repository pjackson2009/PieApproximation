import time
import math


# Prime Numbers
def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    max_divisor = int(num ** 0.5) + 1
    for i in range(3, max_divisor, 2):
        if num % i == 0:
            return False
    return True


def find_prime_numbers(max_limit):
    prime_numbers = [2]  # Start with 2 as the only even prime
    for num in range(3, max_limit + 1, 2):
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers


# Triangle Numbers
def generate_triangle_numbers(max_limit):
    triangle_numbers = []
    total = 0

    for number in range(1, max_limit + 1):
        total += number  # Add the next natural number to the total
        if total > max_limit:
            break
        else:
            triangle_numbers.append(total)

    return triangle_numbers


# Square Numbers
def generate_square_numbers(max_limit):
    square_numbers = []

    for number in range(1, int((max_limit + 1) ** 0.5)):
        square_number = number ** 2
        square_numbers.append(square_number)

    return square_numbers


# Square Root Numbers
def generate_square_root_numbers(max_limit):
    square_root_numbers = []

    for number in range(1, max_limit + 1):
        square_root_number = number ** 0.5
        if square_root_number <= max_limit + 1:
            square_root_numbers.append(square_root_number)

    return square_root_numbers


# Cube Numbers
def generate_cube_numbers(max_limit):
    cube_numbers = []

    for number in range(1, int((max_limit + 1) ** (1 / 3))):
        cube_number = number ** 3
        cube_numbers.append(cube_number)

    return cube_numbers


def calculate_pi_estimate(max_limit, numbers_to_check):
    places_correct_to = 0
    closest_estimate = 3
    new_closest_estimate = closest_estimate
    percentage_improvement = 1
    items_checked = 0
    best_n = 0
    best_m = 0

    start_time = time.time()

    for n in numbers_to_check:
        for m in numbers_to_check:
            new_estimate = n / m
            pi_difference = abs(math.pi - new_estimate)

            if pi_difference < abs(math.pi - closest_estimate):
                new_closest_estimate = new_estimate
                percentage_improvement = abs((1 - closest_estimate / math.pi) - (1 - (new_estimate / math.pi)))
                closest_estimate = new_closest_estimate
                best_n = n
                best_m = m

        items_checked += 1

    end_time = time.time()
    duration = end_time - start_time

    for p in range(1, len(str(math.pi)) - 2):  # maximum decimal places stored for pi in Python
        if round(math.pi, p) == round(new_closest_estimate, p):
            places_correct_to = p

    return best_n, best_m, new_closest_estimate, duration, places_correct_to
