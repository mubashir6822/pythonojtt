'''/ — Opens or begins regex.
\( — Escapes a single opening parenthesis literal.
[^()] —Any character that is not (^) an opening or closing parenthesis (( or )). 
The brackets represent a character class, and when combined with a caret following the opening bracket ([^)
\) — Escapes a single closing parenthesis literal.
/ — Closes the regex.
'''
import re

html = "<divvv>some content</divvv> <p>more content</p> <img> <param> </param>"
pattern = r"<[a-zA-Z]{5,}>|</[a-zA-Z]{5,}>"
matches = re.findall(pattern, html)

print(matches)