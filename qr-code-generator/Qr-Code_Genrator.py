import time
import qrcode


def generate_qr():
    print("=" * 40)
    print("      QR Code Generator")
    print("=" * 40)

    data = input("\nEnter text or URL: ").strip()

    if not data:
        print("Input cannot be empty.")
        return

    file_name = input("Enter file name (Press Enter for default): ").strip()

    if not file_name:
        file_name = "qrcode"

    print("\nGenerating QR Code",end = "")
    for i in range(5):
      print(".",end = "",flush = True) 
      time.sleep(0.1)

    qr_image = qrcode.make(data)
    qr_image.save(f"{file_name}.png")

    print("\n✅ QR Code created successfully!")
    print(f"📁 Saved as: {file_name}.png")


if __name__ == "__main__":
    generate_qr()