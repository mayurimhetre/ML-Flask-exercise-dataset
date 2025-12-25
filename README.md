# ML-Flask-exercise-dataset

# Seaborn Exercise Dataset

The **exercise dataset** is a built-in example dataset available in the Seaborn Python library.  
It contains heart rate measurements of individuals recorded under different physical activity conditions.

## Dataset Description

Each row in the dataset represents a single observation of heart rate measured during an activity session.  
The dataset includes information about the type of exercise, the time of measurement, and the diet group of the participant.

## Columns

- **id** – Unique identifier for each participant  
- **diet** – Diet group of the participant  
- **pulse** – Heart rate measurement  
- **time** – Time point of the measurement  
- **kind** – Type of exercise (rest, walking, running)

## Purpose

This dataset is primarily used for learning and demonstration purposes, especially for:
- Categorical data visualization
- Repeated-measures analysis
- Practicing Seaborn plotting functions

## Usage

```python
import seaborn as sns

df = sns.load_dataset("exercise")
df.head()
```

**Model deployed on Heroku Platform:**

This project was developed in Pycharm and for web application Flask is used.

1.Logistic Regression gives 94 % accuracy.

2.There are 3 categories in dependent variables- running, walking and rest.


![image](https://user-images.githubusercontent.com/68188457/118449469-d1abf780-b710-11eb-8330-ab57e88cf2a8.png)


![image](https://user-images.githubusercontent.com/68188457/118449829-251e4580-b711-11eb-8506-c3b7807fa6ed.png)



