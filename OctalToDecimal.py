#this function is for converting octal number to decimal number 

def octToDec(oct_number):
	dec_number = 0
    	c = 0
    	while oct_number > 0:
        		num = oct_number%10
        		oct_number = int(oct_number/10)
        		dec_number+= num*(8**c)
        		c+=1
    	return dec_number
    
print(octToDec(7531))