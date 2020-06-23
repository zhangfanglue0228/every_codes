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

fig = px.scatter(final_data, x="lifeExp", y="gdpPercap", animation_frame="year",
                 animation_group="country",size="gdpPercap", color="continent",
                 hover_name="country",log_x=True, size_max=45)
plot(fig)
