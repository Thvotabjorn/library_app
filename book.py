

class Book:
    def __init__(
            self,
            title: str,
            year: int,
            author: str,
            status: str,
            id=None):
        self.title = title
        self.year = year
        self.author = author
        self.status = status
        self.id = id

    def generate_json_view(self):
        ...
