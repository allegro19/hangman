import random
medium_word = 'parkrun','cherry','bannana','flip flops','school','guitar','camera','pigglet'
easy_word = 'cat','dog','hat','tree','ziva','sat','cat'
hard_word = 'adaptation','variation','sufficient','insufficient','systematically'
print('Hello,please select a level ')
print('m ,for medium')
print('e for easy')
print('h for hard.')
level = raw_input()
if level=='m':
   target = random.choice(medium_word)
if level=='e':
    target = random.choice(easy_word)
if level=='h':
    target = random.choice(hard_word)
def letter_search(letter,word):
    index_number=[]
    search_pointer=0
    while word.find(letter,search_pointer)!=-1:
        result=word.find(letter,search_pointer )
        search_pointer=result+1
        index_number.append(result)
    return index_number


def replace_letter(word,number,letter):
    return word[0:number]+letter+word[number+1:]
        
        
def replace_letters(word,numbers,letter_guess):
    for x in numbers:
        word=replace_letter(word,x,letter_guess)
        print(word)   
        
    return word
lives = 9
word ='-'*len(target)
print('Guess a letter')
print(word)
while True:
    print(str(lives) + ' lives left')
    print('please type in a letter.') 
    letter_guess = raw_input()
    if target.find(letter_guess,0)==-1:
        lives=lives-1
        print('incorrect guess')
        if lives==0:
            print('GAME OVER!')
            print('your word was' +target)
            break
    else:
        word=replace_letters(word,letter_search(letter_guess,target),letter_guess)
        print(word)
        print('Yes! good guess.')
        if word==target:
            print('well done')
            break 
print('would you like to play again?')
print('y/n')
play_again=raw_input()
if play_again=='no':
    print('Bye bye:)')
    print('thank you for playing.')
