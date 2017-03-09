from django import forms
from model_one.models import Publisher
class PublisherForm(forms.ModelForm):
#     name = forms.CharField() #添加lable标签报错，原因不知
#     address = forms.CharField()
#     city = forms.CharField()
#     state_province = forms.CharField()
#     country = forms.CharField()
#     website = forms.URLField()
    
    class Meta:
        model = Publisher
        exclude = ('id',)
        
    