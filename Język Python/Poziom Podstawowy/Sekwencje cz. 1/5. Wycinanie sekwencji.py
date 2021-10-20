def get_year( data ):
    
   if data[-4:-1] == '199':

       return data[-4:]

   elif data[0:3] == '199':

       return data[0:4]
