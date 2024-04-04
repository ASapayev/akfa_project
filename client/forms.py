from django import forms
from .models import OrderDetail



class OrderFileForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
      super(OrderFileForm, self).__init__(*args, **kwargs)
      self.fields['file'].widget.attrs.update({
          'class': 'form-control-file'
      })
  class Meta:
    model = OrderDetail
    fields =['order','owner','message','status','file']