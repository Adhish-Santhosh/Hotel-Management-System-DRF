from rest_framework import serializers
from .models import Room, Booking


class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = '__all__'

    def create(self, validated_data):

        room = validated_data['room']

        check_in = validated_data['Check_In']
        check_out = validated_data['Check_Out']

        days = (check_out - check_in).days

        validated_data['Total_Amount'] = (
            days * room.Price_Per_Day
        )

        return Booking.objects.create(**validated_data)