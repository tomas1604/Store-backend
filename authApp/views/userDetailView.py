from django.conf import settings
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated
from authApp.serializers.userSerializer import UserSerializer
from authApp.models.user import User

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args,**kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm= settings.SIMPLE_JWT['ALGORITHM'])
        token_data = tokenBackend.decode(token, verify=False)

        if token_data['user_id'] != kwargs['pk']:
            return Response({'detail':'No está autorizado'}, status = status.HTTP_401_UNAUTHORIZED)
        
        return super().get(request, *args,**kwargs)
