import re
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
'''
How regex works:
^        this represents the start of the line
[a-z0-9] this means a to z, 0 to 9. These are characters that can be put in that spot
[\._]?   this means a period character (.) can be put here, but not necessary
[@]    must contain @ sign
\w     similar to a to z and 0 to 9, but more available characters: [a-zA-Z0-9_]
[.]    must contain a period (.)
{2,3}    2-3 characters must match: (co, com, gov, org) is good, (a, comm, aaaa, gove) wont work
$        end of line
'''
def check(email):
    if(re.search(regex, email)):
        print("Valid Email")
    else:
        print("Invalid")

if __name__=='__main__':
    email = input("Enter Email Address: ")
    check(email)