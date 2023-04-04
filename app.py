from flask import Flask, request, render_template, redirect, url_for, flash

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

all_books_dict = [

    {

        "title": "The Hobbit",

        "author": "J.R.R. Tolkien",

        "pages": 295,

        "classification": "fiction",

        "details": "read, recommend",

        "acquisition": "library",

    },]

# Handling error 404 and displaying relevant web page
@app.errorhandler(404)
def not_found_error(error):
    return render_template("404.html"), 404

# Handling error 500 and displaying relevant web page
@app.errorhandler(500)
def internal_error(error):
    return render_template("500.html"), 500

@app.route("/", methods=["GET", "POST"])

def index():

    return render_template("index.html", pageTitle="My Library", books=all_books_dict)

 

@app.route("/", methods=["GET", "POST"])
def homepage():
    return redirect(url_for("index"))


@app.route("/add", methods=["POST"])
def add():
    print("inside add function")
    if request.method == "POST":

        form = request.form

        title = form["title"]
        author = form["author"]
        pages = form["pages"]
        classification = form["genre"]
        details = form["book"]
        acquistion = form.getlist("how")  # this is a PYthon list

        print(title)
        print(author)
        print(pages)
        print(classification)
        print(details)
        print(acquistion)

        acquistion_string = ", ".join(acquistion)  # make the Python list into a string

        book_dict = {
            "title": title,
            "author": author,
            "pages": pages,
            "classification": classification,
            "details": details,
            "acquisition": acquistion_string,
        }

        print(book_dict)
        all_books_dict.append(
            book_dict
        )  # append this dictionary entry to the larger friends dictionary
        print(all_books_dict)
        flash('Record successfully added.')
        return redirect(url_for("index"))
    else:
        return redirect(url_for("index"))

@app.route('/about')
def about():
    return render_template(
        "about.html", pageTitle="About Us", books=all_books_dict
    )

if __name__ == "__main__":
    app.run(debug=True)
