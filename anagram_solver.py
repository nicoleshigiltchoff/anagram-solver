####PREPROCESSING####

import csv
import sys
from itertools import combinations

alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
all_words=set()

for letter in alphabet:

    letter_words = open('words/'+letter+'word.csv')
    csv_f = csv.reader(letter_words)

#preprocessing of every word and adding it to all_words
    for word in csv_f:
        str_word_1="".join(word) #turn list into string. each word is initially a list of chars.
        str_word_2=str_word_1.strip() #remove spaces at end and beginning
        
        #if there's a weird situation with \n, split by that and strip
        if "\n" in str_word_2:
            word_list=str_word_2.split("\n")
            for word in word_list:
                str_word_3=word.strip()
                all_words.add(str_word_3)
        else:
            all_words.add(str_word_2)
            
words_and_letters={} #a dictionary to hold a word and its letters

for word in all_words:
    words_and_letters[word]=list(word)
    
def all_letter_anagram(scramble_list, duplicate=False): #finds anagrams using all the given letters
    unscrambled_words=[]
    #finding the anagrams!
    for word in words_and_letters:
        #if words have the same length and the same letters, they're anagrams
        if len(scramble_list)==len(words_and_letters[word]) and sorted(scramble_list)==sorted(words_and_letters[word]):
            if duplicate:
                unscrambled_words.append(word)
            else:
                if list(scramble_list)!=words_and_letters[word]:
                    unscrambled_words.append(word)
            
    return unscrambled_words

def given_number_anagram(scramble_list, number): #finds anagrams of all subsections of given length
    unscrambled_words=[]
    
    all_combos=set(combinations(scramble_list, number)) #every combination of all the letters of a given length
    for combo in all_combos: #find words of all the combinations
        unscrambled_words=unscrambled_words+all_letter_anagram(list(combo), True)
        
    return unscrambled_words
    
def any_letter_anagram(scramble_list): #finds anagrams of all subsections of all length
    unscrambled_words=[]
    
    #find words of all possible lengths
    for length in range(2, len(scramble_list)+1):
        unscrambled_words=unscrambled_words+given_number_anagram(scramble_list, length)
            
    return unscrambled_words
    
def return_words(unscrambled_words): #grammatically correct messages to display the answers
    
    if len(unscrambled_words)==0:
        return str("there are no solutions to your letters in my dictionary")
        
    if len(unscrambled_words)==1:
        return str("your solution is "+str(unscrambled_words[0]))
        
    if len(unscrambled_words)==2:
        return str("your solutions are "+str(unscrambled_words[0])+" and "+str(unscrambled_words[1]))
     
    if len(unscrambled_words)>2:
        soln_str=""
        for i in range(len(unscrambled_words)-1):
            soln_str=soln_str+str(unscrambled_words[i])+", "
        soln_str.join(str("and "+unscrambled_words[-1]))
        soln_str=soln_str+"and "+str(unscrambled_words[-1])
        return str("your solutions are "+soln_str) 
    
def intro_message(): 
    #displays at the beginning of every run
    print()
    print("~~~~~~~~~~~")
    print("hello and welcome to Nicole's anagram maker!")
    print("you can type ''EXIT'' to leave at any time")
    print("small note: due to the word data I used containing mostly singular forms of nouns and infinitive of verbs,")
    print("this solver generally cannot find words that are plural nouns or non-infinitive forms of verbs")
    print()
    
def tier_1_qs(): #asks what type of anagram, and acts accordingly
    while True:
        
        scramble_list=input("what letters do you want an anagram for?  ").lower()
        
        if scramble_list=='EXIT':
            break
        elif not scramble_list.isalpha(): #tossed out for non-compliance
            print("enter only alphabetic characters, and try again")
        print()
        
        print("do you want to use all your letters, any number of your letters, or a certain number of your letters?")
        scramble_type=input("answer ''all-letter'' or ''any-letter'' or ''number''  ")
        print()
        if scramble_list=='EXIT' or scramble_type=='EXIT': #can start exiting with "EXIT"
            break
        
        elif scramble_type=="all-letter":
            print(return_words(all_letter_anagram(scramble_list)))
            break
            
        elif scramble_type=="any-letter":
            print(return_words(any_letter_anagram(scramble_list)))
            break
            
        elif scramble_type=="number":
            numerical_qs(scramble_list)
            break
        
        else: #tossed out for non-compliance
            print("enter either 'all-letter'', ''any-letter'' or ''number'', and try again")
            
def numerical_qs(scramble_list):
    
    number=input("how many letters do you want to use? enter a numerical answer  ")
    print()
    
    #checking to make sure answer is numeric, a whole number, and of reasonable length
    if number.isnumeric(): 
        if float(number)-int(number)==0:
            if int(number)<=len(scramble_list) and int(number)>=1:
                print(return_words(given_number_anagram(scramble_list, int(number))))
            
            #tossed out for non-compliance    
            else:
                print("enter a number between 1 and the word length, inclusive, and try again")
        else:
            print("enter a whole number, such as 2 or 2.0, and try again")
    else:
        print("enter a whole number, such as 2, and try again")

if __name__ == "__main__":
    intro_message()    
        
    while True:  
              
        tier_1_qs() 
        print()
        
        #play again or allow exit    
        play_again=input("do you want to do another word? answer 'yes' or 'no'  ")
        if play_again=="no" or play_again=="EXIT":
            break
        elif play_again=="yes":
            print()
        else:
            print()
            print("you said something other than ''yes'' or ''no'', so you have exited")
            print("you can rerun anagram_solver.py to play again")
            break

