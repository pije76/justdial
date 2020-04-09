from django import forms
from django.urls import reverse
from django.utils.translation import ugettext as _

from allauth.account.forms import LoginForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field
from crispy_forms.bootstrap import FormActions

from .models import User


class MyLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(MyLoginForm, self).__init__(*args, **kwargs)
        self.fields['login'].label = ""
        self.fields['login'].required = False
        self.fields['login'].widget = forms.TextInput()
        self.fields['password'].label = ""
        self.fields['password'].required = False
        self.fields['password'].widget = forms.PasswordInput()

        helper = FormHelper()
        helper.form_show_labels = False
        helper.label_class = 'title_login'
        helper.layout = Layout(
            Field('login', placeholder='Username', id='id_login'),
            Field('password', placeholder='Password', id='id_password'),
            FormActions(
                Submit('submit', 'Login', css_class='btn-primary')
            ),
        )
        self.helper = helper
