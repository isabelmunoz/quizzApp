preguntas_basicas = {
    'pregunta_1': {'enunciado':['¿Cuántos litros de sangre tiene una persona adulta?'],
    'alternativas': [['Tiene entre 2 y 4 litros', 0],
                     ['Tiene entre 4 y 6 litros', 1],
                     ['Tiene 10 litros', 0],
                     ['Tiene 0,5 litros', 0]]},

    'pregunta_2': {'enunciado':['¿Quién es el autor de la frase "Pienso, luego existo"?'],
    'alternativas': [['Platón', 0],
                     ['Galileo Galilei', 0],
                     ['Descartes', 1],
                     ['Sócrates', 0]]},
    
    'pregunta_3': {'enunciado':['¿Cuál es el país más grande y el más pequeño del mundo?'],
    'alternativas': [['Canadá y Mónaco', 0],
                     ['China y Nauru', 0],
                     ['Estados Unidos y Malta', 0],
                     ['Rusia y Vaticano', 1]]}
}
preguntas_intermedias = {
    'pregunta_1': {'enunciado':['¿Cuál es el libro más vendido en el mundo después de la Biblia?'],
    'alternativas': [['El Señor de los Anillos', 0],
                     ['Don Quijote de la Mancha', 1],
                     ['El Principito', 0],
                     ['La Odisea', 0]]},

    'pregunta_2': {'enunciado':['¿Cuántos decimales tiene el número pi π?'],
    'alternativas': [['Cien', 0],
                     ['Mil', 0],
                     ['Dos', 0],
                     ['Infinitos', 1]]},
    
    'pregunta_3': {'enunciado':['La sal común está formada por dos elementos, ¿cuáles son?'],
    'alternativas': [['Sodio y potasio', 0],
                     ['sodio y cloro', 1],
                     ['Potasio y cloro', 0],
                     ['Cristal y sodio', 0]]}
}

preguntas_avanzadas = {
    'pregunta_1': {'enunciado':['¿Cuáles son los representantes más destacados de la literatura renacentista?'],
    'alternativas': [['Goethe, Victor Hugo, Gustavo Adolfo Bécquer', 0],
                     ['Caravaggio, Bernini, Borromini', 0],
                     ['Miguel de Cervantes, William Shakespeare, Luis de Camões', 1],
                     ['Leonardo da Vinci, Miguel Angel Buonarroti, Sandro Boticelli', 0]]},

    'pregunta_2': {'enunciado':['¿En qué orden se presentaron los modelos atómicos?'],
    'alternativas': [['Bohr, Rutherford, cuántico, Einstein', 0],
                     ['Dalton, Thomson, Rutherford, cuántico', 1],
                     ['Dalton, Einstein, cuántico, Sheldon Cooper', 0],
                     ['Rutherford, Dalton, Thomson, cuántico', 0]]},
    
    'pregunta_3': {'enunciado':['¿En qué periodo de la prehistoria fue descubierto el fuego?'],
    'alternativas': [['paleolítico', 1],
                     ['Edad de piedra', 0],
                     ['Neolítico', 0],
                     ['Edad media', 0]]}
}

pool_preguntas = {'basicas': preguntas_basicas,
                  'intermedias': preguntas_intermedias,
                  'avanzadas': preguntas_avanzadas}