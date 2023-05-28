# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# import plotly.offline as pyo
# import plotly.graph_objs as go
# import plotly.express as px
# #import sort_dataframeby_monthorweek as sd

# #read csv file using read_csv

# df=pd.read_csv("hotel_bookings.csv")
# # print(df.head())
# # print(df.shape)
# # pd.set_option("display.max_columns",32)
# # print(df.head())
# # print(df.columns)
# # print(df.nunique())
#print(df['hotel'].value_counts())
# # print(df["meal"].value_counts())
# # print(df["country"].value_counts())
# # print(df["market_segment"].value_counts())
#print(df['distribution_channel'].value_counts())
# # sns.countplot(data=df,x="market_segment")
# # sns.countplot(data=df,x="market_segment",hue="meal")
# # plt.show()


# # #data preparation

# # print(df.isnull().values.any())
# # print(df.isnull().sum())
# # df.fillna(0,inplace=True)
# # print(df.isnull().sum())
# # print(df['meal'].unique())
# # df["meal"].replace("Undefined","SC",inplace=True)
# # print(df['meal'].unique())
# # Subset=df[(df['children']==0)&(df['adults']==0)&(df['babies']==0)]
# # print(Subset[['adults','babies','children']])
# # print(type(Subset))


# delete=(df['children']==0)&(df['adults']==0)&(df['babies']==0)
# # # print(type(delete))
# # # print(delete)
# data=df[~delete]
# # print(data.head())
# # print(data.shape)
# # Subset=data[(data['children']==0)&(data['adults']==0)&(data['babies']==0)]
# # print(Subset)
#data.to_csv('Updataed_Hotel_Booking.csv', index=False)
#

# # guest_country=data[data['is_canceled']==0]['country'].value_counts().reset_index()

# # guest_country.columns=['country', 'Number of Guests']
# # print(guest_country.columns)


# # guest_country=data[data['is_canceled']==0]['country'].value_counts().reset_index()
# # print(guest_country)

# # total_guests=guest_country["Number of guests"].sum()
# # guest_country["Guests in %"]=round(guest_country["Number of guests"]/total_guests*100,2)
# # print(guest_country)

# # total_guests = guest_country["Number of guests"].sum()
# # print(total_guests)

# # guest_country["Guests in %"] = round(guest_country["Number of guests"] / total_guests * 100, 2)
# # print(guest_country)
# # trace= go.Bar(
# #     x=guest_country["country"],
# #     y=guest_country['Number of guests'],
# #     marker=dict(color='#CD7F32') 
# # )
# # data1 = [ trace]
# # layout = go.Layout(
# #     title='Guests by Country'
# # )
# # fig = go.Figure(data=data1, layout=layout)
# # pyo.plot(fig)
# # map_guest = px.choropleth(guest_country,
# #                     locations=guest_country['country'],
# #                     color=guest_country['Number of guests'], 
# #                     hover_name=guest_country['country'], 
# #                     title="Home country of guests")
# # map_guest.show()

# resort = data[(data["hotel"] == "Resort Hotel") & (data["is_canceled"] == 0)]
# # print(resort)
# city = data[(data["hotel"] == "City Hotel") & (data["is_canceled"] == 0)]
# # print(city)

# # resort_hotel=resort.groupby(['arrival_date_month'])['adr'].mean().reset_index()
# # print(resort_hotel)

# # city_hotel=city.groupby(['arrival_date_month'])['adr'].mean().reset_index()
# # print(city_hotel)
# final=resort_hotel.merge(city_hotel,on='arrival_date_month')
# final.columns=['month','price_for_resort','price_for_city_hotel']
# print(final)
# final=sd.Sort_Dataframeby_Month(df=final,monthcolumnname='month')
# final
# # px.line(final, x='month',
# #         y=['price_for_resort','price_for_city_hotel'],
# #         title='Room price per night over the Months')
# data["adr_Updated"]=data["adr"]/(data["adults"]+data["children"])
# resort = data[(data["hotel"] == "Resort Hotel") & (data["is_canceled"] == 0)]
# city = data[(data["hotel"] == "City Hotel") & (data["is_canceled"] == 0)]

# resort_hotel=resort.groupby(['arrival_date_month'])['adr_Updated'].mean().reset_index()
# print(resort_hotel)
# city_hotel=city.groupby(['arrival_date_month'])['adr_Updated'].mean().reset_index()
# print(city_hotel)

# final=resort_hotel.merge(city_hotel,on='arrival_date_month')
# final.columns=['month','price_for_resort','price_for_city_hotel']
# print(final)
# final=sd.Sort_Dataframeby_Month(df=final,monthcolumnname='month')
# final

# px.line(final, x='month',
#         y=['price_for_resort','price_for_city_hotel'], 
#         title='Room price per night over the Months')

# #Summer in Portugal sits between June and mid-September 
# #while the winter season falls between December 

# df['reserved_room_type'].unique()
# data["adr_Updated"]=data["adr"]/(data["adults"]+data["children"])
# print(data)
# data["adr_Updated"]=data["adr"]/(data["adults"]+data["children"])
# valid_guest= data.loc[data["is_canceled"] == 0]
# prices = valid_guest[["hotel", "reserved_room_type", "adr_Updated"]].sort_values("reserved_room_type")

# # plt.figure(figsize=(12, 8))
# # sns.boxplot(x="reserved_room_type",
# #             y="adr_Updated",
# #             hue="hotel",
# #             data=prices
# #            )
# # plt.title("Price of room types per night and person", fontsize=16)
# # plt.xlabel("Room type", fontsize=16)
# # plt.ylabel("Price [EUR]", fontsize=16)

