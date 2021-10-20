def get_index( value, text ):
    if value in text:
        if text.index(value) != 0:
            return text.index(value)
    else:
        return -1