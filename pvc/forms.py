from django import forms
from .models import PVCFile,CharacteristikaFilePVC


class FileFormPVC(forms.ModelForm):
  def __init__(self, *args, **kwargs):
      super(FileFormPVC, self).__init__(*args, **kwargs)
      self.fields['file'].widget.attrs.update({
          'class': 'form-control-file'
      })
  class Meta:
    model =PVCFile
    fields =['file','file_type']

class FileFormCharPVC(forms.ModelForm):
  def __init__(self, *args, **kwargs):
      super(FileFormCharPVC, self).__init__(*args, **kwargs)
      self.fields['file'].widget.attrs.update({
          'class': 'form-control-file'
      })
  class Meta:
    model =CharacteristikaFilePVC
    fields =['file','file_type']



