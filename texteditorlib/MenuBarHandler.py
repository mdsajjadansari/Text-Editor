
from tkinter.font import Font
if __name__ == '__main__':
    from Graphics import Tkinter
else:
    from .Graphics import Tkinter

"""
SelectAll
DeselectAll
OpenFile
Credits
Cut
Redo
SaveAs
Save
Root
Undo
FindAll
FontChooser
ReplaceAll
OpenNew
ConfigApply
SaveConfig
Open
ResetTags
Copy
Paste
Find
Replace

"""


class MenuBar:
    def __init__(self, text):
        self.text = text
        self.create_menubar()

    def create_menubar(self):
        self.bar = Tkinter.Menu(self.text.storeobj['Root'])

        # Creating Sub menu
        sub_menu = Tkinter.Menu(self.bar, tearoff=0)

        self.bar.add_cascade(label='File', menu=sub_menu)
        sub_menu.add_command(
            label="New", command=self.text.storeobj['OpenNew'])
        sub_menu.add_command(label="Open",  command=self.text.storeobj['Open'])
        sub_menu.add_separator()
        sub_menu.add_command(label="Save",  command=self.text.storeobj['Save'])
        sub_menu.add_command(
            label="Save As", command=self.text.storeobj['SaveAs'])
        sub_menu.add_separator()
        sub_menu.add_command(label="Quit", command=self.text.storeobj['Quit'])

        # Creating Sub menu
        sub_menu = Tkinter.Menu(self.bar, tearoff=0)
        self.bar.add_cascade(label='Edit', menu=sub_menu)

        sub_menu.add_command(label="Redo", command=self.text.storeobj['Redo'])
        sub_menu.add_command(label="Undo",  command=self.text.storeobj['Undo'])
        sub_menu.add_separator()
        sub_menu.add_command(label="Copy",  command=self.text.storeobj['Copy'])
        sub_menu.add_command(label="Cut",  command=self.text.storeobj['Cut'])
        sub_menu.add_command(
            label="Paste",  command=self.text.storeobj['Paste'])
        sub_menu.add_separator()
        sub_menu.add_command(label="Select All",
                             command=self.text.storeobj['SelectAll'])
        sub_menu.add_command(label="Deselect All",
                             command=self.text.storeobj['DeselectAll'])

        # Creating Sub menu
        sub_menu = Tkinter.Menu(self.bar, tearoff=0)
        self.bar.add_cascade(label='View', menu=sub_menu)

        sub_menu.add_command(label="Find and Replace",
                             command=self.text.storeobj['Find and Replace'])
        sub_menu.add_command(
            label="Reset",  command=self.text.storeobj['Reset'])
        # sub_menu.add_command(label="Find All", command=self.text.storeobj['FindAll'])
        # sub_menu.add_separator()
        # sub_menu.add_command(label="Replace",  command=self.text.storeobj['Replace'])
        # sub_menu.add_command(label="Replace All", command=self.text.storeobj['ReplaceAll'])

        # Creating Sub menu
        sub_menu = Tkinter.Menu(self.bar, tearoff=0)
        self.bar.add_cascade(label='Prefrence', menu=sub_menu)

        sub_menu.add_command(label="Font and Size",
                             command=self.text.storeobj['FontChooser'])
        # sub_menu.add_separator()
        # sub_menu.add_command(label="Settings",  command=self.text.storeobj['OpenNew'])

        # Creating Sub menu
        # sub_menu=Tkinter.Menu(self.bar, tearoff=0)
        # self.bar.add_cascade(label='Help', menu=sub_menu)

        # sub_menu.add_command(label="Plugins",  command=self.text.storeobj['OpenNew'])
        # sub_menu.add_command(label="Author", command=self.text.storeobj['OpenNew'])

        # Creating Sub menu
        sub_menu = Tkinter.Menu(self.bar, tearoff=0)
        self.bar.add_cascade(label='About', menu=sub_menu)
        sub_menu.add_command(
            label="Credit", command=self.text.storeobj['Credits'])

        self.text.storeobj['Root'].configure(menu=self.bar)

        return


if __name__ == '__main__':
    root = Tkinter.Tk()
    pad = Tkinter.Text(root)
    pad.pack()
    pad.storeobj = {"Root": root}
    MenuBar(pad)
    root.mainloop()
