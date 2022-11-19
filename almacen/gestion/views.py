from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import PruebaSerializer, DepartamentoSerializer
from .models import DepartamentoModel
from rest_framework import status

@api_view(http_method_names=['GET', 'POST'])
def saludar(request: Request):
    print(request.data)
    print(request.query_params)
    if request.method == 'GET':
        return Response(data={'saludo': 'Hola mundo'}, status=200)
    elif request.method == 'POST':
        body = request.data
        nombre = body.get('nombre')
        return Response(data={
            'message': f'Hola {nombre}'
        })
        
@api_view(http_method_names=['GET'])
def parametros(request: Request,nombre):
    print (nombre)
    return Response(data={
        'message': 'bienvenido al endopont de parametros'
    })
    
class PruebaApiView(ListCreateAPIView):
    
    serializer_class = PruebaSerializer
    queryset = [
        {
            'nombre': 'Juan',
            'apellido': 'Perez'
        },
        {
            'nombre': 'Jesus',
            'apellido': 'Pez'
        },
        {
            'nombre': 'Jan',
            'apellido': 'Rerez'
        }
        
    ]
    def post(self, request: Request):
        print (request.data)
        body = request.data
        serializador = PruebaSerializer(data=body)
        dataValida = serializador.is_valid()
        if not dataValida:
            return Response(data= { 'message': 'Error en los datos' , 'content' : serializador.errors})
        else: 
            print(serializador.validated_data)
            self.queryset.append(serializador.validated_data)
            return Response(data={ 'message': 'Usuario agregado exitosamente'}, status=status.HTTP_201_CREATED)
        

class DepartamentosApiView(ListCreateAPIView):
    serializer_class = DepartamentoSerializer
    queryset = DepartamentoModel.objects.all()
    
    
class DepartamentoDetalleApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = DepartamentoSerializer
    queryset = DepartamentoModel.objects.all()