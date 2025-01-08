# case 1 - real-time anomaly prediction for a mobile communications company

## problem statement

The data comes from the various network elements (mobile antenna/radio equipment) a mobile communications company owns. Each element acts as an aggregator (similar to a router), and records time-series data with varying precision/sampling frequency (e.g., hourly or more frequently, such as every 15 minutes).

The recorded data includes hourly values of many Key performance indexes (KPIs), including the following:

* Timestamp: The specific time of the measurement.
* Number of calls (voice traffic): Total call volume.
* Number of initiated calls: The total calls attempted.
* Number of failed calls: Calls that drop or fail to connect successfully.
* Number of handovers: Calls that transfer to another cell tower.
* Number of mobile users: Total unique users connected.

The company aims to develop a real-time model that can predict whether an anomaly will occur in the next 5 minutes.

## solution

the (very general) steps would be something like this

* Collect and preprocess real-time KPI data streams.
* Use a time-series forecasting model (e.g., ARIMA, LSTM, Prophet) to predict KPI values for the next 5 minutes.
* Identify anomalies in the predictions by comparing them to expected ranges, using statistical methods or machine learning-based anomaly detection algorithms (e.g., Isolation Forest, One-Class SVM).

So, first you do create a predictive model that captures the general trend (and the weekly/daily/etc variations) and then identify anomalies in those predictions using a anomaly detection model.

Details of the solution:

* collect KPI data - real-time data from network elements is aggregated (e.g., every 15 minutes).

* about the preprocessing
  * use FFT (fast fourier transform) to analyze periodic components. Apply a low-pass filter to remove high-frequency noise.
  * this approach is similar to "STL": <https://www.statsmodels.org/dev/examples/notebooks/generated/stl_decomposition.html>

* about the forecasting model
  * train ARIMA models on the preprocessed data. Use these models to forecast KPI values for the next 5 minutes.
    * <https://en.wikipedia.org/wiki/Autoregressive_integrated_moving_average>

  * seasonal variation
    * there's seasonal variation in the data. Seasonality refers to recurring patterns or cycles in time-series data that happen at regular intervals. Common examples include daily seasonality (patterns repeating within a day, e.g., higher network usage during business hours), weekly seasonality (patterns repeating across the days of a week, e.g., higher traffic on weekdays, lower on weekends), annual seasonality (patterns repeating over a year, e.g., increased retail sales during holidays). The weekly variation seems important in the data - the data exhibits systematic variations across days of the week, such as: Higher call volumes on weekdays due to work-related activity. Lower call volumes on weekends or holidays. Increased anomalies during specific timeframes (e.g., Monday mornings or Friday afternoons). These variations are tied to behavioral patterns of users and qualify as weekly seasonality.
    * in theory, could be captured by SARIMA (Seasonal ARIMA). Not sure why but SARIMA didn't work. Instead, they deal with it by creating different models.
    * week-specific models - trained weekly or bi-weekly to adapt to weekly fluctuations in the data, ensuring that the model remains performant...
    * another option is day-specific models - a separate model is created for each day of the week. For example, one model for Monday, another for Tuesday, and so on. This approach helps account for patterns specific to each day (e.g., weekend traffic may differ from weekday traffic). When training or using these models, the data is filtered by the corresponding day of the week.

* about the anomaly detection
  * they use the Isolation Forest algorithm to detect anomalies in the forecasted data.
  * there are few anomalies in the training data so they inject artificial anomalies - To train the model, introduce synthetic anomalies into the historical data. They are modeled as poisson noise.

## References

these books seem to be a good place to start...

* [2022 Time series forecasting in Python, peixeiro MANNING](https://www.amazon.com/Time-Series-Forecasting-in-Python/dp/B0C3WSDLJL/)
* [2025 Outlier detection in Python, kennedy MANNING](https://www.amazon.com/Outlier-Detection-Python-Brett-Kennedy/dp/1633436470/)
