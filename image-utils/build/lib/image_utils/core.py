from PIL import Image

def open_image(path):
    """Abre uma imagem a partir do caminho."""
    return Image.open(path)

def resize_image(image, size):
    """Redimensiona a imagem para o tamanho especificado (largura, altura)."""
    return image.resize(size)

def convert_to_grayscale(image):
    """Converte a imagem para tons de cinza."""
    return image.convert("L")

def save_image(image, path):
    """Salva a imagem no caminho especificado."""
    image.save(path)
