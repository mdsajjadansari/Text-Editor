if __name__ == '__main__':
    from Graphics import Tkinter as tk, tkFileDialog, tkMessageBox
    import tkinter
    import Tkinter as tk
    from tkinter import *
    from tkinter import Tk, scrolledtext, Menu, Button, filedialog, END, messagebox, simpledialog, ttk

else:
    from .Graphics import Tkinter as tk, tkFileDialog, tkMessageBox
    import tkinter
    from tkinter import *
    from tkinter import Tk, scrolledtext, Menu, Button, filedialog, END, messagebox, simpledialog, ttk


def FindAsk(self, parent, *args):
    root = self.tk.toplevel(parent)
    root.title("Find")
    root.transient(parent)
    root.focus_force()
    root.resizable(width=0, height=0)
    root['padx'] = 20
    fields = {}
    field = {}
    for r, label in enumerate(self, args):
        store_label = self.tkinter.Label(root, text=label)
        store_label.grid(row=r, column=0, ipady=5, ipadx=20)
        store_entry = tkinter.Entry(root)
        store_entry.grid(row=r, column=1)
        field[label] = store_entry
    fields['submit'] = False

    def sub():
        for l, t in self.field.iteritems():
            fields[l] = t.get()
        fields['submit'] = True
        root.destroy()
        return
    submit = tkinter.Button(root, text="Ok", command=sub)
    submit.grid(row=r+1, column=2)
    root.wait_window()
    return fields


class FindReplaceFunctions:
    def __init__(self, text):
        self.text = text
        self.key_binding_functions()
        self.binding_functions_configuration()

    def binding_functions_configuration(self):
        self.text.storeobj['Find'] = self.find_
        self.text.storeobj['FindAll'] = self.find_all
        self.text.storeobj['Replace'] = self.replace
        self.text.storeobj['ReplaceAll'] = self.replace_all
        self.text.storeobj['ResetTags'] = self.reset_tags
        return

    def key_binding_functions(self):
        for key in ['<Control-F>', "<Control-f>"]:
            self.text.bind(key, self.find_)
        for key in ['<Control-Shift-F>', "<Control-Shift-f>"]:
            self.text.bind(key, self.find_all)
        for key in ['<Control-Shift-H>', "<Control-Shift-h>"]:
            self.text.bind(key, self.replace_all)
        for key in ['<Control-H>', "<Control-h>"]:
            self.text.bind(key, self.replace)
        for key in ['<Any-Button>']:
            self.text.bind(key, self.reset_tags)
        return

    def _search_(self, word):
        if word:
            countvar = self.tkinter.StringVar()
            f = self.text.search(word, "1.0", count=countvar)
            starting_index = f
            ending_index = "{}+{}c".format(starting_index, countvar.get())
            self.text.tag_add("search", starting_index, ending_index)
            self.text.tag_configure(
                "search", background="skyblue", foreground="red")
            return True
        else:
            return None

    def reset_tags(self, event=None):
        self.text.tag_delete("search")
        return

    def _search_all_(self, word):
        index = "1.0"
        if word:
            while True:
                f = self.text.search(word, index, stopindex=Tkinter.END)
                if not f:
                    break
                starting_index = int(f.split(".")[0])
                ending_index = len(word)+int(f.split(".")[1])
                coordinates = "{}.{}".format(starting_index, ending_index)
                self.text.tag_add("search", f, coordinates)
                self.text.tag_configure(
                    "search", background="skyblue", foreground="red")
                index = coordinates
            return True
        else:
            return None

    def _replace_(self, word):
        if word:
            coordinates = []
            l = list(self.text.tag_ranges("search"))
            l.reverse()
            while l:
                coordinates.append([l.pop(), l.pop()])
            for start, end in coordinates:
                self.text.delete(start, end)
                self.text.insert(start, word)
        return

    def _replace_all_(self, word):
        if word:
            coordinates = []
            l = list(self.text.tag_ranges("search"))
            l.reverse()
            while l:
                coordinates.append([l.pop(), l.pop()])
            for start, end in coordinates:
                self.text.delete(start, end)
                self.text.insert(start, word)

        return

    def find_(self, event=None):
        t = FindAsk(self.text.master, "Find")
        if t['submit']:
            self._search_(t['Find'])
        return

    def find_all(self, event=None):
        t = FindAsk(self.text.master, "FindAll")
        if t['submit']:
            self._search_all_(t['FindAll'])
        return

    def replace(self, event=None):
        t = FindAsk(self.text.master, "Find", "Replace")
        if t['submit']:
            self._search_(t['Find'])
            self._replace_all_(t['Replace'])
        return

    def replace_all(self, event=None):
        t = FindAsk(self.text.master, "FindAll", "ReplaceAll")
        if t['submit']:
            self._search_all_(t['FindAll'])
            self._replace_all_(t['ReplaceAll'])
        return


if __name__ == '__main__':
    root = Tkinter.Tk()
    pad = Tkinter.Text(root)
    pad.pack()
    pad.storeobj = {}
    FindReplaceFunctions(pad)
    # print FindAsk(root,"a","b",1)
    root.mainloop()
