# QR Code Generator

A simple Python utility that generates QR codes from text or URLs and saves them as PNG images.

## Features

- Generate QR codes from text or URLs.
- Choose a custom filename for the generated QR code.
- Validate empty user input.
- Display a generation progress animation in the terminal.
- Save QR codes as PNG images.

## Technologies Used

- Python
- qrcode
- Pillow

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/bhanuu-u/python-utilities.git
   ```

2. Navigate to the project folder:

   ```bash
   cd python-utilities/qr-code-generator
   ```

3. Install the required library:

   ```bash
   pip install "qrcode[pil]"
   ```

## Usage

Run the Python script:

```bash
python main.py
```

Enter the text or URL you want to convert into a QR code. Then enter a filename or press Enter to use the default filename, `qrcode`.

The generated QR code will be saved as a PNG image.

## Author

**A. Revanth Bhanu**
