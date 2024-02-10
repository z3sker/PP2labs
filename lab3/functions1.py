#grams to ounces
def grams_to_ounces(grams):
    return 28.3495231 * grams

#Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)

#chicken and rabbit zadacha
def solve(numheads, numlegs):
    for rabbits in range(numheads + 1):
        chickens = numheads - rabbits
        if (4 * chickens + 2 * rabbits) == numlegs:
            return chickens, rabbits
    return "No solution"

#only prime numbers
def filter_prime(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    return [num for num in numbers if is_prime(num)]

#all permutations
from itertools import permutations

def print_permutations(string):
    perms = permutations(string)
    for perm in perms:
        print(''.join(perm))

#word reversing
def reverse_words(sentence):
    words = sentence.split()
    return ' '.join(reversed(words))

#dve troiki podryad
def has_33(nums):
    for i in range(len(nums)-1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False

#007
def spy_game(nums):
    code = [0, 0, 7, 'x']
    for num in nums:
        if num == code[0]:
            code.pop(0)
    return len(code) == 1

#sphere ob'em
def sphere_volume(radius):
    return (4/3) * 3.14159 * radius**3

#unique elements
def unique_elements(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

#palindrome proverka
def is_palindrome(word):
    return word == word[::-1]

#histogram
def histogram(numbers):
    for num in numbers:
        print('*' * num)

# Function to play the number guessing game
import random

def number_guessing_game():
    name = input("Hello! What is your name?\n")
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    number_to_guess = random.randint(1, 20)
    num_guesses = 0
    while True:
        guess = int(input("Take a guess.\n"))
        num_guesses += 1
        if guess < number_to_guess:
            print("Your guess is too low.")
        elif guess > number_to_guess:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {num_guesses} guesses!")
            break