"""
Write a Program to find the search element in the given list
Input & Output Format:
Input consists of one list and one integer.
First input consists of a size of a list.
Second inputs corresponds to the elements of list in single line separated by space.
Third input consists of the element which we need to search
Sample Input 1:
5
1 2 3 6 5
3
Sample Output 1:
3 is present in the given list
Sample Input 2:
5
1 2 3 6 5
4
"""
n = int(input("Enter the size of the list: "))
elements = list(map(int, input("Enter the elements separated by space: ").split()))
search_element = int(input("Enter the element to search: "))
if search_element in elements:
    print(f"{search_element} is present in the given list")
else:
    print(f"{search_element} is not present in the given list")
