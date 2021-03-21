from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from robertBosch.mentorship.user.serializers import UserRegistrationSerializer
from robertBosch.mentorship.user.serializers import UserLoginSerializer


class UserRegistrationView(CreateAPIView):

    authentication_classes = ()
    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny,)
    queryset = ''

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {
            'success' : 'True',
            'status code' : status.HTTP_200_OK,
            'message': 'User registered successfully',
            }
        status_code = status.HTTP_200_OK
        return Response(response, status=status_code)


class UserLoginView(RetrieveAPIView):

    authentication_classes = ()
    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer
    queryset = ''
    lookup_field = 'id'

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = {
            'success' : 'True',
            'status code' : status.HTTP_200_OK,
            'message': 'User logged in successfully',
            'token' : serializer.data['token'],
            }
        status_code = status.HTTP_200_OK

        return Response(response, status=status_code)
