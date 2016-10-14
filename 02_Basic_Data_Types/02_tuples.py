'''
Task
Given an integer, , and  space-separated integers as input, create a tuple, , of those  integers. Then compute and print the result of .

Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.

Input Format

The first line contains an integer, , denoting the number of elements in the tuple.
The second line contains  space-separated integers describing the elements in tuple .

Output Format

Print the result of .

Sample Input:

2
1 2

Sample Output:

3713081631934410656
'''

n = int(input())                     #input the first line
second_line = input()                #input the second line
second_string = second_line.split()  #convert the second line into strings
for i in range(n):                   #loop to convert all the values in second string from string to int
    second_string[i] = int(second_string[i])
t = tuple(second_string)             #convert values stored in int form to tuple
print (hash(t))                      #convert the value of t into hash form and print
