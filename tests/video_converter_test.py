import unittest 
from unittest.mock import patch, Mock
import os
from moviepy.editor import VideoFileClip
from src.video_converters import convert_video

def create_test_function(input_format, output_format):
    @patch('src.video_converters.VideoFileClip')
    def test(self, mock_video_clip):
        mock_video = mock_video_clip.return_value.__enter__.return_value
        mock_video.write_videofile.return_value = True
        self.assertTrue(convert_video(f'input.{input_format}', f'output.{output_format}', output_format))
    return test

class TestFormatConversions(unittest.TestCase):
    pass

class TestVideoConversionFailures(unittest.TestCase):
    @patch('src.video_converters.VideoFileClip')
    def test_unsupported_video_format(self, mock_video_clip):
        mock_video_clip.side_effect = ValueError("Unsupported format")
        input_video_path = "input_video.mkv"
        output_video_path = "output_video.unknown"  # Unsupported format
        output_video_format = 'unknown'
        result = convert_video(input_video_path, output_video_path, output_video_format)
        self.assertFalse(result)

valid_formats = ['mp4', 'avi', 'mkv', 'mov', 'webm', 'flv', 'm4v']
# Dynamically adding test methods to TestFormatConversions
for input_format in valid_formats:
    for output_format in valid_formats:
        if input_format != output_format:
            test_name = f'test_convert_{input_format}_to_{output_format}'
            test = create_test_function(input_format, output_format)
            setattr(TestFormatConversions, test_name, test)

if __name__ == '__main__':
    unittest.main()