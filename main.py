#defining a function 
def pattern_num(num:int):
    ''' this function take int parameter and prints out the result pattern '''
    for i in range(num,0,-1):
       
       for j in range(i,0,-1):
           print(j, end=" ")
        
       print(" ")
      
    
#calling the function
pattern_num(5)

#accessing documentation
print(pattern_num.__doc__)