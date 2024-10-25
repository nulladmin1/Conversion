import os
import tomllib
from PIL import Image, UnidentifiedImageError

class ConversionApp:
    def __init__(self):
        with open('conversion/supported.toml', 'rb') as f:
            self.supported_files = tomllib.load(f)
    def img_convert(self, input_file: str, output_file: str) -> None:
        input_image: Image = Image.open(input_file)
        input_image.convert('RGB').save(output_file)
def main():
    conversion_app = ConversionApp()
    input_file = input("Please enter image file name: ")
    if not os.path.isfile(input_file):
        raise FileNotFoundError("File does not exist")
    output_file = input("Please enter output image file name: ")
    conversion_app.img_convert(input_file, output_file)

if __name__ == "__main__":
    main()
