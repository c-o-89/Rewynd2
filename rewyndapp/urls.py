from django.urls import path

from . import views

app_name = 'rewyndapp' #see https://docs.djangoproject.com/en/2.1/intro/tutorial03/
urlpatterns = [
    # /
    path('', views.index, name='index'),

    # /programs/
    path('programs/', views.programs_page, name='programs_page'),

    # /programs/5
    path('programs/<int:program_id>/', views.program_listview, name='program_listview'),

    # /episode/5
    path('episode/<int:id>/', views.episode_page, name='episode_page'),

    # /about/
    path('about/', views.about_page, name='about_page'),

    path('api/programlist/', views.ProgramList.as_view()),
    path('api/episodelist/<int:program_id>/', views.EpisodeList.as_view()),
    path('api/episodetweets/<int:episode_id>/', views.EpisodeTweets.as_view()),
]
