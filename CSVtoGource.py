import csv, time, datetime, tkMessageBox, os, random
from Tkinter import *
from tkFileDialog import askopenfilename




dates = []
#dates2 = [['2010-01-01 05:05:21.992','Name1','path1','asdf','juir8','test'],
#              ['2011-06-12 05:05:32.122','Name2','path2','3','sad','fsad','test']]


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
        newlines = []
        filename = askopenfilename()
        csvTABdata = list(csv.reader(open(filename, 'rb'), delimiter='\t'))
        
        
        for sublist in csvTABdata:
            for x, item in enumerate(sublist):
                if x == 0: #loadHistoryComplete
                    try:
                        sublist[x] = time.mktime(datetime.datetime.strptime(item, '%Y-%m-%d %H:%M:%S.%f').timetuple())
                    except StandardError:
                        pass
                     
                elif x == 1: #LoadAuthor
                    pass
                  
                elif x == 2: #Environment
                    pass
        
                elif x == 3: #PeriodID
                    pass
                  
                elif x == 4: #LoadReason
                    sublist[x] = sublist[x].replace(' ','')
                 
                elif x == 5: #Loaded CarrierID list
                    if sublist[x] == 'NULL':
                        pass
                    else:
                        carrierIdLoadList = sublist[x].split(',')
                        for key, carrierID in enumerate(carrierIdLoadList):
                            templist = []
                            templist.append(sublist[0])
                            templist.append(sublist[1])
                            templist.append('A')
                            templist.append(str(sublist[1]+'/'+sublist[2]+'/'+sublist[3]+'/'+carrierIdLoadList[key]+'.'+sublist[4]))
                            newlines.append(templist)


                             
                elif x == 6: #Removed carrierID list
                    if sublist[x] == 'NULL':
                        pass
                    else:
                        removeIdLoadList = sublist[x].split(',')
                        for key2, removeID in enumerate(removeIdLoadList):
                            templist2 = []
                            templist2.append(sublist[0])
                            templist2.append(sublist[1])
                            templist2.append('D')
                            templist2.append(str(sublist[1]+'/'+sublist[2]+'/'+sublist[3]+'/'+removeIdLoadList[key2]+'.'+sublist[4]))
                            newlines.append(templist2)

                else:
                    pass


        newlines = sorted(newlines)

       
        outFile = open('final.log', 'w')
        for row in newlines:
            for itemnum, item in enumerate(row):
                if itemnum == 0:
                    outFile.write(str(item)[:-2])
                    if itemnum < len(row)-1:
                        outFile.write('|')
                    else:
                        pass
                else:
                    outFile.write(str(item))
                    if itemnum < len(row)-1:
                        outFile.write('|')
                    else:
                        pass
            outFile.write('\n')
        outFile.close()
        

        #Box confirming file was written
        tkMessageBox.showinfo('Format CSV','File creation complete,\nPlease proceed to next step')

    def runInGource(self):
        gourcecommands = raw_input('Please provide a comma separated list of Gource run time commands, or type "none":')
        os.system('Gource '+gourcecommands+' final.log')
        
   

root = Tk() 
app = App(root)
root.mainloop() 
root.destroy() #destroys the window/quits the app once the loop is exited
