from reader import Reader

PATH = 'books/gpt3/gpt3.pdf'

def __main__(*args, **kwargs):
    reader = Reader(PATH)
    for page in range(10, 20):
            print(reader.get())

if __name__ == '__main__':
		__main__()