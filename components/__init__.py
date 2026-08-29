# from flask import (Flask, render_template,
#                    request, url_for,
#                    send_from_directory, redirect,
#                    )
# from flask_login import LoginManager
# from components.forms import ContactForm

# from config import SECRET_KEY
# from flask_sqlalchemy import SQLAlchemy
# from decorators import async_task
# from mail_service import (service_account_login, create_message,
#                           send_message, create_content,
#                           create_document_content)
# from werkzeug.utils import secure_filename
# import os
# service = service_account_login()

# @async_task
# def send_email(name, email, query, mobile):
#     content = create_content(name, email, query, mobile)
#     send_message(service, create_message(to=email, message_text=content))

# @async_task
# def send_product_email(name, phone, work_email, company, product, comments):
#     create_document_content(name=name, phone=phone, work_email=work_email,
#                             company=company, product=product, comments=comments)

# app = Flask(__name__)
# app.config.from_object('config')
# app.config['SECRET_KEY'] = SECRET_KEY
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ayn_infotech.sqlite3'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
# UPLOAD_FOLDER = 'data/resume'
# ALLOWED_EXTENSIONS = {'pdf'}
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# ## Database Tables
# from components.mod_users import models as user_model
# from components.mod_blog import models as blog_model
# from components.mod_product.controllers import mod_product
# from components.mod_need.controllers import mod_need
# from components.mod_service.controllers import mod_service
# from components.mod_about.controllers import mod_about
# from components.mod_users.controllers import mod_users
# from components.mod_blog.controllers import mod_blog
# from components.mod_career.controller import mod_career


# app.register_blueprint(mod_product)
# app.register_blueprint(mod_service)
# app.register_blueprint(mod_need)
# app.register_blueprint(mod_about)
# app.register_blueprint(mod_users)
# app.register_blueprint(mod_blog)
# app.register_blueprint(mod_career)


# ## Initialize Login Manager
# login_manager = LoginManager()
# login_manager.login_view = 'auth.login'
# login_manager.init_app(app)

# ## Load Login User
# @login_manager.user_loader
# def load_user(user_id):
#     return user_model.Users.query.get(user_id)

# ## Handle Unauthorize Access
# @login_manager.unauthorized_handler
# def unauthorized_callback():
#     return redirect('/admin/login')

# ## Error page
# @app.errorhandler(404)
# def page_not_found(e):
#     # note that we set the 404 status explicitly
#     return render_template('404.html', active_menu=["", "", "", "", "", "", ""]), 404

# # SITEMAP, ROBOTS
# @app.route('/robots.txt')
# @app.route('/sitemap.xml')
# def static_from_root():
#     return send_from_directory(app.static_folder, request.path[1:])

# @app.route('/sitemap/')
# def sitemap():
#     return redirect(url_for('mod_about.sitemap')), 301


# @app.route('/<type>/thankyou/')
# def thankyou(type):
#     if type == 'contact':
#         return render_template('thankyou.html', page_for='contact',
#                                active_menu=["", "", "", "", "", "", ""])
#     else:
#         return render_template('404.html'), 404



# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':

#         name = request.form.get('name')
#         work_email = request.form.get('work_email')
#         phone = request.form.get('phone')
#         message = request.form.get('message')
#         country = request.form.get('country_code').split(',')

#         contact_form = user_model.Customers(name=name, email=work_email,
#                                             country=country[1], phone_number=country[0]+' '+phone,
#                                             comments=message, type='Contact Us')
#         db.session.add(contact_form)
#         db.session.commit()

#         send_email(name=name, email=work_email, query=message, mobile=phone)
#         return redirect(url_for('thankyou', type='contact'))

#     else:
#         blogs = blog_model.Blogs.query.order_by(blog_model.Blogs.id.desc()).limit(3)
#         return render_template('index.html',
#                                 posts=blogs,
#                                 active_menu=["", "", "", "", "", "", ""])

# @app.route('/contact/', methods=["GET", "POST"])
# def contact():
#     from components.forms import ContactForm
#     form = ContactForm(request.form)
#     if form.validate_on_submit():
#         name = form.name.data
#         work_email = form.work_email.data
#         phone = form.phone.data
#         message = form.message.data
#         country = request.form.get('country_code').split(',')
#         contact_form = user_model.Customers(name=name, email=work_email,country=country[1],
#              phone_number=phone, comments=message, type='Contact Us')
#         db.session.add(contact_form)
#         db.session.commit()

