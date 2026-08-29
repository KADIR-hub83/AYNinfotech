from flask import Blueprint, render_template
from config_product import *
mod_product = Blueprint('mod_product', __name__, url_prefix='')


# Cedar Overview
@mod_product.route('cedar-healthcare/')
def cedar():

    return render_template('product/product.html',
                           title=CEDAR_TITLE,
                           description=CEDAR_DESCRIPTION,
                           keywords=CEDAR_KEYWORDS,

                           heading_1=CEDAR_HEADING_1,
                           image_1=CEDAR_IMAGE_1,
                           alt_text_1=CEDAR_ALT_TEXT_1,
                           para_1=CEDAR_PARA_1,
                           button_1_1=CEDAR_PRODUCT_DOC_BTN_1,
                           button_1_2=CEDAR_DEMO_VID_BTN_1,

                           heading_2=CEDAR_HEADING_2,
                           features_2=CEDAR_FEATURES_2,
                           button_2_1=CEDAR_KNOW_MORE_BTN_2,

                           heading_3=CEDAR_HEADING_3,
                           image_3=CEDAR_IMAGE_3,
                           alt_text_3=CEDAR_ALT_TEXT_3,
                           para_3=CEDAR_PARA_3,
                           features_3=CEDAR_FEATURES_3,

                           heading_4=CEDAR_HEADING_4,
                           image_4=CEDAR_IMAGE_4,
                           alt_text_4=CEDAR_ALT_TEXT_4,
                           para_4=CEDAR_PARA_4,
                           features_4=CEDAR_FEATURES_4,
                           button_4_1=CEDAR_LEARN_MORE_BTN_4,

                           heading_5=CEDAR_HEADING_5,
                           features_5=CEDAR_FEATURES_5,

                           heading_6=CEDAR_HEADING_6,
                           para_6=CEDAR_PARA_6,
                           features_6=CEDAR_FEATURES_6,


                           why_product=WHY_CEDAR,
                           active_menu=ACTIVE_STATUS)

# Cedar- what is
@mod_product.route('/cedar-healthcare/what-is-healthcare')
def what_is_healthcare():
    return render_template('product/what-is.html',
                           title=CEDAR_TITLE_WHATIS,
                           description=CEDAR_DESCRIPTION_WHATIS,
                           keywords=CEDAR_KEYWORDS_WHATIS,

                           heading_1=CEDAR_HEADING_1_WHATIS,
                           image_1=CEDAR_IMAGE_1_WHATIS,
                           alt_text_1=CEDAR_ALT_TEXT_1_WHATIS,
                           para_1=CEDAR_PARA_1_WHATIS,
                           button_1_1=CEDAR_DEMO_VID_BTN_1_WHATIS,

                           heading_2=CEDAR_HEADING_2_WHATIS,
                           para_2=CEDAR_PARA_2_WHATIS,
                           features_2=CEDAR_FEATURES_2_WHATIS,

                           image_3=CEDAR_IMAGE_3_WHATIS,
                           alt_text_3=CEDAR_ALT_TEXT_3_WHATIS,
                           heading_3=CEDAR_HEADING_3_WHATIS,
                           features_3=CEDAR_FEATURES_3_WHATIS,

                           heading_4=CEDAR_HEADING_4_WHATIS,
                           features_4=CEDAR_FEATURES_4_WHATIS,

                           heading_5=CEDAR_HEADING_5_WHATIS,
                           title_5=CEDAR_TITLE_5_WHATIS,
                           para_5=CEDAR_PARA_5_WHATIS,

                            active_menu=ACTIVE_STATUS)


@mod_product.route('/cedar-healthcare/features')
def cedar_features():
    return render_template('product/features.html',
                           title=CEDAR_TITLE_FEATURE,
                           description=CEDAR_DESCRIPTION_FEATURE,
                           keywords=CEDAR_KEYWORDS_FEATURE,

                           heading_1=CEDAR_HEADING_1_FEATURE,
                           image_1=CEDAR_IMAGE_1_FEATURE,
                           alt_text_1=CEDAR_ALT_TEXT_1_FEATURE,
                           para_1=CEDAR_PARA_1_FEATURE,
                           button_1_1=CEDAR_PRODUCT_DOC_BTN_1_FEATURE,

                           heading_2=CEDAR_HEADING_2_FEATURE,
                           features_2=CEDAR_FEATURES_2_FEATURE,

                           active_menu=ACTIVE_STATUS)


