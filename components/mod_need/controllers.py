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

@mod_need.route('/digital-transformation/')
def digital_transformation():
    return render_template('service/need.html',
                           title=DT_TITLE,
                           description=DT_DESCRIPTION,
                           keywords=DT_KEYWORDS,

                           heading_1=DT_HEADING_1,
                           image_1=DT_IMAGE_1,
                           alt_text_1=DT_ALT_TEXT_1,
                           para_1=DT_PARA_1,
                           button_1=DT_BUTTON_1,

                           heading_2=DT_HEADING_2,
                           para_2=DT_PARA_2,
                           features_2=DT_FEATURES_2,

                           heading_3=DT_HEADING_3,
                           features_3=DT_FEATURES_3,

                           heading_4=DT_HEADING_4,
                           features_4=DT_FEATURES_4,

                           contact_heading=CONTACT_AYN_HEADING,
                           contact_image=CONTACT_AYN_IMAGE,
                           contact_alt_text=CONTACT_AYN_ALT_TEXT,
                           contact_button=CONTACT_AYN_BUTTON,

                           active_menu=ACTIVE_STATUS)


@mod_need.route('/application-services/')
def application_services():
    return render_template('service/need.html',
                           title=AS_TITLE,
                           description=AS_DESCRIPTION,
                           keywords=AS_KEYWORDS,

                           heading_1=AS_HEADING_1,
                           image_1=AS_IMAGE_1,
                           alt_text_1=AS_ALT_TEXT_1,
                           para_1=AS_PARA_1,
                           button_1=AS_BUTTON_1,

                           heading_2=AS_HEADING_2,
                           para_2=AS_PARA_2,
                           features_2=AS_FEATURES_2,

                           heading_3=AS_HEADING_3,
                           features_3=AS_FEATURES_3,

                           heading_4=AS_HEADING_4,
                           features_4=AS_FEATURES_4,

                           contact_heading=CONTACT_AYN_HEADING,
                           contact_image=CONTACT_AYN_IMAGE,
                           contact_alt_text=CONTACT_AYN_ALT_TEXT,
                           contact_button=CONTACT_AYN_BUTTON,

                           active_menu=ACTIVE_STATUS)


@mod_need.route('/it-infrastructure/')
def it_infrastructure():
    return render_template('service/need.html',
                           title=ITIF_TITLE,
                           description=ITIF_DESCRIPTION,
                           keywords=ITIF_KEYWORDS,

                           heading_1=ITIF_HEADING_1,
                           image_1=ITIF_IMAGE_1,
                           alt_text_1=ITIF_ALT_TEXT_1,
                           para_1=ITIF_PARA_1,
                           button_1=ITIF_BUTTON_1,

                           heading_2=ITIF_HEADING_2,
                           para_2=ITIF_PARA_2,
                           features_2=ITIF_FEATURES_2,

                           heading_3=ITIF_HEADING_3,
                           features_3=ITIF_FEATURES_3,

                           heading_4=ITIF_HEADING_4,
                           features_4=ITIF_FEATURES_4,

                           contact_heading=CONTACT_AYN_HEADING,
                           contact_image=CONTACT_AYN_IMAGE,
                           contact_alt_text=CONTACT_AYN_ALT_TEXT,
                           contact_button=CONTACT_AYN_BUTTON,

                           active_menu=ACTIVE_STATUS)

@mod_need.route('/cloud/')
def cloud():
    return render_template('service/need.html',
                           title=CLOUD_TITLE,
                           description=CLOUD_DESCRIPTION,
                           keywords=CLOUD_KEYWORDS,

                           heading_1=CLOUD_HEADING_1,
                           image_1=CLOUD_IMAGE_1,
                           alt_text_1=CLOUD_ALT_TEXT_1,
                           para_1=CLOUD_PARA_1,
                           button_1=CLOUD_BUTTON_1,

                           heading_2=CLOUD_HEADING_2,
                           para_2=CLOUD_PARA_2,
                           features_2=CLOUD_FEATURES_2,

                           heading_3=CLOUD_HEADING_3,
                           features_3=CLOUD_FEATURES_3,

                           heading_4=CLOUD_HEADING_4,
                           features_4=CLOUD_FEATURES_4,

                           contact_heading=CONTACT_AYN_HEADING,
                           contact_image=CONTACT_AYN_IMAGE,
                           contact_alt_text=CONTACT_AYN_ALT_TEXT,
                           contact_button=CONTACT_AYN_BUTTON,

                           active_menu=ACTIVE_STATUS)

@mod_need.route('/technology-innovation/')
def technology_innovation():
    return render_template('service/need.html',
                           title=TI_TITLE,
                           description=TI_DESCRIPTION,
                           keywords=TI_KEYWORDS,

                           heading_1=TI_HEADING_1,
                           image_1=TI_IMAGE_1,
                           alt_text_1=TI_ALT_TEXT_1,
                           para_1=TI_PARA_1,
                           button_1=TI_BUTTON_1,

                           heading_2=TI_HEADING_2,
                           para_2=TI_PARA_2,
                           features_2=TI_FEATURES_2,

                           heading_3=TI_HEADING_3,
                           features_3=TI_FEATURES_3,

                           heading_4=TI_HEADING_4,
                           features_4=TI_FEATURES_4,

                           contact_heading=CONTACT_AYN_HEADING,
                           contact_image=CONTACT_AYN_IMAGE,
                           contact_alt_text=CONTACT_AYN_ALT_TEXT,
                           contact_button=CONTACT_AYN_BUTTON,

                           active_menu=ACTIVE_STATUS)

