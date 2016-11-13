print('Type in a word.')
word=raw_input()
print('Now type in a letter')
letter=raw_input()

def letter_search(letter,word):
    index_number=[]
    search_pointer=0
    while word.find(letter,search_pointer)!=-1:
        result=word.find(letter,search_pointer )
        search_pointer=result+1
        # index_number=index_number+[result]
        index_number.append(result)
    return index_number

def replace_letter(word,number,letter):
    return word[0:number]+letter+word[number:]



answer=replace_letter('school',1,'k')
print(answer)
letter_search(letter,word)
letter_search(letter,word)
