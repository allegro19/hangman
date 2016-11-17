target = 'parkrun'
lives = 9
word ='-'*len(target)
print('Guess a letter')
print(word)
while True:
    letter_guess = raw_input()
    lives = lives-1
    if lives >=1:
       print(str(lives) + ' lives left')
       print(word)
    if lives <=0:




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
    lives = lives-1
    if lives >=1:
       print(str(lives) + ' lives left')
       print(word)
    if lives <=0:

        answer=replace_letters(word,[],letter_guess)
        print(answer)

        break

print('GAME OVER!')
