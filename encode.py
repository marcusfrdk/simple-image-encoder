import argparse
import os

def get_arguments() -> dict:
    parser = argparse.ArgumentParser(description="Encode strings or files to an image as JSON.", usage="encode.py path")
    parser.add_argument("path", help="path to the image to be encoded, must be jpg or png")
    parser.add_argument("-s", "--string", dest="string", metavar="", help="store the string in an image")
    parser.add_argument("-f", "--file", dest="file", metavar="", help="stringify a file and store it in an image")
    return parser.parse_args()


def validate_image(path: str) -> bool:
    valid_extensions = ("jpg", "jpeg", "png")

    is_file = os.path.isfile(path)
    extension_is_valid = path.split(".")[-1] in valid_extensions \
        if "." in path else False

    return is_file and extension_is_valid


def parse_input(args: dict) -> str:
    if args.string:
        return str(args.string)
    elif args.file:
        with open(args.file) as f:
            return str(f.read())
    else:
        return ""


def extract_path(path: str) -> tuple:
    prepath = ""
    name = ""
    extension = ""

    # Get prepath
    if "/" in path:
        prepath = "".join([f"{x}/" for x in path.split("/")[0:-1]])

    # Get name
    if "." in path:
        name = path.split(".")[-2].replace("/", "")

        # Get extension
        extension = path.split(".")[-1]

    return prepath, name, extension


def encode(path: str, input: str) -> None:
    try:
        lines = open(path, "rb").readlines()
        prepath, name, extension = extract_path(path)

        new_name = name + "-encoded" + f".{extension}"
        number = 1

        # Make sure file does not exist
        while os.path.exists(new_name):
            new_name = name + "-encoded" + f"-{number}" + f".{extension}"

        # Encoode file
        with open(new_name, "wb") as encoded_image:
            encoded_image.writelines(lines)
            encoded_image.write(bytes(input, "utf-8"))
            encoded_image.close()
    except:
        print("Failed to encode image, please try again.")

def main() -> None:
    args = get_arguments()
    
    if validate_image(args.path):
        input = parse_input(args)

        if input:
            encode(args.path, input)
        else:
            print("Nothing to encode, please use the -s or -f flags.")
    else:
        print("Image is not valid, try another one.")


if __name__ == "__main__":
    main()