from resources import Book, MultiMedia


# classes that handles data persistence

class BookPersistence:

    def __init__(self):
        self.file_name = "books.csv"

    # reads file content and returns a dictionary of the content
    def read_csv(self):

        books_dictionary = {}

        try:

            file = open(self.file_name, "r")

            line = file.readline()
            while not line == "":
                values_list = line.split(",")
                print(values_list)
                book = Book(values_list[0], values_list[1], values_list[2], values_list[3].replace("\n",""))

                books_dictionary[values_list[0]] = book
                print(book.book_description)
                line = file.readline()

            file.close()
            print(books_dictionary)
            return books_dictionary

        except IOError:
            print("Unable to retrieve data")

    # reads updated data to a CSV
    def write_csv(self, books_dictionary):

        try:
            file = open(self.file_name, "w")

            for title, book in books_dictionary.items():
                file.write(
                    "%s,%s,%s,%s" % (book.get_title(), book.get_description(), book.get_isbn(), book.get_author()))
                file.write("\n")
            file.close()
            print("Saved books data successfully")

        except IOError:
            print("Failed to write live update")


# class that reads  and persist multimedia  data
class MultimediaPersistence:

    def __init__(self):
        self.file_name = "multimedia.csv "

    # reads a csv file and returns data representing the data
    def read_csv(self):

        multimedia_dictionary = {}

        try:

            file = open(self.file_name, "r")

            line = file.readline()

            while not line == "":
                values = line.split(",")
                if len(values) == 1:
                    break
                print(values)
                multimedia = MultiMedia(values[0], values[1], values[2], values[3].replace("\n", ""))
                multimedia_dictionary[values[0]] = multimedia
                line = file.readline()

            file.close()
            return multimedia_dictionary

        except IOError:
            print("Unable to read multimedia file")

    # writes live data to the csv
    def write_csv(self, multimedia_dictionary):

        try:

            file = open(self.file_name, "w")

            for title, media in multimedia_dictionary.items():
                file.write("%s,%s,%s,%s" % (
                    media.get_id(), media.get_title(), media.get_media_description(), media.get_media_type()))
                file.write("\n")

            file.close()
            print("Saved multimedia content")

        except IOError:
            print("Unable to write multimedia update")
