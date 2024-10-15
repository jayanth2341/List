"""
Write a Python Program to find the largest number in a list
Input & Output Format:
Input consists of one list and one integer.
First input consists of a size of a list.
Second inputs corresponds to the size of the list.
Output consists of the largest element.
Sample Input:
5
1
2
3
6
5
"""
n = int(input("Enter the size of the list: "))
elements = []
for _ in range(n):
    element = int(input("Enter an element: "))
    elements.append(element)
largest_element = max(elements)
print("The largest element is:", largest_element)
