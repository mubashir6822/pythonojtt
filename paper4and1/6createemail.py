username=input("Entern your Username : ")
department=input("Entern your Department : ")
service=input("Enter Service name : ")
    # define a function for creating an  email
# def create_email(username, department):
def create_email(username, department,service):
    # if any uppecase letters are there in username and department it convert to lowercase
    username = username.lower()
    department = department.lower()
    service= service.lower()
    # create the email ID by concatenating the username, department, service ,"@" symbol, and ".com"
    # email = username + "." +department+ "@gmail" + ".com"

    email = username + "." +department+ "@" + service + ".com"
    
    return email
    



created=create_email(username,department,service)

print(created)

if created.endswith(".com"):
    print("valid email")
else:
    print("invalid email")

# check email ends with .com 