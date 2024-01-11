from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from accounts.forms import RegistrationForm
# Create your tests here.
class TestAccountsForm(TestCase):
    def test_accounts_form_with_vaild_data(self):
        form = RegistrationForm(data={
            'username':"reza72rg",
            'password1':'123456789ab',
            'password2':'123456789ab',
        })
        self.assertTrue(form.is_valid())
    
    def test_accounts_form_with_no_data(self):
        form = RegistrationForm(data={})
        self.assertFalse(form.is_valid())