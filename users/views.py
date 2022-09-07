from rest_framework.views import APIView
from rest_framework.response import Response

users = [
    {'id': 1, 'name': 'Martha', 'age': 25},
    {'id': 2, 'name': 'Oleh', 'age': 21},
    {'id': 3, 'name': 'Andriy', 'age': 20},
    {'id': 4, 'name': 'Karina', 'age': 22},
    {'id': 5, 'name': 'Katrina', 'age': 19}
]


class UserView(APIView):
    def get(self, request):
        return Response(users)

    def post(self, *args, **kwargs):
        params_dict = self.request.query_params.dict()
        print(params_dict)
        new_usr = self.request.data
        users.append(new_usr)
        return Response(new_usr)


class UserRetrieveUpdateDelete(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        for user in users:
            if user['id'] == pk:
                return Response(user)
        return Response('Not found')

    def put(self, *args, **kwargs):
        pk = kwargs.get('pk')
        for user in users:
            if user['id'] == pk:
                user |= self.request.data
                return Response(user)
        return Response('Not found')

    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk')
        for user in users:
            if user['id'] == pk:
                users.remove(user)
                return Response('deleted')
        return Response('Not found')
