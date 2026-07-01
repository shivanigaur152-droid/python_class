#Q1. Python Program to Find the Sum of All Elements in a List.

# list=[10, 20, 30,40, 50]
# s=0
# for i in list:
#     s+=i
# print(s)

#O2.Write a Python program to display the odd and even elements from the list.

# numbers = [10, 23, 11, 12, 33, 44, 2, 5, 6]

# even = []
# odd = []

# for num in numbers:
#     if num % 2 == 0:
#         even.append(num)
#     else:
#         odd.append(num)

# print("Even elements:", even)
# print("Odd elements:", odd)


#Q3. Python Program to Count Odd and Even Numbers in a List

# numbers = [10, 23, 11, 12, 33, 44, 2, 5, 6]

# even_count = len([num for num in numbers if num % 2 == 0])
# odd_count = len([num for num in numbers if num % 2 != 0])

# print("Number of even elements:", even_count)
# print("Number of odd elements:", odd_count)


#Q4. Python Program to Interchange the First and Last Elements of a List

# list=[10,23, 11, 12, 33, 44, 2, 5, 6]
# temp=list[0]
# list[0]=list[-1]
# list[-1]=temp
# print(list)


#Q5.Python program to duplicate all the items in the list

# li = [1, 2, 3]
# print(li*len(li))

#Q6. Find the smallest element in the list.

# numbers = [10, 23, 11, 12, 33, 44, 2, 5, 6]
# smallest= min(numbers)
# print("list:", numbers)
# print("smallest element:", smallest)

#Q7. Find the greatest element in the list.

# numbers=[10,23,11,12,33,44,2,5,6]
# greatest= max(numbers)
# print("list:", numbers)
# print("greatest element:",greatest)

#Q8.  Find the repetitive elements in the list.

# list=[1,2,3,4,56,1,22,23,33,23,56]
# l=[]
# l1=[]
# for i in list:
#     if i not in l:
#         l.append(i)
#     else:
#         l1.append(i)
# print("repetitive elements are:",l1)

#Q9. Remove all the odd elements from the list.

# list=[10,23,11,12,33,44,2,5,6]
# for i in list[:]:
#   if i%2!=0:
#     list.remove(i)
# print(list)

# Q10. Find all non-repetitive elements in the list.

# list=[1,2,3,4,56,1,22,23,33,23,56]
# l=[]
# l1=[]
# for i in list:
#   if i not in l:
#     l.append(i)
#   else:
#     l1.append(i)
# res=[i for i in l if i not in l1]
# print("non repetitive elements are:",res)

# Q11. Python program to duplicate all items in the list

# li=[1,2,3]
# print(li*len(li))

# Q12. Find the second greatest element in the list

# l=[89, 23, 24, 2, 55, 54, 64]
# for i in range(len(l)):
#     m=l[i]
#     for j in range(i+1,len(l)):
#         if l[j]>l[i]:
#             l[i],l[j]=l[j],l[i]
#     if i==2:
#         break
# print("second greatest element is",l[1])

# Q13. Reverse the list [1, 2, 3, 4, 56, 1, 22, 23, 33, 23, 56].
# l=[1, 2, 3, 4, 56, 1, 22, 23, 33, 23, 56]
# l1=[]
# for i in range(len(l)-1,-1,-1):
#   l1.append(l[i])
# print(l1)

# Q14. Arrange the list [1, 2, 3, 4, 56, 1, 22, 23, 33, 23, 56] in ascending order.
# numbers=[1, 2, 3, 4, 56, 1, 22, 23, 33, 23, 56]
# numbers.sort()
# print("list in ascending order:")
# print(numbers)

# Q15. Arrange the list in descending order.
# l=[1, 2, 3, 4, 56, 1, 22, 23, 33, 23, 56]
# l.sort(reverse=True)
# print("list in descending order:")
# print(l)

# Q16. Write a Python program to print all the vowels present in the given list of strings ["Dreamer", "infotech"].
# l=["Dreamer", "infotech"]
# a="".join(l)
# res=""
# for i in a:
#     if i in "AEIOUaeiou":
#         res+=i
# print(res)

# Q17. Write a Python program to take input from the user to create a list of elements. The user should input each element of the list one by one. Create a list with these elements (maximum of 5 elements).
# l=[]
# n=int(input("enter no of elements you want to insert into the list:"))
# for i in range(n):
#     l.append(int(input()))
# print(l)

# Q18. Write a Python program to generate a list of numbers in reverse order from 10 to 1 using list comprehension

# res=[i for i in range(10,0,-1)]
# print(res)

# Q19. Create a list of square numbers from 1 to 10 using list comprehension.

# res=[i**2 for i in range(1,11)]
# print(res)

# Q20. Create a list of even numbers from 1 to 10 using list comprehension
# res=[i for i in range(1,11) if i%2==0]
# print(res)

# Q21. Filter strings from the list language 
# language = ['python', 'php', 'java', 'c++', 'javascript', 'ruby']
# ch=input("enter the char:")
# l=[]
# for i in language:
#   if ch in i:
#     l.append(i)
# print(l)

# Q22. Flatten a nested list like [[1,2], [3,4], [5,6]] into a single list.
# l=[[1,2], [3,4], [5,6]]
# l1=[]
# for i in range(len(l)):
#     for j in range(len(l[i])):
#         l1.append(l[i][j])
# print(l1)

