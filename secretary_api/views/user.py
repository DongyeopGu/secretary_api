from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from secretary_api.models import UserInfo


class UserViewSet(GenericViewSet):
    queryset = UserInfo.objects.all()

    @action(detail=False, methods=['POST'], url_name='create_user', url_path='join')
    def join(self, *args, **kwargs):
        name = self.request.get('name')
        email = self.request.get('email')
        gender = self.request.get('gender')
        birth = self.request.get('birth')
        job_position = self.request.get('job_position')
        return Response(data={'result': 'success'})

    @action(detail=False, methods=['GET'], url_name='login', url_path='login')
    def login(self, *args, **kwargs):

        return Response(data={'result': '이런거 나온다'})