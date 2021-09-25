import os
import argparse
from encode import validate_image

def get_arguments() -> dict:
    parser = argparse.ArgumentParser(description="Decode an encoded image.", usage="decode.py path")
    parser.add_argument("path", help="Path to the image to be decoded.")
    return parser.parse_args()


def decode_image(args: dict) -> str: 
    if validate_image(args.path):
        decoded = ""
        with open(args.path, "rb") as encoded_file:
            content = encoded_file.read()
            offset = content.index(bytes.fromhex("FFD9"))

            encoded_file.seek(offset + 2)
            decoded = bytes.decode(encoded_file.read())
            
        return decoded
    else:
        return ""


if __name__ == "__main__":
    args = get_arguments()

    if os.path.isfile(args.path):
        decoded = decode_image(args)
        if decoded:
            print(decoded)
        else:
            print("Found no encoded information.")
    else:
        print("Image not found, please try another path.")
