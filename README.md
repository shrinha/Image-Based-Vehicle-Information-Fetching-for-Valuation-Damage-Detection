# Image-Based-Vehicle-Information-Fetching-for-Valuation-Damage-Detection
Repository for the prototype submission of the National Finale of TVS Credit E.P.I.C IT 5.0 Challenge.
The Challenge aimed at identifying areas of improvement, coming up with innovative solutions, and developing a prototype for the firm 

## Abstract & Idea
During the case study round, we identified an area of improvement in the valuation domain. TVS Credit, an NBFC focusing primarily on vehicle and used vehicle loans, did have a system for vehicle valuation on its website. However, it depended heavily on the need to know about the specifics of the vehicle, such as its variant and model, before going forward. Subsequently, an IBB Price is returned, which is highly static and does not capture market dynamics well. Moreover, there's no such system for mobile applications where cameras can be used "on the fly" to check the vehicle's damage/condition.

Further explanation of the topic, its motivation, and a walkthrough can be found in the Presentation inside the Abstract & Ideas Directory.  
The rough framework of the model is below.


![Framework](https://github.com/shrinha/Image-Based-Vehicle-Information-Fetching-for-Valuation-Damage-Detection/blob/main/Abstract%20%26%20Presentation/Framework.jpg)

## Colab Notebooks 
The Directory consists of all the ipynb files for building the various models.   

### Part A: Information Fetching
The Dataset can be found here: https://drive.google.com/drive/folders/1LTQlHwB_PUSlybd_2xLF9uYYo5vTCf-t?usp=sharing.  
Three ipynb files are used for this. First, the XML_to_Csv notebook creates data frames and saves the label in CSV format. The object_detection file consists of training several models (MobileNetV2, InceptionV3, InceptionResNetV2) for segmenting the number plate from the image and choosing the best one. The Make Predictions is used to feed the test image and extract the number plate as strings from the segmented image.

### Part B: Damage Assessment 
The Dataset can be found here: https://drive.google.com/drive/folders/1L9MndprxDAI98seN1qu-F613eocQ2NfA?usp=sharing    
This Part has 4 Google Colab Notebooks. The first three each aim to answer the following question: 
  
* If the car is damaged or not.  
* The Location of Damage (side/rear/front).   
* The Severity of The Damage (severe, moderate, minor).  
    
 A VGG16 Architecture with our own fine-tuning layers is used for these tasks. Lastly the test_damage_models file loads all of these and test it on an image.

### Part C: Feeding the Data into an Existing Price Regressor Model

All the Data thus compiled can be fetched directly into an existing regressor model (an example of which we've provided below) or be used in tandem with the IBB Pricing tool available for easy automation.  

Link to example Price Regressor Model: https://colab.research.google.com/drive/1Qs4bowVTbJdElrpEfN6ytHjTF-5_fibU?usp=sharing (An accuracy of )

## Building the Web App
Flask is used to render the HTML files inside the template directory and send the uploaded image to run the models on it. The deeplearning.py files consist of the function definitions for this task.

## API Call 
We've used the following API to get the required information from the number plate and then display it back on our web app :   
https://rapidapi.com/flashbomberapp/api/rto-vehicle-details  
This was tested using Thunderclient. The test.py file contains the function definition for sending the packaged payload and returning the required information from the API.









