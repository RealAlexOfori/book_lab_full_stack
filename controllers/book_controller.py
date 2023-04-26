from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.book import Book
from models.books_list import books
import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

books_blueprint = Blueprint("books", __name__)

@books_blueprint.route("/books")
def books():
    books = book_repository.select_all() # NEW
    return render_template("books/index.html", all_books = books)