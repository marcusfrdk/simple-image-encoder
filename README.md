<p align="center"><img src="https://i.imgur.com/Uo1Ad45.png" /></p>

# Image Encoder

Encode a string or a file to an image.

## Requirements

- Python 3 or greater

## How to use

### Encode

```bash
python3 encode.py PATH
```

#### Required Flags

_One of the following._

- -s, --string -> String to be encoded
- -f, --file -> File to be encoded

#### Optional Flags

- -n, --name -> Name of the output file, will overwrite a file if it exists.

### Decode

```bash
python3 decode.py PATH
```

## Todo

- [ ] If encoding a file that is already encoded, overwrite the encoded content
- [ ] Add support for encoding a file type and creating a file with that type and content.
- [ ] Add support for files with multiple dots
- [ ] Add support for embedding images in other images

## Credit

### Example image

Photo by [Marius Tandberg](https://unsplash.com/@mbtandberg?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/photos/USw5NJ6Lkxw)

### Inspiration

I got inspiration to do this project thanks to [NeuralNine](https://www.youtube.com/watch?v=r-7d3w5xerY).
