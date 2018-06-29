from collections import Counter
   def word_count('nikhil.txt','r'):
   	    with open('nikhil.txt') as f:
            return Counter(f.read().split())
   print("Number of words in the file :",word_count("test.txt"))
