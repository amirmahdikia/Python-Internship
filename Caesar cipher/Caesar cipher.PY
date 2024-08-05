english_alphabet = ["a"	,"b" ,"c" ,"d" ,"e" ,"f" ,"g" ,"h" ,"i"	,"j" ,"k" ,"l" ,"m"	,"n" ,"o" ,"p" ,"q"	,"r" ,"s" ,"t" ,"u" ,"v" ,"w" ,"x" ,"y" ,"z",
                    "a","b" ,"c" ,"d" ,"e" ,"f" ,"g" ,"h" ,"i"	,"j" ,"k" ,"l" ,"m"	,"n" ,"o" ,"p" ,"q"	,"r" ,"s" ,"t" ,"u" ,"v" ,"w" ,"x" ,"y" ,"z"]

word = str.lower(input("please write your word : "))

shift = int(input("please enter your shift : "))

new_shift = shift % 26

shifted_word = ""

for letter in word :

    letter_index = english_alphabet.index(letter)

    new_index = letter_index + new_shift
    
    shifted_letter = english_alphabet[new_index]
    
    shifted_word = shifted_word + shifted_letter
    
print(shifted_word)