import data_reader as dr
import regression
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from helper_methods import *

import classification.logistic_regression as lr

"""Regression

Follow jupyter notebook workflow for better 
understanding of how to apply data_reader and
Regression model to train your AI.

Link: https://github.com/kotsky/ai-dev/blob/main/regression_workflow.ipynb
Package: https://github.com/kotsky/ai-dev/blob/main/regression.py

"""

"""Logistic Regression

Follow jupyter notebook workflow for better 
understanding of how to apply data_reader and
Logistic Regression model to train your AI.

Link: https://github.com/kotsky/ai-dev/blob/main/logistic_regression_workflow.ipynb
Package: https://github.com/kotsky/ai-dev/blob/main/classification/logistic_regression.py

"""


if __name__ == '__main__':

    main_data = dr.DataTable("data/loan_train.csv")
    target_name = "loan_status"
    main_data.select_target(target_name)
    main_data.plot(parameter1='age', parameter2='Gender', classifier=target_name)
