import colorama
import sys
import time
import pytest
import numpy as np
import math
import time
import pynmea2
import serial

# from process import timing_bits as p
# from process import find as find
# from process import serialcomms as s
# from process import gps as g

from process.timing_bits import *
from process.find import *
from process.serialcomms import *
from process.gps import *

black   =  '\033[1;30m'
red     =  '\033[1;31m'
green   =  '\033[1;32m'
yellow  =  '\033[1;33m'
blue    =  '\033[1;34m'
magenta =  '\033[1;35m'
cyan    =  '\033[1;36m'
white   =  '\033[1;37m'