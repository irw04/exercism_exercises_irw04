def transform(legacy_data):
    reformat = {}

    for score, letter_list in legacy_data.items(): 
        #outer loop to get the dict and iteratations
        for letter in letter_list:
        #inner loop to see the key and it's values ec {key: valu, value, value}
            reformat[letter.lower()] = score
            #putting the NEW lowercase letter as the key, and giving it a value that is the score. 
    return reformat