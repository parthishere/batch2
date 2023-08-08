import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("UN_Migrations.csv", low_memory=False)
data = data.fillna(0)
data = data.replace([".."], 0)
data = data.values.tolist()
areas = []
labels = data[0]


graph_data = {
    "geographic_region": ["Africa", "Asia", "Europe", "Latin_america", "North_America", "Ocenia"],
    1990: {
        "world": None,
        "top_5_region": [],
        "top_5_regions_values": [],


        "less_developed_region_total": None,
        "less_developed_region_names": [],
        "less_developed_region_values": [],

        "more_developed_region_total": None,
        "more_developed_region_names": [],
        "more_developed_region_values": [],

        "least_developed_region_total": None,
        "least_developed_region_names": [],
        "least_developed_region_values": [],


        "high_income_region_total": None,
        "high_income_region_names": [],
        "high_income_region_values": [],

        "middle_income_region_total": None,
        "middle_income_region_names": [],
        "middle_income_region_values": [],

        "low_income_region_total": None,
        "low_income_region_names": [],
        "low_income_region_values": [],

        "no_income_region_total": None,
        "no_income_region_names": [],
        "no_income_region_values": [],

        "Africa": {
            "total": None,
            "top_5_regions": [],
            "top_5_regions_values": [],
        },
        "Asia": {
            "total": None,
            "top_5_regions": [],
            "top_5_regions_values": [],
        },
        "Europe": {
            "total": None,
            "top_5_regions": [],
            "top_5_regions_values": [],
        },
        "Latin_america": {
            "total": None,
            "top_5_regions": [],
            "top_5_regions_values": [],
        },
        "North_America": {
            "total": None,
            "top_5_regions": [],
            "top_5_regions_values": [],
        },
        "Ocenia": {
            "total": None,
            "top_5_regions": [],
            "top_5_regions_values": [],
        },

    },


    1995: {
        "world": None,
        "top_5_regions": [],
        "top_5_regions_values": [],


        "less_developed_region_total": None,
        "less_developed_region_names": [],
        "less_developed_region_values": [],

        "more_developed_region_total": None,
        "more_developed_region_names": [],
        "more_developed_region_values": [],

        "least_developed_region_total": None,
        "least_developed_region_names": [],
        "least_developed_region_values": [],


        "high_income_region_total": None,
        "high_income_region_names": [],
        "high_income_region_values": [],

        "middle_income_region_total": None,
        "middle_income_region_names": [],
        "middle_income_region_values": [],

        "low_income_region_total": None,
        "low_income_region_names": [],
        "low_income_region_values": [],

        "no_income_region_total": None,
        "no_income_region_names": [],
        "no_income_region_values": [],

        "Africa": {
            "total": None,
            "top_5_regions": [],
            "top_5_regions_values": [],
        },
        "Asia": {
            "total": None,
            "top_5_regions": [],
            "top_5_regions_values": [],
        },
        "Europe": {
            "total": None,
            "top_5_regions": [],
            "top_5_regions_values": [],
        },
        "Latin_america": {
            "total": None,
            "top_5_regions": [],
            "top_5_regions_values": [],
        },
        "North_America": {
            "total": None,
            "top_5_regions": [],
            "top_5_regions_values": [],
        },
        "Ocenia": {
            "total": None,
            "top_5_regions": [],
            "top_5_regions_values": [],
        },

    },



    2000: {
        "world": None,
        "top_5_regions": [],
        "top_5_regions_values": [],


        "less_developed_region_total": None,
        "less_developed_region_names": [],
        "less_developed_region_values": [],

        "more_developed_region_total": None,
        "more_developed_region_names": [],
        "more_developed_region_values": [],

        "least_developed_region_total": None,
        "least_developed_region_names": [],
        "least_developed_region_values": [],


        "high_income_region_total": None,
        "high_income_region_names": [],
        "high_income_region_values": [],

        "middle_income_region_total": None,
        "middle_income_region_names": [],
        "middle_income_region_values": [],

        "low_income_region_total": None,
        "low_income_region_names": [],
        "low_income_region_values": [],

        "no_income_region_total": None,
        "no_income_region_names": [],
        "no_income_region_values": [],

        "Africa": {
            "total": None,
            "top_5_regions": [],
            "top_5_regions_values": [],
        },
        "Asia": {
            "total": None,
            "top_5_regions": [],
            "top_5_regions_values": [],
        },
        "Europe": {
            "total": None,
            "top_5_regions": [],
            "top_5_regions_values": [],
        },
        "Latin_america": {
            "total": None,
            "top_5_regions": [],
            "top_5_regions_values": [],
        },
        "North_America": {
            "total": None,
            "top_5_regions": [],
            "top_5_regions_values": [],
        },
        "Ocenia": {
            "total": None,
            "top_5_regions": [],
            "top_5_regions_values": [],
        },

    },



    2005: {
        "world": None,
        "top_5_regions": [],
        "top_5_regions_values": [],


        "less_developed_region_total": None,
        "less_developed_region_names": [],
        "less_developed_region_values": [],

        "more_developed_region_total": None,
        "more_developed_region_names": [],
        "more_developed_region_values": [],

        "least_developed_region_total": None,
        "least_developed_region_names": [],
        "least_developed_region_values": [],


        "high_income_region_total": None,
        "high_income_region_names": [],
        "high_income_region_values": [],

        "middle_income_region_total": None,
        "middle_income_region_names": [],
        "middle_income_region_values": [],

        "low_income_region_total": None,
        "low_income_region_names": [],
        "low_income_region_values": [],

        "no_income_region_total": None,
        "no_income_region_names": [],
        "no_income_region_values": [],

        "Africa": {
            "total": None,
            "top_5_regions": [],
            "top_5_regions_values": [],
        },
        "Asia": {
            "total": None,
            "top_5_regions": [],
            "top_5_regions_values": [],
        },
        "Europe": {
            "total": None,
            "top_5_regions": [],
            "top_5_regions_values": [],
        },
        "Latin_america": {
            "total": None,
            "top_5_regions": [],
            "top_5_regions_values": [],
        },
        "North_America": {
            "total": None,
            "top_5_regions": [],
            "top_5_regions_values": [],
        },
        "Ocenia": {
            "total": None,
            "top_5_regions": [],
            "top_5_regions_values": [],
        },

    },




    2010: {
        "world": None,
        "top_5_regions": [],
        "top_5_regions_values": [],


        "less_developed_region_total": None,
        "less_developed_region_names": [],
        "less_developed_region_values": [],

        "more_developed_region_total": None,
        "more_developed_region_names": [],
        "more_developed_region_values": [],

        "least_developed_region_total": None,
        "least_developed_region_names": [],
        "least_developed_region_values": [],


        "high_income_region_total": None,
        "high_income_region_names": [],
        "high_income_region_values": [],

        "middle_income_region_total": None,
        "middle_income_region_names": [],
        "middle_income_region_values": [],

        "low_income_region_total": None,
        "low_income_region_names": [],
        "low_income_region_values": [],

        "no_income_region_total": None,
        "no_income_region_names": [],
        "no_income_region_values": [],
        "Africa": {
            "total": None,
            "top_5_regions": [],
            "top_5_regions_values": [],
        },
        "Asia": {
            "total": None,
            "top_5_regions": [],
            "top_5_regions_values": [],
        },
        "Europe": {
            "total": None,
            "top_5_regions": [],
            "top_5_regions_values": [],
        },
        "Latin_america": {
            "total": None,
            "top_5_regions": [],
            "top_5_regions_values": [],
        },
        "North_America": {
            "total": None,
            "top_5_regions": [],
            "top_5_regions_values": [],
        },
        "Ocenia": {
            "total": None,
            "top_5_regions": [],
            "top_5_regions_values": [],
        },

    }
}

