from main_API import app

if "__main__" == __name__:
    app.run(port=5000, host='localhost', debug=True)