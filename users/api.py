from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import CustomUser
from .serializers import CustomUserSerializer
from .sms import send_sms_verification
from django.contrib.auth.hashers import check_password


class CustomUserLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        if 'phone_number' in request.data and 'password' in request.data:
            phone_number = request.data.get('phone_number')
            password = request.data.get("password")
            try:
                user = CustomUser.objects.get(phone_number=phone_number)

                if not check_password(password, user.password):
                    return Response({'error': 'Wrong password'}, status=status.HTTP_400_BAD_REQUEST)

                # user.sms_verify = user.generate_verification_code()
                # user.save()

                serializer = CustomUserSerializer(user)

                token, created = Token.objects.get_or_create(user=user)

                # send_sms_verification(user.phone_number, user.sms_verify)

                return Response({'message': 'Login successfully', 'user': serializer.data, 'token': token.key}, status=status.HTTP_200_OK)

            except CustomUser.DoesNotExist:
                return Response({'error': 'Invalid phone number'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Phone number and Password required'}, status=status.HTTP_400_BAD_REQUEST)

    # def put(self, request):
    #     if 'phone_number' in request.data and 'verification_code' in request.data:
    #         phone_number = request.data.get('phone_number')
    #         verification_code = request.data.get('verification_code')
    #
    #         try:
    #             user = CustomUser.objects.get(phone_number=phone_number, sms_verify=verification_code)
    #         except CustomUser.DoesNotExist:
    #             return Response({'error': 'Invalid verification code'},
    #                             status=status.HTTP_400_BAD_REQUEST)
    #
    #         serializer = CustomUserSerializer(user)
    #
    #         token, created = Token.objects.get_or_create(user=user)
    #
    #         return Response(
    #             {'message': 'Login successfully', 'user': serializer.data, 'token': token.key},
    #             status=status.HTTP_200_OK)
    #     return Response({'error': 'Verification code is required'},
    #                     status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        if 'phone_number' in request.data:
            phone_number = request.data.get('phone_number')

            try:
                user = CustomUser.objects.get(phone_number=phone_number)
            except CustomUser.DoesNotExist:
                return Response({'error': 'Invalid phone number'}, status=status.HTTP_400_BAD_REQUEST)

            user.sms_verify = user.generate_verification_code()
            user.save()

            send_sms_verification(user.phone_number, user.sms_verify)

            return Response({'message': 'Verification code sent successfully'}, status=status.HTTP_200_OK)

        return Response({'error': 'Phone number is required'}, status=status.HTTP_400_BAD_REQUEST)

class CustomUserLoadApi(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        serializer = CustomUserSerializer(request.user)
        return Response(serializer.data)