# Pine overview
@mod_product.route('pine-customer-relationship-management/')
def pine():
    return render_template('product/product.html',
                           title=PINE_TITLE,
                           description=PINE_DESCRIPTION,
                           keywords=PINE_KEYWORDS,

                           heading_1=PINE_HEADING_1,
                           image_1=PINE_IMAGE_1,
                           alt_text_1=PINE_ALT_TEXT_1,
                           para_1=PINE_PARA_1,
                           button_1_1=PINE_PRODUCT_DOC_BTN_1,
                           button_1_2 = PINE_DEMO_VID_BTN_1,

                           heading_2=PINE_HEADING_2,
                           features_2=PINE_FEATURES_2,
                           button_2_1=PINE_KNOW_MORE_BTN_2,

                           heading_3=PINE_HEADING_3,
                           image_3=PINE_IMAGE_3,
                           alt_text_3=PINE_ALT_TEXT_3,
                           para_3=PINE_PARA_3,
                           features_3=PINE_FEATURES_3,

                           heading_4=PINE_HEADING_4,
                           image_4=PINE_IMAGE_4,
                           alt_text_4=PINE_ALT_TEXT_4,
                           para_4=PINE_PARA_4,
                           features_4=PINE_FEATURES_4,
                           button_4_1=PINE_LEARN_MORE_BTN_4,

                           heading_5=PINE_HEADING_5,
                           features_5=PINE_FEATURES_5,

                           heading_6=PINE_HEADING_6,
                           para_6=PINE_PARA_6,
                           features_6=PINE_FEATURES_6,

                           why_product=WHY_PINE,
                           active_menu=ACTIVE_STATUS)

#Pine what is
@mod_product.route('/pine-customer-relationship-management/what-is-crm')
def what_is_crm():
    return render_template('product/what-is.html',
                           title=PINE_TITLE_WHATIS,
                           description=PINE_DESCRIPTION_WHATIS,
                           keywords=PINE_KEYWORDS_WHATIS,

                           heading_1=PINE_HEADING_1_WHATIS,
                           image_1=PINE_IMAGE_1_WHATIS,
                           alt_text_1=PINE_ALT_TEXT_1_WHATIS,
                           para_1=PINE_PARA_1_WHATIS,
                           button_1_1=PINE_DEMO_VID_BTN_1_WHATIS,

                           heading_2=PINE_HEADING_2_WHATIS,
                           para_2=PINE_PARA_2_WHATIS,
                           features_2=PINE_FEATURES_2_WHATIS,

                           image_3=PINE_IMAGE_3_WHATIS,
                           alt_text_3=PINE_ALT_TEXT_3_WHATIS,
                           heading_3=PINE_HEADING_3_WHATIS,
                           features_3=PINE_FEATURES_3_WHATIS,

                           heading_4=PINE_HEADING_4_WHATIS,
                           features_4=PINE_FEATURES_4_WHATIS,

                           heading_5=PINE_HEADING_5_WHATIS,
                           title_5=PINE_TITLE_5_WHATIS,
                           para_5=PINE_PARA_5_WHATIS,

                           active_menu=ACTIVE_STATUS)

@mod_product.route('/pine-customer-relationship-management/features')
def pine_features():
    return render_template('product/features.html',
                           title=PINE_TITLE_FEATURE,
                           description=PINE_DESCRIPTION_FEATURE,
                           keywords=PINE_KEYWORDS_FEATURE,

                           heading_1=PINE_HEADING_1_FEATURE,
                           image_1=PINE_IMAGE_1_FEATURE,
                           alt_text_1=PINE_ALT_TEXT_1_FEATURE,
                           para_1=PINE_PARA_1_FEATURE,
                           button_1_1=PINE_PRODUCT_DOC_BTN_1_FEATURE,

                           heading_2=PINE_HEADING_2_FEATURE,
                           features_2=PINE_FEATURES_2_FEATURE,

                           active_menu=ACTIVE_STATUS)