#         # send_email(name=name, email=work_email, query=message, mobile=phone)
#         return redirect(url_for('thankyou', type='contact'))
#     return render_template('other/contact.html',active_menu=["", "", "", "", "", "", "menu-active"], form=form)


# @app.route('/careers/', methods=['GET', 'POST'])
# def career():
#     if request.method == 'POST':
#         resume = request.files['resume']
#         filename = secure_filename(resume.filename)
#         resume.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

#         full_name = request.form.get('full_name')
#         phone = request.form.get('phone')
#         email = request.form.get('email')
#         resume = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#         applied_for = request.form.get('applied_for')
#         message = request.form.get('message')

#         job = job_model.Jobs(full_name=full_name, phone=phone, email=email,
#                    resume=resume, applied_for=applied_for, message=message)
#         db.session.add(job)
#         db.session.commit()
#         return redirect(url_for('career'))
#     else:
#         return render_template('other/career.html',
#                                 active_menu=["", "", "", "", "menu-active", "", ""])

# @app.route('/about/')
# def about_us_new():
#     return render_template('about/about.html', active_menu=["", "", "", "menu-active", "", "", ""])

# @app.route('/privacy-policy/')
# def privacy_policy():
#     return render_template('other/terms-of-use.html', active_menu=["", "", "", "", "", "", ""])

# @app.route('/contact-us/')
# @app.route('/global/')
# def contact_redirect():
#     return redirect(url_for('contact')), 301


# @app.route('/mechanical-engineering/')
# @app.route('/capital-market-services/')
# @app.route('/industrial-manufacturing/')
# @app.route('/electronic-payment-method/')
# @app.route('/wealth-management-services/')
# @app.route('/capital-market-services-view/')
# @app.route('/digital-engineering-services/')
# @app.route('/banking-and-finance-services/')
# @app.route('/industrial-manufacturing-view/')
# @app.route('/service/financial-services/')
# def electronic_payment_method():
#     return redirect(url_for('mod_service.banking')), 301

# @app.route('/web-development/')
# @app.route('/ios-development/')
# @app.route('/demanding-product/')
# @app.route('/windows-development/')
# @app.route('/android-development/')
# @app.route('/ecommerce-development/')
# @app.route('/web-design-strategies/')
# @app.route('/research-and-innovation/')
# @app.route('/software-product-testing/')
# @app.route('/benefits-of-mobile-design-app/')
# @app.route('/index.php/capital-market-services/')
# @app.route('/advanced-web-development-services/')
# @app.route('/android-app-development-life-cycle/')
# @app.route('/systems-hardware-engineering-services/')
# def research():
#     return redirect(url_for('index')), 301

# @app.route('/analytics')
# @app.route('/cloud-applications')
# @app.route('/cloud-infrastructure')
# @app.route('/cloud-computing-services/')
# @app.route('/static-vs-dynamic-website/')
# @app.route('/oracle-application-framework-services')
# @app.route('/everything-you-wanted-to-know-about-cloud-computing/')
# def redirect_analytics():
#     return redirect(url_for('mod_need.analytics')), 301

# @app.route('/telecom/')
# @app.route('/vlsi-design-services/')
# @app.route('/vlsi-design-services-view/')
# @app.route('/energy-resources-utilities/')
# @app.route('/mechanical-engineering-view/')
# @app.route('/embedded-engineering-system-design/')
# @app.route('/embedded-engineering-system-design-view/')
# @app.route('/service/telecom/')
# def hardware():
#     return redirect(url_for('mod_service.telecommunications')), 301

# @app.route('/automation-and-ai/')
# @app.route('/customer-intelligence-insights/')
# @app.route('/cognitive-automation-outsourcing/')
# @app.route('/artificial-intelligence-seo-future/')
# @app.route('/need/artificial-intelligence/')
# def need_redirect():
#     return redirect(url_for('mod_need.ai')), 301

# @app.route('/product-lifecycle-management-plm/')
# @app.route('/healthcare-and-life-sciences-services-view/')
# @app.route('/service/healthcare-and-life-sciences/')
# @mod_service.route('/healthcare-and-life-sciences-services-view/')
# def healthcare_and_lifesciences():
#     return redirect(url_for('mod_service.healthcare')), 301

# @app.route('/need/blockchain/')
# def redirect_blockchain():
#     return redirect(url_for('mod_need.blockchain')), 301

# @app.route('/internet-of-things-IoT/')
# @app.route('/what-is-automation-marketing-Its-tools')
# @app.route('/need/internet-of-things/')
# def redirect_iot():
#     return redirect(url_for('mod_need.iot')), 301

