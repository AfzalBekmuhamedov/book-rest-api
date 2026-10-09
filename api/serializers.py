from datetime import date
from rest_framework.fields import CharField,IntegerField,DateField
from rest_framework.serializers import ModelSerializer, ValidationError
from .models import *

def check_last_name(value):
    if len(value) < 3:
        raise ValidationError("Noto'g'ri ism kiritildi")
    return value

class AuthorSerializer(ModelSerializer):
    last_name = CharField(max_length=100,validators=[check_last_name])
    class Meta:
        model = Author
        fields = ['id','first_name','last_name']

    def validate_first_name(self, value):
        if len(value) < 3:
            raise ValidationError("Noto'g'ri ism kiritildi")
        return value

    def validate(self, attrs):
        if attrs['first_name'] == attrs['last_name']:
            raise ValidationError("Bir xil bo'lishi mumkin emas")
        return attrs


def check_title(value):
   if len(value) < 3:
       raise ValidationError("Kitob nomi noto'g'ri kiritildi")
   return value

def check_price(value):
    if value == 0:
        raise ValidationError("Kitob tekin emas")
    return value

def check_time(value):
    if value >= date.today():
        raise ValidationError("Qanday qilib kitob bugun yoki kelajakda chiqishi mumkin ?")
    return value

class BookSerializer(ModelSerializer):
    title = CharField(max_length=100, validators=[check_title])
    price = IntegerField(validators=[check_price])
    published_at = DateField(validators=[check_time])
    class Meta:
        model = Book
        fields = ['id','title','author','price','published_at']