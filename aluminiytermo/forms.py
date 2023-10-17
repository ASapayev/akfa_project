from django import forms
from .models import AluFileTermo,CharacteristikaFile


class FileFormTermo(forms.ModelForm):
  def __init__(self, *args, **kwargs):
      super(FileFormTermo, self).__init__(*args, **kwargs)
      self.fields['file'].widget.attrs.update({
          'class': 'form-control-file'
      })
  class Meta:
    model =AluFileTermo
    fields =['file','file_type']

class FileFormChar(forms.ModelForm):
  def __init__(self, *args, **kwargs):
      super(FileFormChar, self).__init__(*args, **kwargs)
      self.fields['file'].widget.attrs.update({
          'class': 'form-control-file'
      })
  class Meta:
    model = CharacteristikaFile
    fields =['file','file_type']