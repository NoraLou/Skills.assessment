# Things you should be able to do.

number_list = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
word_list = [ "What", "about", "the", "Spam", "sausage", "spam", "spam", "bacon", "spam", "tomato", "and", "spam"]

# Write a function that takes a list of numbers and returns a new list with only the odd numbers.
def all_odd(number_list):
    all_odd = []   #  O(1) constant time
    for i in number_list: # O(n) n is number of iterations
        if i % 2 != 0: # O(1)
            all_odd.append(i) # O(1)
    return all_odd

#\(O(1) + O(n) * (O(1) + O(1))\) 
# reduce to O(2n) >> O(n)

# 1(assign) + loop(1(if) + 1(append)) + 1(return)

# 2 + (2n)

print(all_odd(number_list))


# Write a function that takes a list of numbers and returns a new list with only the even numbers.
def all_even(number_list):
    all_even = []
    for i in number_list:
        if i % 2 == 0:
            all_even.append(i)
    return all_even

print(all_even(number_list))

# Write a function that takes a list of strings and a new list with all strings of length 4 or greater.
def long_words(word_list):
    long_words = []
    for i in word_list:
        if len(i) >= 4:
         long_words.append(i)
    return long_words

print(long_words(word_list))    

# Write a function that finds the smallest element in a list of integers and returns it.

def smallest(number_list):
    smallest = number_list[0]  # O(1)
    for number in number_list: # O(n)
        if number < smallest:  # O(1)
             number == smallest # O(1)
    return smallest
print smallest(number_list)

# O(2n)

# Write a function that finds the largest element in a list of integers and returns it.
def largest(number_list):
    largest = number_list[0]
    for number in number_list:
        if number > largest:
            largest = number
    return largest

print(largest(number_list)) 

# O(2n)

# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(number_list):
    halvesies = []            # O(1)
    for number in number_list: # O(n)
        halvesies.append(number/2) #0
    return halvesies

print(halvesies(number_list))

# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lengths(word_list):
    word_lengths = []
    for word in word_list:
        word_lengths.append(len(word))
    return word_lengths

print(word_lengths(word_list))


# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(number_list):
    sum_numbers = 0
    for number in number_list:
        sum_numbers += number
    return sum_numbers

print sum_numbers(number_list)

    
# Write a function that multiplies all the numbers in a list together.
def mult_numbers(number_list):
    mult_number = 1
    for number in number_list:
        mult_number *= number
    return mult_number
print mult_numbers(number_list)


# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(word_list):
    joined_list = " "
    for i in word_list:
        joined_list += i
    return joined_list


print(join_strings(word_list), 'join words')

# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(number_list):
    average = sum_numbers(number_list)/float(len(number_list)) 

    return average

print(average(number_list))









