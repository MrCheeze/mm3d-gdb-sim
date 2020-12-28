gdb_path = "C:\\MinGW\\bin\\gdb.exe"
citra_path = "C:\\Users\\Matthew\\Documents\\git\\citra\\build\\bin\\citra-qt.exe"
mm3d_path = "C:\\Users\\Matthew\\Documents\\Emulation\\Majora ACE\\3DS1192 - The Legend Of Zelda Majoras Mask 3D ( Usa) Decrypted.3ds"

### not ideal to hardcode this, but whatever
player_addr = 0x09022400
#player_addr = 0x0934F3C0

VK_CODE = {'backspace':0x08,
           'tab':0x09,
           'clear':0x0C,
           'enter':0x0D,
           'shift':0x10,
           'ctrl':0x11,
           'alt':0x12,
           'pause':0x13,
           'caps_lock':0x14,
           'esc':0x1B,
           'spacebar':0x20,
           'page_up':0x21,
           'page_down':0x22,
           'end':0x23,
           'home':0x24,
           'left_arrow':0x25,
           'up_arrow':0x26,
           'right_arrow':0x27,
           'down_arrow':0x28,
           'select':0x29,
           'print':0x2A,
           'execute':0x2B,
           'print_screen':0x2C,
           'ins':0x2D,
           'del':0x2E,
           'help':0x2F,
           '0':0x30,
           '1':0x31,
           '2':0x32,
           '3':0x33,
           '4':0x34,
           '5':0x35,
           '6':0x36,
           '7':0x37,
           '8':0x38,
           '9':0x39,
           'a':0x41,
           'b':0x42,
           'c':0x43,
           'd':0x44,
           'e':0x45,
           'f':0x46,
           'g':0x47,
           'h':0x48,
           'i':0x49,
           'j':0x4A,
           'k':0x4B,
           'l':0x4C,
           'm':0x4D,
           'n':0x4E,
           'o':0x4F,
           'p':0x50,
           'q':0x51,
           'r':0x52,
           's':0x53,
           't':0x54,
           'u':0x55,
           'v':0x56,
           'w':0x57,
           'x':0x58,
           'y':0x59,
           'z':0x5A,
           'numpad_0':0x60,
           'numpad_1':0x61,
           'numpad_2':0x62,
           'numpad_3':0x63,
           'numpad_4':0x64,
           'numpad_5':0x65,
           'numpad_6':0x66,
           'numpad_7':0x67,
           'numpad_8':0x68,
           'numpad_9':0x69,
           'multiply_key':0x6A,
           'add_key':0x6B,
           'separator_key':0x6C,
           'subtract_key':0x6D,
           'decimal_key':0x6E,
           'divide_key':0x6F,
           'F1':0x70,
           'F2':0x71,
           'F3':0x72,
           'F4':0x73,
           'F5':0x74,
           'F6':0x75,
           'F7':0x76,
           'F8':0x77,
           'F9':0x78,
           'F10':0x79,
           'F11':0x7A,
           'F12':0x7B,
           'F13':0x7C,
           'F14':0x7D,
           'F15':0x7E,
           'F16':0x7F,
           'F17':0x80,
           'F18':0x81,
           'F19':0x82,
           'F20':0x83,
           'F21':0x84,
           'F22':0x85,
           'F23':0x86,
           'F24':0x87,
           'num_lock':0x90,
           'scroll_lock':0x91,
           'left_shift':0xA0,
           'right_shift ':0xA1,
           'left_control':0xA2,
           'right_control':0xA3,
           'left_menu':0xA4,
           'right_menu':0xA5,
           'browser_back':0xA6,
           'browser_forward':0xA7,
           'browser_refresh':0xA8,
           'browser_stop':0xA9,
           'browser_search':0xAA,
           'browser_favorites':0xAB,
           'browser_start_and_home':0xAC,
           'volume_mute':0xAD,
           'volume_Down':0xAE,
           'volume_up':0xAF,
           'next_track':0xB0,
           'previous_track':0xB1,
           'stop_media':0xB2,
           'play/pause_media':0xB3,
           'start_mail':0xB4,
           'select_media':0xB5,
           'start_application_1':0xB6,
           'start_application_2':0xB7,
           'attn_key':0xF6,
           'crsel_key':0xF7,
           'exsel_key':0xF8,
           'play_key':0xFA,
           'zoom_key':0xFB,
           'clear_key':0xFE,
           '+':0xBB,
           ',':0xBC,
           '-':0xBD,
           '.':0xBE,
           '/':0xBF,
           '`':0xC0,
           ';':0xBA,
           '[':0xDB,
           '\\':0xDC,
           ']':0xDD,
           "'":0xDE,
           '`':0xC0}

