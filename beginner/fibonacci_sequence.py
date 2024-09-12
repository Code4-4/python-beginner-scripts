# fibonacci_sequence.py
def fibonacci(n):
    a, b = 0, 1
    sequence = []
    while a < n:
        sequence.append(a)
        a, b = b, a + b
    return sequence

if __name__ == "__main__":
    num = int(input("Generate Fibonacci sequence up to: "))
    print(f"Fibonacci sequence up to {num}: {fibonacci(num)}")
