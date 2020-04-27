

if __name__=='__main__':
	from Graphics import Tkinter
else:
	from .Graphics import Tkinter
import re
import keyword


codes = " and   as   assert   break   class   continue   def   del   elif   else   except   exec   finally   for   from   global   if   import   in   is   lambda   not   or   pass   print   raise   return   try   while   with   yield "


class AutoComplete:
	def __init__(self, pad):
		self.text = pad
		self.s = None
		self.text.bind("<KeyRelease>", self.check)

	def check(self, event=None):
		print event.x, event.y
		word = self.text.get("insert linestart","insert wordend").split(" ")[-1]
		x,y = self.text.winfo_pointerxy()
		print x,y
		#self.ShowSuggestion(x,y,Data, self.GetSuggestion(Data))
		#print Data
		return

	
	def GetSuggestion(self, hint):
		engine = re.compile('\S'+hint+"\S+")
		return engine.findall(self.text.get("1.0","end")+codes)

	def ShowSuggestion(self,x, y, hint ,suggestions):
		if self.s:
			print "DEstroy"
			self.s.destroy()
		if suggestions:
			Top=Tkinter.Toplevel(self.text.master)
			l=Tkinter.Listbox(Top, bg="black", fg='white')
			l.pack(expand=True, fill='both')
			Top.geometry("+%d+%d" % (x, y))
			for i in suggestions:
				l.insert('end',i)
			Top.overrideredirect(True)
			self.s = Top
			#self.s.focus()
		return



if __name__ == '__main__':
	root = Tkinter.Tk()
	t= Tkinter.Text(root)
	t.pack()
	AutoComplete(t)



	root.mainloop()
