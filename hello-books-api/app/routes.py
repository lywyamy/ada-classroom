from flask import Blueprint, jsonify, abort, make_response, request
from app import db
from app.models.book import Book
from app.models.author import Author
from app.models.genre import Genre

books_bp = Blueprint("books", __name__, url_prefix="/books")
authors_bp = Blueprint("authors", __name__, url_prefix="/authors")
genres_bp = Blueprint("genres", __name__, url_prefix="/genres")

#******************** Books ********************#

@books_bp.route("", methods=["POST"])
def add_one_book():
    request_body = request.get_json()
    
    try:
        new_book = Book.from_dict(request_body)

    except:
        raise KeyError()

    db.session.add(new_book)
    db.session.commit()

    return jsonify(f"Book {new_book.title} successfully created"), 201

@books_bp.route("", methods=["GET"])
def get_all_books():
    requested_title = request.args.get("title")
    if requested_title is not None:
        books = Book.query.filter_by(title=requested_title)
    else:
        books = Book.query.all()

    response = []
    for book in books:
        response.append(book.to_dict())
    
    return jsonify(response), 200

@books_bp.route("/<book_id>", methods=["GET"])
def get_one_book(book_id):
    book = validate_model(Book, book_id)
    
    return jsonify(book.to_dict()), 200

@books_bp.route("/<book_id>", methods=["PUT"])
def update_one_book(book_id):
    book = validate_model(Book, book_id)

    request_body = request.get_json()
    try:
        book.title = request_body["title"]
        book.description = request_body["description"]
    except:
        abort(make_response("Some information is missing from your input."))
    
    db.session.commit()
    
    return make_response(jsonify(f"Book #{book.id} successfully updated"), 200)

@books_bp.route("/<book_id>", methods=["DELETE"])
def delete_one_book(book_id):
    book = validate_model(Book, book_id)

    db.session.delete(book)
    db.session.commit()

    return make_response(jsonify(f"Book #{book.id} successfully deleted"), 200)

#******************** Authors ********************#

@authors_bp.route("", methods=["POST"])
def add_one_author():
    request_body = request.get_json()
    
    try:
        new_author = Author.from_dict(request_body)

    except:
        raise KeyError()

    db.session.add(new_author)
    db.session.commit()

    return jsonify(f"Author {new_author.name} successfully created"), 201


@authors_bp.route("/<author_id>/books", methods=["POST"])
def add_book_for_author(author_id):
    author = validate_model(Author, author_id)

    request_body = request.get_json()
    new_book = Book(
        title=request_body["title"],
        description=request_body["description"],
        author=author
    )

    db.session.add(new_book)
    db.session.commit()

    return jsonify(f"Book {new_book.title} by {new_book.author.name} successfully created"), 201


@authors_bp.route("", methods=["GET"])
def get_all_authors():
    authors = Author.query.all()

    response = []
    for author in authors:
        response.append(author.to_dict())
    
    return jsonify(response), 200


@authors_bp.route("/<author_id>/books", methods=["GET"])
def get_books_of_one_author(author_id):
    author = validate_model(Author, author_id)

    response_body = []
    for book in author.books:
        response_body.append(
            book.to_dict()
        )

    return jsonify(response_body), 200

#******************** Authors ********************#

@genres_bp.route("", methods=["POST"])
def create_genre():
    request_body = request.get_json()
    new_genre = Genre(name=request_body["name"],)

    db.session.add(new_genre)
    db.session.commit()

    return make_response(jsonify(f"Genre {new_genre.name} successfully created"), 201)


@genres_bp.route("", methods=["GET"])
def read_all_genres():
    
    genres = Genre.query.all()

    genres_response = []
    for genre in genres:
        genres_response.append(
            {
                "name": genre.name
            }
        )
    return jsonify(genres_response)


@genres_bp.route("/<genre_id>/books", methods=["POST"])
def create_book(genre_id):

    genre = validate_model(Genre, genre_id)

    request_body = request.get_json()
    new_book = Book(
        title=request_body["title"],
        description=request_body["description"],
        author_id=request_body["author_id"],
        genres=[genre]
    )

    db.session.add(new_book)
    db.session.commit()
    return make_response(jsonify(f"Book {new_book.title} by {new_book.author.name} successfully created"), 201)


@genres_bp.route("/<genre_id>/books", methods=["GET"])
def read_all_books(genre_id):
    genre = validate_model(Genre, genre_id)

    books_response = []
    for book in genre.books:
        books_response.append(
            book.to_dict()
        )
    return jsonify(books_response)

#******************** Helper Functions ********************#

def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        abort(make_response({"message":f"{cls.__name__} {model_id} invalid"}, 400))
    
    model = cls.query.get(model_id)

    if not model:
        abort(make_response({"message":f"{cls.__name__} {model_id} not found"}, 404))

    return model

# class Book:
#     def __init__(self, id, title, description):
#         self.id = id
#         self.title = title
#         self.description = description

# books = [
#     Book(1, "The Three-body Problem", "sci-fi"),
#     Book(2, "Insivible Women", "social justice"),
#     Book(3, "Algorithms", "education - computer science")
# ]

# @books_bp.route("", methods=["GET"])
# def handle_books():
#     books_response = []
#     for book in books:
#         books_response.append(
#             {
#                 "id": book.id,
#                 "title": book.title,
#                 "description": book.description
#             }
#         )
#     return jsonify(books_response)

# @books_bp.route("/<book_id>", methods=["GET"])
# def handle_book(book_id):
#     book = validate_book(book_id)

#     return {
#         "id": book.id,
#         "title": book.title,
#         "description": book.description,
#     }

# def validate_book(book_id):
#     try:
#         book_id = int(book_id)
#     except:
#         abort(make_response({"message":f"book {book_id} invalid"}, 400))

#     for book in books:
#         if book.id == book_id:
#             return book

#     abort(make_response({"message":f"book {book_id} not found"}, 404))

# Alternative to implement books_bp.route("/<book_id>", methods=["GET"]) w/o helper function
# @books_bp.route("/<book_id>", methods=["GET"])
# def handle_book(book_id):
#     try:
#         book_id = int(book_id)
#     except:
#         abort(make_response({"message": "Book_id has to be an integer."}, 400))
    
#     for book in books:
#         if book.id == book_id:
#             book_dict = {
#                 "id": book.id,
#                 "title": book.title,
#                 "description": book.description
#             }

#             return jsonify(book_dict), 200
    
#     abort(make_response("Couldn't find the book with {}.".format(book_id), 404))

#******************** hello_world ********************#
# hello_world_bp = Blueprint("hello_world", __name__)

# @hello_world_bp.route("/hello-world", methods=["GET"])
# def say_hello_world():
#     my_beautiful_response_body = "Hello, World!"
#     return my_beautiful_response_body

# @hello_world_bp.route("/hello/JSON", methods=["GET"])
# def say_hello_json():
#     return {
#         "name": "Yangweiyi Li",
#         "message": "PSG.LGD",
#         "hobbies": ["kayaking", "painting", "working out"]
#     }

# @hello_world_bp.route("/broken-endpoint-with-broken-server-code")
# def broken_endpoint():
#     response_body = {
#         "name": "Ada Lovelace",
#         "message": "Hello!",
#         "hobbies": ["Fishing", "Swimming", "Watching Reality Shows"]
#     }
#     new_hobby = "Surfing"
#     response_body["hobbies"].append(new_hobby)
#     return response_body