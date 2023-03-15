from django import forms
from client.models import Gallery, Sample, Family


class GalleryForm(forms.ModelForm):
  class Meta:
    model = Gallery
    fields = ['img', 'title']
    
    

class SampleForm(forms.ModelForm):
  class Meta:
    model = Sample
    fields = ['img', 'name']
       