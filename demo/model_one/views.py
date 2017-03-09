from django.shortcuts import render
from django.contrib.auth.models import User
from model_one.models import Publisher
from django.http.response import HttpResponse
from model_one.forms import PublisherForm

# Create your views here.
def hello(request):
    print(request.POST.get('key'))
    user_list = User.objects.all()
    #return render(request, 'table.html',{'user_list':user_list})
    #lalal
    
    print(locals())
    return render(request, 'table.html',locals())

def add_publisher(request):
    if request.method == 'POST':
        #1.不适用django form的情况进行表单填写
#         publisher = Publisher()
#         
#         publisher.name = request.POST.get('name')
#         publisher.address = request.POST.get('address')
#         publisher.city = request.POST.get('city')
#         publisher.state_province = request.POST.get('state_province')
#         publisher.country = request.POST.get('country')
#         publisher.website = request.POST.get('website')
#         
#         publisher.save()
#         
#         return HttpResponse('添加出版社信息成功')
        #2.使用 django Form
#         publisher_form = PublisherForm(request.POST)
#         if publisher_form.is_valid():
#             Publisher.objects.create(
#                 name = publisher_form.cleaned_data['name'],
#                 address = publisher_form.cleaned_data['address'],
#                 city = publisher_form.cleaned_data['city'],
#                 state_province = publisher_form.cleaned_data['state_province'],
#                 country = publisher_form.cleaned_data['country'],
#                 website = publisher_form.cleaned_data['website'],
#             )
#         
        #3.使用 django model.Form
        publisher_form = PublisherForm(request.POST)
        if publisher_form.is_valid():
            publisher_form.save()
            return HttpResponse('添加出版社信息成功')
        
    else:
        publisher_form = PublisherForm()
    return render(request,'add_publisher.html',locals())
    
    
    
    
    
    