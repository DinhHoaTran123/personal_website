from flask import *

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def homepage():
    return render_template('index.html')


@app.route("/about")
def about_page():
    return render_template('about.html')

@app.route("/skills")
def skills_page():
    return render_template('skills.html')

@app.route("/projects")
def projects_page():
    return render_template('projects.html')

@app.route("/contact")
def contact_page():
    return render_template('contact.html')

@app.route("/social-media-facebook")
def redirect_facebook():
    return redirect("https://www.facebook.com/thanhphat.tee/")

@app.route("/social-media-instagram")
def redirect_instagram():
    return redirect("https://www.instagram.com/thanhphat.tee/")

@app.route("/social-media-linkedin")
def redirect_linkedin():
    return redirect("https://www.linkedin.com/in/teelam/")
if __name__ == "__main__":
    app.run(debug=True)
