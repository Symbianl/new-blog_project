from django.contrib.auth.forms import UserCreationForm
from blog.models import User

class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
       model = User
       fields = ('username','first_name','last_name','email',)