from flask import Blueprint, render_template
from config_industry import *

mod_service = Blueprint('mod_service', __name__, url_prefix='')


@mod_service.route('/automotive/')
def automotive():
    return render_template('service/service_1.html',
                           title=AUTOMOTIVE_TITLE,
                           description=AUTOMOTIVE_DESCRIPTION,
                           keywords=AUTOMOTIVE_KEYWORDS,

                           heading_1=AUTOMOTIVE_HEADING_1,
                           image_1=AUTOMOTIVE_IMAGE_1,
                           alt_text_1=AUTOMOTIVE_ALT_TEXT_1,
                           para_1=AUTOMOTIVE_PARA_1,

                           heading_2=AUTOMOTIVE_HEADING_2,
                           image_2=AUTOMOTIVE_IMAGE_2,
                           alt_text_2=AUTOMOTIVE_ALT_TEXT_2,
                           para_2=AUTOMOTIVE_PARA_2,

                           heading_3=AUTOMOTIVE_HEADING_3,
                           features_3=AUTOMOTIVE_FEATURES_3,

                           heading_4=AUTOMOTIVE_HEADING_4,
                           features_4=AUTOMOTIVE_FEATURES_4,

                           active_menu=ACTIVE_STATUS)

@mod_service.route('/healthcare/')
def healthcare():
    return render_template('service/service_1.html',
                           title=HEALTHCARE_TITLE,
                           description=HEALTHCARE_DESCRIPTION,
                           keywords=HEALTHCARE_KEYWORDS,

                           heading_1=HEALTHCARE_HEADING_1,
                           image_1=HEALTHCARE_IMAGE_1,
                           alt_text_1=HEALTHCARE_ALT_TEXT_1,
                           para_1=HEALTHCARE_PARA_1,

                           heading_2=HEALTHCARE_HEADING_2,
                           image_2=HEALTHCARE_IMAGE_2,
                           alt_text_2=HEALTHCARE_ALT_TEXT_2,
                           para_2=HEALTHCARE_PARA_2,

                           heading_3=HEALTHCARE_HEADING_3,
                           features_3=HEALTHCARE_FEATURES_3,

                           heading_4=HEALTHCARE_HEADING_4,
                           features_4=HEALTHCARE_FEATURES_4,

                           active_menu=ACTIVE_STATUS)

@mod_service.route('/education/')
def education():
    return render_template('service/service_1.html',
                           title=EDUCATION_TITLE,
                           description=EDUCATION_DESCRIPTION,
                           keywords=EDUCATION_KEYWORDS,

                           heading_1=EDUCATION_HEADING_1,
                           image_1=EDUCATION_IMAGE_1,
                           alt_text_1=EDUCATION_ALT_TEXT_1,
                           para_1=EDUCATION_PARA_1,

                           heading_2=EDUCATION_HEADING_2,
                           image_2=EDUCATION_IMAGE_2,
                           alt_text_2=EDUCATION_ALT_TEXT_2,
                           para_2=EDUCATION_PARA_2,

                           heading_3=EDUCATION_HEADING_3,
                           features_3=EDUCATION_FEATURES_3,

                           heading_4=EDUCATION_HEADING_4,
                           features_4=EDUCATION_FEATURES_4,

                           active_menu=ACTIVE_STATUS)

@mod_service.route('/hotel-food-industry/')
def hotel_food_industry():
    return render_template('service/service_1.html',
                           title=HOTEL_TITLE,
                           description=HOTEL_DESCRIPTION,
                           keywords=HOTEL_KEYWORDS,

                           heading_1=HOTEL_HEADING_1,
                           image_1=HOTEL_IMAGE_1,
                           alt_text_1=HOTEL_ALT_TEXT_1,
                           para_1=HOTEL_PARA_1,

                           heading_2=HOTEL_HEADING_2,
                           image_2=HOTEL_IMAGE_2,
                           alt_text_2=HOTEL_ALT_TEXT_2,
                           para_2=HOTEL_PARA_2,

                           heading_3=HOTEL_HEADING_3,
                           features_3=HOTEL_FEATURES_3,

                           heading_4=HOTEL_HEADING_4,
                           features_4=HOTEL_FEATURES_4,

                           active_menu=ACTIVE_STATUS)

@mod_service.route('/banking/')
def banking():
    return render_template('service/service_1.html',
                           title=BANKING_TITLE,
                           description=BANKING_DESCRIPTION,
                           keywords=BANKING_KEYWORDS,

                           heading_1=BANKING_HEADING_1,
                           image_1=BANKING_IMAGE_1,
                           alt_text_1=BANKING_ALT_TEXT_1,
                           para_1=BANKING_PARA_1,

                           heading_2=BANKING_HEADING_2,
                           image_2=BANKING_IMAGE_2,
                           alt_text_2=BANKING_ALT_TEXT_2,
                           para_2=BANKING_PARA_2,

                           heading_3=BANKING_HEADING_3,
                           features_3=BANKING_FEATURES_3,

                           heading_4=BANKING_HEADING_4,
                           features_4=BANKING_FEATURES_4,

                           active_menu=ACTIVE_STATUS)

