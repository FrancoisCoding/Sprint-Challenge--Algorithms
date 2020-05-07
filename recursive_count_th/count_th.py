'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # If word is less than 2 than it can't contain 'th'
    if len(word) < 2:
        return 0

    # Place word in list 
    x = list(word)

    # Check if first two letters are 'th' and remove first letter and add 1
    if x[0] == "t" and x[1] == "h":
        x.remove(x[0])
        return 1 + count_th("".join(x))

    # Remove first letter because the first two letters are not 'th'
    else:
        x.remove(x[0])
        return 0 + count_th("".join(x))


# Letters are repeatedly checked and removed until no letters remain