#Walnut overview
@mod_product.route('walnut-enterprise-resource-planning/')
def walnut():
    return render_template('product/product.html',
                           title=WALNUT_TITLE,
                           description=WALNUT_DESCRIPTION,
                           keywords=WALNUT_KEYWORDS,

                           heading_1=WALNUT_HEADING_1,
                           image_1=WALNUT_IMAGE_1,
                           alt_text_1=WALNUT_ALT_TEXT_1,
                           para_1=WALNUT_PARA_1,
                           button_1_1=WALNUT_PRODUCT_DOC_BTN_1,
                           button_1_2 = WALNUT_DEMO_VID_BTN_1,

                           heading_2=WALNUT_HEADING_2,
                           features_2=WALNUT_FEATURES_2,
                           button_2_1=WALNUT_KNOW_MORE_BTN_2,

                           heading_3=WALNUT_HEADING_3,
                           image_3=WALNUT_IMAGE_3,
                           alt_text_3=WALNUT_ALT_TEXT_3,
                           para_3=WALNUT_PARA_3,
                           features_3=WALNUT_FEATURES_3,

                           heading_4=WALNUT_HEADING_4,
                           image_4=WALNUT_IMAGE_4,
                           alt_text_4=WALNUT_ALT_TEXT_4,
                           para_4=WALNUT_PARA_4,
                           features_4=WALNUT_FEATURES_4,
                           button_4_1=WALNUT_LEARN_MORE_BTN_4,

                           heading_5=WALNUT_HEADING_5,
                           features_5=WALNUT_FEATURES_5,

                           heading_6=WALNUT_HEADING_6,
                           para_6=WALNUT_PARA_6,
                           features_6=WALNUT_FEATURES_6,

                           why_product=WHY_WALNUT,
                           active_menu=ACTIVE_STATUS)

#walnut what is
@mod_product.route('/walnut-enterprise-resource-planning/what-is-erp')
def what_is_erp():
    return render_template('product/what-is.html',
                           title=WALNUT_TITLE_WHATIS,
                           description=WALNUT_DESCRIPTION_WHATIS,
                           keywords=WALNUT_KEYWORDS_WHATIS,

                           heading_1=WALNUT_HEADING_1_WHATIS,
                           image_1=WALNUT_IMAGE_1_WHATIS,
                           alt_text_1=WALNUT_ALT_TEXT_1_WHATIS,
                           para_1=WALNUT_PARA_1_WHATIS,
                           button_1_1=WALNUT_DEMO_VID_BTN_1_WHATIS,

                           heading_2=WALNUT_HEADING_2_WHATIS,
                           para_2=WALNUT_PARA_2_WHATIS,
                           features_2=WALNUT_FEATURES_2_WHATIS,

                           image_3=WALNUT_IMAGE_3_WHATIS,
                           alt_text_3=WALNUT_ALT_TEXT_3_WHATIS,
                           heading_3=WALNUT_HEADING_3_WHATIS,
                           features_3=WALNUT_FEATURES_3_WHATIS,

                           heading_4=WALNUT_HEADING_4_WHATIS,
                           features_4=WALNUT_FEATURES_4_WHATIS,

                           heading_5=WALNUT_HEADING_5_WHATIS,
                           title_5=WALNUT_TITLE_5_WHATIS,
                           para_5=WALNUT_PARA_5_WHATIS,

                           active_menu=ACTIVE_STATUS)


@mod_product.route('/walnut-enterprise-resource-planning/features')
def walnut_features():
    return render_template('product/features.html',
                           title=WALNUT_TITLE_FEATURE,
                           description=WALNUT_DESCRIPTION_FEATURE,
                           keywords=WALNUT_KEYWORDS_FEATURE,

                           heading_1=WALNUT_HEADING_1_FEATURE,
                           image_1=WALNUT_IMAGE_1_FEATURE,
                           alt_text_1=WALNUT_ALT_TEXT_1_FEATURE,
                           para_1=WALNUT_PARA_1_FEATURE,
                           button_1_1=WALNUT_PRODUCT_DOC_BTN_1_FEATURE,

                           heading_2=WALNUT_HEADING_2_FEATURE,
                           features_2=WALNUT_FEATURES_2_FEATURE,

                           active_menu=ACTIVE_STATUS)


