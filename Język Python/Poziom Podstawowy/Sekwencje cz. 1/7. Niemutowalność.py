def formatName( name ):
    space = name.index("_")
    pierwsza= name[:space]
    druga= name[space+1:]
    return pierwsza + druga.capitalize()