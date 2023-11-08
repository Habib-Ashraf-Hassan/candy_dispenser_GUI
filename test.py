def insert_in_descending_order(lst, k):
    # Check if k is a number
    if not isinstance(k, (int, float)):
        return lst  # If k is not a number, do nothing

    # Iterate through the list
    for i in range(len(lst)):
        # Check if the current element is a number
        if isinstance(lst[i], (int, float)):
            # Compare k with the current element
            if k > lst[i]:
                lst.insert(i, k)  # Insert k before the current element
                return lst
    # If k is not smaller than any number in the list, append it to the end
    lst.append(k)
    return lst

# Example usage:
my_list = [5, 4, 3, "apple", 2, 1]
k = 3.5
result = insert_in_descending_order(my_list, k)
print(result)
