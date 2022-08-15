#prime no bw 100 and 200
for num in range(100,200):
    if all(num%i !=0 for i in range(2,num)):
        print(num)


""" sort function to sort a list
l = [56,89,2,4,5,1,90,345,234]
l.sort(reverse= False)
print(l)
"""

""" write sorting function without using list.sort (descending)
l = [56,89,2,4,5,1,90,345,234]
new_list=[]
while l:
    minimum=l[0]
    for x in l:
        if x > minimum:
            minimum = x
    new_list.append(minimum)
    l.remove(minimum)cl
print(new_list)
"""

""" to print fibonacci series
def F(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return F(n-1) + F(n-2)
for i in range(0,7):
    print(F(i))
"""

""" to print a list in reverse (no need to sort just reverse)
list = [56,89,2,4,5,1,90,345,234]

def rev(l):
    return l[::-1]

print(rev(list))
"""

""" to check whether a string is palindrome or not
def isPalindrome(s):
    #using predefined fun to reverse string or we can use rev=s[::-1]
    rev = ''.join(reversed(s))
    
    if s == rev:
        return True
    return False

ans=isPalindrome("malayalam")
if(ans):
    print("yes")
else:
    print("No")
"""

""" to print set of duplicates in a list
list = [1,3,4,6,8,8,1,2,29,3]
print(set([x for x in list if list.count(x)>1]))
"""

""" to print no of words in a given sentence
s = "My name is Sirigireddy Siva Pradeep Reddy"
print(len(s.split()))
"""

""" program for linear search   time complexity for linear search  = O(n)
# Given an array arr[] of n elements, program to search element x in arr[]
def search(arr,x):
    for i in range(len(arr)):
        if (arr[i] == x):
            return i
    return -1

l = [1,2,3,4,5,5,5,8]
result = search(l,15)
if(result == -1):
    print("Element is not present in array")
else:
    print("Element is present at index", result)
"""

""" program for recursive binary search, time complexity for linear search  = O(Log n)
# Returns index of x in arr if present, else -1
def binarySearch (arr, lower, upper, x):
 
    # Check base case
    if upper >= lower:
 
        mid = lower + (upper - lower) // 2
 
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
         
        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, lower, mid-1, x)
 
        # Else the element can only be present
        # in right subarray
        else:
            return binarySearch(arr, mid + 1, upper, x)
 
    else:
        # Element is not present in the array
        return -1
 
arr = [ 2, 3, 4, 10, 40 ]
x = 3
 
result = binarySearch(arr, 0, len(arr)-1, x)
 
if result != -1:
    print ("Element is present at index % d" % result)
else:
    print ("Element is not present in array")
"""

"""import pandas as pd"""
