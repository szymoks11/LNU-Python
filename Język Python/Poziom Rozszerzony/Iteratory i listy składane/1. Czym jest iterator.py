def cleanup(string):
    poprawiona = ""
    iterator = iter(string)
    while True:
        try:
            element = next(iterator)
            if element.isalnum() == True:
                poprawiona+= element
        except StopIteration:
            break
    return poprawiona