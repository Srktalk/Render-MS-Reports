# coding: utf-8
# Call the funtions
from custom_functions import *

# Library Calls
import dash
#import dash_core_components as dcc
#import dash_bootstrap_components as dbc
import dash_html_components as html
#import dash_maintain_components as dmc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import logging
import dash_mantine_components as dmc
import plotly.graph_objects as go
import textwrap
import dash_table
from dash import dcc
from dash import html
from dash import dash_table
from dash.dash_table.Format import Group


#------------------------

# Importing Data

# Specify the path to your CSV file
# = 'G:/1. Market Search June2022 onward/EES-Market Search/Sample Project/EES_Sample_GS1.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv('EES_Sample_GS1.csv')




# Initialize the Dash app
app = dash.Dash(__name__)
server = app.server
# Define the layout of the Dash app
app.layout = html.Div(
    children=[
        dmc.Title(children='Employee Engagement: --Company Name--', order=3,
                   style={'font-family': 'IntegralCF-ExtraBold', 'text-align': 'center', 'color': 'slategray'}),
        dmc.Divider(label='Overview', labelPosition='center', size='xl'),
        # Add a button to the layout
        html.Button('Update Metrics', id='update-metrics-button', n_clicks=0),

        dmc.Group(
            display='flex',
            grow=True,
            children=[
                dmc.Paper(
                    radius="md",
                    withBorder=True,
                    shadow='xs',
                    p='sm',
                    style={'height': '350px'},
                    children=[
                        dmc.Text('Total Number of Respondents', size='xs', color='dimmed',
                                 style={'font-family': 'IntegralCF-ExtraBold'}),
                        dmc.Text(id='sample_size', size='xl', style={'font-family': 'IntegralCF-ExtraBold'}),
                    ]
                ),
                dmc.Paper(
                    radius="md",
                    withBorder=True,
                    shadow='xs',
                    p='sm',
                    style={'height': '350px', 'display': 'flex', 'flex-direction': 'column'},
                    children=[
                        dmc.Text('Overall Index', size='xs', color='dimmed',
                                 style={'font-family': 'IntegralCF-ExtraBold'}),
                        dcc.Graph(id='overall_index', style={'flex': '1'})
                    ]
                ),
                dmc.Paper(
                    radius="md",
                    withBorder=True,
                    shadow='xs',
                    p='sm',
                    style={'height': '350px'},
                    children=[
                        dmc.Title('Pillars of Engagement Drivers', order=2, 
                                  style={'font-family': 'IntegralCF-Regular', 'text-align': 'center', 'color': 'grey', 'letter-spacing': '1px','font-size':'16px'}),
                        dcc.Graph(id='engagement_drivers')
                    ]
                ),
            ]
        ),
        #dmc.Divider(label='Engagement Drivers', labelPosition='center', size='xl'),
        #dmc.Group(
        #    display='flex',
        #    grow=True,
        #    children=[
        #        dmc.Paper(
        #            radius="md",
        #            withBorder=True,
        #            shadow='xs',
        #            p='sm',
        #            style={'height': '450px'},
        #            children=[
        #                dmc.Title('Pillars of Engagement Drivers', order=2, style={'font-family': 'IntegralCF-Regular', 'text-align': 'center', 'color': 'grey', 'letter-spacing': '1px'}),
        #                dcc.Graph(id='engagement_drivers')
        #            ]
        #        ),
        #    ]
        #),
        dmc.Divider(label='Engagement Drivers - Broad Parameters', labelPosition='center', size='xl'),
        dmc.Group(
            display='flex',
            grow=True,
            children=[
                dmc.Paper(
                    radius="md",
                    withBorder=True,
                    shadow='xs',
                    p='sm',
                    style={'height': '450px'},
                    children=[
                        dmc.Title('Emotional Connect', order=2, 
                                  style={'font-family': 'IntegralCF-Regular', 'text-align': 'center', 'color': 'grey', 'letter-spacing': '1px','font-size':'16px'}),
                        dcc.Graph(id='emotional_connect')
                    ]
                ),
                dmc.Paper(
                    radius="md",
                    withBorder=True,
                    shadow='xs',
                    p='sm',
                    style={'height': '450px'},
                    children=[
                        dmc.Title('Work Culture', order=2, 
                                  style={'font-family': 'IntegralCF-Regular', 'text-align': 'center', 'color': 'grey', 'letter-spacing': '1px','font-size':'16px'}),
                        dcc.Graph(id='work_culture')
                    ]
                ),
                dmc.Paper(
                    radius="md",
                    withBorder=True,
                    shadow='xs',
                    p='sm',
                    style={'height': '450px'},
                    children=[
                        dmc.Title('People Approach', order=2, 
                                  style={'font-family': 'IntegralCF-Regular', 'text-align': 'center', 'color': 'grey', 'letter-spacing': '1px','font-size':'16px'}),
                        dcc.Graph(id='people')
                    ]
                ),

                
            ]
        ),
        dmc.Divider(label='Engagement Drivers - Broad Parameters - Continued', labelPosition='center', size='xl'),
        dmc.Group(
            display='flex',
            grow=True,
            children=[
                
                dmc.Paper(
                    radius="md",
                    withBorder=True,
                    shadow='xs',
                    p='sm',
                    style={'height': '450px'},
                    children=[
                        dmc.Title('Pay & Perks', order=2, 
                                  style={'font-family': 'IntegralCF-Regular', 'text-align': 'center', 'color': 'grey', 'letter-spacing': '1px','font-size':'16px'}),
                        dcc.Graph(id='pay_perk')
                    ]
                ),

                dmc.Paper(
                    radius="md",
                    withBorder=True,
                    shadow='xs',
                    p='sm',
                    style={'height': '450px'},
                    children=[
                        dmc.Title('Growth Opportunities', order=2, 
                                  style={'font-family': 'IntegralCF-Regular', 'text-align': 'center', 'color': 'grey', 'letter-spacing': '1px','font-size':'16px'}),
                        dcc.Graph(id='growth_opportunities')
                    ]
                ),
                dmc.Paper(
                    radius="md",
                    withBorder=True,
                    shadow='xs',
                    p='sm',
                    style={'height': '450px'},
                    children=[
                        dmc.Title('Engagement Levels', order=2, 
                                  style={'font-family': 'IntegralCF-Regular', 'text-align': 'center', 'color': 'grey', 'letter-spacing': '1px','font-size':'16px'}),
                        dash_table.DataTable(
                            id='engagement-levels-table',
                            columns=[
                                {'name': 'Engagement Level', 'id': 'Engagement Level'},
                                {'name': 'Percentage', 'id': 'Percentage', 'type': 'numeric'},
                            ],
                            style_table={'height': '300px', 'overflowY': 'auto'},
                            style_header={
                                'backgroundColor': 'rgb(230, 230, 230)',  # Header background color
                                'fontWeight': 'bold',
                            },
                            style_cell={
                                'textAlign': 'center',
                                'minWidth': '100px',  # Minimum width of each cell
                                'maxWidth': '100px',  # Maximum width of each cell
                                'whiteSpace': 'normal',  # Allow text to wrap
                                'height':'auto'
                            },
                            style_data_conditional=[
                                {
                                    'if': {'column_id': 'Percentage'},
                                    'textAlign': 'center',  # Center align values in the 'Percentage' column
                                    
                                },
                            ],
                        ),
                        
                    ]
                ),

            ]
        ),
        dmc.Divider(label='Importance Vs Significance', labelPosition='center', size='xl'),
        dmc.Group(
            display='flex',
            grow=True,
            children=[
                dmc.Paper(
                    radius="md",
                    withBorder=True,
                    shadow='xs',
                    p='sm',
                    style={'height': '650px'},
                    children=[
                        
                        dmc.Title('Quatdrant Plot', order=2, 
                                  style={'font-family': 'IntegralCF-Regular', 'text-align': 'center', 'color': 'grey', 'letter-spacing': '1px','font-size':'16px'}),
                        
                        # Add a new Graph component for the scatter plot
                        dcc.Graph(id='average_correlation_scatter', style={'flex': '1'}),
                        
                    ]
                ),
            ]
        ),

    ],  # End of first Child
)  # End of app.layout

