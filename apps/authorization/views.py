from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, permissions
from apps.authorization.serializers import UserLoginSerializer


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def login(request):
    serializer = UserLoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    return Response(serializer.data)


@api_view(['POST'])
def logout(request):
    Token.objects.get(user=request.user).delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
