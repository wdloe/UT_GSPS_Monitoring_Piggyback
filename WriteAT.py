# Write AT+CSQ
# CREATED by William Damario Lukito
import time
import serial

# GUIDELINE
## AT+CGSN for getting IMEI data
## AT+CSQ for getting <RSSI>,<BER>

# Choose which USB Port ?
## ut_port = input()
ut_port = '/dev/ttyUSB1'

# Serial Connection to Modem
ut = serial.Serial(ut_port, 115200, timeout=0)

#check OK
cmd='AT\r'
ut.write(cmd.encode())
ut_ok=ut.readline()
print(ut_ok.decode('utf-8'))

#check IMEI
cmd='AT+CGSN\r'
ut.write(cmd.encode())
ut_imei=ut.readline()
print(ut_imei.decode('utf-8'))

#check RSSI and BER
cmd='AT+CSQ\r'
ut.write(cmd.encode())
ut_csq=ut.readline()
print(ut_csq.decode('utf-8'))
