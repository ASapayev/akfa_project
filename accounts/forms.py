from django import forms
from .models import User

class AccountForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
      super(AccountForm, self).__init__(*args, **kwargs)
      self.fields['file'].widget.attrs.update({
          'class': 'form-control-file'
      })
  class Meta:
    model = User
    fields =['username','email']