# @app.route('/retail-services/')
# @app.route('/retail-services-view/')
# @app.route('/service/retail/')
# def retail_services():
#     return redirect(url_for('mod_service.retail')), 301

# @app.route('/industrial-engineering-services/')
# @app.route('/need/analytics/')
# def industrial_engineering_services():
#     return redirect(url_for('mod_need.analytics')), 301

# @app.route('/hotel-and-food-industries-view/')
# @app.route('/service/hotel-and-food/')
# def hotel_and_food():
#     return redirect(url_for('mod_service.hotel_food_industry')), 301

# @app.route('/insurance-services/')
# @app.route('/service/insurance/')
# def insurance_services():
#     return redirect(url_for('mod_service.insurance')), 301

# @app.route('/education-erp-services/')
# @app.route('/service/education/')
# def education_erp_services():
#     return redirect(url_for('mod_service.education')), 301

# @app.route('/automation-and-ai-view/')
# def automation_and_ai():
#     return redirect(url_for('mod_need.ai')), 301

# @app.route('/investor-relations-view/')
# def investor_relations_view():
#     return redirect(url_for('mod_about.investors')), 301

# @app.route('/service/public-sector/')
# def software():
#     return redirect(url_for('mod_service.government')), 301


# @app.route('/about-us/')
# @app.route('/about-us-view')
# @app.route('/about/Nasrin-sheikh/')
# @app.route('/about/nasrin-sheikh/')
# @app.route('/about/our-values/')

# def about_us():
#     return redirect(url_for('mod_about.our_story')), 301


# @app.route('/about/vision/')
# def _vision():
#     return redirect(url_for('mod_about.vision')), 301

# @app.route('/about/investor-relations/')
# def _invrel():
#     return redirect(url_for('mod_about.investors')), 301

# @app.route('/service/non-profit-organisation/')
# def redirect_npo():
#     return redirect(url_for('mod_service.nonprofit'))


# #PRODUCT(WHY AND WHAT)
# @app.route('/product/what-is-healthcare/')
# def what_healthcare():
#     return redirect(url_for('mod_product.what_is_healthcare')), 301

# @app.route('/product/what-is-crm/')
# def what_crm():
#     return redirect(url_for('mod_product.what_is_crm')), 301

# @app.route('/product/what-is-cbs/')
# def what_cbs():
#     return redirect(url_for('mod_product.what_is_cbs')), 301

# @app.route('/product/what-is-erp/')
# def what_erp():
#     return redirect(url_for('mod_product.what_is_erp')), 301

# @app.route('/product/why-oak/')
# def why_oak():
#     return redirect(url_for('mod_product.oak_features')), 301

# @app.route('/product/why-cedar/')
# def why_cedar():
#     return redirect(url_for('mod_product.cedar_features')), 301

# @app.route('/product/why-pine/')
# def why_pine():
#     return redirect(url_for('mod_product.pine_features')), 301

# @app.route('/product/why-walnut/')
# def why_walnut():
#     return redirect(url_for('mod_product.walnut_features')), 301

# @app.route('/product/oak/')
# def pro_oak():
#     return redirect(url_for('mod_product.oak')), 301

# @app.route('/product/pine/')
# def pro_pine():
#     return redirect(url_for('mod_product.pine')), 301

# @app.route('/product/cedar/')
# def pro_cedar():
#     return redirect(url_for('mod_product.cedar')), 301

# @app.route('/product/walnut/')
# @app.route('/education-erp/')
# def pro_walnut():
#     return redirect(url_for('mod_product.walnut')), 301




from flask import (
    Flask,
    render_template,
    request,
    url_for,
    send_from_directory,
    redirect,
)

from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename

import os

from decorators import async_task
from mail_service import (
    service_account_login,
    create_message,
    send_message,
    create_content,
    create_document_content,
)
from components.forms import ContactForm


# =========================================================
# APP
# =========================================================

app = Flask(__name__)


# =========================================================
# ENVIRONMENT
# =========================================================

IS_VERCEL = bool(os.environ.get("VERCEL"))
IS_PRODUCTION = (
    os.environ.get("FLASK_ENV") == "production"
    or IS_VERCEL
)


# =========================================================
# SECRET KEY
# =========================================================

app.config["SECRET_KEY"] = os.environ.get(
    "SECRET_KEY",
    "local-development-secret-key"
)


# =========================================================
# DATABASE
# =========================================================

