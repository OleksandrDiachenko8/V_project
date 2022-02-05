from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from test_app.serializers import QuestionsSerializer, ResultSerializer, TestedUserSerializer, AnswerSerializer
from test_app.models import Question, Answer_variants, Result, TestedUser, Answer
from test_app.logic import question, check_add_user, save_answer, get_test_time


# .../testing/        user info ----> D --> questions pool
class Testing(APIView):
    def post(self, request):
        data = request.data
        current_test = get_test_time()
        current_user = check_add_user(data)
        if current_user is None:
            response_data = {'user_id': -1, 'info': 'user already exists!!'}
            return Response(status=202, data=response_data)
        else:
            data = question()
            serializer = QuestionsSerializer(data, many=True)
            response_data = serializer.data
            response_data.insert(0, {'user_id': current_user, 'time_for_test': current_test})
            return Response(status=201, data=response_data)


# .../answers and result/    user answers ----> D save --> result
class AnswerApi(APIView):
    def post(self, request):
        data = request.data
        result_data = save_answer(data)
        return Response(status=201, data=result_data)


class ResultApiView(ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer


class TestedUserApiView(ModelViewSet):
    queryset = TestedUser.objects.all()
    serializer_class = TestedUserSerializer