# Q23.Find the frequency of each element in a list.
# l=[1, 2, 2, 3, 4, 1, 5, 2]
# l1=[]
# for i in range(len(l)):
#     count=1
#     if l[i] not in l1:
#         for j in range(i+1,len(l)):
#             if l[i]==l[j]:
#                 count+=1
#         l1.append(l[i])
#         print(l[i],"-->",count,"times")


# Q24. Check whether a given list is a palindrome.
# l=[1, 2, 3, 2, 1]
# a=l[::-1]
# if a==1:
#   print("palindrome")
# else:
#   print("not palindrome")

# Q25. Find the longest string in a list of strings.
# l=["cat", "elephant", "dog", "hippopotamus"]
# a=len(l[0])
# l1=[]
# for word in l:
#     if len(word)>a:
#         l1.append(word)
# print(l1[-1])

# Q26.Count how many strings in a list start with a vowel.
# l=["apple", "banana", "orange", "umbrella", "grape", "ice"]
# l1=[]
# count=0
# for i in l:
#     if i[0] in "AEIOUaeiou":
#         count+=1
#         l1.append(i)
# print(f"{count} strings start with a vowel:",tuple(l1))

# Q27. Replace all negative numbers in a list with zero

# l=[5, -3, 7, -1, 0, -8, 4]
# l1=[]
# for i in l:
#   if i<0:
#     l1.append(0)
#   else:
#     l1.append(i)
# print(l1)


# Q28. Create a new list containing only prime numbers from a given list.

# l=[2,3,4,5,6,7,8,11,12,24,31]
# l1=[]
# for i  in l:
#     count=0
#     for j in range(2,i+1):
#         if i%j==0:
#             count+=1
#     if count==1:
#         l1.append(i)
# print(l1)


# Q29. Convert a list of integers into a single integer number (e.g., [1,2,3,4] → 1234).
l=[1,2,3,4]
a=''
for i in l:
  a+=str(i)
print(int(a))

# Q30.Group elements of a list based on even and odd indices.

# l=[2,3,4,5,6,7,8,11,12,24,31]
# l1=[]
# l2=[]
# for i in range(len(l)):
#   if i%2==0:
#     l1.append(l[i])
#   else:
#     l2.append(l[i])
# print("even indices elements are:",l1)
# print("odd indices element are:",l2)

# Q31.Find the largest even number in a list

# l=[2,3,4,5,6,7,8,11,12,24,31]
# m_even=float('-inf')
# for i in l:
#     if i%2==0:
#         if i>m_even:
#             m_even=i
# print("largest even number is:",m_even)

# Q32.Find the majority element in a list (an element that appears more than n/2 times).

# l=[2, 2, 1, 2, 3, 2, 2]
# l1=[]
# a=len(l)
# for i in range(len(l)):
#     count=1
#     if l[i] not in l1:
#         for j in range(i+1,len(l)):
#             if l[i]==l[j]:
#                 count+=1
#         l1.append(l[i])
#     if count>=a//2:
#         print(l[i])


# Q33.Find the difference between the maximum and minimum values in a list.

# l=[10, 4, 7, 2, 15, 6]
# a=max(l)
# b=min(l)
# print(a-b)


# Q34. Remove every third element from a list.

# l=[1, 2, 3, 4, 5, 6, 7, 8, 9]
# print([i for i in range(len(l)) if i%3!=0])

# Q35.Insert an element at every even index of a list.

# l=[1, 2, 3]
# n=int(input("enter an ele u want to insert:"))
# for i in range(len(l)):
#     if i%2==0:
#         l.insert(i,n)
# print(l)


# Q36.Rearrange a list so that positive and negative numbers alternate

# l=[1, 2, -3, -4, 5, -6]
# l1=[]
# l2=[]
# for i in l:
#     if i>0:
#         l1.append(i)
#     else:
#         l2.append(i)
# res=[]
# i=0
# j=0
# while(i<len(l1) and j<len(l2)):
#     res.append(l1[i])
#     res.append(l2[j])
#     i+=1
#     j+=1
# print(res)

# Q37. Find all pairs of elements in a list whose sum equals a given target number.

# l = [2, 4, 3, 5, 7, 8, 9]
# tar=int(input("enter your target numbers:"))
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]+l[j]==tar:
#             print(l[i],l[j])


# Q38.Find the Missing Number from a Sequence.
# l=[1, 2, 4, 5, 6]
# a=max(l)
# b=min(l)
# for i in range(b,a+1):
#   if i not in l:
#     print(i,end=" ")

# Q39. Split a List into Chunks of Size 3

# l=[1, 2, 3, 4, 5, 6, 7, 8, 9]
# l1=[l[i:i+3] for i in range(0,len(l),3)]
# print(l1)

# Q40. Reverse Each String in a List.

# l=["python","java","script"]
# l1=[]
# for i in l:
#   l1.append(i[::-1])
# print(l1)


# Q41.Extract All Digits from a List of Strings

# l=["abc123", "45def", "gh6"]
# l1=[]
# for i in l:
#     a=''
#     for j in i:
#         if j.isdigit():
#             a+=j
#     l1.append(a)
# print(l1)

# Q42..Find All Anagram Groups in a List of Words

# List of words
words = ["eat", "tea", "tan", "ate", "nat", "bat"]

anagram_groups = {}
for word in words:
    key = "".join(sorted(word))
    
    if key not in anagram_groups:
        anagram_groups[key] = []
    
    anagram_groups[key].append(word)

result = list(anagram_groups.values())

print( result)
print("han g thik ho na")