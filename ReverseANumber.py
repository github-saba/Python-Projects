# This function returns a number in reverse order

def reverseANumber(number):
    revNumber = ""
    while number > 0:
        	revNumber += str(number%10)
        	number = int(number/10)
    return revNumber
    
print(reverseANumber(123456789))
