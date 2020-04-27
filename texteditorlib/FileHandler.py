if __name__ == '__main__':
    from Graphics import Tkinter as tk, tkFileDialog, tkMessageBox
    import tkinter
    from tkinter import *
    from tkinter import Tk, scrolledtext, Menu, Button, filedialog, END, messagebox, simpledialog, ttk
else:
    from .Graphics import Tkinter as tk, tkFileDialog, tkMessageBox
    import tkinter
    from tkinter import *
    from tkinter import Tk, scrolledtext, Menu, Button, filedialog, END, messagebox, simpledialog, ttk


class FileHandler:
    def __init__(self, text):
        self.text = text
        self.text.storeobj['OpenFile'] = None
        self.functions_key_bindings()
        self.binding_key_configuration()
        self.already_open_file()

    def already_open_file(self):

        path = None

        if path:
            data = open(path, "rb").read()
            self.text.delete('1.0', 'end')
            self.text.insert("1.0", data)
            self.text.storeobj['OpenFile'] = path
        return

    def binding_key_configuration(self):
        for key in ['<Control-N>', "<Control-n>"]:
            self.text.bind(key, self.new_file)
        for key in ['<Control-S>', "<Control-s>"]:
            self.text.bind(key, self.save_file)
        for key in ['<Control-Shift-S>', "<Control-Shift-s>"]:
            self.text.bind(key, self.save_as)
        for key in ['<Control-O>', "<Control-o>"]:
            self.text.bind(key, self.open_file)
        for key in ['<Control-q>', "<Control-Q>"]:
            self.text.bind(key, self.quit)
        return

    def functions_key_bindings(self):
        self.text.storeobj['Open'] = self.open_file
        self.text.storeobj['Save'] = self.save_file
        self.text.storeobj['SaveAs'] = self.save_as
        self.text.storeobj['OpenNew'] = self.new_file
        self.text.storeobj['Quit'] = self.quit
        self.text.storeobj['Credits'] = self.Credits
        self.text.storeobj['Find and Replace'] = self.findinFile
        self.text.storeobj['Reset'] = self.Reset
        return

    def open_file(self, event=None):
        path = tkFileDialog.askopenfilename()
        if path:
            data = open(path, "rb").read()
            self.text.delete('1.0', 'end')
            self.text.insert("1.0", data)
            self.text.storeobj['OpenFile'] = path
        return

    def save_file(self, event=None):

        if not self.text.storeobj['OpenFile']:
            path = tkFileDialog.asksaveasfilename()
        else:
            path = self.text.storeobj['OpenFile']
        if path:
            data = self.text.get("1.0", 'end')
            f_ = open(path, "w")
            f_.write(data)
            f_.close()
            self.text.storeobj['OpenFile'] = path

 #   path = tkFileDialog.asksaveasfilename(title='w', filetypes=(
  #      ("Text file", "*.txt"), ("All files", "*.*")))
  #  if path != None:
   #     data = self.text.get('1.0', END + '-1c')
            # path.write(data)
            # path.close()
   #     f_ = open(path, "w")
        #    f_.write(data)
     #   f_.close()
        # return

    #	if not self.text.storeobj['OpenFile']:
    #		path = tkFileDialog.asksaveasfilename()
    #	else:
    #		path = self.text.storeobj['OpenFile']
    #	if path:
    #		data = self.text.get("1.0",'end')
    #		f_=open(path,"wb")
    #		f_.write(data)
    #		f_.close()
    #		self.text.storeobj['OpenFile']=path

    def save_as(self, event=None):
        path = tkFileDialog.asksaveasfilename(title='w', filetypes=(
            ("Text file", "*.txt"), ("All files", "*.*")))
        if path:
            data = self.text.get("1.0", 'end')
            f_ = open(path, "w")
            f_.write(data)
            f_.close()
        return

    def new_file(self, event=None):

        if len(self.text.get('1.0', END+'-1c')) > 0:
            if messagebox.askyesno("Save", "Do You Want To Save It as New File?"):
                self.save_as()
                self.text.delete('1.0', END)
            else:
                self.text.delete('1.0', END)

        #import os
        #os.system("python main.py")
        # return

    def quit(self, event=None):
        if len(self.text.get('1.0', END+'-1c')) > 0:
            if messagebox.askyesno("Save", "Do You Want To Save It?"):
                self.save_as()
            ask = tkMessageBox.askyesno(
                title="Quit", message="Do You Really Want to Exit?")
            if ask == False:
                return
            elif ask == True:
                # pass
               # else:
               #     self.save_file()
               # if self.text.storeobj['OpenFile']:

               #     f = open("cachememory", 'w')
               #     f.write(self.text.storeobj['OpenFile'])
               #     f.close()
                import sys
                self.text.delete('1.0', END)
                sys.exit(0)
            # self.root.destroy()
                return
        else:
            ask = tkMessageBox.askyesno(
                title="Quit", message="Do You Really Want to Exit?")
        if ask == False:
            return
        elif ask == True:
            # pass
           # else:
           #     self.save_file()
           # if self.text.storeobj['OpenFile']:

           #     f = open("cachememory", 'w')
           #     f.write(self.text.storeobj['OpenFile'])
           #     f.close()
            import sys
            self.text.delete('1.0', END)
            sys.exit(0)
            # self.root.destroy()
            return

    def Credits(self, event=None):
        ask = tkMessageBox.showinfo(
            title="Credits", message="✵ Md Sajjad Ansari\r\n✵ Ali Hussain Khan")

    def Reset(self, event=None):
        self.text.delete('1.0', END)

    def findinFile(self, event=None):

        findstring = simpledialog.askstring(" Find ", "Enter text")
        textData = self.text.get('1.0', END)
        occ = textData.upper().count(findstring.upper())
        if occ == 0:
            label = messagebox.showerror(" RESULTS ", "Text Not Found")
        else:
            length = len(textData)
            pos = []
            strng = ''
            line_word = []
            line = 1
            word = 0
            for i in range(length):
                if textData[i] == '\n':
                    pos.append(i)
                    line_word.append(strng)
                    strng = ''
                    line = line + 1
                    word = 0
                else:
                    strng += textData[i]
                    word = word + 1
            print(pos)
            print(line_word)

            for j in range(len(line_word)):
                res = [i for i in range(len(line_word[j]))
                       if line_word[j].startswith(findstring, i)]
                print(res)
                for i in range(len(res)):
                    line_no = j+1
                    word_no = res[i]
           # textArea.delete(str(line_no)+'.'+str(word_no),str(line_no)+'.'+str(word_no+len(findstring)))
           # textArea.insert(str(line_no)+'.'+str(word_no), "REPLACE")
                    self.text.tag_add("here", str(line_no)+'.'+str(word_no),
                                      str(line_no)+'.'+str(word_no+len(findstring)))
                    self.text.tag_config(
                        "here", background="yellow", foreground="blue")
            replacestring = simpledialog.askstring(" Replace ", "Enter text")
            print('replace string is ', replacestring)

            for j in range(len(line_word)):
                res = [i for i in range(len(line_word[j]))
                       if line_word[j].startswith(findstring, i)]
                print(res)
                for i in range(len(res)):
                    line_no = j + 1
                    word_no = res[i]
                    if replacestring != None:
                        self.text.delete(str(line_no)+'.'+str(word_no),
                                         str(line_no)+'.'+str(word_no+len(findstring)))
                        self.text.insert(str(line_no)+'.' +
                                         str(word_no), replacestring)
                    self.text.tag_add("here", str(line_no) + '.' + str(word_no),
                                      str(line_no) + '.' + str(word_no + len(findstring)))
                    self.text.tag_config(
                        "here", background="white", foreground="black")


if __name__ == '__main__':
    root = Tkinter.Tk()
    pad = Tkinter.Text(root)
    pad.pack()
    pad.storeobj = {}
    FileHandler(pad)
    root.mainloop()
