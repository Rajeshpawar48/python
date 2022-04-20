#PRAC1
#PROGRAM ON 1D ARRAY
'''
def sum(arr):
    sum=0
    for i in arr:
        sum=sum+i
    return(sum)
arr=[]
arr=[10,20,30,40,50]
n=len(arr)
ans=sum(arr)
print("Sum of array is:",ans)

#Program on 1D array[Searching an element]
x=['p','y','t','h','o','n']
print(x.index('o'))
x=[5,1,7,0,3,4]
print(x.index(7))

#program on 2d array{to find sum of rows and columns elements prsent in an array}
n=int(input("Enter Number of rows:"))
m=int(input("Enter Number of columns:"))
matrix=[]
print("Enter values in matrix")
for i in range(n):
      data=[]
      for j in range(m):
          data.append(int(input()))
      matrix.append(data)
for i in range(n):
    for j in range(m):
        print(matrix[i][j],end=" ")
    print()
for i in range(n):
    sum=0
    for j in range(m):
        sum=sum+matrix[i][j]
    print("Sum of rows",i+1,":",sum)
for i in range(m):
      sum=0
      for j in range(n):
          sum=sum+matrix[j][i]
      print("Sum of columns",i+1,":",sum)
      
#PRAC2
#Program on 2d array {Sum of diagobal elements}
MAX=100
def printDiagonalSums(mat,n):
    principal=0
    secondary=0
    for i in range(0,n):
        for j in range(0,n):
            if(i==j):
                principal=principal+mat[i][j]
            if ((i+j)==(n-1)):
                secondary=secondary+mat[i][j]
    print("Pricipal Diagonal:",principal)
    print("Secondary Diagonal:",secondary)

a=[[1,2,3,4],
  [5,6,7,8],
  [1,2,3,4],
  [5,6,7,8]]
printDiagonalSums(a,4)

#Program for Multiplication of 2 matrices
# Program to multiply two matrices (vectorized implementation)

# Program to multiply two matrices (vectorized implementation)
import numpy as np
# take a 3x3 matrix
A = [[12, 7, 3],
	[4, 5, 6],
	[7, 8, 9]]

# take a 3x4 matrix
B = [[5, 8, 1, 2],
	[6, 7, 3, 0],
	[4, 5, 9, 1]]

# result will be 3x4

result= [[0,0,0,0],
		[0,0,0,0],
		[0,0,0,0]]

result = np.dot(A,B)

for r in result:
	print(r)


# Program to add two matrices using nested loop

X = [[1,2,3],
	[4 ,5,6],
	[7 ,8,9]]

Y = [[9,8,7],
	[6,5,4],
	[3,2,1]]


result = [[0,0,0],
		[0,0,0],
		[0,0,0]]

# iterate through rows
for i in range(len(X)):
# iterate through columns
	for j in range(len(X[0])):
		result[i][j] = X[i][j] + Y[i][j]

for r in result:
	print(r)

PRAC 3
#Program to create list based stack and perform various stack operations.
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:
    def __init__(self):
        self.head=None

    def push(self,data):
        if self.head is None:
            self.head=Node(data)
        else:
            new_node=Node(data)
            new_node.next=self.head
            self.head=new_node
    def pop(self):
        if self.head is None:
            return None
        else:
            popped=self.head.data
            self.head=self.head.next
            return popped
s=Stack()
while True:
    print('push<value>')
    print('pop')
    print('quit')
    do=input('What would you like to do?').split()
    operation=do[0].strip().lower()
    if operation =='push':
        s.push(int(do[1]))
    elif operation =='pop':
        popped=s.pop()
        if popped is None:
            print("stack is empty")
        else:
            print("popped value:",int(popped))
    elif operation=="quit":
        break

#Prac 4
##4A:LINEAR SEARCH=

def LinearSearch(array,n,k):
    for j in range(0,n):
        if (array[j]==k):
            return j
            return -1
array=[1,3,5,7,9]
k=7
n=len(array)
result=LinearSearch(array,n,k)
if(result == -1):
        print("Element not found")
else:
        print("Element found at index:",result)


##4B-BINARY SEARCH

def BinarySearch(arr,k,low,high):
    if high>=low:
        mid=low+(high-low)//2
        if arr[mid]==k:
            return mid
        elif arr[mid]>k:
            return BinarySearch(arr,k,low,mid-1)
        else:
            return BinarySearch(arr,k,mid+1,high)
    else:
        return -1
arr=[1,3,5,7,9,15,16,14,45]
k=15
result=BinarySearch(arr,k,0,len(arr)-1)
if result!=-1:
    print("Element is present at index:"+ str(result))
else:
    print("NOT FOUND")


#PRAC 5  
##PROGRAM 5-A:BUBBLE SORT

def bubble_sort(list1):
    for i in range(0,len(list1)-1):
        for j in range(len(list1)-1):
            if(list1[j]>list1[j+1]):
                temp=list1[j]
                list1[j]=list1[j+1]
                list1[j+1]=temp
    return list1
list1=[5,3,8,6,7,2]
print("The unsorted list is:",list1)
print("The sorted list is:",bubble_sort(list1))

#Insertion Sort
def InsertionSort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key

arr=[12,11,13,5,6]
InsertionSort(arr)
for i in range(len(arr)):
    print("%d"%arr[i])

#Selection Sort

# Selection sort in Python


def selectionSort(array, size):
   
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
         
            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i
         
        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])


data = [-2, 45, 0, 11, -9]
size = len(data)
selectionSort(data, size)
print('Sorted Array in Ascending Order:')
print(data)

    

#PRAC 6
##Program to select the Nth Max/Min element in the list by using an algorithm
class pair:
    def __init__(self):
        self.min=0
        self.max=0
def getMinMax(arr:list,n:int)-> pair:
        minmax=pair()
        if n==1:
            minmax.max=arr[0]
            minmax.min=arr[1]
            return minmax
        if arr[0] > arr[1]:
            minmax.max=arr[0]
            minmax.min=arr[1]
        else:
            minmax.max=arr[1]
            minmax.min=arr[0]
        for i in range(2,n):
            if arr[i] > minmax.max:
                minmax.max=arr[i]
            elif arr[i] < minmax.min:
                minmax.min=arr[i]
        return minmax
if __name__=="__main__":
    arr=[1000,11,445,1,330,3000]
    arr_size=6
    minmax=getMinMax(arr,arr_size)
    print("MINIMUM ELEMENT IS ",minmax.min)
    print("MAXIMUM ELEMENT IS",minmax.max)
'''

