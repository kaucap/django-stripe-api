from django.urls import path
from app_shop.views import MainPage, ItemDetail, SuccessView, CancelView, buy_item

urlpatterns = [
    path('', MainPage.as_view(), name='main_page'),
    path('item/<int:pk>', ItemDetail.as_view(), name='item_detail'),
    path('buy/<int:pk>', buy_item, name='buy_item'),
    path('success/', SuccessView.as_view(), name='success'),
    path('cancel/', CancelView.as_view(), name='cancel')
]