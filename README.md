# Snowflake_May_2024_Hackathon

## Homeless Population Forecasting Application

### Description

This project was developed as part of a hackathon aimed at utilizing Snowflake for creating a data-driven application to forecast the homeless population. The application leverages Snowflake's data warehousing capabilities along with Python's data analysis and visualization libraries to provide insights and forecasts based on historical data.

### Hackathon Activities

The hackathon included the following activities:

1. **Create a Snowflake Trial Account:**
   - Set up a Snowflake trial account to utilize its data warehousing and analysis capabilities.

2. **Create Homeless Database and Schema:**
   - Set up a Homeless Database (`Homeless_DB`) and schema (`Homeless_Schema`) in Snowflake.
   - Imported the provided dataset into Snowflake and created the necessary tables for analysis.

3. **Data Analysis and Reporting:**
   - Conducted data analysis using Snowflake's Snowsight.
   - Developed a Streamlit application to generate reports based on the loaded dataset, allowing users to aggregate and explore homeless data across multiple states and time periods.

4. **Forecast Application:**
   - Built a forecasting application using Streamlit and Scikit-Learn to predict future homeless population trends.
   - Implemented a linear regression model to forecast the yearly growth of unsheltered HUD Point-in-Time (PIT) counts by Continuum of Care (CoC) number.
   - Provided interactive features for users to select metrics and visualize historical and forecasted data.

5. **Demo - Test Drive Arctic Vector Embedding:**
   - Explored Arctic for data storage and retrieval.
   - Tested vector embedding concepts using Arctic to gain hands-on experience with advanced data techniques.

### Features

- **User Selection:**
  - Allows users to select a specific Continuum of Care (CoC) number to visualize and forecast data for that particular region.

- **Metric Selection:**
  - Users can choose from various metrics to analyze and forecast, such as total sheltered or unsheltered counts.

- **Interactive Visualizations:**
  - Provides interactive charts to display historical and forecasted data, enhancing data exploration and decision-making.

- **Forecasting:**
  - Utilizes linear regression to predict future trends in the homeless population, providing valuable insights for planning and resource allocation.

### Technology Stack

- **Snowflake:** Data warehousing and analysis platform.
- **Streamlit:** Python library for creating interactive web applications.
- **Scikit-Learn:** Machine learning library for predictive modeling.
- **Pandas:** Data manipulation and analysis library.
- **Matplotlib:** Visualization library for creating static, animated, and interactive plots.

### How to Run the Application

1. **Clone the Repository:**
   ```sh
   git clone https://github.com/StarLord598/your-repo-name.git
   cd your-repo-name
   ```

2. **Install the Required Packages:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Run the Streamlit Application:**
   ```sh
   streamlit run homeless_forecast_app.py
   ```

4. **Access the Application:**
   - Open the provided URL in your web browser to interact with the application.

### Image Screenshots of Output

![image](https://github.com/StarLord598/Snowflake_May_2024_Hackathon/assets/41198155/cfa9d0ec-344b-44c4-85d8-44e83124e01d)

![image](https://github.com/StarLord598/Snowflake_May_2024_Hackathon/assets/41198155/84282906-507b-448d-98c2-75f6c9455d61)


### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

You can place this description in the `README.md` file of your GitHub repository. This will help others understand the purpose of your project, its features, and how to run it. If you have any other specific details you'd like to include, feel free to modify the description accordingly.
