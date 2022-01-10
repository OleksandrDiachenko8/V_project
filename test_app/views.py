

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from test_app.serializers import QuestionsSerializer, ResultSerializer, TestedUserSerializer, AnswerSerializer
from test_app.models import Question, Answer_variants, Result, TestedUser, Answer
from test_app.logic import question, check_add_user, result_fit


# .../testing/
class Testing(APIView):
    def post(self, request):
        data = request.data
        current_user = check_add_user(data)
        data = question()
        serializer = QuestionsSerializer(data, many=True)
        data = serializer.data
        data.insert(0, {'user_id': current_user})
        print(len(data))
        return Response(status=201, data=data)


def print_questions(request):
    return render(request, 'index.html', {'questions': Question.objects.all(),
                                          'variants': Answer_variants.objects.all()
                                          })


class ResultApiView(ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer


class TestedUserApiView(ModelViewSet):
    queryset = TestedUser.objects.all()
    serializer_class = TestedUserSerializer


class AnswerApiView(ModelViewSet):
    def get_serializer(self, *args, **kwargs):
        if "data" in kwargs:
            data = kwargs["data"]

            # check if many is required
            if isinstance(data, list):
                kwargs["many"] = True

        return super(AnswerApiView, self).get_serializer(*args, **kwargs)

    def post(self, request):
        print("1212121212")
        data = request.data
        result_fit(data)
        # data = question()
        #
        # serializer = AnswerSerializer(data, many=True)   #???
        # print(serializer.data)
        # return Response(status=201, data=serializer.data)

    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

# class AnswerApiView(APIView):
#     def post(self, request):
#         data = request.data
#         current_user = check_add_user(data)
#         data = question()
#         serializer = QuestionsSerializer(data, many=True)
#         data = serializer.data
#         data.insert(0, {'user_id': current_user})
#         print(len(data))
#         return Response(status=201, data=data)


