import PyPDF2
import gtts
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract


f= open('i0.pdf','rb')

c=PyPDF2.PdfFileReader(f)

print(c)
m=[]
#for i in range(0,c.numPages):
for i in range(10,197):
    print(i)
    mu=' '.join((c.getPage(i).extractText()).split('\n'))
    m.append(mu+'\n')

g=open('0010.txt','w')
g.writelines(m)
tts=gtts.gTTS(mu, lang='es-us')
tts.save("Bunea.mp3")




    
