# DAIM (Imaging) Learning Outcomes

This document details the high level learning outcomes for each seminar and workshop in the course.

The following learning levels (LLs) should be able to be mapped to the learning points. 
1. **Level 1 - Basic Practical Skills (coding skills)** \* E.g. How to reshape a numpy array from `(3, 3, 3)` into `(9, 3)`. 
2. **Level 2 - Theory (modelling skills)** \* E.g. How k-means splits data up into clusters 
3. **Level 3 - Project Planning and Management** \* E.g. How to write a class for plotting similar plots when opening a DICOM file. 
4. **Level 4 - Clinical Translation** \* E.g. What format data needs to be collected in to train a clinical outcome predictor from chest x-ray data.

The seminars will consist mainly of LL2 and LL4 information, whereas workshops will consist of LL1 and LL3 information. The workshops at the start of the course should feature extension tasks which are more complex for people to work through in the workshops if they finish the content before the workshop happens.

# Overall Structure

-   The course will be split into the following modules:
    -   Module 1 - Introduction (no workshop)
    -   Module 2 - Core Python for Image Processing
        -   This can be stretched over multiple weeks depending on the skills and level of the people on the course
    -   Module 3 - Python and DICOM
        -   This will include the coding skills needed to open and use DICOM files
        -   The workshop will include a mixture of work to do outside a session and tasks to do within a session with a tutor.
    -   Module 5 - AI for Medicine 
        -   This will be a set of two or more seminars with a long workbook that will be worked through over multiple weeks
        -   The work in the workbook will be mostly independent.
    -   Module 6 - Closing (no workshop)

# Module 1 - Course Introduction

## Seminar

By the end of the seminar, clinicians should be able to: 
- Know the overall aims and philosophy of the course 
- Aims of the DAIM courses 
    - Translate a basic knowledge of Python into workable clinical skill 
    - Inspire the individual to seek further resources to learn more about the topic 
    - Empower the learner to build complex applications 
- General coding information 
    - Know the layout of documentation and how to use it (LL3) 
    - Know what StackOverflow is and when to use it (LL3) 
    - Understand what constitutes "machine readable" data and what considerations clinicians must make to maximise this (LL4)

# Module 2 - Core Python for Image Processing

## Seminar

By the end of the seminar, clinicians should:

-   Know general uses of image data in clinical settings
-   Digital image representation
    -   Understand what a pixel is, and the values it can take on (0.0-1.0, 0-255) (LL2)
    -   Understand the difference between greyscale and colour images (LL2)
    -   Understand how brightness maps on value (LL2)
    -   Understand different ways to represent colours (RGB, HSV) (LL2)
    -   Be able to read a hex colour code (LL2)
    -   Understand what the dimensions of an image represent (LL2)
    -   Understand what the difference between compressed and uncompressed images are (LL2) 
    -   Understand the difference between lossy and lossless compression (LL2)
    -   Be able to list different image formats (LL2)
    -   Understand how these concepts extend to 3D images (volumetric images) (LL2)
-   Transforms
    -   Be able to state what a transform is (LL2)
-   Convolution
    -   Understand why convolution has been chosen as the example transform for this course (LL2)
        -   Use in ML, easy to visualise
    -   Understand what convolution is and what it is used for (LL2)
    -   Understand what a convolution kernel is (LL2)
    -   Understand what types of operation can be done with convolution (blurring, sharpening) (LL2)
    -   Understand intuitively how to average a signal using an averaging kernel e.g. `[0.2, 0.2, 0.2, 0.2, 0.2]` (LL2)
    -   Appreciate that convolution can be used in less than or more than 2 dimensions (LL2)
-   Basics of PIL (LL1)
    -   Why PIL is valuable in the Python ecosystem (LL3)
    -   The sorts of operations that PIL can do (LL1)

-   Basics of NumPy (LL1)
    -   Know why NumPy exists within the Python ecosystem (speed of array operations, ease of working with multidimensional data) (LL2)
    -   Understand the concept of multidimensional arrays and the 'shape' of an array (LL2)
    -   Explain what a NumPy array is (LL2)
    -   Understand how to use NumPy functions and common pitfalls e.g. shape mismatches (LL1)
-   Explain how to represent common data structures as NumPy data (quiz-style questions to test understanding) (LL2)
    -   Image data - NumPy array

## Workshop

The aim of this workshop is to recap some basic Python skills and to ensure that course attendees have the appropriate knowledge of core packages before starting more in-depth content. The NumPy section will focus on combining and modifying arrays and using basic library functions. An task using convolution will be used to demonstrate this to conceptually prepare for the machine learning section of the course.

Use an example X-ray image with a simulated CSV file describing an imaginary small dataset of patients.

By the end of the workshop, clinicians should be able to:

-   Basics of PIL
    -   Open an image from disk with PIL (LL1)
    -   Show an image with PIL (LL1)
    -   Rotate an image with PIL (LL1)
    -   Crop an image with PIL (LL1)
    -   Convert to greyscale with PIL (LL1)
    -   Understand the internal representation of images within PIL (LL1)
