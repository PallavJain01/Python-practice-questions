from math import sqrt

# Template:  [Q no.] - [level i]
# Question: ...
# solution: ...

# Q.1- level 1
# Question: Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

def ans_1():
  result = ""
  for i in range(2000, 3200):
    if (i % 7 == 0 and i % 5 != 0):
      result += f"{i} "
  print(result)


# Q.2- level 1
# Question: Write a program which can compute the factorial of a given numbers. The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program: 8 Then, the output should be: 40320

def ans_2():
  num = int(input())
  factorial = 1
  if (num != 0):
    for i in range(1, num + 1):
      factorial *= i
    print(factorial)
  elif(num == 0):
    print("1")


# Q.3- level 1
# Question: With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included)
# and then the program should print the dictionary. Suppose the following input is supplied to the program: 8 Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

def ans_3():
  num = input()
  result = dict()
  if (num != 0):
    for i in range(1, num + 1):
      result[i] = i*i
    print(result)
  elif (num == 0):
    print("Plese enter a number greater than 0")


# Q.4- level 1
# Question: Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number. Suppose the following input is supplied to the program: 34,67,55,33,12,98 Then, the output should be: ['34', '67', '55', '33', '12', '98'] ('34', '67', '55', '33', '12', '98')
def ans_4():
  nums = input()
  print(list(nums.replace(",", "")))


# Q.5- level 1
# Question: Define a class which has at least two methods: getString: to get a string from console input printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

class ans_5(object):
  def __init__(self):
    self.string = ""

  def getString(self):
    self.string = input()

  def printString(self):
    print(self.string)


# Q.6- level 2
# Question: Write a program that calculates and prints the value according to the given formula: Q = Square root of [(2 * C * D)/H].
#Following are the fixed values of C and H: C is 50. H is 30. D is the variable whose values should be input to your program in a comma-separated sequence. Example Let us assume the following comma separated input sequence is given to the program: 100,150,180 The output of the program should be: 18,22,24

def ans_6():
  nums = input()
  C = 50
  H = 30
  res = ""
  D = list(nums.split(","))
  for i in range(0, len(D)):
    Q = int(sqrt((2 * C * int(D[i])) / H))
    res += str(Q) + ","
  print(res[:-1])


# Q.7- level 2
# Question: Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,Y-1. Example Suppose the following inputs are given to the program: 3,5 Then, the output of the program should be:
# [
#  [0, 0, 0, 0, 0],
#  [0, 1, 2, 3, 4],
#  [0, 2, 4, 6, 8]
# ]

def ans_7():
  inp = input()
  lst = list(inp.replace(",", ""))
  X,Y = lst[0],lst[1]
  lst_init = []
  lst_final = []
  for i in range(int(X)):
    for j in range(int(Y)):
      lst_init.append(i * j)
    lst_final.append(lst_init)
    lst_init = []
  print(lst_final)


# Q.8- level 2
# Question: Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program: without,hello,bag,world Then, the output should be: bag,hello,without,world

def ans_8():
  inp = input()
  words = [i for i in inp.split(",")]
  words.sort()
  print(",".join(words))


# Q.9- level 2
# Question: Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
# Suppose the following input is supplied to the program: Hello world Practice makes perfect Then, the output should be: HELLO WORLD PRACTICE MAKES PERFECT

def ans_9():
  text_f = ""
  for i in range(5):
    text = input()
    text_f += f"{text} "
  print(text_f.upper())


# Q.10- level 2
# Question: Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and
# sorting them alphanumerically. Suppose the following input is supplied to the program: hello world and practice makes perfect and hello world again Then, the output should be: again and hello makes perfect practice world

def ans_10():
  words = [i for i in input().split(" ")]
  print(" ".join(sorted(list(set(words)))))
