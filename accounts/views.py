from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer
from .models import User
import jwt, datetime, json, ast
from rest_framework import serializers

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if(len(request.data['name']) < 5):
            raise serializers.ValidationError("USERNAME ERROR")
        if(len(request.data['password']) < 5):
            raise serializers.ValidationError("PASSWORD ERROR")
            
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class WatchlistAddView(APIView):
    def post(self, request):
        name = request.data['name']
        watchlist = request.data['watchlist']

        user = User.objects.filter(name=name).first()
        users = User.objects.all()

        if user is None:
            raise AuthenticationFailed('User not found!')

        list = users.filter(name=name).values()[0]['watchlist']
        if list is None:
            list = "[]"
        list = ast.literal_eval(list)
        if(watchlist not in list):
            list.append(watchlist)
        
        users.filter(name=name).update(watchlist=list)

        response = Response()

        watchlist = json.dumps(list)

        response.data = {
            'watchlist': watchlist  
        }
        return response

class UpdateAccountName(APIView):
    def post(self, request):
        name = request.data['name']
        newname = request.data['newname']

        # Check if new username is same than old username
        if(name == newname):
            raise serializers.ValidationError("SAME USERNAME")

        # Check if username is long enough
        if(len(newname) < 5):
            raise serializers.ValidationError("SHORT USERNAME")

        # Update username
        users = User.objects.all()
        users.filter(name=name).update(name=newname)

        response = Response()

        response.data = {
            'name': newname
        }
        return response

class UpdateAccountPassword(APIView):
    def post(self, request):
        name = request.data['name']

        users = User.objects.all()
        watchlist = users.filter(name=name).values()[0]['watchlist']

        # Check if password is long enough
        if(len(request.data['password']) < 5):
            raise serializers.ValidationError("SHORT PASSWORD")

        # If password is valid delete old account and create a new one with the new password

        User.objects.filter(name=name).first().delete()

        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # Move watchlist from old account to new
        users.filter(name=name).update(watchlist=watchlist)

        return Response(serializer.data)


class WatchlistDeleteView(APIView):
    def post(self, request):
        name = request.data['name']
        watchlist = request.data['watchlist']

        user = User.objects.filter(name=name).first()
        users = User.objects.all()

        if user is None:
            raise AuthenticationFailed('User not found!')

        list = users.filter(name=name).values()[0]['watchlist']
        list = ast.literal_eval(list)
        if(watchlist in list):
            list.remove(watchlist)
        
        users.filter(name=name).update(watchlist=list)

        response = Response()

        watchlist = json.dumps(list)

        response.data = {
            'watchlist': watchlist  
        }
        return response

class LoginView(APIView):
    def post(self, request):
        name = request.data['name']
        password = request.data['password']

        user = User.objects.filter(name=name).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=1),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()

        watchlist = json.dumps(user.watchlist)

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token,
            'watchlist': watchlist,
            'name': name
        }
        return response

class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed("Unauthenticated")
        
        try:
            payload = jwt.decode(token, 'secret', algorithms='HS256')

        except:
            raise AuthenticationFailed("Unauthenticated")

        user = User.objects.filter(id = payload['id']).first()
        serializer = UserSerializer(user)

        return Response(serializer.data)


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }

        return response




        
        
