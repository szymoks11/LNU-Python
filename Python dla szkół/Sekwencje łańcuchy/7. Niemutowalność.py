def emailProvider( email ):
    malpa = email.index("@")
    return email[malpa+1:]