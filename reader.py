import googletrans
from gtts import gTTS
import PyPDF2

class Reader:
		def __init__(self, pdf_file,init_page=0):
				self.titulo = pdf_file
				self.pdf = open(pdf_file, 'rb')
				self.pdf_reader = PyPDF2.PdfReader(self.pdf)
				self.num_pages = len(self.pdf_reader.pages)
				self.actual_page = init_page

		def textFromActualPage(self):
				text = self.pdf_reader.pages[self.actual_page].extract_text()
				self.actual_page += 1
				return text
    
		def format(self, text):
				return self.translete(text.replace('\n', ' ').replace('\t', ' ').replace('\xa0', ' '))
		
		def translete(self,text):
				return googletrans.Translator().translate(text,src= "en",dest= "es").text
		
		def gen_audio(self, text):
				speak = gTTS(text=text, lang="es", slow= False)
				speak.save(self.titulo.split('.')[0] + "_" + str(self.actual_page) + '.mp3')
		
		def gen_text(self,text):
				file = open(self.titulo.split('.')[0] + "_" + str(self.actual_page) + '.txt', 'w')
				file.write(text)
				file.close()

		def get(self):
				text_response = self.format(self.textFromActualPage())
				self.gen_audio(text_response)
				return text_response
