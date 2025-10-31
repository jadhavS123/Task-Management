from django.shortcuts import render,redirect,get_object_or_404
from .models import Article
from django.db.models import Q

# Create your views here.
def home(request):
    if request.method == 'POST':
        name_data = request.POST['name']
        date_data = request.POST['date']
        clas_data = request.POST['clas']
        # dept_data = request.POST['dept']
        # roll_data = request.POST['roll']
        # tel_data = request.POST['tel']

        Article.objects.create(name=name_data,date=date_data,clas=clas_data,)
        return redirect('read')
    return render(request,'home.html')

# name_icontains  -- to make thesearch free from case sensitivity
# Q ---- Searching the whole data as it is 
# q ---- searching the data based on character
def read(request):
    search = request.GET.get('q')
    if search:
        data = Article.objects.filter(
            Q(name__icontains = search) | Q(date__icontains = search)| Q(clas__icontains = search)
        )
    else:
        data = Article.objects.all().order_by('-id')
    return render(request,'read.html',{'data':data,'search':search})

def update(request,sid):
    data = get_object_or_404(Article,id=sid)
    if request.method == 'POST':
        data.name = request.POST['name']
        data.date = request.POST['date']
        data.clas = request.POST['clas']
        # data.dept = request.POST['dept']
        # data.roll = request.POST['roll']
        # data.tel = request.POST['tel']
        data.save()
        return redirect('read')
    return render(request,'update.html',{'data':data})


def delete_data(request,sid):
    data = get_object_or_404(Article,id=sid)
    if request.method == 'POST':
        data.delete()
        return redirect('read')
    return render(request,'delete.html',{'data':data})









