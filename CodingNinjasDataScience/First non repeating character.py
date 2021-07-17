"""
First non repeating character
Send Feedback
In a given string, find the first non-repeating character .You are given a string,
that can contain repeating characters.
Your task is to return the first character in this string that does not repeat. i.e., occurs exactly once.
The string will contain characters only from English alphabet set, i.e., ('A' - 'Z') and ('a' - 'z').
If there is no non-repeating character print the first character of string.
Input Format :
Line 1 : A String , as mentioned above.
Output Format :
First non-repeating character
Sample Input 1 :
aDcadhc
Sample Output 1:
D
Sample Input 2 :
gdhIgHada
Sample Output 2 :
h
"""


def nonRepeatingChar(string):
    # Please add your code here
    dictionary = dict()
    for ele in string:
        dictionary[ele] = dictionary.get(ele, 0) + 1
    for ele in string:
        if dictionary[ele] == 1:
            return ele


# Main
string = input()
print(nonRepeatingChar(string))
