
from tkinter import *
from tkinter.filedialog import *
from tkinter import ttk
import os

isat=Tk()
isat.title('Dummy File Creator')

screen_width = isat.winfo_screenwidth()
screen_height = isat.winfo_screenheight()
width = 590
height = 328
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
isat.geometry('%dx%d+%d+%d' % (width, height, x, y))
isat.resizable(0,0)

s=ttk.Style()
s.configure('TRadiobutton', font=('helvetica', 14), foreground='black')
s.configure('TButton', font=('helvetica', 10), foreground='blue')
s.configure('TLabel', font=('helvetica',12), foreground='black')
s.configure('TCombobox', font=('helvetica',12), foreground='black')
va=IntVar();

def save():
    spinget=int(spin.get())
    comboget=c.get()
    sav = asksaveasfilename(filetypes=(('dump file','*.dmp'),('All files','*.*')))
    if sav:
        if comboget=='Bytes' :
            result=spinget*1 ;
            with open(sav, 'wb') as f: f.write(os.urandom(result))
        elif comboget=='KB' :
            result=spinget*1024 ;
            with open(sav, 'wb') as f: f.write(os.urandom(result))
        elif comboget=='MB' :
            result=spinget*1024*1024 ;
            with open(sav, 'wb') as f: f.write(os.urandom(result))
        elif comboget=='GB' :
            result=spinget*1024*1024*1024 ;
            with open(sav, 'wb') as f: f.write(os.urandom(result))      
def browse():
    folder=askdirectory()
    if folder:
        en.config(text=folder)

current_dir = os.getcwd()
        
f=Frame(isat, width=500,height=10, relief='flat', bd=12 ); f.grid(row=0,column=0, pady=10, padx=24, stick='ew')
la=LabelFrame(f, text='Mode',font=('helvetica',12), fg='black')
la.grid(row=0, column=0, pady=10, padx=15)
rd1=ttk.Radiobutton(la, text='Single File', var=va, value=1)
rd1.grid(row=0, column=0, padx=4, pady=4)

rd2=ttk.Radiobutton(la, text='Multiple Files(needs a batch list)', var=va, value=2, state=DISABLED)
rd2.grid(row=0, column=1, padx=11, pady=3)
va.set(1)

f1=Frame(isat, width=450, height=9, relief='flat',);f1.grid(row=1, column=0, pady=3, stick='ew')
ttk.Label(f1, text='Path to store dummy file:', ).grid(row=0, column=0, pady=3, padx=2, )
en=Label(f1, text=f'{current_dir}',font=('helvetica',12), fg='black',width=30, bg='gray');
en.grid(row=0, column=1, ipadx=9, pady=3);
bt1=ttk.Button(f1, text='Browse', command=browse);bt1.grid(row=0, column=3, padx=4, pady=3,)


f2=Frame(isat, width=200, height=9, relief='flat',);
f2.grid(row=2, column=0, pady=3, stick='ew')

lbl=ttk.Label(f2, text='File Size:\t',);
lbl.grid(row=0, column=0, pady=9,)
spin=Spinbox(f2, from_=1, to=100, width=6,  font=('helvetica',12) );
spin.grid(row=0 ,column=1,pady=6,padx=1,)

lbl=ttk.Label(f2, text="Select Unit:\t",);
lbl.grid(row=0, column=2, pady=9,)
c=ttk.Combobox(f2, width='7',  )
c['values']=('Bytes', 'KB', 'MB', 'GB')
c.grid(row=0, column=3, stick='w')   
chk=Checkbutton(f2, text='Random File Content(non compresible)', font=('helvetica',11));
chk.grid(row=2, column=1, pady=10)

f3=Frame(isat, width=200, height=5, relief='flat',);f3.grid(row=3, column=0, pady=10, stick='ew')
Label(f3, width=27).grid(row=2, column=0)
Button(f3, text='Create', command=save, width=5, bd=0,fg='blue', font=('helvetica',14)).grid(row=2, column=1, pady=3, padx=10)
Button(f3, text='Exit', width=5, fg='red',bd=0, font=('helvetica',14)).grid(row=2, column=2, pady=3, padx=10, stick='e')

Label(f3, text=u'\N{COPYRIGHT SIGN}' " issat 2019", fg='green').grid(row=4, column=0, stick='s')
isat.rowconfigure(1, weight=0)
isat.columnconfigure(1, weight=0)

mainloop()
