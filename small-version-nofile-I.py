import time, csv, sys, datetime
from Tkinter import *
import os


dates = []
dates2 = [['2010-01-01 05:05:21.992','Name1','path1','asdf','juir8','test'],['2011-06-12 05:05:32.122','Name2','path2','3','sad','fsad','test']]


class App:
    def __init__(self, master):
        frame = LabelFrame(master, text='CSV to Gource', padx=10, pady=10)
        frame.pack(padx=15, pady=15)

        self.textinfo = Message(frame, justify='center', relief='ridge', text='Welcome to CSV to Gource. Please prepare a CSV file from SQL based on the CSV to Gource readme specs, then select your action.')
        self.textinfo.pack()
        
        self.csvinit = Button(frame, text="Csv to Gource", command=self.csvtogource)
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
        print dates
    
#the following lines will handle writing files and running those files in gource

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

root = Tk() #names and creates an instance of Tk
app = App(root) #Provides the class data to Tk, also names this instance 'app'
root.mainloop() #loops the application, in this case our class
root.destroy() #destroys the window/quits the app once the loop is exited


