def _validar_lineas(lineas: list) -> None:
    if not isinstance(lineas, list) or len(lineas) == 0:
        raise ValueError("lineas debe ser una lista no vacía")
    for linea in lineas:
        if not isinstance(linea, str):
            raise ValueError("Cada línea debe ser una cadena de texto")


def parsear_producto(linea: str) -> dict:
    if not isinstance(linea, str):
        raise ValueError("linea debe ser una cadena de texto")

    partes = linea.split(",")
    if len(partes) != 4:
        raise ValueError("La línea debe tener exactamente 4 elementos")

    codigo, nombre, precio_texto, cantidad_texto = [parte.strip() for parte in partes]

    try:
        precio = float(precio_texto)
    except (TypeError, ValueError):
        raise ValueError("El precio debe ser un número válido")
    if precio < 0:
        raise ValueError("El precio no puede ser negativo")

    try:
        cantidad = int(cantidad_texto)
    except (TypeError, ValueError):
        raise ValueError("La cantidad debe ser un entero válido")
    if cantidad < 0:
        raise ValueError("La cantidad no puede ser negativa")

    return {
        "codigo": codigo,
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad,
    }


def resumen_de_producto(linea: str) -> str:
    producto = parsear_producto(linea)
    valor = round(producto["precio"] * producto["cantidad"], 1)
    return f'{producto["codigo"]} - {producto["nombre"]}: ${valor}'


def resumen_de_lotes(lineas: list) -> list:
    _validar_lineas(lineas)
    salida = []
    for linea in lineas:
        salida.append(resumen_de_producto(linea))
    return salida


def valor_de_lote(lineas: list) -> float:
    _validar_lineas(lineas)
    total = 0.0
    for linea in lineas:
        producto = parsear_producto(linea)
        total += producto["precio"] * producto["cantidad"]
    return round(total, 1)


def producto_maximo_valor(lineas: list) -> str:
    _validar_lineas(lineas)
    mejor = parsear_producto(lineas[0])
    mejor_valor = mejor["precio"] * mejor["cantidad"]

    for linea in lineas[1:]:
        producto = parsear_producto(linea)
        valor = producto["precio"] * producto["cantidad"]
        if valor > mejor_valor:
            mejor = producto
            mejor_valor = valor

    valor_redondeado = round(mejor_valor, 1)
    return f'{mejor["codigo"]} - {mejor["nombre"]}: ${valor_redondeado}'


if __name__ == "__main__":
    products = [
        "P001,Lapiz,0.5,100",
        "P002,Cuaderno,1.25,50",
        "P003 , Borrador ,1.35 , 10",
    ]
    print(resumen_de_producto(products[0]))
    print(resumen_de_lotes(products))
    print(valor_de_lote(products))
    print(producto_maximo_valor(products))
