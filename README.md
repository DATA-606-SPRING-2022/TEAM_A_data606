

# Adverse Reaction of Vaccination : Risk Prediction and Side Effects Clustering
Under the guidance: **Prof. Wang, Chaojie**

Presented By :

**Sharath Srinivas**

**Chetan B Desai**

**Saideep Malgireddy**

![what-are-adverse-events-and-emergency-use-authorisation-1600](https://user-images.githubusercontent.com/11175353/166166119-5704c59e-bce4-4e34-9d79-ec9a4001cc07.png)


## Abstract

An adverse event (AE) is a poor or damaging outcome that occurs after a patient receives medical care or therapy. The goal of this study is to develop a model for identifying serious and non-serious AE. Due to varying demographics, surroundings, and drug quality, adverse side effects of a drug may vary over time and space. It is impossible to discover all adverse effects during development. After a medicine is approved, doctors and patients record any adverse effects they encounter, which are then entered into the CDC and FDA Vaccine Adverse Event Reporting System. 
The Vaccines which are considered for our project are COVID19 (COVID19 VACCINE), VARZOS (VARICELLA-ZOSTER VACCINE ),HEP (HEPATITIS B VACCINE),FLU (INFLUENZA) Duplicates were deleted, null values were imputed or dropped, and the target column 'serious' was formed in the data cleaning section. Age, Patient Gender, Symptom Text, Patient Died, Patient Life Threatening, Hospitalization, Stay in Hospital, Patient Disability, Recovered status, Other Medication, Current Illness, Patient History, Patient Birth defect, Patient Allergies, and Vaccine Manufacturer were Selected via EDA, to predict the patient's seriousness.

We trained the model on different vaccine data separately and below are the result:

A total of 5 models were evaluated - 
1. Logistic Regression
2. Naive Bayes - Multinomal
3. Random Forest Classifier
4. Ada Boost Classifier
5. Support Vector Machine (SVM). 

Train-test split were chosen: 70/30. Modelling was done with and without Synthetic Minority Oversampling Technique (SMOTE), and the model that met the target was ADA Boost utilizing TF-IDF vectorizer with 70/30 split without SMOTE. This model yielded test accuracy of as showed below for different vaccine.

![Results](https://user-images.githubusercontent.com/11175353/166166725-a53237ce-7c98-4168-b306-d33a83c94031.jpeg)

In conclusion, the model was successful in meeting the requirements from the problem statement by implementing the model as a preliminary screening tool for all incoming AE reports, to get an initial seriousness classification. This would help to enable serious reports to get expedited and processed more quickly, enabling signal detection to occur more efficiently. Oue recommendation is to work for other vaccine and try to work with Health care professionals to understand more about the symptoms and predict the severity level of the patient(Mild, Moderate and Severe).


## Introduction
CDC received reports of clusters of anxiety-related episodes after delivery of the Janssen COVID-19 vaccine from five mass vaccination locations, all in different states, on April 7, 2021, after 5 weeks of usage under the Food and Drug Administration's (FDA) Emergency Use Authorization (EUA). CDC interviewed vaccination site staff members to acquire further information about the reported occurrences and immunization site protocols in order to further examine these cases. Four of the five locations were temporarily shut down while an investigation was conducted. Overall, 64 anxiety-related incidents were recorded from these sites for vaccines provided between April 7 and 9, including 17 instances of syncope (fainting), an anxiety-related event, among 8,624 Janssen COVID-19 vaccine recipients.
Following up on these interviews, the CDC looked into complaints of syncope received immediately after receiving the Janssen COVID-19 vaccine to the Vaccine Adverse Event Reporting System (VAERS), the CDC and FDA-run vaccine safety monitoring program. Reports of syncopal events after influenza vaccine administration in the 2019–20 influenza season were also evaluated to compare the occurrence of these events to those reported after receiving other vaccines. VAERS received a complaint of syncope following the Janssen COVID-19 vaccine (8.2 episodes per 100,000 doses). Syncope was reported in 0.05 events per 100,000 doses after influenza vaccination, by comparison. Any immunization can result in anxiety-related reactions.
Any immunization can result in anxiety-related reactions. It is critical that vaccination providers understand that anxiety-related adverse events may occur more frequently after receiving the Janssen COVID-19 vaccine than after receiving influenza vaccination, and that they monitor all COVID-19 vaccine recipients for at least 15 minutes after vaccine administration for any adverse reactions.

An adverse event (AE) is a poor or damaging outcome that occurs after a patient receives medical care or therapy.There are no vaccine, drug or medical devices which are completely free from the side effects. Vaccine protects many people in Fighting the pandemic like Covid-19. So Its important for any healthcare proffesionals or End users of Vaccine must be aware of the side effects and to prevent any life threathening situtaions.1 million 'COVID-vaccine injuries' are reported in a CDC database. Most side effects from vaccination are mild and Serious side effects are rare, but may include seizure or life-threatening allergic reaction.

Anyone who has received a vaccine and had an adverse reaction should file a VAERS report online, even though they are unsure that the vaccine is to blame. So, This project makes use of data from the Vaccine Adverse Event Reporting System (VAERS), which was designed by the Food and Drug Administration (FDA) and the Centers for Disease Control and Prevention (CDC) to receive reports concerning vaccine-related adverse events.


## Background
The U.S. Food and Drug Administration (FDA) defines an adverse drug experience as any AE associated with the use of a drug in humans, whether or not considered drug related, while the International Conference on Harmonisation (ICH) guideline ICH E2A similarly defines an AE as an untoward medical occurrence in a patient administered a pharmaceutical product, whether or not the occurrence is related to or considered to have a causal relationship with the treatment. Timely adverse event reporting is essential for  signal event detection to minimize further patients receiving unsafe vaccines.The most notable event occurred in 2010 when increased incidence of fever and seizures occurred following seasonal influenza vaccines. The vaccine was withdrawn 10 days later, Incident including a prolonged febrile seizure resulting in profound disability in a previously healthy 11-month-old child.The multi-million dollar compensation decision recognized the delays in reporting and state and federal response processes that were identified in an independent enquiry. VAERS is a passive reporting system, meaning it relies on individuals to send in reports of their experiences to CDC and FDA. VAERS is not designed to determine if a vaccine caused a health problem, but is especially useful for detecting unusual or unexpected patterns of adverse event reporting that might indicate a possible safety problem with a vaccine. This way, VAERS can provide CDC and FDA with valuable information that additional work and evaluation is necessary to further assess a possible safety concern.


## Goals

The goal of this Project is to group various vaccination adverse events. The project's goal is to first gain a thorough understanding of the most common types of adverse reactions, and then to determine suitable manufacturer of a particular vaccine which has least side effects based on their medical history, allergies, gender and age. Classification based on common symptoms and patient information to anticipate the need for urgent care. Clustering (unsupervised machine learning) is used to segment individuals based on undesirable reactions.We plan on providing Web interative application using python Dash, Django or Flask for patients and medical professionals which helps them to determine best suitable vacination based on their health records to reduce the life threatening incidents to decide on their vaccine immunization. 

## Data Set and Preprocessing 
This project makes use of data from the Vaccine Adverse Event Reporting System (VAERS), which was designed by the Food and Drug Administration (FDA) and the Centers for Disease Control and Prevention (CDC) to receive reports concerning vaccine-related adverse events. Medical practitioners are urged to report adverse events, and VAERS data may include coincidental events that are unrelated to the vaccine.In addition, due to the human factor in data input, we should expect incomplete examples.

Data sets files can be downloaded from <a href="https://vaers.hhs.gov/data/datasets.html">here</a> 

Data Discription can be found <a href="https://vaers.hhs.gov/docs/VAERSDataUseGuide_November2020.pdf">here</a>

There are three data types:

NUM = numeric data

CHAR = text or "character" data

DATE = date fields in mm/dd/yy format

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

#### VAERS Data Limitations

When analyzing VAERS data, keep in mind that no cause-and-effect relationship has been proven for any reported occurrence. VAERS receives reports of all possible links between vaccines and adverse events (possible side effects). As a result, VAERS collects information on any adverse event that occurs after immunization, whether it is coincidental or actually caused by the vaccine. A report of an adverse event to VAERS is not proof that the occurrence was caused by the vaccine.

VAERS is a passive reporting system, which means that reports of adverse events are not collected automatically and must be reported to VAERS. Anyone, including healthcare providers, patients, and family members, can voluntarily submit VAERS reports. The quality and completeness of reports varies. They frequently lack details and, on sometimes, may provide inaccurate information.

One of the major drawbacks of passive monitoring systems, such as VAERS, is "underreporting." The phrase "underreporting" refers to the reality that only a tiny percentage of genuine adverse events are reported to VAERS. The extent of underreporting differs greatly. For example, many of the millions of immunizations given by injection each year induce pain, yet only a small percentage of these instances result in a VAERS report. Minor side effects of vaccines often include this type of soreness, as well as low fevers, as physicians and patients are aware. Serious and unexpected medical events, on the other hand, are more likely to be reported than minor ones, especially when they occur soon after immunization, even if they are unrelated to the vaccine.

A report to VAERS does not always imply that the indicated vaccine(s) were to blame for the adverse event. It merely validates that the alleged occurrence happened after the vaccine was administered. VAERS will accept the report without requiring confirmation that the occurrence was caused by the immunization. VAERS accepts all reports without determining if the vaccine was to blame.

Using glob to separate VAERSDATA.CSV,VAERSVAX.CSV,VAERSSYMPTOMS.CSV files from the raw data obtained from VAERS website,
checking the information of the dataframe to be consider,
Storing the data back in the drive for further consideration,
Taking care of Missing values, 
Taking care of Categorical Features, 
Normalization of data set.


## EDA(Exploratory Data Analysis)

#### Steps Carried out as a part of Exploratory Data Analysis:

We have described EDA for 1)  COVID19 (COVID19 VACCINE) Here similary we carried the same set of operations for other vaccines as well.

Considering the respective vaccines data from the drive where we stored our data as a part of Preprocessing techniques.Then Describing the Data, checked for duplicate values or missing data, dropping the columns which are not required for our modelling. Converting the Date columns to the Datetype, converting sex to binary 0 for female, 1 for male, 2 for not known, applying regular expression to clean the columns such as "SYMPTOM_TEXT", "OTHER_MEDS", "HISTORY" etc. We filtered only the vaccine data which is after january 2021.
Removed Following Symptoms which are irrelavent for our analyis.
1. Wrong drug administered
2. Incorrect route of drug administration
3. Incorrect dose administered
4. Product administered at inappropriate site
5. Incomplete course of vaccination
6. Incorrect route of product administration
7. Inappropriate schedule of drug administration
8. Inappropriate schedule of product administration


We created Target variable serious and non serious. Non Serious means Common Events Like Fever, cough, Pain etc and More Serious falls into one of the Serious criteria
For Serious criteria we selected Death, Life threatening, Hospitalization, Disability or permanant dammage, Congenital Anomaly or Birth Defect and Other Serious Important Medical Terminology. Other Serious Important Medical Terminology was downloaded from MeDDRA a Event dictonary maintained by Upsaala.
Sample of IME list looks like below:
![image](https://user-images.githubusercontent.com/60420184/169676508-ae6efbf9-6c5f-4af1-b74a-df48f7cb3479.png)


We compared Symptoms1 to Symptoms5 from our data with IME List and derive IME column with 0 and 1 values and mergerd both Serious and IME column.

![image](https://user-images.githubusercontent.com/60420184/169676513-c4ca3a70-7b7c-4c1d-b001-55d81c2935c4.png)
Below are additional graphs ploted using Plotly:
1. Age distributions and the box plot to identify the outliers in them, we considered the age group of vaccines to be between 18 to 100,
![download (1)](https://user-images.githubusercontent.com/11175353/166147134-d5fdff80-b7b5-4967-8189-ac53ac916da5.png)

2. Distribution of adverse event severity based on age.
![download (2)](https://user-images.githubusercontent.com/11175353/166147333-e525258e-5c10-4039-bc96-bdae3f87a80b.png)
3. Seriousness plot of vaccines based on vaccine manufacturers
![Screenshot 2022-05-01 075105](https://user-images.githubusercontent.com/11175353/166147139-8fc7545f-6010-4c3a-a4af-efe2dd89f66f.png)

4.  Word cloud for covid vaccine in its shape.
![Screenshot 2022-05-01 075410](https://user-images.githubusercontent.com/11175353/166147143-e5caaf90-689f-416d-a468-4c114129d367.png)
5. State wise Comparission of gender getting severe reactions after vacinated
![Screenshot 2022-05-01 075439](https://user-images.githubusercontent.com/11175353/166147144-40f016a4-a34d-45c1-8ac3-e4197cc634f2.png)
6. PLot of Age category vs Sex with serious and non serious
 ![Screenshot 2022-05-01 075237](https://user-images.githubusercontent.com/11175353/166147697-cb1c3416-fc9c-454e-b9d3-9b3ca85c9b14.png)
7. PLot of Age category vs Sex with Deaths and no Deaths.
   ![image](https://user-images.githubusercontent.com/11175353/166163213-595dd132-f2ba-489f-9d59-4d9b73352c2b.png)
 
 And then Explored the other vaccine data in similary ways. We created the cleaned csv file with names "covid_ml_clean.csv", "flu_ml_clean","varzos_ml_clean","hep_ml_clean" to consider for model building in the next phase.

 ## Modelling
 For each indivial vaccine we split the data 70% and 30% and used below features
 
 ![image](https://user-images.githubusercontent.com/60420184/169676636-8672eca8-e946-450f-9648-163b7fa427bc.png)

 We Have described the steps for COVID vaccine follow similarly for other vaccines as well.
 
 1) Plotting the correlation plot of the features

 ![download (4)](https://user-images.githubusercontent.com/11175353/166149365-36e5aebd-0906-40b9-b903-a4bc164b4303.png)
 
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
8) Model Results:
![image](https://user-images.githubusercontent.com/11175353/168337842-9ea8a9e4-4777-490f-a0fb-44972f53d547.png)

9) To get the related symptoms from user input we selected KDTree model from sklearn.neighbors
![new 02](https://user-images.githubusercontent.com/11175353/168339664-334f6a22-5be5-470f-b6c2-028e2a6fe2cc.png)


10) Connecting the model to the Web App with user interface which takes in User, patients or clinicians details and outputs if they have serious or non serious threat.
Web Interface :
![new 03](https://user-images.githubusercontent.com/11175353/168339805-578854e5-abfb-4081-8eb0-007aa4cc2932.png)
![new 04](https://user-images.githubusercontent.com/11175353/168339807-4d300878-c03c-43c7-9573-4c051c428c5a.png)
![new 05](https://user-images.githubusercontent.com/11175353/168339810-10ddbc55-5d7b-422c-a54b-5de55d7cd07c.png)
![new 06](https://user-images.githubusercontent.com/11175353/168339813-a5676395-ddf9-422a-adca-5c436cac63f3.png)













 













### Team Roles and Responsibilities
![new 07](https://user-images.githubusercontent.com/11175353/168339953-29b81019-9da8-4da6-b0bc-4218410d3a41.png)



## Reference 

[1]. https://www.cdc.gov/coronavirus/2019-ncov/vaccines/safety/adverse-events.html

[2]. https://pubmed.ncbi.nlm.nih.gov/15071280/

[3].https://www.cdc.gov

[4].https://www.ema.europa.eu/documents/other/meddra-important-medical-event-terms-list-version-250_en.xlsx

[5].https://plotly.com/python/

[6].https://www.historyofvaccines.org/content/articles/vaccine-side-effects-and-adverse-events

[7].https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6518966/

[8].https://www.medscape.com/viewarticle/950781?reg=1


## YouTube Link
<a href="https://youtu.be/VX2x8jXAEHY">**Phase 1**</a> 

<a href="https://youtu.be/yM4uPlgo7Xk">**Final Phase**</a> 


