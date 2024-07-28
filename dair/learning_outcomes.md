# DAIR Learning Outcomes

This document details the high level learning outcomes for each seminar and workshop in the course.

The following learning levels (LLs) should be able to be mapped to the learning points.
1. **Level 1 - Basic Practical Skills (coding skills)**
* E.g. How to reshape a numpy array from `(3, 3, 3)` into `(9, 3)`.
2. **Level 2 - Theory (modelling skills)**
* E.g. How k-means splits data up into clusters
3. **Level 3 - Project Planning and Management**
* E.g. How to write a class for plotting similar plots during EDA. 
4. **Level 4 - Clinical Translation**
* E.g. What format data needs to be collected in to train a sepsis predictor from NEWS score. 

The seminars will consist mainly of LL2 and LL4 information, whereas workshops will consist of LL1 and LL3 information.

# Learning outcomes to match

The outcomes below have not been matched to a module yet.
- one-hot encoding and why (LL2) 


# Session 1 - Course Introduction

## Seminar

By the end of the seminar, clinicains should be able to:
- Know the overall aims and philosophy of the course
- General coding information
  - Know the layout of documentation and how to use it (LL3)
  - Know what StackOverflow is and when to use it (LL3)
  - Understand what constitutes "machine readable" data and what considerations clinicians must make to maximise this (LL4)
- NumPy
  - Know why NumPy exists within the Python ecosystem (speed of array operations, ease of working with multidimensional data) (LL2)
  - Understand the concept of multidimensional arrays and the 'shape' of an array (LL2)
  - Explain what a NumPy array is (LL2)
  - Understand how to use NumPy functions and common pitfalls e.g. shape mismatches (LL1)
- Pandas
  - Know why Pandas exists within the Python ecosystem (ease of processing for tabular data without having to create parsers, seamlessly working with different datatypes) (LL2)
  - Appreciate how Pandas is built on NumPy (LL2)
  - Understand the CSV/TSV format (LL2)
  - Have a broad understanding of the types of tasks that Pandas is able to perform (grouping data, generating summary statistics) (LL2)
  - Be able to explain common abbreviations that are used in Pandas code and how it is usually structured (LL3)
  - Understand Pandas' indexing system
- Explain how to represent common data structures as NumPy or Pandas data (quiz-style questions to test understanding) (LL2)
  - Image data - NumPy array
  - Tabular data - Pandas DataFrame
  - A series of time-series ventilator measurements - NumPy array or Pandas DataFrame
- Matplotlib and Pyplot
  - Know why Pyplot exists within the Python ecosystem (ease of plotting data) (LL2)
  - Know the general structure of Pyplot calls and how they are used in projects (LL3)
  - Have a general appreciation for the wide array of plots that Pyplot can generate (LL2)
  - Have an appreciation that other plotting libraries exist that are often easier to use for complex plots (Seaborn) (LL2)
  - Understand some formatting rules for academic journals and how to comply with these using Pyplot (saving high resolution plots, changing fonts) (LL4)
- SciKit
  - Know why SciKit exists within the Python ecosystem (ease of use of complex algorithms and statistical tests) (LL2)
  - Understand the sorts of algorithms that are available within SciKit (LL2)
  - Understand the general layout of a SciKit function and how they fit into projects (LL3)
- Two basic concepts to prepare for workshop (LL2)
  - Basic recap of what an unpaired t-test is used for (LL2)
  - Understand what convolution is and what it is used for (LL2)
  - Understand intuitively how to average a signal using an averaging kernel e.g. `[0.2, 0.2, 0.2, 0.2, 0.2]` (LL2)
  - Appreciate that convolution can be used in more than 1 dimension - *will be covered in the machine learning section of the course* (LL2)

Good resources for planning this section include Pandas' [Getting Started](https://pandas.pydata.org/docs/getting_started/index.html#getting-started) guide, [10 minutes to Pandas](https://pandas.pydata.org/docs/user_guide/10min.html#min).

## Workshop

