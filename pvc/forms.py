from django import forms
from .models import PVCFile


class FileFormPVC(forms.ModelForm):
  def __init__(self, *args, **kwargs):
      super(FileFormPVC, self).__init__(*args, **kwargs)
      self.fields['file'].widget.attrs.update({
          'class': 'form-control-file'
      })
  class Meta:
    model =PVCFile
    fields =['file','file_type']

# class FileFormChar(forms.ModelForm):
#   def __init__(self, *args, **kwargs):
#       super(FileFormChar, self).__init__(*args, **kwargs)
#       self.fields['file'].widget.attrs.update({
#           'class': 'form-control-file'
#       })
#   class Meta:
#     model =CharacteristikaFile
#     fields =['file','file_type']