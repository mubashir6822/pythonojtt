from datetime import datetime
emp_dict={
    "priya":{
            "loc":"hyd",
            "date":"05/09/2022"
            },
    "mubu":{
            "loc":"hyd",
            "date":"05/08/2022"
            },
    "mahi":{
            "loc":"bangalore",
            "date":"10/12/2023"
            },
    "raja":{
            "loc":"bangalore",
            "date":"14/10/2022"
            },
    "prabhu":{
                "loc":"hyd",
                "date":"02/01/2023"
             }
}
# req_location=input("entr your req location: ")
# doj =input("enter req date: ").split("/")
# # print(doj)
# for key,value in emp_dict.items():
#         if value["loc"]=="hyd" :
#             if int(doj[-2])>=int(value["date"].split("/")[-2]):
#                 # print(value["date"].split("/")[-2])
#                 print(key)
req_date='02/09/2022'
c=datetime.strptime(req_date,'%d/%m/%Y')
print(c)
for key,values in emp_dict.items():
     print(key,values['date'])