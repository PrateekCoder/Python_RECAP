'''
You are given  numbers. Store them in a list and find the second largest number.

Input Format
The first line contains . The second line contains an array [] of  integers each separated by a space.

Constraints


Output Format
Output the value of the second largest number.

Sample Input

5
2 3 6 6 5
Sample Output

5
'''

n = int(input())                            #Takes the value of number of inputs you want.
arr = input()                               #All the inputs are stored in an array arr.
l = list(map(int,arr.split(' ')))           #All the inputs in the arr are then stored in l as list and as an int.
c = max(l)                                  #Using the max() function we find out the maximum value in the list l.
while max(l) == c:                          #Using this loop we check if there is any other value in the list which is same as the maximum value.
    l.remove(max(l))                        #If there is any other value in the list same as the the largest one, we remove it.

print(max(l))                               # After performing all the above operation, max value from the list has been removed, and the second largest value is now the max value in the list so we just print the value the max value.
