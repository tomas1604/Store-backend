from authApp.models.account import Account
from authApp.models.user import User
from .accountSerializer import AccountSerializer
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    account = AccountSerializer()
    class Meta:
        model = User
        fields = ['id', 'username','password','name','email','account']
    
    def create(self, data): #DESERIALIZACIÓN
        accountData = data.pop('account') 
        userObject = User.objects.create(**data)
        Account.objects.create(**accountData,user = userObject)
        return userObject   

    def to_representation(self, instance): #SERIALIZACIÓN
        userObj = User.objects.get(id = instance.id )
        account = Account.objects.get(user = instance.id)
        return {
            'id': userObj.id,
            'username': userObj.username,
            'name': userObj.name,
            'email': userObj.email,
            'account':{
                'id': account.id,
                'balance': account.balance,
                'lastChangeDate': account.lastChangeDate,
                'isActive': account.isActive
            }
        }