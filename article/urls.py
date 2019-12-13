from django.urls import path,re_path
from . import views
from django.conf.urls import include, url

from django.conf.urls.static import static
from django.conf import settings

app_name = 'article'

urlpatterns = [
    path('article-list/',views.article_list,name = 'article_list'),
    path('article-detail/<int:id>/',views.article_detail,name = 'article_detail'),
    # path('article-create/',views.article_create,name = 'article_create'),
    path('article-create/',views.md_create,name = 'article_create'),
    path('article-delete/<int:id>/',views.article_delete,name='article_delete'),
    path('article-update/<int:id>/',views.article_update,name = 'article_update'),
    path('article-own/',views.article_own,name='article_own'),
    re_path('searchtag/(?P<category>.{0,20})/',views.searchtag,name = 'searchtag'),
    # url(r'mdeditor/', include('mdeditor.urls'))
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)