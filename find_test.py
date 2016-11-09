#print('Type in a word.')
#word=raw_input()
#print('Now type in a letter')
#letter=raw_input()
#
def letter_search(letter,word):
    index_number=[]
    search_pointer=0
    while word.find(letter,search_pointer)!=-1:
        result=word.find(letter,search_pointer )
#        print(result)
        search_pointer=result+1
        index_number=[result]
        return result
    index_number=[result]
    
letter_search('o','school')
#letter_search(letter,word)