DATABASE_URL = os.environ.get("DATABASE_URL")

if DATABASE_URL:

    # Some providers still return postgres://
    # SQLAlchemy expects postgresql://
    if DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = DATABASE_URL.replace(
            "postgres://",
            "postgresql://",
            1
        )

    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL

else:

    # Local development
    # On Vercel this is temporary only (data will NOT persist
    # across requests/deploys). Set DATABASE_URL in Vercel env
    # vars pointing to a real Postgres DB (e.g. Neon, Supabase)
    # for production use.
    if IS_VERCEL:
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/ayn_infotech.sqlite3"
    else:
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ayn_infotech.sqlite3"


app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
    "pool_pre_ping": True
}


db = SQLAlchemy(app)


# =========================================================
# FILE UPLOAD
# =========================================================

if IS_VERCEL:
    UPLOAD_FOLDER = "/tmp/resume"
else:
    UPLOAD_FOLDER = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "data",
        "resume"
    )


os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = {"pdf"}


# =========================================================
# GOOGLE / MAIL SERVICE
# =========================================================

# IMPORTANT:
# Do NOT login to Google when Flask application imports.
# Otherwise Vercel function crashes if credentials are absent.

_service = None


def get_mail_service():
    global _service

    if _service is not None:
        return _service

    try:
        _service = service_account_login()
        return _service

    except Exception as error:
        print("Google mail service unavailable:", str(error))
        return None


@async_task
def send_email(name, email, query, mobile):

    try:
        service = get_mail_service()

        if service is None:
            print("Email skipped: Google service unavailable")
            return

        content = create_content(
            name,
            email,
            query,
            mobile
        )

        message = create_message(
            to=email,
            message_text=content
        )

        send_message(
            service,
            message
        )

    except Exception as error:
        # Email failure should never crash website
        print("send_email error:", str(error))


@async_task
def send_product_email(
    name,
    phone,
    work_email,
    company,
    product,
    comments
):

    try:
        create_document_content(
            name=name,
            phone=phone,
            work_email=work_email,
            company=company,
            product=product,
            comments=comments
        )

    except Exception as error:
        print("send_product_email error:", str(error))


# =========================================================
# DATABASE MODELS + BLUEPRINTS
# =========================================================

from components.mod_users import models as user_model
from components.mod_blog import models as blog_model
from components.mod_career import models as job_model

from components.mod_product.controllers import mod_product
from components.mod_need.controllers import mod_need
from components.mod_service.controllers import mod_service
from components.mod_about.controllers import mod_about
from components.mod_users.controllers import mod_users
from components.mod_blog.controllers import mod_blog
from components.mod_career.controller import mod_career


app.register_blueprint(mod_product)
app.register_blueprint(mod_service)
app.register_blueprint(mod_need)
app.register_blueprint(mod_about)
app.register_blueprint(mod_users)
app.register_blueprint(mod_blog)
app.register_blueprint(mod_career)


# =========================================================
# LOGIN MANAGER
# =========================================================

login_manager = LoginManager()

# Your login blueprint endpoint
login_manager.login_view = "mod_users.login"

login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):

    try:
        return user_model.Users.query.get(int(user_id))
    except Exception:
        return None


@login_manager.unauthorized_handler
def unauthorized_callback():
    return redirect("/admin/login/")


# =========================================================
# ERROR HANDLER
# =========================================================

@app.errorhandler(404)
def page_not_found(error):

    return render_template(
        "404.html",
        active_menu=["", "", "", "", "", "", ""]
    ), 404


@app.errorhandler(500)
def internal_server_error(error):

    print("500 ERROR:", str(error))

    return "Internal Server Error", 500


# =========================================================
# STATIC ROOT FILES
# =========================================================

@app.route("/robots.txt")
@app.route("/sitemap.xml")
def static_from_root():

    return send_from_directory(
        app.static_folder,
        request.path[1:]
    )


@app.route("/sitemap/")
def sitemap():

    return redirect(
        url_for("mod_about.sitemap")
    ), 301


# =========================================================
# CORE ROUTES
# =========================================================

