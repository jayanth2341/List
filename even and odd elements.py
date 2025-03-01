"""
Write a Python Program to put the even and odd elements in a list into two different lists.
Input format:
Input consists of one integer and one list.
First input consists of the size of the list.
Second input consists of the elements based on the size.
Output format:
Output consists of two lists.
First list consists of all the even numbers in the list.
Second list consists of all the odd numbers in the list.
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
even_list = []
odd_list = []
for number in elements:
    if number % 2 == 0:
        even_list.append(number)
    else:
        odd_list.append(number)
print("Even numbers:", even_list)
print("Odd numbers:", odd_list)
