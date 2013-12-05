import pifacecad

character = [0b10000,0b00000,0b00000,0b00000,0b00000,0b00000,0b00000,0b00000]
bitmasks = [0b10000,0b01000,0b00100,0b00010,0b00001,0b11111]

bitmap = pifacecad.LCDBitmap(character)

cad = pifacecad.PiFaceCAD()
cad.lcd.backlight_on()
cad.lcd.blink_off()
cad.lcd.cursor_off()

cad.lcd.store_custom_bitmap(0,bitmap)
cad.lcd.write_custom_bitmap(0)


posX = 0
posY = 0

# def refresh():
	# cad.lcd.store_custom_bitmap(0,bitmap)

def reset(event):
	global posX, posY
	posX = 0 
	posY = 0
	for i, x in enumerate(character):
		character[i] = 0b00000
	update()



def update():
	global posX, posY
	character[posY] = character[posY]^bitmasks[posX]
	bitmap = pifacecad.LCDBitmap(character)
	cad.lcd.store_custom_bitmap(0,bitmap)

def invert(event):
	for i, x in enumerate(character):
		character[i] = character[i]^bitmasks[5]
	bitmap = pifacecad.LCDBitmap(character)
	cad.lcd.store_custom_bitmap(0,bitmap)


def left(event):
	global posX
	update()
	posX = (posX-1)%5
	update()

def right(event):
	global posX
	update()
	posX = (posX+1)%5
	update()

def up(event):
	global posY
	update()
	posY = (posY-1)%8
	update()

def down(event):
	global posY
	update()
	posY = (posY+1)%8
	update()

def enter(event):
	update()

def printCharacter(event):
	update()
	for line in character:
		print(bin(line))
	update()

listener = pifacecad.SwitchEventListener(cad)
listener.register(0, pifacecad.IODIR_FALLING_EDGE, left)
listener.register(1, pifacecad.IODIR_FALLING_EDGE, down)
listener.register(4, pifacecad.IODIR_FALLING_EDGE, enter)
listener.register(2, pifacecad.IODIR_FALLING_EDGE, up)
listener.register(3, pifacecad.IODIR_FALLING_EDGE, right)
listener.register(5, pifacecad.IODIR_FALLING_EDGE, printCharacter)
listener.register(6, pifacecad.IODIR_FALLING_EDGE, invert)
listener.register(7, pifacecad.IODIR_FALLING_EDGE, reset)
listener.activate()