# --------------------




# Modify callback decorator and function
@app.callback(
    [Output('sample_size', 'children'),
     Output('overall_index', 'figure'),
     Output('engagement_drivers', 'figure'),
     Output('emotional_connect', 'figure'),
     Output('work_culture', 'figure'),
     Output('people', 'figure'),
     Output('pay_perk', 'figure'),
     Output('growth_opportunities', 'figure'),
     Output('engagement-levels-table', 'data'),
     Output('average_correlation_scatter', 'figure')],
    [Input('update-metrics-button', 'n_clicks')]
)
def update_metrics(n_clicks):
    try:
        # Assuming you have a DataFrame named df loaded with data
        count = len(df)
        overall_index = calculate_overall_index(df)
        engagement_drivers_data = calculate_engagement_drivers(df)
        engagement_index_data = calculate_engagement_index(df)
        emotional_b_index_data = calculate_emotional_b_index(df)
        workculture_b_index_data = calculate_workculture_b_index(df)
        people_b_index_data = calculate_people_b_index(df)
        payperk_b_index_data = calculate_payperk_b_index(df)
        growthopp_b_index_data = calculate_growthopp_b_index(df)
        #engagement_levels_table_data = [{'Engagement Level': level, 'Percentage': percentage} for level, percentage in engagement_levels.items()]
        engagement_levels_table_data = [{'Engagement Level': level, 'Percentage': f"{percentage:.1f}%"} 
                                        for level, percentage in engagement_levels.items()]
        
        # Calculate average ratings and correlations
        average_ratings = calculate_average_rating(df)
        correlations = calculate_correlation_quadrant(df)

        
        
        # Create a DataFrame for the scatter plot
        scatter_data = pd.DataFrame({'Parameter': list(average_ratings.keys()),
                                     'Average': list(average_ratings.values()),
                                     'Correlation': list(correlations.values())})
        
        # Calculate median values for x and y axes
        median_average = scatter_data['Average'].median()
        median_correlation = scatter_data['Correlation'].median()
        
        # Shift x and y axes to their respective median values
        #scatter_data['Shifted_Average'] = scatter_data['Average'] - median_average
        #scatter_data['Shifted_Correlation'] = scatter_data['Correlation'] - median_correlation
        
    except Exception as e:
        logging.exception("Error in callback: %s", str(e))
        #scatter_data = pd.DataFrame({'Parameter': [], 'Average': [], 'Correlation': [], 'Shifted_Average': [], 'Shifted_Correlation': []})
        #scatter_data = pd.DataFrame({'Parameter': [], 'Average': [], 'Correlation': []})
        # Set default values for scatter_data in case of an exception
        scatter_data = pd.DataFrame({'Parameter': [], 'Average': [], 'Correlation': []})
        median_average = 0
        median_correlation = 0





    # Set the range for the gauge chart (e.g., 0 to 100 for percentage)
    gauge_range = [0, 100]
    
    fig=go.Figure()

    fig.add_traces(go.Indicator (
        mode="gauge+number",
        value=overall_index,
        title="Overall Index",
        gauge=dict(
            axis=dict(range=gauge_range),
            bar=dict(color="blue"),
            bgcolor="white",
            borderwidth=2,
            bordercolor="gray",
            steps=[
                dict(range=[gauge_range[0], gauge_range[1] / 3], color="red"),
                dict(range=[gauge_range[1] / 3, 2 * gauge_range[1] / 3], color="yellow"),
                dict(range=[2 * gauge_range[1] / 3, gauge_range[1]], color="green"),
            ],
        ),
    ))
    
    fig.update_layout(
        margin=dict(t=50),
    )
    
     # Example input values for color ranges
    low_threshold = 40
    mid_threshold = 70
    high_threshold = 90
    
    # Wrap text for x-axis labels
    #wrapped_labels = [textwrap.fill(label, width=10) for label in engagement_drivers_data.keys()]

    # Create a bar chart for engagement drivers
    fig_engagement_drivers = px.bar(
        x=list(engagement_drivers_data.keys()),
        y=list(engagement_drivers_data.values()),
        labels={'y': 'Engagement Index'},
        text=[f'{val:.2f}' for val in engagement_drivers_data.values()],  # Display the values on top of the bars
        opacity=0.7,
        color=[color_based_on_threshold(val, low_threshold, mid_threshold, high_threshold) for val in engagement_drivers_data.values()],
        color_discrete_map={'red': 'red', 'gold': 'gold', 'green': 'green'},
        width=10,
    )
    # Customize layout for better appearance
    fig_engagement_drivers.update_layout(
        xaxis_title='Engagement Drivers',
        yaxis_title='Engagement Index',
        showlegend= False,
        margin=dict(t=25),
        height=300,  # Adjust the height as needed
        width=480,   # Adjust the width as needed
        xaxis=dict(
            #tickangle=0,  # Rotate x-axis labels by 45 degrees
            #tickmode='array',
            #tickvals=list(range(len(engagement_drivers_data))),
            #ticktext=list(engagement_drivers_data.keys()),
            #tickfont=dict(size=10),
            tickmode='array',
            tickvals=list(range(len(engagement_drivers_data))),
            ticktext=[label[:10] + '<br>' + label[10:] if len(label) > 10 else label for label in engagement_drivers_data.keys()],
            tickfont=dict(size=10),
        )
    )

    # Create a bar chart for emotional connect
    fig_emotional_connect = px.bar(
        x=list(emotional_b_index_data.keys()),
        y=[min(val, 100) for val in emotional_b_index_data.values()],  # Cap y-values at 100
        labels={'y': 'Engagement Index'},
        text=[f'{min(val, 100):.2f}' for val in emotional_b_index_data.values()],  # Display the values on top of the bars
        opacity=0.7,
        color=[color_based_on_threshold(min(val, 100), low_threshold, mid_threshold, high_threshold) for val in emotional_b_index_data.values()],
        color_discrete_map={'red': 'red', 'gold': 'gold', 'green': 'green'},
        width=10,
    )
    # Customize layout for better appearance
    fig_emotional_connect.update_layout(
        #title_text='Emotional Connect',
        #xaxis_title='Emotional Connect',
        #yaxis_title='Engagement Index',
        showlegend=False,
        margin=dict(t=25),
        height=350,  # Adjust the height as needed
        width=450,   # Adjust the width as needed
        xaxis=dict(
            tickmode='array',
            tickvals=list(range(len(emotional_b_index_data))),
            ticktext=[label[:10] + '<br>' + label[10:] if len(label) > 10 else label for label in emotional_b_index_data.keys()],
            tickfont=dict(size=10),
        ),
        yaxis=dict(
            range=[0, 100],  # Set the y-axis range to be [0, 100]
        )
    )

    # Create a bar chart for work culture connect
    fig_work_culture = px.bar(
        x=list(workculture_b_index_data.keys()),
        y=[min(val, 100) for val in workculture_b_index_data.values()],  # Cap y-values at 100
        labels={'y': 'Engagement Index'},
        text=[f'{min(val, 100):.2f}' for val in workculture_b_index_data.values()],  # Display the values on top of the bars
        opacity=0.7,
        color=[color_based_on_threshold(min(val, 100), low_threshold, mid_threshold, high_threshold) for val in workculture_b_index_data.values()],
        color_discrete_map={'red': 'red', 'gold': 'gold', 'green': 'green'},
        width=10,
    )

    # Customize layout for better appearance
    fig_work_culture.update_layout(
        #title_text='Work Culture',
        #xaxis_title='Work Culture',
        yaxis_title='Engagement Index',
        showlegend=False,
        margin=dict(t=50),
        height=350,  # Adjust the height as needed
        width=450,   # Adjust the width as needed
        xaxis=dict(
            #tickangle=0,  # Rotate x-axis labels by 45 degrees
            #tickmode='array',
            #tickvals=list(range(len(engagement_drivers_data))),
            #ticktext=list(engagement_drivers_data.keys()),
            #tickfont=dict(size=10),
            tickmode='array',
            tickvals=list(range(len(workculture_b_index_data))),
            ticktext=[label[:10] + '<br>' + label[10:] if len(label) > 10 else label for label in workculture_b_index_data.keys()],
            tickfont=dict(size=10),
        ),
        yaxis=dict(
            range=[0, 100],  # Set the y-axis range to be [0, 100]
        )
    )

    # Create a bar chart for People
    fig_people = px.bar(
        x=list(people_b_index_data.keys()),
        y=list(people_b_index_data.values()),
        labels={'y': 'People Index'},
        text=[f'{val:.2f}' for val in people_b_index_data.values()],  # Display the values on top of the bars
        opacity=0.7,
        color=[color_based_on_threshold(val, low_threshold, mid_threshold, high_threshold) for val in people_b_index_data.values()],
        color_discrete_map={'red': 'red', 'gold': 'gold', 'green': 'green'},
        width=10,
    )

    # Customize layout for better appearance
    fig_people.update_layout(
        #title_text='People Approach',
        #xaxis_title='People Approach',
        yaxis_title='Engagement Index',
        showlegend=False,
        margin=dict(t=50),
        height=350,  # Adjust the height as needed
        width=450,   # Adjust the width as needed
        xaxis=dict(
            #tickangle=0,  # Rotate x-axis labels by 45 degrees
            #tickmode='array',
            #tickvals=list(range(len(engagement_drivers_data))),
            #ticktext=list(engagement_drivers_data.keys()),
            #tickfont=dict(size=10),
            tickmode='array',
            tickvals=list(range(len(people_b_index_data))),
            ticktext=[label[:10] + '<br>' + label[10:] if len(label) > 10 else label for label in people_b_index_data.keys()],
            tickfont=dict(size=10),
        )

    )

    # Create a bar chart for Pay and Perk connect
    fig_pay_perk = px.bar(
        x=list(payperk_b_index_data.keys()),
        y=list(payperk_b_index_data.values()),
        labels={'y': 'Work Culture Index'},
        text=[f'{val:.2f}' for val in payperk_b_index_data.values()],  # Display the values on top of the bars
        opacity=0.7,
        color=[color_based_on_threshold(val, low_threshold, mid_threshold, high_threshold) for val in payperk_b_index_data.values()],
        color_discrete_map={'red': 'red', 'gold': 'gold', 'green': 'green'},
        width=10,
    )

    # Customize layout for better appearance
    fig_pay_perk.update_layout(
        #title_text='Pay & Perk',
        #xaxis_title='Pay & Perk',
        yaxis_title='Engagement Index',
        showlegend=False,
        margin=dict(t=50),
        height=350,  # Adjust the height as needed
        width=450,   # Adjust the width as needed
        xaxis=dict(
            #tickangle=0,  # Rotate x-axis labels by 45 degrees
            #tickmode='array',
            #tickvals=list(range(len(engagement_drivers_data))),
            #ticktext=list(engagement_drivers_data.keys()),
            #tickfont=dict(size=10),
            tickmode='array',
            tickvals=list(range(len(payperk_b_index_data))),
            ticktext=[label[:10] + '<br>' + label[10:] if len(label) > 10 else label for label in payperk_b_index_data.keys()],
            tickfont=dict(size=10),
        )

    )

    # Create a bar chart for growth Opportunities
    fig_growth_opportunities = px.bar(
        x=list(growthopp_b_index_data.keys()),
        y=list(growthopp_b_index_data.values()),
        labels={'y': 'Work Culture Index'},
        text=[f'{val:.2f}' for val in growthopp_b_index_data.values()],  # Display the values on top of the bars
        opacity=0.7,
        color=[color_based_on_threshold(val, low_threshold, mid_threshold, high_threshold) for val in growthopp_b_index_data.values()],
        color_discrete_map={'red': 'red', 'gold': 'gold', 'green': 'green'},
        width=10,
    )

    # Customize layout for better appearance
    fig_growth_opportunities.update_layout(
        #title_text='Growth Opportunities',
        #xaxis_title='Growth Opportunities',
        yaxis_title='Engagement Index',
        showlegend=False,
        margin=dict(t=50),
        height=350,  # Adjust the height as needed
        width=450,   # Adjust the width as needed
        xaxis=dict(
            #tickangle=0,  # Rotate x-axis labels by 45 degrees
            #tickmode='array',
            #tickvals=list(range(len(engagement_drivers_data))),
            #ticktext=list(engagement_drivers_data.keys()),
            #tickfont=dict(size=10),
            tickmode='array',
            tickvals=list(range(len(growthopp_b_index_data))),
            ticktext=[label[:10] + '<br>' + label[10:] if len(label) > 10 else label for label in growthopp_b_index_data.keys()],
            tickfont=dict(size=10),
        )

    )
    
    # Create a scatter plot for average versus correlation
    fig_scatter = px.scatter(scatter_data, x='Average', y='Correlation', text='Parameter', size='Average', color='Parameter',
                             labels={'Average': 'Average Rating', 'Correlation': 'Correlation with Engagement Score'},
                             #title='Average Rating vs Correlation',
                             width=1000, height=600)

    fig_scatter.update_traces(
        textposition='middle right',  # Adjust the text position as needed
        hoverinfo='text',  # Show text on hover
    )
    # Set the layout to position x-axis and y-axis at median values
    fig_scatter.update_layout(
        showlegend=False,
        shapes=[
            dict(
                type='line',
                x0=median_average,
                x1=median_average,
                y0=0,
                y1=0.8,
                line=dict(color='black', width=1)
            ),
            dict(
                type='line',
                x0=2,
                x1=5,
                y0=median_correlation,
                y1=median_correlation,
                line=dict(color='black', width=1)
            )
        ]
    )

    return f"{count:,} respondents", fig, fig_engagement_drivers, fig_emotional_connect, fig_work_culture, fig_people, fig_pay_perk, fig_growth_opportunities, engagement_levels_table_data, fig_scatter

if __name__ == '__main__':
    app.run_server(debug=True)
