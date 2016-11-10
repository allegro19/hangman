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


searchletter=letter_search(letter,word)
print(searchletter)
letter_search(letter,word)
