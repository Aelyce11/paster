from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, validators
from wtforms.validators import DataRequired, ValidationError
from app.models import Post


class PostForm(FlaskForm):
    title = StringField(
        "Title :", [validators.Length(max=128), validators.DataRequired()]
    )
    content = TextAreaField(
        "Content :", [validators.Length(max=1024), validators.DataRequired()]
    )
    path = StringField(
        "Path :", [validators.Regexp(r"[A-Za-z0-9]{4}"), validators.Optional()]
    )
    submit = SubmitField("Post it !")

    def validate_path(self, path):
        post = Post.query.filter_by(path=path.data).first()
        if post is not None:
            raise ValidationError("Please use a different path.")
