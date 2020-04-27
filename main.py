import sys
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True



def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Google_Map_Extactor (root)
    
    root.mainloop()

w = None
def create_Google_Map_Extactor(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Google_Map_Extactor (w)
    _support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Google_Map_Extactor():
    global w
    w.destroy()
    w = None

class Google_Map_Extactor:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("314x481+576+301")
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=-0.223, rely=-0.042, relheight=0.218
                , relwidth=2.022)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#1154d8")
        self.Frame1.configure(width=635)

        self.Title = tk.Label(top)
        self.Title.place(relx=0.064, rely=0.01, height=61, width=264)
        self.Title.configure(background="#1154d8")
        self.Title.configure(disabledforeground="#a3a3a3")
        self.Title.configure(font="-family {Bluefish Black Demo} -size 14 -weight bold")
        self.Title.configure(foreground="#fffdfa")
        self.Title.configure(text='''Google Maps Extractor''')
        self.Title.configure(width=264)

        self.Countrylabel = tk.Label(top)
        self.Countrylabel.place(relx=0.016, rely=0.198, height=31, width=90)
        self.Countrylabel.configure(background="#d9d9d9")
        self.Countrylabel.configure(disabledforeground="#a3a3a3")
        self.Countrylabel.configure(foreground="#000000")
        self.Countrylabel.configure(text='''Country Code:''')
        self.Countrylabel.configure(width=90)

        self.countrycode = tk.Entry(top)
        self.countrycode.place(relx=0.303, rely=0.218, height=20, relwidth=0.363)

        self.countrycode.configure(background="white")
        self.countrycode.configure(disabledforeground="#a3a3a3")
        self.countrycode.configure(font="TkFixedFont")
        self.countrycode.configure(foreground="#000000")
        self.countrycode.configure(insertbackground="black")
        self.countrycode.configure(width=114)

        self.Countrylabel_1 = tk.Label(top)
        self.Countrylabel_1.place(relx=-0.032, rely=0.27, height=31, width=90)
        self.Countrylabel_1.configure(activebackground="#f9f9f9")
        self.Countrylabel_1.configure(activeforeground="black")
        self.Countrylabel_1.configure(background="#d9d9d9")
        self.Countrylabel_1.configure(disabledforeground="#a3a3a3")
        self.Countrylabel_1.configure(foreground="#000000")
        self.Countrylabel_1.configure(highlightbackground="#d9d9d9")
        self.Countrylabel_1.configure(highlightcolor="black")
        self.Countrylabel_1.configure(text='''Keyword:''')

        self.keyword = tk.Entry(top)
        self.keyword.place(relx=0.303, rely=0.281,height=20, relwidth=0.363)
        self.keyword.configure(background="white")
        self.keyword.configure(disabledforeground="#a3a3a3")
        self.keyword.configure(font="TkFixedFont")
        self.keyword.configure(foreground="#000000")
        self.keyword.configure(highlightbackground="#d9d9d9")
        self.keyword.configure(highlightcolor="black")
        self.keyword.configure(insertbackground="black")
        self.keyword.configure(selectbackground="#c4c4c4")
        self.keyword.configure(selectforeground="black")

        self.TProgressbar1 = ttk.Progressbar(top)
        self.TProgressbar1.place(relx=-0.032, rely=0.956, relwidth=1.146
                , relheight=0.0, height=22)
        self.TProgressbar1.configure(length="360")

        self.Countrylabel_2 = tk.Label(top)
        self.Countrylabel_2.place(relx=0.0, rely=0.333, height=31, width=110)
        self.Countrylabel_2.configure(activebackground="#f9f9f9")
        self.Countrylabel_2.configure(activeforeground="black")
        self.Countrylabel_2.configure(background="#d9d9d9")
        self.Countrylabel_2.configure(disabledforeground="#a3a3a3")
        self.Countrylabel_2.configure(foreground="#000000")
        self.Countrylabel_2.configure(highlightbackground="#d9d9d9")
        self.Countrylabel_2.configure(highlightcolor="black")
        self.Countrylabel_2.configure(text='''List of city Names:''')
        self.Countrylabel_2.configure(width=110)

        self.citylists = tk.Text(top)
        self.citylists.place(relx=0.127, rely=0.395, relheight=0.383
                , relwidth=0.745)
        self.citylists.configure(background="white")
        self.citylists.configure(font="TkTextFont")
        self.citylists.configure(foreground="black")
        self.citylists.configure(highlightbackground="#d9d9d9")
        self.citylists.configure(highlightcolor="black")
        self.citylists.configure(insertbackground="black")
        self.citylists.configure(selectbackground="#c4c4c4")
        self.citylists.configure(selectforeground="black")
        self.citylists.configure(width=234)
        self.citylists.configure(wrap="word")

        self.Runbtn = tk.Button(top)
        self.Runbtn.place(relx=0.143, rely=0.79, height=34, width=227)
        self.Runbtn.configure(activebackground="#ececec")
        self.Runbtn.configure(activeforeground="#000000")
        self.Runbtn.configure(background="#09d82b")
        self.Runbtn.configure(disabledforeground="#a3a3a3")
        self.Runbtn.configure(font="-family {Segoe UI} -size 14 -weight bold")
        self.Runbtn.configure(foreground="#000000")
        self.Runbtn.configure(highlightbackground="#d9d9d9")
        self.Runbtn.configure(highlightcolor="black")
        self.Runbtn.configure(pady="0")
        self.Runbtn.configure(text='''Run!''')
        self.Runbtn.configure(width=227)
 
if __name__ == '__main__':
    vp_start_gui()
 
 

