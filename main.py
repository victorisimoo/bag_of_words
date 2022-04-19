# establecimiento del universo

spam = ['offer is secret', 'click secret link', 'secret sports link']
ham = ['play sports today', 'went play sports', 'secret sports event', 'sports is today', 'sports cost money']

# probabilidad de que una palabra sea spam o ham
total_sentences = len(spam) + len(ham)
p_spam = len(spam) / total_sentences
p_ham = len(ham) / total_sentences

# print (p_spam)
# print (p_ham)

# creación de tablas de frecuencias
def crear_tabla_frecuencias(corpus):
    frecuencias = {}
    for oracion in corpus:
        tokens = oracion.split(" ")
        for token in tokens:
            if token not in frecuencias.keys():
                frecuencias[token] = 1
            else:
                frecuencias[token] += 1
    return frecuencias

# cuenta la cantidad de palabras del universo
def contar_palabras(corpus):
    frecuencia = 0
    for oracion in corpus:
        frecuencia += len(oracion.split(" "))
    return frecuencia

# frecuencia de las palabras en el universo
frecuencia_spam = crear_tabla_frecuencias(spam)
frecuencia_ham = crear_tabla_frecuencias(ham)

total_spam = contar_palabras(spam)
total_ham = contar_palabras(ham)

# print(total_spam)
# print(total_ham)


# frecuencia_spam - cuenta total de cada palabra dentro del universo de spam
# P(M="secret"| SPAM) = frecuencia_secret / total_palabras_spam
p_secret = frecuencia_spam["secret"] / total_spam

# transformador de frecuencia en probabilidad
def transformar_frecuencia_probabilidad(frecuencia, total):
    cpt_equivalente = {}
    for k, v in frecuencia.items():
        probabilidad = v / total
        cpt_equivalente[k] = probabilidad
    return cpt_equivalente

cpt_spam = transformar_frecuencia_probabilidad(frecuencia_spam, total_spam)
cpt_ham  = transformar_frecuencia_probabilidad(frecuencia_ham, total_ham)

# print (cpt_spam)
# print (cpt_ham)

p_mensaje_spam = (cpt_spam['sports'] * p_spam)/(cpt_spam['sports'] * p_spam + cpt_ham['sports'] * p_ham)

p_mensaje_completo = (cpt_spam['secret'] * cpt_spam['secret'] * cpt_spam['is'] * p_spam) / ((cpt_spam['secret'] * cpt_spam['secret'] * cpt_spam['is'] * p_spam) + (cpt_ham['secret'] * cpt_ham['secret'] * cpt_ham['is'] * p_ham))
print (p_mensaje_completo)