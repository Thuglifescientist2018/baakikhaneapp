from django.shortcuts import get_object_or_404, render, reverse, HttpResponseRedirect
from .models import CustomerKoBaaki
from .forms import BaakiLekhneForm
from Total.models import Total


# Create your views here.


def customerbaakis(request):
    template_name = "baaki.html"
    customerKoBaaki = CustomerKoBaaki.objects.all().order_by("-id")

    if(len(Total.objects.all()) == 0):
        Total.objects.create(total_price=0)
    context = {
        "baakiharu": customerKoBaaki,
        "total": Total.objects.all().first().total_price
    }

    return render(request, template_name, context)


def baakiLekhne(request):
    template_name = "baakilekhne.html"
    lekhne_form = BaakiLekhneForm(request.POST or None, request.FILES or None)
    if lekhne_form.is_valid():
        if(len(Total.objects.all()) == 0):
            Total.objects.create(total_price=0)
        form_price = float(lekhne_form.cleaned_data.get("product_price"))
        total_first = Total.objects.all().first()
        total_first.total_price += form_price
        total_first.save()
        lekhne_form.save()
        return HttpResponseRedirect(reverse("baakiharu"))

    # save
    # redirect to home

    context = {
        "form": lekhne_form
    }

    return render(request, template_name, context)


def baakiEdit(request, id):

    template_name = "baakiEdit.html"
    baaki = get_object_or_404(CustomerKoBaaki, id=id)
    edit_form = BaakiLekhneForm(request.POST or None, instance=baaki)
    initial_baaki_price = baaki.product_price
    if edit_form.is_valid():
        total_first = Total.objects.all().first()
        total_first_price = (total_first.total_price -
                             initial_baaki_price) + baaki.product_price
        total_first.total_price = total_first_price
        total_first.save()
        edit_form.save()
        return HttpResponseRedirect(reverse("baakiharu"))
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
        total_first = Total.objects.all().first()
        total_first_price = total_first.total_price - obj.product_price
        total_first.total_price = total_first_price
        total_first.save()
        obj.delete()
        # we must 'return' the redirect or it will not work or execute
        return HttpResponseRedirect(reverse('baakiharu'))
    context = {'baaki': obj}
    return render(request, template_name, context)
