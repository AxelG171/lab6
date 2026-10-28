import modelos_biblioteca

categorias = {"Novela", "Historia"}
inventario = {}
usuarios = {}


inventario, categorias = modelos_biblioteca.registrar_libro(
    inventario,
    "100-1",
    "Invisible",
    "Eloy Moreno",
    "Realismo mágico",
    categorias,
)

inventario, categorias = modelos_biblioteca.registrar_libro(
    inventario,
    "100-2",
    "Harry Potter y el caliz de fuego",
    "J.K. Rowling",
    "Fantasía",
    categorias,
)


usuarios = modelos_biblioteca.registrar_usuario(usuarios, "001", "Ana")
usuarios = modelos_biblioteca.registrar_usuario(usuarios, "002", "Luis")


usuarios = modelos_biblioteca.prestar_libro("100-1", "001", inventario, usuarios)

print("Inventario:", inventario)
print("Categorías:", categorias)
print("Usuarios:", usuarios)
