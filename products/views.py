from django.db.transaction import commit
from django.shortcuts import render , get_object_or_404 , reverse, redirect
from django.views import generic
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
#from django.http import HttpResponse
from wsgiref.util import FileWrapper
from django.contrib.auth.mixins import LoginRequiredMixin ,UserPassesTestMixin


from .models import Products , Comment
from .forms import CommentForm ,ProductSearchForm
from cart.forms import AddToCart


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
        context["add_to_cart_form"] = AddToCart()
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


        messages.success(self.request , "successfully created")

        return super().form_valid(form)



def search_products(request):
    form = ProductSearchForm(request.GET)
    results = []

    if form.is_valid():
        search_query = form.cleaned_data['search_query']
        results = Products.objects.filter(
            Q(title__icontains=search_query) | Q(description__icontains=search_query)
        )

    return render(request, 'Products/search_results.html', {'form': form, 'results': results})

@login_required
def like_product(request, pk):
    product = get_object_or_404(Products, pk=pk)
    user = request.user
    # حذف دیس‌لایک اگر کاربر محصول را دیس‌لایک کرده باشد
    if product.is_disliked_by(user):
        product.like_set.filter(user=user, value=False).delete()
    # اضافه یا حذف لایک بسته به وضعیت کنونی
    if product.is_liked_by(user):
        product.like_set.filter(user=user, value=True).delete()
    else:
        product.like_set.create(user=user, value=True)
    # بازگشت به صفحه محصول
    return redirect("product_list")

@login_required
def dislike_product(request, pk):
    product = get_object_or_404(Products, pk=pk)
    user = request.user
    # حذف لایک اگر کاربر محصول را لایک کرده باشد
    if product.is_liked_by(user):
        product.like_set.filter(user=user, value=True).delete()
    # اضافه یا حذف دیس‌لایک بسته به وضعیت کنونی
    if product.is_disliked_by(user):
        product.like_set.filter(user=user, value=False).delete()
    else:
        product.like_set.create(user=user, value=False)
    # بازگشت به صفحه محصول
    return redirect("product_list")




from django.http import HttpResponse, HttpResponseServerError, HttpResponseNotFound
from wsgiref.util import FileWrapper
import os

def download_pdf(request):
    filename = 'faults.pdf'
    try:
        file = open(filename, 'rb')
        content = FileWrapper(file)
        response = HttpResponse(content, content_type='application/pdf')
        response['Content-Length'] = os.path.getsize(filename)
        response['Content-Disposition'] = 'attachment; filename=%s' % 'faults.pdf'
        return response
    except (FileNotFoundError, IOError):
        return HttpResponseNotFound("File not found or not readable: %s" % filename)
    except Exception as e:
        return HttpResponseServerError("An error occurred: %s" % str(e))


class ProductsCreateView(LoginRequiredMixin , generic.CreateView):

    model = Products
    fields = ["title", "description", "price","short_description","image","pdf_file",]
    template_name = "products/product_create.html"


