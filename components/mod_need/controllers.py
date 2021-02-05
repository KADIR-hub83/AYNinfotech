from flask import Blueprint, render_template
from config_need import *

mod_need = Blueprint('mod_need', __name__, url_prefix='')


@mod_need.route('/artificial-intelligence/')
def ai():
    return render_template('service/need.html',
                           title=AI_TITLE,
                           description=AI_DESCRIPTION,
                           keywords=AI_KEYWORDS,

                           heading_1=AI_HEADING_1,
                           image_1=AI_IMAGE_1,
                           alt_text_1=AI_ALT_TEXT_1,
                           para_1=AI_PARA_1,
                           button_1=AI_BUTTON_1,

                           heading_2=AI_HEADING_2,
                           para_2=AI_PARA_2,
                           features_2=AI_FEATURES_2,

                           heading_3=AI_HEADING_3,
                           features_3=AI_FEATURES_3,

                           heading_4=AI_HEADING_4,
                           features_4=AI_FEATURES_4,

                           contact_heading=CONTACT_AYN_HEADING,
                           contact_image=CONTACT_AYN_IMAGE,
                           contact_alt_text=CONTACT_AYN_ALT_TEXT,
                           contact_button=CONTACT_AYN_BUTTON,

                           active_menu=ACTIVE_STATUS)


@mod_need.route('/blockchain/')
def blockchain():
    return render_template('service/need.html',
                           title=BLOCKCHAIN_TITLE,
                           description=BLOCKCHAIN_DESCRIPTION,
                           keywords=BLOCKCHAIN_KEYWORDS,

                           heading_1=BLOCKCHAIN_HEADING_1,
                           image_1=BLOCKCHAIN_IMAGE_1,
                           alt_text_1=BLOCKCHAIN_ALT_TEXT_1,
                           para_1=BLOCKCHAIN_PARA_1,
                           button_1=BLOCKCHAIN_BUTTON_1,

                           heading_2=BLOCKCHAIN_HEADING_2,
                           para_2=BLOCKCHAIN_PARA_2,
                           features_2=BLOCKCHAIN_FEATURES_2,

                           heading_3=BLOCKCHAIN_HEADING_3,
                           features_3=BLOCKCHAIN_FEATURES_3,

                           heading_4=BLOCKCHAIN_HEADING_4,
                           features_4=BLOCKCHAIN_FEATURES_4,

                           contact_heading=CONTACT_AYN_HEADING,
                           contact_image=CONTACT_AYN_IMAGE,
                           contact_alt_text=CONTACT_AYN_ALT_TEXT,
                           contact_button=CONTACT_AYN_BUTTON,

                           active_menu=ACTIVE_STATUS)

@mod_need.route('/internet-of-things/')
def iot():
    return render_template('service/need.html',
                           title=IOT_TITLE,
                           description=IOT_DESCRIPTION,
                           keywords=IOT_KEYWORDS,

                           heading_1=IOT_HEADING_1,
                           image_1=IOT_IMAGE_1,
                           alt_text_1=IOT_ALT_TEXT_1,
                           para_1=IOT_PARA_1,
                           button_1=IOT_BUTTON_1,

                           heading_2=IOT_HEADING_2,
                           para_2=IOT_PARA_2,
                           features_2=IOT_FEATURES_2,

                           heading_3=IOT_HEADING_3,
                           features_3=IOT_FEATURES_3,

                           heading_4=IOT_HEADING_4,
                           features_4=IOT_FEATURES_4,

                           contact_heading=CONTACT_AYN_HEADING,
                           contact_image=CONTACT_AYN_IMAGE,
                           contact_alt_text=CONTACT_AYN_ALT_TEXT,
                           contact_button=CONTACT_AYN_BUTTON,

                           active_menu=ACTIVE_STATUS)

@mod_need.route('/analytics/')
def analytics():
    return render_template('service/need.html',
                           title=ANALYTICS_TITLE,
                           description=ANALYTICS_DESCRIPTION,
                           keywords=ANALYTICS_KEYWORDS,

                           heading_1=ANALYTICS_HEADING_1,
                           image_1=ANALYTICS_IMAGE_1,
                           alt_text_1=ANALYTICS_ALT_TEXT_1,
                           para_1=ANALYTICS_PARA_1,
                           button_1=ANALYTICS_BUTTON_1,

                           heading_2=ANALYTICS_HEADING_2,
                           para_2=ANALYTICS_PARA_2,
                           features_2=ANALYTICS_FEATURES_2,

                           heading_3=ANALYTICS_HEADING_3,
                           features_3=ANALYTICS_FEATURES_3,

                           heading_4=ANALYTICS_HEADING_4,
                           features_4=ANALYTICS_FEATURES_4,

                           contact_heading=CONTACT_AYN_HEADING,
                           contact_image=CONTACT_AYN_IMAGE,
                           contact_alt_text=CONTACT_AYN_ALT_TEXT,
                           contact_button=CONTACT_AYN_BUTTON,

                           active_menu=ACTIVE_STATUS)