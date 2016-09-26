import time, csv, sys, datetime
from Tkinter import *
import tkMessageBox
import os


dates = []
dates2 = [['2010-01-01 05:05:21.992','Name1','path1','asdf','juir8','test'],
              ['2011-06-12 05:05:32.122','Name2','path2','3','sad','fsad','test']]


class App:
    def __init__(self, master):
        frame = LabelFrame(master, text='CSV to Gource', padx=10, pady=10)
        frame.pack(padx=15, pady=15)

        #self.textinfo = Message(frame, justify='center', text='GNU GPL-3.0 Copyleft 09/2016')
        #self.textinfo.pack()
        logo = PhotoImage(file='sloum2.gif')
        self.sloum = Label(frame, image=logo)
        self.sloum.logo = logo
        self.sloum.pack()
        
        self.csvinit = Button(frame, text="Format CSV for Gource", command=self.csvtogource)
        self.csvinit.pack()

        self.csvinit = Button(frame, text="Run CSV In Gource", command=self.runInGource)
        self.csvinit.pack()

        self.button = Button(frame, text="Quit", command=frame.quit)
        self.button.pack()

        
    def csvtogource(self):
        templist = []
        for list in dates2:
            for x, item in enumerate(list):
                if x == 0:
                    try:
                        list[x] = int(time.mktime(datetime.datetime.strptime(item, '%Y-%m-%d %H:%M:%S.%f').timetuple()))
                    except StandardError:
                        pass
                    templist.append(list[x])
                elif x == 1:
                    templist.append(list[x])
                elif x == 2:
                    concatversion = '/'.join(list[2:len(list)-1])
                    concatversion = concatversion + '.' + list[len(list)-1]
                    templist.append(concatversion)
                else:
                    pass
            dates.append(templist)
            templist = []
        tkMessageBox.showinfo('Format CSV','File creation complete,\nPlease proceed to next step')

    def runInGource(self):
        gourcecommands = raw_input('Please provide a comma separated list of Gource run time commands, or type "none":')
        print gourcecommands
        
##        outputdata = dates2
##
##        outFile = open('test.txt', 'w')
##        for row in outputdata:
##            for itemnum, item in enumerate(row):
##                if itemnum == 0:
##                    outFile.write(str(item)[:-2])
##                    if itemnum < len(row)-1:
##                        outFile.write('|')
##                    else:
##                        pass
##                else:
##                    outFile.write(str(item))
##                    if itemnum < len(row)-1:
##                        outFile.write('|')
##                    else:
##                        pass
##            outFile.write('\n')
##        outFile.close()
##        os.system('Gource ./text.txt')
##
##        

root = Tk() 
app = App(root)
root.mainloop() 
root.destroy() #destroys the window/quits the app once the loop is exited


