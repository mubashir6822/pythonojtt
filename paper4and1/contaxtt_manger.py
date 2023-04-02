with open('m.txt', 'r') as f:
  contents = f.read()
  print(contents)

print(f.closed)

# why we have to use contaxt manager while openng a file

'''WHAT IS THE WITH STATEMENT IN PYTHON?
1.In Python, the with statement replaces a try-catch block with a concise shorthand. 
2.More importantly, it ensures closing resources right after processing them. 
3.A common example of using the with statement is reading or writing to a file. 
4.A function or class that supports the with statement is known as a context manager. 
  A context manager allows you to open and close resources right when you want to. 
5.For example, the open() function is a context manager. When you call the 
  open() function using the with statement, the file closes automatically after you've processed the file.'''