from django import forms
from .models import OnlineSavdoFile


class FileForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
      super(FileForm, self).__init__(*args, **kwargs)
      self.fields['file'].widget.attrs.update({
          'class': 'form-control-file'
      })
  class Meta:
    model =OnlineSavdoFile
    fields =['file','file_type']

class FileForm2(forms.ModelForm):
  def __init__(self, *args, **kwargs):
      super(FileForm2, self).__init__(*args, **kwargs)
      self.fields['file'].widget.attrs.update({
          'class': 'form-control-file','multiple':True
      })
  class Meta:
    model =OnlineSavdoFile
    fields =['file','file_type']

