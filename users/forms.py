from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms 

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True,widget=forms.EmailInput(attrs ={"class":"mx-6 border-2 border-gray-300 focus:bg-gray-200 pl-2 rounded-lg text-xl w-[250px] h-[28px]","placeholder":"gmail@gmai.com"}))
    username = forms.CharField(required=True,widget=forms.TextInput(attrs ={"class":"mx-6 border-2 border-gray-300 focus:bg-gray-200 pl-2 rounded-lg text-xl w-[250px] h-[28px]","placeholder":"enter username"}))
    password1 = forms.Field(required=True,widget=forms.PasswordInput(attrs ={"class":"mx-6 border-2 border-gray-300 focus:bg-gray-200 pl-2 rounded-lg text-xl w-[250px] h-[28px]","placeholder":"enter password"}))
    password2 = forms.CharField(required=True,widget=forms.PasswordInput(attrs ={"class":"mx-6 border-2 border-gray-300 focus:bg-gray-200 pl-2 rounded-lg text-xl w-[250px] h-[28px]","placeholder":"enter password"}))


    class Meta:
        model = User
        fields = ("username","email","password1","password2")
    

    # def save(self,commit=True):
    #     user = super(NewUserForm,self).save(commit=False)
    #     user.email = self.cleaned_data['email']
    #     if commit:
    #         user.save()

