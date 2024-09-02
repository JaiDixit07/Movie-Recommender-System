# Student Performance Predictor

![Student Performance Predictor](https://assets-homepages-learning.3plearning.net/wp-content/uploads/2020/06/blog-20-student-engagement-strategies-captivating-classroom.png)

## Overview

Welcome to the Student Performance Predictor! This project aims to predict student performance based on various input features using a machine learning model. The web application built with Streamlit allows users to input features and get predictions on student scores.

## Project Features

- **User-Friendly Interface**: Interactive and easy-to-use Streamlit application.
- **Model Performance**: The model achieves an accuracy of around 90% with Linear Regression.

## Technologies Used

- **Streamlit**: For building the interactive web application.
- **Pandas**: Data manipulation and analysis.
- **NumPy**: Numerical operations.
- **Seaborn**: Statistical data visualization.
- **Matplotlib**: Data visualization.
- **Scikit-learn**: Machine learning models and tools.
- **XGBoost**: Gradient boosting model.
- **Dill**: Serialization of Python objects.

## Installation

To run the application locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/yourrepository.git
    cd yourrepository
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

## Requirements

Create a `requirements.txt` file with the following content:

streamlit pandas numpy seaborn matplotlib scikit-learn xgboost dill


## App URL

You can access the deployed app [here](https://student-performance-lsendtwp5wowef2qfydvm5.streamlit.app).

## Model Training

The `model_trainer.py` script is used to train and select the best model for predicting student performance. The script includes various regression models such as RandomForest, DecisionTree, GradientBoosting, and XGBoost. The best performing model based on accuracy is saved for use in the application.

## Author

**Jai Dixit**

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Scikit-learn Documentation](https://scikit-learn.org/stable/documentation.html)
- [XGBoost Documentation](https://xgboost.readthedocs.io/en/latest/)

