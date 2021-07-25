from django import forms


class ClimateData(forms.Form):
    temperature = forms.IntegerField(label='Temperature(°C)', widget=forms.TextInput(
        attrs={'class': 'form-control', 'type': "number", 'id': "temperature", 'placeholder': 'eg. 50'}))
    moisture = forms.IntegerField(label='Moisture(%)', widget=forms.TextInput(
        attrs={'class': 'form-control', 'type': "number", 'id': "moisture", 'placeholder': 'eg. 50', 'min': 0, 'max': 100}))
    humidity = forms.IntegerField(label='Humidity(%)', widget=forms.TextInput(
        attrs={'class': 'form-control', 'type': "number", 'id': "humidity", 'placeholder': 'eg. 50', 'min': 0, 'max': 100}))
    email = forms.EmailField(label="Email", widget=forms.TextInput(
        attrs={'class': 'form-control', 'type': "email", 'id': "email", 'placeholder': 'eg. abc@email.com'}))
