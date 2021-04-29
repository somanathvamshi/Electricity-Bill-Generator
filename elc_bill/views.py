from django.shortcuts import render
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView
from .models import Details
from .forms import ElcForm
from django.template.loader import get_template 
# Create your views here.
from django.views.generic import ListView
# def index(request):
#     det = Details.objects.all()
#     form = ElcForm()
    
#     return render(request,'index.html',{'dets':det,'form':form})
class ElcListView(ListView):
    model = Details
    template_name = 'index.html'
    context_object_name = 'dets'
class ElcDetailView(DetailView):
    model=Details
    template_name = 'detail.html'
    context_object_name = 'dets'
from django.http import HttpResponse
from django.views.generic import View

from .utils import render_to_pdf #created in step 4


class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        field_value = self.kwargs.get("pk")
        template = get_template('invoice.html')
        print()
        b1 = Details.objects.get(id = field_value)
        context = {
            "invoice_id": b1.id,
            "customer_name": b1.first_name,
            "amount": b1.price,
            "date": b1.from_date,
            "image":b1.image,
            "to_date":b1.to_date,
            "address":b1.address,
            "state":b1.state,
            "no_units":b1.no_units

         }
        html = template.render(context)
        pdf = render_to_pdf('invoice.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" %("12341231")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")
class ElcCreateView(CreateView):
    model = Details
    template_name = 'create.html'
    # fields = ['first_name','gender','address','date','state','download_pdf','no_units','price','image']
    form_class = ElcForm
    context_object_name = 'form'
    success_url = '/'
class ElcUpdateView(UpdateView):
    model = Details
    template_name = 'create.html'
    # fields = ['first_name','gender','address','date','state','download_pdf','no_units','price','image']
    form_class = ElcForm
    context_object_name = 'form'
    success_url = '/'
class ElcDeleteView(DeleteView):
    model = Details
    success_url ='/'
    template_name = 'confirm-delete.html'
# def elc_details(request):

#     button = request.POST['b1']
#     if  button == 'Save':
#         name = request.POST['first_name']
#         address = request.POST['address']
#         gender = request.POST['gender']
#         date = request.POST['date']
#         state = request.POST['state']
#         download = bool(request.POST['download_pdf'])
#         units = int(request.POST['no_units'])
#         price = int(request.POST['price'])
#         image = request.FILES['image']
#         d1 = Details.objects.create(first_name=name,address=address,gender=gender,date=date,state=state,download_pdf=download,no_units=units,price=price,image = image)
        
#         msg = 'record saved'
#         return render(request,'index.html',{'msg':msg})