-   NumPy
    -   Open a CSV file into a NumPy array (LL1)
    -   Convert a column of a DataFrame to a NumPy array (LL1)
    -   Print the shape of a NumPy array (LL1)
    -   Accessing array elements using array slicing (e.g. `[0:4]`, `[:-1]`)
    -   Count the number of unique items in an array with `numpy.unique()` (LL1)
-   Convolution example task (LL1)
    -   Create a new array (convolution kernel) of ones of a specified shape (LL1)
    -   Divide this new array by its length (LL1)
    -   Convolve the kernel with the NumPy array using `np.convolve()` (LL1)
    -   Display this image with PIL (LL1)
    -   Smooth an image with PIL and a custom convolution kernel (LL1)
    -   Sharpen an image with PIL and a custom convolution kernel (LL1)
    -   Combine all of these into a function which takes an argument to specify a type of operation to perform (LL1)

# Module 3 - Python and DICOM

The aim of this module is to give clinicians an introduction into the DICOM file format, what type of data is represented in this file format, and how to extract basic 2D and 3D image data from these files. 

***N.B.** The interpretation of images in any form will not be covered in this unit.*

## Seminar

By the end of the seminar, clinicians should:

-   Understand the aims of this module (LL4)
-   Basics of image representation (LL2)
    -   Understand what a pixel is (LL2)
    -   Understand what a voxel is, by extension (LL2)
    -   Greyscale images
        -   Understand what values greyscale values are are usually given in (0.0-1.0, 0-255, HU) (LL2)
        -   Understand what a Houndsfield Unit is (LL2)
    -   Colours
        -   Understand how RGB data is used to represent most images (LL2)
        -   Understand what a colourmap is and when it is used (LL2)
-   The DICOM format
    -   Know the history of the DICOM standard and why it was introduced (LL4)
    -   Understand what information is contained within a DICOM file (LL2)
    -   Understand that DICOM is a lossless standard (LL2)
    -   Understand broadly how a DICOM file stores image data (both 2D and 3D) (LL2)
    -   Understand why Pydicom is a useful tool for clinicians (LL4)
-   Understand what considerations are needed when coding in Python to convert images, with interactive questions (array shapes) (LL3)
-   Understand the difference between volumetric 3D images and 3D meshes and what is needed to convert between them (segmentation)
-   Understand the basics of image segmentation in 2D and 3D (LL2)
-   Understand where volumetric imaging is used and where mesh reconstructions are used in clinical medicine (LL4)

## Workshop

By the end of the workshop, clinicians should be:

-   Open a DICOM file with Python (LL1)
-   Scan information
    -   Understand that there are three different types of element in a DICOM file (LL2)
    -   Understand different ways to access elements (by hex tag and keyword) (LL2)
    -   Extract basic scan information by keyword e.g. `PatientName` (LL1)
