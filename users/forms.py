from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import UserModel


class CustomUserCreationForm(UserCreationForm):
    mobile_no = forms.IntegerField(required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'mobile_no', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        # self.fields['email'].required = True
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

    def save(self, commit=True):
        if not commit:
            raise NotImplementedError(
                "Can't create User and UserProfile without database save")
        user = super(CustomUserCreationForm, self).save(commit=True)
        user_model = UserModel(
            user=user, mobile_no=self.cleaned_data['mobile_no'])
        user_model.save()
        return user, user_model
