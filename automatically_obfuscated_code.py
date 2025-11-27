# automatically_obfuscated_code.py
import math 

def func_obf(x): 
    
    res_val = 1
    i_val = 1
    
    
    state = 0 
    
    while state != 3: 
        
        if state == 0:
            
            if i_val > x:
                state = 3 
            else:
                state = 1 
                
        elif state == 1:
            
            res_val = res_val * i_val
            state = 2 
            
        elif state == 2:
            
            i_val += 1
            state = 0 
            
        else:
            
            return -1 
            
    return res_val 


print(f"Auto-Obfuscated Factorial of 5: {func_obf(5)}")