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
target = 'parkrun'
lives = 9
word ='-'*len(target)
print('Guess a letter')
print(word)
while True:
    letter_guess = raw_input()
    if letter_guess==target:
       print(str(lives) + ' lives left')
       answer=replace_letters(word,letter_search(letter_guess,target),letter_guess)
       print(answer)
    lives = lives-1
    if lives <=0:


        break
print('GAME OVER!')

