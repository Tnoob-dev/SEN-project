import json
import os

if not os.path.exists("./docs/"):
    os.mkdir("./docs/")

def gen(init_day: int, last_day: int, month: int, year: int):
    file = open("./plantilla_SEN.json")
    content = json.loads(file.read())
    
    for i in range(init_day, last_day + 1):    
        with open(f"./docs/{year}{month if month > 10 else str(f"0{month}")}{i}.json", "w") as file:
            file.write(json.dumps(content, indent=4))
        
        with open(f"./docs/{year}{month if month > 10 else str(f"0{month}")}{i}.txt", "w") as file:
            file.write("")

gen(17, 28, 7, 2024)