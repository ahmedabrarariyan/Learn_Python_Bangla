#Lesson 8: Number Data Types

  #int (integer): purno shongkha
  #float: doshomik shongkha
  #complex: purno + kalponik shongkha
    #higher math e amra 7+8i evabe likhi
    #engineering/coding e i er bodole j bebohar hoy; 4+5j emon


num1 = 2+3j #amra evabe directly complex number likhte pari
num2 = complex(2,3) #othoba amra bebohar korte pari complex() function
  #1st ta real part, 2nd ta imaginary part

print(num2.real, num2.imag) #eta the real and imaginary part of num2

  #Built-in functions that help with numbers:

abs(-2004) #this will return the absolute value of a number.
  #(positive arki) (oije modulus chinnoh)
print(abs(-684))

  #round() function rounds a number to the nearest integer.
print(round(3.49)) #returns 3
print(round(5.5)) #returns 6
  #now, I can put in a 2nd value in the round() function.
  #the 2nd value determinds how many decimal places to round to.
  #if the 2nd value is 0, it will round to the nearest integer.
  #if the 2nd value is 1, it will round to the nearest tenth.
  #tarpor 2 boshaile nearest 100th. maane doshomiker pore 2 ghor. 3 boshaile 3 ghor.
print(round(3.49, 1)) #returns 3.5
print(round(6.4795, 3)) #returns 6.479
print(round(6.4796, 3)) #returns 6.48
  #first ghore 5 boshailei baray fele. but tarpor theke 6 boshaile bare, naile bare na.
  #eije porer part ta ja lekhlam, ta bujhar jonne math ghata lagbe.