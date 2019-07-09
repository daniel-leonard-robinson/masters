from __future__ import print_function
from process.globals import *

colorama.init()

# print (yellow, 'Welcome to the', green, 'AT command', yellow, 'tester by Daniel Robinson.')

def setup_module(module):
    print()
    serialOpen()
 
def teardown_module(module):
    serialClose()

def test_capture():
    capture(1000)

def test_nuestats():
    print(yellow + nuestats())

def test_view():
        tPTW = [2.56,5.12,7.68,10.24,12.8,15.36,17.92,20.48,23.04,25.6,28.16,30.72,33.28,35.84,38.4,40.96]
        tEDRX = [10.24, 20.48, 40.96, 81.92, 163.84, 327.68, 655.36, 1310.72, 1966.08, 2621.44]
        tActive = [2, 60, 360, 0]
        tPeriodicTau = [600, 3600, 36000, 2, 30, 60, 1152000, 0]

# 2340,33501,35841,116366.94,108
# 9521,29339,38860,62170.99,127

def test_edrxSet():
#     setEDRX(0, 9, 0, 5, 3, 10) # off. drx @104,4.3 ptau 72 drx @87,4.3, ptau 89, drx 70,4.3, ptau 106, drx 53,4.3, ptau 123, drx 36, 4.3, p140, 23.5
#     setEDRX(1, 4, 0, 5, 3, 10) # 20 sec delay. 2 drx. 30 sec ptau
#     setEDRX(0, 0, 0, 5, 3, 10) # 2.56 continuous
#     setEDRX(1, 0, 0, 10, 3, 15) # 2.56 cont, 30 sec ptau
#     setEDRX(0, 0, 0, 0, 3, 2) # 5.5 sec ptau
#     setEDRX(0, 1, 0, 1, 0, 1) # 12 2.56 DRX for 30 sec. silence after
#     setEDRX(0, 2, 0, 15, 3, 20) # one DRX at 20 sec. 30e, 30a, 40p
#     setEDRX(0, 1, 0, 15, 3, 20) # 2, 20, 30, 40 but 2, 30s ptau
    setEDRX(1, 0, 0, 15, 3, 15) # 2.56 cont, 30 sec ptau

def test_change():
        print()
        sendTIM('r')
        setEDRX(0, 9, 0, 5, 3, 10) # off
        test_capture(1)

def test_edrxQuery():
    edrxQuery()