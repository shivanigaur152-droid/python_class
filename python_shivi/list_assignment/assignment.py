# 1.sum of all elements
# numbers = [10, 20, 30, 40, 50]
# total = 0

# for i in numbers:
#     total = total + i

# print("Sum of all elements:", total)

# 2.display the odd and even element.
# numbers = [10, 23, 11, 12, 33, 44, 2, 5, 6]

# print("Even:")
# for i in numbers:
#     if i % 2 == 0:
#         print(i, end=" ")

# print("Odd:")
# for i in numbers:
#     if i % 2 != 0:
#         print(i, end=" ")

# 3.count the even and odd numbers
# numbers = [10, 23, 11, 12, 33, 44, 2, 5, 6]

# even = 0
# odd = 0

# for i in numbers:
#     if i % 2 == 0:
#         even += 1
#     else:
#         odd += 1

# print("Even numbers:", even)
# print("Odd numbers:", odd)

# 4. Interchange the first and last elements

# numbers = [10, 23, 11, 12, 33, 44, 2, 5, 6]

# numbers[0], numbers[-1] = numbers[-1], numbers[0]

# print(numbers)

# 5. Duplicate all the items
# li = [1, 2, 3]
# output = li * 3
# print(output)

# 6. find the smallest element
# numbers = [10, 23, 11, 12, 33, 44, 2, 5, 6]
# smallest = numbers[0]

# for num in numbers:
#     if num < smallest:
#         smallest = num
# print("Smallest element:", smallest)

#Using min() function
# numbers = [10, 23, 11, 12, 33, 44, 2, 5, 6]
# print("Smallest element:", min(numbers))

# 7. find the greatest elm.
# number=[89,23,24,2,55,54,64]
# greatest = numbers[0]
# for num in numbers:
#     if num > greatest:
#         greatest=num
# print("greatest element:",greatest)

# 8.find repetitive element
# numbers = [1, 2, 3, 4, 56, 1, 22, 23, 33, 23, 56]
# duplicates = []
# for num in numbers:
#     if numbers.count(num) > 1 and num not in duplicates:
#         duplicates.append(num)

# print("Repetitive elements:", duplicates)

# 9.remove all odd elm.
# numbers = [10, 23, 11, 12, 33, 44, 2, 5, 6]
# even_numbers = []
# for num in numbers:
#     if num % 2 == 0:
#         even_numbers.append(num)

# print("List after removing odd elements:", even_numbers)

# 10.find non-repetitive elm
# numbers = [1, 2, 3, 4, 56, 1, 22, 23, 33, 23, 56]
# non_repetitive = []
# for num in numbers:
#     if numbers.count(num) == 1:
#         non_repetitive.append(num)

# print("Non-repetitive elements:", non_repetitive)

#11.duplicate all items 3 times
# l = [1, 2, 3]

# result = []

# for i in range(3):
#     result.extend(l)

# print(result)

#12.find the second greatest elm.
# numbers = [89, 23, 24, 2, 55, 54, 64]

# largest = second_largest = float('-inf')

# for num in numbers:
#     if num > largest:
#         second_largest = largest
#         largest = num
#     elif num > second_largest and num != largest:
#         second_largest = num

# print("Second greatest element:", second_largest)

#sort
# numbers = [89, 23, 24, 2, 55, 54, 64]
# numbers.sort()
# print("Second greatest element:", numbers[-2])

# 13.reverse list
# numbers = [1, 2, 3, 4, 56, 1, 22, 23, 33, 23, 56]
# reversed_list = []
# for i in range(len(numbers) - 1, -1, -1):
#     reversed_list.append(numbers[i])

# print("Reversed List:", reversed_list)

# 14.arrange list in ascending order.
# numbers = [1, 2, 3, 4, 56, 1, 22, 23, 33, 23, 56]
# ascending = sorted(numbers)

# print("Ascending Order:", ascending)

# 15.arrange list in decending order.
# numbers = [1, 2, 3, 4, 56, 1, 22, 23, 33, 23, 56]

# descending_list = sorted(numbers, reverse=True)

# print(descending_list)

#16. waf to print all vowels.
# data = ["Dreamer", "infotech"]

# vowels = "aeiouAEIOU"

# for word in data:
#     for ch in word:
#         if ch in vowels:
#             print(ch)

#17. Create a List with Maximum 5 Elements
# my_list = []

# for i in range(5):
#     element = input(f"Enter element {i+1}: ")
#     my_list.append(element)

# print("List created:", my_list)


# 18.list of numbers from 10 to 1 in reverse order
# numbers = [i for i in range(10, 0, -1)]
# print(numbers)


#19.list of square numbers from 1 to 10
# squares = [i**2 for i in range(1, 11)]
# print(squares)

# 20.list of even numbers from 1 to 10
# even_numbers = [i for i in range(1, 11) if i % 2 == 0]
# print(even_numbers)


# 21.Python program that filters strings from the list
# language = ['python', 'php', 'java', 'c++', 'javascript', 'ruby']

# letter = input("Enter a letter: ")

# result = [lang for lang in language if letter.lower() in lang.lower()]

# print("Languages containing", letter, ":", result)


