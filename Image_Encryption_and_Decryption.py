#Image Encryption and Decryption using Pixel Manipulation For image encryption, we'll modify pixel values, and to decrypt, 
#we’ll reverse the modification. This example adds a constant value to each pixel for encryption, and subtracts it for decryption.

from PIL import Image
import numpy as np

def encrypt_image(image_path, output_path, key=100):
    image = Image.open(image_path)
    img_array = np.array(image)

    # Encrypt by adding key to each pixel value
    encrypted_img_array = (img_array + key) % 256
    encrypted_image = Image.fromarray(encrypted_img_array.astype('uint8'))
    encrypted_image.save(output_path)
    print("Image encrypted and saved as:", output_path)

def decrypt_image(encrypted_image_path, output_path, key=100):
    encrypted_image = Image.open(encrypted_image_path)
    encrypted_img_array = np.array(encrypted_image)

    # Decrypt by subtracting key from each pixel value
    decrypted_img_array = (encrypted_img_array - key) % 256
    decrypted_image = Image.fromarray(decrypted_img_array.astype('uint8'))
    decrypted_image.save(output_path)
    print("Image decrypted and saved as:", output_path)

# Usage
encrypt_image("input_image.png", "encrypted_image.png")
decrypt_image("encrypted_image.png", "decrypted_image.png")


#This requires the Pillow library; install it via pip install pillow.
