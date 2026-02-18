# Personal Blog with Flask 

## Project Description 
A full-featured personal blog website built with Flask featuring user authentication, blog post management, commenting system, and responsive design. This project demonstrates complete web development skills with Python. 

## What I Learned 
1. **Flask Framework**: Building web applications with Python
2. **Database Integration**: Using SQLAlchemy with SQLite
3. **User Authentication**: Secure login/registration systems
4. **Template Engine**: Dynamic HTML with Jinja2
5. **Form Handling**: Processing user input securely
6. **Web Security**: Password hashing, CSRF protection
7. **Responsive Design**: Mobile-friendly web interfaces


## Features 
- ✅ User registration and authentication
- ✅ Create, read, update, delete blog posts
- ✅ Comment system with moderation
- ✅ Rich text editor for post creation
- ✅ Search functionality
- ✅ Pagination for post lists
- ✅ Responsive Bootstrap design
- ✅ Image upload support
- ✅ RSS feed generation
- ✅ Contact form


## How to Run 
```bash 
# Install dependencies
pip install -r requirements.txt

# Initialize database
flask db init
flask db migrate
flask db upgrade

# Run the application
python run.py

# Access
at http://localhost:5000
```

## Required Libraries 
- Flask: Web framework
- Flask-SQLAlchemy: Database ORM
- Flask-WTF: Form handling
- Flask-Login: User session management
- Flask-Migrate: Database migrations
- Werkzeug: Security and utilities
- Bootstrap-Flask: Bootstrap integration


## Sample Output 
```
🌟 WELCOME TO MY BLOG 
======================= 📝
 LATEST POSTS:
1. Getting Started with Flask Web Development
Published: 2024-01-25 | Author: John Doe | Comments: 12 Learn how to build your first Flask application with this comprehensive guide... [Read More]

2. Python Data Analysis with
Pandas Published: 2024-01-20 | Author: Jane Smith | Comments: 8 Explore data analysis techniques using Python's pandas library... [Read More]

3. Building REST APIs with Flask
Published: 2024-01-15 | Author: John Doe | Comments: 15 A step-by-step guide to creating RESTful APIs... [Read More]

👥 RECENT COMMENTS:
- "Great tutorial! Helped me a lot."- Alex on Flask post
- "Looking forward to the next part!"- Sarah on Pandas post
- "Could you add more examples?" - Mike on API post

📊 BLOG STATS:
- Total Posts: 25
- Total Comments: 156
- Registered Users: 89
- Most Active User: John Doe (15 posts)

```
