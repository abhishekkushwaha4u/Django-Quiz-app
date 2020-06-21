from django.urls import path,include,re_path
from rest_framework.routers import DefaultRouter
from quiz import views
from quiz.views import SaveUsersAnswer,UsersAnswerSerializer,Resultview



router=DefaultRouter()
router.register('Quiz',views.QuizViewSet)
router.register('Questiondetail',views.QuestionDetailViewset)

urlpatterns=[
    path('',include(router.urls)),
    path('save-answer/<pk>/', views.SaveUsersAnswer.as_view()),
    path('quizzes/(?P<slug>[\w\-]+)/result/$", views.Resultview.as_view()),
    ]
