from django import forms
from norma.models import NormaExcelFiles


class NormaFileForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
      super(NormaFileForm, self).__init__(*args, **kwargs)
      self.fields['file'].widget.attrs.update({
          'class': 'form-control-file'
      })
  class Meta:
    model = NormaExcelFiles
    fields =['file','type']


  