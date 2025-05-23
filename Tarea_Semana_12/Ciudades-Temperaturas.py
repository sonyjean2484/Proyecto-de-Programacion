#Primera dimensión: Ciudades (Quito,Guayaquil,Cuenca)
#Segunda dimensión: Semanas (4 semanas)
#Tercera dimensión: Días de la semana (7 días)
#Creación de la matriz
temperatura = [
    [ # Quito
        [ # Semana 1
            {"dia":"Lunes","temp":18},
            {"dia":"Martes","temp":19},
            {"dia":"Miércoles","temp":20},
            {"dia":"Jueves","temp":16},
            {"dia":"Viernes","temp":15},
            {"dia":"Sábado","temp":17},
            {"dia":"Domingo","temp":21}
        ],
        [# Semana 2
            {"dia":"Lunes","temp":19},
            {"dia":"Martes","temp":18},
            {"dia":"Miércoles","temp":16},
            {"dia":"Jueves","temp":17},
            {"dia":"Viernes","temp":19},
            {"dia":"Sábado","temp":13},
            {"dia":"Domingo","temp":14}
        ],
        [# Semana 3
            {"dia":"Lunes","temp":16},
            {"dia":"Martes","temp":19},
            {"dia":"Miércoles","temp":18},
            {"dia":"Jueves","temp":21},
            {"dia":"Viernes","temp":17},
            {"dia":"Sábado","temp":19},
            {"dia":"Domingo","temp":20}
        ],
        [# Semana 4
            {"dia":"Lunes","temp":14},
            {"dia":"Martes","temp":17},
            {"dia":"Miércoles","temp":15},
            {"dia":"Jueves","temp":12},
            {"dia":"Viernes","temp":11},
            {"dia":"Sábado","temp":16},
            {"dia":"Domingo","temp":13}
        ]
    ],
    [# Guayaquil
        [ # Semana 1
            {"dia":"Lunes","temp":31},
            {"dia":"Martes","temp":32},
            {"dia":"Miércoles","temp":30},
            {"dia":"Jueves","temp":27},
            {"dia":"Viernes","temp":28},
            {"dia":"Sábado","temp":29},
            {"dia":"Domingo","temp":26}
        ],
        [# Semana 2
            {"dia":"Lunes","temp":33},
            {"dia":"Martes","temp":28},
            {"dia":"Miércoles","temp":32},
            {"dia":"Jueves","temp":27},
            {"dia":"Viernes","temp":29},
            {"dia":"Sábado","temp":31},
            {"dia":"Domingo","temp":29}
        ],
        [# Semana 3
            {"dia":"Lunes","temp":28},
            {"dia":"Martes","temp":29},
            {"dia":"Miércoles","temp":28},
            {"dia":"Jueves","temp":32},
            {"dia":"Viernes","temp":31},
            {"dia":"Sábado","temp":30},
            {"dia":"Domingo","temp":27}
        ],
        [# Semana 4
            {"dia":"Lunes","temp":31},
            {"dia":"Martes","temp":27},
            {"dia":"Miércoles","temp":25},
            {"dia":"Jueves","temp":32},
            {"dia":"Viernes","temp":31},
            {"dia":"Sábado","temp":26},
            {"dia":"Domingo","temp":29}
        ]
    ],
    [# Cuenca
        [ # Semana 1
            {"dia":"Lunes","temp":21},
            {"dia":"Martes","temp":22},
            {"dia":"Miércoles","temp":20},
            {"dia":"Jueves","temp":17},
            {"dia":"Viernes","temp":18},
            {"dia":"Sábado","temp":19},
            {"dia":"Domingo","temp":16}
        ],
        [# Semana 2
            {"dia":"Lunes","temp":23},
            {"dia":"Martes","temp":18},
            {"dia":"Miércoles","temp":22},
            {"dia":"Jueves","temp":17},
            {"dia":"Viernes","temp":19},
            {"dia":"Sábado","temp":21},
            {"dia":"Domingo","temp":19}
        ],
        [# Semana 3
            {"dia":"Lunes","temp":18},
            {"dia":"Martes","temp":19},
            {"dia":"Miércoles","temp":18},
            {"dia":"Jueves","temp":22},
            {"dia":"Viernes","temp":21},
            {"dia":"Sábado","temp":20},
            {"dia":"Domingo","temp":17}
        ],
        [# Semana 4
            {"dia":"Lunes","temp":21},
            {"dia":"Martes","temp":17},
            {"dia":"Miércoles","temp":15},
            {"dia":"Jueves","temp":22},
            {"dia":"Viernes","temp":21},
            {"dia":"Sábado","temp":16},
            {"dia":"Domingo","temp":19}
        ]
    ]
]
# Calcular el promedio de temperaturas para cada ciudad y por cada semana.
print("-------TEMPERTURAS--------")
ciudades=["QUITO","GUAYAQUIL","CUENCA"]
for ciudad_ind, ciudad in enumerate(temperatura):
    print(f"Ciudad: {ciudades[ciudad_ind]}")
    for semana_ind , semana in enumerate(ciudad):
        print(f"\tSemana {semana_ind+1}:", end=" ")
        suma = 0
        for dia in semana:
            suma += dia['temp']
        promedio= suma / len(semana)
        print(f"{promedio:.2f} °C")
