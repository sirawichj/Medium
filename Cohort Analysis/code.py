import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
import numpy as np


# Read dataset
df = pd.read_excel('/gdrive/My Drive/Colab Notebooks/Tutorial/Online Retail.xlsx')


# Check top 5 rows of data
df.head(5)