target = 'parkrun'
lives = 9
word ='-'*len(target)
print('Guess a letter')
print(word)
while True:
    leter_guess = raw_input()
    lives = lives-1
    if lives >=1:
       print(str(lives) + ' lives left')
       print(word)
    if lives <=0:
        break
print('GAME OVER!')
