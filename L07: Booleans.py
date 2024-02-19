#Lesson 8: Booleans

    #[Boolean holo ekta data type jar shudhu duita value e thakte pare: True, False]
    #True aar False case sensitive. 1st letter capital hotei hobe
    #bool() command diye boolean prokash kora hoy

done = True

print(type(done) == bool) #True
print(isinstance(done, bool)) #True

if done:
    print("yes")
else:
    print("no")

    #0 baad e shokol shongkha (positive/negative etc) True
    #strings, parenthesis etc False hobe, jokhon empty(khali)

    #any() ekta function ja diye check kora hoy, ontoto ekta jinish True ache ki na
book_1_read = True
book_2_read = False

read_any_book = any([book_1_read, book_2_read]) #any er vitore list akare duita jinish rakhlam

print(read_any_book) #True; karon ontoto ekta ekhane True ache

    #shobgulai True ki na, sheta check korar jonno bebohar kora hoy all() function
ingredients_purchased = True
meal_cooked = False

ready_to_serve = all([ingredients_purchased, meal_cooked]) #all er vitore list akare input dilam

print(ready_to_serve); #False; karon shobgula ekhane True na