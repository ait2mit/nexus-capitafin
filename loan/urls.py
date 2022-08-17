from django.urls import path, include  # add this
from . import views
from .views import DataUpdateView, DataDeleteView, EvaluateLoan

urlpatterns = [
    path("loan", views.loan, name="loan"),
    path("data/insert-loan/", views.insert_data, name="insert-loan"),
    path(
        "data/<int:pk>/update-loan/", DataUpdateView.as_view(), name="data-update-loan"
    ),
    path(
        "data/<int:pk>/delete-loan/", DataDeleteView.as_view(), name="data-delete-loan"
    ),
    path(
        "data/<int:pk>/evaluate-loan/", EvaluateLoan.as_view(), name="evaluate-loan"
    ),  # This one works as view as per pk
    path(
        "data/eval_process_loan/", views.eval_process_loan, name="eval_process_loan"
    ),  # View after Process
]
