from datetime import datetime

from flask import (
    Blueprint, render_template,
    request, redirect, url_for, jsonify)
from flask_api import status
from .models import Blogs, db
from flask_login import login_required
from sqlalchemy.sql.expression import func
from time import strptime

mod_blog = Blueprint('mod_blog', __name__)


@mod_blog.route('/blogs/')
@mod_blog.route('/blogs/<int:page_no>', methods=['GET'])
def blog_list(page_no=1):
    print("I am in List blog page view")
    # blogs = Blogs.query.filter_by(active=True).order_by(Blogs.id.desc()).paginate(per_page=6, page=page_no,
    #                                                                               error_out=True)
    blogs = Blogs.query.filter_by(active=True).order_by(Blogs.published_date.desc()).paginate(per_page=9, page=page_no,
                                                                                  error_out=True)
    page_count = blogs.pages - page_no
    if page_count > 2:
        return render_template("blog/blog_list.html", current_page=page_no, next_pages=3, posts=blogs)
    else:
        total_pages = blogs.pages

        if total_pages > 3:
            current_page = page_no + page_count - 3
            next_page = 3

        else:
            current_page = 0
            next_page = total_pages

        return render_template("blog/blog_list.html", current_page=current_page, next_pages=next_page, posts=blogs,
                               active_menu=["", "", "", "", "", "menu-active", ""])


@mod_blog.route('/blogs/<url_endpoint>/')
def blog_detail(url_endpoint):
    blog = Blogs.query.filter_by(url_endpoint=url_endpoint).first()
    get_date = blog.published_date
    get_month = get_date[4:6]
    year = get_date[0:4]
    day = get_date[6:]
    new_month = datetime.strptime(get_month, "%m").strftime("%b")
    new_date = str(day) + "-" + new_month + "-" + year
    blog.published_date = new_date

    #print(blog.description)
    if blog:
        random_blogs = Blogs.query.filter(Blogs.url_endpoint != url_endpoint, Blogs.active).order_by(
            func.random()).limit(3)
        return render_template('blog/blog_detail.html', url_endpoint=url_endpoint, post=blog, random_blogs=random_blogs,
                               active_menu=["", "", "", "", "", "menu-active", ""])
    else:
        return render_template('404.html'), 404


def status_count(status):
    count = Blogs.query.filter_by(active=status).count()
    return count


@mod_blog.route('/admin/blog/dashboard/', methods=['GET', 'POST'])
@mod_blog.route('/admin/blog/dashboard/<int:page_no>', methods=['GET'])
@login_required
def blog_dashboard(page_no=1):
    # blogs = Blogs.query.order_by(Blogs.id.desc()).paginate(per_page=10, page=page_no, error_out=True)
    blogs = Blogs.query.order_by(Blogs.published_date.desc()).paginate(per_page=10, page=page_no, error_out=True)
    graph_data = []
    graph_data.append(['Active', status_count(True), "rgb(75,192,192)"])
    graph_data.append(['Disabled', status_count(False), "rgb(255, 99, 132)"])

    page_count = blogs.pages - page_no
    if page_count > 2:
        return render_template("blog/dashboard.html", current_page=page_no, next_pages=3,
                               posts=blogs, graph_data=graph_data)
    else:
        total_pages = blogs.pages
        if total_pages > 3:
            current_page = page_no + page_count - 3
            next_page = 3

        else:
            current_page = 0
            next_page = total_pages

        return render_template("blog/dashboard.html", current_page=current_page, next_pages=next_page,
                               posts=blogs, graph_data=graph_data)


@mod_blog.route('/admin/blog/add/', methods=['GET', 'POST'])
@login_required
def blog_add():
    if request.method == 'POST':
        url_endpoint = request.form.get('endpoint_url').strip("/")
        image_src = request.form.get('blog_image')
        alt_text = request.form.get('alt_text')
        title = request.form.get('blog_title')
        dashboard_title = request.form.get('dashboard_title')
        content = request.form.get('blog_content')
        active = request.form.get('blog_active')
        published_date = request.form.get('published_date')

        print(published_date)
        date_list = published_date.split("-")
        month = date_list[1]
        int_month = strptime(month, '%b').tm_mon
        if (int_month >= 1) and (int_month <= 9):
            date_list[1] = "0" + str(int_month)
        else:
            date_list[1] = str(int_month)

        print(date_list[1])

        new_date = date_list[2]+date_list[1]+date_list[0]
        published_date = new_date
        print(published_date)

        description = request.form.get('description')
        blog = Blogs(image_src=image_src, alt_text=alt_text,
                     title=title.strip(), dashboard_title=dashboard_title,
                     content=content.strip(), url_endpoint=url_endpoint,
                     description=description, published_date=published_date,
                     active=True if active else False)
        db.session.add(blog)
        db.session.commit()
        return redirect(url_for("mod_blog.blog_dashboard"))

    else:
        default_title = """<h1 data-aos="fade-right" class="aos-init aos-animate">Blog <span class="text-primary">Title</span></h1>"""
        default_content = """<p>Blog Content</p>"""
        return render_template('blog/blog_add.html', title=default_title, content=default_content)


@mod_blog.route('/admin/blog/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def blog_edit(id):
    blog = Blogs.query.filter_by(id=id).first()
    if blog and request.method == 'GET':
        return render_template('blog/blog_edit.html', id=id, post=blog)
    elif blog and request.method == 'POST':
        blog.description = request.form.get('description')
        blog.url_endpoint = request.form.get('endpoint_url').strip("/")
        blog.image_src = request.form.get('blog_image')
        blog.alt_text = request.form.get('alt_text')
        blog.title = request.form.get('blog_title').strip()
        blog.dashboard_title = request.form.get('dashboard_title').strip()
        blog.content = request.form.get('blog_content').strip()
        blog.active = True if request.form.get('blog_active') else False
        blog.published_date = request.form.get('published_date')
        print(blog.published_date)

        date_list = blog.published_date.split("-")

        month = date_list[1]
        int_month = strptime(month, '%b').tm_mon
        if (int_month >= 1) and (int_month <= 9):
            date_list[1] = "0" + str(int_month)
        else:
            date_list[1] = str(int_month)

        new_date = date_list[2] + date_list[1] + date_list[0]
        blog.published_date = new_date
        db.session.commit()
        return render_template('blog/blog_edit.html', id=id, post=blog)
    else:
        return render_template('404.html'), 404


@mod_blog.route('/admin/blog/preview/<int:id>', methods=['GET', 'POST'])
@login_required
def blog_preview(id):
    blog = Blogs.query.filter_by(id=id).first()
    if blog:
        random_blogs = Blogs.query.filter(Blogs.id != id, Blogs.active).order_by(func.random()).limit(3)
        return render_template('blog/blog_preview.html', id=id, post=blog, random_blogs=random_blogs)
    else:
        return render_template('404.html'), 404


@mod_blog.route('/get/<url_endpoint>/', methods=['GET'])
def get_url_endpoint(url_endpoint):
    url_endpoint = Blogs.query.filter_by(url_endpoint=url_endpoint).first()

    if not url_endpoint:
        return jsonify(status=status.HTTP_200_OK)
    else:
        return jsonify(status=status.HTTP_404_NOT_FOUND)


