from django.shortcuts import render
import shorter

def index(request):
    if request.method == 'POST':
        shorter.shorter_core.del_from_base(int(request.POST['id_inbase']))
    data = shorter.models.Main_db.objects.all()
    tmp = {}
    for i in data:
        t = []
        t.append(str(i.shorturl))
        t.append(str(i.longurl))
        tmp[i.id] = t
    data = tmp
    return render(request, "admin.html", {'data':data})
