# DAIR Learning Outcomes

This document details the high level learning outcomes for each seminar and workshop in the course.

The following learning levels (LLs) should be able to be mapped to the learning points.
1. **Level 1 - Basic Practical Skills**
* E.g. How to reshape a numpy array from `(3, 3, 3)` into `(9, 3)`.
2. **Level 2 - Theory**
* E.g. How k-means splits data up into clusters
3. **Level 3 - Project Planning and Structure**
* E.g. How to write a class for plotting similar plots during EDA. 
4. **Level 4 - Clinical Translation**
* E.g. What format data needs to be collected in to train a sepsis predictor from NEWS score. 

The seminars will consist mainly of LL2 and LL4 information, whereas workshops will consist of LL1 and LL3 information.

# Session 1 - Course Introduction

## Seminar

By the end of the seminar, clinicains should be able to:
- Know the overall aims and philosophy of the course
- General coding information
  - Know the layout of documentation and how to use it (LL3)
  - Know what StackOverflow is and when to use it (LL3)
  - Understand what constitutes "machine readable" data and what considerations clinicians must make to maximise this (LL4)
- Pandas
  - Know why Pandas exists within the Python ecosystem (ease of processing for tabular data without having to create parsers, seamlessly working with different datatypes) (LL2)
  - Understand the CSV/TSV format (LL2)
  - Have a broad understanding of the types of tasks that Pandas is able to perform (grouping data, generating summary statistics) (LL2)
  - Be able to explain common abbreviations that are used in Pandas code and how it is usually structured (LL3)
- NumPy
  - Know why NumPy exists within the Python ecosystem (speed of array operations, ease of working with multidimensional data) (LL2)
  - Understand the concept of multidimensional arrays and the 'shape' of an array (LL2)
  - Explain what a NumPy array is (LL2)
  - Understand how to use NumPy functions and common pitfalls e.g. shape mismatches (LL1)
- Explain how to represent common data structures as NumPy or Pandas data (quiz-style questions to test understanding) (LL2)
  - Image data - NumPy array
  - Tabular data - Pandas DataFrame
  - A series of time-series ventilator measurements - NumPy array or Pandas DataFrame
- Matplotlib and Pyplot
  - Know why Pyplot exists within the Python ecosystem (ease of plotting data) (LL2)
  - Know the general structure of Pyplot calls and how they are used in projects (LL3)
  - Have a general appreciation for the wide array of plots that Pyplot can generate (LL2)
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
- TODO

## Workshop

By the end of the workshop, clinicians should be able to:
- TODO

The data used in this workshop will be simulated.

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

# Session 4 - AI for Medicine (Part 1)

## Seminar

By the end of the seminar, clinicians should:

- Understand what machine learning is at a broad level (LL2)
- Be able to list clinical uses for ML (LL4)
- Understand the difference between supervised and unsupervised learning (LL2)
- Understand the inputs and outputs of a neural network (LL2)
- Understand the difference between a covolutional layer and dense layer at a broad level (LL2)
- Pneumonia detection task
  - Disclaimer that this course will not cover intepretation of chest X-rays
  - Understand dataset bias and clincial factors that can confound a dataset (LL4)
    - Use examples to demonstrate clinical bias *TODO find appropriate examples* (LL4)

*Maybe a radiologist/senior clinician could speak about the features that the bot may be dectecting in each scan?*

## Workshop

By the end of the workshop, clinicians should be able to:

- Open image data for training a machine learning model (LL1)
- Conduct basic data preprocessing for machine learning model input (LL1)
- Understand how to construct a basic convolutional neural network using Keras/TensorFlow (LL1)
- Understand how to run a training loop for a neural network (LL1)
- How to structure machine learning projects to to allow for reuse of model weights (LL3) 

The model structure will be a convolutional neural network with single sigmoid output node denoting probability of pneumonia in the scan.

# Session 5 - AI for Medicine (Part 2)

## Seminar

By the end of the seminar, clinicians should:

- Be able to describe the high-level steps needed to implement a ML model (collect data, preprocess data, augment data, define model, compile model, train model, evaluate model) (LL2)
- Be able to describe important metrics for a classifier (positive/negative predictive value, sensitivity and specificity) (LL2)
- Be able to describe the statistical tests needed to evaluate a binary classifier (F1 score, AUC and ROC curves) (LL2)
- Be able to give a broad overview of the common metrics that are used with other types of machine learning model (softmax for multiclass classifiers, pixel accuracy and intersection over union (IoU) for segmentation) (LL2)
- Be able to discuss the uses, advantages, and disadvantages of more modern approaches to machine learning (stable diffusion, large language models) (LL2) (LL4)

## Workshop

By the end of the workshop, clinicians should be able to:

- Calculate and understand precision, recall, and F1 scores (LL1)
- Use pyplot and scipy to plot a formal ROC curve for a binary classifier (LL1)
- Calculate the AUC value for this curve (LL1)
- Understand the importance of splitting data into training, validation, and testing datasets (LL2)

# Session 6 - Closing Session

*TODO*