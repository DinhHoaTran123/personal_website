from flask import *
from flask_mail import Mail, Message
import json

# Set up config
app = Flask(__name__)

# Social Media Link
FACEBOOK_LINK = "https://www.facebook.com/thanhphat.tee/"
INSTAGRAM_LINK = "https://www.instagram.com/thanhphat.tee/"
LINKEDIN_LINK = "https://www.linkedin.com/in/teelam/"

# Set up email
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'tee.thanhlam@gmail.com'
app.config['MAIL_PASSWORD'] = '@Phatlam7428'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


@app.route("/")
@app.route("/index")
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


@app.route("/form-success")
def redirect_form_success():
    return render_template("form_success.html")


@app.route("/contact", methods=['POST'])
def contact_page_form():
    name = request.form.get('Name')
    email = request.form.get('Email')
    message = request.form.get('Message')

    # Get Contact info from sender
    info = {

        "Name": name,
        "Email": email,
        "Message": message

    }

    # Write contact info into JSON file, named contact.json
    with open("contact.json", "a") as fp:
        json.dump(info, fp)

    # Send confirmation email with email and body (message)
    send_confirmation_email(email, "Thanks for connecting with Lam. I will contact you")

    return render_template("form_success.html")


@app.route("/social-media-facebook")
def redirect_facebook():
    return redirect(FACEBOOK_LINK)


@app.route("/social-media-instagram")
def redirect_instagram():
    return redirect(INSTAGRAM_LINK)


@app.route("/social-media-linkedin")
def redirect_linkedin():
    return redirect(LINKEDIN_LINK)


# Send confirmation email
def send_confirmation_email(email, message):
    msg = Message("Thanks for reaching out", sender="tee.thanhlam@gmail.com", recipients=[email])
    msg.body = message
    mail.send(msg)


if __name__ == "__main__":
    app.run(debug=True)