#oak Overview
@mod_product.route('oak-core-banking-solution/')
def oak():
    return render_template('product/product.html',
                           title=OAK_TITLE,
                           description=OAK_DESCRIPTION,
                           keywords=OAK_KEYWORDS,

                           heading_1=OAK_HEADING_1,
                           image_1=OAK_IMAGE_1,
                           alt_text_1=OAK_ALT_TEXT_1,
                           para_1=OAK_PARA_1,
                           button_1_1=OAK_PRODUCT_DOC_BTN_1,
                           button_1_2 = OAK_DEMO_VID_BTN_1,

                           heading_2=OAK_HEADING_2,
                           features_2=OAK_FEATURES_2,
                           button_2_1=OAK_KNOW_MORE_BTN_2,

                           heading_3=OAK_HEADING_3,
                           image_3=OAK_IMAGE_3,
                           alt_text_3=OAK_ALT_TEXT_3,
                           para_3=OAK_PARA_3,
                           features_3=OAK_FEATURES_3,

                           heading_4=OAK_HEADING_4,
                           image_4=OAK_IMAGE_4,
                           alt_text_4=OAK_ALT_TEXT_4,
                           para_4=OAK_PARA_4,
                           features_4=OAK_FEATURES_4,
                           button_4_1=OAK_LEARN_MORE_BTN_4,

                           heading_5=OAK_HEADING_5,
                           features_5=OAK_FEATURES_5,

                           heading_6=OAK_HEADING_6,
                           para_6=OAK_PARA_6,
                           features_6=OAK_FEATURES_6,

                           why_product=WHY_OAK,
                           active_menu=ACTIVE_STATUS)

#oak what is
@mod_product.route('/oak-core-banking-solution/what-is-cbs')
def what_is_cbs():
    return render_template('product/what-is.html',
                           title=OAK_TITLE_WHATIS,
                           description=OAK_DESCRIPTION_WHATIS,
                           keywords=OAK_KEYWORDS_WHATIS,

                           heading_1=OAK_HEADING_1_WHATIS,
                           image_1=OAK_IMAGE_1_WHATIS,
                           alt_text_1=OAK_ALT_TEXT_1_WHATIS,
                           para_1=OAK_PARA_1_WHATIS,
                           button_1_1=OAK_DEMO_VID_BTN_1_WHATIS,

                           heading_2=OAK_HEADING_2_WHATIS,
                           para_2=OAK_PARA_2_WHATIS,
                           features_2=OAK_FEATURES_2_WHATIS,

                           image_3=OAK_IMAGE_3_WHATIS,
                           alt_text_3=OAK_ALT_TEXT_3_WHATIS,
                           heading_3=OAK_HEADING_3_WHATIS,
                           features_3=OAK_FEATURES_3_WHATIS,

                           heading_4=OAK_HEADING_4_WHATIS,
                           features_4=OAK_FEATURES_4_WHATIS,

                           heading_5=OAK_HEADING_5_WHATIS,
                           title_5=OAK_TITLE_5_WHATIS,
                           para_5=OAK_PARA_5_WHATIS,

                           active_menu=ACTIVE_STATUS)


@mod_product.route('/oak-core-banking-solution/features')
def oak_features():
    return render_template('product/features.html',
                           title=OAK_TITLE_FEATURE,
                           description=OAK_DESCRIPTION_FEATURE,
                           keywords=OAK_KEYWORDS_FEATURE,

                           heading_1=OAK_HEADING_1_FEATURE,
                           image_1=OAK_IMAGE_1_FEATURE,
                           alt_text_1=OAK_ALT_TEXT_1_FEATURE,
                           para_1=OAK_PARA_1_FEATURE,
                           button_1_1=OAK_PRODUCT_DOC_BTN_1_FEATURE,

                           heading_2=OAK_HEADING_2_FEATURE,
                           features_2=OAK_FEATURES_2_FEATURE,

                           active_menu=ACTIVE_STATUS)

