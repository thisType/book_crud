from UserInteraction import BookUserInteraction, MediaUserInterface
from datapersistence import BookPersistence, MultimediaPersistence
from resource_management import BookManager, MultiMediaManager


def main():
    print("Welcome:")

    booksPersistence = BookPersistence()
    multimediaPersistence = MultimediaPersistence()

    book_data = booksPersistence.read_csv()
    media_data = multimediaPersistence.read_csv()

    booksManager = BookManager(book_data)
    mediaManager = MultiMediaManager(media_data)

    bookActivity = BookUserInteraction(booksManager)
    mediaActivity = MediaUserInterface(mediaManager)

    while True:

        print("1. Books")
        print("2. Multimedia")
        print("3. exit")

        user_input = input("Selection>")

        if user_input == "1":

            bookActivity.book_activity()
        elif user_input == "2":
            mediaActivity.multimedia_activity()

        elif user_input == "3":

            # saving data
            booksPersistence.write_csv(booksManager.get_update())
            multimediaPersistence.write_csv(mediaManager.get_update())
            break
        else:
            print("Invalid choice")

main()
