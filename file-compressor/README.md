# File Size Compressor

A Python utility that compresses images and optimizes PDF documents to reduce file size where possible. The application provides image quality controls, optional resizing, and compression statistics while preserving the original files.

## Features

- **Image Compression:** Supports JPG, JPEG, PNG, and WebP formats.
- **Quality Control:** Adjust compression quality for JPEG and WebP images.
- **Image Resizing:** Set a maximum image dimension while maintaining the aspect ratio.
- **PDF Optimization:** Compress PDF content streams and remove duplicate or unreferenced objects where possible.
- **Size Comparison:** Display original size, compressed size, space saved, and percentage reduction.
- **Safe Output:** Save compressed files separately without overwriting existing output files.
- **Input Validation:** Handle invalid file paths, unsupported formats, and invalid input values.

## Technologies Used

- Python
- Pillow
- pypdf
- pathlib

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/bhanuu-u/python-utilities.git
   ```

2. Navigate to the project directory:

   ```bash
   cd python-utilities/file-compressor
   ```

3. Install the required libraries:

   ```bash
   pip install Pillow pypdf
   ```

## Usage

Run the application:

```bash
python file_compressor.py
```

Select one of the available options:

1. Compress an image
2. Compress a PDF

Enter the path of the file you want to process.

For images, specify a quality value between 1 and 95 and optionally enter a maximum dimension in pixels. The program saves the processed file in the same directory as the original.

## Compression Results

After processing, the application displays:

- Original file size
- Compressed file size
- Space saved or size increase
- Percentage size reduction
- Output file path

Compression results depend on the file format, original encoding, and selected settings. PDF optimization may provide limited savings when most of the file size comes from embedded images.

## Project Structure

```text
file-compressor/
├── file_compressor.py
└── README.md
```

## Implementation

- Developed a menu-driven file compression utility.
- Implemented image optimization using Pillow.
- Added optional image resizing and quality controls.
- Implemented PDF content stream compression and object optimization using pypdf.
- Added file size calculations and compression statistics.
- Implemented input validation and error handling.
- Preserved original files by generating separate output files.

## Author

**A. Revanth Bhanu**
