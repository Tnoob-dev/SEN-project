#  JSON files for extracting information regarding the National Electric System (in spanish SEN)

[Json files can be found at jsons folder](./jsons/)
<br>
[txt files can be found at txts folder](./txts/)
<br>
[Json files about plants info can be found at plants folder](./plants/)

### Data to extract:
    - Zones with problems
    - Date
    - URL
    - Prediction:
        - Availability
        - Max Demand
        - Impact
        - Deficit
        - Backup
    - Morning Info:
        - Time
        - Availability
        - Demand
        - Deficit
    - Plants:
        - ID
        - Broken
        - Maintenance
        - Limitation
    - Distributed:
        - Motors with problems
        - Total Impact
        - Combustible problems
        - Ships with problems
        - Motors Impact

### SEN.json:

```json
{
    "zones_with_problems": ["west" , "middle", "east"], 
    "date": "",
    "url": "", 
    "prediction": {
        "availability": "",  
        "demand_max": "",
        "impact": "",
        "deficit": "",
        "backup": ""
    },
    "morning_info": {
        "time": "", 
        "availability": "", 
        "demand": "", 
        "deficit": "" 
    }, 
    "plants": [
        {
            "id":"",
            "broken": [],
            "maintenance": [],
            "limitation": ""
    } 
],
    "distributed": {
        "motors_with_problems": "",
        "total_impact": "",
        "combustible_problem": "",
        "snips_with_problems": "",
        "motors_impact": ""
    },
    "impact": {
        "total_hours": "",
        "max": "",
        "max_hour": ""
    }
}
```

### plants.json:

```json
{
    "MG": {
        "name": "CTE Máximo Gómez",
        "location": "Artemisa,Mariel",
        "national_fuel":true,
        "units": {
            "5": {
                "power": 90
            },
            "6": {
                "power": 100
            },
            "7": {
                "power": 90
            },
            "8": {
                "power": 90
            }
        }
    },
    "OP": {
        "name": "CTE Otto Parellada",
        "location": "La Habana,La Habana Vieja",
        "national_fuel":false,
        "units": {
            "7": {
                "power": 60
            }
        }
    },
    "EG": {
        "name": "CTE Ernesto Guevara",
        "location": "Mayabeque,Santa Cruz del Norte",
        "national_fuel":true,
        "units": {
            "1": {
                "power": 100
            },
            "2": {
                "power": 100
            },
            "3": {
                "power": 95
            }
        }
    },
    "AG": {
        "name": "CTE Antonio Guiteras",
        "location": "Matanzas,Matanzas",
        "national_fuel":true,
        "units": {
            "1": {
                "power": 317
            }
        }
    },
    "CM": {
        "name": "CTE Carlos Manuel de Céspedes",
        "location": "Cienfuegos,Cienfuegos",
        "national_fuel":true,
        "units": {
            "3": {
                "power": 158
            },
            "4": {
                "power": 158
            }
        }
    },
    "DO": {
        "name": "CTE Diez de Octubre",
        "location": " Camagüey,Nuevitas",
        "national_fuel":false,
        "units": {
            "4": {
                "power": 125
            },
            "5": {
                "power": 125
            },
            "6": {
                "power": 125
            }
        }
    },
    "LR": {
        "name": "CTE Lidio Ramón Pérez",
        "location": "Holguín ,Felton",
        "national_fuel":false,
        "units": {
            "1": {
                "power": 250
            },
            "2": {
                "power": 230
            }
        }
    },
    "AM": {
        "name": "CTE Antonio Maceo",
        "location": "Santiago de Cuba,Renté Peninsula",
        "national_fuel":true,
        "units": {
            "4": {
                "power": 95
            },
            "5": {
                "power": 95
            },
            "6": {
                "power": 95
            },
            "7": {
                "power": 95
            }
        }
    },
    "EV": {
        "name": "Energas Varadero",
        "location": "Matanzas,Cárdenas",
        "national_fuel":true,
        "units": {
            "1": {
                "power": 160
            }
        }
    },
    "EB": {
        "name": "Energas Boca de Jaruco",
        "location": "Mayabeque,Boca de Jaruco,",
        "national_fuel":true,
        "units": {
            "1": {
                "power": 320
            }
        }
    }
}
```