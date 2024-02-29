from django.shortcuts import render,reverse
from django.http import HttpResponse,JsonResponse
from .models import FormTemplate,FormDetail
import pandas as pd
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
from io import BytesIO

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

def reportView(request):
    if not request.user.is_authenticated:
        return HttpResponse(f'You are not authorized to access this page, click <a href="{reverse('index')}">here</a> here to go to the homepage')

    code = request.GET.get('code')

    return render(request,'report.html',{
        'code':code,
        'link':reverse('report')
    })

def getReport(request):
    if not request.user.is_authenticated:
        return HttpResponse(f'You are not authorized to access this page, click <a href="{reverse('index')}">here</a> here to go to the homepage')
    code = request.GET.get('code')
    value = request.GET.get('value')

    template = FormTemplate.objects.filter(code=code)
    if template.exists():
        template = template[0]
    else:
        return HttpResponse(f'Invalid code, click <a href="{reverse('report')}">here</a> here to try again')

    data = []

    for form in template.formdetail_set.all():
        for field in form._meta.get_fields():
            if field.name == value:
                data.append(getattr(form, field.name))

  # Create a DataFrame with the frequency of each number
    df = pd.DataFrame({'Number': data})
    frequency_table = df['Number'].value_counts().reset_index()
    frequency_table.columns = ['Number', 'Frequency']
    
    # Plot the table
    fig, ax = plt.subplots()
    ax.bar(frequency_table['Number'], frequency_table['Frequency'], color='blue', edgecolor='black')

    # Customize bar chart
    ax.set_ylabel('Frequency')
    ax.set_title(f'Bar Chart: Report for {code}({value})')

    # Save the figure to a BytesIO buffer
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()

    # Create a Django HttpResponse with the image
    response = HttpResponse(content_type='image/png')
    response.write(buffer.read())

    return response