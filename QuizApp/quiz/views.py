from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework import viewsets
from .models import (
    Answer, 
    Question,
    UsersAnswer,
    result,
    Quiz
)

from .serializers import (
    QuizListSerializer, 
    QuizListSerializer,
    QuestionSerializers,
    UsersAnswerSerializer,
    resultserializers
)

class QuizViewSet(viewsets.ModelViewSet):

    serializer_class =  QuizListSerializer
    queryset = Quiz.objects.all()

class QuestionDetailViewset(viewsets.ModelViewSet):

    serializer_class = QuestionSerializers
    queryset = Question.objects.all()


class SaveUsersAnswer(generics.UpdateAPIView):
    serializer_class=UsersAnswerSerializer
    queryset = UsersAnswer.objects.all()

class Resultview(generics.GenericAPIView):
    serializer_class=resultserializers

    def post(self, request, *args, **kwargs):
        result_id = request.data.get('result')
        question_id = request.data.get('question')
        answer_id = request.data.get('answer')

        result = get_object_or_404(QuizTaker, id=result_id)
        question = get_object_or_404(Question, id=question_id)

        quiz = Quiz.objects.get(slug=self.kwargs['slug'])
        correct_answers = 0

        for users_answer in UsersAnswer.objects.all():
            answer = Answer.objects.get(question=users_answer.question, is_correct=True)
            print(answer)
            print(users_answer.answer)
            if users_answer.answer == answer:
                correct_answers += 1

        result.score =  correct_answers
        print(result.score)
        result.save()

        return Response(self.get_serializer(quiz).data)
