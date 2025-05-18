import qrcode

def generate_qr_code(url, filename="qr_code.png"):
    # Create a QRCode object with desired settings
    qr = qrcode.QRCode(
        version=1,  # size of the QR Code
    )
    
    # Add the URL to the QR code
    qr.add_data(url)
    qr.make(fit=True)

    # Generate the image
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image
    img.save(filename)
    print(f"Successfully saved the QRCode in: '{filename}'.")

if __name__ == "__main__":
    print("Welcome to the QR Code Generator!!")
    url_input = input("Please enter the URL: ").strip()
    generate_qr_code(url_input)
