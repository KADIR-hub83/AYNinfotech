from flask import (
    Blueprint, render_template,
    redirect, request,
    url_for, flash)
from flask_api import status
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from . models import db, Users, Customers, TaskStatus
from datetime import datetime


mod_users = Blueprint('mod_users', __name__, url_prefix='/admin')


def status_count(status):
    count = Customers.query.filter_by(sale_status=status, archive=False).count()
    return count

@mod_users.route('/login/', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('mod_users.dashboard'))

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = Users.query.filter_by(email=email).first()

        if not user or not check_password_hash(user.password, password):
            flash('Please check your login details and try again.')
            return redirect(url_for('mod_users.login'))

        login_user(user)
        user.write_time_stamp = datetime.utcnow()
        db.session.commit()
        return redirect(url_for('mod_users.dashboard'))

    return render_template('users/login.html')

@mod_users.route('/logout/')
@login_required
def logout():
    logout_user()
    return redirect(url_for('mod_users.login')), 301

@mod_users.route('/signup/', methods=['POST'])
def signup():
    if request.method == 'POST':
        first_name=request.form.get('first_name')
        last_name=request.form.get('last_name')
        phone_number=request.form.get('phone_number')
        email=request.form.get('email')
        password=request.form.get('password')
        secret_key = request.form.get('secret_key')
        content = ""

        if email and password and secret_key == "AYN Admin Panel":
            new_user = Users(first_name=first_name, last_name=last_name,
                             phone_number=phone_number, email=email,
                             password=generate_password_hash(password , method='pbkdf2:sha256', salt_length=8))

            db.session.add(new_user)
            db.session.commit()
            return content, status.HTTP_200_OK

        else:
            content = "Credentials provided are Invalid."
            return content, status.HTTP_401_UNAUTHORIZED

@mod_users.route('/sales/customer/archive/<int:id>', methods=['GET'])
def customer_archive(id):
    customer = Customers.query.filter_by(id=id).first()
    if customer:
        customer.archive=True
        db.session.commit()
        return redirect(url_for('mod_users.dashboard'))
    else:
        return redirect(url_for('404.html'))


@mod_users.route('/sales/dashboard/', methods=['GET'])
@mod_users.route('/sales/dashboard/<int:page_no>', methods=['GET'])
@login_required
def dashboard(page_no=1):
    customers = Customers.query.filter_by(archive=False).order_by(Customers.id.desc()).paginate(per_page=10, page=page_no, error_out=True)

    graph_data = []
    for rec in TaskStatus:
        graph_data.append([rec.value[0], status_count(rec.name), rec.value[1]])

    page_count = customers.pages - page_no

    if page_count > 2:
        return render_template("users/dashboard.html", current_page=page_no, next_pages=3,
                               posts=customers, graph_data=graph_data)
    else:
        total_pages = customers.pages
        if total_pages > 3:
            current_page = page_no + page_count - 3
            next_page = 3

        else:
            current_page = 0
            next_page = total_pages

        return render_template("users/dashboard.html", current_page=current_page, next_pages=next_page,
                               posts=customers, graph_data=graph_data)

@mod_users.route('/sales/dashboard/detail/<int:id>', methods=['GET', 'POST'])
@login_required
def detail_view(id):
    customer = Customers.query.filter_by(id=id, archive=False).first()

    if request.method == 'POST' and customer:
        customer.sales_comments = request.form.get('sales_comments')
        customer.sale_status = request.form.get('sale_status')
        customer.sales_person = request.form.get('sales_person')
        customer.project_cost = request.form.get('project_cost')
        customer.product_service = request.form.get('product_service')
        customer.product = request.form.get('product')
        customer.company = request.form.get('company')

        db.session.commit()

        return render_template("users/detailed_view.html", post=customer, sale_status=TaskStatus)
    elif request.method == 'GET' and customer:
        return render_template("users/detailed_view.html", post=customer, sale_status=TaskStatus)
    else:
        return render_template("404.html")

@mod_users.after_request
def after_request(response):
    if request.endpoint == 'mod_users.dashboard' or request.endpoint == 'mod_users.detail_view':
        response.headers.add('Cache-Control', 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0')
    return response