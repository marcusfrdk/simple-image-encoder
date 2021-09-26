import argparse
import os
import time

def get_arguments() -> dict:
    parser = argparse.ArgumentParser(description="Encode strings or files to an image as JSON.", usage="encode.py path")
    parser.add_argument("image", help="path to the image to be encoded.")
    parser.add_argument("data", help="data to be encoded, if the string is a path, the file will be encoded, else the provided string will be used.")
    parser.add_argument("-n", "--name", dest="name", metavar="", help="saves the encoded image with the name, will overwrite any existing file with the same name.")
    return parser.parse_args()


def extract_path(path: str) -> tuple:
    sections = path.split(".")[-2:]
    name = sections[0].split("/")[-1]
    extension = sections[-1]

    return name, extension


def get_output_name(args: dict) -> str:
    name, extension = extract_path(args.image)

    new_name = name + "-encoded" + f".{extension}"
    number = 1

    if args.name:
        new_name = args.name + f".{extension}"
    else:
        # Make sure file does not exist
        while os.path.exists(new_name):
            new_name = name + "-encoded" + f"-{number}" + f".{extension}"
            number += 1

    return new_name


def parse_data(data: str) -> str:
    is_file = os.path.isfile(data)
    result = data
    if is_file:
        with open(data) as f:
            result = f.read()
    return result


def format_data(data: str) -> bytes:
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
    valid_extensions = ("jpg", "jpeg", "png")

    is_file = os.path.isfile(path)
    extension_is_valid = path.split(".")[-1] in valid_extensions \
        if "." in path else False

    return is_file and extension_is_valid


def encode_image(args: dict)  -> None:
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
    args = get_arguments()

    if validate_image(args.image):
        encode_image(args)
    else:
        print("Image is not valid.")
        

if __name__ == "__main__":
    main()
