from flask import Flask, render_template, url_for, flash, redirect, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from models import db, User, Post, Comment
from forms import RegistrationForm, LoginForm, PostForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '660d4dcbe353b7ed3031790ffd10f2c9'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # This only runs if the form passes all validators!
        hashed_password = generate_password_hash(form.password.data)
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    if request.method == 'POST':
        post = Post(title=request.form['title'], content=request.form['content'], author=current_user)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('create_post.html', title='New Post')

@app.route("/post/<int:post_id>/comment", methods=['POST'])
@login_required
def post_comment(post_id):
    comment_body = request.form.get('body')
    new_comment = Comment(body=comment_body, post_id=post_id, user_id=current_user.id)
    db.session.add(new_comment)
    db.session.commit()
    return redirect(url_for('post', post_id=post_id))

@app.route("/")
@app.route("/home")
def home():
    # This fetches all posts so the Jinja loop can display them
    posts = Post.query.order_by(Post.date_posted.desc()).all()
    return render_template('index.html', posts=posts)

@app.route("/post/<int:post_id>", methods=['GET', 'POST'])
def post(post_id):
    post = Post.query.get_or_404(post_id)
    form = CommentForm()
    
    if form.validate_on_submit():
        if not current_user.is_authenticated:
            flash('You must be logged in to comment.', 'danger')
            return redirect(url_for('login'))
            
        comment = Comment(body=form.body.data, post_id=post.id, user_id=current_user.id)
        db.session.add(comment)
        db.session.commit()
        flash('Your comment has been added!', 'success')
        return redirect(url_for('post', post_id=post.id))
        
    return render_template('post.html', title=post.title, post=post, form=form)

@app.route("/search")
def search():
    query = request.args.get('q')
    if query:
        # Searches for the query string inside the Title OR Content
        posts = Post.query.filter(
            (Post.title.contains(query)) | (Post.content.contains(query))
        ).order_by(Post.date_posted.desc()).all()
    else:
        posts = []
    return render_template('index.html', posts=posts, title="Search Results")


@app.errorhandler(404)
def error_404(error):
    # We return the template and the specific 404 status code
    return render_template('errors/404.html'), 404

@app.errorhandler(403)
def error_403(error):
    return render_template('errors/403.html'), 403

@app.errorhandler(500)
def error_500(error):
    return render_template('errors/500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)