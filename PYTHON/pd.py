import pandas as pd
import csv


mydict = [{"Country": "Brazil", "Capital": "Brasilia", "Area": 8.516, "Population": 200.4},
          {"Country": "Russia", "Capital": "Moscow", "Area": 17.10, "Population": 143.5},
          {"Country": "India", "Capital": "New Dehli", "Area": 3.286, "Population": 1252},
          {"Country": "China", "Capital": "Beijing", "Area": 9.597, "Population": 1357},
          {"Country": "South Africa", "Capital": "Pretoria", "Area": 1.221, "Population": 52.98}
]

fields = ["Country", "Capital", "Area", "Population"]
csv.register_dialect('myDialect',
                     quoting=csv.QUOTE_ALL
                    )

# Creating csv file (excel)
with open("mydict.csv", "w", newline='') as fp:
    fpw = csv.DictWriter(fp, fieldnames=fields, dialect='myDialect')
    fpw.writeheader()
    fpw.writerows(mydict)
    fp.close()

# Reading file using panda
brics = pd.DataFrame(mydict)
data = pd.read_csv("mydict.csv")
data.index = ["BR", "RU", "IN", "CH", "SA"]
print(data)



