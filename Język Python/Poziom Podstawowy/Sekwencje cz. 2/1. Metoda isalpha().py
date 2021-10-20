def formatFirstName( name ):
    if name.isalpha() == True:
        return name.capitalize()
    else:
        return None

print(formatFirstName("$"))