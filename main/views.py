from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, request
from .models import Farmer, Counselor, PredictedDisease
from .forms import ClimateData
from .utilities import get_info, get_predictions, send_email


def index(request):
    if request.method == 'POST':
        form = ClimateData(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            values = list(data.values())
            values, email = values[:3], values[-1]
            result = get_predictions([values])
            PredictedDisease(prediction=result).save()
            last_6_days = PredictedDisease.objects.order_by(
                '-day_timestamp')[:6]
            hasDisease = True
            prev_d = last_6_days[0].prediction
            for d in last_6_days:
                if prev_d != d.prediction:
                    hasDisease = False
            if hasDisease == False:
                result = "No"
                image = "..."
            image, managements, symptoms, treatments = get_info(result)
            if(result != 'No'):
                send_email(result, image, managements,
                           symptoms, treatments, email)
            return render(request, 'main/result.html', {'result': result, 'image': image, 'managements': managements, 'symptoms': symptoms, 'treatments': treatments, })
    else:
        form = ClimateData()
    return render(request, 'main/index.html', {'form': form})


def farmerdetails(request):
    farmers = Farmer.objects.all()
    params = {'farmers': farmers}
    return render(request, 'main/farmer.html', params)


def counselordetails(request):
    counselors = Counselor.objects.all()
    params = {'counselors': counselors}
    return render(request, 'main/counselor.html', params)