The aim of this workshop is to recap some basic Python skills and to ensure that course attendees have the appropriate knowledge of core packages before starting more in-depth content. The Pandas section will focus on table manipulation and grouping data, and the NumPy section will focus on combining and modifying arrays and using basic library functions. An task using convolution will be used to demonstrate this to conceptually prepare for the machine learning section of the course. *TODO: Does the convolution LL2 content need to be moved to the seminar?*

By the end of the workshop, clinicians should be able to:

- Pandas
  - Open a CSV file into pandas (LL1)
  - Extract row and column information using pandas (LL1)
  - Describe a Dataframe using the `.describe()` method (LL1)
  - Search a column for a string (LL1)
  - Clean a dataframe by removing empty `NaN` entries (LL1)
  - Counting unique strings in a column and plotting them as a bar chart (LL1)
  - Convert strings to `Datetime` objects using date formatting strings (LL1) 
  - T-test example task (*One candidate dataset is the dataset of survivors from the Titanic*) (LL2)
    - Plotting grouped numerical data as a bar chart (LL1)
    - Grouping data for statistical testing (unpaired t-test) (LL1)
- NumPy
  - Convert a column of a DataFrame to a NumPy array (LL1)
  - Print the shape of a NumPy array (LL1)
  - Accessing array elements using array slicing (e.g. `[0:4]`, `[:-1]`)
  - Convolution example task (LL1)
    - Understand what concatenation is and the importance of matching array shapes (LL2)
    - Concatenate two NumPy arrays together (LL1)
    - Create a new array (convolution kernel) of ones of a specified shape (LL1)
    - Divide this new array by its length (LL1)
    - Convolve the kernel with the NumPy array using `np.convolve()` (LL1)
- Pyplot and Matplotlib
  - Plot time series data on a simple line graph (LL1)
  - Plot two time series signals (raw data and convolved data) on a plot (LL1)
  - Plot a bar graph of categorical data (LL1)
  - Plotting numerical data as a histogram (LL1)
- Scikit
  - How to perform a statistical test (unpaired t-test) on grouped data using `scipy.stats.ttest_ind()` (LL1)

# Session 2 - Datasets and Python

- TODO - Discuss the outcomes for this module, and update to include EDA content

## Seminar

By the end of the seminar, clinicians should:
- Understand the aims of this module and how they relate to clinical practice (LL4)
- Exploratory data analysis (EDA)
  - Understand what EDA is (LL1)
  - Why do EDA and where EDA fits into a clinical/scientific data analysis pipeline (LL4)
  - How to effectively handle missing data in a dataset (LL2) 
  - Understand the concept of collinearity between variables in a dataset (LL2)
- Error messages
  - Understand the general format of an error message (LL2)
- Effective debugging
  - Learn to debug and deal with 'error messages' (LL2)
  - Understand common formats of documentation (LL2)
  - How to use documentation to debug an external function/method (LL2)
  - Understand when to raise exceptions to prevent unwanted behaviour or bugs (LL2)

## Workshop

By the end of the workshop, clinicians should be able to:
- TODO
- Data preprocessing
  - Remove or replace missing data in a meaningful way (LL1)
- EDA
  - collinearity and variance management
  - Undertake EDA 
  - Learn to write custom functions and why
- Debugging
  - Check that a varaible is within a required range, and raise an exception if it is not (LL1)
- Use of documentation

We need to identify appropriate data to design this workshop around.

# Session 3 - DICOM and Python

## Seminar

By the end of the seminar, clinicians should:

- Understand the aims of this module (LL4)
- Basics of image representation (LL2)
  - Understand what a pixel is (LL2)
  - Understand what a voxel is, by extension (LL2)
  - Greyscale images
    - Understand what values greyscale values are are usually given in (0.0-1.0, 0-255, HU) (LL2)
    - Understand what a Houndsfield Unit is (LL2)
  - Colours
    - Understand how RGB data is used to represent most images (LL2)
    - Understand what a colourmap is and when it is used (LL2)
  - Image formats other than DICOM
    - Understand why compression is needed to store images (LL2)
    - Understand the difference between lossy and lossless image compression
    - Name an image compression algorithm (discrete cosine transform) (LL2)
    - Name common everyday image formats and when they may be used (JPEG, PNG) (LL2)
