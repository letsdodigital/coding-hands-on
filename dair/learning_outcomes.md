# DAIR Workshop Learning Outcomes

This document details the high level learning outcomes for each seminar and workshop in the course.

# Session 1 - Course Introduction

*TODO*

# Session 2 - Datasets and Python

## Seminar

By the end of the seminar, clinicians should:
- Understand the CSV format
- Understand what constitutes "machine readable" data and what considerations clinicians must make to maximise this
- Understand the different data types in a table - strings, integers, floats
- Understand the broad uses of this type of information

## Workshop

By the end of the workshop, clinicians should be able to:

- Open a CSV file into pandas
- Extract row and column information 
- Search a column for a string
- Perform basic excel maths on array E.g. averaging
- *TODO*

The data used in this workshop will be simulated.

# Session 3 - DICOM and Python

## Seminar

By the end of the seminar, clinicians should:

- Understand the DICOM format
- Understand what information is contained within a DICOM file
- Understand broadly how a DICOM file stores image data

## Workshop

By the end of the workshop, clinicians should be:

- Able to open a DICOM file with Python
- extract basic scan information E.g. patient info
- Be able to display image data from a DICOM in Python

The study used in this workshop will be the same as the one used in the 3D printing section of the course.

# Session 4 - 3D Printing for Medicine

## Seminar

By the end of the seminar, clincians should:

- Understand how 3D printing works
- Be able to list medical uses of 3D printing
- Understand what steps are needed to get from voxels to object 

## Workshop

This workshop will cover the basics of segmentation with InVesalius. Course attendees will be instructed to install Invesalius at the end of the preceding seminar. The workshop will cover loading 3D DICOM studies with InVesalius, how to navigate the image, how to segment anatomy from a scan, and how to export for fused-deposition modelling (FDM) 3D printing. Slicing with Ultimaker Cura may be demonstrated at the end of the session. A post-workshop activity will include an informal competition for producing the best object segmentation with InVesalius. The best anatomical models at the end of the workshop will be printed and showcased on course social media.

### Session Structure
      
- Opening a 3D DICOM scan with InVesalius
- Navigating a study with InVesalius
    - Brief discussion of abdominal anatomy and views in each window (sagittal, coronal, axial)
- Segmentation with InVesalius
    - How to threshold a scan to make an initial mask
    - How to crop a mask
    - How to manually remove holes from the mask in 2D and 3D
    - How to perform watershed segmentation, and when the IFT method works best (brain segmentation)
    - Brief overview of the remaining tools which have not been covered
- Exporting segmentation for 3D printing
    - How to select different surfaces and delete irrelevant anatomy or segmentation noise
    - What file formats 3D printers accept, and how to convert between STL and G-code
    - The importance of the mesh being manifold, and how 3D printer software copes with this

*NB - A DICOM study for this section of the course which we have the relevant permissions/anonimity to use needs to be identified.*

# Session 5 - AI for Medicine (Part 1)

## Seminar

By the end of the seminar, clinicians should:

- Understand what machine learning is at a broad level
- Be able to list clinical uses for ML
- Understand the difference between supervised and unsupervised learning
- Understand the inputs and outputs of a neural network
- Understand the difference between a covolutional layer and dense layer at a broad level

## Workshop

By the end of the workshop, clinicians should be able to:

- Open image data for training a machine learning model
- Conduct basic data preprocessing for machine learning model input
- Understand how to construct a basic convolutional neural network using Keras/TensorFlow
- Understand how to run a training loop for a neural network

The model structure will be a convolutional neural network with single sigmoid output node denoting probability of pneumonia in the scan.

# Session 6 - AI for Medicine (Part 2)

## Seminar

By the end of the seminar, clinicians should:

- Be able to describe the high-level steps needed to implement a ML model (collect data, preprocess data, augment data, define model, compile model, train model, evaluate model)
- Be able to describe important metrics for a classifier (positive/negative predictive value, sensitivity and specificity)
- Be able to describe the statistical tests needed to evaluate a binary classifier (F1 score, AUC and ROC curves)
- Be able to give a broad overview of the common metrics that are used with other types of machine learning model (softmax for multiclass classifiers, pixel accuracy and intersection over union (IoU) for segmentation)
- Be able to discuss the uses, advantages, and disadvantages of more modern approaches to machine learning (stable diffusion, large language models)

## Workshop

By the end of the workshop, clinicians should be able to:

- Calculate and understand precision, recall, and F1 scores
- Use pyplot and scipy to plot a formal ROC curve for a binary classifier
- Calculate the AUC value for this curve
- Understand the importance of splitting data into training, validation, and testing datasets

# Session 7 - Closing Session

*TODO*