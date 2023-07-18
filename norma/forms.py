from django import forms
from .models import NormaExcelFiles,Norma


class NormaFileForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
      super(NormaFileForm, self).__init__(*args, **kwargs)
      self.fields['file'].widget.attrs.update({
          'class': 'form-control-file'
      })
  class Meta:
    model = NormaExcelFiles
    fields =['file','type']

class NormaEditForm(forms.ModelForm):
  class Meta:
    model = Norma
    fields ='__all__'