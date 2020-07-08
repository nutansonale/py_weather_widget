from tkinter import *
import json
import requests


def weatherdata():
    url_api="http://api.openweathermap.org/data/2.5/forecast?id=1254089&mode=json&appid=88dab273e4a0c83a9f90bbe1601a13b1"

    response = requests.get(url_api)
    
        
    data=json.loads(response.content.decode('utf-8'))
    main_data=data.get('list')

    #weather data
    main_rain=main_data[1].get('weather')[0].get('main')
    description=main_data[1].get('weather')[0].get('description')

    #temperature data
    temp=main_data[1].get('main').get('temp')
    humid=main_data[1].get('main').get('humidity')

    #wind speed
    wind=main_data[1].get('wind').get('speed')
    wind_direct=main_data[1].get('wind').get('deg')

    for i in range(1):
        #weather data
        main_rain=main_data[i].get('weather')[0].get('main')
        description=main_data[i].get('weather')[0].get('description')

        #temperature data
        temp=main_data[i].get('main').get('temp')
        humid=main_data[i].get('main').get('humidity')

        #wind speed
        wind=main_data[i].get('wind').get('speed')
        wind_direct=main_data[i].get('wind').get('deg')
    
        #date
        date=main_data[i].get('dt_txt')
    
        #print("\nfor date ",date," temperature will be ",temp-273.15,"celsius with humidity of ",humid,"% \nwind speed will be ",wind,"m/s in direction of ",wind_direct,"\n with chance of ",description)
        data="\nhumidity of "+str(humid)+"% \nwind speed "+str(wind)+"m/s "+"\nwith chance of "+str(description)
    
    return(data,f'{temp-273.15:.2f}',str(date))  


root = Tk()
root.wait_visibility(root)
root.wm_attributes('-alpha',0.5)
root.wm_attributes("-topmost",False)
root.wm_attributes('-type', 'splash')

x=0
y=root.winfo_screenheight()
root.geometry('%dx%d+%d+%d' % (200, 300, x, y))
lab=Label(root, text="hello nutan!",fg='blue',font=("Helvetica", 16))
lab.grid(column=2,row=0)

data,temp,date=weatherdata()
lab0=Label(root,text=date,fg='blue')
lab1=Label(root,text=temp+"\u2103",fg='blue',font=("Helvetica", 30))
lab2=Label(root, text=data,fg='blue')
lab0.grid(column=2,row=1)
lab1.grid(column=2,row=2)
lab2.grid(column=2,row=3)
root.mainloop()

