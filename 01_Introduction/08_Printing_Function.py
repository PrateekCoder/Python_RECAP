'''
Read an integer .

Without using any string methods, try to print the following:


Note that "" represents the values in between.

Input Format
The first line contains an integer .

Output Format
Output the answer as explained in the task.

Sample Input

3
Sample Output

123
Tip
You can use the print function inside a map(). Can you write a  line code to solve the problem above?
'''

n = int(input())
for i in range(1, n+1):
    print(i, sep="", end="") # The sep="" helps and giving no spaces between the integers and end="" helps in printing all the integers on the same line.
