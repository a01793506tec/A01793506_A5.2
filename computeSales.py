# pylint: disable=invalid-name
"""
Programa Actividad 5.2 Ejercicio de programación 2
A01793506 Erick Nájera Olivero
"""
import argparse
import json
import time


def leer_archivo(ruta_archivo):
    """ Funcion para cargar el archivo"""
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        contenido = json.load(archivo)
    return contenido


def obtener_precio_por_titulo(titulo_, datos):
    """ Funcion para obtener el precio del producto"""
    for producto in datos:
        if producto["title"] == titulo_:
            return producto["price"]
    return None


if __name__ == "__main__":
    with open('SalesResults.txt', 'w', encoding='latin-1') as result:
        inicio = time.time()
        parser = argparse.ArgumentParser(description='Leer archivos de texto.')
        parser.add_argument('priceCatalogue')
        parser.add_argument('salesRecord')
        args = parser.parse_args()

        contenido_archivo1 = leer_archivo(args.priceCatalogue)
        contenido_archivo2 = leer_archivo(args.salesRecord)

        coleccion = {}
        col_error = []

        for registro in contenido_archivo1:
            nombre = registro['title']
            detalle = registro['description']
            precio = registro['price']

        for elemento in contenido_archivo2:
            titulo = elemento.get("Product")
            cantidad = elemento.get("Quantity", 0)
            if titulo in coleccion:
                coleccion[titulo] += cantidad
            else:
                coleccion[titulo] = cantidad
        gtotal = 0

        header = (
          f"{'Producto':<40} | {'Cantidad':>10} |"
          f"{'Precio':>15} | {'Total':>10}"
                )
        print(header)

        header = (
          f"{'-' * 40:<40} | {'-' * 10:^10} |"
          f"{'-' * 15:>15} | {'-' * 10:>10}"
                )
        print(header)
        cuerpo = (
          f"{'Producto':<40} | {'Cantidad':>10} |"
          f"{'Precio':>15} | {'Total':>10}\n"
                )
        result.write(cuerpo)
        cuerpo = (
          f"{'-' * 40:<40} | {'-' * 10:^10} |"
          f"{'-' * 15:>15} | {'-' * 10:>10}\n"
                )
        result.write(cuerpo)

        for titulo, cantidad in coleccion.items():
            prec = obtener_precio_por_titulo(titulo, contenido_archivo1)
            if prec is not None:
                tot = prec * cantidad
                gtotal += tot
                tot = round(tot, 3)
                cuerpo = (
                 f"{titulo:<40} | {str(cantidad):>10} |"
                 f"{prec:>15,} | {str(tot):>10}"
                )
                print(cuerpo)
                cuerpo = (
                  f"{titulo:<40} | {str(cantidad):>10} |"
                  f"{prec:>15,} | {str(tot):>10}\n"
                        )
                result.write(cuerpo)

            else:
                col_error.append(titulo)

        inferior = (
          f"{'-' * 40:<40} | {'-' * 10:^10} |"
          f"{'-' * 15:>15} | {'-' * 10:>10}"
        )
        print(inferior)
        inferior = (
          f"{'':<40} | {'':>10} | {'':>15} |"
          f"{round(gtotal, 3):>10,}"
        )
        print(inferior)

        inferior = (
          f"{'-' * 40:<40} | {'-' * 10:^10} |"
          f" {'-' * 15:>15} | {'-' * 10:>10}\n"
        )
        result.write(inferior)
        inferior = (
          f"{'':<40} | {'':>10} | {'':>15} |"
          f"{round(gtotal, 3):>10,}\n"
        )
        result.write(inferior)

        print()
        if col_error:
            mensaje = (
              "Los siguientes productos no se encontraron"
              "en el catálogo de precios:"
                    )
            print(mensaje)
            result.write("\n")
            result.write(mensaje)
            for titulo in col_error:
                print(format(titulo))
                result.write(f"{titulo:<50}\n")
        fin = time.time()
        tiempo_total = fin - inicio
        print()
        print("El tiempo de ejecución fue de:", tiempo_total, "segundos")
        result.write("\n")
        result.write(f"El tiempo de ejecución fue de:{tiempo_total}")