- The DICOM format
  - Know the history of the DICOM standard and why it was introduced (LL2)
  - Understand what information is contained within a DICOM file (LL2)
  - Understand that DICOM is a lossless standard (LL2)
  - Understand broadly how a DICOM file stores image data (both 2D and 3D) (LL2)
  - Understand why Pydicom is a useful tool for clinicians (LL4)
- Understand what considerations are needed when coding in Python to convert images, with interactive questions (array shapes) (LL3)
- Understand the difference between volumetric 3D images and 3D meshes and what is needed to convert between them (segmentation)
- Understand the basics of image segmentation (LL2)
- Understand where volumetric imaging is used and where mesh reconstructions are used in clinical medicine (LL4)

## Workshop

By the end of the workshop, clinicians should be:

- Open a DICOM file with Python (LL1)
- Scan information  
  - Understand that there are three different types of element in a DICOM file (LL2)
  - Understand different ways to access elements (by hex tag and keyword) (LL2)
  - Extract basic scan information by keyword e.g. `PatientName` (LL1)
- Image extraction
  - Understand what data is needed to accurately reconstruct data from a DICOM study for 3D and 2D images (image shape, slice indices) (LL1)
  - Extract 2D image data into a NumPy array using `ds.pixel_array` (LL1)
  - Extract 2D colourmap data (*e.g. Doppler flow rate data*) and plot this appropriately (LL1)
  - Reconstruct 3D image from a DICOM study and [plot axial, sagittal and coronal views](https://pydicom.github.io/pydicom/stable/auto_examples/image_processing/reslice.html#sphx-glr-auto-examples-image-processing-reslice-py) (LL1)
  - Preprocess the image for display in Python (LL1)
  - Plot image data from a DICOM file in Python (LL1)
  
We need a candidate DICOM study/studies for this portion of the course. Options include:
- [Patient Contributed Image Repository](https://www.pcir.org/) - This is where Pydicom gets it's official example studies.
- Pydicom's official test files

We need the following studies:
- 2D basic scan (e.g. CXR)
- 2D scan with colourmap data (e.g. Doppler Ultrasound)
- 3D volumetric scan (e.g. CT head)

# Session 4 - Modelling for Medicine

## Seminar

By the end of the seminar, clinicians should:
- *TODO Complete these aims*
- Understand the aims of this module and what it will cover
- Types of statistical model
  - Understand what a statistical model is at a broad level (LL2)
  - Parametric models
    - Linear / logistic regression as a parametric model example (LL2)
  - Nonparametric models
    - k-nearest neighbour model as a flexible non-parametric model (LL2)
- Be able to describe the high-level steps needed to train a statistical model (collect data, preprocess data, augment data, define model, compile model, train model, evaluate model) (LL2)
- Understanding the importance of splitting the data into training, testing, and validation datasets (LL2)
- Assumptions of models
  - Understand dataset bias and clincial factors that can confound a dataset (LL4)
  - Use examples to demonstrate clinical bias *TODO find appropriate examples* (LL4)
- Bias-variance trade off and overfitting
  - Gain an intuitive understanding of overfitting vs overfitting using a linear model as an example (LL2)
- Hyperparameters
  - Understand what a hyperparameter is (LL2)
  - How a hyper-parameter effects model output (LL2)
  - Understand that hyperparameters can be tuned (LL2)
- Evaulating models
  - Describe methods for evaulating regression models (LL2)
  - Be able to describe important metrics for a classifier (positive/negative predictive value, sensitivity and specificity) (LL2)
  - Be able to describe the statistical tests needed to evaluate a binary classifier (F1 score, AUC and ROC curves) (LL2) *TODO Maybe move this to module 5?*
  - Be able to give a broad overview of the common metrics that are used with other types of model (softmax for multiclass classifiers, pixel accuracy and intersection over union (IoU) for segmentation) (LL2)
- Common pitfalls
  - How to deal with overfitting. (LL2)
  - How to deal with multicollinearity (LL2)
  - How to deal with missing data and sensitivity analysis (LL2)

## Workshop

By the end of the workshop, clinicians should be able to:

*TODO This session should be based around fitting a basic model to basic tabular data - use linear regression and k-means*

# Session 5 - AI for Medicine

## Seminar

By the end of the seminar, clinicians should:

- Understand the aims of this first AI module and what it will cover
- Be able to list clinical uses for ML (LL4)
  - Understand what machine learning is at a broad level (LL2)
- Understand what a loss function is (LL2)
- Appreciate that there are a wide variety of optimisers and loss functions that can be used (LL2)
- Understand the difference between supervised and unsupervised learning (LL2)
- Gain an intuition for how training via backpropagation works via the ball on a hill analogy (LL2)
- Pneumonia detection task
  - Disclaimer that this course will not cover intepretation of chest X-rays
- Data preprocessing
  - Understand considerations that must be made when standardising image data for model input (image size, image dimensions, contrast, brightness) (LL2)
  - Understand the importance of data augmentation when training (LL2)
  - Be able to name common data augmentation techniques (shearing, rotation, stretching, elastic deformation in medical imaging datasets) (LL2)
  - Understand how these concepts apply to other types of data (e.g. time-series data) (LL2)
- Model architecture and training
  - Understand why ML frameworks exist in the Python ecosystem (TensorFlow, PyTorch) and what they allow the user to do (LL2)
  - Understand the inputs and outputs of a neural network (LL2)
  - Understand the difference between a convolutional layer and dense layer at a broad level (LL2)
  - Understand what an epoch of training is (LL2)
  - Understand why data needs to be batched when training a network (LL3)
  - Understand what a sigmoid layer is and why it is used for probabilistic outputs (LL2)
- Appreciate that the task we are performing is fairly simple and that more complex techniques exist (LL2)
- Be able to discuss the uses, advantages, and disadvantages of more modern approaches to machine learning (stable diffusion, large language models) (LL2) (LL4)

*Maybe a radiologist/senior clinician could speak about the features that the bot may be dectecting in each scan?*

## Workshop

The pneumonia dataset that will be used is [this one](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia/data). It has a CC BY 4.0 licence, which means it is free to use for commercial use. Dataset features include:
- 2GB size - course participants will download the dataset directly to the Colab instance and decompress it using the following commands:

```bash
!kaggle datasets download -d paultimothymooney/chest-xray-pneumonia
!unzip chest-xray-pneumonia.zip
```

By the end of the workshop, clinicians should be able to:

- Data preprocessing
  - Open an image using PIL with `Image.open()` and extract basic information about the image (format, size) (LL1)
  - Centre crop an image to standardise for machine learning (LL1)
  - Resize images using PIL method `Image.resize()` (LL1)
  - Convert an image to grayscale (LL1)
  - Pack greyscale images into a 3 dimensional array for training and testing (LL1)
  - Understand why using Python generators is important for loading data (LL3)
  - Construct a generator using the `yield` command (LL1)
- Model architecture
  - Understand the difference between `Sequential` models and other models in Keras (LL2)
  - Understand how to construct a basic convolutional neural network using Keras/TensorFlow (LL1)
  - Understand how to compile a model and view its architecture using `model.summary()` (LL1)
- Model training
  - Understand how to run a training loop for a neural network (LL1)
- Model saving
  - Structure machine learning projects to to allow for reuse of model weights (LL3) 
  - Save files from Google Colab for reuse later (LL1)
- Model tuning
  - Appropriately tune hyperparameters and model architecture to improve model performance and size (LL1)
  - *Note: This should be done in conjunction with the model evaulation step below.*
- Open a machine learning model from file (LL1)
- Binary classifier model evaulation
  - Evaulate a model using testing data (LL1)
  - Calculate and understand precision, recall, and F1 scores (LL1)
  - Use pyplot and scipy to plot a formal ROC curve for a binary classifier (LL1)
  - Calculate the AUC value for this curve (LL1)
- Understand the importance of splitting data into training, validation, and testing datasets (LL2)

The model structure will be a convolutional neural network with single sigmoid output node denoting probability of pneumonia in the scan.

# Session 6 - Closing Session

*TODO*