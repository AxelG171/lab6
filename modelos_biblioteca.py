def agregar_categoria(categorias: set, nueva_categoria: str) -> set:
    categorias.add(nueva_categoria)
    return categorias


def registrar_libro(
        inventario: dict,
        isbn: str, titulo: str, 
        autor: str,
        categoria: str, 
        categorias: set
        ) -> tuple:
    libro = (titulo, autor, categoria)
    inventario[isbn] = libro
    agregar_categoria(categorias, categoria)
    return inventario, categorias


def registrar_usuario(usuarios: dict, id_usuario: str, nombre: str) -> dict:
    usuarios[id_usuario] = {
        "nombre": nombre,
        "libros_prestados": [],
    }
    return usuarios


def prestar_libro(
        isbn: str, 
        id_usuario: str, 
        inventario: dict, 
        usuarios: dict
        ) -> dict:
    if isbn in inventario and id_usuario in usuarios:
        usuarios[id_usuario]["libros_prestados"].append(isbn)
        del inventario[isbn]
    return usuarios
