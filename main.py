from reader import Reader

def __main__(*args, **kwargs):
    reader = Reader('books/book/book.pdf')
    for page in range(reader.num_pages):
            print(reader.get(page))

if __name__ == '__main__':
		__main__()