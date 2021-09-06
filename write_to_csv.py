import csv
from os import write


info =[ {
        "Name": "name",
        "Email": "email",
        "Message": "message"

    }]

fieldsname = ['Name','Email',"Message"]

with open('contact.csv','a', encoding="utf-8", newline='') as f: 
    writer = csv.DictWriter(f,fieldnames=fieldsname)
    writer.writerows(info)