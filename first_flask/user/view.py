from flask import Blueprint,jsonify,request
from first_flask import db
from first_flask.user.models import Student_info  #importing model.py file
mod= Blueprint('user',__name__,url_prefix='/user_info')


@mod.route('/',methods=['GET'])
def fetch_users():
    users=Student_info.query.all()
    response=[x.__repr__() for x in users]
    return jsonify(response)

    ##http://127.0.0.1:5000/user_info

@mod.route('/<user_id>',methods=["GET"])
def show(user_id):
    users=Student_info.query.get(int(user_id))
    response=users.__repr__()
    response.pop('password')
    return  jsonify(response)

    ##http://127.0.0.1:5000/user_info/1

@mod.route('/get_user',methods=["GET"])
def fetch_user_name():
    username= request.args.get('username')
    stu=Student_info.query.filter(Student_info.username==username).first()
    response=stu.__repr__()
    return jsonify(response)

    ##http://127.0.0.1:5000/user_info/get_user?username=sai

@mod.route('/create_user',methods=["POST"])
def create_user1():
    user_data=request.get_json()
    user=Student_info(
        username=user_data['username'],
        email= user_data['email'],
        password =user_data['password']
    )
    db.session.add(user)
    db.session.commit()
    return "user add succesfully"

    ##http://127.0.0.1:5000/user_info/create_user

@mod.route('/create_user_form',methods=["POST"])
def create_user2():
    username=request.form.get('username')
    email =request.form.get('email')
    password=request.form.get('password')
    user=Student_info(
        username=username,
        email=email,
        password=password
    )
    db.session.add(user)
    db.session.commit()
    return "user add succesfully"

    ##http://127.0.0.1:5000/user_info/create_user_form

@mod.route('/update_user/<user_id>',methods=["PUT"])
def update_user(user_id):
    user_data=request.get_json()
    user=Student_info.query.get(int(user_id))
    user.email=user_data['email']
    db.session.commit()
    return "user details update succesfully"

    ##http://127.0.0.1:5000/user_info/update_user/4

@mod.route('/delete_user/<user_id>',methods=["DELETE"])
def delete_user(user_id):
    user=Student_info.query.get(int(user_id))
    db.session.delete(user)
    db.session.commit()
    return "user has been deleted succesfully"

    ##http://127.0.0.1:5000/user_info/delete_user/6
