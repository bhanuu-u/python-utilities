
from pathlib import Path
from PIL import Image, UnidentifiedImageError
from pypdf import PdfWriter


def format_size(size):
    if size < 1024 * 1024:
        return f"{size / 1024:.2f} KB"
    return f"{size / (1024 * 1024):.2f} MB"


def show_results(original, output):
    old_size = original.stat().st_size
    new_size = output.stat().st_size
    saved = old_size - new_size

    print("\nCompression completed!")
    print(f"Original size   : {format_size(old_size)}")
    print(f"Compressed size : {format_size(new_size)}")

    if saved > 0:
        percentage = saved / old_size * 100 if old_size else 0
        print(f"Space saved     : {format_size(saved)}")
        print(f"Size reduction  : {percentage:.2f}%")
    elif saved < 0:
        print(f"Size increased  : {format_size(-saved)}")
    else:
        print("File size unchanged.")

    print(f"Output file     : {output}")


def compress_image(file_path):
    quality_input = input("Quality (1-95, default 75): ").strip()

    try:
        quality = int(quality_input) if quality_input else 75
        if not 1 <= quality <= 95:
            print("Quality must be between 1 and 95.")
            return
    except ValueError:
        print("Enter a valid quality number.")
        return

    resize_input = input(
        "Maximum dimension in pixels (Enter to skip): "
    ).strip()

    try:
        max_dimension = int(resize_input) if resize_input else None
        if max_dimension is not None and max_dimension <= 0:
            print("Dimension must be positive.")
            return
    except ValueError:
        print("Enter a valid dimension.")
        return

    output = file_path.with_name(
        f"{file_path.stem}_compressed{file_path.suffix}"
    )

    if output.exists():
        print("Output file already exists. Rename or move it first.")
        return

    try:
        with Image.open(file_path) as image:
            image.load()
            image_format = image.format

            if image_format not in ("JPEG", "PNG", "WEBP"):
                print("Supported images: JPG, JPEG, PNG and WebP.")
                return

            if max_dimension:
                image.thumbnail((max_dimension, max_dimension))

            if image_format == "JPEG":
                if image.mode not in ("RGB", "L"):
                    image = image.convert("RGB")

                image.save(
                    output,
                    "JPEG",
                    quality=quality,
                    optimize=True,
                    progressive=True
                )

            elif image_format == "PNG":
                image.save(output, "PNG", optimize=True)

            elif image_format == "WEBP":
                image.save(
                    output,
                    "WEBP",
                    quality=quality,
                    method=6
                )

        show_results(file_path, output)

    except (OSError, ValueError, UnidentifiedImageError) as error:
        try:
            if output.exists():
                output.unlink()
        except OSError:
            pass

        print(f"Image compression failed: {error}")


def compress_pdf(file_path):
    output = file_path.with_name(
        f"{file_path.stem}_compressed.pdf"
    )

    if output.exists():
        print("Output file already exists. Rename or move it first.")
        return

    try:
        writer = PdfWriter(clone_from=str(file_path))

        for page in writer.pages:
            page.compress_content_streams()

        writer.compress_identical_objects(
            remove_identicals=True,
            remove_orphans=True
        )

        with output.open("wb") as pdf_file:
            writer.write(pdf_file)

        show_results(file_path, output)

    except Exception as error:
        try:
            if output.exists():
                output.unlink()
        except OSError:
            pass

        print(f"PDF compression failed: {error}")


def main():
    print("=" * 40)
    print("       File Size Compressor")
    print("=" * 40)
    print("1. Compress an image")
    print("2. Compress a PDF")

    choice = input("\nChoose an option: ").strip()
    file_path = input("Enter file path: ").strip().strip('"')

    path = Path(file_path)

    if not path.is_file():
        print("File not found.")
        return

    if choice == "1":
        if path.suffix.lower() not in (".jpg", ".jpeg", ".png", ".webp"):
            print("Please select a supported image file.")
            return

        compress_image(path)

    elif choice == "2":
        if path.suffix.lower() != ".pdf":
            print("Please select a PDF file.")
            return

        compress_pdf(path)

    else:
        print("Invalid option.")


if __name__ == "__main__":
    main()