@mod_service.route('/insurance/')
def insurance():
    return render_template('service/service_1.html',
                           title=INSURANCE_TITLE,
                           description=INSURANCE_DESCRIPTION,
                           keywords=INSURANCE_KEYWORDS,

                           heading_1=INSURANCE_HEADING_1,
                           image_1=INSURANCE_IMAGE_1,
                           alt_text_1=INSURANCE_ALT_TEXT_1,
                           para_1=INSURANCE_PARA_1,

                           heading_2=INSURANCE_HEADING_2,
                           image_2=INSURANCE_IMAGE_2,
                           alt_text_2=INSURANCE_ALT_TEXT_2,
                           para_2=INSURANCE_PARA_2,

                           heading_3=INSURANCE_HEADING_3,
                           features_3=INSURANCE_FEATURES_3,

                           heading_4=INSURANCE_HEADING_4,
                           features_4=INSURANCE_FEATURES_4,

                           active_menu=ACTIVE_STATUS)

@mod_service.route('/lifescience/')
def lifescience():
    return render_template('service/service_1.html',
                           title=LIFESCIENCE_TITLE,
                           description=LIFESCIENCE_DESCRIPTION,
                           keywords=LIFESCIENCE_KEYWORDS,

                           heading_1=LIFESCIENCE_HEADING_1,
                           image_1=LIFESCIENCE_IMAGE_1,
                           alt_text_1=LIFESCIENCE_ALT_TEXT_1,
                           para_1=LIFESCIENCE_PARA_1,

                           heading_2=LIFESCIENCE_HEADING_2,
                           image_2=LIFESCIENCE_IMAGE_2,
                           alt_text_2=LIFESCIENCE_ALT_TEXT_2,
                           para_2=LIFESCIENCE_PARA_2,

                           heading_3=LIFESCIENCE_HEADING_3,
                           features_3=LIFESCIENCE_FEATURES_3,

                           heading_4=LIFESCIENCE_HEADING_4,
                           features_4=LIFESCIENCE_FEATURES_4,

                           active_menu=ACTIVE_STATUS)

@mod_service.route('/logistics/')
def logistics():
    return render_template('service/service_1.html',
                           title=LOGISTIC_TITLE,
                           description=LOGISTIC_DESCRIPTION,
                           keywords=LOGISTIC_KEYWORDS,

                           heading_1=LOGISTIC_HEADING_1,
                           image_1=LOGISTIC_IMAGE_1,
                           alt_text_1=LOGISTIC_ALT_TEXT_1,
                           para_1=LOGISTIC_PARA_1,

                           heading_2=LOGISTIC_HEADING_2,
                           image_2=LOGISTIC_IMAGE_2,
                           alt_text_2=LOGISTIC_ALT_TEXT_2,
                           para_2=LOGISTIC_PARA_2,

                           heading_3=LOGISTIC_HEADING_3,
                           features_3=LOGISTIC_FEATURES_3,

                           heading_4=LOGISTIC_HEADING_4,
                           features_4=LOGISTIC_FEATURES_4,

                           active_menu=ACTIVE_STATUS)

@mod_service.route('/manufacturing/')
def manufacturing():
    return render_template('service/service_1.html',
                           title=MANUFACTURING_TITLE,
                           description=MANUFACTURING_DESCRIPTION,
                           keywords=MANUFACTURING_KEYWORDS,

                           heading_1=MANUFACTURING_HEADING_1,
                           image_1=MANUFACTURING_IMAGE_1,
                           alt_text_1=MANUFACTURING_ALT_TEXT_1,
                           para_1=MANUFACTURING_PARA_1,

                           heading_2=MANUFACTURING_HEADING_2,
                           image_2=MANUFACTURING_IMAGE_2,
                           alt_text_2=MANUFACTURING_ALT_TEXT_2,
                           para_2=MANUFACTURING_PARA_2,

                           heading_3=MANUFACTURING_HEADING_3,
                           features_3=MANUFACTURING_FEATURES_3,

                           heading_4=MANUFACTURING_HEADING_4,
                           features_4=MANUFACTURING_FEATURES_4,

                           active_menu=ACTIVE_STATUS)

