from unittest import TestCase
import os
from PIL import Image
from src.image_converters import convert_image, resize_and_save_as_icon, convert_to_grayscale, resize_image, svg_to_image

class TestImageConverters(TestCase):
    def test_convert_image_to_jpeg(self):
        input_path = "data/sample.png"
        output_path = "data/result.jpg"
        # Ensure the output file doesn't already exist
        if os.path.exists(output_path):
            os.remove(output_path)
            
        # Test the conversion function
        result = convert_image(input_path, output_path, 'JPEG')
        self.assertTrue(result)
        # Check that the output file was created
        self.assertTrue(os.path.exists(output_path))
        
        # Cleanup: Remove created file after test
        if os.path.exists(output_path):
            os.remove(output_path)
    
    def test_convert_image_to_png(self):
        input_path = "data/sample.jpg"
        output_path = "data/result.png"
        # Ensure the output file doesn't already exist
        if os.path.exists(output_path):
            os.remove(output_path)
            
        # Test the conversion function
        result = convert_image(input_path, output_path, 'PNG')
        self.assertTrue(result)
        # Check that the output file was created
        self.assertTrue(os.path.exists(output_path))
        
        # Cleanup: Remove created file after test
        if os.path.exists(output_path):
            os.remove(output_path)

    def test_resize_and_save_as_icon(self):
        input_file = "data/sample.jpg"
        output_file = "data/result.ico"
        size = 32

        # Call the function to resize and save as an icon
        result = resize_and_save_as_icon(input_file, output_file, size)

        # Check if the function returned True (indicating success)
        self.assertTrue(result)

        # Check if the output file exists
        self.assertTrue(os.path.exists(output_file))

        # Clean up: remove the test files
        os.remove(output_file)

    def test_convert_to_grayscale(self):
        input_file = "data/sample.jpg"
        output_file = "data/result.jpg"

        # Call the function to convert to grayscale and save
        result = convert_to_grayscale(input_file, output_file)

        # Check if the function returned True (indicating success)
        self.assertTrue(result)

        # Check if the output file exists
        self.assertTrue(os.path.exists(output_file))

        # Clean up: remove the test files
        os.remove(output_file)

    def test_resize_image(self):
        input_file = "data/sample.jpg"
        output_file = "data/test_output.jpg"
        width = 512
        height = 512

        # Call the function to resize the sample image
        result = resize_image(input_file, output_file, width, height)

        # Check if the function returned True (indicating success)
        self.assertTrue(result)

        # Check if the output file exists
        self.assertTrue(os.path.exists(output_file))

        # Check if the resized image has the correct dimensions
        with Image.open(output_file) as resized_image:
            self.assertEqual(resized_image.size, (width, height))

        # Clean up: remove the test output file
        os.remove(output_file)

    def test_svg_to_png(self):
        input_file = "data/sample.svg"
        png_output_file = "data/result.png"

        # Call the function to convert SVG to PNG
        svg_to_image(input_file, png_output_file, "PNG")

        # Check if the PNG output file exists
        self.assertTrue(os.path.exists(png_output_file))

        # Clean up: remove the PNG output file
        os.remove(png_output_file)

    def test_svg_to_jpg(self):
        input_file = "data/sample.svg"
        jpg_output_file = "data/result.jpg"

        # Call the function to convert SVG to JPG
        svg_to_image(input_file, jpg_output_file, "JPG")

        # Check if the JPG output file exists
        self.assertTrue(os.path.exists(jpg_output_file))

        # Clean up: remove the JPG output file
        os.remove(jpg_output_file)
    
    def test_convert_tiff_to_png(self):
        input_path = "data/sample.jpg"
        output_path = "data/result.tiff"
        # Ensure the output file doesn't already exist
        if os.path.exists(output_path):
            os.remove(output_path)
            
        # Test the conversion function
        result = convert_image(input_path, output_path, 'TIFF')
        self.assertTrue(result)
        # Check that the output file was created
        self.assertTrue(os.path.exists(output_path))
        
        # Cleanup: Remove created file after test
        if os.path.exists(output_path):
            os.remove(output_path)

if __name__ == 'main':
    unittest = TestImageConverters()
    unittest.run()