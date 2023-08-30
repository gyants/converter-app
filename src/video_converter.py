import ffmpeg


def convert_video(filepath, format_to):
    try:
        output_path = filepath.rsplit('.', 1)[0] + f'.{format_to}'
        ffmpeg.input(filepath).output(output_path).run()
        print(f"Video saved to {output_path}")
    except Exception as e:
        print(f"Error: {e}")
