# auto[2]    ó    auto["marca"]

perfil_vacio = {} # inicializo un diccionario vacio

usuario_instagram = {
    "username": "@JuanPro",
    "seguidores": 4353,
    "verificado": True,
    "post_guardados": ["foto_playa", "meme_python"]
}

producto = {"nombre": "teclado mecanico", "precio": 76.99, "stock": 45}

# 1. Leer un valor (acceso)
print(usuario_instagram["username"]) # Resultado: "@JuanPro"
print(usuario_instagram["verificado"]) # resultado: True

# Modificar un valor
usuario_instagram["seguidores"] = 4600 # actualizanos el valor de la llave corres.
usuario_instagram["seguidores"] += 1
print(usuario_instagram["seguidores"]) # Resultado: 4601

# Agregar un nuevo par clave : valor
usuario_instagram["edad"] = 25 # si no existe la llave "edad" se crea
usuario_instagram["edad"] = 34 # si ya existe, se sobreescribe el valor

print(usuario_instagram)

# Eliminar
del usuario_instagram["post_guardados"]

print(usuario_instagram)

# Error de sintaxis común
print(usuario_instagram["pais"])