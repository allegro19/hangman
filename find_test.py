def letter_search():
    print('Type in a word.')
    word=raw_input()
    print('Now type in a letter')
    letter=raw_input()
    search_pointer=0
    while word.find(letter,search_pointer)!=-1:
        result=word.find(letter,search_pointer )
        print(result)
        search_pointer=result+1

letter_search()
