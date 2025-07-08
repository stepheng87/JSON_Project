import json

infile = open(r'C:\Users\Stephen_Gonzales1\Documents\AdvPython\JSON_Project\eq_data_30_day_m1.json','r')

outfile = open(r'C:\Users\Stephen_Gonzales1\Documents\AdvPython\JSON_Project\readable_eq_data.json','w')

eq_data = json.load(infile)

print(type(eq_data))

json.dump(eq_data, outfile, indent=4)

list_of_eqs =  eq_data['features']

print(len(list_of_eqs))

mags, lons, lats, hover_texts = [], [], [], []

for eq in list_of_eqs:
    mag = eq['properties']['mag']
    lon = eq['geometry']['coordinates'][0]
    lat = eq['geometry']['coordinates'][1]
    hover_text = eq['properties']['place']

    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(hover_text)

print(mags[:5])
print(lons[:5])
print(lats[:5])

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

#data = [Scattergeo(lon=lons,lat=lats)]
data = [{
    'type':'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker':{
        'size':[5*mag for mag in mags],
        'color':mags,
        'colorscale': 'Viridis',
        'reversescale':True,
        'colorbar':{'title':'Magnitude'}
    }
}]

my_layout = Layout(title='Global Earthquakes 30 days')

fig = {'data':data,'layout':my_layout}

offline.plot(fig,filename='global_earthquakes_1_dat.html')

