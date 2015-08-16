from django.conf.urls import patterns, url

urlpatterns = patterns('rat.views',  
    url(r'^index/$', 'index'),
    url(r'^import_allocation_data', "import_allocation_data", name="import_allocation_data"),
    # url(r'^articles/2003/$', 'news.views.special_case_2003'),  
    # url(r'^articles/(\d{4})/$', 'news.views.year_archive'),  
    # url(r'^articles/(\d{4})/(\d{2})/$', 'news.views.month_archive'),  
    # url(r'^articles/(\d{4})/(\d{2})/(\d+)/$', 'news.views.article_detail'),  
)
