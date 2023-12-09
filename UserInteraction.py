# class that manages user interactions
from resources import *


# Book user interactions

class BookUserInteraction:

    # gets book name from the user
    def __init__(self,  book_manager):
        self.isbn_list = book_manager.get_isbn_list()
        self.book_manager = book_manager

    def get_book_title(self):

        while True:

            user_input = input("Book Title: ")

            if not user_input == "":
                return user_input

                break
            else:
                print("Book must have a title")

    def get_book_description(self):

        while True:
            user_input = input("Book Description")

            if user_input == "":
                print("Book Must have a description!")
            else:
                return user_input
                break

    def get_book_isbn(self):

        while True:

            user_input = input("isbn")

            if user_input == "":
                print("Book Must Have ISBN!")
            elif not user_input.isdigit():
                print("ISBN must be a digit")
            elif not len(user_input) == 13:
                print("ISBN Must be 13 digit number!")

            elif user_input in self.isbn_list:
                print("ISBN exist!")
            else:
                return user_input

    def get_book_author(self):

        while True:

            user_input = input("Author: ")

            if not user_input == "":
                return user_input
            else:
                print("Book Must have an author")

    def create_book(self):

        book = Book(self.get_book_title(), self.get_book_description(), self.get_book_isbn(), self.get_book_author())
        self.book_manager.add_book(book)

    def user_find_book(self):

        found_books = []
        found_book = None

        while True:
            print("Find Book By.")
            print("1.ISBN")
            print("2.Title")

            user_input = input("Selection")
            if user_input == "1":
                isbn = input("ISBN")
                found = self.book_manager.find_book_by_isbn(isbn)
                break
            elif user_input == "2":
                user_title = input("book title")
                found = self.book_manager.find_books_by_title(user_title)
                break
            else:
                print("Invalid choice!")

        if found_book is None:
            print("Found no book by ISBN")

        else:
            print("Found: %s \n %s \n %s %s" % (
                found_book.get_title(), found_book.get_description(), found.get_isbn(), found_book.get_author()))

        if len(found_books) == 0:
            print("Found no book!")
        else:

            for bk in found_books:
                print("Found: %s \n %s \n %s %s" % (
                    bk.get_title(), bk.get_description(), bk.get_isbn(), bk.get_author()))

    def user_update_book(self):

        update_isbn = self.get_book_isbn()

        update = Book(self.get_book_title(), self.get_book_description(), update_isbn, self.get_book_author())
        self.book_manager.add_book(update)

        self.book_manager.update_book(update)
        print("Update successful")

    def user_delete_book(self):
        isbn = self.get_book_isbn()

        delete = Book(self.get_book_title(), self.get_book_description(), isbn, self.get_book_author())
        self.book_manager.add_book(delete)
        print("Delete successful")

    # methods present book activity
    def book_activity(self):

        while True:
            print("1. Add Book")
            print("2. Find Book")
            print("3. Update Book")
            print("4. Delete Book")
            print("5. Exit")

            user_input = input("Selection")
            if user_input == "1":
                self.create_book()
            elif user_input == "2":
                self.user_find_book()
            elif user_input == "3":
                self.user_update_book()
            elif user_input == "4":
                self.user_delete_book()
            elif user_input == "5":
                print("Exiting...")
                break
            else:
                print("Invalid selection!")


class MediaUserInterface:

    def __init__(self, media_manager):
        self.media_manager = media_manager
        self.media_id_list = media_manager.get_id_list()

    def get_media_id(self):

        while True:

            user_input = input("media Id")

            if not user_input.isdigit():
                print("Id must be a digit")
            elif user_input in self.media_id_list:
                print("id already exist")

            elif not len(user_input) == 7:
                print("it must 7 digit")
            else:
                return user_input

    def get_media_title(self):

        while True:

            user_input = input("Media Title: ")

            if user_input == "":
                print("MultiMedia must have a title")
            else:
                return user_input

    def get_media_description(self):

        while True:

            user_input = input("Media Description: ")

            if user_input == "":
                print("MultiMedia must have a decription")
            else:
                return user_input

    def get_media_type(self):
        while True:

            user_input = input("Media Type: ")

            if user_input == "":
                print("MultiMedia must have a type")
            elif not user_input.lower() == "video" or user_input.lower() == "audio":
                print("Must be either audio or video")


            else:
                return user_input

    def create_media(self):

        media = MultiMedia(self.get_media_id(), self.get_media_title(), self.get_media_description(),
                           self.get_media_type())
        self.media_manager.add_multimedia(media)
        print("Added succesfully")

    def find_media(self):
        media = []
        found_media = None

        while True:
            print("Find Media By.")
            print("1.Media Id")
            print("2.Title")

            user_input = input("Selection")
            if user_input == "1":
                media_id = input("Multimedia Id")
                found_media = self.media_manager.find_multimedia_by_Id(media_id)
                break
            elif user_input == "2":
                user_title = input("Media title")
                media = self.media_manager.find_media_by_title(user_title)
                break
            else:
                print("Invalid choice!")

        if found_media is None:
            print("Found no multimedia")

        else:
            print("Found: %s \n %s \n %s %s" % (found_media.get_id(),
                                                found_media.get_title(), found_media.get_media_description(),
                                                found_media.get_media_type()))

        if len(media) == 0:
            print("Found no book!")
        else:

            for m in media:
                print("Found: %s \n %s \n %s %s" % (m.get_id(),
                                                    m.get_title(), m.get_media_description(),
                                                    m.get_media_type()))

    def media_update(self):

        print("MultiMedia update")

        media_id = self.get_media_id()

        media = MultiMedia(media_id, self.get_media_title(), self.get_media_description(),
                           self.get_media_type())
        self.media_manager.media_update(media)
        print("updated successfully")

    #
    def delete_media(self):
        print("MultiMedia delete")

        delete_id = self.get_media_id()
        media = MultiMedia(delete_id, self.get_media_title(), self.get_media_description(),
                           self.get_media_type())
        self.media_manager.delete_multimedia(media)

        print("Deleted successfully ")

    # methods handles multimedia activity
    def multimedia_activity(self):

        while True:
            print("1. Add Multimedia")
            print("2. Search Multimedia")
            print("3. Update Multimedia")
            print("4. Delete Multimedia")
            print("5. Exit")

            user_input = input("Selection> ")

            if user_input == "1":
                self.create_media()
            elif user_input == "2":
                self.find_media()
            elif user_input == "3":
                self.media_update()
            elif user_input == "4":
                self.delete_media()
            elif user_input == "5":
                break
            else:
                print("Invalid selection!")


