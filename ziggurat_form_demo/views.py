from pyramid.i18n import TranslationStringFactory
from pyramid.view import view_config
from ziggurat_form.form import ZigguratForm
from .test_schemas import UserSchema, PhonesSchema, UserLoginSchema, UserRegisterSchema
import pprint

_ = TranslationStringFactory('ziggurat_form_demo')


@view_config(route_name='/', renderer='index.jinja2')
def index(request):
    return {}


@view_config(route_name='forms', match_param='view=user_login_form', renderer='form_page.jinja2')
def user_login_form(request):
    form = ZigguratForm(UserLoginSchema)
    if request.method == 'POST':
        form.set_data(request.POST)
        form.validate()
    return {"form": form}

@view_config(route_name='forms', match_param='view=user_register_form', renderer='form_page.jinja2')
def user_register_form(request):
    form = ZigguratForm(UserRegisterSchema)
    if request.method == 'POST':
        form.set_data(request.POST)
        form.validate()
    return {"form": form}

@view_config(route_name='forms', match_param='view=basic_form', renderer='form_page.jinja2')
def basic_form(request):
    data = {'password': 'xx', "phones": [{}], "subperson": {}, "user_name": "us"}

    form = ZigguratForm(UserSchema)
    if request.method == 'POST':
        form.set_data(request.POST)
        form.validate()
    else:
        form.set_data(data)

    return {"form": form}


@view_config(route_name='forms', match_param='view=phones_form', renderer='form_page.jinja2')
def phones_form(request):
    form = ZigguratForm(PhonesSchema)

    data = {
        "prefix": 1,
        "aaaa": "bbbb",
        "phones": [{'number': '1', 'location': 'dadada'},
                   {'y': 5},
                   {'number': 'abc'},
                   {},
                   {'location': 'warsaw', 'number': 123}],
        "suffix": "bla"
    }

    if request.method == 'POST':
        form.set_data(request.POST)
        form.validate()
    else:
        form.set_data(data)
    return {"form": form}
