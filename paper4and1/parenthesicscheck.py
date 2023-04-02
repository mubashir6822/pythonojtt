'''/ — Opens or begins regex.
\( — Escapes a single opening parenthesis literal.
[^()] —Any character that is not (^) an opening or closing parenthesis (( or )). 
The brackets represent a character class, and when combined with a caret following the opening bracket ([^)
\) — Escapes a single closing parenthesis literal.
/ — Closes the regex.
'''

import re

def valid_par(s: str) :
    pattern = r'\(\)|\[\]|\{\}'  # Matches valid pairs of parentheses, brackets, and braces
    while re.search(pattern, s):
        s = re.sub(pattern,'', s)
    return not  s

pair=input()
print(valid_par(pair))  
 
