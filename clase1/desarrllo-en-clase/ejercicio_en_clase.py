""""
Instrucciones Crea una lista llamada comentarios con cuatro frases Y luego usa un Ciclo for para revisar cada comentario, Si el comentario contiene la palabra "muere" O "spoiler", Imprime "Comentario oculto por alerta de spoiler" Sí no imprime El comentario normal.
"""
comentarios = ["me encanta tu contenido", "cuidado con el spoiler", "qué gran foto", "ayer vi la pelicula"]

for comentario in comentarios:
    if comentario.__contains__("muerte"):
        print("COMENTARIO OCULTO POR SER INAPROPIADO")
    elif comentario.__contains__("spoiler"):
        print("COMENTARIO OCULTO POR ALERTA DE SPOILER")
    else:
        print(comentario)