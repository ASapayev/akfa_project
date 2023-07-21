from django import forms
from .models import User,UserProfile

class AccountForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
      super(AccountForm, self).__init__(*args, **kwargs)
      self.fields['first_name'].widget.attrs.update({
          'class': 'form-control'
      })
      self.fields['username'].widget.attrs.update({
          'class': 'form-control'
      })
      self.fields['email'].widget.attrs.update({
          'class': 'form-control'
      })
      self.fields['last_name'].widget.attrs.update({
          'class': 'form-control'
      })
      self.fields['phone_number'].widget.attrs.update({
          'class': 'form-control'
      })
  class Meta:
    model = User
    fields =['first_name','username','email','last_name','phone_number']

class UserProfileForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
      super(UserProfileForm, self).__init__(*args, **kwargs)
      self.fields['profile_picture'].widget.attrs.update({
          'class': 'form-control'
      })
      self.fields['address'].widget.attrs.update({
          'class': 'form-control'
      })
      self.fields['country'].widget.attrs.update({
          'class': 'form-control'
      })
      self.fields['state'].widget.attrs.update({
          'class': 'form-control'
      })
      self.fields['city'].widget.attrs.update({
          'class': 'form-control'
      })
      self.fields['pin_code'].widget.attrs.update({
          'class': 'form-control'
      })
      self.fields['latitude'].widget.attrs.update({
          'class': 'form-control'
      })
      self.fields['longitute'].widget.attrs.update({
          'class': 'form-control'
      })
  class Meta:
    model = UserProfile
    fields =['profile_picture','address','country','state','city','pin_code','latitude','longitute']