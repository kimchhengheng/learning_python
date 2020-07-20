import pyttsx3
import PyPDF2

book=open('crush.pdf', 'rb')
# we can use tkinter asktoopenfile to get the book , this would allow use to select any book we want
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
# print(pages)
speaker = pyttsx3.init()
speaker.setProperty("rate", 250)
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[1].id)
output=[]
for var in range(0, pages):
    page = pdfReader.getPage(var)
    text = page.extractText()
    # speaker.say(text)
    output.append(text)
# pdftotext.PDF is more easy to convert pdf to text

book2=open('Student_Record.pdf', 'rb')
finalpdf=PyPDF2.PdfFileMerger()
finalpdf.append(book)
finalpdf.append(book2)
finalpdf.write("merge.pdf")

# speaker.save_to_file(output, 'crush.mp3')
# speaker.runAndWait()
#
# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# print(voices[0])
# print(voices[1])
# for voice in voices:
#    engine.setProperty('voice', voice.id)
#
#    engine.say('The quick brown fox jumped over the lazy dog.')
# engine.runAndWait()
