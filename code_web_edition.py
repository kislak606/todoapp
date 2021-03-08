import json
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import datetime

dbfile = "C:\\Users\\vlaks\\Downloads\\Parking Lot Project\\web apps\\tasks.json"
f = open(dbfile,"a")
f.flush()
f = open(dbfile,"a")
now = datetime.datetime.now()
nowstr = now.strftime("%m/%d/%Y %H:%M:%S");
parkingLot = [0] * 10 
reservedParkingSlots = []
reservedParkingSlotsLicensePlateNumber = {}
FreeParkingSlotsLicensePlateNumber = [0] * 10
global rows
global cols
rows, cols = (10, 5) 
slots=[ ([""] * cols) for row in range(rows) ]
number_of_transactions = []
money_made = 0
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

def add_slot_details(name, date):
    d = {
        "name": name,
        "date": date.strftime("%Y/%m/%d")
    }
    with open(dbfile, "a") as f:
        json.dump(d, f)
        f.write("\n")

def Reserve_slot():
    global z
    global y
    global n
    global FreeSlots
    global money_made
    global f
    global string_money_made
    z = int(st.selectbox("which slot do you want to reserve?", list(FreeSlots.keys())))
    z=z-1
    if parkingLot[z] == 0:
        parkingLot[z] = 1
        y = st.text_input("what is your license plate number? ")
        n = st.text_input("what is the name of your car? ")
        reservedParkingSlots.append(parkingLot[z])
        reservedParkingSlotsLicensePlateNumber.update({z : y})
        string_money_made = str(money_made)
        slots[z][0] = y
        slots[z][1] = n
        slots[z][2] = money_made
        slots[z][3] = "reserve"
        slots[z][4] = z
        print(slots)
        if st.button('Enter'):
            data = {
            "time" : nowstr,
            "slot" : z,
            "action" : "reserve",
            "license_plate_number" : y,
            "car_name" : n,
            "cost" : 0
        }
            with open(dbfile, "a") as outfile:
                json.dump(data, outfile)
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
    else:
        z = st.text_input("The slot you have chosen is occupied at the moment, please enter a different parking slot. ")
        y = st.text_input("what is your license plate number? ")
        if parkingLot[int(z)] == 0:
            parkingLot[int(z)] = 1
            reservedParkingSlots.append(parkingLot[int(z)])
            reservedParkingSlotsLicensePlateNumber.update({z : y})
            del FreeSlots[z]
        slots[z][0] = y
        slots[z][1] = n
        slots[z][2] = money_made
        slots[z][3] = "reserve"
        slots[z][4] = z

        if st.button('Enter'):
            data = {
            "time" : nowstr,
            "slot" : z,
            "action" : "reserve",
            "license_plate_number" : y,
            "car_name" : n,
            "cost" : 0
        }
            with open(dbfile, "a") as outfile:
                json.dump(data, outfile)
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

def Free_slot():
    global FreeSlots
    global money_made
    global string_money_made
    global revenue

    z = int(input("What is the parking slot number? "))
    z=z-1
    if parkingLot[z] == 1:
        parkingLot[z] = 0
        del reservedParkingSlots[parkingLot[z]]
        del reservedParkingSlotsLicensePlateNumber[z]
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
            data = {
            "time" : nowstr,
            "slot" : z,
            "action" : "free",
            "license_plate_number" : y,
            "car_name" : n,
            "cost" : 10
            }
            with open(dbfile, "a") as outfile:
                json.dump(data, outfile)
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


def revenue_made():
    infile = open(dbfile, 'r')
    revenue = 0
    try :
        for line in infile :
            json_data = json.loads(line)
            revenue = json_data['cost']
    except :
       print("No DATA ...")
       revenue = 0
    st.write(revenue)


def List():
    global FreeSlots
    slots = len(FreeParkingSlotsLicensePlateNumber)
    slotsstr = str(slots)
    print("There are " + slotsstr + " slots available")
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
    Reserve_slot()
elif choice == 'free':
    Free_slot()
elif choice == 'revenue made':
    revenue_made()
elif choice == 'list':
    List()
elif choice == 'slot popularity graph':
    graph_maker()
elif choice == 'slot occupancy graph':
    slot_graph()