#Prac 7
#7A:Program to find a pattern in general way
'''
def search(pat,txt):
    M=len(pat)
    N=len(txt)
    for i in range(N-M+1):
        j=0
        while(j<M):
            if (txt[i+j]!=pat[j]):
                break
            j=j+1
        if(j==M):
            print("Pattern found at y index",i)
if __name__=="__main__":
    txt="AABAACAADAABAAABAA"
    pat="AABA"
    search(pat,txt)
'''
#7B:Program to find a pattern by Brute force tecnique
'''
def linear_search(lst,match):
    for idx in range(len(lst)):
        if lst[idx]==match:
            return idx
        else:
            raise ValueError("{0} NOT IN LIST".format(match))
recipe=["nori","tuna","soy sauce","sushi rice"]
ingredient="avocado"
try:
    print(linear_search(recipe,ingredient))
except ValueError as msg:
    print("{0}".format(msg))
'''



#PRAC8
            #8A Recursion Factorial 
'''
def factorial(n):
    if(n==1 or n==0):
        return 1
    else:
        return(n*factorial(n-1))
num=5;
print("Number",num)
print("Factorial: ",factorial(num))
'''

        #8B Recursion fibonacci
'''
def recur_fibo(n):
    if n<=1:
        return n
    else:
        return (recur_fibo(n-1)+ recur_fibo(n-2))
nterms =10
if nterms<=0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence: ")
for i in range(nterms):
    print(recur_fibo(i))
'''

        #8C Recursion Tower of Hanoi
'''
def TowOfHan(n,source,destination,auxilliary):
    if n==1:
        print("Move disk 1 from source",source,"to destination",destination)
        return

    TowOfHan(n-1,source,auxilliary,destination)
    print("Move disk",n,"from source",source,"to destination",destination)
    TowOfHan(n-1,auxilliary,destination,source)
n=4
TowOfHan(n,'A','B','C')

'''


'''    
PRAC 9          
#Write any one program to implement greedy apporach like: Counting Coins 
def findMin(V):
      
    # All denominations of Indian Currency
    deno = [1, 2, 5, 10, 20, 50, 
            100, 500, 1000]
    n = len(deno)
      
    # Initialize Result
    ans = []
  
    # Traverse through all denomination
    i = n - 1
    while(i >= 0):
          
        # Find denominations
        while (V >= deno[i]):
            V -= deno[i]
            ans.append(deno[i])
  
        i -= 1
  
    # Print result
    for i in range(len(ans)):
        print(ans[i], end = " ")
  
# Driver Code
if __name__ == '__main__':
    n = 93
    print("Following is minimal number",
          "of change for", n, ": ", end = "")
    findMin(n)
'''



#PRAC 10
'''
# MergeSort in Python


def mergeSort(array):
    if len(array) > 1:

        #  r is the point where the array is divided into two subarrays
        r = len(array)//2
        L = array[:r]
        M = array[r:]

        # Sort the two halves
        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1


# Print the array
def printList(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()


# Driver program
if __name__ == '__main__':
    array = [2, 5, 16, 10, 20, 1]
    mergeSort(array)
    print("Sorted array is: ")
    printList(array)
'''












