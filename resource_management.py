# resource management services


# class that manages book live data

class BookManager:

    # variable initialization
    def __int__(self, books):
        # holds book state
        self.books_dictionary = books

    # adds a book
    def add_book(self, book):
        self.books_dictionary[book.get_title()] = book

    # finds a book by ISBN
    def find_book_by_isbn(self, isbn):

        book_found = None

        for name, book in self.books_dictionary:

            if book.get_isbn() == isbn:
                book_found = book
                break

        return book_found

    def find_books_by_title(self, title):
        found_book = []

        for name, book in self.books_dictionary:
            # to lower case for case-insensivity
            if not book.get_title().lower(0).indexOf(title.lower()) == -1:
                found_book.append(book)
                break

        return found_book

    # updates a book by isbn
    def update_book(self, book):
        self.books_dictionary[book.book_title] = book

    # deletes a book
    def delete_book(self, book):
        del self.books_dictionary[book.get_title()]

    # returns live update to be written in a file
    def get_update(self):
        return self.books_dictionary

    def get_isbn_list(self):

        isbn_list = []

        for name, book in self.books_dictionary:
            isbn_list.append(book.isbn)

        return  isbn_list


# class that manages media resource
class MultiMediaManager:

    def __int__(self, multi_media):
        # holds data from a resource file
        self.media_dictionary = multi_media

    # adds a new multimedia
    def add_multimedia(self, multi_media):

        self.media_dictionary[multi_media.get] = multi_media

    # gets multimedia by id
    def find_multimedia_by_Id(self, id):

        multi_media_found = None

        for title, multi_media in self.media_dictionary:

            if id == multi_media.get_id():
                multi_media_found = multi_media
                break

        return multi_media_found

    def multi_media_update(self, multi_media):

        self.media_dictionary[multi_media.getTitle] = multi_media

    def find_media_by_title(self, title):

        multi_media_list = []

        for name, multi_media in self.media_dictionary:
            # case-insensitivity
            if not name.lower().indexOf(title.lower()) == -1:
                multi_media_list.append(multi_media)

        return multi_media_list

    # delete multimedia
    def delete_multi_media(self, multi_media):
        del self.media_dictionary[multi_media.getTitle()]

    # returns an updated multi_media state
    def get_update(self):
        return self.media_dictionary

    # returns a list of multimedia id
    def get_id_list(self):
        id_list = []

        for  title, media in self.media_dictionary:
            id_list.append(media.media_id)

        return id_list

