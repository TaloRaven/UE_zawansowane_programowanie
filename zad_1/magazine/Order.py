import magazine.utils

class Order:
    def __init__(self, employee: str,
                 student: str, books: list, order_date: str):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date
        self.list_to_srt = ' '.join([str(elem) for elem in books])

    def __str__(self):
        return f'''
            ===============================================
            ===============================================
            DATA:
            {self.order_date}
            {self.employee}
            OSOBA WYPOŻYCZAJĄCA:
            {self.student}
            ZAWARTOŚĆ ZAMÓWIENIA:
            {self.list_to_srt}
            ===============================================
            ===============================================
                '''
