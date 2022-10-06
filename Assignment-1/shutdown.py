import PySimpleGUI as sg
import os, random, string, json

dir = "C:\Program Files\Bitcoin\daemon"
os.chdir(dir)

os.system("bitcoin-cli stop")