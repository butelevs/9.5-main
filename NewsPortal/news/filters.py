from django_filters import FilterSet,DateFilter
from .models import Post, Author


class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {
            'header_post': ['icontains'],
            'post': ['exact'],
            'date_post': ['gt']
        }