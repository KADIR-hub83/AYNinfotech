from flask import Blueprint, render_template
from config_career import *

mod_career = Blueprint('mod_career', __name__, url_prefix='')


@mod_career.route('/careers/machine-learning/')
def aiml():
    return render_template('other/career-detail.html',
                           title=AIML_TITLE,
                           description=AIML_DESCRIPTION,
                           keywords=AIML_KEYWORDS,

                           heading_1=AIML_HEADING_1,
                           image_1=AIML_IMAGE_1,
                           alt_text_1=AIML_ALT_TEXT_1,
                           para_1=AIML_PARA_1,
                           active_menu=ACTIVE_STATUS)

@mod_career.route('/careers/nodejs/')
def nodejs():
    return render_template('other/career-detail.html',
                           title=NODE_TITLE,
                           description=NODE_DESCRIPTION,
                           keywords=NODE_KEYWORDS,

                           heading_1=NODE_HEADING_1,
                           image_1=NODE_IMAGE_1,
                           alt_text_1=NODE_ALT_TEXT_1,
                           para_1=NODE_PARA_1,
                           active_menu=ACTIVE_STATUS)

@mod_career.route('/careers/react-native/')
def react():
    return render_template('other/career-detail.html',
                           title=REACT_TITLE,
                           description=REACT_DESCRIPTION,
                           keywords=REACT_KEYWORDS,

                           heading_1=REACT_HEADING_1,
                           image_1=REACT_IMAGE_1,
                           alt_text_1=REACT_ALT_TEXT_1,
                           para_1=REACT_PARA_1,
                           active_menu=ACTIVE_STATUS)

@mod_career.route('/careers/technical-lead/')
def technical():
    return render_template('other/career-detail.html',
                           title=TECH_TITLE,
                           description=TECH_DESCRIPTION,
                           keywords=TECH_KEYWORDS,

                           heading_1=TECH_HEADING_1,
                           image_1=TECH_IMAGE_1,
                           alt_text_1=TECH_ALT_TEXT_1,
                           para_1=TECH_PARA_1,
                           active_menu=ACTIVE_STATUS)

@mod_career.route('/careers/business-analyst/')
def ba():
    return render_template('other/career-detail.html',
                           title=BUS_TITLE,
                           description=BUS_DESCRIPTION,
                           keywords=BUS_KEYWORDS,

                           heading_1=BUS_HEADING_1,
                           image_1=BUS_IMAGE_1,
                           alt_text_1=BUS_ALT_TEXT_1,
                           para_1=BUS_PARA_1,
                           active_menu=ACTIVE_STATUS)

@mod_career.route('/careers/software-architect/')
def software_arc():
    return render_template('other/career-detail.html',
                           title=SA_TITLE,
                           description=SA_DESCRIPTION,
                           keywords=SA_KEYWORDS,

                           heading_1=SA_HEADING_1,
                           image_1=SA_IMAGE_1,
                           alt_text_1=SA_ALT_TEXT_1,
                           para_1=SA_PARA_1,
                           active_menu=ACTIVE_STATUS)

@mod_career.route('/careers/bdm/')
def bdm():
    return render_template('other/career-detail.html',
                           title=BDM_TITLE,
                           description=BDM_DESCRIPTION,
                           keywords=BDM_KEYWORDS,

                           heading_1=BDM_HEADING_1,
                           image_1=BDM_IMAGE_1,
                           alt_text_1=BDM_ALT_TEXT_1,
                           para_1=BDM_PARA_1,
                           active_menu=ACTIVE_STATUS)

@mod_career.route('/careers/bde/')
def bde():
    return render_template('other/career-detail.html',
                           title=BDE_TITLE,
                           description=BDE_DESCRIPTION,
                           keywords=BDE_KEYWORDS,

                           heading_1=BDE_HEADING_1,
                           image_1=BDE_IMAGE_1,
                           alt_text_1=BDE_ALT_TEXT_1,
                           para_1=BDE_PARA_1,
                           active_menu=ACTIVE_STATUS)

@mod_career.route('/careers/technical-writer/')
def technical_writer():
    return render_template('other/career-detail.html',
                           title=TW_TITLE,
                           description=TW_DESCRIPTION,
                           keywords=TW_KEYWORDS,

                           heading_1=TW_HEADING_1,
                           image_1=TW_IMAGE_1,
                           alt_text_1=TW_ALT_TEXT_1,
                           para_1=TW_PARA_1,
                           active_menu=ACTIVE_STATUS)


