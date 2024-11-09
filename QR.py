import qrcode
import os
import re

def generate_upi_qr_codes(upi_id, payment_urls):
    """Generates QR codes for given UPI ID and payment URLs."""

    # Validate UPI ID
    if not re.match(r"^[a-zA-Z0-9@.]+$", upi_id):
        raise ValueError("Invalid UPI ID format. Please enter a valid UPI ID.")

    # Create QR codes for each payment URL
    for app, url in payment_urls.items():
        qr_code = qrcode.make(url.format(upi_id=upi_id))
        qr_code.save(f"{app.lower()}_qr.png")

    print("QR codes generated successfully!")

if __name__ == "__main__":
    upi_id = input("Enter your UPI ID: ")

    # Define payment URLs with placeholders (replace with actual parameters)
    payment_urls = {
        "PhonePe": "upi://pay?pa={upi_id}&pn=Recipient%20Name&am=1&cu=INR",
        "Paytm": "upi://pay?pa={upi_id}&pn=Recipient%20Name",
        "Google Pay": "upi://pay?pa={upi_id}&pn=Recipient%20Name"
    }

    try:
        generate_upi_qr_codes(upi_id, payment_urls)
    except ValueError as e:
        print(e)