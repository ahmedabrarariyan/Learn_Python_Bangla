#Lesson 6: Strings

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
    #Examples:
print("ahmed".upper()) #AHMED #shobkichuke capital kore
print("ahMED".lower()) #ahmed #shobkichuke small kore
print("ahmed abrar".title()) #Ahmed Abrar #Prottek shobder prothom word ke capital kore

print("ahMEd".islower()) #False #shob letter small ki na, check kore
print("Ahmed".isupper()) #False #shob letter capital ki na, check kore
print("Ahmed Abrar".istitle()) #True #shob word er 1st letter capital ki na, check kore

    #string method gular ekta purno list niche jukto kora hoyeche

    #Escaping in strings
    #[backslash(\) bebohar kore amra emon kichuke output e ante pari, ja emnite onno kaje bebohar hoy]
    #quote(") bebohar kore string shuru aar shesh hoy, tai etake amra emnite output e dekhi na
    #jodi etake output e show korte chai, tahole etar aage \ bebohar korte hobe.

print("Keu \"Thamate \"Parbe \"Na.") #Keu "Thamate "Parbe "Na)

    #ekhon, jodi amra backslash(\) ke show korte chai, taile dite hobe \\
print("Keu \\ Thamate \\ Parbe \\ Na.") #Keu \ Thamate \ Parbe \ Na.

    #Coding e 0 theke gonona shuru hoy aar 0 ke negative dhora hoy na.
    #string er por squared brackets[] er moddhe number boshiye oi index er character pawa jay
print("chocolat"[0]) #c; 1st index e c chilo
print("custurd"[1]) #u; 2nd index e u chilo
print("bachur"[-1]) #r; last index e r chilo

    #Slicing a string
    #[a:b] diye slice korle, amake a theke b-1 porjonto index er character dekhabe
print("Doodh"[1:3]) #ekhane 1(2nd index) e o, 3(4th index) e d. tai result oo
        #3-1(3rd index) er character o
print("Oh accha tai naki"[1:7]) #ekhane 1(2nd index) e h, 7(8th index) e a. result- h acch
        #7-1(7th index) er character h


    #Bivinno String Methods:

      #capitalize(); string er 1st character ke capitalize kore
print("ahmed abrar".capitalize()) #Ahmed abrar

      #casefold(); puro string er shob character ke small kore
print("AHmed AbRAR".casefold()) #ahmed abrar
      #lower(); puro string er shob character ke small kore. casefold() aar eta same

      #center(); kendre obosthito string dekhabe
        #string ke kendre sthaponer jonne duipashe onno character boshabe
        #by default, space diye duipash purno korbe
        #othoba amra chaile kono nirdishto character diye oi jayga purno korte parbo
print(name.center(100)) #prottek pashe 100 pixel space dibe.
print(name.center(50, "O")) #ekhane O diye prottek pashe 50 pixel kore purno korbe
        #prothome length of padding, tarpore character of padding
        #[length beshi choto hole, character ta show kore na]

      #count(); ekta nirdishto value kotobar ekta string e ache, sheita bole
print("Joy Bangla".count("g")) #1
print("Joy Bangla".count("Bang")) #1

      #encode(); Returns an encoded version of the string
print("Valobasha".encode()) #b'Valobasha' (wtf is encoded? b er abar kaj ki?)

      #endswith(); Amra jei value dilam, ta diye oi string ta shesh hoy na, sheta check kore
print("Jhaira Lok".endswith("k")) #True
print("Jhaira Lok".endswith("Lok")) #True

      #expandtabs(); Sets the tab size of the string

      #find(); Searches the string for a specified value and returns the position of where it was found
        
      #format(); Formats specified values in a string

      #format_map(); Formats specified values in a string

      #index(); Searches the string for a specified value and returns the position of where it was found
        
      #isalnum(); Returns True if all characters in the string are alphanumeric

      #isalpha(); Returns True if all characters in the string are in the alphabet

      #isascii(); Returns True if all characters in the string are ascii characters

      #isdecimal(); Returns True if all characters in the string are decimals

      #isdigit(); Returns True if all characters in the string are digits

      #isidentifier(); Returns True if the string is an identifier

      #islower(); Returns True if all characters in the string are lower case

      #isnumeric(); Returns True if all characters in the string are numeric

      #isprintable(); Returns True if all characters in the string are printable

      #isspace(); Returns True if all characters in the string are whitespaces

      #istitle(); Returns True if the string follows the rules of a title

      #isupper(); Returns True if all characters in the string are upper case

      #join(); Converts the elements of an iterable into a string

      #ljust(); Returns a left justified version of the string

      #lstrip(); Returns a left trim version of the string

      #maketrans(); Returns a translation table to be used in translations

      #partition(); Returns a tuple where the string is parted into three parts

      #replace(); Returns a string where a specified value is replaced with a specified value

      #rfind(); Searches the string for a specified value and returns the last position of where it was found
        
      #rindex(); Searches the string for a specified value and returns the last position of where it was found
        
      #rjust(); Returns a right justified version of the string
        
      #rpartition(); Returns a tuple where the string is parted into three parts
        
      #rsplit(); Splits the string at the specified separator, and returns a list
        
      #rstrip(); Returns a right trim version of the string
        
      #split(); Splits the string at the specified separator, and returns a list
        
      #splitlines(); Splits the string at line breaks and returns a list

      #startswith(); Returns true if the string starts with the specified value

      #strip(); Returns a trimmed version of the string

      #swapcase(); Swaps cases, lower case becomes upper case and vice versa

      #title(); Converts the first character of each word to upper case

      #translate(); Returns a translated string

      #upper(); Converts a string into upper case

      #zfill(); Fills the string with a specified number of 0 values at the beginning