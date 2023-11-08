import math
import time
from Functions import *

max_limit = 1000
closest_estimate = 3
places_correct_to = 0
new_closest_estimate = closest_estimate
percentage_improvement = 1
start_time = time.time()


# Example usage
numbers = list(range(1, max_limit + 1))
prime_numbers = find_prime_numbers(numbers)

while percentage_improvement >= 1 / max_limit:
    for n in prime_numbers:
        for m in prime_numbers:
            new_estimate = n / m
            pi_difference = abs(math.pi - new_estimate)

            if abs(math.pi - closest_estimate) > pi_difference:
                new_closest_estimate = new_estimate
                percentage_improvement = abs((1 - closest_estimate / math.pi) - (1 - (new_estimate / math.pi)))

                print(
                    f"New best estimate is {n} / {m} ({new_closest_estimate}) - {percentage_improvement:.10f}% improvement compared to {closest_estimate:.10f}")

                closest_estimate = new_closest_estimate
                best_n = n
                best_m = m

                for p in range(1, len(str(math.pi)) - 2):  # maximum decimal places stored for pi in Python
                    if truncate(math.pi, p) == truncate(new_closest_estimate, p):
                        places_correct_to = p

                print(f"    This is now accurate to {places_correct_to} decimal places.")
    print(f"{n} and {m} checked")

end_time = time.time()
duration = end_time - start_time

print(
    f"It took {duration:.6f} seconds to find the best rational estimate for pi using prime numbers up to {max_limit} which was {best_n}/{best_m}.")
