from math import sqrt
import re

# Template:  [Q no.] - [level i]
# Question: ...
# solution: ...

# Q.1- level 1
# Question: Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200
# (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.

def ans_1():
  result = ""
  for i in range(2000, 3200):
    if (i % 7 == 0 and i % 5 != 0):
      result += f"{i} "
  print(result)


# Q.2- level 1
# Question: Write a program which can compute the factorial of a given numbers. The results should be printed in a comma-separated
# sequence on a single line. Suppose the following input is supplied to the program: 8 Then, the output should be: 40320

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
# Question: With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an
# integral number between 1 and n (both included). and then the program should print the dictionary. Suppose the following
# input is supplied to the program: 8 Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

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
# Question: Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which
# contains every number. Suppose the following input is supplied to the program: 34,67,55,33,12,98 Then, the output should be:
# ['34', '67', '55', '33', '12', '98'] ('34', '67', '55', '33', '12', '98')
def ans_4():
  nums = input()
  print(list(nums.replace(",", "")))


# Q.5- level 1
# Question: Define a class which has at least two methods: getString: to get a string from console input printString: to print the
# string in upper case. Also please include simple test function to test the class methods.

class ans_5(object):
  def __init__(self):
    self.string = ""

  def getString(self):
    self.string = input()

  def printString(self):
    print(self.string)


# Q.6- level 2
# Question: Write a program that calculates and prints the value according to the given formula: Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H: C is 50. H is 30. D is the variable whose values should be input to your program in a
# comma-separated sequence. Example Let us assume the following comma separated input sequence is given to the program: 100,150,180
# The output of the program should be: 18,22,24

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
# Question: Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row
# and j-th column of the array should be i*j. Note: i=0,1.., X-1; j=0,1,¡­Y-1. Example Suppose the following inputs are given to the program:
# 3,5 Then, the output of the program should be: 
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
# Question: Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence
# after sorting them alphabetically. Suppose the following input is supplied to the program: without,hello,bag,world Then, the output should be:
# bag,hello,without,world

def ans_8():
  inp = input()
  words = [i for i in inp.split(",")]
  words.sort()
  print(",".join(words))


# Q.9- level 2
# Question: Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
# Suppose the following input is supplied to the program: Hello world Practice makes perfect Then, the output should be:
# HELLO WORLD PRACTICE MAKES PERFECT

def ans_9():
  text_f = ""
  for i in range(5):
    text = input()
    text_f += f"{text} "
  print(text_f.upper())


# Q.10- level 2
# Question: Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all
# duplicate words and sorting them alphanumerically. Suppose the following input is supplied to the program: hello world and practice
# makes perfect and hello world again Then, the output should be: again and hello makes perfect practice world

def ans_10():
  words = [i for i in input().split(" ")]
  print(" ".join(sorted(list(set(words)))))


# Q.11- level 2
# Question: Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether
# they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
# Example: 0100,0011,1010,1001 Then the output should be: 1010 Notes: Assume the data is input by console.

def ans_11():
  inp = input()
  nums = [i for i in inp.split(",")]
  div = []
  for i in nums:
    if (int(i) % 5 == 0):
      div.append(i)
  print(",".join(div))


# Q.12- level 2
# Question: Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit
# of the number is an even number. The numbers obtained should be printed in a comma-separated sequence on a single line.

def ans_12():
  res = []
  for i in range(1000, 3001):
    si = str(i)
    if (int(si[0]) % 2 == 0) and (int(si[1]) % 2 == 0) and (int(si[2]) % 2 == 0) and (int(si[3]) % 2 == 0): res.append(i)
  set(res)
  print(",".join([str(x) for x in res]))


# Q.13- level 2
# Question: Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program: hello world! 123 Then, the output should be: LETTERS 10 DIGITS 3


def ans_13():
  sent = input()
  sent = sent.replace(" ", "")
  sent_lst = list(sent)
  digits, letters = 0, 0
  for i in sent_lst:
    if i.isdigit() == True:
      digits += 1
    elif i.isdigit() == False:
      letters += 1
  print(f"LETTERS: {letters} | DIGITS: {digits}")


# Q.14- level 2
# Question: Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program: Hello world! Then, the output should be: UPPER CASE 1 LOWER CASE 9

def ans_14():
  sent = input()
  sent = sent.replace(" ", "")
  sent_lst = list(sent)
  uppercase,lowercase = 0, 0
  for i in sent_lst:
    if i.isupper() == True: uppercase += 1
    elif i.isupper() == False: lowercase += 1
  print(f"UPPERCASE: {uppercase} | LOWERCASE: {lowercase}")


# Q.15- level 2
# Question: Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program: 9 Then, the output should be: 11106

def ans_15():
  inp = input()
  for i in range(1, 5): res = res + int(inp * i)
  print(res)


# Q.16- level 2
# Question: Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
# Suppose the following input is supplied to the program: 1,2,3,4,5,6,7,8,9 Then, the output should be: 1,9,25,49,81

def ans_16():
  inp = input()
  inp = inp.split(",")
  res = []
  for i in inp:
    if (int(i) % 2 == 1):
      res.append(int(i)**2)
  print(",".join([str(x) for x in res]))


# Q.17- level 2
# Question: Write a program that computes the net amount of a bank account based a transaction log from console input.
# The transaction log format is shown as following: D 100 W 200
# D means deposit while W means withdrawal. Suppose the following input is supplied to the program: D 300 D 300 W 200 D 100 Then,
# the output should be: 500

def ans_17():
  total = 0
  while True:
    inp = input()
    if not inp: break
    inp = inp.split(" ")
    type = inp[0]
    amt = int(inp[1])
    if (type == "D"): total += amt
    elif (type == "W"): total -= amt
  print(total)


# Q.18- level 3
"""
Question: A website requires the users to input username and password to register. Write a program to check the validity of password input by 
users. Following are the criteria for checking the password:

- At least 1 letter between [a-z]
- At least 1 number between [0-9]
- At least 1 letter between [A-Z]
- At least 1 character from [$#@]
- Minimum length of transaction password: 6
- Maximum length of transaction password: 12

Your program should accept a sequence of comma separated passwords and will check them according to the above criteria.
Passwords that match the criteria are to be printed, each separated by a comma. Example If the following passwords are given as 
input to the program: ABd1234@1,a F1#,2w3E*,2We3345 Then, the output of the program should be: ABd1234@1
"""
def ans_18():
  value = []
  inp = input()
  items=inp.split(",")
  for i in items:
      if len(i)<6 or len(i)>12: continue
      else: pass

      if not re.search("[a-z]",i):   continue
      elif not re.search("[0-9]",i): continue
      elif not re.search("[A-Z]",i): continue
      elif not re.search("[$#@]",i): continue
      elif re.search("\s",i):        continue
      else: pass
      value.append(i)
  print(",".join(value))
