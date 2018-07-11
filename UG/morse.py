# -*- coding: UTF-8 -*-
#from gpiozero import LED
from time import sleep

length = 0.25
#led = LED(17)

def dot():
#    led.on()
    print("."),
    sleep(1 * length)
#    led.off()

def dash():
#    led.on()
    print("-"),
    sleep(3 * length)
#    led.off()

def space():
    print(" "),
    sleep(1 * length)

def letter_space():
    print("   "),
    sleep(3 * length)

def word_space():
    print("\n")
    sleep(7 * length)

letters = {
	"A": lambda: [	dot(), space(), dash(), ],
	"B": lambda: [	dash(), space(),  dot(), space(), dot(), space(), dot(), ],
	"C": lambda: [	dash(), space(),  dot(), space(), dash(), space(),  dot(), ],
	"D": lambda: [	dash(), space(),  dot(), space(), dot(), ],
	"E": lambda: [	dot(), ],
	"F": lambda: [	dot(), space(), dot(), space(), dash(), space(),  dot(), ],
	"G": lambda: [	dash(), space(),  dash(), space(),  dot(), ],
	"H": lambda: [	dot(), space(), dot(), space(), dot(), space(), dot(), ],
	"I": lambda: [	dot(), space(), dot(), ],
	"J": lambda: [	dot(), space(), dash(), space(),  dash(), space(),  dash(), ],
	"K": lambda: [	dash(), space(),  dot(), space(), dash(), ],
	"L": lambda: [	dot(), space(), dash(), space(),  dot(), space(), dot(), ],
	"M": lambda: [	dash(), space(),  dash(), ],
	"N": lambda: [	dash(), space(),  dot(), ],
	"O": lambda: [	dash(), space(),  dash(), space(),  dash(), ],
	"P": lambda: [	dot(), space(), dash(), space(),  dash(), space(),  dot(), ],
	"Q": lambda: [	dash(), space(),  dash(), space(),  dot(), space(), dash(), ],
	"R": lambda: [	dot(), space(), dash(), space(),  dot(), ],
	"S": lambda: [	dot(), space(), dot(), space(), dot(), ],
	"T": lambda: [	dash(), ],
	"U": lambda: [	dot(), space(), dot(), space(), dash(), ],
	"V": lambda: [	dot(), space(), dot(), space(), dot(), space(), dash(), ],
	"W": lambda: [	dot(), space(), dash(), space(),  dash(), ],
	"X": lambda: [	dash(), space(),  dot(), space(), dot(), space(), dash(), ],
	"Y": lambda: [	dash(), space(),  dot(), space(), dash(), space(),  dash(), ],
	"Z": lambda: [	dash(), space(),  dash(), space(),  dot(), space(), dot(), ],
	u"Ä": lambda: [ 	dot(), space(), dash(), space(),  dot(), space(), dash(), ],
	u"Á": lambda: [ 	dot(), space(), dash(), space(),  dash(), space(),  dot(), space(), dash(), ],
	u"Å": lambda: [ 	dot(), space(), dash(), space(),  dash(), space(),  dot(), space(), dash(), ],
	u"É": lambda: [ 	dot(), space(), dot(), space(), dash(), space(),  dot(), space(), dot(), ],
	u"Ñ": lambda: [ 	dash(), space(),  dash(), space(),  dot(), space(), dash(), space(),  dash(), ],
	u"Ö": lambda: [ 	dash(), space(),  dash(), space(),  dash(), space(),  dot(), ],
	u"Ü": lambda: [ 	dot(), space(), dot(), space(), dash(), space(),  dash(), ],
	"0": lambda: [ 	dash(), space(),  dash(), space(),  dash(), space(),  dash(), space(),  dash(), ],
	"1": lambda: [ 	dot(), space(), dash(), space(),  dash(), space(),  dash(), space(),  dash(), ],
	"2": lambda: [ 	dot(), space(), dot(), space(), dash(), space(),  dash(), space(),  dash(), ],
	"3": lambda: [ 	dot(), space(), dot(), space(), dot(), space(), dash(), space(),  dash(), ],
	"4": lambda: [ 	dot(), space(), dot(), space(), dot(), space(), dot(), space(), dash(), ],
	"5": lambda: [ 	dot(), space(), dot(), space(), dot(), space(), dot(), space(), dot(), ],
	"6": lambda: [ 	dash(), space(),  dot(), space(), dot(), space(), dot(), space(), dot(), ],
	"7": lambda: [ 	dash(), space(),  dash(), space(),  dot(), space(), dot(), space(), dot(), ],
	"8": lambda: [ 	dash(), space(),  dash(), space(),  dash(), space(),  dot(), space(), dot(), ],
	"9": lambda: [ 	dash(), space(),  dash(), space(),  dash(), space(),  dash(), space(),  dot(), ],
	".": lambda: [  dot(), space(), dash(), space(),  dot(), space(), dash(), space(),  dot(), space(), dash(), ],
	",": lambda: [ 	dash(), space(),  dash(), space(),  dot(), space(), dot(), space(), dash(), space(),  dash(), ],
	":": lambda: [ 	dash(), space(),  dash(), space(),  dash(), space(),  dot(), space(), dot(), space(), dot(), ],
	"?": lambda: [ 	dot(), space(), dot(), space(), dash(), space(),  dash(), space(),  dot(), space(), dot(), ],
	"'": lambda: [ 	dot(), space(), dash(), space(),  dash(), space(),  dash(), space(),  dash(), space(),  dot(), ],
	"-": lambda: [ 	dash(), space(),  dot(), space(), dot(), space(), dot(), space(), dot(), space(), dash(), ],
	"\"": lambda: [ 	dot(), space(), dash(), space(),  dot(), space(), dot(), space(), dash(), space(),  dot(), ],
	"@": lambda: [ 	dot(), space(), dash(), space(),  dash(), space(),  dot(), space(), dash(), space(),  dot(), ],
	"=": lambda: [	dash(), space(),  dot(), space(), dot(), space(), dot(), space(), dash(), ]
}

def morse(to_send):
    for c in to_send:
        letters[c]()
        letter_space()
    return 

def read_input():
    to_read = raw_input("Text: ");
    return morse(list(to_read.upper()))

if __name__ == "__main__":
    read_input()
    print("Done")
