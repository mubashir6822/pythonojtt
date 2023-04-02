import os
files = [f for f in os.listdir() if '.txt' in f.lower() or '.csv' in f.lower()]
print(files)
for file in files:
    print(file)
    if file.endswith('.csv'):
        new_path1 = 'csv_d/' + file
        os.rename(file, new_path1)
        
    else:
        print(file)
        new_path = 'txt_d/' + file
        os.rename(file, new_path)



# files = [f for f in os.listdir() if '.jpg' in f.lower()]
# file2 = [f for f in os.listdir() if '.txt' in f.lower()]
# for file in files:
#     if file.endswith('.csv'):
#         new_path1 = 'csv_d/' + file
#         os.rename(file, new_path1)
        
# for file in file2:
#     if file.endswith('.txt'):
#         new_path = 'txt_d/' + file
#         os.rename(file, new_path1)