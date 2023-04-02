with open('input.txt', 'r') as file1:
    urls = file1.read().splitlines()

with open('output.txt', 'w') as file:   
    for url in urls:
        if url.startswith('https://'):
            if any(char in url for char in ',*&%$#@! ') or ' ' in url:
                file.write(f'{url} invalid\n')
            else:
                file.write(f'{url} valid\n')
        else:
            file.write(f'{url} invalid\n')
    

f=open('output.txt')
print(f.read())