#Lesson 5: Data Types

        #data types---      #python e jevabe likha lage---    #konta ki---
        #Text Type: 	    str                               string = str
        #Numeric Types: 	int, float, complex               purno_shongkha = int, doshomik = float, jotil = complex
        #Sequence Types: 	list, tuple, range                list = [], tuple = ()
        #Mapping Type: 	    dict                              dictionary = {key: value}
        #Set Types: 	    set, frozenset                    set = {}
        #Boolean Type: 	    bool                              True, False
        #Binary Types: 	    bytes, bytearray, memoryview
        #None Type: 	    NoneType

    #[kono data er type janar jonno amra type() function bebohar korte pari]    
nambar = 16.04
print(type(nambar)) #prints float

    #[kono data nirdishto kono type er data ki na, oita amra 2 vabe check korte pari]

        #1 type function diye, kono ekta type er shoman ki na---
print(type(412) == str) #prints False

        #2 isinstance function diye, kono ekta type er ki na---
print(isinstance(nambar, int)) #prints True


    #'Class_Constructor' naam er ekta feature ache, jeta diye amra data type bodlate pari
#
feb = 2
print(type(feb) == float) #prints False

Feb = float(feb) #ekhane etake float bananor command dilam
print(isinstance(Feb, float)) #prints True

#
age = "16"
print(isinstance(age, int)) #Prints False

Age = int(age) #ekhane etake int bananor command dilam
print(isinstance(Age, int)) #Prints True

    #[kintu obosshoi, str er vitore kono shongkha na thakle, sheta ke int banano jabe na]
name = "Nantu Ghotok"
Name = int(name)
print(isinstance(Name, int)) #ERROR


    #Bivinno type er data er Example:
"Mounota"                                       #string
100                                             #int
4.00                                            #float
4+12j                                           #complex
["Pohela", "Layba", 23]                         #list
("Pahar", "Shomudro", 14)                       #tuple
{"Groho": "Prithibi", "Upogroho": "Chand"}      #dictionary
{"Adam", "Ibrahim", "Musa", "Muhammad"}         #set