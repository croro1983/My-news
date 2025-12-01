import requests
import dash
from dash import dcc, html
import json

# Fetch data from NewsData.io API
apikey = "pub_e01786d969bd455ea939b8aceea71f14"
city = input("Enter the city you want to search for: ")

url = f"https://newsdata.io/api/1/latest?apikey={apikey}&country=ro&language=ro&region={city}"
response = requests.get(url)
data = response.json()

# Create Dash app
app = dash.Dash(__name__)

# Build the dashboard layout
app.layout = html.Div([
    html.H1("NewsData.io Dashboard"),
    html.H2(f"Results for: {city}"),
    html.Pre(json.dumps(data, indent=2))
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)