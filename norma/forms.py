from django import forms
from .models import NormaExcelFiles,Norma,ViFiles
from imzo.models import TexCartaTime


class NormaFileForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
      super(NormaFileForm, self).__init__(*args, **kwargs)
      self.fields['file'].widget.attrs.update({
          'class': 'form-control-file'
      })
  class Meta:
    model = NormaExcelFiles
    fields =['file','type']

class ViFileForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
      super(ViFileForm, self).__init__(*args, **kwargs)
      self.fields['file'].widget.attrs.update({
          'class': 'form-control-file'
      })
  class Meta:
    model = ViFiles
    fields =['file',]


class NormaEditForm(forms.ModelForm):
  
  class Meta:
    model = Norma
    fields ='__all__'

class TexcartaEditForm(forms.ModelForm):
  
  class Meta:
    model = TexCartaTime
    fields ='__all__'