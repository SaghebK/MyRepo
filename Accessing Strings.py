'''
Accessing Strings


You need to make a program that counts the number of vowels in a given text.
The vowels are a, e, i, o, and u.

Take a string as input and output the number of vowels.

Sample Input:
this is great

Sample Output:
4
'''
i=input()
count=0
ws=['a','e','i','o','u']
for w in i:
    if w in ws:
        count+=1
print(count)
