NASA Battery Dataset Analysis


This project aims to analyze and visualize the NASA Battery dataset using Plotly and pandas. The dataset contains various battery performance metrics such as charge/discharge cycles, impedance, electrolyte resistance (Re), charge transfer resistance (Rct), and more. The analysis helps in understanding how these parameters change as the battery ages over multiple cycles.

Prerequisites:
--------------
Python 3.x
pandas
plotly
--------------
You can install the required libraries using pip:

bash
Copy code
pip install pandas plotly
Project Overview
The project contains two main tasks:

Battery Impedance and Resistance Analysis
This analysis visualizes the battery impedance, electrolyte resistance (Re), and charge transfer resistance (Rct) over charge/discharge cycles.
Battery Test Measurements Visualization
A separate analysis for test measurements (voltage, current, temperature, etc.) for the battery load during the testing.


1. Battery Impedance and Resistance Analysis
This code loads the dataset and visualizes the battery impedance, electrolyte resistance (Re), and charge transfer resistance (Rct) against the cycle count. It uses the Plotly library to create interactive line charts.

with RE:
<img width="1420" alt="Screenshot 2024-12-16 at 10 33 40 PM" src="https://github.com/user-attachments/assets/d67adcc0-9d8d-4526-8192-89dc75b9eeb3" />

with CTR:
<img width="1462" alt="Screenshot 2024-12-16 at 10 33 21 PM" src="https://github.com/user-attachments/assets/5cadabbd-297e-49c9-845b-ec77dab00d5f" />


2. Test Measurements Visualization
This code analyzes and visualizes the battery's test measurements, such as voltage, current, and temperature, over time during the test. It plots the measured values against time to show how these parameters change during testing.

i) Voltage Measured over Time
<img width="1384" alt="Screenshot 2024-12-16 at 10 52 49 PM" src="https://github.com/user-attachments/assets/f48b78df-90f5-4191-96bd-14169082b5b3" />

ii) Current Measured over Time
<img width="1367" alt="Screenshot 2024-12-16 at 10 56 14 PM" src="https://github.com/user-attachments/assets/85476a7a-90d1-4331-bab1-4bb275f3d2c1" />

iii) Temperature Measured over Time
<img width="1433" alt="Screenshot 2024-12-16 at 11 00 26 PM" src="https://github.com/user-attachments/assets/a5e47fcb-da8a-40c1-a1d6-9added740f5e" />

iv) Voltage under load over Time
<img width="1432" alt="Screenshot 2024-12-16 at 11 01 18 PM" src="https://github.com/user-attachments/assets/d42bb1c5-59dc-4228-877a-b4a06bb67df4" />

v) Current nder load over Time
<img width="1415" alt="Screenshot 2024-12-16 at 11 02 14 PM" src="https://github.com/user-attachments/assets/20d41939-52b3-45b5-a7d4-a7bba4bbaf5e" />

Data Files:

metadata_nasa_battery.csv: This file contains the battery data including charge/discharge cycles, electrolyte resistance (Re), and charge transfer resistance (Rct).
00001.csv: This file contains the battery test measurements like voltage, current, temperature, etc.

Output:

The output of the above code will be interactive line plots showing:

Electrolyte resistance (Re) and charge transfer resistance (Rct) over cycles.
Measured voltage, current, and temperature over time.
These visualizations help in understanding how the battery's internal parameters and external measurements change as the battery undergoes multiple charge and discharge cycles.

Conclusion
By visualizing these battery parameters, we can analyze the aging process and how the internal conditions (such as resistance) change during cycling. This helps in understanding the battery's health and performance over time.
