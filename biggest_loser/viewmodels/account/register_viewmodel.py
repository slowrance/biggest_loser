from pyramid.request import Request

from biggest_loser.viewmodels.shared.viewmodel_base import ViewModelBase


class RegisterViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)

        self.fname = self.request_dict.fname
        self.lname = self.request_dict.lname
        self.code_name = self.request_dict.code_name
        self.email = self.request_dict.email
        self.password = self.request_dict.password

        if self.email:
            self.email = self.email.lower().strip()

    def validate(self):
        if not self.fname:
            self.error = 'You must specify a first name'
        if not self.lname:
            self.error = 'You must specify a last name'
        if not self.code_name:
            self.error = 'You must specify a code name'
        if not self.email:
            self.error = 'You must specify an email address'
        if not self.password:
            self.error = 'You must specify a password'
