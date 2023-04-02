'''/ — Opens or begins regex.
\( — Escapes a single opening parenthesis literal.
[^()] —Any character that is not (^) an opening or closing parenthesis (( or )). 
The brackets represent a character class, and when combined with a caret following the opening bracket ([^)
\) — Escapes a single closing parenthesis literal.
/ — Closes the regex.
'''

import re

data = ["example (.com)", "MSys", "github (.com)", "keka (.com)"]

for s in data:
    # Use regular expression to match the parenthesis and its contents
    match = re.search(r'\([^)]*\)', s)
    if match:
        # Remove the matched substring
        s = s.replace(match.group(),'')
    print(s)
    # print(list[s])



# # =================================
given = ["example (.com)", "MSys", "github (.com)", "keka (.com)"]

for d in given:
    result2 = ''.join(c for c in d if c not in '()')
    print(result2)