data_2000 = []
data_1990 = []
data_1995 = []
data_2005 = []
data_2010 = []
f_data = []
for row in data:
    year = row[0]
    if year == 2010:
        data_2010.append(row)
    if year == 2005:
        data_2005.append(row)
    if year == 1995:
        data_1995.append(row)
    if year == 2000:
        data_2000.append(row)
    if year == 1990:
        data_1990.append(row)

f_data.append(data_1990)
f_data.append(data_1995)
f_data.append(data_2000)
f_data.append(data_2005)
f_data.append(data_2010)


for i, year_data in enumerate(f_data):
    for j, sub_row in enumerate(year_data):
        f_sub_row = []
        year = int(sub_row[0])
        sub_row[2] = 0

        for element in sub_row:
            try:
                if isinstance(element, str):
                    try:
                        f_sub_row.append(int(element.replace(",", "").strip()))
                    except Exception as e:

                        f_sub_row.append(0)
                else:
                    f_sub_row.append(int(element))
            except Exception as e:
                print(e)
                pass

        if j == 0:
            # World
            graph_data[year]["world"] = f_sub_row[6]
            list1 = f_sub_row[7:]
            list2 = labels[7:]
            top_5_region_values, top_5_region_names = zip(
                *sorted(zip(list1, list2), key=lambda x: x[0], reverse=True))
            top_5_region_values = top_5_region_values[0:5]
            top_5_region_names = top_5_region_names[0:5]

            graph_data[year]["top_5_region"] = top_5_region_names
            graph_data[year]["top_5_regions_values"] = top_5_region_values

            print(top_5_region_values, top_5_region_names)

        elif j == 2:
            # more develop
            graph_data[year]["more_developed_region_total"] = f_sub_row[6]
            list1 = f_sub_row[7:]
            list2 = labels[7:]
            more_developed_region_values, more_developed_region_names = zip(
                *sorted(zip(list1, list2), key=lambda x: x[0], reverse=True))
            more_developed_region_values = more_developed_region_values[0:5]
            more_developed_region_names = more_developed_region_names[0:5]

            graph_data[year]["more_developed_region_values"] = more_developed_region_values
            graph_data[year]["more_developed_region_names"] = more_developed_region_names
        elif j == 3:
            # less develop
            graph_data[year]["less_developed_region_total"] = f_sub_row[6]
            list1 = f_sub_row[7:]
            list2 = labels[7:]
            less_developed_region_values, less_developed_region_names = zip(
                *sorted(zip(list1, list2), key=lambda x: x[0], reverse=True))
            less_developed_region_values = less_developed_region_values[0:5]
            less_developed_region_names = less_developed_region_names[0:5]

            graph_data[year]["less_developed_region_values"] = less_developed_region_values
            graph_data[year]["less_developed_region_names"] = less_developed_region_names
        elif j == 4:
            # least develop
            graph_data[year]["least_developed_region_total"] = f_sub_row[6]
            list1 = f_sub_row[7:]
            list2 = labels[7:]
            least_developed_region_values, least_developed_region_names = zip(
                *sorted(zip(list1, list2), key=lambda x: x[0], reverse=True))
            least_developed_region_names = least_developed_region_names[0:5]
            least_developed_region_values = least_developed_region_values[0:5]

            graph_data[year]["least_developed_region_names"] = least_developed_region_names
            graph_data[year]["least_developed_region_values"] = least_developed_region_values

        elif j == 7:
            # high income
            graph_data[year]["high_income_region_total"] = f_sub_row[6]
            list1 = f_sub_row[7:]
            list2 = labels[7:]
            high_income_region_values, high_income_region_names = zip(
                *sorted(zip(list1, list2), key=lambda x: x[0], reverse=True))
            high_income_region_names = high_income_region_names[0:5]
            high_income_region_values = high_income_region_values[0:5]

            graph_data[year]["high_income_region_names"] = high_income_region_names
            graph_data[year]["high_income_region_values"] = high_income_region_values
        elif j == 8:
            # middle income
            graph_data[year]["middle_income_region_total"] = f_sub_row[6]
            list1 = f_sub_row[7:]
            list2 = labels[7:]
            middle_income_region_values, middle_income_region_names = zip(
                *sorted(zip(list1, list2), key=lambda x: x[0], reverse=True))
            middle_income_region_names = middle_income_region_names[0:5]
            middle_income_region_values = middle_income_region_values[0:5]

            graph_data[year]["middle_income_region_names"] = middle_income_region_names
            graph_data[year]["middle_income_region_values"] = middle_income_region_values
        elif j == 11:
            # low income
            graph_data[year]["low_income_region_total"] = f_sub_row[6]
            list1 = f_sub_row[7:]
            list2 = labels[7:]
            low_income_region_values, low_income_region_names = zip(
                *sorted(zip(list1, list2), key=lambda x: x[0], reverse=True))
            low_income_region_names = low_income_region_names[0:5]
            low_income_region_values = low_income_region_values[0:5]

            graph_data[year]["low_income_region_names"] = low_income_region_names
            graph_data[year]["low_income_region_values"] = low_income_region_values
        elif j == 12:
            # no income
            graph_data[year]["no_income_region_total"] = f_sub_row[6]
            list1 = f_sub_row[7:]
            list2 = labels[7:]
            no_income_region_values, no_income_region_names = zip(
                *sorted(zip(list1, list2), key=lambda x: x[0], reverse=True))
            no_income_region_names = no_income_region_names[0:5]
            no_income_region_values = no_income_region_values[0:5]

            graph_data[year]["no_income_region_names"] = no_income_region_names
            graph_data[year]["no_income_region_values"] = no_income_region_values

        elif j == 14:
            # Africa
            graph_data[year]["Africa"]["total"] = f_sub_row[6]
            list1 = f_sub_row[7:]
            list2 = labels[7:]
            top_5_regions, top_5_regions_values = zip(
                *sorted(zip(list1, list2), key=lambda x: x[0], reverse=True))
            top_5_regions = top_5_regions[0:5]
            top_5_regions_values = top_5_regions_values[0:5]

            graph_data[year]["Africa"]["top_5_regions"] = top_5_regions
            graph_data[year]["Africa"]["top_5_regions_values"] = top_5_regions_values
        elif j == 15:
            # Asia
            graph_data[year]["Asia"]["total"] = f_sub_row[6]
            list1 = f_sub_row[7:]
            list2 = labels[7:]
            top_5_regions, top_5_regions_values = zip(
                *sorted(zip(list1, list2), key=lambda x: x[0], reverse=True))
            top_5_regions = top_5_regions[0:5]
            top_5_regions_values = top_5_regions_values[0:5]

            graph_data[year]["Asia"]["top_5_regions"] = top_5_regions
            graph_data[year]["Asia"]["top_5_regions_values"] = top_5_regions_values
        elif j == 16:
            # Europe
            graph_data[year]["Europe"]["total"] = f_sub_row[6]
            list1 = f_sub_row[7:]
            list2 = labels[7:]
            top_5_regions, top_5_regions_values = zip(
                *sorted(zip(list1, list2), key=lambda x: x[0], reverse=True))
            top_5_regions = top_5_regions[0:5]
            top_5_regions_values = top_5_regions_values[0:5]

            graph_data[year]["Europe"]["top_5_regions"] = top_5_regions
            graph_data[year]["Europe"]["top_5_regions_values"] = top_5_regions_values
        elif j == 17:
            # Latin_america
            graph_data[year]["Latin_america"]["total"] = f_sub_row[6]
            list1 = f_sub_row[7:]
            list2 = labels[7:]
            top_5_regions, top_5_regions_values = zip(
                *sorted(zip(list1, list2), key=lambda x: x[0], reverse=True))
            top_5_regions = top_5_regions[0:5]
            top_5_regions_values = top_5_regions_values[0:5]

            graph_data[year]["Latin_america"]["top_5_regions"] = top_5_regions
            graph_data[year]["Latin_america"]["top_5_regions_values"] = top_5_regions_values
        elif j == 18:
            # Ocenia
            graph_data[year]["Ocenia"]["total"] = f_sub_row[6]
            list1 = f_sub_row[7:]
            list2 = labels[7:]
            top_5_regions, top_5_regions_values = zip(
                *sorted(zip(list1, list2), key=lambda x: x[0], reverse=True))
            top_5_regions = top_5_regions[0:5]
            top_5_regions_values = top_5_regions_values[0:5]

            graph_data[year]["Ocenia"]["top_5_regions"] = top_5_regions
            graph_data[year]["Ocenia"]["top_5_regions_values"] = top_5_regions_values

        region_of_africa = ["Eastern Africa", "Middle Africa",
                            "Southern Africa", "Westarn Africa", "Northen Africa"]
        region_of_asia = ["Western Asia", "Central Asia",
                          "Southern Asia", "Eastern Asia", "South-Eastern Asia"]
        america = ["Caribbean", "Central America",
                   "South America", "NORTHERN AMERICA"]
        oceania = ["Australia/New Zealand",
                   "Malesia", "Micronesia", "Polynesia"]
        europe = ["Eastern Europe", "Northern Europe", "Western Europe", ]

        if j in range(14, len(f_sub_row)):
            pass
