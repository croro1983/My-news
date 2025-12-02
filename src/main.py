import dash
from dash import html
import requests
import webbrowser

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Latest News from Romania"),
    html.Div(id='news-container', style={'marginTop': '20px'})
])

@app.callback(
    dash.Output('news-container', 'children'),
    dash.Input('interval-component', 'n_intervals'),
    prevent_initial_call=False
)
def update_news(n):
    url = "https://newsdata.io/api/1/latest"
    params = {
        "country": "ro",
        "apikey": "pub_e01786d969bd455ea939b8aceea71f14"  
    }
    
    try:
        response = requests.get(url, params=params)
        data = response.json()
        
        if data.get('results'):
            news_items = []
            for article in data['results'][:10]:  # Display top 10 articles
                news_items.append(
                    html.Div([
                        html.H3(article.get('title', 'No title')),
                        html.P(article.get('description', 'No description')),
                        html.A('Read more', href=article.get('link', '#'), target='_blank'),
                        html.Hr()
                    ], style={'border': '1px solid #ddd', 'padding': '10px', 'marginBottom': '10px'})
                )
            return news_items
        else:
            return html.P("No news available.")
    
    except Exception as e:
        return html.P(f"Error fetching news: {str(e)}")

if __name__ == '__main__':
    app.run(port=8050, open_browser=True)