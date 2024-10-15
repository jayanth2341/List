"""
Write a program to sort the given list and print it.
Sample Input:
30 20 10 50 40
"""
input_list = input("Enter the elements separated by space: ").split()
number_list = [int(num) for num in input_list]
sorted_list = sorted(number_list)
print("Sorted list:", ' '.join(map(str, sorted_list)))
