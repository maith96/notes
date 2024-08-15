from django.urls import path
from .views import (
    SchoolIDListCreate,
    SchoolIDDelete,
    NationalIDListCreate,
    NationalIDDelete,
    SearchItemByIdentifier
)

urlpatterns = [
    # SchoolID URLs
    path('school_ids/', SchoolIDListCreate.as_view(), name='school-id-list-create'),
    path('school_ids/delete/<int:pk>/', SchoolIDDelete.as_view(), name='school-id-delete'),

    # NationalID URLs
    path('national_ids/', NationalIDListCreate.as_view(), name='national-id-list-create'),
    path('national_ids/delete/<int:pk>/', NationalIDDelete.as_view(), name='national-id-delete'),

    # Search URL
    path('search/<str:item_type>/<str:identifier>/', SearchItemByIdentifier.as_view(), name='search-item-by-identifier'),
]
