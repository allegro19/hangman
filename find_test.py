print('Type in a word.')
word=raw_input()
print('Now type in a letter')
letter=raw_input()
index_number=[]

def letter_search(letter,word):
    search_pointer=0
    while word.find(letter,search_pointer)!=-1:
        result=word.find(letter,search_pointer )
#        print(result)
        search_pointer=result+1
index_number=[letter,word]
print(index_number)
letter_search('o','school')
letter_search('e','elephant')
letter_search(letter,word)
