import re
import datetime
class Enter_lane_reader1():
    def __init__(self):
        self.en_amb_time = {}
        self.en = None
        self.no = None
        self.ambno_signo={}
        self.time_entered = None
    def ambulance_enters_reader1(self):
        self.en=[str(i) for i in input("ambulance data:").split()]
        self.no=[str(i) for i in input("signal no. on ambulance data:").split()]
        self.time_entered = datetime.datetime.now()
    def amb_sig_no(self):
        i = 0
        for j in self.en:
            self.ambno_signo[j] = self.no[i]
            i = i+1
        print(self.ambno_signo)
        self.ambno_signo=list(self.ambno_signo.items())
        self.ambno_signo.sort(reverse=True)
        print("ordered list of Ambulance with signal",self.ambno_signo)
        self.en.sort(reverse=True)
    def amb_en_time(self):
        for j in self.en:
            self.en_amb_time[j] = self.time_entered
            print("Ambulance time:",self.en_amb_time)
objenreader1=Enter_lane_reader1()
objenreader1.ambulance_enters_reader1()
objenreader1.amb_sig_no()

class Enter_lane_reader2():
    def __init__(self):
        self.ex_amb_time = {}
        self.ex = None
        self.time_passed = None
    def ambulance_enters_reader2(self):
        self.ex=[str(i) for i in input("Ambulance detected in Exit RFID:").split()]
        self.ex.sort(reverse=True)
        self.time_passed = datetime.datetime.now()
        print(self.ex)
    def amb_ex_time(self):
        for j in self.ex:
            self.ex_amb_time[j]=self.time_passed
            print(self.ex_amb_time)
objenreader2=Enter_lane_reader2()
objenreader2.ambulance_enters_reader2()
objenreader2.amb_ex_time()

class Update_entrance2(Enter_lane_reader2):
    def updated_list_of_reader2(self):
        self.equated_list = objenreader1.en
        for i in objenreader2.ex:
            if i in self.equated_list:
                self.equated_list.remove(i)
                print("Remaining list of Ambulance in junction:",self.equated_list)
objupdate_list1=Update_entrance2()
objupdate_list1.updated_list_of_reader2()

class database_of_ambulance_passed():
    print("Database of Ambulance Passed The Junction:")
    def ambulance_db(self):
        i = 0
        self.amb_nu = []
        for key,value in objenreader1.ambno_signo:
            amb_no = re.findall("TN\d\d\w\w\d\d\d\d",key)
            self.amb_nu.append(amb_no)
        while i <= len(objenreader1.ambno_signo):
            if objenreader1.ambno_signo[i] in objenreader2.ex[i]:
                print("Ambulance no. %s entered lane %s on %s and passed the signal at %s"%(self.amb_nu[i],objenreader1.ambno_signo[objenreader1.ambno_signo[i]],objenreader1.time_entered,objenreader2.ex_amb_time[objenreader1.ambno_signo[i]]))
            else:
                print("Ambulance no. %s entered lane %s on %s and not passed the signal"%(self.amb_nu[i],objenreader1.ambno_signo[objenreader1.ambno_signo[i]],objenreader1.time_entered))
            i=i+1
            '''for p in objenreader2.ex_amb_time:
                print(p)
                if p in objenreader2.ex:
                    print("Ambulance no. %s entered lane %s on %s and passed the signal at %s"%(amb_no,value,objenreader1.time_entered,objenreader2.ex_amb_time[p]))
                else:
                    print("Ambulance no. %s entered lane %s on %s and not passed still" % (
                    amb_no, value, objenreader1.time_entered))'''
        print(self.amb_nu)
objdata=database_of_ambulance_passed()
objdata.ambulance_db()


