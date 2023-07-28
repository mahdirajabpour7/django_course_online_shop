from django.db.transaction import commit
from django.shortcuts import render , get_object_or_404 , reverse
from django.views import generic


from .models import Products , Comment
from .forms import CommentForm



class ProductListView(generic.ListView):
    #model = Products
    queryset = Products.objects.filter(active=True)
    template_name = "Products/Products_list.html"
    context_object_name = "Products"


class ProductDetailVeiw(generic.DetailView):
    model = Products
    template_name = "Products/Products_detail.html"
    context_object_name = "Products"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comment_forms"] = CommentForm()
        return context


class CommentCreatView(generic.CreateView):
    model = Comment
    form_class = CommentForm

    #def get_success_url(self):
        #return reverse("product_list")


    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user

        pk = int(self.kwargs["pk"])
        product = get_object_or_404(Products, id=pk)
        obj.product = product
        return super().form_valid(form)






