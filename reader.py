from googletrans import Translator
from PyPDF2 import PdfReader
from gtts import gTTS

class Reader:
		def __init__(self, pdf_file,init_page=0):
				self.titulo = pdf_file
				self.pdf = open(pdf_file, 'rb')
				self.pdf_reader = PdfReader(self.pdf)
				self.num_pages = len(self.pdf_reader.pages)
				self.actual_page = init_page

		def textFromPage(self,	page):
				return self.pdf_reader.pages[page].extract_text()
    
		def format(self, text):
				return text.replace('\n', ' ').replace('\t', ' ').replace('\xa0', ' ')
		
		def translete(self,text):
				return Translator().translate(text,src= "en",dest= "es").text
		
		def gen_audio(self, text):
				speak = gTTS(text=text, lang="es", slow= False)
				speak.save(self.titulo.split('.')[0] + "_" + str(self.actual_page) + '.mp3')
		
		def gen_text(self,text):
				file = open(self.titulo.split('.')[0] + "_" + str(self.actual_page) + '.txt', 'w')
				file.write(text)
				file.close()

		def next(self, gen_audio=True,	translete=True):
				text_response = self.format(self.textFromPage(self.actual_page))
				self.actual_page += 1
				if translete:
					text_response = self.translete(text_response)
				if gen_audio:
					self.gen_audio(text_response)
				return text_response

		def get(self,	page,	gen_audio=True,	translete=True):
				text_response = self.format(self.textFromPage(page))
				if translete:
					text_response = self.translete(text_response)
				if gen_audio:
					self.gen_audio(text_response)
				return text_response
