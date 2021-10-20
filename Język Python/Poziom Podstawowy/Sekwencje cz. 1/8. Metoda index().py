def get_initials( name ):
    space = name.index(" ")
    pierwsza= name[0]
    druga= name[space+1:space+2]
    razem = pierwsza + druga
    return razem.upper()