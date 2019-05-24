from django.shortcuts import render
from .models import Category, Kakeibo
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .forms import KakeiboForm
from django.urls import reverse_lazy


class KakeiboListView(ListView):
    model = Kakeibo
    # 以下は書かなくても自動で取得できる
    template_name = "kakeibo/kakeibo_list.html"
    def queryset(self):
        return Kakeibo.objects.all()


class KakeiboCreateView(CreateView):
    model = Kakeibo
    form_class = KakeiboForm
    success_url = reverse_lazy("kakeibo:create_done")

def create_done(request):
    return render(request, "kakeibo/create_done.html")


class KakeiboUpdateView(UpdateView):
    model = Kakeibo
    form_class = KakeiboForm
    success_url = reverse_lazy("kakeibo:update_done")

def update_done(request):
    return render(request, "kakeibo/update_done.html")


class KakeiboDeleteView(DeleteView):
    model = Kakeibo
    success_url = reverse_lazy("kakeibo:delete_done")

def delete_done(request):
    return render(request, "kakeibo/delete_done.html")