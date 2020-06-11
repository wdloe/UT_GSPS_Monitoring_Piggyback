#Step-by-step
import serial
import time

ut_port='/dev/ttyUSB0' #by default, in first after boot will be USB0
ut=serial.Serial(ut_port, 115200, timeout=2)
print()
print(ut.name)

#check OK
cmd_ok='AT\r'
ut.write(cmd_ok.encode())
print('Getting device ready ... ')

ut_ok=ut.readline() #blank
ut_ok=ut.readline() #OK
ut_ok=ut_ok.decode('utf-8')
oke=ut_ok[0:2]
if oke=='OK':
    print(oke+': Your device is ready')
else:
    print(oke+': Your device is not ready. Please try again')
    
#checking device IMEI
ut.reset_output_buffer()
cmd_imei='AT+CGSN\r'
ut.write(cmd_imei.encode())
print()
print('Getting device information ... ')

ut_cgsn=ut.readline() #blank
ut_cgsn=ut.readline() #IMEI
ut_cgsn=ut_cgsn.decode('utf-8')
imei=ut_cgsn[0:15] #unique id upload to server
print('IMEI : '+imei)

#getting RSSI data
ut.reset_output_buffer()
cmd_csq='AT+CSQ\r'
ut.write(cmd_csq.encode())
print()
print('Getting RSSI ... ')

ut_csq=ut.readline() #blank
ut_csq=ut.readline() #OK
ut_csq=ut.readline() #blank
ut_csq=ut.readline() #CSQ
ut_csq=ut_csq.decode('utf-8')

colon=ut_csq.find(',')
rssi=ut_csq[colon-2:colon]
ber=ut_csq[colon+1:colon+3]
print('RSSI: '+rssi)
print('Bit-Error-Rate: '+ber)
print()