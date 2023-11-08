import unittest
from unittest.mock import patch
from src.audio_converters import convert_audio  # replace 'src.audio_converters' with the actual name of your module

valid_formats = ['mp3', 'm4a', 'ogg', 'wav', '3gp', 'aa', 'aac', 'webm']

def create_test_function(input_format, output_format):
    @patch('src.audio_converters.AudioFileClip')
    def test(self, mock_audio_clip):
        mock_audio = mock_audio_clip.return_value.__enter__.return_value
        mock_audio.write_audiofile.return_value = True
        self.assertTrue(convert_audio(f'input.{input_format}', f'output.{output_format}', output_format))
    return test

class TestAudioFormatConversions(unittest.TestCase):
    pass

class TestAudioConversionFailures(unittest.TestCase):
    @patch('src.audio_converters.AudioFileClip')
    def test_unsupported_audio_format(self, mock_audio_clip):
        mock_audio_clip.side_effect = ValueError("Unsupported format")
        input_audio_path = "input_audio.mp3"
        output_audio_path = "output_audio.unknown"  # Unsupported format
        output_audio_format = 'unknown'
        result = convert_audio(input_audio_path, output_audio_path, output_audio_format)
        self.assertFalse(result)

# Dynamically adding test methods to TestAudioFormatConversions
for input_format in valid_formats:
    for output_format in valid_formats:
        if input_format != output_format:
            test_name = f'test_convert_{input_format}_to_{output_format}'
            test = create_test_function(input_format, output_format)
            setattr(TestAudioFormatConversions, test_name, test)

if __name__ == '__main__':
    unittest.main()
