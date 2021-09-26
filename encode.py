import argparse
import os
import time

def get_arguments() -> dict:
    """ Returns the programs arguments """
    parser = argparse.ArgumentParser(description="Encode strings or files to an image as JSON.", usage="encode.py image data")
    parser.add_argument("image", help="path to the image to be encoded.")
    parser.add_argument("data", help="data to be encoded, if the string is a path, the file will be encoded, else the provided string will be used.")
    parser.add_argument("-n", "--name", dest="name", metavar="", help="saves the output image with the selected name, will overwrite an existing file.")
    return parser.parse_args()


def extract_path(path: str) -> tuple:
    """ Extracts information from a path """
    sections = path.split(".")[-2:]
    name = sections[0].split("/")[-1]
    extension = sections[-1]

    return name, extension


def get_output_name(args: dict) -> str:
    """ Gets a valid name for the output file """
    name, extension = extract_path(args.image)

    output_name = name + "-encoded" + f".{extension}"
    number = 1

    if args.name:
        output_name = args.name + f".{extension}"
    else:
        # Make sure file does not exist
        while os.path.exists(output_name):
            output_name = name + "-encoded" + f"-{number}" + f".{extension}"
            number += 1

    return output_name


def parse_data(data: str) -> str:
    """ 
    Parses the dynamic input and returns the data.
    If a file, it reads the file and returns its contents, otherwise
    it will return the data as a string.
    """
    is_file = os.path.isfile(data)
    result = data
    if is_file:
        with open(data) as f:
            result = f.read()
            f.close()
    return result


def format_data(data: str) -> bytes:
    """ Formats the data to the optimal format """
    is_file = os.path.isfile(data)
    file_type = data.split(".")[-1] if "." in data and is_file else ""
    encoded_at = time.time()

    print("Encoding file..." if file_type else "Encoding string...")

    return bytes(str({
        "file_type": file_type,
        "encoded_at": encoded_at,
        "data": parse_data(data)
    }), "utf-8")


def validate_image(path: str) -> bool:
    """ Checks and makes sure the input image is valid """
    valid_extensions = ("jpg", "jpeg", "png")

    is_file = os.path.isfile(path)
    extension_is_valid = path.split(".")[-1] in valid_extensions \
        if "." in path else False

    return is_file and extension_is_valid


def encode_image(args: dict)  -> None:
    """ Encodes the output image """

    data = format_data(args.data)
    name = get_output_name(args)

    # Get image and remove encoding
    image = ""
    with open(args.image, "rb") as of:
        content = of.read()
        offset = content.index(bytes.fromhex("FFD9")) + 2
        image = content[0:offset]
        of.close()

    with open(name, "wb") as nf:
        nf.write(image + data)
        nf.close()


def main() -> None:
    """ The main program """
    args = get_arguments()

    if validate_image(args.image):
        encode_image(args)
    else:
        print("Image is not valid.")
        

if __name__ == "__main__":
    main()
