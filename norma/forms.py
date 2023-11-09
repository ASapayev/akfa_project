from django import forms
from .models import NormaExcelFiles,Norma,ViFiles,Kraska,Nakleyka,Lamplonka
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

class KraskaAddForm(forms.ModelForm):
  
  class Meta:
    model = Kraska
    fields ='__all__'

class NakleykaAddForm(forms.ModelForm):
  
  class Meta:
    model = Nakleyka
    fields ='__all__'

class LaminationAddForm(forms.ModelForm):
  
  class Meta:
    model = Lamplonka
    fields ='__all__'