<p align="center"><img src="https://i.imgur.com/e8KL7xj.png" /></p>

# Image Encoder

Embed strings or entire files in a image. All without noticing a difference in the image.

_Note: This is NOT meant for encryption, all data is CLEARTEXT and fully visible for anyone who checks the source code of the image._

## Requirements

I have only used Python 3.9 with standard libraries. It should work for any Python 3.X version running Windows, MacOS or Linux.

## Installation

### Git

```sh
git clone https://github.com/marcusfrdk/image-encoder.git
```

### Manual Download

![How to download the repository](https://i.imgur.com/iRoazjY.png)

## How to use

### Encode

```sh
python encode.py path data
```

- data - if the string is equal to a path where a jpg, jpeg or png file exists. It will read the file and encode this as the data. Otherwise it will take whatever string you supply.

### Decode

```sh
python decode.py path
```

## Example

### Encoding strings

```sh
python encode.py example.jpg "Hello World"
# Encoding string...
```

### Encoding files

```sh
python encode.py example.jpg example.txt
# Encoding file...
```

### Decoding files

```sh
python decode.py example-encoded.jpg
```

## Flags

### Encode

| Flag       | Description                                         | Required | Type            |
| ---------- | --------------------------------------------------- | -------- | --------------- |
| path       | The path to the source image.                       | Yes      | path            |
| data       | The data to be encoded, can be a path or a string.  | Yes      | path or string  |
| -n, --name | Set the output file's name.                         | No       | string          |

### Decode

| Flag                   | Description                          | Required  | Type    |
| ---------------------- | ------------------------------------ | --------- | ------- |
| path                   | The path to the image                | Yes       | path    |
| -a, --all              | Output the entire message            | No        | boolean |
| -t, --time             | Outputs the time it was encoded      | No        | boolean |
| -b, --build            | Rebuilds an encoded file             | No        | boolean |
| -re, --remove-encoding | Removed the encoded data from a file | No        | boolean |

## FAQ

### What can this be used for?

Encoding files with data ([steganography](https://en.wikipedia.org/wiki/Steganography)) can be used for many things, but it is primarily used for hiding messages. Allowing only people who know how to decode it to read the message.

### How does it work?

Steganography can be done in many ways, but this implementation simply appends the message after the "FF D9" hex code, which is the official end to any image file. Meaning the image won't be affected.

### Can I contribute code?

Of course! I would be more than happy if you would do that.

## Todo

- [ ] Encrypt the encoded messages
- [ ] Add a simple local webserver people can use instead of the terminal.
- [ ] Containerize functions and simplify functionality.
- [ ] Unit testing among other tests
- [ ] Support more file types, such as audio, video and text files.

## Notes

- I've only tested this on Linux (Ubuntu 20.04) and MacOS (Big sur). It might not work fully as expected on Windows. I will test this as soon as possible.
- This project is only for fun and should never be used in production or mission critical projects.

## Credits

### Example image

Photo by [Marius Tandberg](https://unsplash.com/@mbtandberg?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/photos/USw5NJ6Lkxw)

### Inspiration

I got inspiration to do this project thanks to [NeuralNine](https://www.youtube.com/watch?v=r-7d3w5xerY).
