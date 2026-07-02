# Lista
feed_instagram = ["foto_playa", "meme_de_programacion", "video_gato"]
print("Tu feed inicial: ", feed_instagram)

# append(): para agregar un elemento al final de la lista (feed_instagram)

feed_instagram.append("foto_cena")
print("Tu feed actualizado: ", feed_instagram)

# insert : inserta elemento en la posición especificada
feed_instagram.insert(2, "PUBLICIDAD_ZAPATILLAS")
print("Tu feed actualizado después del insert: ", feed_instagram)

# remove() - pop()
feed_instagram.remove("PUBLICIDAD_ZAPATILLAS")

print(feed_instagram)

# a medida que consumimos el feed, instagram va eliminado el primer elemento de la lista
feed_instagram.pop(0)
print("Tu feed actualizado: ", feed_instagram)

# len() cuenta los elementos de la lista
print(f"te faltan {len(feed_instagram)} publicaiciones por ver.")











