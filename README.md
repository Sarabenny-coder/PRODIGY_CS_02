# PRODIGY_CS_02
Pixel Manipulation for Image Encryption
This project is part of the Prodigy InfoTech Cybersecurity Internship.

### Description

A Python tool to encrypt and decrypt images using basic pixel manipulation.  
It performs mathematical operations on RGB values to scramble or restore an image.

Users can:
- Choose whether to encrypt or decrypt an image.
- Input the image file (preferably `.png`).
- Provide a numeric key to perform the operation.
- Save the encrypted/decrypted image.

> ⚠️ Recommended image format: `.png` (lossless).  
> Avoid `.jpg` files as they may result in inaccurate decryption due to compression.

### How to Run

1. Make sure you have Python and Pillow installed:
   ```bash
   pip install pillow
Run the script using:

bash
Copy
Edit
python image_cipher.py
Follow the prompts:

Input image file (with .png extension)

Output image filename

Encryption/decryption key (number)
