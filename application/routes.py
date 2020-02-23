from flask import render_template, request, redirect
from application import app
from application.models import BlogPost, Users, Books

@app.route('/')
@app.route('/home')
def home():
     return render_template('home.html', title='Home')

@app.route('/books')
def books():
     return render_template('books.html', title='Books')

@app.route('/register')
def register():
     return render_template('register.html', title='Register')

@app.route('/login')
def login():
     return render_template('login.html', title='Login')

@app.route('/login/myaccount')
def myaccount():
     return render_template('myaccount.html', title='My Account')

@app.route('/login/myaccount/logout')
def logout():
     return render_template('logout.html', title='Logout')

@app.route('/login/myaccount/posts', methods=['GET', 'POST'])
def posts():
    if request.method == 'POST':
        post_title = request.form['title']
        post_author = request.form['author']
        post_content = request.form['content']
        new_post = BlogPost(title=post_title, content=post_content, author=post_author)
        db.session.add(new_post)
        db.session.commit()
        return redirect('/login/myaccount/posts')
    else:
        all_posts = BlogPost.query.order_by(BlogPost.date_posted).all()
        return render_template('/login/myaccount.html', all_posts=BlogPost)

@app.route('/login/myaccount/posts/delete/<int:id>')
def delete(id):
    post = BlogPost.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return redirect('/login/myaccount.html')

@app.route('/login/myaccount/posts/edit/<int:id>', methods=['GET','POST'])
def edit(id):
    post = BlogPost.query.get_or_404(id)
    if request.method == 'POST': 
        post.title = request.form['title']
        post.author = request.form['author']
        post.content = request.form['content']
        db.session.commit()
        return redirect('/posts')
    else:
        return render_template('edit.html', post=BlogPost)

@app.route('/login/myaccount/admin', methods=['GET','POST'])
def bookentry(id):
    post = BlogPost.query.get_or_404(id)
    if request.method == 'POST': 
        post.title = request.form['title']
        post.author = request.form['author']
        post.content = request.form['content']
        db.session.commit()
        return redirect('/posts')
    else:
        return render_template('edit.html', post=BlogPost)
