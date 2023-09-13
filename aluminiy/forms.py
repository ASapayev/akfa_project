from django import forms
from .models import AluFile,LengthOfProfile,ExchangeValues


class FileForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
      super(FileForm, self).__init__(*args, **kwargs)
      self.fields['file'].widget.attrs.update({
          'class': 'form-control-file'
      })
  class Meta:
    model =AluFile
    fields =['file','file_type']

class LengthOfProfilwForm(forms.ModelForm):
  class Meta:
    model = LengthOfProfile
    fields ='__all__'


class ExchangeValueForm(forms.ModelForm):
  class Meta:
    model = ExchangeValues
    fields ='__all__'