@app.route("/<type>/thankyou/")
def thankyou(type):
    if type == "contact":
        return render_template(
            "thankyou.html",
            page_for="contact",
            active_menu=["", "", "", "", "", "", ""]
        )
    else:
        return render_template("404.html"), 404


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        name = request.form.get("name")
        work_email = request.form.get("work_email")
        phone = request.form.get("phone")
        message = request.form.get("message")
        country = request.form.get("country_code", "").split(",")

        contact_form = user_model.Customers(
            name=name,
            email=work_email,
            country=country[1] if len(country) > 1 else "",
            phone_number=(country[0] if country else "") + " " + (phone or ""),
            comments=message,
            type="Contact Us"
        )
        db.session.add(contact_form)
        db.session.commit()

        send_email(name=name, email=work_email, query=message, mobile=phone)
        return redirect(url_for("thankyou", type="contact"))

    else:
        blogs = blog_model.Blogs.query.order_by(blog_model.Blogs.id.desc()).limit(3)
        return render_template(
            "index.html",
            posts=blogs,
            active_menu=["", "", "", "", "", "", ""]
        )


@app.route("/contact/", methods=["GET", "POST"])
def contact():
    form = ContactForm(request.form)
    if form.validate_on_submit():
        name = form.name.data
        work_email = form.work_email.data
        phone = form.phone.data
        message = form.message.data
        country = request.form.get("country_code", "").split(",")

        contact_form = user_model.Customers(
            name=name,
            email=work_email,
            country=country[1] if len(country) > 1 else "",
            phone_number=phone,
            comments=message,
            type="Contact Us"
        )
        db.session.add(contact_form)
        db.session.commit()

        # send_email(name=name, email=work_email, query=message, mobile=phone)
        return redirect(url_for("thankyou", type="contact"))

    return render_template(
        "other/contact.html",
        active_menu=["", "", "", "", "", "", "menu-active"],
        form=form
    )


@app.route("/careers/", methods=["GET", "POST"])
def career():
    if request.method == "POST":
        resume = request.files["resume"]
        filename = secure_filename(resume.filename)
        resume.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

        full_name = request.form.get("full_name")
        phone = request.form.get("phone")
        email = request.form.get("email")
        resume_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        applied_for = request.form.get("applied_for")
        message = request.form.get("message")

        job = job_model.Jobs(
            full_name=full_name,
            phone=phone,
            email=email,
            resume=resume_path,
            applied_for=applied_for,
            message=message
        )
        db.session.add(job)
        db.session.commit()
        return redirect(url_for("career"))
    else:
        return render_template(
            "other/career.html",
            active_menu=["", "", "", "", "menu-active", "", ""]
        )


@app.route("/about/")
def about_us_new():
    return render_template(
        "about/about.html",
        active_menu=["", "", "", "menu-active", "", "", ""]
    )


@app.route("/privacy-policy/")
def privacy_policy():
    return render_template(
        "other/terms-of-use.html",
        active_menu=["", "", "", "", "", "", ""]
    )


@app.route("/contact-us/")
@app.route("/global/")
def contact_redirect():
    return redirect(url_for("contact")), 301


@app.route("/mechanical-engineering/")
@app.route("/capital-market-services/")
@app.route("/industrial-manufacturing/")
@app.route("/electronic-payment-method/")
@app.route("/wealth-management-services/")
@app.route("/capital-market-services-view/")
@app.route("/digital-engineering-services/")
@app.route("/banking-and-finance-services/")
@app.route("/industrial-manufacturing-view/")
@app.route("/service/financial-services/")
def electronic_payment_method():
    return redirect(url_for("mod_service.banking")), 301


@app.route("/web-development/")
@app.route("/ios-development/")
@app.route("/demanding-product/")
@app.route("/windows-development/")
@app.route("/android-development/")
@app.route("/ecommerce-development/")
@app.route("/web-design-strategies/")
@app.route("/research-and-innovation/")
@app.route("/software-product-testing/")
@app.route("/benefits-of-mobile-design-app/")
@app.route("/index.php/capital-market-services/")
@app.route("/advanced-web-development-services/")
@app.route("/android-app-development-life-cycle/")
@app.route("/systems-hardware-engineering-services/")
def research():
    return redirect(url_for("index")), 301


@app.route("/analytics")
@app.route("/cloud-applications")
@app.route("/cloud-infrastructure")
@app.route("/cloud-computing-services/")
@app.route("/static-vs-dynamic-website/")
@app.route("/oracle-application-framework-services")
@app.route("/everything-you-wanted-to-know-about-cloud-computing/")
def redirect_analytics():
    return redirect(url_for("mod_need.analytics")), 301


@app.route("/telecom/")
@app.route("/vlsi-design-services/")
@app.route("/vlsi-design-services-view/")
@app.route("/energy-resources-utilities/")
@app.route("/mechanical-engineering-view/")
@app.route("/embedded-engineering-system-design/")
@app.route("/embedded-engineering-system-design-view/")
@app.route("/service/telecom/")
def hardware():
    return redirect(url_for("mod_service.telecommunications")), 301


