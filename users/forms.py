#  -*- coding:utf-8 -*-
from django.contrib.auth.forms import UserCreationForm
from blog.models import User

class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
       model = User
       fields = ('username','first_name','last_name','email',)

    def clean(self):
        cleaned_data = super(RegisterForm,self).clean()
        email =cleaned_data.get('email')
        db_email = User.objects.filter(email=email)
        if email in [email.email for email in db_email]:
            self._errors['email'] = self.error_class([u'邮箱以存在，请换一个'])

            return cleaned_data