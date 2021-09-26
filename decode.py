import os
import argparse
import ast
import traceback

def get_arguments() -> dict:
    parser = argparse.ArgumentParser(description="Decode an encoded image.", usage="decode.py image")
    parser.add_argument(
        "image", 
        help="path to the image to be decoded."
    )
    parser.add_argument(
        "-a", 
        "--all", 
        action="store_true", 
        help="outputs the entire encoding."
    )
    parser.add_argument(
        "-t", 
        "--time", 
        action="store_true", 
        help="reconstructs the encoded file."
    )
    parser.add_argument(
        "-b", 
        "--build", 
        action="store_true", 
        help="builds the encoded file."
    )
    parser.add_argument(
        "-re", 
        "--remove-encoding", 
        action="store_true", 
        help="removes the encoding from an encoded file."
    )
    return parser.parse_args()


def decode_image(image: str) -> dict:
    data = None

    with open(image, "rb") as f:
        content = f.read()
        offset = content.index(bytes.fromhex("FFD9")) + 2
        f.seek(offset)
        data = f.read().decode("utf-8")
        f.close()

    return dict(ast.literal_eval(data)) if data else dict()


def remove_encoding(path: str) -> None:
    try:
        image = ""
        with open(path, "rb") as rf:
            image = rf.read()

        with open(path, "wb") as wf:
            offset = image.index(bytes.fromhex("FFD9")) + 2
            wf.write(image[0:offset])
            wf.close()

        print("Encoding removed...")
    except Exception:
        traceback.print_exc()
        print("Failed to remove encoding.")

def build(data: dict) -> None:
    file_name = data["file_name"]
    file_type = data["file_type"]
    if file_name and file_type and data["data"]:
        with open(f"{file_name}-rebuild.{file_type}", "w") as f:
            f.write(data["data"])
            f.close()
    else:
        print("No file encoded.")


def main() -> None:
    args = get_arguments()

    if os.path.isfile(args.image):
        data = decode_image(args.image)

        if data:
            if args.build:
                build(data)
            elif args.remove_encoding:
                remove_encoding(args.image)
            else:
                # Just print
                if args.time:
                    print(data["encoded_at"])
                elif args.all:
                    print(data)
                else:
                    print(data["data"])
        else:
            print("No encoding found.")

    else:
        print("Image not found, please try another path.")


if __name__ == "__main__":
    main()