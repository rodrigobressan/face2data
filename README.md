# Face2Data: Extract meaningful information from a person face in less than a second

## Overview

This project is intended to showcase the adoption of Keras multi-output models to predict age, gender and race from a given persons face. The generated model is
served through a REST API with Flask.

## The dataset

 The UTKFace dataset is a large dataset composed of over 20 thousand face images with their respective annotations of age, gender and ethnicity. The images are properly cropped into the face region, but display some variations in pose, illumination, resolution, etc. If you want to know more about this dataset, please check their website.

<div style="width: 100%; text-align: center">
    <img style='width: 80%; object-fit: contain' src="/images/utk_dataset.jpg"/>
</div>

<br/>

## Training phase

Our Neural Network is composed of three major branches, one for each of the features we are trying to predict. We have used a default set of hidden layers, based on the stacking of several Conv2D with ReLU activation, followed by a Batch Normalization, then a MaxPooling and finally a Dropout layer. The full Neural Network architecture can be seen below:


<div style="width: 100%; text-align: center">
    <img style='width: 80%; object-fit: contain' src="/images/model.png"/>
</div>

We performed our training phase by adopting an Adam optimizer with a learning rate of 1e-4 and a decay based on the initial learning rate divided by the number of epochs. A hundred epochs were used to train our model, in which we have seen that we had an efficient learning process, asserted by plotting both the accuracy and loss curves, as shown below:


<div style="width: 100%; text-align: center">
    <img style='width: 80%; object-fit: contain' src="/images/acc_gender.png"/>
</div>


<div style="width: 100%; text-align: center">
    <img style='width: 80%; object-fit: contain' src="/images/acc_race.png"/>
</div>


<div style="width: 100%; text-align: center">
    <img style='width: 80%; object-fit: contain' src="/images/mae_age.png"/>
</div>


<div style="width: 100%; text-align: center">
    <img style='width: 80%; object-fit: contain' src="/images/overall_loss.png"/>
</div>

## TODO

- Add some unit tests for both Flask application and model predictions
- Setup Continuous Integration and Deployment
- Add SHAP for model explainability

## References

UTK Face Dataset: [http://aicip.eecs.utk.edu/wiki/UTKFace](http://aicip.eecs.utk.edu/wiki/UTKFace)

Keras Multi-output documentation: [https://keras.io/getting-started/functional-api-guide/](https://keras.io/getting-started/functional-api-guide/)

SanjayaSubedi post on multi-output model: [https://sanjayasubedi.com.np/deeplearning/multioutput-keras/](https://sanjayasubedi.com.np/deeplearning/multioutput-keras/)

PyImageSearch post on FashionNet: [https://www.pyimagesearch.com/2018/06/04/keras-multiple-outputs-and-multiple-losses/](https://www.pyimagesearch.com/2018/06/04/keras-multiple-outputs-and-multiple-losses/)

Plotly: [https://plot.ly/](https://plot.ly/)
