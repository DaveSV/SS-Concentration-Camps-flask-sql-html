# archivo >> SS_Camps_Definitive.xls
import sqlite3
import json
import codecs
# import pandas
import limpiarString

# excel_data_df = pandas.read_excel('SS_Camps_Definitive.xls', sheet_name='Sheet1', usecols=['SUBCAMP,C,254', 'LAT,N,19,11', 'LONG,N,19,11'])
# print(excel_data_df)

conn = sqlite3.connect('SS_Camps_Definitive.sqlite')
cur = conn.cursor()

datos = cur.execute('SELECT LAT_N_19_11, LONG_N_19_11, SUBCAMP_C_254 FROM Sheet1')


fhand = codecs.open('where.js', 'w', "utf-8")
fhand.write("myData = [\n")
count = 0
for dato in datos:
    
    lat = dato[0]
    lng = dato[1]
    where = dato[2]
    where = limpiarString.limpiar(where)
    count = count + 1
    if count > 1 : fhand.write(",\n")
    output = "["+ str(lat) + "," + str(lng) + ", '" + str(where) + "']"
    fhand.write(output)
    

fhand.write("\n];\n")
cur.close()
fhand.close()
print(count, "records written to where.js")
print("Open where.html to view the data in a browser")

