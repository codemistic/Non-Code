Predictive modeling is using past data to determine future outcomes. Before building a predictive model, there are steps that need to be followed and they have been summarised in the picture below.

![Screen Shot 2022-10-21 at 9 06 27 AM](https://user-images.githubusercontent.com/110051825/197145882-e49d634e-5fd0-42ee-841b-04d279ac6260.png)

# Problem definition
The right problem statement needs to be defined before it can become a mathematical equation. A good problem statement is not vague.
Example of bad problem statement: Want to reduce customer churn for company
Example of good problem statement: Want to identify types of customers likely to churn 

# Hypothesis generation
A good problem statement is only the starting point. After that, you can begin generating hypothesis around it. At this stage you want to list down as many variables potentially influencing customer churn as possible.
For example hypothesis statements can include:
- Long term customers are less likely to churn than new customers
- Female customers are less likely to churn
- Customers over the age of 30 are less likely to churn

# Data extraction
Hypothesis generation helps in knowing what to look for. After generating a list of statements, you can begin data collection from various relevant sources. In this case, a relevant source could be customer demographics and their transaction history.

# Data exploration
This is the stage where you explore your data for trends and insights. It's also the stage where you transform the data to use in your model. Thus, data exploration has the following stages:
- Variable identification: exploring variable types in the data
- Univariate analysis: statistical analysis on one variable at a time
- Bivariate analysis: statistical analysis on multiple variables at a time
- Missing value treatment: detecting the cause of a missing value and solving it
- Outlier treatment: detecting the cause of an outlier and solving it
- Variable transformation: e.g. transforming one numeric variable to a different type of numeric variable better suited for the model

# Predictive model and deployment
The steps involved in predictive modeling include:
- Algorithm selection: these can be further classified into two types namely, supervised learning and unsupervised learning. Supervised helps with prediction while unsupervised helps with inference and the presence of a dependent variable determines what algorithm to use. For example, if there is a dependent variable, supervised learning is to be used, and if not then it's unsupervised learning.
- Training model: this is the process where the model learns the relationship between independent and dependent variables. It's at this stage that the dataset is split into test and training
- Predicting/scoring: using the previous model created to make predictions about the future

Once the model is created, the next step is to implement in the real world by creatign data driven products
