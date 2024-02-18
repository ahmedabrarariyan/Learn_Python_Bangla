#Lesson 7: Strings

    #[""(quotation mark) er moddhe aboddho kichu character]
    #single quote('') ba double quote("") duivabei shuddho, jotokkhon duipashe ek e rokom thake
    #orthat single quote diye shuru korle double quote diye shesh kora jabe na


    #plus operator(+) bebohar kore string concatenate(jora lagano) kora jay
    #Example:
name = "Tutul Miya"
phrase = "Goru" + " ghash " + "khay."
phrase1 = name + " ghash" + " khay."
print(phrase); print(phrase1)

    #+= operator bebohar koreo ei kaaj ta kora jay
name += " gaan" + " kore."
print(name)

    #str class constructor diye ekta number ke string e convert kora jay
    #[eta L04 e amra shikhechi]
age = str(36)
print(isinstance(age, str)) #True
print(type(age) == int) #False

    #[triple quote(""" """) bebohar kore kono string ke ekadhik line er banano jay]
print("""Goru
ghash
khay.""")
    #amra \n diyeo notun line banate pari
print("Goru\nGhash\nKhay") #notun line er jonne \n

    #String Methods
print("ahmed".upper()) #AHMED #turns everything to capital
print("ahMED".lower()) #ahmed #turns everything to small
print("ahmed abrar".title()) #Ahmed Abrar #turns first letter of each word to capital

print("ahMEd".islower()) #False #checks if all letters are small
print("Ahmed".isupper()) #False #checks if all letters are capital
print("Ahmed Abrar".istitle()) #True

    #Various String Methods:

      #
      #capitalize()	Converts the Only The First character to upper case
print("ahmed abrar".capitalize()) #Ahmed abrar

      #casefold()	Converts the whole string into lower case
print("AHmed AbRAR".casefold()) #ahmed abrar
      #lower()	Converts a string into lower case. Similar to casefold()

      #center()	Returns a centered string
        #The center() method will center align the string,
        #using a specified character (space is default) as the fill character.
print(name.center(100)) #this is use 100 pixels of space for each side.
print(name.center(50, "O")) #prothome length of padding, tarpore character of padding
        #also, length beshi choto hole, character ta show kore na.

      #count()	Returns the number of times a specified value occurs in a string
print("Joy Bangla".count("g")) #1
print("Joy Bangla".count("Bang")) #1

      #encode()	Returns an encoded version of the string
print("Valobasha".encode()) #b'Valobasha' (wtf is encoded? b er abar kaj ki?)

      #endswith()	Returns true if the string ends with the specified value
print("Jhaira Lok".endswith("k")) #True
print("Jhaira Lok".endswith("Lok")) #True

      #expandtabs()	Sets the tab size of the string

      #find()	Searches the string for a specified value and returns the position of where it was found
        
      #format()	Formats specified values in a string

      #format_map()	Formats specified values in a string

      #index()	Searches the string for a specified value and returns the position of where it was found
        
      #isalnum()	Returns True if all characters in the string are alphanumeric

      #isalpha()	Returns True if all characters in the string are in the alphabet

      #isascii()	Returns True if all characters in the string are ascii characters

      #isdecimal()	Returns True if all characters in the string are decimals

      #isdigit()	Returns True if all characters in the string are digits

      #isidentifier()	Returns True if the string is an identifier

      #islower()	Returns True if all characters in the string are lower case

      #isnumeric()	Returns True if all characters in the string are numeric

      #isprintable()	Returns True if all characters in the string are printable

      #isspace()	Returns True if all characters in the string are whitespaces

      #istitle()	Returns True if the string follows the rules of a title

      #isupper()	Returns True if all characters in the string are upper case

      #join()	Converts the elements of an iterable into a string

      #ljust()	Returns a left justified version of the string



      #lstrip()	Returns a left trim version of the string

      #maketrans()	Returns a translation table to be used in translations

      #partition()	Returns a tuple where the string is parted into three parts

      #replace()	Returns a string where a specified value is replaced with a specified value

      #rfind()	Searches the string for a specified value and returns the last position of where it was found
        
      #rindex()	Searches the string for a specified value and returns the last position of where it was found
        
      #rjust()	Returns a right justified version of the string
        
      #rpartition()	Returns a tuple where the string is parted into three parts
        
      #rsplit()	Splits the string at the specified separator, and returns a list
        
      #rstrip()	Returns a right trim version of the string
        
      #split()	Splits the string at the specified separator, and returns a list
        
      #splitlines()	Splits the string at line breaks and returns a list

      #startswith()	Returns true if the string starts with the specified value

      #strip()	Returns a trimmed version of the string

      #swapcase()	Swaps cases, lower case becomes upper case and vice versa

      #title()	Converts the first character of each word to upper case

      #translate()	Returns a translated string

      #upper()	Converts a string into upper case

      #zfill()	Fills the string with a specified number of 0 values at the beginning

  #Escaping in strings
    #We can use \ to use something in a string that's usually used for something else.
print("Keu \"Thamate \"Parbe \"Na.") #Keu "Thamate "Parbe "Na)
    #Now, to use a backslash in a string, we have to use \\
print("Keu \\ Thamate \\ Parbe \\ Na.") #Keu \ Thamate \ Parbe \ Na.

  #In coding, counting starts from 0. And 0 is not considered negative.
  #We can use squared brackets after string to get a character at a specific index.
print("chocolat"[0]) #c
print("custurd"[1]) #u
print("bachur"[-1]) #r

  #Slicing a string
  #if I input [a:b], then it show only the part of the string from a to b-1.
print("Doodh"[1:3]) #ekhane 1 tomo digit o, 3 tomo digit d. tai oo result
print("Oh accha tai naki"[1:7]) #ekhane 1 tomo digit h, 7 tomo digit a. result- h acch