# # plt.ylim(0, 160)
# # plt.show()

# prices_C=prices[prices['reserved_room_type']=='C']
# print(prices_C)
# prices_City=prices_C[prices_C['hotel']=='City Hotel']
# prices_Resort=prices_C[prices_C['hotel']=='Resort Hotel']
# print(prices_Resort)
# print(prices_City)
# print(prices_Resort.describe())


# df3=data[data['is_canceled']==0]
# df3["total_nights"] = df3["stays_in_weekend_nights"] + df3["stays_in_week_nights"]

# print(df3)


# df4=df3[['total_nights','hotel','is_canceled']]
# print(df4)


# hotel_stay=df4.groupby(['total_nights','hotel']).agg('count').reset_index()

# print(hotel_stay)

# hotel_stay=hotel_stay.rename(columns={'is_canceled':'Number of stays'})
# print(hotel_stay.head())


# hotel_stay_r=hotel_stay[hotel_stay['hotel']=='Resort Hotel']
# print(hotel_stay_r)

# hotel_stay_c=hotel_stay[hotel_stay['hotel']=='City Hotel']
# print(hotel_stay_c)



# # trace = go.Bar(
# #     x=hotel_stay_r["total_nights"],
# #     y=hotel_stay_r["Number of stays"],
# #     name='Resort Stay'
# #     )

# # trace1=go.Bar(
# #     x=hotel_stay_c["total_nights"],
# #     y=hotel_stay_c["Number of stays"],
# #     name='City stay'
# #     )


# # data5 = [trace,trace1]
# # layout = go.Layout(
# #     title='Total Number of stays by Guest'
# # )
# # fig = go.Figure(data=data5, layout=layout)
# # pyo.plot(fig)


# segments=data["market_segment"].value_counts()
# print(segments)

# segments=data["market_segment"].value_counts()

# # pie plot
# # fig = px.pie(segments,
# #              values=segments.values,
# #              names=segments.index,
# #              title="Bookings per market segment",
# #              template="gridon"
# #              )
# # fig.update_traces(rotation=-90, textinfo="percent+label")
# # fig.show()

# # plt.figure(figsize=(12, 8))
# # sns.barplot(x="market_segment",
# #             y="adr_Updated",
# #             hue="reserved_room_type",
# #             data=data,
# #             ci=None)
# # plt.title("ADR by market segment and room type", fontsize=16)
# # plt.xlabel("Market segment", fontsize=16)
# # plt.xticks(rotation=45)
# # plt.ylabel("ADR per person [EUR]", fontsize=16)
# # plt.legend(loc="upper left")
# # plt.show()


# Cancel=data['is_canceled']==1
# cancel=Cancel.sum()
# resort_cancelation = data.loc[data["hotel"] == "Resort Hotel"]["is_canceled"].sum()
# city_cancelation = data.loc[data["hotel"] == "City Hotel"]["is_canceled"].sum()
# print(resort_cancelation)
# print(city_cancelation)

# print(f"Total Booking Cancelled : {cancel} . ")
# print(f"Total Resort Hotel Booking Cancelled : {resort_cancelation} . ")
# print(f"Total City Hotel Booking Cancelled : {city_cancelation} . ")


# #which month have highest cancellation


# res_book_per_month = data.loc[(data["hotel"] == "Resort Hotel")].groupby("arrival_date_month")["hotel"].count()
# res_cancel_per_month = data.loc[(data["hotel"] == "Resort Hotel")].groupby("arrival_date_month")["is_canceled"].sum()

# cty_book_per_month = data.loc[(data["hotel"] == "City Hotel")].groupby("arrival_date_month")["hotel"].count()
# cty_cancel_per_month = data.loc[(data["hotel"] == "City Hotel")].groupby("arrival_date_month")["is_canceled"].sum()

# res_cancel_data = pd.DataFrame({"Hotel": "Resort Hotel",
#                                 "Month": list(res_book_per_month.index),
#                                 "Bookings": list(res_book_per_month.values),
#                                 "Cancelations": list(res_cancel_per_month.values)})
# cty_cancel_data = pd.DataFrame({"Hotel": "City Hotel",
#                                 "Month": list(cty_book_per_month.index),
#                                 "Bookings": list(cty_book_per_month.values),
#                                 "Cancelations": list(cty_cancel_per_month.values)})



# print(res_cancel_data)


# # import sort_dataframeby_monthorweek as sd
# # res_cancel_data=sd.Sort_Dataframeby_Month(df=res_cancel_data,monthcolumnname='Month')
# # print(res_cancel_data)
# # cty_cancel_data=sd.Sort_Dataframeby_Month(df=cty_cancel_data,monthcolumnname='Month')
# # print(cty_cancel_data)



# plt.figure(figsize=(12, 8))

# trace = go.Bar(
#     x=res_cancel_data["Month"],
#     y=res_cancel_data["Cancelations"],
#     name="Rst Cancelled"
#     )
# trace1 = go.Bar(
#     x=cty_cancel_data["Month"],
#     y=cty_cancel_data["Cancelations"],
#     name="Cty Cancelled"
#     )


# data6 = [trace,trace1]
# layout = go.Layout(
#     title='Total Number of stays by Guest'
# )
# fig = go.Figure(data=data6, layout=layout)
# pyo.plot(fig)