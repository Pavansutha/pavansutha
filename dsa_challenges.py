def filter_and_sort_evens(numbers):
    """
    Takes a list of integers and returns a sorted list of even numbers.
    """
    evens = [num for num in numbers if num % 2 == 0]
    return sorted(evens)


def count_character_frequency(text):
    """
    Takes a string and returns a dictionary with character frequencies (case-insensitive).
    """
    freq = {}
    for char in text.lower():
        freq[char] = freq.get(char, 0) + 1
    return freq


# Example calls
if __name__ == "__main__":
    print(filter_and_sort_evens([3, 1, 4, 1, 5, 9, 2, 6]))  # Output: [2, 4, 6]
    
    sample_text = "Hello World"
    print(count_character_frequency(sample_text))
    # Output: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
