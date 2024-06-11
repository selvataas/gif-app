from django import forms
from .models import Image

class UploadImageForm(forms.ModelForm):
  class Meta:
    model = Image
    fields = ["image", "title"]
    widgets = {
      "title": forms.Textarea(
        attrs={
          "cols": 60,
          "rows": 3,
        }
      ),
    }