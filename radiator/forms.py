from django import forms
from norma.models import NormaExcelFiles
from .models import ViFiles


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


  