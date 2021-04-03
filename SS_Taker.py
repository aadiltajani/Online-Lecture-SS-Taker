import datetime
import os
import time
import pyautogui
import tkinter as tk

ajud = 'AJ/UD'
cpdp = 'CPDP/2'
mivj = 'MI/VJ'
dv = 'DV'
mi = 'MI'
tocdk = 'TOC/DK'
ajvj = 'AJ/VJ'
mibb = 'MI/BB'
dm = 'DM'
aj = 'AJ'
tocjb = 'TOC/JB'
toc = 'TOC'


def get_path():
    time_slot = 0
    time_range = [[8, 30], [9, 30], [10, 45], [11, 45], [13, 30], [14, 30]]
    cur = datetime.datetime.now().time()
    for i in enumerate(time_range):
        cr = datetime.time(hour=i[1][0], minute=i[1][1])
        delta = datetime.timedelta(hours=cur.hour, minutes=cur.minute) - datetime.timedelta(hours=cr.hour,
                                                                                            minutes=cr.minute)
        if str(delta).split(':')[0] == '0':
            time_slot = i[0]
    tt = {'Mon': [ajud, cpdp, mivj, dv, aj, aj], 'Tue': [dv, dv, tocdk, ajvj, mibb, dm],
          'Wed': [tocdk, cpdp, dm, mibb, mi, mi], 'Thu': [dm, dm, tocjb, dv, '', ''],
          'Fri': [dv, dv, tocjb, dm, ajvj, toc]}
    if not os.path.exists('D:/Class Notes/' + tt[str(time.strftime('%a'))][time_slot]):
        os.makedirs('D:/Class Notes/' + tt[str(time.strftime('%a'))][time_slot])
    path = 'D:/Study & Pojeks/CLASS NOTES/' + tt[str(time.strftime('%a'))][time_slot] + '/Screenshot ' + str(
        time.strftime('%Y-%m-%d %H%M%S ')) + '.png'
    return path


root = tk.Tk()
root.title('SS')
canvas1 = tk.Canvas(root, width=230, height=60)
canvas1.pack()


def takeScreenshot():
    root.withdraw()
    time.sleep(0.17)
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(get_path())
    root.deiconify()


myButton = tk.Button(text='Take Screenshot', command=takeScreenshot, bg='green', fg='white', font=5)
canvas1.create_window(120, 30, window=myButton)

root.mainloop()