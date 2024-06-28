from rest_framework import serializers
from . import models
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.password_validation import validate_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserModel
        fields = ['id', 'username',  'first_name', 'last_name', 'email','phone','address','shop_name','is_customer','is_seller']


class UserRegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required = True)
    
    class Meta:
        model = models.UserModel
        fields = ['username', 'first_name', 'last_name', 'email','phone','address','shop_name','is_customer','is_seller', 'password', 'confirm_password',  ]

    def save(self):
        username = self.validated_data['username']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email']
        phone = self.validated_data['phone']
        address = self.validated_data['address']
        is_customer = self.validated_data['is_customer']
        is_seller = self.validated_data['is_seller']
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']

        if password != confirm_password:
            raise serializers.ValidationError({'confirm_password': ['Password does not match!']})
        
        userAc = models.UserModel(username=username, first_name = first_name, last_name = last_name, email = email,phone=phone,address=address,is_customer=is_customer,is_seller=is_seller)

        userAc.set_password(password)
        userAc.is_active = False
        userAc.save()

        return userAc
    

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required = True)
    password = serializers.CharField(required = True)


User = get_user_model()

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True, validators=[validate_password])

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError('Old password is not correct')
        return value

    def validate(self, data):
        if data['old_password'] == data['new_password']:
            raise serializers.ValidationError('New password cannot be the same as the old password')
        return data

    def save(self, **kwargs):
        user = self.context['request'].user
        user.set_password(self.validated_data['new_password'])
        user.save()
        return user
    new_password = serializers.CharField(write_only=True, min_length=8)
    uidb64 = serializers.CharField()
    token = serializers.CharField()

    def validate(self, attrs):
        try:
            uid = urlsafe_base64_decode(attrs['uidb64']).decode()
            user = User.objects.get(pk=uid)
        except (User.DoesNotExist, ValueError, TypeError, OverflowError):
            raise serializers.ValidationError('Invalid user ID or token')
        
        if not default_token_generator.check_token(user, attrs['token']):
            raise serializers.ValidationError('Invalid token')

        return attrs

    def save(self, **kwargs):
        uid = urlsafe_base64_decode(self.validated_data['uidb64']).decode()
        user = User.objects.get(pk=uid)
        user.set_password(self.validated_data['new_password'])
        user.save()