import json

infile = open(r'C:\Users\Stephen_Gonzales1\Documents\AdvPython\JSON_Project\schools.geojson','r')

outfile = open(r'C:\Users\Stephen_Gonzales1\Documents\AdvPython\JSON_Project\readable_school_data.json','w')

infile2 = open(r'C:\Users\Stephen_Gonzales1\Documents\AdvPython\JSON_Project\univ.json','r')

outfile2 = open(r'C:\Users\Stephen_Gonzales1\Documents\AdvPython\JSON_Project\readable_school_data1.json','w')

school_data = json.load(infile)

school_data2 = json.load(infile2)

json.dump(school_data, outfile, indent=4)

json.dump(school_data2, outfile2, indent=4) 

list_of_schools =  school_data['features']

school_data_mod = {school['instnm']: int(school['Total  enrollment (DRVEF2020)']) for school in school_data2}


