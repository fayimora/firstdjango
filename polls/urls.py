from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, kwargs=None, name="index"),

    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name="detail"),

    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),

    # ex: /polls/5/votes
    url(r'^(?P<question_id>[0-9]+)/votes/$', views.vote, name='vote')
]
