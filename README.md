
# Adverse Reaction of Vaccination : Risk Prediction and Side Effects Clustering

Proposal By :

Sharath Srinivas

Chetan B Desai

Saideep Malgireddy

![what-are-adverse-events-and-emergency-use-authorisation-1600](https://user-images.githubusercontent.com/60420184/166168397-f31a6db9-d7aa-4ff3-9983-f43d7d0f56c2.png)
## Abstract

In conclusion, the model was successful in meeting the requirements from the problem statement by implementing the model as a preliminary screening tool for all incoming AE reports, to get an initial seriousness classification. This would help to enable serious reports to get expedited and processed more quickly, enabling signal detection to occur more efficiently. Oue recommendation is to work for other vaccine and try to work with Health care professionals to understand more about the symptoms and predict the severity level of the patient(Mild, Moderate and Severe)


## Introduction
There are no vaccine, drug or medical devices which are completely free from the side effects. Vaccine protects many people in Fighting the pandemic like Covid-19. So Its important for any healthcare proffesionals or End users of Vaccine must be aware of the side effects and to prevent any life threathening situtaions.

Anyone who has received a vaccine and had an adverse reaction should file a VAERS report online, even though they are unsure that the vaccine is to blame. So, This project makes use of data from the Vaccine Adverse Event Reporting System (VAERS), which was designed by the Food and Drug Administration (FDA) and the Centers for Disease Control and Prevention (CDC) to receive reports concerning vaccine-related adverse events.


## Background


## Goals

The goal of this Project is to group various vaccination adverse events. The project's goal is to first gain a thorough understanding of the most common types of adverse reactions, and then to determine suitable manufacturer of a particular vaccine which has least side effects based on their medical history, allergies, gender and age. Classification based on common symptoms and patient information to anticipate the need for urgent care. Clustering (unsupervised machine learning) is used to segment individuals based on undesirable reactions.We plan on providing Web interative application using python Dash, Django or Flask for patients and medical professionals which helps them to determine best suitable vacination based on their health records to reduce the life threatening incidents to decide on their vaccine immunization. 

## Data Preprocessing
Using glob to separate VAERSDATA.CSV,VAERSVAX.CSV,VAERSSYMPTOMS.CSV files from the raw data obtained from VAERS website,
checking the information of the dataframe to be consider,
Storing the data back in the drive for further consideration,
Taking care of Missing values, 
Taking care of Categorical Features, 
Normalization of data set.


## EDA(Exploratory Data Analysis)

This project makes use of data from the Vaccine Adverse Event Reporting System (VAERS), which was designed by the Food and Drug Administration (FDA) and the Centers for Disease Control and Prevention (CDC) to receive reports concerning vaccine-related adverse events. Medical practitioners are urged to report adverse events, and VAERS data may include coincidental events that are unrelated to the vaccine.In addition, due to the human factor in data input, we should expect incomplete examples.

<a href="https://vaers.hhs.gov/data/datasets.html">Dataset</a> 

<a href="https://vaers.hhs.gov/docs/VAERSDataUseGuide_November2020.pdf">Data Guide</a>

The VAERS data can be accessed by downloading raw data in comma-separated value (CSV) files.
The following datasets consists of 3 files from year 2010 to 2022: VAERSDATA, VAERSSYMPTOMS, and VAERSVAX. 

VAERSDATA provides the event IDs (VAERS ID) as well as personal information such as age, gender, symptom, allergy type, medical history, deceased, hospitalized, and life threat.

VAERSSYMPTOMS contains The events' IDs and symptom keywords retrieved from the symptom text in VAERSDATA.

VAERSVAX inscribes vaccine types and vaccine manufacturers.

We have select below vaccine as part of our project : 

1. COVID19 (COVID19 VACCINE)
2. VARZOS (VARICELLA-ZOSTER VACCINE )
3. HEP (HEPATITIS B VACCINE)
4. FLU (INFLUENZA)



#### Steps Carried out as a part of Exploratory Data Analysis:

We have described EDA for 1)  COVID19 (COVID19 VACCINE) Here similary we carried the same set of operations for other vaccines as well.

