from django import forms
from .models import EpdmFile,TexcartaFile



class NormaEpdmFileForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
      super(NormaEpdmFileForm, self).__init__(*args, **kwargs)
      self.fields['file'].widget.attrs.update({
          'class': 'form-control-file'
      })
  class Meta:
    model = EpdmFile
    fields =['file','file_type']

class TexcartaEpdmFileForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
      super(TexcartaEpdmFileForm, self).__init__(*args, **kwargs)
      self.fields['file'].widget.attrs.update({
          'class': 'form-control-file'
      })
  class Meta:
    model = TexcartaFile
    fields =['file','file_type']




  