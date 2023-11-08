import math

max_range = 100000  # Adjust the maximum number of sides as needed
starting_sides = 3
accuracy_threshold = 1 / starting_sides

for i in range(starting_sides, max_range + 1):
    pi_sides_ratio = math.pi / i
    estimate = (2 * math.tan(pi_sides_ratio) / math.sqrt(4 * math.tan(pi_sides_ratio) / i)) ** 2
    difference_from_pi = abs(math.pi - estimate)
    accuracy = difference_from_pi / math.pi
    print(
        f"The estimate with {i} sides is {estimate}. Pi difference = {difference_from_pi}, accuracy = {accuracy}, accuracy threshold = {accuracy_threshold}")
    accuracy_threshold = 0.1 ** 6

    if accuracy < accuracy_threshold:
        break
