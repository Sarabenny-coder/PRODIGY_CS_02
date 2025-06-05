from PIL import Image

# Function to encrypt the image
def encrypt_image(input_path, output_path, key):
    img = Image.open(input_path).convert("RGB")  # Ensure correct format
    pixels = img.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            pixels[i, j] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)

    img.save(output_path)
    print("✅ Image encrypted and saved as", output_path)

# Function to decrypt the image
def decrypt_image(input_path, output_path, key):
    img = Image.open(input_path).convert("RGB")
    pixels = img.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            pixels[i, j] = ((r - key) % 256, (g - key) % 256, (b - key) % 256)

    img.save(output_path)
    print("✅ Image decrypted and saved as", output_path)

# Main program
print("🔒 Image Encryption Tool")
print("1. Encrypt")
print("2. Decrypt")
choice = input("Choose (1 or 2): ")
input_image = input("Enter input image filename (with extension): ")
output_image = input("Enter output image filename (with extension): ")
key = int(input("Enter encryption/decryption key (number): "))

if choice == '1':
    encrypt_image(input_image, output_image, key)
elif choice == '2':
    decrypt_image(input_image, output_image, key)
else:
    print("⚠️ Invalid choice.")
