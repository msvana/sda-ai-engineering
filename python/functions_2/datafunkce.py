def suma(numbers):
    total = 0
    for i in numbers:
        total += i
    return total

def mean(numbers):
    total = suma(numbers)
    result = total / len(numbers)
    return result

def center(numbers):
    numbers_centered = []
    numbers_mean = mean(numbers)
    for number in numbers:
        centered = number - numbers_mean
        numbers_centered.append(centered)
    return numbers_centered

revenues = [50000, 45000, 60000, 30000, 70000, 85000, 65000]
weekly_revenue = suma(revenues)
mean_revenue = mean(revenues)
print(f"Celkove trzby {weekly_revenue}")
print(f"Prumerne trzby {mean_revenue}")

simple_list = [1, 3, 5]
centered_list = center(simple_list)

assert centered_list == [-2, 0, 2]
print(centered_list)

