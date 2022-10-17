import json

with open("start.txt", encoding="utf-8") as f:
    data = json.load(f)

ma = -1
mc = ""

countries = open("countries.txt", "w", encoding="utf-8")
squares = open("squares.txt", "w", encoding="utf-8")

for key in data.keys():
    countries.write(key+"\n")
    squares.write(str(data[key])+"\n")
    if int(data[key]) > ma:
        ma = int(data[key])
        mc = key

countries.close()
squares.close()

with open("largest.txt", "w", encoding="utf-8") as f:
    f.write(f"{mc} : {ma}")
