from django.shortcuts import render,reverse
from django.http import HttpResponse,JsonResponse
from .models import FormTemplate,FormDetail
import pandas as pd
import matplotlib.pyplot as plt
import mpld3

# Create your views here.
def index_view(request): 
    return render(request,'index.html')

def getForm(request):
    if not request.method == 'POST':
        return HttpResponse(f'You are in the wrong page, click <a href="{reverse('index')}">here</a> here to go to the homepage')
    
    code = request.POST['code']
    template = FormTemplate.objects.filter(code=code)
    if template.exists():
        template = template[0]
    else:
        return JsonResponse({'message':f'Invalid code, click <a href="{reverse('index')}">here</a> here to try again'},status=400)

    fields = template._meta.get_fields()
    data = {}
    for field in fields:
        if field.name == 'formdetail' or field.name == 'code':
            continue
        data[field.name]=getattr(template, field.name)

    return JsonResponse(data,status=200)

def submitForm(request):
    if not request.method == 'POST':
        return HttpResponse(f'You are in the wrong page, click <a href="{reverse('index')}">here</a> here to go to the homepage')
    
    code = request.POST['code']
    template = FormTemplate.objects.filter(code=code)
    if template.exists():
        template = template[0]
    else:
        return JsonResponse({'message':f'Invalid code, click <a href="{reverse('index')}">here</a> here to try again'},status=400)

    form = FormDetail(template=template)
    for key,val in request.POST.items():
        if key == 'csrfmiddlewaretoken' or key == 'code':
            continue
        if hasattr(form, key):
            setattr(form,key,val)
    
    form.save()

    return JsonResponse({'message':'success'},status=200)

def getReport(request):
    if not request.user.is_authenticated:
        return HttpResponse(f'You are not authorized to access this page, click <a href="{reverse('index')}">here</a> here to go to the homepage')
    code = request.GET.get('code')
    template = FormTemplate.objects.filter(code=code)
    if template.exists():
        template = template[0]
    else:
        return HttpResponse(f'Invalid code, click <a href="{reverse('report')}">here</a> here to try again')

    data = {}
    for form in template.formdetail_set.all():
        pass
    data = {'length': [1.5, 0.5, 1.2, 0.9, 3],
            'width': [0.7, 0.2, 0.15, 0.2, 1.1]}
    index = ['pig', 'rabbit', 'duck', 'chicken', 'horse']
    df = pd.DataFrame(data, index=index)

    # Create a histogram
    fig, ax = plt.subplots()
    hist = df.hist(bins=3, ax=ax)

    # Use mpld3 to embed the plot in HTML
    html_code = mpld3.fig_to_html(fig)

    return HttpResponse(html_code)