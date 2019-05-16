from tkinter import *
import subprocess

class window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()


    # creation of init window
    def init_window(self):
        self.x = 0
        # change the title of the GUI
        self.master.title("GUI")
        # allowing the widget to take full space of the root window
        self.pack(fill=BOTH, expand=1)

        ''' Traffic Frames'''
        traffic_main = LabelFrame(self, text="VPN Traffic", width=365, height=280)
        traffic_main.config(font=("Arial", 20), labelanchor=N)
        traffic_main.place(x=20, y=20)

        traffic_txframe = LabelFrame(traffic_main, text="TX", width=120, height=210)
        traffic_txframe.config(font=("Arial", 18), labelanchor=N)
        traffic_txframe.place(x=100, y=15)

        traffic_rxframe = LabelFrame(traffic_main, text="RX", width=120, height=210)
        traffic_rxframe.config(font=("Arial", 18), labelanchor=N)
        traffic_rxframe.place(x=230, y=15)

        '''Traffic main Labels'''
        label_bytes = Label(traffic_main, text="bytes")
        label_bytes.config(font=("Arial bold", 14))
        label_bytes.place(x=10,y=50)

        label_packets = Label(traffic_main, text="packets")
        label_packets.config(font=("Arial bold", 14))
        label_packets.place(x=10,y=95)

        label_errors = Label(traffic_main, text="errors")
        label_errors.config(font=("Arial bold", 14))
        label_errors.place(x=10,y=140)

        label_dropped = Label(traffic_main, text="dropped")
        label_dropped.config(font=("Arial bold", 14))
        label_dropped.place(x=10,y=185)

        '''Traffic TX Labels'''
        self.tx_bytes = Label(traffic_txframe, text="----")
        self.tx_bytes.config(font=("Arial", 12))
        #tx_bytes.place(x=10,y=140)
        self.tx_bytes.place(relx=.5, y=20, anchor="center")

        self.tx_packets = Label(traffic_txframe, text="----")
        self.tx_packets.config(font=("Arial", 12))
        #tx_packets.place(x=10,y=140)
        self.tx_packets.place(relx=.5, y=65, anchor="center")

        self.tx_errors = Label(traffic_txframe, text="----")
        self.tx_errors.config(font=("Arial", 12))
        #tx_errors.place(x=10,y=140)
        self.tx_errors.place(relx=.5, y=110, anchor="center")

        self.tx_dropped = Label(traffic_txframe, text="----")
        self.tx_dropped.config(font=("Arial", 12))
        #tx_dropped.place(x=10,y=140)
        self.tx_dropped.place(relx=.5, y=155, anchor="center")

        '''Traffic RX Labels'''
        self.rx_bytes = Label(traffic_rxframe, text="----")
        self.rx_bytes.config(font=("Arial", 12))
        #rx_bytes.place(x=10,y=140)
        self.rx_bytes.place(relx=.5, y=20, anchor="center")

        self.rx_packets = Label(traffic_rxframe, text="----")
        self.rx_packets.config(font=("Arial", 12))
        #rx_packets.place(x=10,y=140)
        self.rx_packets.place(relx=.5, y=65, anchor="center")

        self.rx_errors = Label(traffic_rxframe, text="----")
        self.rx_errors.config(font=("Arial", 12))
        #rx_errors.place(x=10,y=140)
        self.rx_errors.place(relx=.5, y=110, anchor="center")

        self.rx_dropped = Label(traffic_rxframe, text="----")
        self.rx_dropped.config(font=("Arial", 12))
        #rx_dropped.place(x=10,y=140)
        self.rx_dropped.place(relx=.5, y=155, anchor="center")

        ''' Users Frames'''
        users_main = LabelFrame(self, text="Connected Devices", width=380, height=440)
        users_main.config(font=("Arial", 20), labelanchor=N)
        users_main.place(x=400, y=20)

        user_countframe = LabelFrame(users_main, width=60, height=32)
        user_countframe.place(x=195, y=10)

        # self.users_devices = LabelFrame(users_main, text="Connected Devices", width=360, height=350)
        # self.users_devices.config(font=("Arial", 16), labelanchor=N)
        # self.users_devices.place(x=10, y=40)

        user_count_text = Label(users_main, text="count :")
        user_count_text.config(font=("Arial", 14))
        #rx_bytes.place(x=10,y=140)
        user_count_text.place(x=120, y=10)

        self.user_count = Label(user_countframe, text="--")
        self.user_count.config(font=("Arial", 14))
        #rx_bytes.place(x=10,y=140)
        self.user_count.place(relx=.5, rely=0.5, anchor="center")

        ''' Buttons '''
        self.SD_button = Button(self.master, text="Shutdown", command=self.shutdown, height= 2, width= 10)
        self.SD_button.config(font=("Arial", 14))
        self.SD_button.place(x=60,y=360)
        self.RS_button = Button(self.master, text="Restart", command=self.restart, height= 2, width= 10)
        self.RS_button.config(font=("Arial", 14))
        self.RS_button.place(x=230,y=360)

        ''' Text Field '''
        self.device_box=Text(users_main,width=40, height=19)
        self.device_box.config(font=("Arial", 12))
        self.device_box.place(relx=0.5, y=220, anchor="center")

        self.update_fields()

    def shutdown(self):
        subprocess.check_output("sudo shutdown -h now", shell=True)
        exit()

    def restart(self):
        subprocess.check_output("sudo reboot", shell=True)
        exit()

    def update_fields(self):
        ''' Update VPN Traffic '''
        # face || Recieve || Transmit
        # face || bytes, packets, errs, drop, fifo, frame, compressed, multicast || bytes, packets, errs, drop, fifo, colls, carrier, compressed
        try:
            traffic_tun0 = subprocess.check_output("cat /proc/net/dev | grep tun0 | grep -o '[0-9]*'", shell=True).decode().split("\n")
            if int(traffic_tun0[1]) > 9e2 and int(traffic_tun0[1]) <= 9e5: # > 900 bytes
                self.rx_bytes.config(text=str(round(int(traffic_tun0[1]) / 1e3,2)) + " kB")
            elif int(traffic_tun0[1]) > 9e5 and int(traffic_tun0[1]) <= 9e8: # > 900 kB
                self.rx_bytes.config(text=str(round(int(traffic_tun0[1]) / 1e6,2)) + " MB")
            elif int(traffic_tun0[1]) > 9e8: # > 900 MB
                self.rx_bytes.config(text=str(round(int(traffic_tun0[1]) / 1e9,2)) + " GB")
            else:
                self.rx_bytes.config(text=traffic_tun0[1] + " bytes")
            #self.rx_bytes = traffic_tun0[1]
            self.rx_packets.config(text=traffic_tun0[2])
            self.rx_errors.config(text=traffic_tun0[3])
            self.rx_dropped.config(text=traffic_tun0[4])

            if int(traffic_tun0[9]) > 9e2 and int(traffic_tun0[9]) <= 9e5: # > 900 bytes
                self.tx_bytes.config(text=str(round(int(traffic_tun0[9]) / 1e3,2)) + " kB")
            elif int(traffic_tun0[9]) > 9e5 and int(traffic_tun0[9]) <= 9e8: # > 900 kB
                self.tx_bytes.config(text=str(round(int(traffic_tun0[9]) / 1e6,2)) + " MB")
            elif int(traffic_tun0[9]) > 9e8: # > 900 MB
                self.tx_bytes.config(text=str(round(int(traffic_tun0[9]) / 1e9,2)) + " GB")
            else:
                self.tx_bytes.config(text=traffic_tun0[1] + " bytes")
            #self.tx_bytes = traffic_tun0[9]
            self.tx_packets.config(text=traffic_tun0[10])
            self.tx_errors.config(text=traffic_tun0[11])
            self.tx_dropped.config(text=traffic_tun0[12])
        except:
            pass

        '''Update User Count'''
        try:
            devices = subprocess.check_output("arp -ai wlan-ap", shell=True).decode().split("\n")
            idx = 0
            flag_tmp = True
            self.device_box.configure(state='normal')
            self.device_box.delete('1.0', END)
            self.device_box.configure(state='disabled')
            for device in devices:
                if len(device) is not 0:
                    device_list = device.split(" ")
                    res = [y for y in device_list if "arp:" in y]
                    if len(res) > 0:
                        flag_tmp = False
                    else:
                        flag_tmp = True
                    if device_list[3] != '<incomplete>' and flag_tmp is True :
                        idx += 1
                        self.device_box.configure(state='normal')
                        self.device_box.insert(END,"  " + device_list[0] + " " + device_list[1] + '\n')
                        self.device_box.configure(state='disabled')
            self.user_count.config(text=str(idx))

        except:
            self.user_count.config(text="0")
            pass

        self.after(1000, self.update_fields)


root = Tk()

# size of the window
root.geometry("800x480")

#root.config(cursor="none")
#root.attributes("-fullscreen", True)

app = window(root)

root.mainloop()
