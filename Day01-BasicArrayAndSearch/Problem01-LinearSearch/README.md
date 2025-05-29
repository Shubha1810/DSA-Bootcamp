Problem Statement
Write a function that searches for a target value in an array of integers using linear search.

Approach / Thought Process
Take Input from User: Number of elements in the array (n)
                      Elements of the array one by one
                      The target value to search

Linear Search Function: Traverse the array from start to end.
                        Compare each element with the target.
                        If found, print the index and stop.
                        If not found, return -1.

Print the Result: Display the index if found.
                  If the result is -1, indicate that the target was not found.

Time & Space Complexity
Time Complexity:
Best Case: O(1) (if the target is the first element)
Worst Case: O(n) (if the target is at the end or not present)

Space Complexity: O(n)
Space is required to store n elements in the array.


Sample Inputs / Edge Cases
Sample Input 1:
Enter the number of elements in array: 5  
Enter the target value needed to search: 3  
Input elements: 1 2 3 4 5  

Output:
Index is  3  
[1, 2, 3, 4, 5]

Sample Input 2 (Edge Case - Element not present):
Enter the number of elements in array: 4  
Enter the target value needed to search: 10  
Input elements: 2 4 6 8  

Output:
Index -1  
[2, 4, 6, 8]
