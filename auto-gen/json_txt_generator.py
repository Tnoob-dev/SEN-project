import json
import os

paths = ["../jsons/", "../txts/", "../plants/"]

for path in paths:
    if not os.path.exists(path):
        os.mkdir(path)

def gen(init_day: int, last_day: int, month: int, year: int):
    file = open("./SEN.json")
    plants_file = open("./plants.json")
    
    content = json.loads(file.read())
    plants_content = json.loads(plants_file.read())
    
    for i in range(init_day, last_day + 1):    
        with open(f"../jsons/{year}{month if month > 10 else str(f"0{month}")}{i if i > 10 else str(f"0{i}")}.json", "w") as file:
            file.write(json.dumps(content, indent=4))
        
        with open(f"../plants/plants-{year}{month if month > 10 else str(f"0{month}")}{i if i > 10 else str(f"0{i}")}.json", "w") as file:
            file.write(json.dumps(plants_content, indent=4))
        
        with open(f"../docs/{year}{month if month > 10 else str(f"0{month}")}{i if i > 10 else str(f"0{i}")}.txt", "w") as file:
            file.write("")

# use example
# gen(15, 28, 7, 2024)