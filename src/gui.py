from tkinter import Frame, Label, Button, Entry, StringVar, OptionMenu
from image_converter import convert_image
from video_converter import convert_video


class ConverterApp(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.filepath_label = Label(self, text="Select File:")
        self.filepath_label.grid(row=0, column=0)

        self.filepath_entry = Entry(self)
        self.filepath_entry.grid(row=0, column=1)

        self.format_label = Label(self, text="Convert To:")
        self.format_label.grid(row=1, column=0)

        self.format_var = StringVar()
        self.format_var.set("png")
        self.format_menu = OptionMenu(
            self, self.format_var, "png", "jpeg", "mp4", "avi")
        self.format_menu.grid(row=1, column=1)

        self.convert_button = Button(
            self, text="Convert", command=self.convert)
        self.convert_button.grid(row=2, columnspan=2)

    def convert(self):
        filepath = self.filepath_entry.get()
        format_to = self.format_var.get()

        if filepath.lower().endswith(("png", "jpg", "jpeg", "gif")):
            convert_image(filepath, format_to)
        elif filepath.lower().endswith(("mp4", "avi", "mkv", "flv")):
            convert_video(filepath, format_to)
