from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

class HomeAPI(APIView):
    def get(self, request, format=None):
        print(request.user)
        response = {
            'project-name': 'AdoptLife',
            'purpose': 'Ayudar a las mascotas a encontrar un hogar.',
            'cration-date': '07 de Octubre del 2021',
            'programmers': {
                'names': [
                    'Camilo Zaque',
                    'Jairo Daniel Cortés',
                    'Adolfo Cuartas',
                    'Liliana Gómez'
                ],
            },
            'program': {
                'name': 'Misión TIC 2022',
                'cycle': 3,
                'sprint': 3
            }
        }
        return Response(data=response, status=status.HTTP_200_OK)