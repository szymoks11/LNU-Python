def formatHeight( feet, inches ):
    if feet.isnumeric() and ( ( len( feet ) > 1 and feet[0] != '0' ) or len( feet ) == 1 )  and inches.isnumeric() and ( ( len( inches ) > 1 and inches[0] != '0' ) or len( inches ) == 1 ) and 0 <= int( inches ) <= 12:
            return feet+" ft "+inches
    return 0