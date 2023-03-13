from flask import render_template, request, redirect, url_for
from wishlist import app, db
from wishlist.models import Category, Item
from datetime import date


@app.route("/")
def home():
    items = list(Item.query.order_by(Item.item_name).all())
    return render_template("items.html", items=items)


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


@app.route("/edit_category/<int:id>", methods=["GET", "POST"])
def edit_category(id):
    category = Category.query.get_or_404(id)
    if request.method == "POST":
        category.name = request.form.get("name")
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("edit_category.html", category=category)


@app.route("/delete_category/<int:id>")
def delete_category(id):
    category = Category.query.get_or_404(id)
    db.session.delete(category)
    db.session.commit()
    return redirect(url_for("categories"))


@app.route("/add_item", methods=["GET", "POST"])
def add_item():
    categories = list(Category.query.order_by(Category.name).all())
    if request.method == "POST":
        item = Item(
            category_id=request.form.get("category_id"),
            item_name=request.form.get("item_name"),
            is_luxury=bool(True if request.form.get("is_luxury") else False),
            link=request.form.get("link"),
            description=request.form.get("description"),
            date_created=date.today()
            )
        db.session.add(item)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add_item.html", categories=categories)


@app.route("/edit_item/<int:id>", methods=["GET", "POST"])
def edit_item(id):
    item = Item.query.get_or_404(id)
    categories = list(Category.query.order_by(Category.name).all())
    if request.method == "POST":
        item.item_name = request.form.get("item_name")
        item.is_luxury = bool(True if request.form.get("is_luxury") else False)
        item.link = request.form.get("link")
        item.description = request.form.get("description")
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit_item.html", item=item, categories=categories)


@app.route("/delete_item/<int:id>")
def delete_item(id):
    item = Item.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for("home"))
