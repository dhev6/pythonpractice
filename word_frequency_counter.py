import string

def word_frequency_counter():
    print("\nWord frequency counter")
    user_input = input("Enter a sentence or paragraph:\n")

    if not user_input.strip():
        print("No text entered.")
        return

    cleaned_text = ""
    for char in user_input:
        if char not in string.punctuation:
            cleaned_text += char.lower()
        else:
            cleaned_text += " "

    words = cleaned_text.split()


    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
        
    sorted_freq = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

    print("\n--- Word Counts ---")
    print(f"{'Word':<15} | {'Frequency':<10}")
    print("-" * 28)
    
    for word, count in sorted_freq:
        print(f"{word:<15} | {count:<10}")


word_frequency_counter()