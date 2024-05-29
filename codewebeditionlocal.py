import json
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import datetime
import requests
import urllib.parse as urlparse

api_key = "289272e0-7929-418c-9e40-7163dc15cfe2"
headers = {"Api-Key": api_key, "Content-Type": "application/json"}
store_name = "parkingLotProject"
init_store = "init_var"
store_url = f"https://json.psty.io/api_v1/stores/{store_name}"
init_url = f"https://json.psty.io/api_v1/stores/{init_store}"

dbfile = "C:\\Users\\vlaks\\Downloads\\Parking Lot Project\\web apps\\tasks.json"
f = open(dbfile,"a")
f.flush()
f = open(dbfile,"a")
now = datetime.datetime.now()
nowstr = now.strftime("%m/%d/%Y %H:%M:%S");

# def init_data():
#     res = requests.get(init_url, headers=headers)
#     idata = res.json()["data"]
#     return idata

# initialization_count = 0

# res = requests.get(init_url, headers=headers)

# i = {
#      "init" : "one",
#      "first": True
#     }
# data = init_data()
# data.append(i)

# res = requests.put(init_url, headers=headers, data=json.dumps(data))


#if (data.length() <= 1):  
parkingLot = [0] * 10 
    #reservedParkingSlots = []
    #reservedParkingSlotsLicensePlateNumber = {}
FreeParkingSlotsLicensePlateNumber = [0] * 10
global rows
global cols
rows, cols = (10, 5) 
slots=[ ([""] * cols) for row in range(rows) ]
number_of_transactions = []
money_made = 0
print(" initial slots: ")
print(slots) 
FreeSlots = {
    1 : "free",
    2 : "free",
    3 : "free",
    4 : "free",
    5 : "free",
    6 : "free",
    7 : "free",
    8 : "free",
    9 : "free",
    10 : "free"
    }
    #initialization_count += 1



def Reserve_slot():
    global z
    global y
    global n
    global FreeSlots
    global money_made
    global f
    global string_money_made
    global parkingLot

    #parkingLot = save_information()
    z = int(st.selectbox("which slot do you want to reserve?", list(FreeSlots.keys())))
    z=z-1
    if parkingLot[z] == 0:
        parkingLot[z] = 1
        inputy = st.empty()
        inputn = st.empty()
        y = inputy.text_input("what is your license plate number? ", key = 3)
        n = inputn.text_input("what is the name of your car? ", key = 2)
        #reservedParkingSlots.append(parkingLot[z])
        #reservedParkingSlotsLicensePlateNumber.update({z : y})
        #string_money_made = str(money_made)
        slots[z][0] = y
        slots[z][1] = n
        slots[z][2] = money_made
        slots[z][3] = "reserve"
        slots[z][4] = z
        print(" Reserve slots: ")
        print(slots)
        if st.button('Enter'):
            d = {
            "time" : nowstr,
            "slot" : z,
            "action" : "reserve",
            "license_plate_number" : y,
            "car_name" : n,
            "cost" : 0
            }
            inputy.text_input("what is your license plate number? ", value="")
            inputn.text_input("what is the name of your car? ", value="")
            #st.text_input("what is your license plate number? ", value = "", key = 1)

             # return data
             # res = requests.get(store_url, headers=headers)
             # data = res.json()["data"]
            #return data
            #return data
            with open(dbfile, "a") as outfile:
                json.dump(d, outfile)
                outfile.write("\n")
                outfile.close()
            st.json({
                "time" : nowstr,
                "slot" : z,
                "action" : "reserve",
                "license_plate_number" : y,
                "car_name" : n,
                "cost" : 10
            })
            # data = load_data()
            # data.append(d)
            # res = requests.put(store_url, headers=headers, data=json.dumps(data))
            # if parkingLot[z] == 1:
            #     print("hello")
    else:
        z = int(st.selectbox("The slot you have chosen is occupied at the moment, please enter a different parking slot. ", list(FreeSlots.keys())))
        y = st.text_input("what is your license plate number? ")
        if parkingLot[int(z)] == 0:
            parkingLot[int(z)] = 1
            #reservedParkingSlots.append(parkingLot[int(z)])
            #reservedParkingSlotsLicensePlateNumber.update({z : y})
            del FreeSlots[z]
        slots[z][0] = y
        slots[z][1] = n
        slots[z][2] = money_made
        slots[z][3] = "reserve"
        slots[z][4] = z

        if st.button('Enter'):
            d = {
            "time" : nowstr,
            "slot" : z,
            "action" : "reserve",
            "license_plate_number" : y,
            "car_name" : n,
            "cost" : 0
        }
             #  return data
             #  res = requests.get(store_url, headers=headers)
             # data = res.json()["data"]
             #  return data
            with open(dbfile, "a") as outfile:
                json.dump(d, outfile)
                outfile.write("\n")
                outfile.close()
            st.json({
                "time" : nowstr,
                "slot" : z,
                "action" : "reserve",
                "license_plate_number" : y,
                "car_name" : n,
                "cost" : 10
                })      
            # data = load_data()
            # data.append(d)
            # res = requests.put(store_url, headers=headers, data=json.dumps(data))



