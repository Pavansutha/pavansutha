# File: dev_assessment/debug_errors.py

def calculate_average(numbers):
    """
    Calculates the average of a list of numbers.
    Returns 0 if the list is empty.
    """
    try:
        total = 0
        for i in range(len(numbers)):
            total += numbers[i]
        return total / len(numbers)
    except ZeroDivisionError:
        print("Warning: Empty list provided. Returning 0 as average.")
        return 0  # Graceful handling of empty list


def get_list_element(my_list, index):
    """
    Attempts to return the element at the specified index of my_list.
    Handles IndexError and TypeError gracefully.
    """
    try:
        return my_list[index]
    except IndexError:
        print(f"Error: Index {index} is out of bounds for the list.")
        return None
    except TypeError:
        print(f"Error: Provided input is not a list.")
        return None


# Test data for calculate_average
data1 = [10, 20, 30, 40, 50]
data2 = [5, 15]
data3 = []  # This will now be handled safely

print(f"Average of data1: {calculate_average(data1)}")
print(f"Average of data2: {calculate_average(data2)}")
print(f"Average of data3: {calculate_average(data3)}")

# Test cases for get_list_element
sample_list = [100, 200, 300]

print(f"Element at index 1: {get_list_element(sample_list, 1)}")      # valid
print(f"Element at index 5: {get_list_element(sample_list, 5)}")      # out-of-bounds
print(f"Element from wrong type: {get_list_element('not a list', 0)}")  # wrong type
