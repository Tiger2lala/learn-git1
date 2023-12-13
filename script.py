import matplotlib.pyplot as plt
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns

data_df = pd.read_csv("datasets/data.csv")

data_df.head().T
#data_df.info()
data_df.diagnosis = data_df.diagnosis.apply(lambda x: 1 if x == 'M' else 0)
#data_df.info()
data_df.shape
data_df.columns
data_df = data_df.dropna(axis = 1)


B, M = data_df.diagnosis.value_counts()
xtickmarks = ['B', 'M']

print(f'Number of Malignant tumours: {M}')
print(f'Number of Benign tumours   : {B}')

def createCountplot():
    fig = plt.figure(figsize = (8, 6))
    ax = fig.add_subplot()

    sns.set_theme(style = 'whitegrid')

    sns.countplot(data = data_df, 
              x = data_df.diagnosis, 
              label = 'Count',
              lw = 4,
              ec = 'black').set(title = 'A count of benign and malignant tumours',
                                  xlabel = 'Diagnosis',
                                  ylabel = 'Count')

    ax.set_xticklabels(xtickmarks)
    plt.show()

createCountplot()

variables_to_omit = ['id', 'diagnosis']
input_data = data_df.drop(variables_to_omit, axis = 1)
r, c = input_data.shape
print(f'Sample size                    : {r}')
print(f'Number of independent variables: {c}')

Malignant = data_df[data_df['diagnosis'] == 1]
Benign = data_df[data_df['diagnosis'] == 0]
worst_mean_se = ['area_worst', 'fractal_dimension_mean', 'radius_se']


def makeHistogram(features):
    for feature in features:
        if not type(feature) is str:
            raise TypeError('Only strings are permitted')

    fig = plt.figure(figsize=(10, 8))
    for i, feature in enumerate(features):
        ax = fig.add_subplot(1, 3, i + 1)
        sns.histplot(Malignant[feature],
                     bins=bins,
                     color='red',
                     label='Malignant',
                     kde=True)
        sns.histplot(Benign[feature],
                     bins=bins,
                     color='green',
                     label='Benign',
                     kde=True)
        plt.title(str(' Distribution of  ') + str(feature.replace('_', ' ').capitalize()))
        plt.xlabel(str(feature.replace('_', ' ').capitalize()))
        plt.ylabel('Density function')
        plt.legend(loc='upper right')
        ax.grid(False)

    plt.tight_layout()
    plt.show()


bins = 'fd'  # Freedman and Diaconis

makeHistogram(worst_mean_se)