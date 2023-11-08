from moviepy.editor import AudioFileClip

def convert_audio(input_path, output_path, output_format):
    """
    Converts an audio file to the specified format.
    
    :param input_path: str - The path to the input audio file.
    :param output_path: str - The path to save the converted audio file.
    :param output_format: str - The desired output format (e.g., 'mp3', 'm4a', 'ogg', 'wav').
    :return: bool - True if conversion was successful, False otherwise.
    """
    valid_formats = ['mp3', 'm4a', 'ogg', 'wav', '3gp', 'aa', 'aac', 'webm']
    if output_format.lower() not in valid_formats:
        print(f"Unsupported format: {output_format}. Supported formats are: {valid_formats}")
        return False

    try:
        audio = AudioFileClip(input_path)
        # Write the audio to the specified format and output path
        audio.write_audiofile(output_path, codec=output_format)
        return True
    except Exception as e:
        print(f"Failed to convert audio: {e}")
        return False