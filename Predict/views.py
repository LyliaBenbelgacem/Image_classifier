from django.shortcuts import render
from .forms import ImageForm
from .models import ImageModel
import cv2 as cv
import numpy as np
import pickle
from PIL import Image
import joblib
# Create your views here.

def predict(request):

    if request.method=='POST':
        form = ImageForm(request.POST, request.FILES)


        

        if form.is_valid():
            saved_form = form.save(commit = False)
            image_file = Image.open(saved_form.model_image)
            np_image = np.asanyarray(image_file)
            resized = cv.resize(np_image, (300,300))
            img_2_channels = resized[:,:,0]
            final_img = img_2_channels.reshape(1,300,300,1)

            loaded_model = joblib.load("./saved_model/model.joblib")

            prediction = loaded_model.predict(final_img) 
            image_class = np.argmax(prediction)
            if image_class==0:
                Class = "paper"
            elif image_class == 1:
                Class ="Scissors" 
            else:       
                Class ="Rock"
            saved_form.save()
            return render(request, "Predict/result_template.html", {"form" : form, "class": Class })

    else:
        form = ImageForm()        


    return render(request,"Predict/base_template.html",{"form" : form})