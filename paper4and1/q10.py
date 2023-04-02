match = 'version'
given='Upgraded_image_version_8.0.4.3'
if match in given:
    print('YES')
else:
    print('NO')

print('using input method -->')

match = input('enter  :')

given='Upgraded_image_version_8.0.4.3'
if match in given:
    print('YES')
else:
    print('NO')

# ------------------------

match='version'

val=8
# print(match+val)
print(match + str(val))


def m(s):
    if s==10:
        return not s
print(m(10))