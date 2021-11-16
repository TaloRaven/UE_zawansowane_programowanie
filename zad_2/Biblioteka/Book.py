
class Book:
    def __init__(
            self,
            library,
            name: str,
            publication_date: str,
            author_name: str,
            author_surname: str,
            number_of_pages: int):
        self.libary = library
        self.name = name
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f'''
            {self.libary},
            Tytuł: {self.name},
            publikacja:  {self.publication_date},
            autor: {self.author_name} {self.author_surname},
            liczba stron {self.number_of_pages}
                '''