'''
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the types listed above. Iterate through each command in order and perform the corresponding operation on your list.

Input Format

The first line contains an integer, , denoting the number of commands.
Each line  of the  subsequent lines contains one of the commands described above.

Constraints

The elements added to the list must be integers.
Output Format

For each command of type print, print the list on a new line.

Sample Input

12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
Sample Output

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]

'''
n = int(input())                                           #Takes the value of n, which is number of operations you want to perform on the list.
l = []                                                     #Variable l is defined to store all the values, or operations being performed through the process.
for i in range(n):                                         #A for loop to iterate through the value of n and take n inputs.
    s = input().split()                                    #Takes the input command by the user for every single command and split the command using split()
    cmd = s[0]                                             #The first character of the string after splitting is going to be the command like: insert, or print, or sort, so that is stored in variable cmd.
    args = s[1:]                                           #All the characters after the command are going to be the agruments so we store them in args variable.
    if cmd !="print":                                      #If the value of command is not euqual to print, we perform this conditional statement.
        cmd += "("+ ",".join(args) +")"                    #We join the arguments and store it in the cmd.
        eval("l."+cmd)                                     #Then we eval the command and store the avaluated value.
    else:
        print (l)                                          #And when we encounter the print statement in the cmd, we print out the result whatever is being stored after performing the eval fucntion.
