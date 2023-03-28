from django import forms
# from .models import AluFile


class FileFormTermo(forms.ModelForm):
  def __init__(self, *args, **kwargs):
      super(FileFormTermo, self).__init__(*args, **kwargs)
      self.fields['file'].widget.attrs.update({
          'class': 'form-control-file'
      })
  # class Meta:
  #   model =AluFile
  #   fields =['file']