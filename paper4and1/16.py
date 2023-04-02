with open("z.txt", "r") as f1:
    testname = f1.read().split()
with open("m.txt", "r") as f2:
    status = f2.read().split()

result_dict = {}
for key in testname:
    for val in status:
        if key in val:
            result_dict[key] = val.split('-')[-1]
print(result_dict)
