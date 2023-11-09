# Move the sub-notebook into the right_frame
sub_notebook = ttk.Notebook(right_frame)

# Information tab
information_tab = ttk.Frame(sub_notebook)
sub_notebook.add(information_tab, text="Information")

# Label area under Information tab
output_label_area = ttk.LabelFrame(information_tab, text="Output")
output_label_area.pack(fill="x", expand=True, padx=10, pady=10)

output_label = ttk.Label(output_label_area, text="Output")
output_label.pack()

# Radio buttons for format selection
format_var = tk.StringVar()
formats = ["PNG", "JPEG", "WEBP", "TIFF"]
for fmt in formats:
    radio_button = ttk.Radiobutton(
        output_label_area, text=fmt, value=fmt, variable=format_var
    )
    radio_button.pack(side="left")

# Convert button
convert_button = ttk.Button(information_tab, text="Convert")
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