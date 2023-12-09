# resources module

# general resource

class Book:
    # variable intialization
    def __init__(self, title, description, isbn, author):
        self.book_title = title
        self.book_description = description
        self.isbn = isbn
        self.author = author

    # get specific book attribute
    def get_title(self):
        return self.book_title

    def get_description(self):
        return self.book_description

    def get_isbn(self):
        return self.isbn

    def get_author(self):
        return self.author

    # returns a list of isbns


# specialized resource
class MultiMedia:

    def __init__(self, media_id, title, description, media_type):
        self.media_id = media_id
        self.title = title
        self.description = description
        self.media_type = media_type

    def get_id(self):
        return self.media_id

    def get_title(self):
        return self.description

    def get_media_type(self):
        return self.media_type

    def get_media_description(self):
        return self.description
