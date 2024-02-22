# coding: utf-8
import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
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

# Importing Data

# Specify the path to your CSV file
csv_file_path = 'G:/1. Market Search June2022 onward/EES-Market Search/Sample Project/EES_Sample_GS1.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)


 
# Define the calculate_engagement_drivers function

def calculate_engagement_index(df):
    Affinity_columns          = ['Q1', 'Q2']
    Alignment_columns         = ['Q3']
    Work_Environment_columns  = ['Q8']
    Career_columns            = ['Q7']
    Growth_columns            = ['Q9', 'Q10']
    Compensation_columns      = ['Q24', 'Q25']
    Performance_columns       = ['Q21', 'Q22', 'Q23']
    Direct_Manager_columns    = ['Q11', 'Q12', 'Q13', 'Q14']
    Senior_Leadership_columns = ['Q17', 'Q18', 'Q19', 'Q20']
    Teamwork_columns          = ['Q5']
    Communication_columns     = ['Q6']
    Empowerment_columns       = ['Q4']
    Policies_columns          = ['Q15', 'Q16']
    Work_Lifebalance_columns  = ['Q26']

    total_sum_b_af = df[Affinity_columns].sum().sum()
    total_sum_b_al = df[Alignment_columns].sum().sum()
    total_sum_b_wo = df[Work_Environment_columns].sum().sum()
    total_sum_b_ca = df[Career_columns].sum().sum()
    total_sum_b_go = df[Growth_columns].sum().sum()
    total_sum_b_cp = df[Compensation_columns].sum().sum()
    total_sum_b_pe = df[Performance_columns].sum().sum()
    total_sum_b_dm = df[Direct_Manager_columns].sum().sum()
    total_sum_b_sl = df[Senior_Leadership_columns].sum().sum()
    total_sum_b_tw = df[Teamwork_columns].sum().sum()
    total_sum_b_co = df[Communication_columns].sum().sum()
    total_sum_b_em = df[Empowerment_columns].sum().sum()
    total_sum_b_po = df[Policies_columns].sum().sum()
    total_sum_b_wl = df[Work_Lifebalance_columns].sum().sum()

    total_count_b_af = df[Affinity_columns].count().sum()
    total_count_b_al = df[Alignment_columns].count().sum()
    total_count_b_wo = df[Work_Environment_columns].count().sum()
    total_count_b_ca = df[Career_columns].count().sum()
    total_count_b_go = df[Growth_columns].count().sum()
    total_count_b_cp = df[Compensation_columns].count().sum()
    total_count_b_pe = df[Performance_columns].count().sum()
    total_count_b_dm = df[Direct_Manager_columns].count().sum()
    total_count_b_sl = df[Senior_Leadership_columns].count().sum()
    total_count_b_tw = df[Teamwork_columns].count().sum()
    total_count_b_co = df[Communication_columns].count().sum()
    total_count_b_em = df[Empowerment_columns].count().sum()
    total_count_b_po = df[Policies_columns].count().sum()
    total_count_b_wl = df[Work_Lifebalance_columns].count().sum()

    Affinity_index         = ((total_sum_b_af - total_count_b_af) * 100) / (4 * total_count_b_af)
    Alignment_index        = ((total_sum_b_al - total_count_b_al) * 100) / (4 * total_count_b_al)
    Work_Environment_index = ((total_sum_b_wo - total_count_b_wo) * 100) / (4 * total_count_b_wo)
    Career_index           = ((total_sum_b_ca - total_count_b_ca) * 100) / (4 * total_count_b_ca)
    Growth_index           = ((total_sum_b_go - total_count_b_go) * 100) / (4 * total_count_b_go)
    Compensation_index     = ((total_sum_b_cp - total_count_b_cp) * 100) / (4 * total_count_b_cp)
    Performance_index      = ((total_sum_b_pe - total_count_b_pe) * 100) / (4 * total_count_b_pe)
    Direct_Manager_index   = ((total_sum_b_dm - total_count_b_dm) * 100) / (4 * total_count_b_dm)
    Senior_Leadership_index= ((total_sum_b_sl - total_count_b_sl) * 100) / (4 * total_count_b_sl)
    Teamwork_index         = ((total_sum_b_tw - total_count_b_tw) * 100) / (4 * total_count_b_tw)
    Communication_index    = ((total_sum_b_co - total_count_b_co) * 100) / (4 * total_count_b_co)
    Empowerment_index      = ((total_sum_b_em - total_count_b_em) * 100) / (4 * total_count_b_em)
    Policies_index         = ((total_sum_b_po - total_count_b_po) * 100) / (4 * total_count_b_po)
    Work_Lifebalance_index = ((total_sum_b_wl - total_count_b_wl) * 100) / (4 * total_count_b_wl)

    return {
        'Affinity': Affinity_index,
        'Alignment': Alignment_index,
        'Work Environment': Work_Environment_index,
        'Career': Career_index,
        'Growth': Growth_index,
        'Compensation': Compensation_index,
        'Performance': Performance_index,
        'Direct Manager': Direct_Manager_index,
        'Senior Leadership': Senior_Leadership_index,
        'Teamwork': Teamwork_index,
        'Communication': Communication_index,
        'Empowerment': Empowerment_index,
        'Policies': Policies_index,
        'Work Life Balance': Work_Lifebalance_index
    }

