# text_analyzer.py
def analyze_text(text):
    words = text.split()
    word_count = len(words)
    char_count = len(text)
    avg_word_length = char_count / word_count if word_count > 0 else 0

    return word_count, char_count, avg_word_length

if __name__ == "__main__":
    input_text = input("Enter some text to analyze: ")
    word_count, char_count, avg_word_length = analyze_text(input_text)
    print(f"Word Count: {word_count}")
    print(f"Character Count: {char_count}")
    print(f"Average Word Length: {avg_word_length:.2f}")
