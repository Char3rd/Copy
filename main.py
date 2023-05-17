from pynput.keyboard import Controller
from pynput import keyboard
from threading import Thread
from time import sleep
import sys

ALT = False
C = False
Q = False

def output():
    with open('text.txt', 'r', encoding='UTF-8') as f:
        lines = f.readlines()
    
    keyboard_out = Controller()

    for line in lines:
        keyboard_out.type(line)

    print ('end')

def listen(): 
     
    def on_press(key):
        global ALT, C, Q
        if key == keyboard.Key.alt or key == keyboard.Key.alt_l or key == keyboard.Key.alt_r:
            ALT = True
        if key == keyboard.KeyCode(char='c') or key == keyboard.KeyCode(char='C'):
            C = True
        if key == keyboard.KeyCode(char='q') or key == keyboard.KeyCode(char='Q'):
            Q = True

        if ALT and C: 
            ALT = C = False
            sleep(1)
            outputThread = OutputThread()
            outputThread.start()

        if ALT and Q:
            sys.exit()

    def on_release(key):
        global ALT, C
        if key == keyboard.Key.alt or key == keyboard.Key.alt_l or key == keyboard.Key.alt_r:
            ALT = False
        if key == keyboard.KeyCode(char='c') or key == keyboard.KeyCode(char='C'):
                C = False

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()

class ListenThread(Thread):

    def __init__(self):
        super().__init__()

    def run(self):
        listen()

class OutputThread (Thread):
     
    def __init__(self):
        super().__init__()
    
    def run(self):
        output()


if __name__ == '__main__':
    listenThread = ListenThread()  
    listenThread.start()

'''
    需要安装依赖 pynput

    pip install pynput

    使用前请务必调成英文输入法

    将你要输出的文本粘贴指同目录中的 text.txt文件夹中

    Maijs 2023/5/17
'''