@mod_service.route('/media/')
def media():
    return render_template('service/service_1.html',
                           title=MEDIA_TITLE,
                           description=MEDIA_DESCRIPTION,
                           keywords=MEDIA_KEYWORDS,

                           heading_1=MEDIA_HEADING_1,
                           image_1=MEDIA_IMAGE_1,
                           alt_text_1=MEDIA_ALT_TEXT_1,
                           para_1=MEDIA_PARA_1,

                           heading_2=MEDIA_HEADING_2,
                           image_2=MEDIA_IMAGE_2,
                           alt_text_2=MEDIA_ALT_TEXT_2,
                           para_2=MEDIA_PARA_2,

                           heading_3=MEDIA_HEADING_3,
                           features_3=MEDIA_FEATURES_3,

                           heading_4=MEDIA_HEADING_4,
                           features_4=MEDIA_FEATURES_4,

                           active_menu=ACTIVE_STATUS)

@mod_service.route('/government/')
def government():
    return render_template('service/service_1.html',
                           title=GOVERNMENT_TITLE,
                           description=GOVERNMENT_DESCRIPTION,
                           keywords=GOVERNMENT_KEYWORDS,

                           heading_1=GOVERNMENT_HEADING_1,
                           image_1=GOVERNMENT_IMAGE_1,
                           alt_text_1=GOVERNMENT_ALT_TEXT_1,
                           para_1=GOVERNMENT_PARA_1,

                           heading_2=GOVERNMENT_HEADING_2,
                           image_2=GOVERNMENT_IMAGE_2,
                           alt_text_2=GOVERNMENT_ALT_TEXT_2,
                           para_2=GOVERNMENT_PARA_2,

                           heading_3=GOVERNMENT_HEADING_3,
                           features_3=GOVERNMENT_FEATURES_3,

                           heading_4=GOVERNMENT_HEADING_4,
                           features_4=GOVERNMENT_FEATURES_4,

                           active_menu=ACTIVE_STATUS)

@mod_service.route('/retail/')
def retail():
    return render_template('service/service_1.html',
                           title=RETAIL_TITLE,
                           description=RETAIL_DESCRIPTION,
                           keywords=RETAIL_KEYWORDS,

                           heading_1=RETAIL_HEADING_1,
                           image_1=RETAIL_IMAGE_1,
                           alt_text_1=RETAIL_ALT_TEXT_1,
                           para_1=RETAIL_PARA_1,

                           heading_2=RETAIL_HEADING_2,
                           image_2=RETAIL_IMAGE_2,
                           alt_text_2=RETAIL_ALT_TEXT_2,
                           para_2=RETAIL_PARA_2,

                           heading_3=RETAIL_HEADING_3,
                           features_3=RETAIL_FEATURES_3,

                           heading_4=RETAIL_HEADING_4,
                           features_4=RETAIL_FEATURES_4,

                           active_menu=ACTIVE_STATUS)

@mod_service.route('/nonprofit/')
def nonprofit():
    return render_template('service/service_1.html',
                           title=NON_PROFIT_TITLE,
                           description=NON_PROFIT_DESCRIPTION,
                           keywords=NON_PROFIT_KEYWORDS,

                           heading_1=NON_PROFIT_HEADING_1,
                           image_1=NON_PROFIT_IMAGE_1,
                           alt_text_1=NON_PROFIT_ALT_TEXT_1,
                           para_1=NON_PROFIT_PARA_1,

                           heading_2=NON_PROFIT_HEADING_2,
                           image_2=NON_PROFIT_IMAGE_2,
                           alt_text_2=NON_PROFIT_ALT_TEXT_2,
                           para_2=NON_PROFIT_PARA_2,

                           heading_3=NON_PROFIT_HEADING_3,
                           features_3=NON_PROFIT_FEATURES_3,

                           heading_4=NON_PROFIT_HEADING_4,
                           features_4=NON_PROFIT_FEATURES_4,

                           active_menu=ACTIVE_STATUS)

@mod_service.route('/telecommunications/')
def telecommunications():
    return render_template('service/service_1.html',
                           title=TELECOM_TITLE,
                           description=TELECOM_DESCRIPTION,
                           keywords=TELECOM_KEYWORDS,

                           heading_1=TELECOM_HEADING_1,
                           image_1=TELECOM_IMAGE_1,
                           alt_text_1=TELECOM_ALT_TEXT_1,
                           para_1=TELECOM_PARA_1,

                           heading_2=TELECOM_HEADING_2,
                           image_2=TELECOM_IMAGE_2,
                           alt_text_2=TELECOM_ALT_TEXT_2,
                           para_2=TELECOM_PARA_2,

                           heading_3=TELECOM_HEADING_3,
                           features_3=TELECOM_FEATURES_3,

                           heading_4=TELECOM_HEADING_4,
                           features_4=TELECOM_FEATURES_4,

                           active_menu=ACTIVE_STATUS)