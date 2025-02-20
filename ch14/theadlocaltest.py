import threading

local_school = threading.local();
def process_student():
    std  = local_school.tt;
    print('hello,%s in (%s)' %(std ,threading.current_thread().name))


def process_thread(name):
    local_school.tt = name
    process_student()


t1 = threading.Thread(target=process_thread,args=('Alice',),name='ThreadA')
t2 = threading.Thread(target=process_thread,args=('Bob',),name='ThreadB')

t1.start()
t2.start()
t1.join()
t2.join()