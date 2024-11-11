from django import forms
from .models import MatrixFile,TexcartaMatrixFile



class NormaMatrixFileForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
      super(NormaMatrixFileForm, self).__init__(*args, **kwargs)
      self.fields['file'].widget.attrs.update({
          'class': 'form-control-file'
      })
  class Meta:
    model = MatrixFile
    fields =['file']


class TexcartaMatrixFileForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
      super(TexcartaMatrixFileForm, self).__init__(*args, **kwargs)
      self.fields['file'].widget.attrs.update({
          'class': 'form-control-file'
      })
  class Meta:
    model = TexcartaMatrixFile
    fields =['file']




  