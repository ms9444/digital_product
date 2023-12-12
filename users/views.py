import random
import uuid

from django.core.cache import cache   # also we set cache settings in settings.py
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import requires_csrf_token

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import User, Device, UserProfile


class RegisterView(APIView):
    def post(self, request):
        phone_number = request.data.get('phone_number')  # be sure check later

        if not phone_number:
            return Response(status=status.HTTP_400_BAD_REQUEST)
            # return Response({'detail': 'User already registered!'},
            #                 status=status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.get(phone_number=phone_number)
        except User.DoesNotExist:
            user = User.objects.create_user(phone_number=phone_number)

        # user, created = User.objects.get_or_create(phone_number=phone_number)

        device = Device.objects.create(user=user)
        code = random.randint(10000, 99999)

        # send message (sms or email)
        # cache -> we set phone_number and code with 2 min in cash

        cache.set(str(phone_number), code, 2*60)
        # we send code as Response to client
        return Response({'code': code})


class GetTokenView(APIView):
    def post(self, request):
        # server get phone_number and code
        phone_number = request.data.get('phone_number')
        code = request.data.get('code')

        ''' we get phone_number from cash and store that in cashed_code,  and Comparison with code if...
         it is correct a token is given '''
        cashed_code = cache.get(str(phone_number))
        if code != cashed_code:
            return Response(status=status.HTTP_403_FORBIDDEN)

        token = str(uuid.uuid4())

        return Response({'token': token})




