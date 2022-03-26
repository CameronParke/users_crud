from flask import Flask, render_template, request, redirect

from user import User

app = Flask(__name__)


@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def users():
    return render_template("read.html", users=User.get_all())

@app.route('/users/create')
def create():
    return render_template("create.html")


@app.route('/user/add', methods=['POST'])
def add_user():
    print(request.form)
    User.save(request.form)
    # data = { 
    #     "first_name" : request.form["first_name"],
    #     "last_name" : request.form["last_name"],
    #     "email" : request.form["email"],
    #     "created_at" : request.form["created_at"]
    # }
    # new_user_id = User.add_new_user(data)
    return redirect("/users")



@app.route('/user/<int:id>')
def show_user(id):
    data = {
        "id" : id
    }
    # one_friend storing the singular instance we created, now stored in one friend
# to send stuff from the server to the HTML need to include it after the render_template
    return render_template("show_user.html", user = User.get_one_user(data))

@app.route('/user/edit/<int:id>')
def edit_user(id):
    data = {
        "id" : id
    }
# one_friend storing the singular instance we created, now stored in one friend
# to send stuff from the server to the HTML need to include it after the render_template
    return render_template("edit_user.html", user = User.get_one_user(data))

@app.route('/user/edit', methods=['POST'])
def update_user():
    User.update_user(request.form)   
    return redirect('/users')

@app.route('/user/delete/<int:id>')
def delete_user(id):
    data = {
        "id" : id
    }
    User.delete_user(data)
    return redirect('/users')


if __name__ == "__main__":
    app.run(debug=True)

