from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'author':'vince',
        'title':'hi'
    },
    {
        'author':'vince',
        'title':'hello'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)