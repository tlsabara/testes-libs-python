from tkinter.tix import Tree


def eNumero(num):
    
     try:
         #Try to convert the input. 
         float(num)
         
         #If successful, returns true.
         return True
         
     except:
         #Silently ignores any exception.
         pass
     
     #If this point was reached, the input is not a number and the function
     #will return False.
     return False
 
def not_eNumero(num):
        
     try:
         #Try to convert the input. 
         float(num)
         
         #If successful, returns true.
         return False
         
     except:
         #Silently ignores any exception.
         pass
     
     #If this point was reached, the input is not a number and the function
     #will return False.
     return True