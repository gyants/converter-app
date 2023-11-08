from PIL import Image
import cairosvg
import os
# import pyheif

def convert_image(input_path, output_path, output_format):
    """
    Converts an image to the specified format.
    
    :param input_path: str - The path to the input image.
    :param output_path: str - The path to save the converted image.
    :param output_format: str - The desired output format ('JPEG', 'PNG', or 'WEBP').
    :return: bool - True if conversion was successful, False otherwise.
    """
    valid_formats = ['JPEG', 'PNG', 'WEBP', 'TIFF']
    if output_format not in valid_formats:
        print(f"Unsupported format: {output_format}. Supported formats are: {valid_formats}")
        return False

    try:
        with Image.open(input_path) as image:
            # Convert the image to RGB if converting to JPEG
            if output_format == 'JPEG':
                if image.mode != 'RGB':
                    image = image.convert('RGB')

            # Save the image in the specified format
            image.save(output_path, output_format)
        return True
    except Exception as e:
        print(f"Failed to convert image: {e}")
        return False

def resize_and_save_as_icon(input_file, output_file, size):
    """
    Resize the input image to the specified size and save it as an icon.

    :param input_file: str - The path to the input image file.
    :param output_file: str - The path to save the resized image as an icon.
    :param size: int - The desired size for the icon (e.g., 16, 32, 48, etc.).
    :return: bool - True if resizing and saving were successful, False otherwise.
    """
    try:
        with Image.open(input_file) as image:
            # Resize the image to the specified size while maintaining the aspect ratio
            image.thumbnail((size, size))
            # Save the resized image as an icon
            image.save(output_file, "ICO")  # Use "ICO" format for Windows icon files
        return True
    except Exception as e:
        print(f"Failed to resize and save as icon: {e}")
        return False
    
def convert_to_grayscale(input_file, output_file):
    """
    Convert the input image to grayscale and save it as an output image.

    :param input_file: str - The path to the input image file.
    :param output_file: str - The path to save the grayscale image.
    :return: bool - True if conversion and saving were successful, False otherwise.
    """
    try:
        with Image.open(input_file) as image:
            # Convert the image to grayscale
            grayscale_image = image.convert("L")

            # Save the grayscale image
            grayscale_image.save(output_file)

        return True
    except Exception as e:
        print(f"Failed to convert to grayscale: {e}")
        return False
    
def resize_image(input_path, output_path, width, height):
    """
    Resize an image to the specified width and height and save it as a new image.

    :param input_path: str - The path to the input image file.
    :param output_path: str - The path to save the resized image.
    :param width: int - The desired width of the resized image.
    :param height: int - The desired height of the resized image.
    :return: bool - True if resizing and saving were successful, False otherwise.
    """
    try:
        with Image.open(input_path) as image:
            # Resize the image to the specified dimensions using LANCZOS filter
            resized_image = image.resize((width, height), Image.LANCZOS)
            # Save the resized image
            resized_image.save(output_path)
        return True
    except Exception as e:
        print(f"Failed to resize image: {e}")
        return False

def svg_to_image(input_path, output_path, output_format):
    """
    Convert an SVG file to an image (PNG or JPG).

    :param input_path: str - The path to the input SVG file.
    :param output_path: str - The path to save the PNG or JPG image.
    :param output_format: str - The desired output format ('PNG' or 'JPG').
    """
    if output_format not in ['PNG', 'JPG']:
        print(f"Unsupported format: {output_format}. Supported formats are: PNG, JPG")
        return

    try:
        if output_format.upper() == 'PNG':
            cairosvg.svg2png(url=input_path, write_to=output_path)
        elif output_format.upper() == 'JPG':
            # Convert to PNG first, then convert PNG to JPG
            # This is because cairosvg does not support direct svg to jpg conversion
            temp_png_path = output_path.rsplit('.', 1)[0] + ".png"
            cairosvg.svg2png(url=input_path, write_to=temp_png_path)
            
            # Now convert the PNG to JPG using Pillow
            from PIL import Image
            with Image.open(temp_png_path) as img:
                img.convert('RGB').save(output_path, 'JPEG')

            # Clean up the temporary PNG file
            import os
            os.remove(temp_png_path)
    except Exception as e:
        print(f"Failed to convert SVG to {output_format}: {e}")