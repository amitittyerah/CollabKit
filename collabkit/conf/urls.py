from django.conf.urls import patterns, include, url
from django.contrib import admin
from conf import settings
from django.conf.urls.static import static
from quiz import views as template_views
from api import views


admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', template_views.index),
                       url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
                        url(r'^set/add', views.set_add, name='set_add'),
                        url(r'^set/delete', views.set_delete, name='set_delete'),
                        url(r'^set/update', views.set_update, name='set_update'),
                        url(r'^set/list', views.set_list, name='set_list'),
)

urlpatterns += patterns('',
                        url(r'^qc/add', views.qc_add, name='qc_add'),
                        url(r'^qc/delete', views.qc_delete, name='qc_delete'),
                        url(r'^qc/update', views.qc_update, name='qc_update'),
                        url(r'^qc/list', views.qc_list, name='qc_list'),
)

urlpatterns += patterns('',
                        url(r'^question/add', views.question_add, name='question_add'),
                        url(r'^question/delete', views.question_delete, name='question_delete'),
                        url(r'^question/update', views.question_update, name='question_update'),
                        url(r'^question/list', views.question_list, name='question_list'),
                        url(r'^question/check_tf', views.question_check_tf, name='question_check_tf'),
                        url(r'^question/check_mcq', views.question_check_mcq, name='question_check_mcq'),
                        url(r'^question/check_fb', views.question_check_fb, name='question_check_fb'),
                        url(r'^question/get_answer', views.question_get_answer, name='question_get_answer'),
)
