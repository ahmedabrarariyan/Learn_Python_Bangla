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
    #and: jodi 2 ta statement e True hoy, tahole True bolbe.	x < 5 and; x < 10	
    #or: 2 tar moddhe jekono 1 ta True holei, True bolbe.	x < 5 or; x < 4	
    #not:	True ke False aar False ke True bole.	not(x < 5 and x < 10)
      #[orthat uttor True hole oitake False bolbe]

    #Example:
condition1 = True
condition2 = False

print(not(condition1)) #False; True ke False banay dilo
print(condition1 and condition2) #False; 2 te kei True houa lagbe
print(condition1 or condition2) #True; ontoto 1 ta True houa lagbe

#      
  ##OR operator er jadu (searches for true)
    #2 ta value er moddhe 1st ta jodi True hoy, tahole 1st ta e dibe. 2nd tay jabe na
    #2 tar moddhe 1st value ta False hole, 2nd value te jabe, aar 2nd ta e dibe
      #[2nd value ta False holeo, 2nd ta dibe, jodi 1st value False hoy]
    #True values: True, 1, 'abc', ' ', [1,2,3], {1,2,3}, (1,2,3)
    #False values: False, 0, '', [], {}, (), None
      #[orthat, data faka thakle ba 0 hole, oita False]

print(0 or 1) #1; (ekhane 1st value False, tai 2nd value ashche)
print(False or 'hey') #hey; (ekhane 1st value False, tai 2nd value ashche)
print('hi' or 'hey') #hi; (ekhane 1st value tai True, tai 1st value ashche)
print([] or False) #False; (ekhane 1st value False, tai 2nd value ashche) (ekhane kintu 2 tai False)
print(False or []) #[]; (ekhane 1st value False, tai 2nd value ashche) (ekhane kintu 2 tai False)

#
  ##AND operator er jadu (searches for false)
    #1st value True hole, kebol tokhon e 2nd value te jabe ebong 2nd value dibe
    #1st value False hole, kebol tokhon e 1st value dibe

print(0 and 1) #0 (1st value False, tai 1st tai ashche)
print(1 and 0) #0 (1st value True, tai 2nd value ashche)
print(False and 'hey') #'False' (1st value False, tai 1st tai ashche)
print('hi' and 'hey') #'hey' (1st value True, tai 2nd value ashche)
print([] and False) #'[]' (1st value True, tai 2nd value ashche) (ekhane kintu 2 tai False)
print(False and []) #'False' (1st value True, tai 2nd value ashche) (ekhane kintu 2 tai False)

#
  ##Bitwise operators (very rarely used) (only for binary)
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