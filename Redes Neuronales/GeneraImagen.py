from PIL import Image, ImageDraw, ImageFont
import string

def generar_imagen_letra(letra, tamaño_imagen, tamaño_fuente, archivo_salida):
    # Crear una imagen en blanco (modo 'L' para blanco y negro)
    imagen = Image.new('L', (tamaño_imagen, tamaño_imagen), color=255)  # Color 255 es blanco
    
    # Dibujar sobre la imagen
    draw = ImageDraw.Draw(imagen)
    
    # Configurar la fuente
    try:
        # Intenta cargar una fuente del sistema (puedes especificar una fuente en tu sistema)
        fuente = ImageFont.truetype("arial.ttf", tamaño_fuente)
    except IOError:
        # Si no puede cargar la fuente, usar una fuente predeterminada
        fuente = ImageFont.load_default()
    
    # Obtener las dimensiones del cuadro delimitador del texto
    bbox = draw.textbbox((0, 0), letra, font=fuente)
    ancho_texto, alto_texto = bbox[2] - bbox[0], bbox[3] - bbox[1]
    
    # Calcular la posición para centrar la letra
    posicion_x = (tamaño_imagen - ancho_texto) // 2
    posicion_y = (tamaño_imagen - alto_texto) // 2
    
    # Dibujar la letra en la imagen (color 0 es negro)
    draw.text((posicion_x, posicion_y), letra, font=fuente, fill=0)
    
    # Guardar la imagen
    imagen.save(archivo_salida)
    print(f"Imagen guardada como {archivo_salida}")
    
    # Mostrar la imagen
    imagen.show()

def main():
    for letra in string.ascii_uppercase:
        # Imagen de 9x9
        generar_imagen_letra(letra, tamaño_imagen=9, tamaño_fuente=12, archivo_salida=f"{letra}_9x9.png")

        # Imagen de 15x15
        generar_imagen_letra(letra, tamaño_imagen=15, tamaño_fuente=20, archivo_salida=f"{letra}_15x15.png")

if __name__ == "__main__":
    main()
