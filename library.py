import json
import os
from book import Book


class Library:
    def __init__(self, path):
        self.PATH_TO_JSON = path
        if not os.path.exists(path):
            with open(path, "a") as library_file:
                library_file.write("{}")

    def add_book_to_json(self, library_obj, book: Book):
        """Метод вносит книгу в библиотеку."""

    def delete_book_json(self, library_obj, book_id: int):
        """Метод удаляет книгу из библиотеки по id."""

    def find_books_in_json(self, library_obj, **kwargs) -> list[Book]:
        """
        Метод возвращает список книг. Поиск осуществляется
        по одному из параметров: title, author или year.
        """
        result_list = []
        for key, value in library_obj:
            if value[kwargs["parameter"]] == kwargs["value"]:
                result_list.append(key, value)
        return {"command": "find", "result_value": result_list}

    def get_book_list(self, library_obj) -> list[Book]:
        """Метод возвращает список книг."""

    def change_book_status(self, library_obj, **kwargs) -> None:
        """
        Метод для изменения статуса книги. в качестве аргументов
        должны быть переданы id книги ("id") и требуемый статус("status").
        """

    def json_handle(self, action: str, parameters: dict | None = None):
        action_dict = {
            "add": self.add_book_to_json,
            "delete": self.delete_book_json,
            "find": self.find_books_in_json,
            "list": self.get_book_list,
            "change_status": self.change_book_status,
        }
        with open(self.PATH_TO_JSON) as base_file:
            library_obj = json.load(base_file)
            result = action_dict[action](library_obj, kwargs=parameters)
            base_file = json.dump(library_obj)
            return result


if __name__ == "__main__":
    ...
