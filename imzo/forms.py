from django import forms
from .models import ExcelFilesImzo


class FileFormImzo(forms.ModelForm):
  def __init__(self, *args, **kwargs):
      super(FileFormImzo, self).__init__(*args, **kwargs)
      self.fields['file'].widget.attrs.update({
          'class': 'form-control-file'
      })
  class Meta:
    model =ExcelFilesImzo
    fields =['file']