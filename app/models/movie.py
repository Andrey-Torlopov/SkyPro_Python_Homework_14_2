'''
Movie model which keep info in format:
{
    "title": "title",
    "country": "country",
    "release_year": 2021,
    "genre": "listed_in",
    "description": "description"
}
'''
from dataclasses import dataclass


@dataclass(slots=True, order=True)
class Movie(object):
    '''Movie class'''
    title: str
    country: str
    release_year: int
    genre: list[str]
    description: str