# Calualte average rating for broad parameters
def calculate_average_rating(df):
    Affinity_columns          = ['Q1', 'Q2']
    Alignment_columns         = ['Q3']
    Work_Environment_columns  = ['Q8']
    Career_columns            = ['Q7']
    Growth_columns            = ['Q9', 'Q10']
    Compensation_columns      = ['Q24', 'Q25']
    Performance_columns       = ['Q21', 'Q22', 'Q23']
    Direct_Manager_columns    = ['Q11', 'Q12', 'Q13', 'Q14']
    Senior_Leadership_columns = ['Q17', 'Q18', 'Q19', 'Q20']
    Teamwork_columns          = ['Q5']
    Communication_columns     = ['Q6']
    Empowerment_columns       = ['Q4']
    Policies_columns          = ['Q15', 'Q16']
    Work_Lifebalance_columns  = ['Q26']

    average_af = df[Affinity_columns].sum().sum()
    average_al = df[Alignment_columns].sum().sum()
    average_wo = df[Work_Environment_columns].sum().sum()
    average_ca = df[Career_columns].sum().sum()
    average_go = df[Growth_columns].sum().sum()
    average_cp = df[Compensation_columns].sum().sum()
    average_pe = df[Performance_columns].sum().sum()
    average_dm = df[Direct_Manager_columns].sum().sum()
    average_sl = df[Senior_Leadership_columns].sum().sum()
    average_tw = df[Teamwork_columns].sum().sum()
    average_co = df[Communication_columns].sum().sum()
    average_em = df[Empowerment_columns].sum().sum()
    average_po = df[Policies_columns].sum().sum()
    average_wl = df[Work_Lifebalance_columns].sum().sum()

# Define the calculate_overall_index function

def calculate_overall_index(df):
    q_columns = ['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10',
                 'Q11', 'Q12', 'Q13', 'Q14', 'Q15', 'Q16', 'Q17', 'Q18', 'Q19',
                 'Q20', 'Q21', 'Q22', 'Q23', 'Q24', 'Q25', 'Q26']
    
    total_sum = df[q_columns].sum().sum()
    total_count = df[q_columns].count().sum()
   
    overall_index = ((total_sum - total_count) * 100) / (4 * total_count)
 
    return overall_index

# Define the calculate_engagement_drivers function
def calculate_engagement_drivers(df):
    emotional_connect_columns = ['Q1', 'Q2', 'Q3', 'Q8']
    growth_opportunities_columns = ['Q7', 'Q9', 'Q10']
    pay_perks_columns = ['Q21', 'Q22', 'Q23', 'Q24', 'Q25']
    people_columns = ['Q5', 'Q11', 'Q12', 'Q13', 'Q14', 'Q17', 'Q18', 'Q19', 'Q20']
    work_culture_columns = ['Q4', 'Q6', 'Q15', 'Q16', 'Q26']

    total_sum_em = df[emotional_connect_columns].sum().sum()
    total_sum_go = df[growth_opportunities_columns].sum().sum()
    total_sum_pp = df[pay_perks_columns].sum().sum()
    total_sum_pe = df[people_columns].sum().sum()
    total_sum_wc = df[work_culture_columns].sum().sum()

    total_count_em = df[emotional_connect_columns].count().sum()
    total_count_go = df[growth_opportunities_columns].count().sum()
    total_count_pp = df[pay_perks_columns].count().sum()
    total_count_pe = df[people_columns].count().sum()
    total_count_wc = df[work_culture_columns].count().sum()

    emotional_connect_index = ((total_sum_em - total_count_em) * 100) / (4 * total_count_em)
    growth_opportunities_index = ((total_sum_go - total_count_go) * 100) / (4 * total_count_go)
    pay_perks_index = ((total_sum_pp - total_count_pp) * 100) / (4 * total_count_pp)
    people_index = ((total_sum_pe - total_count_pe) * 100) / (4 * total_count_pe)
    work_culture_index = ((total_sum_wc - total_count_wc) * 100) / (4 * total_count_wc)

    return {
        'Emotional Connect': emotional_connect_index,
        'Growth Opportunities': growth_opportunities_index,
        'Pay & Perks': pay_perks_index,
        'People': people_index,
        'Work Culture': work_culture_index
    }

