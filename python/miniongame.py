def minion_game(string):
    # your code goes here
    string = string.lower()
    l = len(string)
    Kevin_score = 0
    Stuart_score = 0
    for i in range(l):
        if string[i] in "aeiou":
            Kevin_score += l-i
        else:
            Stuart_score+=l-i
    if Stuart_score > Kevin_score:
        print("Stuart {}".format(Stuart_score))
    elif Stuart_score < Kevin_score:
        print("Kevin {}".format(Kevin_score))
    else:
        print("Draw")
if __name__ == '__main__':
