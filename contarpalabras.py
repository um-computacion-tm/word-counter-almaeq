def contar_palabras(sentence):
    quitar = ",;:.\n!\"'"
    for caracter in quitar:
        sentence = sentence.replace(caracter," ")
    sentence = sentence.lower()
    palabras_separadas = sentence.split()
    dicc_palabras = {}
    for palabra in palabras_separadas:
        if palabra in dicc_palabras:
            dicc_palabras[palabra] += 1
        else:
            dicc_palabras[palabra] = 1
    return dicc_palabras
