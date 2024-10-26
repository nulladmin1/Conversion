import os
import tomllib
from PIL import Image, UnidentifiedImageError

class ConversionApp:
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    def __init__(self):
        supported_toml = os.path.join(self.ROOT_DIR, "supported.toml")
        with open(supported_toml, 'rb') as f:
            self.supported_files = tomllib.load(f)
    def img_convert(self, input_file: str, output_file: str) -> None:
        images = self.supported_files['image']
        input_file_ending = input_file.split('.')[-1]
        output_file_ending = output_file.split('.')[-1]
        if input_file_ending not in images or output_file_ending not in images :
            raise UnidentifiedImageError(f"{input_file} is not a supported image format. Supported include: {self.supported_files['image']}")
        if not os.path.isfile(input_file):
            raise FileNotFoundError(f"Image file '{input_file}' does not exist.")
        if os.path.isfile(output_file):
            raise FileExistsError(f"Output file '{output_file}' already exists.")

        input_image: Image = Image.open(input_file)
        input_image.convert('RGB').save(output_file)
def main():
    conversion_app = ConversionApp()
    input_file = input("Please enter image file name: ")
    output_file = input("Please enter output image file name: ")
    conversion_app.img_convert(input_file, output_file)

if __name__ == "__main__":
    main()
