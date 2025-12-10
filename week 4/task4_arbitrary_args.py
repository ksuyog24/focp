
print("\n--- Task 4 ---")

def calcAve(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)

print(calcAve(10, 20, 30))
