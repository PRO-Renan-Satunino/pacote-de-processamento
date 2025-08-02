from image_utils.core import open_image, resize_image, convert_to_grayscale, save_image
import os

def test_pipeline():
    img = open_image("tests/sample.jpg")
    img = resize_image(img, (100, 100))
    img = convert_to_grayscale(img)
    save_path = "tests/output.jpg"
    save_image(img, save_path)

    assert os.path.exists(save_path)
