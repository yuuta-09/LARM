from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

# レスポンス用シリアライザー
class SignUpResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField()
    email = serializers.EmailField()
    access = serializers.CharField()
    refresh = serializers.CharField()

class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data.get('email')
        )
        return user