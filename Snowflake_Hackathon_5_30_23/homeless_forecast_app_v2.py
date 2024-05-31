import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from snowflake.snowpark import Session
from snowflake.snowpark.functions import col

# Snowflake connection parameters
connection_parameters = {
    "account": "soppazn-ydb68432",
    "user": "ANDRESCALVAREZ",
    "password": "Vespuchi95!A-",
    "role": "ACCOUNTADMIN",
    "warehouse": "COMPUTE_WH",
    "database": "HOMELESS_DB",
    "schema": "HOMELESS_SCHEMA"
}

# Create Snowflake session
session = Session.builder.configs(connection_parameters).create()

def load_data(session):
    tableName = 'HOMELESS_SCHEMA.HOMELESS_TABLE'
    dataframe = session.table(tableName)
    df = dataframe.to_pandas()
    return df

def main():
    # Load data
    df = load_data(session)
    
    # Check the columns to verify data
    st.write("DataFrame Columns: ", df.columns)
    st.write(df.head())

    # Ensure required columns exist
    if 'YEAR' in df.columns and 'PIT_TOT_UNSHELT_PIT_HUD' in df.columns and 'COCNUMBER' in df.columns:
        # Convert YEAR to integer to avoid displaying commas
        df['YEAR'] = df['YEAR'].astype(int)
        
        # Prepare data for modeling
        data = df[['YEAR', 'PIT_TOT_UNSHELT_PIT_HUD', 'COCNUMBER']].dropna()
        
        # Allow user to select Continuum of Care (CoC) number
        coc_numbers = data['COCNUMBER'].unique()
        selected_coc = st.selectbox('Select Continuum of Care (CoC) Number:', coc_numbers)
        
        # Filter data for the selected CoC
        coc_data = data[data['COCNUMBER'] == selected_coc]
        
        if not coc_data.empty:
            X = coc_data[['YEAR']]
            y = coc_data['PIT_TOT_UNSHELT_PIT_HUD']

            # Train the linear regression model
            model = LinearRegression()
            model.fit(X, y)

            # Forecasting for the next 5 years
            forecast_years = pd.DataFrame({'YEAR': range(df['YEAR'].max() + 1, df['YEAR'].max() + 6)})
            forecast = model.predict(forecast_years)

            # Combine forecast with years
            forecast_years['FORECAST'] = forecast

            # Streamlit UI
            st.title('Homeless Population Forecast')
            st.write(f"Historical Data for CoC {selected_coc}")
            st.write(coc_data)
            
            # Plot combined chart
            plt.figure(figsize=(10, 6))
            plt.plot(coc_data['YEAR'], coc_data['PIT_TOT_UNSHELT_PIT_HUD'], label='Historical Data')
            plt.plot(forecast_years['YEAR'], forecast_years['FORECAST'], 'orange', linestyle='--', label='Forecasted Data')
            plt.xlabel('Year')
            plt.ylabel('Unsheltered PIT Count')
            plt.title(f'Historical and Forecasted Data for CoC {selected_coc}')
            plt.legend()
            plt.grid(True)
            st.pyplot(plt)

            st.write("Forecasted Data")
            st.write(forecast_years)
        else:
            st.write(f"No data available for CoC {selected_coc}")
    else:
        st.write("Columns 'YEAR', 'PIT_TOT_UNSHELT_PIT_HUD', and 'COCNUMBER' not found in the DataFrame.")

if __name__ == "__main__":
    main()
