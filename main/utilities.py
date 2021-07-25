import pickle
from sklearn.svm import SVC
from django.conf import settings
from django.core.mail import EmailMessage


def get_predictions(values):
    svm_model = pickle.load(
        open('main/static/model/svm_model.sav', 'rb'))
    knn_model = pickle.load(
        open('main/static/model/knn_model.sav', 'rb'))
    naiveBayes_model = pickle.load(
        open('main/static/model/naiveBayes_model.sav', 'rb'))
    resultList = [svm_model.predict(values)[0], knn_model.predict(values)[
        0], naiveBayes_model.predict(values)[0]]
    result = max(set(resultList), key=resultList.count)
    return result


def send_email(result, images, managements, symptoms, treatments, email):
    subject = 'Online Email'
    message = f'''Hi from Farm Disease Predictor,
    The Predicted disease is {result}

    Managements : {managements}
    Symptoms : {symptoms}
    Treatments and Pesticides : {treatments}
    '''
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    mail = EmailMessage(subject, message, email_from, recipient_list)
    if(images != '...'):
        mail.attach_file(f'main/static/img/{images}')
    mail.send()


def get_info(result):
    if result == 'Bacterial Blight':
        image = 'bacterialblight.jpeg'
        managements = '''
        1. Wide row spacing.
        2. Selection of disease free seedlings for fresh planting.'''
        symptoms = '''
        1. Appearance of one to several small water soaked, dark colored irregular spots on leaves resulting in premature defoliation under severe cases. 
        2. The pathogen also infects stem and branches causing girdling and cracking symptoms. 
        3. Spots on fruits were dark brown irregular slightly raised with oily appearance, which split open with L-shaped cracks under severe cases.'''
        treatments = '''
        1.Before pruning it should be sprayed with 1% Bordeaux mixture. 
        2.After Ethrel spraying Paste or smear with 0.5g Streptomycin Sulphate + 2.5g Copper oxy chloride + 200g red oxide per lit of water.'''
    elif result == 'Wilt':
        image = 'wilt.jpeg'
        managements = '''
        Do not allow water to stagnate, try to create drainage facility'''
        symptoms = '''
        Affected plants show yellowing of leaves in some twigs or branches, 
        followed by drooping and drying of leaves. The entire tree dies in few months or a year. 
        When affected tree is cut open lengthwise or cross-section dark grayish-brown discolouration 
        of wood is seen.'''
        treatments = '''
        1. At initial stage drench 2ml Propiconazole + 4ml Chloropyriphos per litre water solution, drench 8-10 lit of solution per tree. 
        2. Drench with Formaldehyde @ 25 ml/l.'''
    elif result == 'Fruit Borer':
        image = 'fruitborer.jpg'
        managements = '''
        1.Clean cultivation and aintenance of health and vigour of the tree should be followe
        2.The fruits if screened with polythene or paper bags may escape infestation. 
        3.Removal and destruction of all the affected fruits.'''
        symptoms = '''
        Dark brown, short and stout, covered with short hairs, larval period lasts for 18-47 days.'''
        treatments = '''
        1.Spray Dimethoate 0.06% prior to flowering is important 
        2.In severe condition spray methyl oxy-demeton 0.05% and repeat after fruit set.
        3.Spraying of Melathion 1ml/lit'''
    elif result == 'Fungal Spot':
        image = '...'
        managements = ""
        symptoms = ""
        treatments = ""
    elif result == 'Fito Flora Blight':
        image = '...'
        managements = ""
        symptoms = ""
        treatments = ""
    else:
        image = '...'
        managements = ""
        symptoms = ""
        treatments = ""
    return image, managements, symptoms, treatments
