
class NameAlreadyExists(Exception):

    def __init__(self, message = "Category Name Already Exists"):
        super().__init__(message)


class InvalidCategoryName(Exception):

    def __init__(self, message = "Invalid Category Name"):
        super().__init__(message)