@mod_career.route('/careers/blockchain-developer/')
def blockchain_developer():
    return render_template('other/career-detail.html',
                           title=BCD_TITLE,
                           description=BCD_DESCRIPTION,
                           keywords=BCD_KEYWORDS,

                           heading_1=BCD_HEADING_1,
                           image_1=BCD_IMAGE_1,
                           alt_text_1=BCD_ALT_TEXT_1,
                           para_1=BCD_PARA_1,
                           active_menu=ACTIVE_STATUS)

@mod_career.route('/careers/blockchain-architect/')
def blockchain_architect():
    return render_template('other/career-detail.html',
                           title=BASBD_TITLE,
                           description=BASBD_DESCRIPTION,
                           keywords=BASBD_KEYWORDS,

                           heading_1=BASBD_HEADING_1,
                           image_1=BASBD_IMAGE_1,
                           alt_text_1=BASBD_ALT_TEXT_1,
                           para_1=BASBD_PARA_1,
                           active_menu=ACTIVE_STATUS)

@mod_career.route('/careers/hr-it-recruiter/')
def hr_it_recruiter():
    return render_template('other/career-detail.html',
                           title=HR_TITLE,
                           description=HR_DESCRIPTION,
                           keywords=HR_KEYWORDS,

                           heading_1=HR_HEADING_1,
                           image_1=HR_IMAGE_1,
                           alt_text_1=HR_ALT_TEXT_1,
                           para_1=HR_PARA_1,
                           active_menu=ACTIVE_STATUS)


@mod_career.route('/careers/ui-developer/')
def ui_developer():
    return render_template('other/career-detail.html',
                           title=UI_TITLE,
                           description=UI_DESCRIPTION,
                           keywords=UI_KEYWORDS,

                           heading_1=UI_HEADING_1,
                           image_1=UI_IMAGE_1,
                           alt_text_1=UI_ALT_TEXT_1,
                           para_1=UI_PARA_1,
                           active_menu=ACTIVE_STATUS)


@mod_career.route('/careers/reactjs-developer/')
def reactjs_developer():
    return render_template('other/career-detail.html',
                           title=JS_TITLE,
                           description=JS_DESCRIPTION,
                           keywords=JS_KEYWORDS,

                           heading_1=JS_HEADING_1,
                           image_1=JS_IMAGE_1,
                           alt_text_1=JS_ALT_TEXT_1,
                           para_1=JS_PARA_1,
                           active_menu=ACTIVE_STATUS)


@mod_career.route('/careers/ux-designer/')
def ux_designer():
    return render_template('other/career-detail.html',
                           title=UX_TITLE,
                           description=UX_DESCRIPTION,
                           keywords=UX_KEYWORDS,

                           heading_1=UX_HEADING_1,
                           image_1=UX_IMAGE_1,
                           alt_text_1=UX_ALT_TEXT_1,
                           para_1=UX_PARA_1,
                           active_menu=ACTIVE_STATUS)


@mod_career.route('/careers/angular-developer/')
def angular_developer():
    return render_template('other/career-detail.html',
                           title=AD_TITLE,
                           description=AD_DESCRIPTION,
                           keywords=AD_KEYWORDS,

                           heading_1=AD_HEADING_1,
                           image_1=AD_IMAGE_1,
                           alt_text_1=AD_ALT_TEXT_1,
                           para_1=AD_PARA_1,
                           active_menu=ACTIVE_STATUS)


@mod_career.route('/careers/technical-manager/')
def technical_manager():
    return render_template('other/career-detail.html',
                           title=TM_TITLE,
                           description=TM_DESCRIPTION,
                           keywords=TM_KEYWORDS,

                           heading_1=TM_HEADING_1,
                           image_1=TM_IMAGE_1,
                           alt_text_1=TM_ALT_TEXT_1,
                           para_1=TM_PARA_1,
                           active_menu=ACTIVE_STATUS)


@mod_career.route('/careers/cto/')
def cto():
    return render_template('other/career-detail.html',
                           title=CTO_TITLE,
                           description=CTO_DESCRIPTION,
                           keywords=CTO_KEYWORDS,

                           heading_1=CTO_HEADING_1,
                           image_1=CTO_IMAGE_1,
                           alt_text_1=CTO_ALT_TEXT_1,
                           para_1=CTO_PARA_1,
                           active_menu=ACTIVE_STATUS)


@mod_career.route('/careers/sales-head/')
def sales_head():
    return render_template('other/career-detail.html',
                           title=SALES_TITLE,
                           description=SALES_DESCRIPTION,
                           keywords=SALES_KEYWORDS,

                           heading_1=SALES_HEADING_1,
                           image_1=SALES_IMAGE_1,
                           alt_text_1=SALES_ALT_TEXT_1,
                           para_1=SALES_PARA_1,
                           active_menu=ACTIVE_STATUS)

