from sys import stdin


def highestOccuringChar(string):
    maxcount = 0
    dictionary = dict()
    for char in string:
        count =  dictionary.get(char,0) + 1
        dictionary[char] = count

    for char in string:
        if dictionary[char]>maxcount:
            maxchar = char
            maxcount = dictionary[char]
    return maxchar



# Your code goes here


# main
string = stdin.readline().strip();
ans = highestOccuringChar(string)

print(ans)