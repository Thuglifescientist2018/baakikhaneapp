
from .models import CustomerKoBaaki
from django import forms


class BaakiLekhneForm(forms.ModelForm):
    class Meta:
        model = CustomerKoBaaki
        fields = "__all__"
        labels = {
            "sold_product": "बेचेको / किनेको सामान ",
            "product_image": "सामान्को फोटो",
            "product_price": "सामान्को दाम",
            "miti": "मिती"

        }

    def clean_title(self, *args, **kwargs):
        instance = self.instance
        sold_product = self.cleaned_data.get("sold_product")
        qs = CustomerKoBaaki.objects.filter(sold_product__iexact=sold_product)
        if instance is not None:
            qs = qs.exclude(id=instance.id)
        if qs.exits():
            raise forms.ValidationError(
                "This title has been already taken"
            )
        return sold_product
