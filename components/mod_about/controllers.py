from flask import Blueprint, render_template, redirect, url_for
from config_about import *

mod_about = Blueprint('mod_about', __name__, url_prefix='')

@mod_about.route('/our-values/')
def our_story():
    return render_template('about/our-story.html',
                           heading_1=STORY_HEADING_1,
                           para_1=STORY_PARA_1,
                           image_1=STORY_IMAGE_1,
                           heading_2=STORY_HEADING_2,
                           para_2=STORY_PARA_2,
                           features_2=STORY_FEATURES_2,
                           alt_text_1 = STORY_ALT_TEXT_1,
                           active_menu=ACTIVE_STATUS)



@mod_about.route('/leadership/')
def leadership():
    return render_template('about/leadership.html',
                            active_menu=ACTIVE_STATUS)




@mod_about.route('/vision/')
def vision():
    return render_template('about/vision.html',
                            active_menu=ACTIVE_STATUS)


@mod_about.route('/sitemap/')
def sitemap():
    return render_template('sitemap/sitemap.html',
                            active_menu=ACTIVE_STATUS)


@mod_about.route('/investor-relations')
def investors():
    return render_template('about/investors.html',
                            active_menu=ACTIVE_STATUS)


@mod_about.route('/faq/')
def faq():
    return render_template('about/faq.html',
                            active_menu=ACTIVE_STATUS)




# @mod_about.route('/yakub-sheikh/')
# @mod_about.route('/about/yakub-sheikh/')
# @mod_about.route('/about/leadership/')
# def yakub_sheikh():
#     return redirect(url_for('mod_about.leadership'))
#


