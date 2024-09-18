from django import forms
from .models import KraskaFile,TexcartaFile



class NormaKraskaFileForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
      super(NormaKraskaFileForm, self).__init__(*args, **kwargs)
      self.fields['file'].widget.attrs.update({
          'class': 'form-control-file'
      })
  class Meta:
    model = KraskaFile
    fields =['file','file_type']

class TexcartaKraskaFileForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
      super(TexcartaKraskaFileForm, self).__init__(*args, **kwargs)
      self.fields['file'].widget.attrs.update({
          'class': 'form-control-file'
      })
  class Meta:
    model = TexcartaFile
    fields =['file','file_type']




  