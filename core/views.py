from django.shortcuts import render, redirect
from .models import Info
from .forms import InfoForm

def home(request):
    infos = Info.objects.filter(validated=True).order_by('-created_at')

    return render(request, 'core/home.html', {'infos': infos})

def contribute(request):
    if request.method == "POST":
        form = InfoForm(request.POST)
        if form.is_valid():
            info = form.save(commit=False)
            info.contributor = request.user
            info.save()
            return redirect('home')
    else:
        form = InfoForm()
    return render(request, 'core/contribute.html', {'form': form})

def info_detail(request, info_id):
    info = Info.objects.get(id=info_id)
    return render(request, 'core/info_detail.html', {'info': info})

from django.shortcuts import render
from .models import Info, Category, Region

def all_infos(request):
    infos = Info.objects.all().order_by('-created_at')

    # Récupérer les filtres depuis les paramètres GET
    category_id = request.GET.get('category')
    region_id = request.GET.get('region')

    if category_id and category_id != "":
        infos = infos.filter(category_id=category_id)
    if region_id and region_id != "":
        infos = infos.filter(region_id=region_id)

    categories = Category.objects.all()
    regions = Region.objects.all()

    return render(request, 'core/all_infos.html', {
        'infos': infos,
        'categories': categories,
        'regions': regions,
        'selected_category': category_id,
        'selected_region': region_id
    })



# Create your views here.
