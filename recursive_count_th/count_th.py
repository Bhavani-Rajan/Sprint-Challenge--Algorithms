'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
cache = {'c':0}

def count_th(word):
    #print(word)
    if (word == ""):
     return 0
    elif (word[-2:] == "th"):
        #print(" found th")
        cache['c'] += 1
        count_th(word[:-1])
    else: 
        #print("not found")
        count_th(word[:-1])
    return cache['c']
