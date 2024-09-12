# number_to_words.py
def number_to_words(n):
    ones = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens = ["Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

    if 0 <= n < 10:
        return ones[n]
    elif 10 <= n < 20:
        return teens[n - 10]
    elif 20 <= n < 100:
        return tens[n // 10 - 2] + ('' if n % 10 == 0 else '-' + ones[n % 10])
    else:
        return "Number out of range"

if __name__ == "__main__":
    number = int(input("Enter a number between 0 and 99: "))
    print(f"Number in words: {number_to_words(number)}")
