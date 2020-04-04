#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
import sys
from PIL import Image
print(sys.version)
from pdf2image import convert_from_path
import pytesseract
import os

#file path for doc to be converted
destination = 'CAOS/week5/week2/'
Pdf_file_path = destination+'12.1_to_12.9_pages 211-221.pdf' #your file path

Images = convert_from_path(Pdf_file_path, dpi=500)

Counter=1
for page in Images:
       idx= destination+"image_"+str(Counter)+".jpg" ##or ".png"
       page.save(idx, 'JPEG')
       Counter = Counter+1

file=Counter-1
output= destination+'text.txt' #where you want to save and file name
f=open(output, "w")
for i in range(1,file+1):
    idx= destination+"image_"+str(i)+".jpg" ##or ".png"
    text=str(pytesseract.image_to_string(Image.open(idx))).encode('ascii', 'ignore').decode('ascii')
    f.write(text)
    os.remove(idx)
f.close()