# Define the calculate_emotional_b_index function
def calculate_emotional_b_index(df):
    Affinity          = ['Q1', 'Q2']
    Alignment         = ['Q3']
    Work_Environment  = ['Q8']
    
    emotional_connect_columns = ['Affinity', 'Alignment', 'Work Environment']
    
    # Calculate individual values for each emotional parameter
    affinity_index = ((df[Affinity].sum().sum() - df[Affinity].count().sum()) * 100) / (4 * df[Affinity].count().sum())
    alignment_index = ((df[Alignment].sum().sum() - df[Alignment].count().sum()) * 100) / (4* df[Alignment].count().sum())
    work_environment_index = ((df[Work_Environment].sum().sum() - df[Work_Environment].count().sum()) * 100) / (4* df[Work_Environment].count().sum())

    return {
            'Affinity Towards Organization': affinity_index,
            'Alignment': alignment_index,
            'Work Environment': work_environment_index
        }



# Define the calculate_workculture_b_index function
def calculate_workculture_b_index(df):
    
    Communication     = ['Q6']
    Empowerment       = ['Q4']
    Policies          = ['Q15', 'Q16']
    Work_Lifebalance  = ['Q26']
    
    work_culture_columns = ['Communication', 'Empowerment', 'Policies & Procedure', 'Work Life Balance']
    
    # Calculate individual values for each workculture parameter
    communication_index = ((df[Communication].sum().sum() - df[Communication].count().sum()) * 100) / (4 * df[Communication].count().sum())
    empowerment_index = ((df[Empowerment].sum().sum() - df[Empowerment].count().sum()) * 100) / (4* df[Empowerment].count().sum())
    policies_index = ((df[Policies].sum().sum() - df[Policies].count().sum()) * 100) / (4* df[Policies].count().sum())
    worklife_index = ((df[Work_Lifebalance].sum().sum() - df[Work_Lifebalance].count().sum()) * 100) / (4* df[Work_Lifebalance].count().sum())

    return {
            'Communication': communication_index,
            'Empowerment': empowerment_index,
            'Policies': policies_index,
            'Work Life Balance': worklife_index
        }
    

# Define the calculate_people_b_index function
def calculate_people_b_index(df):
    
    Direct_Manager    = ['Q11', 'Q12', 'Q13', 'Q14']
    Senior_Leadership = ['Q17', 'Q18', 'Q19', 'Q20']
    Teamwork          = ['Q5']
    
    people_columns = ['Direct Manager', 'Senior Leadership', 'Teamwork & Co-Work Relationship']
    
    # Calculate individual values for each workculture parameter
    dm_index = ((df[Direct_Manager].sum().sum() - df[Direct_Manager].count().sum()) * 100) / (4 * df[Direct_Manager].count().sum())
    sl_index = ((df[Senior_Leadership].sum().sum() - df[Senior_Leadership].count().sum()) * 100) / (4* df[Senior_Leadership].count().sum())
    tr_index = ((df[Teamwork].sum().sum() - df[Teamwork].count().sum()) * 100) / (4* df[Teamwork].count().sum())
    

    return {
            'Direct Manager': dm_index,
            'Senior Leadership': sl_index,
            'Teamwork': tr_index,
         }
    

# Define the calculate_Pay and Perk_b_index function
def calculate_payperk_b_index(df):
    
    Compensation      = ['Q24', 'Q25']
    Performance       = ['Q21', 'Q22', 'Q23']
    
    pay_perks_columns = ['Compensation Program', 'Performance Management']
    
    # Calculate individual values for each workculture parameter
    comp_index = ((df[Compensation].sum().sum() - df[Compensation].count().sum()) * 100) / (4 * df[Compensation].count().sum())
    per_index = ((df[Performance].sum().sum() - df[Performance].count().sum()) * 100) / (4* df[Performance].count().sum())
    
    return {        
            'Compensation Program': comp_index,
            'Performance Management': per_index
        }


# Define the calculate_growthopp_b_index function
def calculate_growthopp_b_index(df):
        
    Career            = ['Q7']
    Growth            = ['Q9', 'Q10']
        
    growthopp_columns = ['Career', 'Growth']
    
    # Calculate individual values for each workculture parameter
    carr_index = ((df[Career].sum().sum() - df[Career].count().sum()) * 100) / (4 * df[Career].count().sum())
    grow_index = ((df[Growth].sum().sum() - df[Growth].count().sum()) * 100) / (4* df[Growth].count().sum())
    
    return {
            'Career Program': carr_index,
            'Growth Program': grow_index                                
    }

def color_based_on_threshold(value, low, mid, high):
    if value <= low:
        return 'red'
    elif low < value <= mid:
        return 'gold'
    else:
        return 'green'

    # Assuming you have a DataFrame named engagement_drivers_data loaded with data
    # Replace this with your actual data

   
    # Calculate engagement levels at the overall level
