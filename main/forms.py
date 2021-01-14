from django import forms


class ClimateData(forms.Form):
    temperature = forms.IntegerField(
        label='Temperature', widget=forms.TextInput(attrs={'class': 'form-control',
                                                           'type': "number", 'id': "temperature", 'placeholder': 'In Degree Celcius'}))
    moisture = forms.IntegerField(label='Moisture', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                  'type': "number", 'id': "moisture", 'placeholder': 'In Percentage', 'min': 0, 'max': 100}))
    humidity = forms.IntegerField(label='Humidity', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                  'type': "number", 'id': "humidity", 'placeholder': 'In Percentage', 'min': 0, 'max': 100}))
