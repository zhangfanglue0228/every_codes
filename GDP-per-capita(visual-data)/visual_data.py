import pandas as pd
import plotly.express as px
from plotly.offline import plot

year_list = []
for i in range(2005, 2018 + 1):
    year_list.append(i)

year_list_country = year_list[:]
year_list_country.insert(0, 'country')

country_data = pd.read_excel("Data Geographies - v1 - by Gapminder.xlsx", "list-of-countries-etc")[['name', 'five_regions']]
life_exp_data = pd.read_excel("life_expectancy_years.xlsx")[year_list_country]
pop_data = pd.read_excel("population_total.xlsx")[year_list_country]
gdp_data = pd.read_excel("income_per_person_gdppercapita_ppp_inflation_adjusted.xlsx")[year_list_country]


life_exp_data = life_exp_data.dropna(axis=0)


final_data = pd.DataFrame()
for i in range(len(country_data)):
    a=country_data.loc[i]
    d=pd.DataFrame(a).T
    final_data = final_data.append([d]*14)

final_data['year'] = year_list * 197
final_data.index = [i for i in range(len(final_data))]

gdp,life,pop = [],[],[]
for i in range(len(final_data)):
    x = final_data.loc[i]['name']
    y = final_data.loc[i]['year']
    if x in gdp_data['country'].values.tolist():
        gdp.append(int(gdp_data[(gdp_data['country']==x)][y]))
    else:
        gdp.append(0)
    if x in life_exp_data['country'].values.tolist():
        life.append(int(life_exp_data[(life_exp_data['country']==x)][y]))
    else:
        life.append(0)
    if x in pop_data['country'].values.tolist():
        pop.append(int(pop_data[(pop_data['country']==x)][y]))
    else:
        pop.append(0)

final_data['pop'] = pop
final_data['lifeExp'] = life
final_data['gdpPercap'] = gdp

final_data.columns = ['country', 'continent', 'year', 'pop', 'lifeExp', 'gdpPercap']

# fig = px.scatter(final_data, x="lifeExp", y="gdpPercap", animation_frame="year",
#                  animation_group="country",size="gdpPercap", color="continent",
#                  hover_name="country",log_x=True, size_max=45)
# plot(fig)


# 自适应y轴
years = [str(i) for i in range(2005, 2019)]

for continent in final_data['continent']:
    if continent not in continents:
        continents.append(continent)

figure = {
    'data': [],
    'layout': {},
    'frames': []
}

# fill in most of layout
figure['layout']['xaxis'] = {'range': [30, 85], 'title': '预期寿命'}
figure['layout']['yaxis'] = {'title': '人均生产总值', 'type': 'log'}
figure['layout']['hovermode'] = 'closest'
figure['layout']['sliders'] = {
    'args': [
        'transition', {
            'duration': 400,
            'easing': 'cubic-in-out'
        }
    ],
    'initialValue': '1952',
    'plotlycommand': 'animate',
    'values': years,
    'visible': True
}
figure['layout']['updatemenus'] = [
    {
        'buttons': [
            {
                'args': [None, {'frame': {'duration': 500, 'redraw': False},
                         'fromcurrent': True, 'transition': {'duration': 300, 'easing': 'quadratic-in-out'}}],
                'label': 'Play',
                'method': 'animate'
            },
            {
                'args': [[None], {'frame': {'duration': 0, 'redraw': False}, 'mode': 'immediate',
                'transition': {'duration': 0}}],
                'label': 'Pause',
                'method': 'animate'
            }
        ],
        'direction': 'left',
        'pad': {'r': 10, 't': 87},
        'showactive': False,
        'type': 'buttons',
        'x': 0.1,
        'xanchor': 'right',
        'y': 0,
        'yanchor': 'top'
    }
]

sliders_dict = {
    'active': 0,
    'yanchor': 'top',
    'xanchor': 'left',
    'currentvalue': {
        'font': {'size': 20},
        'prefix': 'Year:',
        'visible': True,
        'xanchor': 'right'
    },
    'transition': {'duration': 300, 'easing': 'cubic-in-out'},
    'pad': {'b': 10, 't': 50},
    'len': 0.9,
    'x': 0.1,
    'y': 0,
    'steps': []
}

# make data
years = 1952
for continent in continents:
    dataset_by_year = final_data[final_data['year'] == year]
    dataset_by_year_and_cont = dataset_by_year[dataset_by_year['continent'] == continent]

    data_dict = {
        'x': list(dataset_by_year_and_cont['lifeExp']),
        'y': list(dataset_by_year_and_cont['gdpPercap']),
        'mode': 'markers',
        'text': list(dataset_by_year_and_cont['country']),
        'marker': {
            'sizemode': 'area',
            'sizeref': 200000,
            'size': list(dataset_by_year_and_cont['pop'])
        },
        'name': continent
    }
    figure['data'].append(data_dict)
    
# make frames
for year in year_list:
    frame = {'data': [], 'name': str(year)}
    for continent in continents:
        dataset_by_year = final_data[final_data['year'] == int(year)]
        dataset_by_year_and_cont = dataset_by_year[dataset_by_year['continent'] == continent]

        data_dict = {
            'x': list(dataset_by_year_and_cont['lifeExp']),
            'y': list(dataset_by_year_and_cont['gdpPercap']),
            'mode': 'markers',
            'text': list(dataset_by_year_and_cont['country']),
            'marker': {
                'sizemode': 'area',
                'sizeref': 200000,
                'size': list(dataset_by_year_and_cont['pop'])
            },
            'name': continent
        }
        frame['data'].append(data_dict)

    figure['frames'].append(frame)
    slider_step = {'args': [
        [year],
        {'frame': {'duration': 300, 'redraw': False},
         'mode': 'immediate',
       'transition': {'duration': 300}}
     ],
     'label': year,
     'method': 'animate'}
    sliders_dict['steps'].append(slider_step)

    
figure['layout']['sliders'] = [sliders_dict]

plot(figure)