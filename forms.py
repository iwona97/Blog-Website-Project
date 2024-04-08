from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL, Email, Length, Regexp
from flask_ckeditor import CKEditorField


# WTForm for creating a blog post
class CreatePostForm(FlaskForm):
    title = StringField(label="Blog Post Title", validators=[DataRequired()])
    subtitle = StringField(label="Subtitle", validators=[DataRequired()])
    img_url = StringField(label="Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField(label="Blog Content", validators=[DataRequired()])
    submit = SubmitField(label="Submit Post")


# Create a form to register new users
class RegisterForm(FlaskForm):
    # Requires email_validator package to be installed. For ex: pip install wtforms[email]
    email = StringField(label="Email", validators=[DataRequired(), Email(message='Invalid email address. A valid email address should contains "." and "@".')])
    password = PasswordField(label="Password",
                             validators=[DataRequired(),
                                         Length(min=8, message="Field must be at least 8 characters long."),
                                         Regexp(regex=r'^(?=.*\d)(?=.*[!@#$%^&*()])(?=.*[a-z])(?=.*[A-Z]).{8,}$', message='Password must contain at least one digit, one special character, and one uppercase letter.')])
    name = StringField(label="Name", validators=[DataRequired()])
    submit = SubmitField(label="Sign Me Up!")


# Create a form to login existing users
class LoginForm(FlaskForm):
    email = StringField(label="Email", validators=[DataRequired(), Email(message='Invalid email address. A valid email address should contains "." and "@".')])
    password = PasswordField(label="Password", validators=[DataRequired()])
    submit = SubmitField(label="Let Me In!")


# Create a form to add comments
class CommentForm(FlaskForm):
    comment_text = CKEditorField(label="Comment", validators=[DataRequired()])
    submit = SubmitField(label="Submit Comment")