import win32com.client
import win32con
import win32gui
import win32api
import win32console
from subprocess import Popen, PIPE, CREATE_NO_WINDOW
import time
import os
import win32api
import signal
import random
import ctypes
from datetime import datetime

def gdbStop():
    # surprisingly difficult to do this programatically, just use this tool
    Popen(['windows-kill.exe','-SIGINT',str(gdb_pid)], creationflags = CREATE_NO_WINDOW)

def gdb(command):
    command += '\n'
    gdb_process.stdin.write(command.encode('ascii'))
    gdb_process.stdin.flush()
    time.sleep(0.1)
    gdb_process.stdout.flush()
    output = os.read(gdb_process.stdout.fileno(),999999).decode('ascii').split(os.linesep)
    #print(output)
    return output

def citraPressKey(key):
    hwndMain = win32gui.FindWindow(None, "Citra | Majora's Mask 3D")
    hwndChild = win32gui.GetWindow(hwndMain, win32con.GW_CHILD)
    win32api.PostMessage(hwndChild, win32con.WM_KEYDOWN, VK_CODE[key], 0)
    
def citraReleaseKey(key):
    hwndMain = win32gui.FindWindow(None, "Citra | Majora's Mask 3D")
    hwndChild = win32gui.GetWindow(hwndMain, win32con.GW_CHILD)
    win32api.PostMessage(hwndChild, win32con.WM_KEYUP, VK_CODE[key], 0)
    
def citraKey(key, dur=0.07):
    time.sleep(0.01)
    citraReleaseKey(key) # shouldn't be needed...
    time.sleep(0.01)
    citraPressKey(key)
    time.sleep(dur)
    citraReleaseKey(key)
    time.sleep(0.01)

def moveLink(x,y,z,rot):
    gdbStop()
    gdb("set *(float[3] *)(0x%X+0x24) = {%f,%f,%f}" % (player_addr, x,y,z))
    gdb("set *(short[1] *)(0x%X+0xC2) = {%d}" % (player_addr, rot))
    gdb('continue')

def keyForItem(item,releaseSword=False):
    if item=='bomb':
        citraKey('s')
    elif item=='bombchu':
        citraKey('a')
    elif item=='sword':
        if releaseSword:
            citraReleaseKey('z')
        else:
            citraPressKey('z')
    else:
        citraKey('j') # dummy
        assert item is None

def getHeldActorAddress():
    gdbStop()
    output = gdb("x/1wx %s+0x920" % (player_addr))
    heldActor = int(output[-2][-10:],base=16)
    #print('held actor:', hex(heldActor))
    gdb('continue')
    return heldActor

def getHeldActorSize():
    heldActor = getHeldActorAddress()
    gdbStop()
    output = gdb("x/1wx %s-0x10" % (heldActor))
    heldActorSize = 0x100000000-int(output[-2][-10:],base=16)
    gdb('continue')
    return heldActorSize

def getTargetActorAddress():
    gdbStop()
    output = gdb("x/1wx %s+0xDFC" % (player_addr))
    targetActor = int(output[-2][-10:],base=16)
    gdb('continue')
    return targetActor

Popen([ 'taskkill', '/F', '/IM', citra_path.split('\\')[-1] ], creationflags = CREATE_NO_WINDOW)
Popen([ 'taskkill', '/F', '/IM', gdb_path.split('\\')[-1] ], creationflags = CREATE_NO_WINDOW)

time.sleep(2)

citra_process = Popen([citra_path, mm3d_path])
citra_pid = citra_process.pid
time.sleep(3)
gdb_process = Popen([gdb_path], stdin = PIPE, stdout = PIPE, creationflags = CREATE_NO_WINDOW)
gdb_pid = gdb_process.pid

time.sleep(3)
gdb('target remote :24689')
time.sleep(1)
gdb('continue')

heapWindow = win32gui.FindWindow(None, "MM3D Heap Viewer")
if heapWindow:
    win32gui.PostMessage(heapWindow,win32con.WM_CLOSE,0,0)

time.sleep(3)

possiblePermutations = {
    'roomAtStart0': [None, 'left', 'right'],
    'roomAtStartItem0': [None, 'bomb', 'bombchu', 'bombchu'],
    'roomAtStart1': [None, 'left', 'right'],
    'roomAtStartItem1': [None, 'bomb', 'bombchu', 'bombchu'],
    'roomAtStart2': [None, 'left', 'right'],
    'roomAtStartItem2': [None, 'bomb', 'bombchu', 'bombchu'],
    'transitionItem1': [None, 'bomb', 'bombchu', 'sword', 'bombchu'],
    'leftRupee1': [False, True],
    'leftRupee2': [False, True],
    'leftRupee3': [False, True],
    'leftPause': {'min':6,'max':6},#{'min':0, 'max':6},
    'transitionItem2': [None, 'bomb', 'bombchu', 'sword', 'bombchu'],
    'rightNutLoaded': [False, True],
 }

