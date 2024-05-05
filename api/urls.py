from django.urls import path, include

from orders.api import (
    OrderAPIView,
    OrderDetailAPIView
)

from sellers.api import SellersListAPIView, SellerDetailAPIView

from loan.api import (
    LoansListAPIView,
    LoanDetailAPIView,
)

urlpatterns = [
    # product
    path('products/', include("product.urls")),

    # orders
    path("orders/", OrderAPIView.as_view(), name="order-list"),
    path("orders/<int:pk>/", OrderDetailAPIView.as_view(), name="order-detail"),

    # shop
    path("shops/", include("shop.urls")),

    # users
    path("user/", include('users.urls')),

    # sellers
    path("sellers/", SellersListAPIView.as_view(), name="sellers-list"),
    path("sellers/<int:pk>/", SellerDetailAPIView.as_view(), name="seller-detail"),

    # loans
    path("loans/", LoansListAPIView.as_view(), name="loans-list"),
    path("loans/<int:pk>/", LoanDetailAPIView.as_view(), name="loan-detail"),

]