# 22.flatten a nested list using list comprehension
# nested_list = [[1, 2], [3, 4], [5, 6]]

# flat_list = [item for sublist in nested_list for item in sublist]

# print(flat_list)

# 23.find the frequency of each element in a list.
# numbers = [1, 2, 2, 3, 4, 1, 5, 2]
# freq = {}

# for num in numbers:
#     if num in freq:
#         freq[num] += 1
#     else:
#         freq[num] = 1

# for key, value in freq.items():
#     print(f"{key} → {value} time{'s' if value > 1 else ''}")



# Q24.A list is a palindrome if it reads the same forwards and backwards.
# numbers = [1, 2, 3, 2, 1]

# if numbers == numbers[::-1]:
#     print("Palindrome")
# else:
#     print("Not Palindrome")


#Q25.longest string in a list using the max() function with the key=len argument.
# animals = ["cat", "elephant", "dog", "hippopotamus"]

# longest = max(animals, key=len)

# print("Longest string:", longest)


#Q 26.Count how many strings in a list start with a vowel.
# words = ["apple", "banana", "orange", "umbrella", "grape", "ice"]

# vowel_words = [word for word in words if word[0].lower() in "aeiou"]

# print(f"{len(vowel_words)} strings start with a vowel")
# print(vowel_words)


# Q27. Replace all negative numbers in a list with zero List:
# numbers = [5, -3, 7, -1, 0, -8, 4]

# result = [0 if num < 0 else num for num in numbers]

# print(result)


#Q28.Create a new list containing only prime numbers from a given list
# numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15]

# prime_numbers = [
#     num for num in numbers
#     if num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1))
# ]

# print(prime_numbers)


#Q29 Convert a list of integers into a single integer number.
# numbers = [1, 2, 3, 4]

# result = int("".join(map(str, numbers)))

# print(result)


#Q30. Group elements of a list based on even and odd indices.
# numbers = [10, 20, 30, 40, 50, 60, 70, 80]

# even_index = [numbers[i] for i in range(len(numbers)) if i % 2 == 0]
# odd_index = [numbers[i] for i in range(len(numbers)) if i % 2 != 0]

# print("Elements at even indices:", even_index)
# print("Elements at odd indices:", odd_index)


# Q31.Find the largest even number in a list.
# numbers = [12, 45, 8, 67, 34, 90, 23, 56]

# even_numbers = [num for num in numbers if num % 2 == 0]

# largest_even = max(even_numbers)

# print("Largest even number:", largest_even)


#Q32..Find the majority element in a list.

numbers = [2, 2, 1, 2, 3, 2, 2]

n = len(numbers)

for num in set(numbers):
    if numbers.count(num) > n // 2:
        print("Majority Element:", num)
        break


#Q33.Find the difference between the maximum and minimum values in a list.

numbers = [10, 4, 7, 2, 15, 6]

difference = max(numbers) - min(numbers)

print("Difference:", difference)


# Q34. .Remove every third element from a list. 

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# result = [numbers[i] for i in range(len(numbers)) if (i + 1) % 3 != 0]

# print(result)


# Q35. .Insert an element at every even index of a list.

# numbers = [1, 2, 3]
# element = 0

# result = []

# for num in numbers:
#     result.append(element)
#     result.append(num)

# print(result)


# Q36. Rearrange a list so that positive and negative numbers alternate.

# numbers = [1, 2, -3, -4, 5, -6]

# positive = [num for num in numbers if num >= 0]
# negative = [num for num in numbers if num < 0]

# result = []

# for p, n in zip(positive, negative):
#     result.append(p)
#     result.append(n)

# print(result)

# Q 37. .Find the Missing Number from a Sequence.

# lst = [1, 2, 4, 5, 6]

# for num in range(1, 7):  # Expected range 1 to 6
#     if num not in lst:
#         print("Missing Number:", num)


# Q38. Find all pairs of elements in a list whose sum equals a given target number.

# lst = [2, 4, 3, 5, 7, 8, 9]
# target = 7

# for i in range(len(lst)):
#     for j in range(i + 1, len(lst)):
#         if lst[i] + lst[j] == target:
#             print((lst[i], lst[j]))


# Q39.Split a List into Chunks of Size 3.

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# chunks = []
# for i in range(0, len(lst), 3):
#     chunks.append(lst[i:i+3])

# print(chunks)

# Q40.Reverse Each String in a List.

# lst = ["python", "java", "script"]

# result = []

# for word in lst:
#     result.append(word[::-1])

# print(result)

# Q41..Extract All Digits from a List of Strings

# lst = ["abc123", "45def", "gh6"]

# result = []

# for item in lst:
#     digits = ""
    
#     for ch in item:
#         if ch.isdigit():
#             digits += ch
    
#     result.append(digits)

# print(result)


# Q42.Find All Anagram Groups in a List of Words.

words = ["eat", "tea", "tan", "ate", "nat", "bat"]

anagrams = {}

for word in words:
    key = "".join(sorted(word))
    
    if key not in anagrams:
        anagrams[key] = []
    
    anagrams[key].append(word)

result = list(anagrams.values())

print(result)