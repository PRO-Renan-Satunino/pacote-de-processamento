from image_utils import open_image, resize_image, convert_to_grayscale, save_image

input_path = "tests/sample.jpg"

img = open_image(input_path)

img = resize_image(img, (100, 100))

img = convert_to_grayscale(img)

output_path = "tests/output.jpg"
save_image(img, output_path)

print(f"imagem processada com sucesso! Arquivo salvo em: {output_path}")