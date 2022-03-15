# Spell Check Starter
# This start code creates two lists
# 1: dictionary: a list containing all of the words from "dictionary.txt"
# 2: aliceWords: a list containing all of the words from "AliceInWonderland.txt"

import re  # Needed for splitting text with a regular expression
import math
import time
from tracemalloc import start
# Menu w/ user input
def menu():
    print("1. Spell Check a Word using Linear Search")
    print("2. Spell Check a Word using Binary Search")
    print("3. Spell Check Alice in Wonderland using Linear Search")
    print("4. Spell Check Alice in Wonderland using Binary Search")
    print("5. Exit")
menu()

option = int(input("Enter a number between 1 & 5: "))


def main():
    # Load data files into lists
    dictionary = loadWordsFromFile("data-files/dictionary.txt")
    aliceWords = loadWordsFromFile("data-files/AliceInWonderLand.txt")

    # Print first 50 values of each list to verify contents
    # print(dictionary[0:50])
    # print(aliceWords[0:50])
    while option != 0:
        
        if option == 1:
            # Spell Check Linear Search
            linearWord = input("Please enter a word: ").lower()
            startTime = time.time()
            print(linearSearch(dictionary, linearWord))
            print(time.time() - startTime, "secs")
        elif option == 2:
            binaryWord = input("Please enter a word: ").lower()
            print(binarySearch(dictionary, binaryWord))
            startTime = time.time()
            print(time.time() - startTime, "secs")
            pass
        elif option == 3:
            # Spell Check AIW using Linear Search




            pass
        elif option == 4:
            # Spell Check AIW using Binary Search
            pass
        else:
            print("Thanks for trying out this program!")
            quit()
# end main()

# Binary Search Function
def binarySearch(anArray, item):
  lowerIndex = 0
  upperIndex = len(anArray)-1
  while lowerIndex <= upperIndex:
    middleIndex = math.floor(lowerIndex + upperIndex) // 2
    if item == anArray[middleIndex]:
      return middleIndex
    elif item < anArray[middleIndex]:
      upperIndex = middleIndex - 1
    else:
      lowerIndex = middleIndex + 1
  return -1
# Linear Search Function
def linearSearch(array, item):
  for i in range(len(array)):
    if array[i] == item:
      return i
  return -1

def loadWordsFromFile(fileName):
    # Read file as a string
    fileref = open(fileName, "r")
    textData = fileref.read()
    fileref.close()

    # Split text by one or more whitespace characters
    return re.split('\s+', textData)
# end loadWordsFromFile()


# Call main() to begin program
main()
