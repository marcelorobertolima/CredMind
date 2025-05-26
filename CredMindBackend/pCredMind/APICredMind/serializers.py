from rest_framework import serializers
from django.contrib.auth.models import User

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.contrib.auth import authenticate
from datetime import datetime
import pytz

from APICredMind.models import Consultas
from APICredMind.models import Analises
from APICredMind.models import ProspecSERASA
from APICredMind.models import EnriquecimentoCNAECedentesOpera
from APICredMind.models import Relatorios

#########################################################################################
#########################################################################################
#########################################################################################
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']

#########################################################################################
#########################################################################################
#########################################################################################
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    email = serializers.EmailField(required=True)

    def validate(self, attrs):
        credentials = {
            'email': attrs.get('email'),
            'password': attrs.get('password')
        }

        if all(credentials.values()):
            user = authenticate(email=credentials['email'], password=credentials['password'])

            if user is None or not user.is_active:
                raise serializers.ValidationError('Nenhuma conta ativa encontrada com as credenciais fornecidas')

            refresh = self.get_token(user)
            access_token = refresh.access_token

            data = {
                'Token': str(access_token),
                'refesh_token': str(refresh),
                'DataExpiracao': datetime.fromtimestamp(access_token['exp'], pytz.UTC).strftime('%Y-%m-%d %H:%M:%S %Z')
            }

            return data
        else:
            raise serializers.ValidationError('É necessário fornecer "email" e "senha".')

#########################################################################################
#########################################################################################
#########################################################################################
class ConsultasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultas
        fields = '__all__'

#########################################################################################
#########################################################################################
#########################################################################################
class ProspecSERASASerializer(serializers.ModelSerializer):
    class Meta:
        model = ProspecSERASA
        fields = '__all__'

#########################################################################################
#########################################################################################
#########################################################################################
class AnalisesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analises
        fields = '__all__'

#########################################################################################
#########################################################################################
#########################################################################################
class EnriquecimentoCNAECedentesOperaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnriquecimentoCNAECedentesOpera
        fields = '__all__'

#########################################################################################
#########################################################################################
#########################################################################################
class RelatoriosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relatorios
        fields = '__all__'