1) Considering the respective vaccines data from the drive where we stored our data as a part of Preprocessing techniques.
2) Then Describing the Data, checked for duplicate values or missing data, dropping the columns which are not required for our modelling.
3) Converting the Date columns to the Datetype, converting sex to binary 0 for female, 1 for male, 2 for not known, applying regular expression to clean the columns such as "SYMPTOM_TEXT", "OTHER_MEDS", "HISTORY" etc.
4) We filtered only the vaccine data which is after january 2021, we created a new column serious from serious = vaers_covid[['DIED', 'L_THREAT', 'HOSPITAL', 'X_STAY', 'DISABLE', 'BIRTH_DEFECT']].copy() and derived Seriousness coloumn 1 being Serious and 0 Non Serious.
5) Downloaded Important Medical Events list MeDDRA a Event dictonary maintained by Upsaala.
6) We compared Symptoms1 to Symptoms5 from our data with IME List and derive IME column with 0 and 1 values and mergerd both Serious and IME column.
7) We plotted age distributions and the box plot to identify the outliers in them, we considered the age group of vaccines to be between 18 to 100,
![download (1)](https://user-images.githubusercontent.com/11175353/166147134-d5fdff80-b7b5-4967-8189-ac53ac916da5.png)

8) Distribution of adverse event severity based on age.
![download (2)](https://user-images.githubusercontent.com/11175353/166147333-e525258e-5c10-4039-bc96-bdae3f87a80b.png)
9) Seriousness plot of vaccines based on vaccine manufacturers
![Screenshot 2022-05-01 075105](https://user-images.githubusercontent.com/11175353/166147139-8fc7545f-6010-4c3a-a4af-efe2dd89f66f.png)

10)  Word cloud for covid vaccine in its shape.
![Screenshot 2022-05-01 075410](https://user-images.githubusercontent.com/11175353/166147143-e5caaf90-689f-416d-a468-4c114129d367.png)
11) State wise Comparission of gender getting severe reactions after vacinated
![Screenshot 2022-05-01 075439](https://user-images.githubusercontent.com/11175353/166147144-40f016a4-a34d-45c1-8ac3-e4197cc634f2.png)
12) PLot of Age category vs Sex with serious and non serious
 ![Screenshot 2022-05-01 075237](https://user-images.githubusercontent.com/11175353/166147697-cb1c3416-fc9c-454e-b9d3-9b3ca85c9b14.png)
 
 And then Explored the other vaccine data in similary ways. We created the cleaned csv file with names "covid_ml_clean.csv", "flu_ml_clean","varzos_ml_clean","hep_ml_clean" to consider for model building in the next phase.
 
 13)PLot of Age category vs Sex with Deaths and no Deaths.
   ![image](https://user-images.githubusercontent.com/11175353/166163213-595dd132-f2ba-489f-9d59-4d9b73352c2b.png)
   
   
 
 
 
 
 #### Machine Learning Models
 
 We Have described the steps for COVID vaccine follow similarly for other vaccines as well.
 
 1) Plotting the correlation plot of the features

 ![download (4)](https://user-images.githubusercontent.com/11175353/166149365-36e5aebd-0906-40b9-b903-a4bc164b4303.png)
 
2) Used the sklearns train test split for splitting and training the cleaned data.
3) We implemented a pipeline with the alogirthms such as Logistic Regression, Naive Bayes, Random Forest, AdaBoostClassifier, SVM, Gradient Boosting, along with the gridsearch and tfidf, CountVectorizer for vectorization. To check which algorithm gives the best result on our current data.
4) For example the confusion matrix for serious and no serious features where plotted like the images shown here for the FLUVACCINE.
Vectorizer being "CountVectorizer"

![download (1)](https://user-images.githubusercontent.com/11175353/166149674-7f775819-875d-47cc-b517-fda1ffd38ae8.png)

Vectorizer being " TfidfVectorizer"

![download](https://user-images.githubusercontent.com/11175353/166149675-a9ec72f6-5eb9-4a93-8f93-9f3f6c0713da.png)

5) Then we choosed AdaBoost to be our final model since it gave the promosing results we stored it in a file named ADABoostFinalmodel for all the vaccine data. 
   We also plotting the ROC curve one such example is for COVID applying Ada Boost Model here:
   ![download (3)](https://user-images.githubusercontent.com/11175353/166150010-f7e8a36e-954e-44d3-9117-b8339fbe8bf4.png)
    The model details are saved in a separate covid_ada_new_model.sav, hep_ada_new_model.sav using pickle dump, etc which will be used for predictions and all the web application for real time data.
    Train score (Accuracy): 0.988, Test score (Accuracy): 0.946
Recall: 0.622, F1 score (test): 0.701, Specificity: 0.983, Precision: 0.803

6) Matric Graphs for the algorithms used
![Algorithm accuracy](https://user-images.githubusercontent.com/11175353/166165723-e9c335f2-595b-483c-add6-14435dc6b134.png)



7) Next Applying the knn model on the cleaned data set , a bit of cleaning was required to replace 'None' , 'NA' 'none' values from the columns such as 'OTHER_MEDS', 'CUR_ILL','ALLERGIES','HISTORY'. Split the data into train and test with X and y respectively. 
8) Connecting the model to the Web App with user interface which takes in User, patients or clinicians details and outputs if they have serious or non serious threat.









 













### Team Roles and Responsibilities

**Chetan B Desai (Captain)** ***: Project Manager***

◈ Data Cleaning Clean Textual data using Natural processing Language

◈ Classification: SVM and K-nearest neighbor

◈ Clustering : K Means 

**Sharath K Srinivas** ***: Deliverable Manager***

◈ Exploratory data analysis

◈ Classification: Multi-layer Perceptron classifier and Random forest

◈ Clean Textual data using Natural processing Language

◈ Clusturing Interpretation 

**Saideep Reddy** ***: Reference Manager and Project Editor***

◈ Logistic Regression and Decision tree

◈ Model Comparison

◈ User Interface using plotly or flask

#### Weekly Meetings

Along with all the task assigned above we also sceduled a weekly meeting on Tuesdays, Fridays and Sundays from 11:00 Am to 2:00 PM to discuss the staus of the project and to resolve any issues regarding the same. 

## Reference 

[1]. https://www.cdc.gov/coronavirus/2019-ncov/vaccines/safety/adverse-events.html

[2]. https://pubmed.ncbi.nlm.nih.gov/15071280/


youtube vedio link for EDA first phase: https://youtu.be/VX2x8jXAEHY