-   Image extraction
    -   Understand what data is needed to accurately reconstruct data from a DICOM study for 3D and 2D images (image shape, slice indices) (LL1)
    -   Extract 2D image data into a NumPy array using `ds.pixel_array` (LL1)
    -   Extract 2D colourmap data (*e.g. Doppler flow rate data*) and plot this appropriately (LL1)
    -   Reconstruct 3D image from a DICOM study and [plot axial, sagittal and coronal views](https://pydicom.github.io/pydicom/stable/auto_examples/image_processing/reslice.html#sphx-glr-auto-examples-image-processing-reslice-py) (LL1)
    -   Preprocess the image for display in Python (LL1)
    -   Plot image data from a DICOM file in Python (LL1)

We need a candidate DICOM study/studies for this portion of the course. Options include: 
- [Patient Contributed Image Repository](https://www.pcir.org/) - This is where Pydicom gets it's official example studies. 
- Pydicom's official test files

We need the following studies: 
- 2D basic scan (e.g. CXR) 
- 3D volumetric scan (e.g. CT head)

*We could also add an extra section to the end to work with colourmaps. This would need imaging with colour data - e.g. ultrasound with flow data.*

# Session 4 - AI for Medicine

## Seminar 1 

By the end of the first seminar, clinicians should:

-   Understand the aims of this first AI module and what it will cover
-   Understand what machine learning is at a broad level (LL2)
-   Be able to list clinical uses for ML (LL4)
-   Be able to describe the high-level steps needed to train a statistical model (collect data, preprocess data, augment data, define model, compile model, train model, evaluate model) (LL2) 
-   Datasets
    -   Understanding the importance of splitting the data into training, testing, and validation datasets (LL2)
    -   Understand dataset bias and clincial factors that can confound a dataset (LL4)
    -   Use examples to demonstrate clinical bias *TODO find appropriate examples* (LL4) 
-   Be able to relate the aims of the example task (Pneumonia detection task) (LL4)
    -   Disclaimer that this course will not cover intepretation of chest X-rays
-   Data preprocessing
    -   Understand considerations that must be made when standardising image data for model input (image size, image dimensions, contrast, brightness) (LL2)
    -   Understand the importance of data augmentation when training (LL2)
    -   Be able to name common data augmentation techniques (shearing, rotation, stretching, elastic deformation in medical imaging datasets) (LL2)
    -   Understand how these concepts apply to other types of data (e.g. time-series data) (LL2)
-   Classifier evaluation
    -   Evaulating models 
    -   Describe methods for evaulating regression models (LL2) 
    -   Be able to describe important metrics for a classifier (positive/negative predictive value, sensitivity and specificity) (LL2) 
    -   Be able to describe the statistical tests needed to evaluate a binary classifier (F1 score, AUC and ROC curves) (LL2) 
    -   Be able to give a broad overview of the common metrics that are used with other types of model (softmax for multiclass classifiers, pixel accuracy and intersection over union (IoU) for segmentation) (LL2)    

## Seminar 2

By the end of the seminar, clinicians should: 

-   Understand the difference between supervised and unsupervised learning (LL2)
-   Understand what a loss function is (LL2)
    -   Appreciate that there are a wide variety of optimisers and loss functions that can be used (LL2)
-   Gain an intuition for how training via backpropagation works via the ball on a hill analogy (LL2)
- Gain an intuitive understanding of overfitting vs overfitting using a linear model as an example (LL2) 
-   Model architecture and training
    -   Understand why ML frameworks exist in the Python ecosystem (TensorFlow, PyTorch) and what they allow the user to do (LL2)
    -   Understand the inputs and outputs of a neural network (LL2)
    -   Understand the difference between a convolutional layer and dense layer at a broad level (LL2)
    -   Understand what an epoch of training is (LL2)
    -   Understand why data needs to be batched when training a network (LL3)
    -   Understand what a sigmoid layer is and why it is used for probabilistic outputs (LL2)
-   Hyperparameters 
    -   Understand what a hyperparameter is (LL2) 
    -   How a hyper-parameter effects model output (LL2) 
    -   Understand that hyperparameters can be tuned (LL2) 
- Common pitfalls 
    -   How to deal with overfitting. (LL2) 
    -   How to deal with multicollinearity (LL2) 
    -   How to deal with missing data and sensitivity analysis (LL2)
-   Appreciate that the task we are performing is fairly simple and that more complex techniques exist (LL2)
-   Be able to discuss the uses, advantages, and disadvantages of more modern approaches to machine learning (stable diffusion, large language models) (LL2) (LL4)

*Maybe a radiologist/senior clinician could speak about the features that the bot may be dectecting in each scan?*

## Workshop

The pneumonia dataset that will be used is [this one](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia/data). It has a CC BY 4.0 licence, which means it is free to use for commercial use. Dataset features include: - 2GB size - course participants will download the dataset directly to the Colab instance and decompress it using the following commands:

``` bash
!kaggle datasets download -d paultimothymooney/chest-xray-pneumonia
!unzip chest-xray-pneumonia.zip
```

This workshop should be run as one over two seminars. The seminar can be used to check in on how people are doing with the workshop content as this will be unsupported. There will be a break point in the workshop (trained model saved) which is used between seminars.

By the end of the workshop, clinicians should be able to:

-   Data preprocessing
    -   Open an image using PIL with `Image.open()` and extract basic information about the image (format, size) (LL1)
    -   Centre crop an image to standardise for machine learning (LL1)
    -   Resize images using PIL method `Image.resize()` (LL1)
    -   Convert an image to grayscale (LL1)
    -   Pack greyscale images into a 3 dimensional array for training and testing (LL1)
    -   Understand why using Python generators is important for loading data (LL3)
    -   Construct a generator using the `yield` command (LL1)
-   Binary classifier model evaulation
    -   Evaluate the performance of a simulated diagnostic classifier using familiar statistics from evidence-based medicine training (LL1)
    -   Calculate and understand precision, recall, and F1 scores (LL1) (LL2)

**Break between seminars.**

-   Model architecture
    -   Understand the difference between `Sequential` models and other models in Keras (LL2)
    -   Understand how to construct a basic convolutional neural network using Keras/TensorFlow (LL1)
    -   Understand how to compile a model and view its architecture using `model.summary()` (LL1)
-   Model training
    -   Understand how to run a training loop for a neural network (LL1)
-   Model saving
    -   Structure machine learning projects to to allow for reuse of model weights (LL3)
    -   Save files from Google Colab for reuse later (LL1)
    -   Open a machine learning model from file (LL1)
-   Model tuning
    -   Appropriately tune hyperparameters and model architecture to improve model performance and size (LL1)
    -   *Note: This should be done in conjunction with the model evaulation step below.*
-   Binary classifier model evaulation
    -   Evaulate a model using testing data (LL1)
    -   Calculate and understand precision, recall, and F1 scores (LL1)
    -   Use pyplot and scipy to plot a formal ROC curve for a binary classifier (LL1)
    -   Calculate the AUC value for this curve (LL1)

The model structure will be a convolutional neural network with single sigmoid output node denoting probability of pneumonia in the scan.

# Session 5 - Closing Session

## Seminar

By the end of the seminar, clinicians should: 
- Understand the core learning outcomes from the course 
- Understand how to grow their skills further by using other available resources (LL4)
- Give feedback for further improvements to the course (LL4)