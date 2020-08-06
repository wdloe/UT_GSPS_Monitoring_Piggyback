# Introduction
This application is a product solution to monitor Inmarsat GSPS UT Signal Strength on any location over the Internet. Signal Strength data is obtained from RSSI data of the following GSPS UT. The RSSI data is obtained by AT command (AT+CSQ). 

The Signal Strength data will be transmitted over the Internet after being processed by a Single Board Computer. SBC will be obtaining the data with a serial communication between it and the GSPS UT.

This application could be used on any internet connection (such as Wi-Fi, Wired Connection, and GSM) since it is linked with a Virtual Private Network (VPN), provided by ZeroTier.

This product solution contains the Software, Hardware, and its container.

# Requirements
1. Python 3
2. Linux Based OS
3. Libraries : serial, os, psutil, sys, time, requests, logging

# How to Use
## User Section
1.	Hardware is powered up by Power-over-Ethernet. So, just plug the RJ45 Cable (output of PoE adaptor) into PoE port in the side of the container.

2.	After the device is powered up, we could start to remote using SSH or Remote Desktop by connecting any Personal Computer (such as PCs, Laptops, Smartphones) to device’s public address. (Ask your Device administrator to know the IP address. The IP address is Static IPv4, so keep in mind.)

3.	Run the program by typing this following syntax on the Terminal/Serial Monitor.
'bash launcher.sh &> /dev/null &'

4.	The program should be run. If you want to close the process we could use two methods.
- By press Ctrl + C.
- Killing its PID, by type kill <PID> in another terminal. You can know the PID number by viewing last file created in the program directory.
  
## Admin Section
1.	For ease, we could configure the device by connecting the SBC to external peripheral, such as: monitor, keyboard, and mouse. Make sure the SBC is connected through the internet.

2.	Make sure that ZeroTier is installed on the SBC. After being installed, connect to our VPN. Contact your company to know the VPN ID. After knowing the VPN ID, input that ID to your ZeroTier interface to connect. Just wait for your company to approve your devices. The ZeroTier will be automatically run every boot. *(Note : Any method like NAT is no problem, while the admin and the remote SBC are in same network)*

3.	Once your device is being approved, you are already joined on our VPN. Run this syntax to know your network identity.
ifconfig
After knowing the public address, we could start to remote the SBC. Please keep in mind that local address is different with public address. In general, public address doesn’t start with 192.168.xxx.xxx.

4.	To run the program, make sure to have these 3 files.
-	launcher.sh
-	getRSSI.py
-	getRSSIevent.py

5. Run the program by typing this following syntax on the Terminal/Serial Monitor.
'bash launcher.sh &> /dev/null &'

6. Once your program already ran, a new file should be appeared. That file is logging the PID number of the process. So, it is very helpful when we want to kill the process.

# How does the program work?
The program is working by using serial library. The serial library will make a communication to the GSPS UT. Since the GSPS UT has same base with GSM, we could use AT commands to it. Basically, the main program is just giving AT commands input in every period of time. The RSSI data is being collected by giving AT+CSQ command.

AT+CSQ command is giving this output: <RSSI>,<BER>. Since we are just going to obtain the RSSI, the program should slice it. For the device unique id, the program obtained IMEI data by giving AT+CGSN command.

Since the output of the serial is an array of character (string), the program should slice its output and translate from string to its adequate data type. By default, csq is float, id is integer, and ts is integer.
 
The program also could report the danger event. Such as: CPU overheat, CPU overload, process not running, and memory overload. 

# Container Specification
The container is fully designed by SolidWorks 2013. The dimensions of this container are 200x180x51 mm without lid, and 200x180x56 mm using lid. The container is using 3D print plastic material, and the lid is using acrylic with rubber around it. There is also passive humidity escape hole.

To stick SBC to the container, use small screw and the using of rubber washer is recommended. IsatPhone2 is no need to use another screw since it has the following mounting at the bottom.

The container has two ports in the right side, there are: BNC connector for antenna and ethernet port for wired internet and PoE. The BNC connector is directly connected to L-band cable, which is ended up by connect it to the bottom of IsatPhone2. 

# Wiring Diagram







