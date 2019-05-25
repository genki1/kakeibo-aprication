from . import views
from django.urls import path


app_name = "kakeibo"


urlpatterns = [
    
    # 家計簿リスト
    path("kakeibo_list/", views.KakeiboListView.as_view(), name="kakeibo_list"),
    
    # 家計簿クリエイト
    path("kakeibo_create/", views.KakeiboCreateView.as_view(), name="kakeibo_create"),
    path("create_done/", views.create_done, name="create_done"),

    # 家計簿アップデート
    path("kakeibo/<int:pk>/", views.KakeiboUpdateView.as_view(), name="kakeibo_update"),
    path("update_done/", views.update_done, name="update_done"),

    # 家計簿消去
    path("delete/<int:pk>/", views.KakeiboDeleteView.as_view(), name="kakeibo_delete"),
    path("delete_done/", views.delete_done, name="delete_done"),

    # 円グラフ
    path("circle/", views.show_circle_graph, name="kakeibo_circle"),

]