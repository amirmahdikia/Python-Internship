import random

letter_list = ["a","b" ,"c" ,"d" ,"e" ,"f" ,"g" ,"h" ,"i","j" ,"k" ,"l" ,"m","n" ,"o" ,"p" ,"q"	,"r" ,"s" ,"t" ,"u" ,"v" ,"w" ,"x" ,"y" ,"z"]
integer_list = ["1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "0"]
character_list = ["!" , "@" , "#" , "$" , "%" , "^" , "&" , "*" , "(" , ")" , "_" , "-" , "=" , "+" , "{" , "}" , "|" , "/" , "." , "," , "<" , ">" , ""]

number_letter = int(input("how mane letter do you want ? "))

empty_string = []

for item in range(number_letter) :

    choosen_letter = random.choice(letter_list)

    empty_string += choosen_letter


number_character = int(input("how many character do you want ? "))

empty_character = []

for character in range(number_character) :

    choosen_character = random.choice(character_list)

    empty_character += choosen_character


number_integer = int(input("how many integer do you want ? "))

empty_integer = []

for int in range(number_integer) :

    choosen_integer = random.choice(integer_list)

    empty_integer += choosen_integer


word = empty_string + empty_character + empty_integer

word_size = len(word)

password = ""

for indicator in range(word_size) :

    word_choice = random.choice(word)
    password += word_choice
    word.remove(word_choice)
    
print(password)