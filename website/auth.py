from flask import Blueprint as bp

auth = bp('auth', __name__)

@auth.route("/authenticate")
def authenticate():
    return "<h1> This is a website made by Jay but its the Auth </h1>"

