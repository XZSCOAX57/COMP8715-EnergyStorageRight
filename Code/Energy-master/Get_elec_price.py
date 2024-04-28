import pandas as pd

# Get electricity prices in different countries
# Note: The data of the prices are offered by electricity_price.csv, which includes the data in 2019 with 188 countries. 
def get_elec_price(country_code):
    data = pd.read_csv('electricity_price.csv', sep=',')
    try:
        return data[data['ISO2']==country_code][['2019']].iloc[0][0] / 100
    except IndexError:
        return 0.176 # the average value of the 188 countries/regions
