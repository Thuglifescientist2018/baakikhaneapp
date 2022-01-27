from django.urls import path

from customer.views import baakiDelete, baakiDetail, customerbaakis, baakiLekhne, baakiEdit, logout


urlpatterns = [
    path('', customerbaakis, name="baakiharu"),
    path('lekhnethaun', baakiLekhne,  name="lekhnethaun"),
    path('edit/<str:id>', baakiEdit,  name="baakiEdit"),
    path('detail/<str:id>', baakiDetail,  name="baakiDetail"),
    path('delete/<str:id>', baakiDelete,  name="baakiDelete"),

]
