# zeiss-data-science-challenge
This repository contains the coding approach to the data science problem as a part of the Zeiss interview process

**I am focussing on the time-series anomaly detection problem.**

* The entire repository is managed with git and hosted on github. Currently, I have set the repository to private.
* The repository uses poetry for package management. Please install virtual environment using `poetry install`.
* The data is stored in `data` folder.
* The data exploration notebook is stored in `notebooks` folder. All the work for this challenge has been done in the [data exploration](/notebooks/data_exploration.ipynb).
* The `tests` folder contains unit tests. Please run `pytest` from the root directory of the repository.
* I have also created `zeiss_iot` folder to package the entire solution for professional use.

## Approach
Based on the description in the problem statement, I have solely focused on analysing the data and visualising it in different manners. I have used `matplotlib` and `seaborn` for visualisation via historgrams, boxplots and line plots. For this short problem, pandas provides more than enough tools for data analysis.

## Assumptions
* The unit of temperature is not specified. It is highly dependent on the industrial process. Since this information is not available, for the sake of simplicity, I assuming that temperature is in degree Celsius.
* Data is originating from a single source_id, so I have assumed that this source_id is generating the data. Another option could be that this is only a data logger, which received the data from multiple machines which could be located in different regions of the world. This would require using time zone information.

## Results
* I have performed all the work for this challenge in `notebooks/data_exploration.ipynb`. The explanation, analysis and results are available in each subsection. I have saved the results/plots inside the notebook so it should be available directly in the notebook. If not, please install poetry virtual environment and execute all the cells using `run all` option from jupyter notebook. I have tested the notebook execution a couple of times and it works. **Please expand all the cells!!**

* `zeiss_iot/data/data_import.py` contains certain functions to showcase my coding style on a daily basis.
PS: I have my own python assistant that can analyse the functions that I write to correct type-hinting and write doc-strings ;) Check out the demonstrator here [SmartPy](https://github.com/kraken24/smartypy).

* Since the task is exploratory in nature, I have written a few pytests to check the data. The test file is present in `tests`. I have used `pytest` for unit testing.

## Hypothesis
The heating and cooling temperature variation is directed such that the temperature of a body or an entity can be maintained constant around 22.5-25 degrees, thereby achieving thermal equilibrium. It could be a HVAC system or controlling temperature during an industrial process.

## Conclusion
Based on various plots, my understanding is that both cooling and heating temperatures are working towards keeping a constant temperature of a certain entity or a body.

## Next Steps
1. A further deep dive could be done to identify trends on week day basis or hourly basis
2. Identify the root cause of missing data
3. Implement z-score (from scipy.stats) to identify outliers
4. Use ML methods like clustering for outlier detection. I have used K-Means and DBSCAN for similar purposes
5. Use Anomaly detection techniques like Isolation Forest, ARIMA etc.
