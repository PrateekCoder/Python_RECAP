'''
Task
Read an integer . For all non-negative integers , print . See the sample for details.

Input Format

The first and only line contains the integer, .

Constraints


Output Format

Print  lines, one corresponding to each .

Sample Input

5
Sample Output

0
1
4
9
16
'''

number = int(input())
if 1<=number<=20:
    for number in range(number):
        print(number*number)
