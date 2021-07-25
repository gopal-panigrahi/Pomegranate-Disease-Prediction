from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Farmer, Counselor, PredictedDisease
from .forms import ClimateData
from .predictions import get_predictions


def index(request):
    if request.method == 'POST':
        form = ClimateData(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            result = get_predictions([list(data.values())])
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
            if result == 'Bacterial Blight':
                image = 'bacterialblight.jpeg'
            elif result == 'Wilt':
                image = 'wilt.jpeg'
            elif result == 'Fruit Borer':
                image = 'fruitborer.jpg'
            elif result == 'Fungal Spot':
                image = '...'
            elif result == 'Fito Flora Blight':
                image = '...'
            else:
                image = '...'

            return render(request, 'main/result.html', {'result': result, 'image': image})
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
