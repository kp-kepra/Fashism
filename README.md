# FASHISM

Frontend repository for latest fashion trends based on pop-stars.
The fashion ranking is made in Caffe.

![alt text](https://github.com/KP-Kepra/Fashism/blob/master/page.png)

## Features
* Uses Caffe and PyFaster RCNN to compute the rankings of latest fashion trends
* Displays the rankings in related fashion images on the Fashism Website

## Installation

*  Install yarn globally by `npm install yarn -g`
*  `yarn install`
*  `yarn start`
*  Open 'localhost:8080' to open the app

## Fashion Detection
*  Requires [Caffe](http://caffe.berkeleyvision.org/) and [PyFaster RCNN](https://github.com/rbgirshick/py-faster-rcnn) to be installed.
*  The Python folder contains fashion_detector.prototxt to specify the model.
*  Run the detect-fashion.py (Needs some adjustments in path locations).

## Credits
Template is based from [react-redux-template-for-ecommerce-site](https://github.com/arshdkhn1/ecommerce-site-template)
