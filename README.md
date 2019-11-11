# Face2Data: Extract meaningful information from a person face in less than a second

## Overview

This project is intended to showcase the adoption of Keras multi-output models to predict age, gender and race from a given persons face. The generated model is
served through a REST API with Flask.

## The dataset

 The UTKFace dataset is a large dataset composed of over 20 thousand face images with their respectivce annotations of age, gender and ethnicity. The images are properly cropped into the face region, but display some variations in pose, illumination, resolution, etc. If you want to know more about this dataset, please check their website.

<div style="width: 100%; text-align: center">
    <img style='width: 80%; object-fit: contain' src="/images/utk_dataset.jpg"/>
</div>

<br/>


## TODO:

- Unit Testing
- CI/CD for Heroku

## References

UTK Face Dataset: [http://aicip.eecs.utk.edu/wiki/UTKFace](http://aicip.eecs.utk.edu/wiki/UTKFace)

Keras Multi-output documentation: [https://keras.io/getting-started/functional-api-guide/](https://keras.io/getting-started/functional-api-guide/)

SanjayaSubedi post on multi-output model: [https://sanjayasubedi.com.np/deeplearning/multioutput-keras/](https://sanjayasubedi.com.np/deeplearning/multioutput-keras/)

PyImageSearch post on FashionNet: [https://www.pyimagesearch.com/2018/06/04/keras-multiple-outputs-and-multiple-losses/](https://www.pyimagesearch.com/2018/06/04/keras-multiple-outputs-and-multiple-losses/)

Plotly: [https://plot.ly/](https://plot.ly/)
