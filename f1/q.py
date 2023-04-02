import os

for file in os.listdir():
    if file.endswith(".txt") or file.endswith(".csv"):
        if file.endswith(".csv"):
            os.rename(file, "{}/{}".format("csv_d",file))
        else:
            os.rename(file, "{}/{}".format("txt_d",file))