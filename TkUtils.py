from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL import ImageTk

#You will never have to manually call this, It's used as part of one of the static methods
class ObservableButton(Button):
    def __init__(self, root, text, callback, main_color, hover_color):
        Button.__init__(self, root, text=text, command=callback, background=main_color, padx=0, relief=FLAT,
                   font="Arial 11 bold", foreground="white")
        self.bind("<Enter>", self.on_hover)
        self.bind("<Leave>", self.on_exit)
        self.main_color = main_color
        self.hover_color = hover_color

    def on_hover(self, event):
        self["background"] = self.hover_color

    def on_exit(self, event):
        self["background"] = self.main_color

#You will never have to manually call this, It's used as part of one of the static methods
class ToolTip:
    """
    Attribution:
        Adapted from: https://stackoverflow.com/a/65524559
    Changes made:
        Minor syntax changes and geometry offset changed from 15 to none
    """
    def __init__(self,root,text=None):

        self.tooltip = None
        self.root=root
        self.text=text

        def on_enter(event):
            self.tooltip=Toplevel(root)
            self.tooltip.overrideredirect(True)
            self.tooltip.geometry(f'+{event.x_root}+{event.y_root}')
            Label(self.tooltip,text=self.text).pack()

        def on_leave(event):
            self.tooltip.destroy()

        self.root.bind('<Enter>', on_enter)
        self.root.bind('<Leave>', on_leave)

class TkUtils:
    red = "#ff8f8f"
    image_width = 540
    image_height = 300

    @staticmethod
    def root():
        """
        Generates the root login window for the application.

        Returns:
            The root tk.Tk() object, prestyled and preconfigured.
        """
        window = Tk()
        window.resizable(False, False)
        window.title("Login")
        window.configure(background="#d9d9d9")
        return window

    #Some operating systems struggle to automatically stretch the window
    #If needed, pass in a manual height and uncomment line 83
    @staticmethod
    def top_level(title_, height=0):
        """
        Generates a top level window for the application.

        Parameters:
            title_ (str): The title of the window.
            height (int, optional): The height of the window.

        Returns:
            The root tk.Tk() object, prestyled and preconfigured.
        """
        tl = Toplevel()
        tl.resizable(False, False)
        tl.title(title_)
        tl.configure(background="#d9d9d9")
        # tl.geometry(f"{TkUtils.width}x{height}")
        return tl

    @staticmethod
    def same_window(title, root):
        """
        A simple way to replace the content of a window without a top level window.

        Parameters:
            title (str): The title of the window.
            root (tk.Tk): The existing window.

        Returns:
            The existing window with all packed elements removed.
        """
        for pack in root.pack_slaves():
            pack.destroy()
        root.title(title)
        return root

    @staticmethod
    def button(root, text_, callback=None):
        """
        Generates a prestyled button according to the assignment specifications.

        Parameters:
            root (tk.Tk): The window or frame containing the button.
            text_ (str): The text of the button.
            callback (function): The callback function.

        Returns:
            A tk.Button() object, prestyled and preconfigured.
        """
        return ObservableButton(root, text_, callback, TkUtils.red, "#ff8080")

    @staticmethod
    def separator(root):
        """
        Generates a prestyled separator according to the assignment specifications.

        Parameters:
            root (tk.Tk): The window or frame containing the separator.

        Returns:
            A ttk.Separator() object, prestyled and preconfigured.
        """
        return ttk.Separator(root, orient='horizontal')

    @staticmethod
    def label(root, text_):
        """
        Generates a prestyled label according to the assignment specifications.

        Parameters:
            root (tk.Tk): The window or frame containing the label.
            text_ (str): The text of the label.

        Returns:
            A tk.Label() object, prestyled and preconfigured.
        """
        return Label(root, text=text_, font="Helvetica 12 bold", foreground=TkUtils.red)

    @staticmethod
    def error_label(root, text_):
        """
        Generates a prestyled error label according to the assignment specifications.

        Parameters:
            root (tk.Tk): The window or frame containing the label.
            text_ (str): The text of the label.

        Returns:
            A tk.Label() object, prestyled and preconfigured.
        """
        return Label(root, text=text_, font="Courier 14", foreground="RED")

    @staticmethod
    def image(root, path, height=None, width=None, background=None):
        """
        Generates an image.

        Parameters:
            root (tk.Tk): The window or frame containing the image.
            path (str): The path to the image.
            height (int, optional): The height of the image. Defaults to the height of the banner image
            width (int, optional): The width of the image. Defaults to the width of the banner image
            background (str, optional): The background of the image. Defaults to no background

        Returns:
            A tk.Label() object with an image attribute, prestyled and preconfigured.
        """
        if height is None:
            height = TkUtils.image_height
        if width is None:
            width = TkUtils.image_width
        image_ = ImageTk.PhotoImage(Image.open(path).resize((width, height)))
        lbl = Label(root, image=image_)
        lbl.photo = image_
        if background:
            lbl.configure(background=background)
        return lbl

    #You will never have to manually call this, It's used as part of one of the static methods
    @staticmethod
    def _select(event, tree):
        item_id = tree.identify_row(event.y)
        if item_id is None:
            return
        if item_id in tree.selection():
            tree.selection_remove(item_id)
            return 'break'

    @staticmethod
    def treeview(root, columns, multi=False, width=500):
        """
        Generates a prestyled treeview according to the assignment specifications.

        Parameters:
            root (tk.Tk): The window or frame containing the treeview.
            columns (list): A list of column names.
            multi (bool, optional): Whether the tree view is multi-column or not. Defaults to browse (single) mode
            width (int, optional): The width of the treeview. Defaults to 500

        Returns:
            A ttk.Treeview() object, prestyled and preconfigured with deselecting
        """
        tree = ttk.Treeview(root, show="headings", height=12, columns=columns, selectmode="extended" if multi else "browse")
        for column in tree["columns"]:
            tree.column(column, anchor=CENTER, width=int(width/len(columns)), stretch=NO)
        for i in range(len(columns)):
            tree.heading(i, text=columns[i])
        tree.bind("<<TreeViewSelect>>", 'break')
        tree.bind("<Button-1>", lambda event: TkUtils._select(event, tree))
        return tree

    @staticmethod
    def attach_tooltip(element, text):
        """
        Attaches a tooltip for a given element

        Parameters:
            element (tk.Tk): The element to generate a tooltip for.
            text (str): The text to display.
        """
        ToolTip(element, text)