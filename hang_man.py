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
        break
print('GAME OVER!')



def replace_letters(target,numbers,letter_guess):
    for x in numbers:
        word=replace_letter(target,x,letter_guess)
        print(word)   
        
    return word

answer=replace_letters(target,[1,2,3],letter_guess)
print(answer)

