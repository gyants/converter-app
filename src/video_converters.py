from moviepy.editor import VideoFileClip

def convert_video(input_path, output_path, output_format):
    """
    Converts a video to the specified format.
    
    :param input_path: str - The path to the input video.
    :param output_path: str - The path to save the converted video.
    :param output_format: str - The desired output format (e.g., 'mp4', 'avi', 'mkv').
    :return: bool - True if conversion was successful, False otherwise.
    """
    valid_formats = ['mp4', 'avi', 'mkv', 'mov', 'webm', 'flv', 'm4v']
    if output_format.lower() not in valid_formats:
        print(f"Unsupported format: {output_format}. Supported formats are: {valid_formats}")
        return False

    try:
        video = VideoFileClip(input_path)
        # Write the video to the specified format and output path
        video.write_videofile(output_path, codec="libx264", audio_codec="aac", preset="medium")
        return True
    except Exception as e:
        print(f"Failed to convert video: {e}")
        return False