import pytesseract as tess

tess.pytesseract.tesseract_cmd = r'C:\Users\Varun Shrivastava\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
import pyttsx3
import cv2

im = cv2.imread("Kaagaz.jpg")
text = tess.image_to_string(im)
f = open("scannedtext.txt", "w")
f.write(text)
f.close()

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 200)
f = open("scannedtext.txt", "r")
for line in f:
    for word in line.split():
        engine.say(str(word))
engine.runAndWait()

f.close()
