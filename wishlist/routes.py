from flask import render_template, request, redirect, url_for
from wishlist import app, db
from wishlist.models import Category, Item


@app.route("/")
def home():
    return render_template("base.html")


@app.route("/categories")
def categories():
    categories = list(Category.query.order_by(Category.name).all())
    return render_template("categories.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = Category(name=request.form.get("name"))
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("add_category.html")
