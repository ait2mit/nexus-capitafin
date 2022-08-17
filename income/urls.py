from django.urls import path, include  # add this
from . import views
from .views import DataUpdateView, DataDeleteView, EvaluateIncome

urlpatterns = [
    # path('income',views.income, name='income'),
    path("income", views.income, name="income"),
    path("data/insert-income/", views.insert_data, name="insert-income"),
    path(
        "data/<int:pk>/update-income/",
        DataUpdateView.as_view(),
        name="data-update-income",
    ),
    path(
        "data/<int:pk>/delete-income/",
        DataDeleteView.as_view(),
        name="data-delete-income",
    ),
    path(
        "data/<int:pk>/evaluate-income/",
        EvaluateIncome.as_view(),
        name="evaluate-income",
    ),  # This one works as view as per pk
    path(
        "data/eval_process_income/",
        views.eval_process_income,
        name="eval_process_income",
    ),  # View after Process
]
