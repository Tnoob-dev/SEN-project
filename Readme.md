# JSONs para la extraccion de informacion acerca del Sistema Electrico Nacional (SEN)

### Datos a extraer:
    - Informacion principal:
        - Fecha
        - Dia
        - URL

    - Estimacion:
        - Horario
        - Disponibilidad
        - Demanda Maxima
        - Deficit
        - Pronostico:
            - Afectacion

    - Info de los horarios:
        - Mañana:
            - Cantidad de MW para la disponibilidad
            - Demanda prevista para ese horario
            - Totalidad del funcionamiento del SEN
        - Mediodia:
            - Pronostico:
                - Afectacion

    - Termoelectricas:
        - Limite en la Generacion Termica
        - Fuera de servicio:
            - Por averias:
                - Nombre de la Unidad
                - Nombre de la CTE
            - Por Mantenimiento:
                - Nombre de la Unidad
                - Nombre de la CTE

    - Centrales de Generacion Distribuida:
        - Sin servicio:
                - Cantidad de Centrales de Generacion Distribuida
                - Razon por la que se encuentra sin servicio
                - Cantidad de MW afectados

    - Pico:
        - Estimacion:
            - Descripcion de la estimacion
            - Razon por la que estuvieron fuera
            - Cantidad de MW totales
    
    - Maxima afectacion del dia:
        - Cantidad de MW afectados
        - Hora en la que ocurrio
        - Descripcion
    
    - Dia anterior:
        - Descripcion
        - Total de horas en las que se estuvo sin servicio
        - Hora en la que se restablecio

### Por lo que el JSON quedaria planteado asi (Tambien puede verlo en el archivo Plantilla_SEN.json):

```json
{
    "sen_info": {
        "main_info": {
            "_comentario": "Las fechas deben expresarse con guiones",
            "fecha": "",
            "dia": "",
            "url": ""
        },
        "_comentario": "Toda esta informacion se expresa en MW",
        "estimacion": {
            "horario": "",
            "disponibilidad": 0,
            "demanda_max": 0,
            "deficit": 0,
            "pronostico": {
                "afectacion": 0
            }
        },
        "info_horarios": {
            "mañana": {
                "disponibilidad": 0,
                "demanda": 0,
                "totalidad": true
            },
            "mediodia": {
                "pronostico": {
                    "afectacion": 0
                }
            }
        },
        "termoelectricas": {
            "_comentario": "Esto quiere decir: Limitaciones en la generacion termica",
            "lim_gen_term": 0,
            "fuera": {
                "averias": [
                    {
                        "nombre": "Unidad",
                        "CTE": ""
                    }
                ],
                "mantenimiento":[
                    {
                        "nombre": "Unidad",
                        "CTE": ""
                    }
                ]
            }
        },
        "centr_gen_distr": {
            "no_servicio": [
                {
                    "cantidad": 0,
                    "razon": "",
                    "mw_afectados": 0
                }
            ]
        },
        "pico": {
            "estimacion": [
                {
                    "desc": "",
                    "razon": "",
                    "cantidad_mw": 0
                }
            ]
        },
        "max_afect_dia": {
            "cantidad_mw": 0,
            "hora": "",
            "desc": ""
        },
        "dia_anterior": {
            "desc": "",
            "horas": 0,
            "hora_rest": ""
        }
    }
}
```