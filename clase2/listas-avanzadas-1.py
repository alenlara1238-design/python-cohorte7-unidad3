# Cada sublista representa un post: [likes, Comentarios, Compartidos]

feed_estadisticas = [
    [160, 45, 56], # Post 0 (foto de playa)
    [2500, 69, 34], # Post 1 (Meme de programacion)
    [43, 78, 12] # Post 2 (Video de cocina)
]

# Cómo accedemos a los datos en esta estructura?
print(feed_estadisticas[1])

# Y si queremos acceder a los comentarios?
comentarios = feed_estadisticas[1][1]
print(f"El meme tiene {comentarios} comentarios")

compartido = feed_estadisticas[2][2]
print(f"El video de cocina ha sido {compartido} veces compartida")

feed_estadisticas[2][2] = feed_estadisticas[2][2] + 1

print(f"estadisticas actualizadas del video de cocina: {feed_estadisticas[2]}")

feed_estadisticas[1][0] = feed_estadisticas[1][0] + 1

# Cómo recorremos la lista de listas
"""
# Cada sublista representa un post: [likes, Comentarios, Compartidos]
feed_estadisticas = [
    [160, 45, 56], # Post 0 (foto de playa)
    [2500, 69, 34], # Post 1 (Meme de programacion)
    [43, 78, 12] # Post 2 (Video de cocina)
]
"""
for estadistica in feed_estadisticas:
    print(f"Post -> likes:{estadistica[0]} | Comentarios: {estadistica[1]} | Compartido: {estadistica[2]}")