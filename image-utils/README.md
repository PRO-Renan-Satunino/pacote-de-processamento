# image_utils

Um pacote simples de processamento de imagens em Python usando Pillow.

## Funcionalidades

- Abrir imagens
- Redimensionar
- Converter para tons de cinza
- Salvar imagem

## Instalação

```bash
pip install .
```

## Exemplo de uso

```python
from image_utils import open_image, resize_image, convert_to_grayscale, save_image

img = open_image("foto.jpg")
img = resize_image(img, (200, 200))
img = convert_to_grayscale(img)
save_image(img, "foto_editada.jpg")
```
