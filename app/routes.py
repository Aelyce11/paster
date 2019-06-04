from flask import render_template, flash, redirect
from app import app, db
from app.models import Post
from app.forms import PostForm
import markdown
import random
import string

from flask import Markup

def autoPath():
    charset = string.ascii_lowercase + string.ascii_uppercase + "0123456789"
    return "".join(random.choice(charset) for i in range(4))


@app.route("/", methods=["GET", "POST"])
def index():
    form = PostForm()
    if form.validate_on_submit():

        if form.path.data == "":
            path = autoPath()
        else:
            path = form.path.data

        p = Post(title=form.title.data, content=form.content.data, path=path)
        db.session.add(p)
        db.session.commit()
        flash("Your post was was correctly uploaded")
        return redirect("/")
    return render_template("index.html", form=PostForm())


@app.route("/articles")
def articles():
    postList = Post.query.all()
    return render_template("postList.html", postList=postList)


@app.route("/articles/<path>")
def post(path):
    post = Post.query.filter_by(path=path).first_or_404()
    content = Markup(markdown.markdown(post.content))
    return render_template("post.html", post=post, content=content)