@app.route("/automation-and-ai/")
@app.route("/customer-intelligence-insights/")
@app.route("/cognitive-automation-outsourcing/")
@app.route("/artificial-intelligence-seo-future/")
@app.route("/need/artificial-intelligence/")
def need_redirect():
    return redirect(url_for("mod_need.ai")), 301


@app.route("/product-lifecycle-management-plm/")
@app.route("/healthcare-and-life-sciences-services-view/")
@app.route("/service/healthcare-and-life-sciences/")
def healthcare_and_lifesciences():
    return redirect(url_for("mod_service.healthcare")), 301


@app.route("/need/blockchain/")
def redirect_blockchain():
    return redirect(url_for("mod_need.blockchain")), 301


@app.route("/internet-of-things-IoT/")
@app.route("/what-is-automation-marketing-Its-tools")
@app.route("/need/internet-of-things/")
def redirect_iot():
    return redirect(url_for("mod_need.iot")), 301


@app.route("/retail-services/")
@app.route("/retail-services-view/")
@app.route("/service/retail/")
def retail_services():
    return redirect(url_for("mod_service.retail")), 301


@app.route("/industrial-engineering-services/")
@app.route("/need/analytics/")
def industrial_engineering_services():
    return redirect(url_for("mod_need.analytics")), 301


@app.route("/hotel-and-food-industries-view/")
@app.route("/service/hotel-and-food/")
def hotel_and_food():
    return redirect(url_for("mod_service.hotel_food_industry")), 301


@app.route("/insurance-services/")
@app.route("/service/insurance/")
def insurance_services():
    return redirect(url_for("mod_service.insurance")), 301


@app.route("/education-erp-services/")
@app.route("/service/education/")
def education_erp_services():
    return redirect(url_for("mod_service.education")), 301


@app.route("/automation-and-ai-view/")
def automation_and_ai():
    return redirect(url_for("mod_need.ai")), 301


@app.route("/investor-relations-view/")
def investor_relations_view():
    return redirect(url_for("mod_about.investors")), 301


@app.route("/service/public-sector/")
def software():
    return redirect(url_for("mod_service.government")), 301


@app.route("/about-us/")
@app.route("/about-us-view")
@app.route("/about/Nasrin-sheikh/")
@app.route("/about/nasrin-sheikh/")
@app.route("/about/our-values/")
def about_us():
    return redirect(url_for("mod_about.our_story")), 301


@app.route("/about/vision/")
def _vision():
    return redirect(url_for("mod_about.vision")), 301


@app.route("/about/investor-relations/")
def _invrel():
    return redirect(url_for("mod_about.investors")), 301


@app.route("/service/non-profit-organisation/")
def redirect_npo():
    return redirect(url_for("mod_service.nonprofit"))


# PRODUCT (WHY AND WHAT)

@app.route("/product/what-is-healthcare/")
def what_healthcare():
    return redirect(url_for("mod_product.what_is_healthcare")), 301


@app.route("/product/what-is-crm/")
def what_crm():
    return redirect(url_for("mod_product.what_is_crm")), 301


@app.route("/product/what-is-cbs/")
def what_cbs():
    return redirect(url_for("mod_product.what_is_cbs")), 301


@app.route("/product/what-is-erp/")
def what_erp():
    return redirect(url_for("mod_product.what_is_erp")), 301


@app.route("/product/why-oak/")
def why_oak():
    return redirect(url_for("mod_product.oak_features")), 301


@app.route("/product/why-cedar/")
def why_cedar():
    return redirect(url_for("mod_product.cedar_features")), 301


@app.route("/product/why-pine/")
def why_pine():
    return redirect(url_for("mod_product.pine_features")), 301


@app.route("/product/why-walnut/")
def why_walnut():
    return redirect(url_for("mod_product.walnut_features")), 301


@app.route("/product/oak/")
def pro_oak():
    return redirect(url_for("mod_product.oak")), 301


@app.route("/product/pine/")
def pro_pine():
    return redirect(url_for("mod_product.pine")), 301


@app.route("/product/cedar/")
def pro_cedar():
    return redirect(url_for("mod_product.cedar")), 301


@app.route("/product/walnut/")
@app.route("/education-erp/")
def pro_walnut():
    return redirect(url_for("mod_product.walnut")), 301