
# Adverse Reaction of Vaccination : Side Effects Clustering and Risk Prediction methods

Proposal By :

Sharath Srinivas

Chetan B Desai

Saideep Malgireddy

![images](https://user-images.githubusercontent.com/60420184/153628674-3a71f712-4f3c-4055-9570-c4a0b5329312.jpg)


## Introduction
There are no vaccine, drug or medical devices which are completely free from the side effects. Vaccine protects many people in Fighting the pandemic like Covid-19. So Its important for any healthcare proffesionals or End users of Vaccine must be aware of the side effects and to prevent any life threathening situtaions.

Anyone who has received a vaccine and had an adverse reaction should file a VAERS report online, even though they are unsure that the vaccine is to blame. So, This project makes use of data from the Vaccine Adverse Event Reporting System (VAERS), which was designed by the Food and Drug Administration (FDA) and the Centers for Disease Control and Prevention (CDC) to receive reports concerning vaccine-related adverse events.


## Background


## Goals

The goal of this Project is to group various vaccination adverse events. The project's goal is to first gain a thorough understanding of the most common types of adverse reactions, and then to determine suitable manufacturer of a particular vaccine which has least side effects based on their medical history, allergies, gender and age. Classification based on common symptoms and patient information to anticipate the need for urgent care. Clustering (unsupervised machine learning) is used to segment individuals based on undesirable reactions.We plan on providing Web interative application using python Dash, Django or Flask for patients and medical professionals which helps them to determine best suitable vacination based on their health records to reduce the life threatening incidents to decide on their vaccine immunization. 

## Data Preprocessing
Taking care of Missing values, 
Taking care of Categorical Features, 
Normalization of data set

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

For example below chart shows the symtoms of the Vaccine.


![Fig9](https://user-images.githubusercontent.com/60420184/155924904-0dfca07f-30ea-4d3b-8ac1-f1ff78122dae.png)

![Fig 12](https://user-images.githubusercontent.com/60420184/155924909-c8f5b8b8-b35e-44e2-bde5-835c69f5e59e.png)

![Fig 13](https://user-images.githubusercontent.com/60420184/155924917-fcb5dc9e-8726-47b0-9411-732bccc69ed5.png)

![Fig14](https://user-images.githubusercontent.com/60420184/155924926-cf93a34a-03ce-45a8-9026-bd183e5a8347.png)



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



