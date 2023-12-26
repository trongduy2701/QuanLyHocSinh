from app import app, login
import dao
from flask import render_template, redirect, request
from flask_login import login_user, logout_user
from app.models import LoaiNguoiDung


@app.route("/")
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def user_login():
    if request.method == 'POST':
        taikhoan = request.form.get('username')
        matkhau = request.form.get('password')

        nguoidung = dao.auth_user(taikhoan=taikhoan, matkhau=matkhau)

        if nguoidung:
            login_user(nguoidung)
            return redirect('/')
        else:
            return render_template('login.html', error='Incorrect username or password.')
    return render_template('login.html')

@login.user_loader
def get_user(user_id):
    return dao.get_user_by_id(user_id)

@app.route('/logout')
def logout():
    logout_user()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)