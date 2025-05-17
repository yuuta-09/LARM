from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import SignUpSerializer, SignUpResponseSerializer
from drf_spectacular.utils import extend_schema, OpenApiResponse

@extend_schema(
    request=SignUpSerializer,
    responses={
        201: OpenApiResponse(response=SignUpResponseSerializer, description="新規登録＆自動ログイン成功時"),
        400: OpenApiResponse(description="バリデーションエラー")
    }
)
class SignUpView(APIView):
    """
    ユーザ新規登録＋トークン自動発行API
    """
    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()  # 1回だけ!
            refresh = RefreshToken.for_user(user)
            return Response({
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "access": str(refresh.access_token),
                "refresh": str(refresh),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)