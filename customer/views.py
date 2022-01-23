from django.shortcuts import get_object_or_404, render, reverse, HttpResponseRedirect
from .models import CustomerKoBaaki
from .forms import BaakiLekhneForm
from Total.models import Total


# Create your views here.


def customerbaakis(request):
    template_name = "baaki.html"

    customerKoBaaki = CustomerKoBaaki.objects.all().order_by("-id")
    if(len(Total.objects.all()) == 0):
        Total.objects.create(total_price=0, count=0)
    total_obj = Total
    total_obj_first = Total.objects.all().first()

    total_count = total_obj.count

    context = {
        "baakiharu": customerKoBaaki,
        "total": Total.objects.all().first().total_price
    }
    return render(request, template_name, context)


def baakiLekhne(request):
    template_name = "baakilekhne.html"
    lekhne_form = BaakiLekhneForm(request.POST or None, request.FILES or None)
    if lekhne_form.is_valid():
        lekhne_form.save()
        return HttpResponseRedirect(reverse('baakiharu'))
    context = {
        "form": lekhne_form
    }

    return render(request, template_name, context)


def baakiEdit(request, id):

    template_name = "baakiEdit.html"
    baaki = get_object_or_404(CustomerKoBaaki, id=id)
    edit_form = BaakiLekhneForm(request.POST or None, instance=baaki)
    if edit_form.is_valid():
        edit_form.save()
        return HttpResponseRedirect(reverse('baakiharu'))
    context = {
        "form": edit_form
    }
    return render(request, template_name, context)


def baakiDetail(request, id):
    template_name = "baakiDetail.html"
    baaki = get_object_or_404(CustomerKoBaaki, id=id)
    context = {
        "baaki": baaki
    }
    return render(request, template_name, context)


def baakiDelete(request, id):
    obj = get_object_or_404(CustomerKoBaaki, id=id)
    template_name = "baakiDelete.html"
    if request.method == "POST":
        obj.delete()
        # we must 'return' the redirect or it will not work or execute
        return HttpResponseRedirect(reverse('baakiharu'))
    context = {'baaki': obj}
    return render(request, template_name, context)
