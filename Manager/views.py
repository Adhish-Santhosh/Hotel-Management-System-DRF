from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Room, Booking
from .serializers import RoomSerializer, BookingSerializer


class RoomAPI(APIView):

    def get(self, request):

        data = Room.objects.all()

        serializer = RoomSerializer(data, many=True)

        return Response(serializer.data)

    def post(self, request):

        serializer = RoomSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors)


class BookingAPI(APIView):

    def get(self, request):

        data = Booking.objects.all()

        serializer = BookingSerializer(data, many=True)

        return Response(serializer.data)

    def post(self, request):

        serializer = BookingSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors)


class UpdateBookingAPI(APIView):

    def put(self, request, id):

        try:
            booking = Booking.objects.get(id=id)

        except Booking.DoesNotExist:
            return Response({"Error": "Booking not found"})

        serializer = BookingSerializer(
            booking,
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors)


class DeleteBookingAPI(APIView):

    def delete(self, request, id):

        try:
            booking = Booking.objects.get(id=id)

        except Booking.DoesNotExist:
            return Response({"Error": "Booking not found"})

        booking.delete()

        return Response({"Message": "Booking Deleted Successfully"})