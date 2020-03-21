'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    count = 0
    return count_th_helper(word,count)

def count_th(word):
    count = {'c':0}
    return helper(word,count)

def helper(word,count):
    if (word == ""):
         return 0
    elif (word[-2:] == "th"):
        count['c'] += 1
        helper(word[:-1],count)
    else: 
        helper(word[:-1],count)
    return count['c']
