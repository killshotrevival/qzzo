from django.shortcuts import render
import json
import base64
import rsa
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.views import APIView
from Crypto.PublicKey import RSA
from django.contrib.auth import logout, login, authenticate

from .models import profile
from .serializers import profileSerializer
from .temp import *


class register(APIView):
    def post(self, request):
        with open('Users/private_key', 'rb') as f:
            priv = f.read()
        priv = import_key(priv)

        received_json_data=json.loads(request.body)
        rec_email = received_json_data['email'];
        rec_email_encr = received_json_data['email_encrypted']
        print('email extracted')
        rec_email_encr = base64.b64decode(rec_email_encr)
        veri = verify_data(rec_email, priv, rec_email_encr)
        print('verified', veri)
        if veri:
            # the request is from a valid user
            user_object = User.objects.create_user(
                username=received_json_data['username'],
                email=rec_email,
                password=received_json_data['password']
            )
            print('user object saved')
            profile_obj = profile.objects.create(
                user = user_object,
                place = received_json_data['place'],
                desc = received_json_data['desc']
                )
            print('done till object')
            profile_obj.save()
            user_object.save()
            print('object saved')
            serializer = profileSerializer(profile_obj)
            new_dict = {'status':{
                'code':1,
                'message': 'User created succesfully'
            },
            'username': received_json_data['username']
            }
            new_dict.update(serializer.data)
            print(new_dict, 'seri')
            return Response(new_dict)
        else:
            return Response(json.dumps({
                'status':{
                    'code': -1,
                    'message' : 'request from unauthenticate user'
                },
            }))



class login(APIView):
    def post(self, request):
        with open('Users/private_key', 'rb') as f:
            priv = f.read()
        priv = import_key(priv)

        received_json_data=json.loads(request.body)
        rec_username = received_json_data['username'];
        rec_username_encr = received_json_data['username_encrypted']
        print('username extracted')
        rec_username_encr = base64.b64decode(rec_username_encr)
        veri = verify_data(rec_username, priv, rec_username_encr)
        print('verified', veri)
        if veri:
            username = received_json_data['username']
            # login(request, user[0])
            user = authenticate(username = received_json_data['username'], password=received_json_data['password'])
            print('login success')
            print('user', user)
            if user is not None:
                login(username = received_json_data['username'], password=received_json_data['password'])

                new_dict = {'status':{
                'code':2,
                'message': 'Login successfully'
                },
                'username': received_json_data['username']
                }
                return Response(new_dict)


            else:
                return Response(json.dumps({
                    'status': {
                        'code': -2,
                        'message': 'No user found in database'
                    },
                }))
        else:
            return Response(json.dumps({
                'status':{
                    'code': -1,
                    'message' : 'request from unauthenticate user'
                },
            }))


