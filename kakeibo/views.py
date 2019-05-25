from django.shortcuts import render
from .models import Category, Kakeibo
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .forms import KakeiboForm
from django.urls import reverse_lazy
from django.db import models


# リスト
class KakeiboListView(ListView):
    model = Kakeibo
    # 以下は書かなくても自動で取得できる
    template_name = "kakeibo/kakeibo_list.html"
    def queryset(self):
        return Kakeibo.objects.all()


# クリエイト
class KakeiboCreateView(CreateView):
    model = Kakeibo
    form_class = KakeiboForm
    success_url = reverse_lazy("kakeibo:create_done")

def create_done(request):
    return render(request, "kakeibo/create_done.html")


# アップデート
class KakeiboUpdateView(UpdateView):
    model = Kakeibo
    form_class = KakeiboForm
    success_url = reverse_lazy("kakeibo:update_done")

def update_done(request):
    return render(request, "kakeibo/update_done.html")


# 消去
class KakeiboDeleteView(DeleteView):
    model = Kakeibo
    success_url = reverse_lazy("kakeibo:delete_done")

def delete_done(request):
    return render(request, "kakeibo/delete_done.html")


# 円グラフ関数
def show_circle_graph(request):
    # 全データ総額
    kakeibo_data = Kakeibo.objects.all()
    total = 0
    for item in kakeibo_data:
        total += item.money
    # カテゴリ毎総額
    category_list = []
    category_data = Category.objects.all()
    for item in category_data:
        category_list.append(item.category_name)
        
    category_dict = {}
    for i,item in enumerate(category_list):
        category_total = Kakeibo.objects.filter(category__category_name=category_list[i]).aggregate(sum=models.Sum("money"))["sum"]
    # 各カテゴリの割合
        if category_total != None:
            ratio = int((category_total / total) * 100)
            category_dict[item] = ratio
        else:
            ratio = 0
            category_dict[item] = ratio

    return render(request, "kakeibo/kakeibo_circle.html", {"category_dict": category_dict})

