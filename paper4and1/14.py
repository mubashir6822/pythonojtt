import json
def jsonread():
    with open("new.json", "r") as f1:
        # testname = f1.read()
        data=json.load(f1)
        return data
        # print(testname)
print(jsonread())