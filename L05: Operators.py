#Lesson 6: Operators

  #Python e prodhanoto 7 dhoroner Operator ache---
    #1. Arithmetic Operators
    #2. Assignment Operators
    #3. Comparison Operators
    #4. Boolean / Logical Operators
      #4a. Bitwise operators (Binary er jonne Boolean)
    #5. Identity operators
    #6. Membership operators
    #7. Ternary Operator

#
  ##Arithmetic Operators---
    #+	Jog     x + y	(Addition)
    #-	Biyog	  x - y (Substraction)
    #*	Gun     x * y	(Multiplication)
    #/	Bhag	  x / y	(Division)
    #%	Bhagshesh	      x % y; 4%3 = 1    (Remainder)
    #**	Ghat(Power)     x ** y; 4**2 = 16 (Exponentiation)  (x^y)
    #//	Floor division	x // y; 5//2 = 2  (Nikot_tomo nicher purno_shongkha ashbe)

    #Examples:
a = 4
b = 11
print(b / a) #2.75 (bhagfol)
print(b % a) #3 (bhagshesh)
print(b ** a) #11*11*11*11 = 1296
print(b // a) #2 (floor division)

#    
  ##Assignment operators
          #Example:      Same as:
    #=	    x = 5	      x = 5	
    #+=	    x += 3	    x = x + 3	
    #-=	    x -= 3	    x = x - 3	
    #*=	    x *= 3	    x = x * 3	
    #/=	    x /= 3	    x = x / 3	
    #%=	    x %= 3	    x = x % 3	
    #//=	  x //= 3	    x = x // 3	
    #**=	  x **= 3	    x = x ** 3	
    #&=	    x &= 3	    x = x & 3	
    #|=	    x |= 3	    x = x | 3	
    #^=	    x ^= 3	    x = x ^ 3	
    #>>=	  x >>= 3	    x = x >> 3	
    #<<=	  x <<= 3	    x = x << 3

#    
  ##Comparison operators
    #==	Equal	x == y                      (shoman)
    #!=	Not equal	x != y                  (shoman noy)
    #>	Greater than	x > y               (baam er ta boro)
    #<	Less than	x < y                   (baam er ta choto)
    #>=	Greater than or equal to	x >= y  (baam er ta boro othoba shoman)
    #<=	Less than or equal to	x <= y      (baam er ta choto othoba shoman)

    #Examples:

a = 1
b = 2
print(a == b) #false
print(a != b) #true
print(a > b)  #false
print(a < b)  #true
print(a >= b) #false
print(a <= b) #true

#
  ##Boolean / Logical operators
    #and 	Returns True if both statements are true	x < 5 and; x < 10	
    #or	Returns True if one of the statements is true	x < 5 or; x < 4	
    #not	Reverse the result, returns False if the result is true;	not(x < 5 and x < 10)
condition1 = True
condition2 = False

print(not(condition1)) #False; just reversed the original
print(condition1 and condition2) #False; both must be true
print(condition1 or condition2) #True; at least one is true
      
      #magic of OR operator (searches for true)
        #if the First of 2 values is True, it will return the First value
        #if the First of 2 values is False, it will return the Second value
        #true values: True, 1, 'abc', ' ', [1,2,3], {1,2,3}, (1,2,3)
        #false values: False, 0, '', [], {}, (), None

print(0 or 1) #1 (here, the first value is false)
print(False or 'hey') #'hey' (here, the first value is false)
print('hi' or 'hey') #'hi' (here, the first value is true)
print([] or False) #'False' (here, the first value is false) (both are false btw)
print(False or []) #'[]' (here, the first value is false) (both are false btw)

      #magic of AND operator (searches for false)
        #if the First of 2 values is True, only then it will return the Second value
        #if the First of 2 values is False, it will return the First value

print(0 and 1) #0 (here, the first value is false)
print(1 and 0) #0 (here, the first value is true)
print(False and 'hey') #'False' (here, the first value is false)
print('hi' and 'hey') #'hey' (here, the first value is true)
print([] and False) #'[]' (here, the first value is false) (both are false btw)
print(False and []) #'False' (here, the first value is false) (both are false btw)


    #Bitwise operators (very rarely used) (only for binary)
          #Name   Work                                              Examples
      #& 	AND	    Sets each bit to 1 if both bits are 1	            x & y	
      #|	OR	    Sets each bit to 1 if one of two bits is 1	      x | y	
      #^	XOR	    Sets each bit to 1 if only one of two bits is 1	  x ^ y	
      #~	NOT	    Inverts all the bits	                            ~x	
      #<<	Shift left operation;	  Shift left by pushing zeros in from the right
        #and let the leftmost bits fall off	                        x << 2	
      #>>	Shift right operation;	    Shift right by pushing copies of the leftmost bit in
        #from the left, and let the rightmost bits fall off	        x >> 2

    #Identity operators
      #is;	Returns True if both variables are the same object;	x is y
      #is not;	Returns True if both variables are not the same object; x is not y

    #Membership operators
      #in;	Returns True if a certain value is present in another list or sequence;	x in y
      #not in;	Returns True if a certain value is not present in another list or sequence; x not in y

    #Ternarry operator (shortcut of if-else statement)
def is_adult(age):
  if age > 18:
    return True
  else:
    return False

def is_adult2(age):
  return True if age > 18 else False
print(is_adult(15)); print(is_adult2(29))