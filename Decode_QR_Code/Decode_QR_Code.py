''' QR Code Decoder '''
# Reads a QR code from an image file (PNG, JPG) and decodes the data inside it.


import cv2
import os


#  SETTINGS — change these as you like
IMAGE_FILE = "qrcode.png"    # Path to your QR code image


def decode_qr(image_file):
    print(f"\n Decoding QR code from: {image_file}\n")

    # Check if file exists
    if not os.path.exists(image_file):
        print(f" Error: File '{image_file}' not found!")
        return

    # Open the image
    img = cv2.imread(image_file)

    # Create QR code detector
    detector = cv2.QRCodeDetector()

    # Decode the QR code
    data, bbox, _ = detector.detectAndDecode(img)

    # Check if any QR code was found
    if not data:
        print(" No QR code found in the image!")
        return

    # Print the results
    print(f"   Type : QRCODE")
    print(f"   Data : {data}")
    print()


if __name__ == "__main__":
    decode_qr(IMAGE_FILE)