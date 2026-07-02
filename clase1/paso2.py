# las listas en python son todo terreno. No solo texto sino pueden guardar lo que sea! (incluzo mexclado)
# es una lista de elementos del mismo tipo
likes =[123, 565,232,535]

usuarios_verificados = [True, False, True]

perfil_usuario = ["@danipro", 25, 1.75, True]
#               [nombre usuario, edad, estatura, cuenta_activa]

# Acceso por indices

# De principio a fin (empieza en cero "0")
feed_instagram = ["foto_playa", "meme_de_programacion", "video_gato"]
#print(feed_instagram[2])
#print(feed_instagram[0])

# Desde el final hasta adelante ( lo contrario de indices positivos)
print(f"immprimiendo con indices nega: {feed_instagram[-2]}")


feed_instagram[1] ="meme de programación con Angular"
print(f"lista modificada: {feed_instagram}")