outfile = open('output/out_%s.txt'%datetime.now().strftime('%Y%m%d%H%M%S'),'w')

def write(string):
    print(string)
    outfile.write(str(string)+'\n')
    outfile.flush()

while True:

    perm = possiblePermutations.copy()
    for key in perm:
        if type(perm[key]) == dict:
            perm[key] = random.uniform(perm[key]['min'],perm[key]['max'])
        else:
            perm[key] = random.choice(perm[key])

    
    write(perm)

    time.sleep(0.5)
    citraKey('0',dur=0.5) # load most recent save

    time.sleep(2.5)

    for i in range(3):
        room = perm['roomAtStart'+str(i)]
        if room:
            if room == 'left':
                moveLink(0,0,1690,0xC000)
            else:
                moveLink(0,0,1690,0x4000)
            time.sleep(0.3)
            citraKey('q')
            time.sleep(0.3)
            keyForItem(perm['roomAtStartItem'+str(i)])
            time.sleep(0.3)
            citraKey('up_arrow', 2.4)
            keyForItem(perm['roomAtStartItem'+str(i)])
            citraKey('down_arrow', 2.4)
            time.sleep(0.3)
    moveLink(10,0,1691,0xC000)
    time.sleep(0.3)
    moveLink(-270,0,1684,0xC000)
    time.sleep(0.3)
    citraKey('q')
    time.sleep(0.3)

    keyForItem(perm['transitionItem1'])
    time.sleep(0.5)
    citraKey('up_arrow', 2.2)
    keyForItem(perm['transitionItem1'],releaseSword=True)
    time.sleep(1)
    if perm['leftRupee1']:
        moveLink(-515, 0, 1559, 0x8000)
    else:
        moveLink(-598, 0, 1710, 0xC000)
    time.sleep(2)
    if perm['leftRupee2']:
        moveLink(-449, 0, 1561, 0x8000)
    else:
        moveLink(-598, 0, 1710, 0xC000)
    time.sleep(2)
    if perm['leftRupee3']:
        moveLink(-385, 0, 1564, 0x8000)
    else:
        moveLink(-598, 0, 1710, 0xC000)
    time.sleep(2)
    moveLink(-334, 100, 1727, 0x720E)
    time.sleep(2)
    citraKey('s')
    time.sleep(0.5)
    citraKey('s')
    time.sleep(0.5)
    moveLink(-336, 92, 1732, 0xFB34)
    time.sleep(3)
    citraKey('left_arrow', 1)
    time.sleep(0.5)
    moveLink(-183, 160, 1954, 0x3CAC)
    time.sleep(0.2)
    citraKey('q')
    time.sleep(perm['leftPause'])
    keyForItem(perm['transitionItem2'])
    time.sleep(0.2)
    citraKey('up_arrow', 2)
    keyForItem(perm['transitionItem2'],releaseSword=True)
    if perm['transitionItem2']:
        citraKey('w',dur=7.5)
    time.sleep(0.25)

    seen_msgs = set()
    for i in range(25):

        try:
            time.sleep(0.25)
            moveLink(250, 160, 1947, 0x4000)
            time.sleep(0.25)
            citraKey('q')
            time.sleep(0.25)
            #if i==5:
            #    break
            citraKey('up_arrow', 1.2)
            citraKey('w',dur=0.8)
            moveLink(373, 160, 2024, 0xA48B)
            time.sleep(0.8)
            firstPotAddr = getHeldActorAddress()
            firstPotSize = getHeldActorSize()
            moveLink(373, 160, 2072, 0xA48B)
            time.sleep(0.8)
            secondPotAddr = getHeldActorAddress()
            secondPotSize = getHeldActorSize()
            msg = '1stPotAddr=%X, 1stPotSize=%X, 2ndPotAddr=%X, 2ndPotSize=%X'%(firstPotAddr,firstPotSize,secondPotAddr,secondPotSize)
            write(msg)
            if msg in seen_msgs:
                break
            if firstPotSize == 0x2E0 or secondPotSize == 0x2E0:
                raise Exception('found setup?')
            seen_msgs.add(msg)
            moveLink(365, 170, 1951, 0xC000)
            time.sleep(0.1)
            citraKey('q')
            time.sleep(0.2)
            if perm['rightNutLoaded']:
                time.sleep(1)
            citraKey('a')
            time.sleep(0.2)
            citraKey('up_arrow', 2)
        except ValueError:
            gdb('continue')
            break

    time.sleep(2.5)