engagement_levels = {
    'Fully engaged': round(((df['Q27'] == 5) & (df['Q28'] == 5)).sum() / df.shape[0] * 100),
    
    'Engaged': round((((df['Q27'] == 4) & (df['Q28'] == 5)) |
                ((df['Q27'] == 4) & (df['Q28'] == 4)) |
                ((df['Q27'] == 5) & (df['Q28'] == 4))).sum() / df.shape[0] * 100),
    
    'Lost Direction': round((((df['Q27'] == 1) & (df['Q28'] == 5)) |
                       ((df['Q27'] == 2) & (df['Q28'] == 5)) |
                       ((df['Q27'] == 3) & (df['Q28'] == 5)) |
                       ((df['Q27'] == 1) & (df['Q28'] == 4)) |
                       ((df['Q27'] == 2) & (df['Q28'] == 4))).sum() / df.shape[0] * 100),
    
    'Indifferent': round((((df['Q27'] == 3) & (df['Q28'] == 4)) |
                    ((df['Q27'] == 3) & (df['Q28'] == 3)) |
                    ((df['Q27'] == 5) & (df['Q28'] == 3))).sum() / df.shape[0] * 100),
    
    'Non Committal': round((((df['Q27'] == 4) & (df['Q28'] == 2)) |
                      ((df['Q27'] == 5) & (df['Q28'] == 2)) |
                      ((df['Q27'] == 5) & (df['Q28'] == 1)) |
                      ((df['Q27'] == 4) & (df['Q28'] == 3))).sum() / df.shape[0] * 100),
    
    'Looking Around': round((((df['Q27'] == 1) & (df['Q28'] == 3)) |
                       ((df['Q27'] == 2) & (df['Q28'] == 3)) |
                       ((df['Q27'] == 2) & (df['Q28'] == 2)) |
                       ((df['Q27'] == 3) & (df['Q28'] == 2)) |
                       ((df['Q27'] == 3) & (df['Q28'] == 1)) |
                       ((df['Q27'] == 4) & (df['Q28'] == 1))).sum() / df.shape[0] * 100),
    
    'Disengaged': round((((df['Q27'] == 1) & (df['Q28'] == 2)) |
                    ((df['Q27'] == 1) & (df['Q28'] == 1)) |
                    ((df['Q27'] == 2) & (df['Q28'] == 1))).sum() / df.shape[0] * 100)
}

def calculate_average_rating(df):
    parameters = {
        'Affinity': ['Q1', 'Q2'],
        'Alignment': ['Q3'],
        'Work_Environment': ['Q8'],
        'Career': ['Q7'],
        'Growth': ['Q9', 'Q10'],
        'Compensation': ['Q24', 'Q25'],
        'Performance': ['Q21', 'Q22', 'Q23'],
        'Direct_Manager': ['Q11', 'Q12', 'Q13', 'Q14'],
        'Senior_Leadership': ['Q17', 'Q18', 'Q19', 'Q20'],
        'Teamwork': ['Q5'],
        'Communication': ['Q6'],
        'Empowerment': ['Q4'],
        'Policies': ['Q15', 'Q16'],
        'Work_Lifebalance': ['Q26']
        
    }

    #'Engagement_Score': ['Q27', 'Q28']
    # Calculate the average rating for each parameter
    average_ratings = {}
    for parameter, columns in parameters.items():
        average_ratings[parameter] = round(df[columns].mean().mean(),2)
        
    return average_ratings

def calculate_correlation_quadrant(df):
    parameters = {
        'Affinity': ['Q1', 'Q2'],
        'Alignment': ['Q3'],
        'Work_Environment': ['Q8'],
        'Career': ['Q7'],
        'Growth': ['Q9', 'Q10'],
        'Compensation': ['Q24', 'Q25'],
        'Performance': ['Q21', 'Q22', 'Q23'],
        'Direct_Manager': ['Q11', 'Q12', 'Q13', 'Q14'],
        'Senior_Leadership': ['Q17', 'Q18', 'Q19', 'Q20'],
        'Teamwork': ['Q5'],
        'Communication': ['Q6'],
        'Empowerment': ['Q4'],
        'Policies': ['Q15', 'Q16'],
        'Work_Lifebalance': ['Q26'],
        'Engagement_Score': ['Q27', 'Q28']
    }
    # Calculate the correlation with 'Engagement Score' for each parameter
            
    correlations = {}
    engagement_columns = parameters['Engagement_Score']
    for parameter, columns in parameters.items():
        if parameter != 'Engagement_Score':
            correlations[parameter] = round(df[columns].mean(axis=1).corr(df[engagement_columns].mean(axis=1)),2)

    return correlations
