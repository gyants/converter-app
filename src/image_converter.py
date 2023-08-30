import imageio


def convert_image(filepath, format_to):
    try:
        image = imageio.imread(filepath)
        output_path = filepath.rsplit('.', 1)[0] + f'.{format_to}'
        imageio.imsave(output_path, image)
        print(f"Image saved to {output_path}")
    except Exception as e:
        print(f"Error: {e}")
