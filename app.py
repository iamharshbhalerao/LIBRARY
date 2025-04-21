from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'
  
# Mocked student credentials (replace with actual credentials and authentication logic)
student_credentials = {
    'student1': 'password1',
    'student2': 'password2'
}

# Mocked data for famous books and additional books
famous_books = [
    {"id": 1, "title": "A Basis for Theoretical Computer Science", "author": "Kfoury, Moll, and Robin", "image": "images/1.jpg"},
    {"id": 2, "title": "A Introduction to C#", "author": "Eric Gunnerson", "image": "images/2.png"},
    {"id": 3, "title": "A Smarter Way to learn Javascript", "author": "Mark Meyers", "image": "images/3.png"},
    {"id": 4, "title": "A Collection of Programming Problems and Techniques", "author": "Maurer and Williams", "image": "images/4.png"},
    {"id": 5, "title": "A Distributed Pi-Calculus", "author": "Hennessy", "image": "images/5.png"}
]

additional_books = [
    {"id": 6,"title": "A First Course in Database Systems 3e", "author": "Ullman and Widom", "image": "images/6.png"},
    {"id": 7,"title": "A Guide to MATLAB for Beginners and Experienced Users", "author": "Hunt, Lipsman, and Rosenberg", "image": "images/7.png"},
    {"id": 8,"title": "A Half-Century of Automata Theory Celebration and Inspiration", "author": "Salomaa, Wood, and Yu", "image": "images/8.png"},
    {"id": 9,"title": "Digital Design", "author": "M. Morris Mano, Michael D. Ciletti", "image": "images/9.png"},
    {"id": 10,"title": "Materials Science and Engineering: An Introduction", "author": "William D. Callister Jr., David G. Rethwisch", "image": "images/10.png"},
    {"id": 11,"title": "Introduction to Algorithms", "author": "Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein", "image": "images/11.png"},
    {"id": 12,"title": "Clean Code: A Handbook of Agile Software Craftsmanship", "author": "Robert C. Martin", "image": "images/12.png"},
    {"id": 13,"title": "The Pragmatic Programmer: Your Journey to Mastery", "author": "Andrew Hunt, David Thomas", "image": "images/13.png"},
    {"id": 14,"title": "Cracking the Coding Interview: 189 Programming Questions and Solutions", "author": "Gayle Laakmann McDowell", "image": "images/14.png"},
    {"id": 15,"title": "Design Patterns: Elements of Reusable Object-Oriented Software", "author": "Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides", "image": "images/15.png"},
    {"id": 16,"title": "Structure and Interpretation of Computer Programs", "author": "Harold Abelson, Gerald Jay Sussman, Julie Sussman", "image": "images/16.png"},
    {"id": 17,"title": "Artificial Intelligence: A Modern Approach", "author": "Stuart Russell, Peter Norvig", "image": "images/17.png"},
    {"id": 18,"title": "Database Management Systems", "author": "Raghu Ramakrishnan, Johannes Gehrke", "image": "images/18.png"},
    {"id": 19,"title": "Operating System Concepts", "author": "Abraham Silberschatz, Peter B. Galvin, Greg Gagne", "image": "images/19.png"},
    {"id": 20,"title": "Introduction to the Theory of Computation", "author": "Michael Sipser", "image": "images/20.png"},
    {"id": 21,"title": "Computer Networks: A Top-Down Approach", "author": "James F. Kurose, Keith W. Ross", "image": "images/21.png"},
    {"id": 22,"title": "The Art of Computer Programming", "author": "Donald E. Knuth", "image": "images/22.png"},
    {"id": 23,"title": "Python Crash Course: A Hands-On, Project-Based Introduction to Programming", "author": "Eric Matthes", "image": "images/23.png"},
    {"id": 24,"title": "Introduction to Machine Learning with Python: A Guide for Data Scientists", "author": "Andreas C. Müller, Sarah Guido", "image": "images/24.png"},
    {"id": 25,"title": "Head First Design Patterns", "author": "Eric Freeman, Elisabeth Robson, Bert Bates, Kathy Sierra", "image": "images/25.png"},
    {"id": 26,"title": "Computer Organization and Design: The Hardware/Software Interface", "author": "David A. Patterson, John L. Hennessy", "image": "images/26.png"},
    {"id": 27,"title": "Deep Learning with Python", "author": "François Chollet", "image": "images/27.png"},
    {"id": 28,"title": "Introduction to Artificial Intelligence", "author": "Wolfgang Ertel", "image": "images/28.png"},
    {"id": 29,"title": "Algorithms Unlocked", "author": "Thomas H. Cormen", "image": "images/29.png"},
    {"id": 30,"title": "Computer Security: Principles and Practice", "author": "William Stallings, Lawrie Brown", "image": "images/30.png"}
]
all_books = famous_books + additional_books

# Mocked authentication logic for student login
def authenticate_student(username, password):
    if username in student_credentials and student_credentials[username] == password:
        return True
    return False

# Initialize cart in session
def initialize_cart():
    if 'cart' not in session:
        session['cart'] = []

@app.route('/')
def index():
    # Pass the books data to the index.html template
    return render_template('index.html', books=all_books)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Mocked admin authentication logic (replace with actual logic)
        if username == 'admin' and password == 'adminpassword':
            return 'Admin Login successful'

        return 'Login unsuccessful. Please check your credentials.'
    
    return render_template('login.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        return 'Message sent successfully'
    
    return render_template('contact.html')

# Route for student login
@app.route('/student_login', methods=['GET', 'POST'])
def student_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Mocked authentication logic (replace with actual authentication)
        if authenticate_student(username, password):
            session['username'] = username
            return redirect('/student_dashboard')
        else:
            return render_template('student_login.html', error='Invalid credentials')
    
    return render_template('student_login.html')

# Route for student dashboard
@app.route('/student_dashboard')
def student_dashboard():
    initialize_cart()
    return render_template('student_dashboard.html', username=session.get('username'), cart=session['cart'], books=all_books)

# Route to add book to cart
@app.route('/add_to_cart/<int:book_id>', methods=['GET'])
def add_to_cart(book_id):
    initialize_cart()
    book = next((b for b in all_books if b['id'] == book_id), None)
    if book:
        session['cart'].append(book)
    return redirect('/student_dashboard')

# Route for search functionality
@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '').lower()
    results = [book for book in all_books if query in book['title'].lower()]
    return render_template('search_results.html', query=query, results=results)

if __name__ == '__main__':
    app.run(debug=True)