#RAFAEL RICARDO DAZA SOLARTE
texto = 'este es un texto el cual deben contar el numero de palabras que tiene, debe tener en cuenta, que las palabras escritas EN MAYUSCULAS y minusculas cuenta como una este. Texto'
ignorar=",;:.\n!\"'"
for quitar in ignorar:
    texto = texto.replace(quitar," ")

texto = texto.lower()
palabras = texto.split(" ")
repeticiones={}
for palabra in palabras:
    if palabra in repeticiones:
        repeticiones[palabra] += 1
    else:
        repeticiones[palabra] = 1
for palabra in repeticiones:
    repetidas = repeticiones[palabra]
    print(f"La Palabra'{palabra}' se repite por '{repetidas}'vez")