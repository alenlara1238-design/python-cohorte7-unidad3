class Post:
    def __init__(self, usuario, likes, es_video):
        self.usuario = usuario
        self.likes = likes
        self.es_video = es_video # Guarda un valor boolean (True:False)


feed_instagram = [
    Post("@JulioDev2026", 150, False),
    Post("@JuanDavid_Crack_python", 2500, True),
    Post("@Mafer-Dark-Silent", 567, True)
]

print(f"Hemos cargado {len(feed_instagram)} objetos Post en el feed")
print(feed_instagram[1].usuario)
print(feed_instagram[2].likes)

# feed_instagram[1].likes = feed_instagram[1].likes + 1
feed_instagram[1].likes += 1

# supongamo que hay un nuevo post que quiero agregar a la lista:
nuevo_post = Post("@python-user", 0, False)
feed_instagram.append(nuevo_post)

# recorrer la lsta de objetos
for post in feed_instagram:
    print(f"usuario: {post.usuario}")
    print(f"likes: {post.likes}")
    print("-"*40)

