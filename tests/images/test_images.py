import os
import unittest

from conversion.main import ConversionApp

from PIL import UnidentifiedImageError

class TestImages(unittest.TestCase):
    conversion_app = ConversionApp()
    default_input = os.path.join(conversion_app.ROOT_DIR, "../tests/images/Tux.png")
    default_output = os.path.join(conversion_app.ROOT_DIR, "../tests/images/Tux.jpg")
    def test_png_to_jpg(self):
        print(self.conversion_app.ROOT_DIR)
        input_file = self.default_input
        output_file = self.default_output

        self.conversion_app.img_convert(input_file, output_file)

        assert os.path.isfile(output_file)

    def test_not_supported_ending(self):
        input_file = os.path.join(self.conversion_app.ROOT_DIR, "../tests/images/Tux.pdf")
        output_file = self.default_output

        with self.assertRaises(UnidentifiedImageError):
            self.conversion_app.img_convert(input_file, output_file)

    def test_input_not_exists(self):
        input_file = os.path.join(self.conversion_app.ROOT_DIR, "../tests/images/Tux.bmp")
        output_file = self.default_output

        with self.assertRaises(FileNotFoundError):
            self.conversion_app.img_convert(input_file, output_file)

    def test_output_already_exists(self):
        input_file = self.default_input
        output_file = self.default_input

        with self.assertRaises(FileExistsError):
            self.conversion_app.img_convert(input_file, output_file)

    def tearDown(self):
        if os.path.isfile(self.default_output):
            os.remove(self.default_output)

    if __name__ == "__main__":
        unittest.main()