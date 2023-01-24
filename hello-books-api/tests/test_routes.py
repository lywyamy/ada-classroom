import pytest
from werkzeug.exceptions import HTTPException
from app.routes import validate_model
from app.models.book import Book


def test_get_all_books_with_no_records(client):
    response = client.get("/books")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == []


def test_get_one_book(client, two_saved_books):
    response = client.get("/books/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "title": "Ocean Book",
        "description": "watr 4evr"
    }


def test_create_one_book(client):
    response = client.post("/books", json={
        "title": "New Book",
        "description": "The Best!"
    })
    response_body = response.get_json()

    assert response.status_code == 201
    assert response_body == "Book New Book successfully created"


def test_get_all_books_with_two_records(client, two_saved_books):
    response = client.get("/books")
    response_body = response.get_json()

    assert response.status_code == 200
    assert len(response_body) == 2
    assert response_body[0] == {
        "id": 1,
        "title": "Ocean Book",
        "description": "watr 4evr"
    }
    assert response_body[1] == {
        "id": 2,
        "title": "Mountain Book",
        "description": "i luv 2 climb rocks"
    }


def test_get_all_books_with_title_query_matching_none(client, two_saved_books):
    data = {'title': 'Desert Book'}
    response = client.get("/books", query_string = data)
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == []


def test_get_all_books_with_title_query_matching_one(client, two_saved_books):
    data = {'title': 'Ocean Book'}
    response = client.get("/books", query_string = data)
    response_body = response.get_json()

    assert response.status_code == 200
    assert len(response_body) == 1
    assert response_body[0] == {
        "id": 1,
        "title": "Ocean Book",
        "description": "watr 4evr"
    }


def test_get_one_book_id_not_found(client, two_saved_books):
    response = client.get("/books/3")
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == {"message": "Book 3 not found"}


def test_get_one_book_id_invalid(client, two_saved_books):
    response = client.get("/books/cat")
    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body == {"message": "Book cat invalid"}


def test_create_one_book_no_title(client):
    test_data = {"description": "The Best!"}

    with pytest.raises(KeyError):
        response = client.post("/books", json=test_data)

def test_create_one_book_no_description(client):
    test_data = {"title": "New Book"}

    with pytest.raises(KeyError):
        response = client.post("/books", json=test_data)

def test_create_one_book_with_extra_keys(client, two_saved_books):
    test_data = {
        "extra": "some stuff",
        "title": "New Book",
        "description": "The Best!",
        "another": "last value"
    }

    response = client.post("/books", json=test_data)
    response_body = response.get_json()

    assert response.status_code == 201
    assert response_body == "Book New Book successfully created"


def test_update_book(client, two_saved_books):
    test_data = {
        "title": "New Book",
        "description": "The Best!"
    }

    response = client.put("/books/1", json=test_data)
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == "Book #1 successfully updated"


def test_update_book_with_extra_keys(client, two_saved_books):
    test_data = {
        "extra": "some stuff",
        "title": "New Book",
        "description": "The Best!",
        "another": "last value"
    }

    response = client.put("/books/1", json=test_data)
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == "Book #1 successfully updated"


def test_update_book_missing_record(client, two_saved_books):
    test_data = {
        "title": "New Book",
        "description": "The Best!"
    }

    response = client.put("/books/3", json=test_data)
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == {"message": "Book 3 not found"}


def test_update_book_invalid_id(client, two_saved_books):
    test_data = {
        "title": "New Book",
        "description": "The Best!"
    }

    response = client.put("/books/cat", json=test_data)
    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body == {"message": "Book cat invalid"}


def test_delete_book(client, two_saved_books):
    response = client.delete("/books/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == "Book #1 successfully deleted"


def test_delete_book_missing_record(client, two_saved_books):
    response = client.delete("/books/3")
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == {"message": "Book 3 not found"}


def test_delete_book_invalid_id(client, two_saved_books):
    response = client.delete("/books/cat")
    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body == {"message": "Book cat invalid"}


def test_validate_book(two_saved_books):
    result_book = validate_model(Book, 1)

    assert result_book.id == 1
    assert result_book.title == "Ocean Book"
    assert result_book.description == "watr 4evr"


def test_validate_book_missing_record(two_saved_books):
    with pytest.raises(HTTPException):
        result_book = validate_model(Book, "3")

    
def test_validate_book_invalid_id(two_saved_books):
    with pytest.raises(HTTPException):
        result_book = validate_model(Book, "cat")