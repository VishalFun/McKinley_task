from rest_framework import viewsets
from .models import UserATM
from . import serializers as model_serializer
from rest_framework.response import Response


def user_authentic(card,pin):
    try:
        res = UserATM.objects.get(user_card=card,pin=pin)
        return res
    except:
        return None

class UserATMView(viewsets.ModelViewSet):
    queryset = UserATM.objects.all()
    serializer_class = model_serializer.UserATMSerializer

class AuthenticUserView(viewsets.ViewSet):
    def list(self,request):
        serializer = model_serializer.UserAuthenticSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        card = data['card']
        pin = data['pin']
        res = user_authentic(card,pin)
        if(res):
            result = True
        else:
            result = False
        return Response({
            "status":"ok",
            "result":result
            })

def notes_dispatch(amount):
    note = {}
    notes = [2000,500,200,100,50,20,10,5,2,1]
    for i in notes:
        res = amount//i
        if(res!=0):
            note[i]=res
        amount = amount%i
    return note
    
class UserWithDrawal(viewsets.ViewSet):
    def list(self,request):
        serializer = model_serializer.UserAmountSerial(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data
        card = data['card']
        pin = data['pin']
        balance = data['balance']
        msg = "WithDrawal Success"
        result=False
        if(float(balance)>20000):
            return Response({
                    "status":"ok",
                    "result":True,
                    "message":"Cannot withdraw more than 20,000 in single transaction"})
        try:
            res = user_authentic(card,pin)
            if(res.balance>=float(balance)):
                bal = float(res.balance) - float(balance)
                res.balance = bal
                res.save()
                notes = notes_dispatch(int(balance))
                return Response({
                    "status":"ok",
                    "result":True,
                    "message":msg,
                    "balance_left":bal,
                    "notes_contain":notes,
                    })
            else:
                msg = "Not Enough Balance to perform withdrawal"
        except Exception as e:
            print(e)
            msg = "Card or PIN is incorrect."
            
        return Response({
            "status":"ok",
            "result":result,
            "message":msg,
            })

class DepositMoney(viewsets.ViewSet):
    def list(self,request):
        serializer = model_serializer.UserAmountSerial(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        card = data['card']
        pin = data['pin']
        balance = data['balance']
        res = user_authentic(card,pin)
        if(res):
            bal = float(res.balance)+ float(balance)
            res.balance =  bal
            res.save()
            return Response({
                    "status":"ok",
                    "result":True,
                    "message":"Balance Updated",
                    "current_balance":bal,})
        else:
            return Response({"status":"ok",
                                 "result":False,
                                 "message":"Input Valid card number or pin."
                                 })
            
            




        
