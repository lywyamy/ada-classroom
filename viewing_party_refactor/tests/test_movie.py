import pytest
from viewing_party.movie import Movie

def test_movie_constructor():
    # Arrange
    title = "Dune"
    genre = "scientific fiction"
    rating = 10
    host = "HBO"

    # Act
    tasha_movie = Movie(title, genre, rating, host)

    # Assert
    assert tasha_movie.title == "Dune"
    assert tasha_movie.genre == "scientific fiction"
    assert tasha_movie.rating == 10
    assert tasha_movie.host == "HBO"