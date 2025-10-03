from website import create_app as ca

app = ca()

if __name__ == "__main__":
    app.run(debug=True)