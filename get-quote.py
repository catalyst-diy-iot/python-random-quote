import random
def function():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  #last = 13
  last = len(quotes) - 1
  rnd = random.randint(0, last)
  print(quotes[rnd])

if __name__== "__main__":
  function()
'''
Add some more quotes to your text file
 Print out more than one quote at a time
 Remove that extra line (called a newline) when printing
 Learn about file writing and add quotes programmatically
 '''