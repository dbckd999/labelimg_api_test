from django import forms
from .models import MyModel, TestModel


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ('photo', )
    # photo = forms.ImageField(required=False)


class TestForm(forms.ModelForm):
    class Meta:
        model = TestModel
        fields = ('txval',)
    txval = forms.CharField(max_length=20)
