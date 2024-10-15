"""
Write a program to print the given list in reverse order.
Sample Input:
10 20 30 40 50 
"""
input_list = input("Enter the elements separated by space: ").split()
reversed_list = input_list[::-1]
print("Reversed list:", ' '.join(reversed_list))
