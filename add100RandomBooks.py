import requests
import json

APIHOST = "http://library.demo.local"
LOGIN = "cisco"
PASSWORD = "Cisco123!"

def getAuthToken():
    authCreds = (LOGIN, PASSWORD)
    r = requests.post(
        f"{APIHOST}/api/v1/loginViaBasic",
        auth = authCreds
    )
    if r.status_code == 200:
        return r.json()["token"]
    else:
        raise Exception(f"Status code {r.status_code} and text {r.text}, while trying to Auth.")

def deleteBook(book_id, apiKey):
    r = requests.delete(
        f"{APIHOST}/api/v1/books/{book_id}",
        headers = {
            "Content-type": "application/json",
            "X-API-Key": apiKey
            },
    )
    if r.status_code == 200:
        print(f"Book {book_id} deleted.")
    else:
        raise Exception(f"Error code {r.status_code} and text {r.text}, while trying to delete book {book_id}.")

def getAllBooks(apiKey):
    r = requests.get(
        f"{APIHOST}/api/v1/books",
        headers = {
            "Content-type": "application/json",
            "X-API-Key": apiKey
            },
    )
    if r.status_code == 200:
        return r.json()
    else:
        raise Exception(f"Error code {r.status_code} and text {r.text}, while trying to get all books.")

# Get the Auth Token Key
apiKey = getAuthToken()

# Get all books
books = getAllBooks(apiKey)

# Get the IDs of the first five and the last five books
book_ids_to_delete = [book['id'] for book in books[:5]] + [book['id'] for book in books[-5:]]

# Delete the selected books
for book_id in book_ids_to_delete:
    deleteBook(book_id, apiKey)