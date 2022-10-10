from myapp import create_app
# from myapp import db
# from myapp.models import User

app = create_app()


if __name__=="__main__":
    # with app.app_context():
    #     db.create_all()
    app.run(debug=True)