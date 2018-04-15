from multiprocessing import Process
import os
import shutil
import filecmp

#shutil.copy('abc.txt', 'nick1.txt')
#shutil.copy('H:\\282\\cn_mabinogi_setup_282.0', 'I:\\candc')

#shutil.copy(r'H:\282\abc.txt', r'I:\candc')

def cp1():
    shutil.copy(r'H:\282\cn_mabinogi_setup_282.0', r'I:\candc')
    if filecmp.cmp(r'H:\282\cn_mabinogi_setup_282.0', r'I:\candc\cn_mabinogi_setup_282.0'):
        print('cp1 pass')

def cp2():
    shutil.copy(r'H:\282\cn_mabinogi_setup_282.0', r'J:\candc')
    if filecmp.cmp(r'H:\282\cn_mabinogi_setup_282.0', r'J:\candc\cn_mabinogi_setup_282.0'):
        print('cp2 pass')

if __name__=='__main__':
    p1 = Process(target= cp1)
    p2 = Process(target= cp2)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    input('nick')
