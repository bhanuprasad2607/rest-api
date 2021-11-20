from rest_framework import serializers
from users.models import UserModel
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    mobile_no = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'mobile_no',
                  'email',
                  'password']

    def get_mobile_no(self, user):
        user_mobile = UserModel.objects.filter(user=user).get()
        print(user_mobile)
        return user_mobile.mobile_no
