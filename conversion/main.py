from conversion import ConversionApp


def main():
    conversion_app = ConversionApp()
    input_file = input("Please enter image file name: ")
    output_file = input("Please enter output image file name: ")
    conversion_app.img_convert(input_file, output_file)

if __name__ == "__main__":
    main()
