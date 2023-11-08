from Functions import *


if __name__ == "__main__":
    while True:
        try:
            max_limit = int(input("What is the maximum integer you would like to check? "))
            break
        except ValueError:
            print("Please enter a valid integer.")

    valid_inputs = ['p', 't', 's', 'r', 'c', 'i']
    while True:
        number_type_to_check = input(
            "Would you like to check prime numbers (p), triangle numbers (t), square numbers (s), square root numbers (r), cube numbers (c), "
            "or integers (i)? ").lower()

        if number_type_to_check in valid_inputs:
            break
        else:
            print("Please enter a valid option: p, t, s, r, c, or i.")

    numbers = list(range(1, max_limit + 1))

    if number_type_to_check[0] == "p":
        numbers_to_check = find_prime_numbers(max_limit)
        number_type = "prime numbers"
    elif number_type_to_check[0] == "t":
        numbers_to_check = generate_triangle_numbers(max_limit)
        number_type = "triangle numbers"
    elif number_type_to_check[0] == "s":
        numbers_to_check = generate_square_numbers(max_limit)
        number_type = "square numbers"
    elif number_type_to_check[0] == "r":
        numbers_to_check = generate_square_root_numbers(max_limit)
        number_type = "square root numbers"
    elif number_type_to_check[0] == "c":
        numbers_to_check = generate_cube_numbers(max_limit)
        number_type = "cube numbers"
    elif number_type_to_check[0] == "i":
        numbers_to_check = numbers
        number_type = "integers"

    best_n, best_m, new_closest_estimate, duration, places_correct_to = calculate_pi_estimate(max_limit, numbers_to_check)

    print(f"The list of {number_type} checked is: {numbers_to_check}")
    print(f"New best estimate is {best_n} / {best_m} ({new_closest_estimate}) which is correct to {places_correct_to} decimal places.")
    print(f"It took {duration:.6f} seconds to find the best rational estimate for pi using {number_type} up to {max_limit} which was {best_n}/{best_m}.")