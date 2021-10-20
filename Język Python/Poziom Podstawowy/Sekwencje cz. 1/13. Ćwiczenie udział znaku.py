def hasDuplicates(text):
   for i in range(0, len(text) - 1):
       if (text[i] == text[i + 1]):
           return True
   return False