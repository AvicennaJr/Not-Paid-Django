from django.shortcuts import render
import datetime


check_pay_date =  datetime.datetime.now() + datetime.timedelta(days=100) # 100 days to pay day


def index(request):

    # Opacity will be equal to the total number of days left to payment

    opacity = (check_pay_date - datetime.datetime.now()).days

    return render(request, index.html, {"opacity": opacity})