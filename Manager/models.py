from django.db import models


class Room(models.Model):

    Room_Number = models.IntegerField()
    Room_Type = models.CharField(max_length=100)
    Price_Per_Day = models.IntegerField()
    Available = models.BooleanField(default=True)

    def __str__(self):
        return str(self.Room_Number)


class Booking(models.Model):

    Customer_Name = models.CharField(max_length=200)
    Mobile = models.CharField(max_length=15)

    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE
    )

    Check_In = models.DateField()
    Check_Out = models.DateField()

    Total_Amount = models.IntegerField(default=0)

    def __str__(self):
        return self.Customer_Name