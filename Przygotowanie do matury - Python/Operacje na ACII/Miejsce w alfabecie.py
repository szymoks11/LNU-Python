import string 
def alphabetIndex( letter ):
    return string.ascii_uppercase.index(letter.capitalize())
print(alphabetIndex("a"))