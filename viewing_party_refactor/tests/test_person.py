import pytest
from viewing_party.person import Person
from viewing_party.movie import Movie

def test_person_constructor():
    # Arrange
    name = "Tasha"
    watched = []
    friends = []
    subscriptions = ["HBO"]

    # Act
    tasha = Person(name, watched, friends, subscriptions)

    # Assert
    assert tasha.name == "Tasha"
    assert len(tasha.watched) == 0
    assert len(tasha.friends) == 0
    assert len(tasha.subscriptions) == 1
    assert tasha.subscriptions[0] == "HBO"

def test_add_watched_method():
    # Arrange
    name = "Tasha"
    watched = []
    friends = []
    subscriptions = ["HBO"]

    title = "Dune"
    genre = "scientific fiction"
    rating = 10
    host = "HBO"

    # Act
    tasha_movie = Movie(title, genre, rating, host)
    tasha = Person(name, watched, friends, subscriptions)
    tasha.add_watched(tasha_movie)

    # Assert
    assert len(tasha.watched) == 1
    assert tasha.watched[0].title == "Dune"
    