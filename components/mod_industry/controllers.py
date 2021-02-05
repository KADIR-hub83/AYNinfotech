from flask import Blueprint, render_template
from config_industry import *

mod_industry = Blueprint('mod_industry', __name__, url_prefix='/industry')
