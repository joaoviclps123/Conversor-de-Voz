import pyttsx3
import PyPDF2 as pdf 
 
livro = open('livro.pdf', 'rb')
leitor_pdf = pdf.PdfFileReader(livro)
 
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 120)
 
for voice in voices:
	engine.setProperty('voice', voice.id)
 
paginas = leitor_pdf.numPages
 
for numero_pagina in range(0, paginas):
	page = leitor_pdf.getPage(numero_pagina)
	texto_para_audio = page.extractText()
	engine.say(texto_para_audio)
	engine.runAndWait()