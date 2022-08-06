from rest_framework import serializers 
from django.contrib.auth import get_user_model
from rest_framework_jwt.settings import api_settings 

class UserSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField('get_auth_token')
    class Meta:

        model = get_user_model()
        fields = ['token','password']
        extra_kwargs = {'password': {'write_only': True}}


    def create (self, validated_data):

        user = get_user_model().objects.create_user(**validated_data)
        return user

    def get_auth_token(self, obj):

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

    def update(self, instance, validated_data):

        password = validated_data.pop('password',None)
        user = super().update(instance, validated_data)

        if password :
            user.set_password(password)
            user.save()
        return user

class CreateUserSerializer(serializers.ModelSerializer):

    token = serializers.SerializerMethodField('get_auth_token')
    class Meta:

        model = get_user_model()
        fields = ('password','token','username')
        extra_kwargs = {'password': {'write_only': True,
                                   'min_length': 5,
                                   'style': {
                                       'input_type': 'password'
                                   }}}

    def create(self, validated_data):
        print(validated_data)
        password = validated_data.pop('password')
        
        user = get_user_model().objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def get_auth_token(self, obj):

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token
