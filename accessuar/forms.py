from django import forms
from .models import AccessuarFiles,Siryo


class AccessuarFileForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
      super(AccessuarFileForm, self).__init__(*args, **kwargs)
      self.fields['file'].widget.attrs.update({
          'class': 'form-control-file'
      })
  class Meta:
    model = AccessuarFiles
    fields =['file','type']


