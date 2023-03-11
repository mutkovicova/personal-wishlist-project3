from wishlist import db


class Category(db.Model):
    # schema for the Category model
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20), unique = True, nullable = False)
    items = db.relationship("Item", backref = "category", cascade = "all, delete", lazy = True)


    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.name


class Item(db.Model):
    # schema for the Item model
    id = db.Column(db.Integer, primary_key = True)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id", ondelete = "CASCADE"), nullable = False)
    item_name = db.Column(db.String(50), unique = True, nullable = False)
    is_luxury = db.Column(db.Boolean, default = False, nullable = False)
    link = db.Column(db.Text, nullable = True)
    description = db.Column(db.Text, nullable = False)
    date_created = db.Column(db.Date, nullable = False)


    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "#{0} - Item: {1} | Luxury: {2}".format(
            self.id, self.item_name, self.is_luxury
        )