from django import forms
from .models import EpdmFile



class NormaEpdmFileForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
      super(NormaEpdmFileForm, self).__init__(*args, **kwargs)
      self.fields['file'].widget.attrs.update({
          'class': 'form-control-file'
      })
  class Meta:
    model = EpdmFile
    fields =['file','file_type']




  