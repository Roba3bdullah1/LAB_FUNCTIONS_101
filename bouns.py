#defining a function 
def pattern_string(num:int) -> str:
    ''' this function take int parameter and return pattern as string '''
    str_pattern:str = ""
    for i in range(num,0,-1):    
       for j in range(i,0,-1):
           str_pattern+=str(j) + " "  
       str_pattern+= "\n"     
    return str_pattern
      
    
#calling the function
print(pattern_string(10))

#accessing documentation
print(pattern_string.__doc__)