#def load_data():
    # now = datetime.datetime.now()
    # nowstr = now.strftime("%m/%d/%Y %H:%M:%S")
    # d = {
    #     "time" : nowstr,
    #     "slot" : z,
    #     "action" : "reserve",
    #     "license_plate_number" : y,
    #     "car_name" : n,
    #     "cost" : 10
    # }
    # res = requests.get(store_url, headers=headers)
    # if res.json():
    #     data = res.json().get("data", [])
    # else: 
    #     data = []
    # return data
    # res = requests.get(store_url, headers=headers)
    # data = res.json()["data"]
    # return data


# def save_information():
#     res = requests.get(store_url, headers=headers).json()['data']
#     parkingLot = [0,0,0,0,0,0,0,0,0,0]
#     for item in res:
#         print(item)
#         z = item["slot"]
#         if (item["action"] == "reserve"):
#             parkingLot[z-1] = 1
#         if (item["action"] == "free"):
#             parkingLot[z-1] = 0
#     return parkingLot

def Free_slot():
    global FreeSlots
    global money_made
    global string_money_made
    global revenue
    global parkingLot

    #parkingLot = save_information()
    z = int(st.selectbox("What is the parking slot number? ", list(FreeSlots.keys())))
    z=z-1
    if parkingLot[z] == 0:
        st.write("The " + str(z+1) + " slot is already free ")
        st.button('Enter')
            #do nothing
    else:
        parkingLot[z] = 0
        #del reservedParkingSlots[parkingLot[z]]
        #del reservedParkingSlotsLicensePlateNumber[z]
        FreeParkingSlotsLicensePlateNumber.append(z)
        FreeSlots.update({z : "free"})
        money_made = money_made + 10
        string_money_made = str(money_made)

        slots[z][0] = y
        slots[z][1] = n
        slots[z][2] = money_made
        slots[z][3] = "free"
        slots[z][4] = z
        if st.button('Enter'):
            d = {
            "time" : nowstr,
            "slot" : z,
            "action" : "free",
            "license_plate_number" : y,
            "car_name" : n,
            "cost" : 10
            }
            # return data
            # res = requests.get(store_url, headers=headers)
            # data = res.json()["data"]
            # return data
            with open(dbfile, "a") as outfile:
                json.dump(d, outfile)
                outfile.write("\n")
                outfile.close()   
            st.json({
                "time" : nowstr,
                "slot" : z,
                "action" : "free",
                "license_plate_number" : y,
                "car_name" : n,
                "cost" : 10
                })     
            # data = load_data()
            # data.append(d)
            # res = requests.put(store_url, headers=headers, data=json.dumps(data))

def revenue_made():
    # infile = open(dbfile, 'r')
    res = requests.get(store_url, headers=headers)
    revenue = 0
    try :
        for line in res :
            json_data = json.loads(line)
            revenue = json_data['cost']
    except :
       print("No DATA ...")
       revenue = 0
    st.write("The revenue is 10 dollars")


def List():
    global FreeSlots
    slots = len(FreeParkingSlotsLicensePlateNumber)
    slotsstr = str(slots)
    st.write("There are " + slotsstr + " slots available")
    print(FreeSlots)


def graph_val():
    global reservations
    global infile
    infile = open(dbfile, 'r')
    reservations = [0]*10
    for line in infile :
        json_val = json.loads(line)
        if json_val['action'] == "reserve":
            reservations[int(json_val['slot'])] = reservations[int(json_val['slot'])] + 1
    print (reservations)
    f = open(dbfile,"a")
def graph_maker():
    import matplotlib.pyplot as plt   
    fig, ax = plt.subplots(1, 1, figsize=(12,6))
    slots = ['1','2','3','4','5','6','7','8','9','10' ]
    colors = ['red', 'yellow', 'lightgrey', 'lightcoral','linen','yellowgreen','lightblue','lightgreen','pink','aqua'] 

    explode = [0,0,0,0,0,0,0,0,0,0]
    slot_counters = reservations
    ax.pie(slot_counters, labels = slots, colors=colors, 
            startangle=50, shadow = True, explode = explode, 
            radius = 2.0,  autopct = '%1.1f%%' ) 
    st.pyplot(fig)
infile = open(dbfile, 'r')


def slot_graph():
    global infile
    infile = open(dbfile, 'r')
    fig, ax = plt.subplots(1, 2, figsize=(12,6))
    spots = [0] * 10
    for line in infile :
        json_val = json.loads(line)
        if json_val['action'] == "reserve":
            spots[json_val['slot']] = 1
        elif json_val['action'] == "free":
            spots[json_val['slot']] = 0
    print(spots)
    plt.imshow([spots])
    st.pyplot(fig)
    #plt.show()

choice = 0

selectCount = 0

def menu():
    global choice
    global selectCount
    selectCount = selectCount+1
    choice = st.selectbox('select your option', ('choose ur option' , 'reserve', 'free', 'revenue made', 'list', 'slot popularity graph', 'slot occupancy graph'),key=selectCount)

    st.write('You selected:', choice)



#while True:
    # choice = st.selectbox('select your option', ('reserve', 'free', 'revenue made', 'list', 'slot popularity grap', 'slot occupancy graph'),key=selectCount)

    # st.write('You selected:', choice)
    # selectCount = selectCount + 1

menu()
graph_val()
if choice == 'reserve':
    #load_data()
    Reserve_slot()
elif choice == 'free':
    Free_slot()
    #load_data()
elif choice == 'revenue made':
    revenue_made()
elif choice == 'list':
    List()
elif choice == 'slot popularity graph':
    graph_maker()
elif choice == 'slot occupancy graph':
    slot_graph()


