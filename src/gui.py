import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
from image_converters import *
import os

# File path
file = None

# Create the main window
root = tk.Tk()
root.title("Media Converter")
root.geometry("1290x690")

# Initialize the Notebook widget
notebook = ttk.Notebook(root)

# Create individual tabs as Frame widgets
tab_image = ttk.Frame(notebook)
tab_video = ttk.Frame(notebook)
tab_audio = ttk.Frame(notebook)

# Add these frames to the notebook with respective labels
notebook.add(tab_image, text="Image")
notebook.add(tab_video, text="Video")
notebook.add(tab_audio, text="Audio")


# Function to handle file selection and image preview
# Modify the select_file function to display the image
def select_file():
    global file
    file_path = filedialog.askopenfilename()
    if file_path:
        # Get file info
        file_info = {
            "Filename": os.path.basename(file_path),
            "Size": os.path.getsize(file_path) / (1024 * 1024),  # Size in MB
        }

        # Open the image to get format and dimensions
        with Image.open(file_path) as img:
            file_info["Format"] = img.format
            file_info["Dimension"] = "{}x{}".format(*img.size)
            # Resize the image for display if necessary
            img.thumbnail(
                (image_frame.winfo_width(), image_frame.winfo_height()),
                Image.Resampling.LANCZOS,
            )
            photo = ImageTk.PhotoImage(img)
            # Update the image_display_label with the image
            image_display_label.config(image=photo)
            # Keep a reference to the image
            image_display_label.image = photo

        # Update the file_info_label with the file info
        file_info_text = (
            f"Filename: {file_info['Filename']}\n"
            f"Format: {file_info['Format']}\n"
            f"Dimension: {file_info['Dimension']}\n"
            f"Size: {file_info['Size']:.2f} MB"
        )
        file_info_label.config(text=file_info_text)
        image_file_label.config(text=file_info["Filename"])
        file = file_path


# Create frames for the left and right sides
left_frame = ttk.Frame(tab_image, width=645)  # Half of the window's width
right_frame = ttk.Frame(tab_image, width=645)  # The other half of the window's width

# Create image_frame to display the image
image_frame = ttk.Frame(left_frame)
image_frame.pack(side="top", fill="both", expand=True)
image_frame.pack_propagate(False)  # Prevent the frame from resizing to fit its contents

# Label for displaying the image
image_display_label = ttk.Label(image_frame)
image_display_label.pack(side="top", fill="both", expand=True)

# Prevent the frames from changing size according to their content
left_frame.pack_propagate(False)
right_frame.pack_propagate(False)

bottom_frame = ttk.Frame(left_frame)
bottom_frame.pack(side="bottom", fill="x", padx=10, pady=10)

# Move the select_button into the bottom_frame and pack to the left
select_button = ttk.Button(bottom_frame, text="Select File", command=select_file)
select_button.pack(side="left", padx=10, pady=10)

# Create the image_file_label and pack to the right of the select_button
image_file_label = ttk.Label(bottom_frame, text="No image selected")
image_file_label.pack(side="left", padx=10, pady=10)

# Position the frames within the tab
left_frame.pack(side="left", fill="y")
right_frame.pack(side="right", fill="both", expand=True)

# Move the sub-notebook into the right_frame
sub_notebook = ttk.Notebook(right_frame)

# Information tab
information_tab = ttk.Frame(sub_notebook)
sub_notebook.add(information_tab, text="Information")

# File info label area
file_info_label_area = ttk.LabelFrame(information_tab, text="File Information")
file_info_label_area.pack(fill="x", expand=True, padx=10, pady=10)

# Label for displaying the file info
file_info_label = ttk.Label(file_info_label_area, text="No file selected")
file_info_label.pack(side="top", fill="x", expand=True)

# Label area under Information tab
output_label_area = ttk.LabelFrame(information_tab, text="Output")
output_label_area.pack(anchor="s", fill="x", expand=True, padx=10, pady=10)


def convert_image_file():
    # Retrieve the filename from the image_file_label
    file_name = image_file_label.cget("text")
    if file_name == "No image selected":
        # No file selected, show an error or a message to the user
        print("No file selected.")
        return

    # Construct the input file path (assuming the file is in the current working directory)
    input_path = file

    # Get the desired output format from the radio buttons
    output_format = selected_format.get()

    # Define the output path (here, replacing the extension with the desired format)
    output_path = os.path.splitext(input_path)[0] + "." + output_format.lower()

    # Attempt to convert the image using the function from image_converters.py
    try:
        # Assuming convert_image function is imported from image_converters.py
        success = convert_image(input_path, output_path, output_format)
        if success:
            print(f"Image converted successfully to {output_path}")
            # Here you can add any post-conversion actions, like updating the GUI with the new file info
        else:
            print("Image conversion failed.")
    except Exception as e:
        print(f"Failed to convert image: {e}")


# Radio buttons for format selection
selected_format = tk.StringVar(value="PNG")  # Default value can be PNG
formats = ["PNG", "JPEG", "WEBP", "TIFF"]
for fmt in formats:
    radio_button = ttk.Radiobutton(
        output_label_area, text=fmt, value=fmt, variable=selected_format
    )
    radio_button.pack(side="top", anchor="w")

# Convert button
convert_button = ttk.Button(information_tab, text="Convert", command=convert_image_file)
convert_button.pack(side="left", padx=10, pady=10)

# Open Folder button
open_folder_button = ttk.Button(information_tab, text="Open Folder")
open_folder_button.pack(side="left", padx=10, pady=10)

# Metadata tab
metadata_tab = ttk.Frame(sub_notebook)
sub_notebook.add(metadata_tab, text="Metadata")

# Resize tab
resize_tab = ttk.Frame(sub_notebook)
sub_notebook.add(resize_tab, text="Resize")

# Pack the sub-notebook
sub_notebook.pack(side="right", fill="both", expand=True, padx=10, pady=10)

# Pack the notebook into the main window
notebook.pack(expand=True, fill="both")

# Start the Tkinter event loop
root.mainloop()
