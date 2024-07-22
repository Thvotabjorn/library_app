from library import Library
from book import Book


class ComandLineHandler:
    COMMAND_LIST = [
        "add",
        "delete",
        "find",
        "list",
        "change_status",
        "exit"
    ]
    MESSAGES = {
        "begin": "Введите команду. При необходимости введите help для вывода списка команд",
        "add_name": "Введите название книги",
        "add_author": "Введите автора книги",
        "add_year": "Введите год издания книги",
        "add_status": "Введите год издания книги",
        "add_success": "Книга была внесена",
        "delete": "Введите id книги",
        "delete_success": "Книга была удалена",
        "find_parameter": "Укажите параметр поиска: title, author или year",
        "find_value": "Введите значение парамтра для поиска",
        "status_id": "Укажите ID книги, статус которой необходимо изменить",
        "status_text": "Укажите новый статус: 'в наличии' или 'выдана').",
        "status_success": "Укажите новый статус: 'в наличии' или 'выдана').",
        "incorrect_command": "Некоректная команда. Для вывода списка команд введите команду help",
        "try_again": "Попробовать ещё раз? Если да, введите 'y'",
        "default_error": "Возникла ошибка, попробуйте снова"
    }
    PATH_TO_BASE = "base.json"

    def __init__(self):
        self.current_step = "begin"
        self.library = Library(self.PATH_TO_BASE)

    def main_loop(self):
        print(self.MESSAGES["begin"])
        while True:
            command = input()
            if not self.validate_command(command):
                print(self.MESSAGES["incorrect_command"])
                continue
            if command == "exit":
                break
            self.handle_command(command)

    def handle_command(self, command):
        try_again = 1
        while try_again:
            if try_again == "again":
                answer = input(self.MESSAGES["try_again"])
                if answer != "yes":
                    break
            try_again = None
            action_dict = {
                "add": self.handle_add,
                "delete": self.handle_delete,
                "find": self.handle_find,
                "list": self.handle_get_list,
                "change_status": self.handle_change_status,
            }
            try:
                result = action_dict[command]()
                print(result)
            except ValueError as e:
                print(f"{e}")
                try_again = "again"

    def handle_add(self) -> str:
        title: str = input(self.MESSAGES["add_name"])
        author: str = input(self.MESSAGES["add_author"])
        year: str = input(self.MESSAGES["add_year"])
        status: str = input(self.MESSAGES["add_status"])
        book: Book = Book(
            title=title,
            author=author,
            year=year,
            status=status
        )
        try:
            book.validate_data()
            self.library.add_book_to_json()
            return self.MESSAGES["add_success"]
        except ValueError as vr:
            return f"{vr}"
        except Exception:
            raise Exception(self.MESSAGES["default_error"])

    def handle_find(self):
        parameter: str = input(self.MESSAGES["find_parameter"])
        if parameter not in ("author", "title", "year"):
            raise ValueError("Недопустимый парамтр для поиска книги")
        value: str = input(self.MESSAGES["find_value"])
        try:
            result = self.library.find_books_in_json(parameter, value)
            return result
        except Exception:
            raise Exception(self.MESSAGES["default_error"])

    def handle_get_list(self) -> str:
        try:
            result = self.library.get_book_list()
            str_result = self.pretty_list_output(result)
            return str_result
        except Exception:
            raise Exception(self.MESSAGES["default_error"])

    def handle_delete(self) -> str:
        book_id: int = input(self.MESSAGES["delete"])
        try:
            self.library.delete_book_json(book_id)
            return self.MESSAGES["delete_success"]
        except Exception:
            raise Exception(self.MESSAGES["default_error"])

    def handle_change_status(self) -> str:
        book_id: str = input(self.MESSAGES["status_id"])
        book_status: str = input(self.MESSAGES["status_status"])
        try:
            self.library.change_book_status(book_id, book_status)
            return self.MESSAGES["status_success"]
        except Exception:
            raise Exception(self.MESSAGES["default_error"])

    def validate_command(self, command) -> bool:
        if command in self.COMMAND_LIST:
            return True
        return False

    def pretty_list_output(list_of_books) -> str:
        ...

if __name__ == "__main__":
    handler = ComandLineHandler()
    print(handler.validate_command("add"))
