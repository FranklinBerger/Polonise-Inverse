EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A3 16535 11693
encoding utf-8
Sheet 1 1
Title "Calculatrice Polonaise Inversse"
Date ""
Rev ""
Comp "Pour ETML 2020"
Comment1 "Sleny Martinez"
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L archive:RF_Module_ESP32-WROOM-32 U3
U 1 1 5EC279B3
P 3800 6050
F 0 "U3" H 3925 4625 50  0000 C CNN
F 1 "ESP32-WROOM-32" H 4250 4700 50  0000 C CNN
F 2 "RF_Module:ESP32-WROOM-32" H 3800 4550 50  0001 C CNN
F 3 "https://www.espressif.com/sites/default/files/documentation/esp32-wroom-32_datasheet_en.pdf" H 3500 6100 50  0001 C CNN
F 4 "33003540884" H 3800 6050 50  0001 C CNN "N° Fournisseur"
F 5 "1904-1010-1-ND" H 3800 6050 50  0001 C CNN "N° Digikey"
	1    3800 6050
	1    0    0    -1  
$EndComp
$Comp
L archive:Battery_Management_Wavga_TP4056 U1
U 1 1 5EC364D8
P 1800 1975
F 0 "U1" H 1625 2275 50  0000 C CNN
F 1 "Wavga_TP4056" H 1875 1725 50  0000 C CNN
F 2 "Module:Wavgat_TP4056" H 1400 2375 50  0001 C CNN
F 3 "" H 1400 2375 50  0001 C CNN
F 4 "32797834680" H 1800 1975 50  0001 C CNN "N° Fournisseur"
	1    1800 1975
	1    0    0    -1  
$EndComp
$Comp
L archive:power_GND #PWR0104
U 1 1 5EC429FF
P 2200 2425
F 0 "#PWR0104" H 2200 2175 50  0001 C CNN
F 1 "GND" H 2205 2252 50  0000 C CNN
F 2 "" H 2200 2425 50  0001 C CNN
F 3 "" H 2200 2425 50  0001 C CNN
	1    2200 2425
	1    0    0    -1  
$EndComp
Wire Wire Line
	2200 2425 2200 2125
Wire Wire Line
	2200 2125 2150 2125
$Comp
L archive:power_+VDC #PWR0105
U 1 1 5EC44C5E
P 4200 1975
F 0 "#PWR0105" H 4200 1875 50  0001 C CNN
F 1 "+VDC" H 4200 2250 50  0000 C CNN
F 2 "" H 4200 1975 50  0001 C CNN
F 3 "" H 4200 1975 50  0001 C CNN
	1    4200 1975
	1    0    0    -1  
$EndComp
$Comp
L archive:power_+BATT #PWR0106
U 1 1 5EC459DA
P 2500 1475
F 0 "#PWR0106" H 2500 1325 50  0001 C CNN
F 1 "+BATT" V 2515 1603 50  0000 L CNN
F 2 "" H 2500 1475 50  0001 C CNN
F 3 "" H 2500 1475 50  0001 C CNN
	1    2500 1475
	0    1    1    0   
$EndComp
$Comp
L archive:power_-BATT #PWR0107
U 1 1 5EC46228
P 2500 1875
F 0 "#PWR0107" H 2500 1725 50  0001 C CNN
F 1 "-BATT" V 2515 2003 50  0000 L CNN
F 2 "" H 2500 1875 50  0001 C CNN
F 3 "" H 2500 1875 50  0001 C CNN
	1    2500 1875
	0    1    1    0   
$EndComp
Wire Wire Line
	2150 1775 2200 1775
$Comp
L archive:Device_Battery_Cell BT1
U 1 1 5EC4AFEB
P 2450 1725
F 0 "BT1" H 2568 1821 50  0000 L CNN
F 1 "Litium 3.4[Ah]" H 2568 1730 50  0000 L CNN
F 2 "Battery:BatteryHolder_Aliexpress_XZT_18650" V 2450 1785 50  0001 C CNN
F 3 "~" V 2450 1785 50  0001 C CNN
F 4 "33016517000 & 33045310581" H 2450 1725 50  0001 C CNN "N° Fournisseur"
F 5 "Conrad 1558873 - 62" H 2450 1725 50  0001 C CNN "N° Digikey"
	1    2450 1725
	1    0    0    -1  
$EndComp
Wire Wire Line
	2450 1825 2450 1875
Wire Wire Line
	2150 1875 2450 1875
Wire Wire Line
	2200 1775 2200 1475
Wire Wire Line
	2200 1475 2450 1475
Wire Wire Line
	2450 1475 2450 1525
Wire Wire Line
	2500 1875 2450 1875
Connection ~ 2450 1875
Wire Wire Line
	2450 1475 2500 1475
Connection ~ 2450 1475
$Comp
L archive:power_+5V #PWR0108
U 1 1 5EC50E7A
P 1450 1825
F 0 "#PWR0108" H 1450 1675 50  0001 C CNN
F 1 "+5V" V 1465 1953 50  0000 L CNN
F 2 "" H 1450 1825 50  0001 C CNN
F 3 "" H 1450 1825 50  0001 C CNN
	1    1450 1825
	0    -1   -1   0   
$EndComp
$Comp
L archive:power_GND #PWR0109
U 1 1 5EC51798
P 1450 2075
F 0 "#PWR0109" H 1450 1825 50  0001 C CNN
F 1 "GND" V 1455 1947 50  0000 R CNN
F 2 "" H 1450 2075 50  0001 C CNN
F 3 "" H 1450 2075 50  0001 C CNN
	1    1450 2075
	0    1    1    0   
$EndComp
Wire Wire Line
	1450 2075 1500 2075
Wire Wire Line
	1500 1825 1450 1825
Text Notes 1100 1425 0    100  ~ 0
Gestion Allimentation\n& Batterie Lithium\n
Text Notes 1125 1500 0    50   ~ 0
Gestionaire Batterie
Text Notes 4100 1400 0    50   ~ 0
Régulateur\nBuck-Boost 3V3\n
$Comp
L archive:power_GND #PWR0113
U 1 1 5EC5E23B
P 3800 7500
F 0 "#PWR0113" H 3800 7250 50  0001 C CNN
F 1 "GND" H 3800 7350 50  0000 C CNN
F 2 "" H 3800 7500 50  0001 C CNN
F 3 "" H 3800 7500 50  0001 C CNN
	1    3800 7500
	1    0    0    -1  
$EndComp
$Comp
L archive:Connector_Conn_01x06_Female J1
U 1 1 5EC5FAB2
P 1150 4750
F 0 "J1" H 1125 5125 50  0000 C CNN
F 1 "FT232RL" H 1025 5050 50  0000 C CNN
F 2 "Connector_PinSocket_2.54mm:PinSocket_1x06_P2.54mm_Horizontal" H 1150 4750 50  0001 C CNN
F 3 "~" H 1150 4750 50  0001 C CNN
F 4 "32826575637" H 1150 4750 50  0001 C CNN "N° Fournisseur"
	1    1150 4750
	-1   0    0    -1  
$EndComp
$Comp
L archive:power_GND #PWR0114
U 1 1 5EC629E0
P 2125 4550
F 0 "#PWR0114" H 2125 4300 50  0001 C CNN
F 1 "GND" V 2130 4422 50  0000 R CNN
F 2 "" H 2125 4550 50  0001 C CNN
F 3 "" H 2125 4550 50  0001 C CNN
	1    2125 4550
	0    -1   -1   0   
$EndComp
Wire Wire Line
	2125 4550 1350 4550
$Comp
L archive:Jumper_SolderJumper_2_Open JP1
U 1 1 5EC65C35
P 1925 4750
F 0 "JP1" H 1925 4825 50  0000 C CNN
F 1 "Jumper à souder" H 2175 4675 50  0000 C CNN
F 2 "Jumper:SolderJumper-2_P1.3mm_Open_TrianglePad1.0x1.5mm" H 1925 4750 50  0001 C CNN
F 3 "~" H 1925 4750 50  0001 C CNN
	1    1925 4750
	1    0    0    -1  
$EndComp
Wire Wire Line
	1775 4750 1350 4750
Wire Wire Line
	1350 4650 1475 4650
$Comp
L archive:power_+5V #PWR0115
U 1 1 5EC68836
P 2125 4750
F 0 "#PWR0115" H 2125 4600 50  0001 C CNN
F 1 "+5V" V 2140 4878 50  0000 L CNN
F 2 "" H 2125 4750 50  0001 C CNN
F 3 "" H 2125 4750 50  0001 C CNN
	1    2125 4750
	0    1    1    0   
$EndComp
Wire Wire Line
	2125 4750 2075 4750
Wire Wire Line
	1450 4850 1350 4850
Wire Wire Line
	1350 4950 1450 4950
Wire Wire Line
	1450 5050 1350 5050
Text GLabel 1450 5050 2    50   Output ~ 0
FTDI_DTR
Text GLabel 1450 4950 2    50   Input ~ 0
FTDI_Rx
Text GLabel 1450 4850 2    50   Output ~ 0
FTDI_Tx
Text GLabel 1475 4650 2    50   Output ~ 0
FTDI_CTS
$Comp
L archive:Switch_SW_wuerth_4.5x6.5mm SW1
U 1 1 5EC8B4A4
P 2200 5925
F 0 "SW1" H 2025 5700 50  0000 C CNN
F 1 "Wuerth_4.5x6.5mm" H 2300 5775 50  0000 C CNN
F 2 "Button_Switch_THT:SW_Wuerth_6.5x4.5mm" H 2050 5755 50  0001 C CNN
F 3 "" H 2050 5755 50  0001 C CNN
F 4 "32856600638" H 2200 5925 50  0001 C CNN "N° Fournisseur"
F 5 "450-1647-ND" H 2200 5925 50  0001 C CNN "N° Digikey"
	1    2200 5925
	1    0    0    -1  
$EndComp
Wire Wire Line
	2000 5825 1950 5825
Wire Wire Line
	1950 5825 1950 5925
Wire Wire Line
	1950 6025 2000 6025
Wire Wire Line
	2400 5825 2450 5825
Wire Wire Line
	2450 5825 2450 5925
Wire Wire Line
	2450 6025 2400 6025
$Comp
L archive:power_+3V3 #PWR0116
U 1 1 5EC92B78
P 1425 5925
F 0 "#PWR0116" H 1425 5775 50  0001 C CNN
F 1 "+3V3" V 1440 6053 50  0000 L CNN
F 2 "" H 1425 5925 50  0001 C CNN
F 3 "" H 1425 5925 50  0001 C CNN
	1    1425 5925
	0    -1   -1   0   
$EndComp
$Comp
L archive:Device_R R1
U 1 1 5EC95FA3
P 1625 5925
F 0 "R1" V 1418 5925 50  0000 C CNN
F 1 "1[KΩ]" V 1509 5925 50  0000 C CNN
F 2 "Resistor_SMD:R_1206_3216Metric_Pad1.42x1.75mm_HandSolder" V 1555 5925 50  0001 C CNN
F 3 "~" H 1625 5925 50  0001 C CNN
F 4 "32859526036" H 1625 5925 50  0001 C CNN "N° Fournisseur"
F 5 "311-1.0KERCT-ND" H 1625 5925 50  0001 C CNN "N° Digikey"
	1    1625 5925
	0    1    1    0   
$EndComp
Wire Wire Line
	1775 5925 1875 5925
Connection ~ 1950 5925
Wire Wire Line
	1950 5925 1950 6025
Text GLabel 1875 5325 1    50   Output ~ 0
EN
Connection ~ 1875 5925
Wire Wire Line
	1875 5925 1950 5925
$Comp
L archive:power_GND #PWR0117
U 1 1 5EC9C2B6
P 2575 5925
F 0 "#PWR0117" H 2575 5675 50  0001 C CNN
F 1 "GND" V 2580 5797 50  0000 R CNN
F 2 "" H 2575 5925 50  0001 C CNN
F 3 "" H 2575 5925 50  0001 C CNN
	1    2575 5925
	0    -1   -1   0   
$EndComp
Wire Wire Line
	2575 5925 2450 5925
Connection ~ 2450 5925
Wire Wire Line
	2450 5925 2450 6025
Wire Wire Line
	1425 5925 1475 5925
Wire Wire Line
	2575 6775 2375 6775
$Comp
L archive:power_GND #PWR0118
U 1 1 5ECAC18F
P 2575 6775
F 0 "#PWR0118" H 2575 6525 50  0001 C CNN
F 1 "GND" V 2580 6647 50  0000 R CNN
F 2 "" H 2575 6775 50  0001 C CNN
F 3 "" H 2575 6775 50  0001 C CNN
	1    2575 6775
	0    -1   -1   0   
$EndComp
Wire Wire Line
	1875 6775 1875 7125
Connection ~ 1875 6775
Wire Wire Line
	2075 6775 1875 6775
$Comp
L archive:Device_C C2
U 1 1 5ECAC186
P 2225 6775
F 0 "C2" V 2425 6725 50  0000 L CNN
F 1 "100[nF]" V 2350 6625 50  0000 L CNN
F 2 "Capacitor_SMD:C_1206_3216Metric_Pad1.42x1.75mm_HandSolder" H 2263 6625 50  0001 C CNN
F 3 "~" H 2225 6775 50  0001 C CNN
F 4 "33059508387" H 2225 6775 50  0001 C CNN "N° Fournisseur"
F 5 "399-C1206C104K5RAC7800CT-ND" H 2225 6775 50  0001 C CNN "N° Digikey"
	1    2225 6775
	0    -1   -1   0   
$EndComp
Wire Wire Line
	1425 7125 1475 7125
Wire Wire Line
	2450 7125 2450 7225
Connection ~ 2450 7125
Wire Wire Line
	2575 7125 2450 7125
$Comp
L archive:power_GND #PWR0119
U 1 1 5ECAC17C
P 2575 7125
F 0 "#PWR0119" H 2575 6875 50  0001 C CNN
F 1 "GND" V 2580 6997 50  0000 R CNN
F 2 "" H 2575 7125 50  0001 C CNN
F 3 "" H 2575 7125 50  0001 C CNN
	1    2575 7125
	0    -1   -1   0   
$EndComp
Wire Wire Line
	1875 7125 1950 7125
Connection ~ 1875 7125
Wire Wire Line
	1875 6525 1875 6775
Text GLabel 1875 6525 1    50   Output ~ 0
BOOT0
Wire Wire Line
	1950 7125 1950 7225
Connection ~ 1950 7125
Wire Wire Line
	1775 7125 1875 7125
$Comp
L archive:Device_R R2
U 1 1 5ECAC16F
P 1625 7125
F 0 "R2" V 1418 7125 50  0000 C CNN
F 1 "1[KΩ]" V 1509 7125 50  0000 C CNN
F 2 "Resistor_SMD:R_1206_3216Metric_Pad1.42x1.75mm_HandSolder" V 1555 7125 50  0001 C CNN
F 3 "~" H 1625 7125 50  0001 C CNN
F 4 "32859526036" H 1625 7125 50  0001 C CNN "N° Fournisseur"
F 5 "311-1.0KERCT-ND" H 1625 7125 50  0001 C CNN "N° Digikey"
	1    1625 7125
	0    1    1    0   
$EndComp
$Comp
L archive:power_+3V3 #PWR0120
U 1 1 5ECAC169
P 1425 7125
F 0 "#PWR0120" H 1425 6975 50  0001 C CNN
F 1 "+3V3" V 1440 7253 50  0000 L CNN
F 2 "" H 1425 7125 50  0001 C CNN
F 3 "" H 1425 7125 50  0001 C CNN
	1    1425 7125
	0    -1   -1   0   
$EndComp
Wire Wire Line
	2450 7225 2400 7225
Wire Wire Line
	2450 7025 2450 7125
Wire Wire Line
	2400 7025 2450 7025
Wire Wire Line
	1950 7225 2000 7225
Wire Wire Line
	1950 7025 1950 7125
Wire Wire Line
	2000 7025 1950 7025
$Comp
L archive:Switch_SW_wuerth_4.5x6.5mm SW2
U 1 1 5ECAC15D
P 2200 7125
F 0 "SW2" H 2025 6900 50  0000 C CNN
F 1 "Wuerth_4.5x6.5mm" H 2300 6975 50  0000 C CNN
F 2 "Button_Switch_THT:SW_Wuerth_6.5x4.5mm" H 2050 6955 50  0001 C CNN
F 3 "" H 2050 6955 50  0001 C CNN
F 4 "32856600638" H 2200 7125 50  0001 C CNN "N° Fournisseur"
F 5 "450-1647-ND" H 2200 7125 50  0001 C CNN "N° Digikey"
	1    2200 7125
	1    0    0    -1  
$EndComp
Wire Wire Line
	4200 1975 4200 2025
Connection ~ 4200 2025
Wire Notes Line
	1075 6200 2900 6200
Wire Notes Line
	2900 5150 1075 5150
Wire Notes Line
	1075 7400 2900 7400
Text Notes 1100 5250 0    50   ~ 0
BP EN\n
Text Notes 1100 6300 0    50   ~ 0
BP Boot0\n
Text Notes 1725 4425 0    50   ~ 0
Connecteur FTDI Programation
Text Notes 1050 4325 0    100  ~ 0
Interfaces\nde contrôle\n
Wire Wire Line
	2575 5575 2375 5575
$Comp
L archive:power_GND #PWR0121
U 1 1 5ECA627F
P 2575 5575
F 0 "#PWR0121" H 2575 5325 50  0001 C CNN
F 1 "GND" V 2580 5447 50  0000 R CNN
F 2 "" H 2575 5575 50  0001 C CNN
F 3 "" H 2575 5575 50  0001 C CNN
	1    2575 5575
	0    -1   -1   0   
$EndComp
Wire Wire Line
	1875 5575 1875 5925
Wire Wire Line
	1875 5325 1875 5575
Connection ~ 1875 5575
Wire Wire Line
	2075 5575 1875 5575
$Comp
L archive:Device_C C1
U 1 1 5ECA1259
P 2225 5575
F 0 "C1" V 2425 5525 50  0000 L CNN
F 1 "100[nF]" V 2350 5425 50  0000 L CNN
F 2 "Capacitor_SMD:C_1206_3216Metric_Pad1.42x1.75mm_HandSolder" H 2263 5425 50  0001 C CNN
F 3 "~" H 2225 5575 50  0001 C CNN
F 4 "33059508387" H 2225 5575 50  0001 C CNN "N° Fournisseur"
F 5 "399-C1206C104K5RAC7800CT-ND" H 2225 5575 50  0001 C CNN "N° Digikey"
	1    2225 5575
	0    -1   -1   0   
$EndComp
Text GLabel 4500 5150 2    50   Input ~ 0
FTDI_Tx
Wire Wire Line
	4500 5150 4400 5150
Text GLabel 4500 4950 2    50   Output ~ 0
FTDI_Rx
Wire Wire Line
	4500 4950 4400 4950
NoConn ~ 4400 5050
Text GLabel 4500 4850 2    50   Input ~ 0
BOOT0
Wire Wire Line
	4500 4850 4400 4850
Text GLabel 3100 4850 0    50   Input ~ 0
EN
Wire Wire Line
	3100 4850 3200 4850
Wire Notes Line
	4475 4775 4850 4775
Wire Notes Line
	4850 4775 4850 5225
Wire Notes Line
	4850 5225 4475 5225
Text Notes 4850 4925 0    50   ~ 0
Pins de\nprogramation
Text Notes 1100 7825 0    50   ~ 0
ROM Serial Bootloader:\nEN => Low Pulse (Reset)\nGPIO0 => Low\nGPIO2 => Low (Pull-Down inside)\nStays there until the device is reset
Wire Notes Line
	1075 4325 1075 7850
Wire Notes Line
	1075 7850 2900 7850
Wire Notes Line
	4475 4775 4475 5225
Text GLabel 4500 5450 2    50   Input ~ 0
P_COL1
Text GLabel 4500 5550 2    50   Input ~ 0
P_COL2
Text GLabel 4500 5650 2    50   Input ~ 0
P_COL3
Text GLabel 4500 5750 2    50   Input ~ 0
P_COL4
Text GLabel 4500 5850 2    50   Input ~ 0
P_COL5
Wire Wire Line
	4500 5450 4400 5450
Wire Wire Line
	4400 5550 4500 5550
Wire Wire Line
	4500 5650 4400 5650
Wire Wire Line
	4400 5750 4500 5750
Wire Wire Line
	4500 5850 4400 5850
Text GLabel 4500 5950 2    50   Input ~ 0
ROW1
Text GLabel 4500 6050 2    50   Input ~ 0
ROW2
Text GLabel 4500 6150 2    50   Input ~ 0
ROW3
Text GLabel 4500 6250 2    50   Input ~ 0
ROW4
Text GLabel 4500 6350 2    50   Input ~ 0
ROW5
Text GLabel 4500 6450 2    50   Input ~ 0
ROW6
Text GLabel 4500 6550 2    50   Input ~ 0
ROW7
Wire Wire Line
	4500 5950 4400 5950
Wire Wire Line
	4400 6050 4500 6050
Wire Wire Line
	4500 6150 4400 6150
Wire Wire Line
	4400 6250 4500 6250
Wire Wire Line
	4500 6350 4400 6350
Wire Wire Line
	4400 6450 4500 6450
Wire Wire Line
	4500 6550 4400 6550
Wire Notes Line
	4850 5400 4850 6600
Text Notes 4850 5500 0    50   ~ 0
Clavier
Text GLabel 4500 6850 2    50   BiDi ~ 0
LCD_SCL
Text GLabel 4500 6950 2    50   BiDi ~ 0
LCD_SDA
Wire Wire Line
	4500 6850 4400 6850
Wire Wire Line
	4400 6950 4500 6950
Wire Notes Line
	4475 7025 4925 7025
Wire Notes Line
	4925 7025 4925 6600
Text Notes 4925 6825 0    50   ~ 0
Écran\nLCD\nContrôle
Wire Notes Line
	5375 4325 5375 7700
Wire Notes Line
	5375 7700 2900 7700
Text Notes 2900 4325 0    100  ~ 0
Microcontrôleur
$Comp
L archive:Switch_SW_Push_45deg SW37
U 1 1 5ED93D16
P 12925 7850
F 0 "SW37" H 12925 8000 50  0000 C CNN
F 1 "G77" H 12925 8040 50  0001 C CNN
F 2 "Button_Switch_THT:SW_PUSH-12mm_Wuerth-430476085716" H 12925 7850 50  0001 C CNN
F 3 "~" H 12925 7850 50  0001 C CNN
F 4 "32668706990" H 12925 7850 50  0001 C CNN "N° Fournisseur"
	1    12925 7850
	1    0    0    -1  
$EndComp
$Comp
L archive:Switch_SW_Push_45deg SW30
U 1 1 5ED93D10
P 12550 7850
F 0 "SW30" H 12550 8000 50  0000 C CNN
F 1 "G77" H 12550 8040 50  0001 C CNN
F 2 "Button_Switch_THT:SW_PUSH-12mm_Wuerth-430476085716" H 12550 7850 50  0001 C CNN
F 3 "~" H 12550 7850 50  0001 C CNN
F 4 "32668706990" H 12550 7850 50  0001 C CNN "N° Fournisseur"
	1    12550 7850
	1    0    0    -1  
$EndComp
$Comp
L archive:Switch_SW_Push_45deg SW23
U 1 1 5ED93D0A
P 12175 7850
F 0 "SW23" H 12175 8000 50  0000 C CNN
F 1 "G77" H 12175 8040 50  0001 C CNN
F 2 "Button_Switch_THT:SW_PUSH-12mm_Wuerth-430476085716" H 12175 7850 50  0001 C CNN
F 3 "~" H 12175 7850 50  0001 C CNN
F 4 "32668706990" H 12175 7850 50  0001 C CNN "N° Fournisseur"
	1    12175 7850
	1    0    0    -1  
$EndComp
$Comp
L archive:Switch_SW_Push_45deg SW16
U 1 1 5ED93D04
P 11800 7850
F 0 "SW16" H 11800 8000 50  0000 C CNN
F 1 "G77" H 11800 8040 50  0001 C CNN
F 2 "Button_Switch_THT:SW_PUSH-12mm_Wuerth-430476085716" H 11800 7850 50  0001 C CNN
F 3 "~" H 11800 7850 50  0001 C CNN
F 4 "32668706990" H 11800 7850 50  0001 C CNN "N° Fournisseur"
	1    11800 7850
	1    0    0    -1  
$EndComp
$Comp
L archive:Switch_SW_Push_45deg SW9
U 1 1 5ED93CFE
P 11425 7850
F 0 "SW9" H 11425 8000 50  0000 C CNN
F 1 "G77" H 11425 8040 50  0001 C CNN
F 2 "Button_Switch_THT:SW_PUSH-12mm_Wuerth-430476085716" H 11425 7850 50  0001 C CNN
F 3 "~" H 11425 7850 50  0001 C CNN
F 4 "32668706990" H 11425 7850 50  0001 C CNN "N° Fournisseur"
	1    11425 7850
	1    0    0    -1  
$EndComp
$Comp
L archive:Switch_SW_Push_45deg SW36
U 1 1 5ED8DC02
P 12925 7475
F 0 "SW36" H 12925 7625 50  0000 C CNN
F 1 "G77" H 12925 7665 50  0001 C CNN
F 2 "Button_Switch_THT:SW_PUSH-12mm_Wuerth-430476085716" H 12925 7475 50  0001 C CNN
F 3 "~" H 12925 7475 50  0001 C CNN
F 4 "32668706990" H 12925 7475 50  0001 C CNN "N° Fournisseur"
	1    12925 7475
	1    0    0    -1  
$EndComp
$Comp
L archive:Switch_SW_Push_45deg SW29
U 1 1 5ED8DBFC
P 12550 7475
F 0 "SW29" H 12550 7625 50  0000 C CNN
F 1 "G77" H 12550 7665 50  0001 C CNN
F 2 "Button_Switch_THT:SW_PUSH-12mm_Wuerth-430476085716" H 12550 7475 50  0001 C CNN
F 3 "~" H 12550 7475 50  0001 C CNN
F 4 "32668706990" H 12550 7475 50  0001 C CNN "N° Fournisseur"
	1    12550 7475
	1    0    0    -1  
$EndComp
$Comp
L archive:Switch_SW_Push_45deg SW22
U 1 1 5ED8DBF6
P 12175 7475
F 0 "SW22" H 12175 7625 50  0000 C CNN
F 1 "G77" H 12175 7665 50  0001 C CNN
F 2 "Button_Switch_THT:SW_PUSH-12mm_Wuerth-430476085716" H 12175 7475 50  0001 C CNN
F 3 "~" H 12175 7475 50  0001 C CNN
F 4 "32668706990" H 12175 7475 50  0001 C CNN "N° Fournisseur"
	1    12175 7475
	1    0    0    -1  
$EndComp
$Comp
L archive:Switch_SW_Push_45deg SW15
U 1 1 5ED8DBF0
P 11800 7475
F 0 "SW15" H 11800 7625 50  0000 C CNN
F 1 "G77" H 11800 7665 50  0001 C CNN
F 2 "Button_Switch_THT:SW_PUSH-12mm_Wuerth-430476085716" H 11800 7475 50  0001 C CNN
F 3 "~" H 11800 7475 50  0001 C CNN
F 4 "32668706990" H 11800 7475 50  0001 C CNN "N° Fournisseur"
	1    11800 7475
	1    0    0    -1  
$EndComp
$Comp
L archive:Switch_SW_Push_45deg SW8
U 1 1 5ED8DBEA
P 11425 7475
F 0 "SW8" H 11425 7625 50  0000 C CNN
F 1 "G77" H 11425 7665 50  0001 C CNN
F 2 "Button_Switch_THT:SW_PUSH-12mm_Wuerth-430476085716" H 11425 7475 50  0001 C CNN
F 3 "~" H 11425 7475 50  0001 C CNN
F 4 "32668706990" H 11425 7475 50  0001 C CNN "N° Fournisseur"
	1    11425 7475
	1    0    0    -1  
$EndComp
$Comp
L archive:Switch_SW_Push_45deg SW35
U 1 1 5ED8DBE4
P 12925 7100
F 0 "SW35" H 12925 7250 50  0000 C CNN
F 1 "G77" H 12925 7290 50  0001 C CNN
F 2 "Button_Switch_THT:SW_PUSH-12mm_Wuerth-430476085716" H 12925 7100 50  0001 C CNN
F 3 "~" H 12925 7100 50  0001 C CNN
F 4 "32668706990" H 12925 7100 50  0001 C CNN "N° Fournisseur"
	1    12925 7100
	1    0    0    -1  
$EndComp
$Comp
L archive:Switch_SW_Push_45deg SW28
U 1 1 5ED8DBDE
P 12550 7100
F 0 "SW28" H 12550 7250 50  0000 C CNN
F 1 "G77" H 12550 7290 50  0001 C CNN
F 2 "Button_Switch_THT:SW_PUSH-12mm_Wuerth-430476085716" H 12550 7100 50  0001 C CNN
F 3 "~" H 12550 7100 50  0001 C CNN
F 4 "32668706990" H 12550 7100 50  0001 C CNN "N° Fournisseur"
	1    12550 7100
	1    0    0    -1  
$EndComp
$Comp
L archive:Switch_SW_Push_45deg SW21
U 1 1 5ED8DBD8
P 12175 7100
F 0 "SW21" H 12175 7250 50  0000 C CNN
F 1 "G77" H 12175 7290 50  0001 C CNN
F 2 "Button_Switch_THT:SW_PUSH-12mm_Wuerth-430476085716" H 12175 7100 50  0001 C CNN
F 3 "~" H 12175 7100 50  0001 C CNN
F 4 "32668706990" H 12175 7100 50  0001 C CNN "N° Fournisseur"
	1    12175 7100
	1    0    0    -1  
$EndComp
$Comp
L archive:Switch_SW_Push_45deg SW14
U 1 1 5ED8DBD2
P 11800 7100
F 0 "SW14" H 11800 7250 50  0000 C CNN
F 1 "G77" H 11800 7290 50  0001 C CNN
F 2 "Button_Switch_THT:SW_PUSH-12mm_Wuerth-430476085716" H 11800 7100 50  0001 C CNN
F 3 "~" H 11800 7100 50  0001 C CNN
F 4 "32668706990" H 11800 7100 50  0001 C CNN "N° Fournisseur"
	1    11800 7100
	1    0    0    -1  
$EndComp
$Comp
L archive:Switch_SW_Push_45deg SW7
U 1 1 5ED8DBCC
P 11425 7100
F 0 "SW7" H 11425 7250 50  0000 C CNN
F 1 "G77" H 11425 7290 50  0001 C CNN
F 2 "Button_Switch_THT:SW_PUSH-12mm_Wuerth-430476085716" H 11425 7100 50  0001 C CNN
F 3 "~" H 11425 7100 50  0001 C CNN
F 4 "32668706990" H 11425 7100 50  0001 C CNN "N° Fournisseur"
	1    11425 7100
	1    0    0    -1  
$EndComp
$Comp
L archive:Switch_SW_Push_45deg SW34
U 1 1 5ED859FA
P 12925 6725
F 0 "SW34" H 12925 6875 50  0000 C CNN
F 1 "G77" H 12925 6915 50  0001 C CNN
F 2 "Button_Switch_THT:SW_PUSH-12mm_Wuerth-430476085716" H 12925 6725 50  0001 C CNN
F 3 "~" H 12925 6725 50  0001 C CNN
F 4 "32668706990" H 12925 6725 50  0001 C CNN "N° Fournisseur"
	1    12925 6725
	1    0    0    -1  
$EndComp
$Comp
L archive:Switch_SW_Push_45deg SW27
U 1 1 5ED859F4
P 12550 6725
F 0 "SW27" H 12550 6875 50  0000 C CNN
F 1 "G77" H 12550 6915 50  0001 C CNN
F 2 "Button_Switch_THT:SW_PUSH-12mm_Wuerth-430476085716" H 12550 6725 50  0001 C CNN
F 3 "~" H 12550 6725 50  0001 C CNN
F 4 "32668706990" H 12550 6725 50  0001 C CNN "N° Fournisseur"
	1    12550 6725
	1    0    0    -1  
$EndComp
$Comp
L archive:Switch_SW_Push_45deg SW20
U 1 1 5ED859EE
P 12175 6725
F 0 "SW20" H 12175 6875 50  0000 C CNN
F 1 "G77" H 12175 6915 50  0001 C CNN
F 2 "Button_Switch_THT:SW_PUSH-12mm_Wuerth-430476085716" H 12175 6725 50  0001 C CNN
F 3 "~" H 12175 6725 50  0001 C CNN
F 4 "32668706990" H 12175 6725 50  0001 C CNN "N° Fournisseur"
	1    12175 6725
	1    0    0    -1  
$EndComp
$Comp
L archive:Switch_SW_Push_45deg SW13
U 1 1 5ED859E8
P 11800 6725
F 0 "SW13" H 11800 6875 50  0000 C CNN
F 1 "G77" H 11800 6915 50  0001 C CNN
F 2 "Button_Switch_THT:SW_PUSH-12mm_Wuerth-430476085716" H 11800 6725 50  0001 C CNN
F 3 "~" H 11800 6725 50  0001 C CNN
F 4 "32668706990" H 11800 6725 50  0001 C CNN "N° Fournisseur"
	1    11800 6725
	1    0    0    -1  
$EndComp
$Comp
L archive:Switch_SW_Push_45deg SW6
U 1 1 5ED859E2
P 11425 6725
F 0 "SW6" H 11425 6875 50  0000 C CNN
F 1 "G77" H 11425 6915 50  0001 C CNN
F 2 "Button_Switch_THT:SW_PUSH-12mm_Wuerth-430476085716" H 11425 6725 50  0001 C CNN
F 3 "~" H 11425 6725 50  0001 C CNN
F 4 "32668706990" H 11425 6725 50  0001 C CNN "N° Fournisseur"
	1    11425 6725
	1    0    0    -1  
$EndComp
$Comp
L archive:Switch_SW_Push_45deg SW33
U 1 1 5ED859DC
P 12925 6350
F 0 "SW33" H 12925 6500 50  0000 C CNN
F 1 "G77" H 12925 6540 50  0001 C CNN
F 2 "Button_Switch_THT:SW_PUSH-12mm_Wuerth-430476085716" H 12925 6350 50  0001 C CNN
F 3 "~" H 12925 6350 50  0001 C CNN
F 4 "32668706990" H 12925 6350 50  0001 C CNN "N° Fournisseur"
	1    12925 6350
	1    0    0    -1  
$EndComp
$Comp
L archive:Switch_SW_Push_45deg SW26
U 1 1 5ED859D6
P 12550 6350
F 0 "SW26" H 12550 6500 50  0000 C CNN
F 1 "G77" H 12550 6540 50  0001 C CNN
F 2 "Button_Switch_THT:SW_PUSH-12mm_Wuerth-430476085716" H 12550 6350 50  0001 C CNN
F 3 "~" H 12550 6350 50  0001 C CNN
F 4 "32668706990" H 12550 6350 50  0001 C CNN "N° Fournisseur"
	1    12550 6350
	1    0    0    -1  
$EndComp
$Comp
L archive:Switch_SW_Push_45deg SW19
U 1 1 5ED859D0
P 12175 6350
F 0 "SW19" H 12175 6500 50  0000 C CNN
F 1 "G77" H 12175 6540 50  0001 C CNN
F 2 "Button_Switch_THT:SW_PUSH-12mm_Wuerth-430476085716" H 12175 6350 50  0001 C CNN
F 3 "~" H 12175 6350 50  0001 C CNN
F 4 "32668706990" H 12175 6350 50  0001 C CNN "N° Fournisseur"
	1    12175 6350
	1    0    0    -1  
$EndComp
$Comp
L archive:Switch_SW_Push_45deg SW12
U 1 1 5ED859CA
P 11800 6350
F 0 "SW12" H 11800 6500 50  0000 C CNN
F 1 "G77" H 11800 6540 50  0001 C CNN
F 2 "Button_Switch_THT:SW_PUSH-12mm_Wuerth-430476085716" H 11800 6350 50  0001 C CNN
F 3 "~" H 11800 6350 50  0001 C CNN
F 4 "32668706990" H 11800 6350 50  0001 C CNN "N° Fournisseur"
	1    11800 6350
	1    0    0    -1  
$EndComp
$Comp
L archive:Switch_SW_Push_45deg SW5
U 1 1 5ED859C4
P 11425 6350
F 0 "SW5" H 11425 6500 50  0000 C CNN
F 1 "G77" H 11425 6540 50  0001 C CNN
F 2 "Button_Switch_THT:SW_PUSH-12mm_Wuerth-430476085716" H 11425 6350 50  0001 C CNN
F 3 "~" H 11425 6350 50  0001 C CNN
F 4 "32668706990" H 11425 6350 50  0001 C CNN "N° Fournisseur"
	1    11425 6350
	1    0    0    -1  
$EndComp
$Comp
L archive:Switch_SW_Push_45deg SW32
U 1 1 5ED7A8EB
P 12925 5975
F 0 "SW32" H 12925 6125 50  0000 C CNN
F 1 "G77" H 12925 6165 50  0001 C CNN
F 2 "Button_Switch_THT:SW_PUSH-12mm_Wuerth-430476085716" H 12925 5975 50  0001 C CNN
F 3 "~" H 12925 5975 50  0001 C CNN
F 4 "32668706990" H 12925 5975 50  0001 C CNN "N° Fournisseur"
	1    12925 5975
	1    0    0    -1  
$EndComp
$Comp
L archive:Switch_SW_Push_45deg SW25
U 1 1 5ED7A8E5
P 12550 5975
F 0 "SW25" H 12550 6125 50  0000 C CNN
F 1 "G77" H 12550 6165 50  0001 C CNN
F 2 "Button_Switch_THT:SW_PUSH-12mm_Wuerth-430476085716" H 12550 5975 50  0001 C CNN
F 3 "~" H 12550 5975 50  0001 C CNN
F 4 "32668706990" H 12550 5975 50  0001 C CNN "N° Fournisseur"
	1    12550 5975
	1    0    0    -1  
$EndComp
$Comp
L archive:Switch_SW_Push_45deg SW18
U 1 1 5ED7A8DF
P 12175 5975
F 0 "SW18" H 12175 6125 50  0000 C CNN
F 1 "G77" H 12175 6165 50  0001 C CNN
F 2 "Button_Switch_THT:SW_PUSH-12mm_Wuerth-430476085716" H 12175 5975 50  0001 C CNN
F 3 "~" H 12175 5975 50  0001 C CNN
F 4 "32668706990" H 12175 5975 50  0001 C CNN "N° Fournisseur"
	1    12175 5975
	1    0    0    -1  
$EndComp
$Comp
L archive:Switch_SW_Push_45deg SW11
U 1 1 5ED7A8D9
P 11800 5975
F 0 "SW11" H 11800 6125 50  0000 C CNN
F 1 "G77" H 11800 6165 50  0001 C CNN
F 2 "Button_Switch_THT:SW_PUSH-12mm_Wuerth-430476085716" H 11800 5975 50  0001 C CNN
F 3 "~" H 11800 5975 50  0001 C CNN
F 4 "32668706990" H 11800 5975 50  0001 C CNN "N° Fournisseur"
	1    11800 5975
	1    0    0    -1  
$EndComp
$Comp
L archive:Switch_SW_Push_45deg SW4
U 1 1 5ED7A8D3
P 11425 5975
F 0 "SW4" H 11425 6125 50  0000 C CNN
F 1 "G77" H 11425 6165 50  0001 C CNN
F 2 "Button_Switch_THT:SW_PUSH-12mm_Wuerth-430476085716" H 11425 5975 50  0001 C CNN
F 3 "~" H 11425 5975 50  0001 C CNN
F 4 "32668706990" H 11425 5975 50  0001 C CNN "N° Fournisseur"
	1    11425 5975
	1    0    0    -1  
$EndComp
$Comp
L archive:Switch_SW_Push_45deg SW31
U 1 1 5ED75780
P 12925 5600
F 0 "SW31" H 12925 5750 50  0000 C CNN
F 1 "G77" H 12925 5790 50  0001 C CNN
F 2 "Button_Switch_THT:SW_PUSH-12mm_Wuerth-430476085716" H 12925 5600 50  0001 C CNN
F 3 "~" H 12925 5600 50  0001 C CNN
F 4 "32668706990" H 12925 5600 50  0001 C CNN "N° Fournisseur"
	1    12925 5600
	1    0    0    -1  
$EndComp
$Comp
L archive:Switch_SW_Push_45deg SW24
U 1 1 5ED73556
P 12550 5600
F 0 "SW24" H 12550 5750 50  0000 C CNN
F 1 "G77" H 12550 5790 50  0001 C CNN
F 2 "Button_Switch_THT:SW_PUSH-12mm_Wuerth-430476085716" H 12550 5600 50  0001 C CNN
F 3 "~" H 12550 5600 50  0001 C CNN
F 4 "32668706990" H 12550 5600 50  0001 C CNN "N° Fournisseur"
	1    12550 5600
	1    0    0    -1  
$EndComp
$Comp
L archive:Switch_SW_Push_45deg SW17
U 1 1 5ED7108A
P 12175 5600
F 0 "SW17" H 12175 5750 50  0000 C CNN
F 1 "G77" H 12175 5790 50  0001 C CNN
F 2 "Button_Switch_THT:SW_PUSH-12mm_Wuerth-430476085716" H 12175 5600 50  0001 C CNN
F 3 "~" H 12175 5600 50  0001 C CNN
F 4 "32668706990" H 12175 5600 50  0001 C CNN "N° Fournisseur"
	1    12175 5600
	1    0    0    -1  
$EndComp
$Comp
L archive:Switch_SW_Push_45deg SW10
U 1 1 5ED6ED5B
P 11800 5600
F 0 "SW10" H 11800 5750 50  0000 C CNN
F 1 "G77" H 11800 5790 50  0001 C CNN
F 2 "Button_Switch_THT:SW_PUSH-12mm_Wuerth-430476085716" H 11800 5600 50  0001 C CNN
F 3 "~" H 11800 5600 50  0001 C CNN
F 4 "32668706990" H 11800 5600 50  0001 C CNN "N° Fournisseur"
	1    11800 5600
	1    0    0    -1  
$EndComp
$Comp
L archive:Switch_SW_Push_45deg SW3
U 1 1 5ED6B7F2
P 11425 5600
F 0 "SW3" H 11425 5750 50  0000 C CNN
F 1 "G77" H 11425 5790 50  0001 C CNN
F 2 "Button_Switch_THT:SW_PUSH-12mm_Wuerth-430476085716" H 11425 5600 50  0001 C CNN
F 3 "~" H 11425 5600 50  0001 C CNN
F 4 "32668706990" H 11425 5600 50  0001 C CNN "N° Fournisseur"
	1    11425 5600
	1    0    0    -1  
$EndComp
Wire Wire Line
	11325 5250 11325 5500
Connection ~ 11325 5500
Wire Wire Line
	11325 5500 11325 5875
Connection ~ 11325 5875
Wire Wire Line
	11325 5875 11325 6250
Connection ~ 11325 6250
Wire Wire Line
	11325 6250 11325 6625
Connection ~ 11325 6625
Wire Wire Line
	11325 6625 11325 7000
Connection ~ 11325 7000
Wire Wire Line
	11325 7000 11325 7375
Connection ~ 11325 7375
Wire Wire Line
	11325 7375 11325 7750
Wire Wire Line
	11700 7750 11700 7375
Connection ~ 11700 5500
Wire Wire Line
	11700 5500 11700 5250
Connection ~ 11700 5875
Wire Wire Line
	11700 5875 11700 5500
Connection ~ 11700 6250
Wire Wire Line
	11700 6250 11700 5875
Connection ~ 11700 6625
Wire Wire Line
	11700 6625 11700 6250
Connection ~ 11700 7000
Wire Wire Line
	11700 7000 11700 6625
Connection ~ 11700 7375
Wire Wire Line
	11700 7375 11700 7000
Wire Wire Line
	12075 5250 12075 5500
Connection ~ 12075 5500
Wire Wire Line
	12075 5500 12075 5875
Connection ~ 12075 5875
Wire Wire Line
	12075 5875 12075 6250
Connection ~ 12075 6250
Wire Wire Line
	12075 6250 12075 6625
Connection ~ 12075 6625
Wire Wire Line
	12075 6625 12075 7000
Connection ~ 12075 7000
Wire Wire Line
	12075 7000 12075 7375
Connection ~ 12075 7375
Wire Wire Line
	12075 7375 12075 7750
Wire Wire Line
	12450 5250 12450 5500
Connection ~ 12450 5500
Wire Wire Line
	12450 5500 12450 5875
Connection ~ 12450 5875
Wire Wire Line
	12450 5875 12450 6250
Connection ~ 12450 6250
Wire Wire Line
	12450 6250 12450 6625
Connection ~ 12450 6625
Wire Wire Line
	12450 6625 12450 7000
Connection ~ 12450 7000
Wire Wire Line
	12450 7000 12450 7375
Connection ~ 12450 7375
Wire Wire Line
	12450 7375 12450 7750
Wire Wire Line
	12825 5250 12825 5500
Connection ~ 12825 5500
Wire Wire Line
	12825 5500 12825 5875
Connection ~ 12825 5875
Wire Wire Line
	12825 5875 12825 6250
Connection ~ 12825 6250
Wire Wire Line
	12825 6250 12825 6625
Connection ~ 12825 6625
Wire Wire Line
	12825 6625 12825 7000
Connection ~ 12825 7000
Wire Wire Line
	12825 7000 12825 7375
Connection ~ 12825 7375
Wire Wire Line
	12825 7375 12825 7750
Wire Wire Line
	11525 5700 11900 5700
Connection ~ 11900 5700
Wire Wire Line
	11900 5700 12275 5700
Connection ~ 12275 5700
Wire Wire Line
	12275 5700 12650 5700
Connection ~ 12650 5700
Wire Wire Line
	12650 5700 13025 5700
Connection ~ 13025 5700
Wire Wire Line
	13025 5700 13200 5700
Wire Wire Line
	13200 6075 13025 6075
Connection ~ 11900 6075
Wire Wire Line
	11900 6075 11525 6075
Connection ~ 12275 6075
Wire Wire Line
	12275 6075 11900 6075
Connection ~ 12650 6075
Wire Wire Line
	12650 6075 12275 6075
Connection ~ 13025 6075
Wire Wire Line
	13025 6075 12650 6075
Wire Wire Line
	13200 6450 13025 6450
Connection ~ 11900 6450
Wire Wire Line
	11900 6450 11525 6450
Connection ~ 12275 6450
Wire Wire Line
	12275 6450 11900 6450
Connection ~ 12650 6450
Wire Wire Line
	12650 6450 12275 6450
Connection ~ 13025 6450
Wire Wire Line
	13025 6450 12650 6450
Wire Wire Line
	13200 6825 13025 6825
Connection ~ 11900 6825
Wire Wire Line
	11900 6825 11525 6825
Connection ~ 12275 6825
Wire Wire Line
	12275 6825 11900 6825
Connection ~ 12650 6825
Wire Wire Line
	12650 6825 12275 6825
Connection ~ 13025 6825
Wire Wire Line
	13025 6825 12650 6825
Wire Wire Line
	13200 7200 13025 7200
Connection ~ 11900 7200
Wire Wire Line
	11900 7200 11525 7200
Connection ~ 12275 7200
Wire Wire Line
	12275 7200 11900 7200
Connection ~ 12650 7200
Wire Wire Line
	12650 7200 12275 7200
Connection ~ 13025 7200
Wire Wire Line
	13025 7200 12650 7200
Wire Wire Line
	13200 7575 13025 7575
Connection ~ 11900 7575
Wire Wire Line
	11900 7575 11525 7575
Connection ~ 12275 7575
Wire Wire Line
	12275 7575 11900 7575
Connection ~ 12650 7575
Wire Wire Line
	12650 7575 12275 7575
Connection ~ 13025 7575
Wire Wire Line
	13025 7575 12650 7575
Wire Wire Line
	13200 7950 13025 7950
Connection ~ 11900 7950
Wire Wire Line
	11900 7950 11525 7950
Connection ~ 12275 7950
Wire Wire Line
	12275 7950 11900 7950
Connection ~ 12650 7950
Wire Wire Line
	12650 7950 12275 7950
Connection ~ 13025 7950
Wire Wire Line
	13025 7950 12650 7950
Text GLabel 11325 5250 1    50   Input ~ 0
COL1
Text GLabel 11700 5250 1    50   Input ~ 0
COL2
Text GLabel 12075 5250 1    50   Input ~ 0
COL3
Text GLabel 12450 5250 1    50   Input ~ 0
COL4
Text GLabel 12825 5250 1    50   Input ~ 0
COL5
Text GLabel 13200 5700 2    50   Output ~ 0
ROW1
Text GLabel 13200 6075 2    50   Output ~ 0
ROW2
Text GLabel 13200 6450 2    50   Output ~ 0
ROW3
Text GLabel 13200 6825 2    50   Output ~ 0
ROW4
Text GLabel 13200 7200 2    50   Output ~ 0
ROW5
Text GLabel 13200 7575 2    50   Output ~ 0
ROW6
Text GLabel 13200 7950 2    50   Output ~ 0
ROW7
$Comp
L archive:Device_LED D1
U 1 1 5EE077B6
P 8950 5225
F 0 "D1" H 9000 5400 50  0000 R CNN
F 1 "Rouge SMD" H 9175 5325 50  0000 R CNN
F 2 "LED_SMD:LED_1206_3216Metric_ReverseMount_Hole1.8x2.4mm" H 8950 5225 50  0001 C CNN
F 3 "~" H 8950 5225 50  0001 C CNN
F 4 "32828059657" H 8950 5225 50  0001 C CNN "N° Fournisseur"
F 5 "754-1158-1-ND" H 8950 5225 50  0001 C CNN "N° Digikey"
	1    8950 5225
	-1   0    0    -1  
$EndComp
$Comp
L archive:Device_R R5
U 1 1 5EE09872
P 9300 5225
F 0 "R5" V 9125 5175 50  0000 L CNN
F 1 "330[Ω]" V 9200 5075 50  0000 L CNN
F 2 "Resistor_SMD:R_1206_3216Metric_Pad1.42x1.75mm_HandSolder" V 9230 5225 50  0001 C CNN
F 3 "~" H 9300 5225 50  0001 C CNN
F 4 "32859526036" H 9300 5225 50  0001 C CNN "N° Fournisseur"
F 5 "311-330FRCT-ND" H 9300 5225 50  0001 C CNN "N° Digikey"
	1    9300 5225
	0    -1   1    0   
$EndComp
$Comp
L archive:power_GNDD #PWR0122
U 1 1 5EE269D9
P 9500 5225
F 0 "#PWR0122" H 9500 4975 50  0001 C CNN
F 1 "GNDD" H 9504 5070 50  0000 C CNN
F 2 "" H 9500 5225 50  0001 C CNN
F 3 "" H 9500 5225 50  0001 C CNN
	1    9500 5225
	0    -1   1    0   
$EndComp
Text GLabel 8750 5225 0    50   Input ~ 0
COL1
Text GLabel 8750 5600 0    50   Input ~ 0
COL2
Text GLabel 8750 5975 0    50   Input ~ 0
COL3
Text GLabel 8750 6350 0    50   Input ~ 0
COL4
Text GLabel 8750 6725 0    50   Input ~ 0
COL5
Wire Wire Line
	9450 5225 9500 5225
Wire Wire Line
	9150 5225 9100 5225
Wire Wire Line
	8800 5225 8750 5225
$Comp
L archive:Device_LED D2
U 1 1 5EE47013
P 8950 5600
F 0 "D2" H 9000 5775 50  0000 R CNN
F 1 "Rouge SMD" H 9175 5700 50  0000 R CNN
F 2 "LED_SMD:LED_1206_3216Metric_ReverseMount_Hole1.8x2.4mm" H 8950 5600 50  0001 C CNN
F 3 "~" H 8950 5600 50  0001 C CNN
F 4 "32828059657" H 8950 5600 50  0001 C CNN "N° Fournisseur"
F 5 "754-1158-1-ND" H 8950 5600 50  0001 C CNN "N° Digikey"
	1    8950 5600
	-1   0    0    -1  
$EndComp
$Comp
L archive:Device_R R6
U 1 1 5EE47019
P 9300 5600
F 0 "R6" V 9125 5550 50  0000 L CNN
F 1 "330[Ω]" V 9200 5450 50  0000 L CNN
F 2 "Resistor_SMD:R_1206_3216Metric_Pad1.42x1.75mm_HandSolder" V 9230 5600 50  0001 C CNN
F 3 "~" H 9300 5600 50  0001 C CNN
F 4 "32859526036" H 9300 5600 50  0001 C CNN "N° Fournisseur"
F 5 "311-330FRCT-ND" H 9300 5600 50  0001 C CNN "N° Digikey"
	1    9300 5600
	0    -1   1    0   
$EndComp
$Comp
L archive:power_GNDD #PWR0123
U 1 1 5EE4701F
P 9500 5600
F 0 "#PWR0123" H 9500 5350 50  0001 C CNN
F 1 "GNDD" H 9504 5445 50  0000 C CNN
F 2 "" H 9500 5600 50  0001 C CNN
F 3 "" H 9500 5600 50  0001 C CNN
	1    9500 5600
	0    -1   1    0   
$EndComp
Wire Wire Line
	9450 5600 9500 5600
Wire Wire Line
	9150 5600 9100 5600
Wire Wire Line
	8800 5600 8750 5600
$Comp
L archive:Device_LED D3
U 1 1 5EE4D07C
P 8950 5975
F 0 "D3" H 9000 6150 50  0000 R CNN
F 1 "Rouge SMD" H 9175 6075 50  0000 R CNN
F 2 "LED_SMD:LED_1206_3216Metric_ReverseMount_Hole1.8x2.4mm" H 8950 5975 50  0001 C CNN
F 3 "~" H 8950 5975 50  0001 C CNN
F 4 "32828059657" H 8950 5975 50  0001 C CNN "N° Fournisseur"
F 5 "754-1158-1-ND" H 8950 5975 50  0001 C CNN "N° Digikey"
	1    8950 5975
	-1   0    0    -1  
$EndComp
$Comp
L archive:Device_R R7
U 1 1 5EE4D082
P 9300 5975
F 0 "R7" V 9125 5925 50  0000 L CNN
F 1 "330[Ω]" V 9200 5825 50  0000 L CNN
F 2 "Resistor_SMD:R_1206_3216Metric_Pad1.42x1.75mm_HandSolder" V 9230 5975 50  0001 C CNN
F 3 "~" H 9300 5975 50  0001 C CNN
F 4 "32859526036" H 9300 5975 50  0001 C CNN "N° Fournisseur"
F 5 "311-330FRCT-ND" H 9300 5975 50  0001 C CNN "N° Digikey"
	1    9300 5975
	0    -1   1    0   
$EndComp
$Comp
L archive:power_GNDD #PWR0124
U 1 1 5EE4D088
P 9500 5975
F 0 "#PWR0124" H 9500 5725 50  0001 C CNN
F 1 "GNDD" H 9504 5820 50  0000 C CNN
F 2 "" H 9500 5975 50  0001 C CNN
F 3 "" H 9500 5975 50  0001 C CNN
	1    9500 5975
	0    -1   1    0   
$EndComp
Wire Wire Line
	9450 5975 9500 5975
Wire Wire Line
	9150 5975 9100 5975
Wire Wire Line
	8800 5975 8750 5975
$Comp
L archive:Device_LED D4
U 1 1 5EE53C56
P 8950 6350
F 0 "D4" H 9000 6525 50  0000 R CNN
F 1 "Rouge SMD" H 9175 6450 50  0000 R CNN
F 2 "LED_SMD:LED_1206_3216Metric_ReverseMount_Hole1.8x2.4mm" H 8950 6350 50  0001 C CNN
F 3 "~" H 8950 6350 50  0001 C CNN
F 4 "32828059657" H 8950 6350 50  0001 C CNN "N° Fournisseur"
F 5 "754-1158-1-ND" H 8950 6350 50  0001 C CNN "N° Digikey"
	1    8950 6350
	-1   0    0    -1  
$EndComp
$Comp
L archive:Device_R R8
U 1 1 5EE53C5C
P 9300 6350
F 0 "R8" V 9125 6300 50  0000 L CNN
F 1 "330[Ω]" V 9200 6200 50  0000 L CNN
F 2 "Resistor_SMD:R_1206_3216Metric_Pad1.42x1.75mm_HandSolder" V 9230 6350 50  0001 C CNN
F 3 "~" H 9300 6350 50  0001 C CNN
F 4 "32859526036" H 9300 6350 50  0001 C CNN "N° Fournisseur"
F 5 "311-330FRCT-ND" H 9300 6350 50  0001 C CNN "N° Digikey"
	1    9300 6350
	0    -1   1    0   
$EndComp
$Comp
L archive:power_GNDD #PWR0125
U 1 1 5EE53C62
P 9500 6350
F 0 "#PWR0125" H 9500 6100 50  0001 C CNN
F 1 "GNDD" H 9504 6195 50  0000 C CNN
F 2 "" H 9500 6350 50  0001 C CNN
F 3 "" H 9500 6350 50  0001 C CNN
	1    9500 6350
	0    -1   1    0   
$EndComp
Wire Wire Line
	9450 6350 9500 6350
Wire Wire Line
	9150 6350 9100 6350
Wire Wire Line
	8800 6350 8750 6350
$Comp
L archive:Device_LED D5
U 1 1 5EE5AB69
P 8950 6725
F 0 "D5" H 9000 6900 50  0000 R CNN
F 1 "Rouge SMD" H 9175 6825 50  0000 R CNN
F 2 "LED_SMD:LED_1206_3216Metric_ReverseMount_Hole1.8x2.4mm" H 8950 6725 50  0001 C CNN
F 3 "~" H 8950 6725 50  0001 C CNN
F 4 "32828059657" H 8950 6725 50  0001 C CNN "N° Fournisseur"
F 5 "754-1158-1-ND" H 8950 6725 50  0001 C CNN "N° Digikey"
	1    8950 6725
	-1   0    0    -1  
$EndComp
$Comp
L archive:Device_R R9
U 1 1 5EE5AB6F
P 9300 6725
F 0 "R9" V 9125 6675 50  0000 L CNN
F 1 "330[Ω]" V 9200 6575 50  0000 L CNN
F 2 "Resistor_SMD:R_1206_3216Metric_Pad1.42x1.75mm_HandSolder" V 9230 6725 50  0001 C CNN
F 3 "~" H 9300 6725 50  0001 C CNN
F 4 "32859526036" H 9300 6725 50  0001 C CNN "N° Fournisseur"
F 5 "311-330FRCT-ND" H 9300 6725 50  0001 C CNN "N° Digikey"
	1    9300 6725
	0    -1   1    0   
$EndComp
$Comp
L archive:power_GNDD #PWR0126
U 1 1 5EE5AB75
P 9500 6725
F 0 "#PWR0126" H 9500 6475 50  0001 C CNN
F 1 "GNDD" H 9504 6570 50  0000 C CNN
F 2 "" H 9500 6725 50  0001 C CNN
F 3 "" H 9500 6725 50  0001 C CNN
	1    9500 6725
	0    -1   1    0   
$EndComp
Wire Wire Line
	9450 6725 9500 6725
Wire Wire Line
	9150 6725 9100 6725
Wire Wire Line
	8800 6725 8750 6725
Wire Notes Line
	1125 2675 1125 1425
Text GLabel 10250 5225 0    50   Input ~ 0
ROW1
Text GLabel 10250 5600 0    50   Input ~ 0
ROW2
Text GLabel 10250 5975 0    50   Input ~ 0
ROW3
Text GLabel 10250 6350 0    50   Input ~ 0
ROW4
Text GLabel 10250 6725 0    50   Input ~ 0
ROW5
Text GLabel 10250 7125 0    50   Input ~ 0
ROW6
Text GLabel 10250 7475 0    50   Input ~ 0
ROW7
$Comp
L archive:Device_LED D6
U 1 1 5EEE9920
P 10450 5225
F 0 "D6" H 10500 5400 50  0000 R CNN
F 1 "Rouge SMD" H 10675 5325 50  0000 R CNN
F 2 "LED_SMD:LED_1206_3216Metric_ReverseMount_Hole1.8x2.4mm" H 10450 5225 50  0001 C CNN
F 3 "~" H 10450 5225 50  0001 C CNN
F 4 "32828059657" H 10450 5225 50  0001 C CNN "N° Fournisseur"
F 5 "754-1158-1-ND" H 10450 5225 50  0001 C CNN "N° Digikey"
	1    10450 5225
	-1   0    0    -1  
$EndComp
$Comp
L archive:Device_R R10
U 1 1 5EEE9926
P 10800 5225
F 0 "R10" V 10625 5175 50  0000 L CNN
F 1 "330[Ω]" V 10700 5075 50  0000 L CNN
F 2 "Resistor_SMD:R_1206_3216Metric_Pad1.42x1.75mm_HandSolder" V 10730 5225 50  0001 C CNN
F 3 "~" H 10800 5225 50  0001 C CNN
F 4 "32859526036" H 10800 5225 50  0001 C CNN "N° Fournisseur"
F 5 "311-330FRCT-ND" H 10800 5225 50  0001 C CNN "N° Digikey"
	1    10800 5225
	0    -1   1    0   
$EndComp
$Comp
L archive:power_GNDD #PWR0127
U 1 1 5EEE992C
P 11000 5225
F 0 "#PWR0127" H 11000 4975 50  0001 C CNN
F 1 "GNDD" H 11004 5070 50  0000 C CNN
F 2 "" H 11000 5225 50  0001 C CNN
F 3 "" H 11000 5225 50  0001 C CNN
	1    11000 5225
	0    -1   1    0   
$EndComp
Wire Wire Line
	10950 5225 11000 5225
Wire Wire Line
	10650 5225 10600 5225
Wire Wire Line
	10300 5225 10250 5225
$Comp
L archive:Device_LED D7
U 1 1 5EEE9935
P 10450 5600
F 0 "D7" H 10500 5775 50  0000 R CNN
F 1 "Rouge SMD" H 10675 5700 50  0000 R CNN
F 2 "LED_SMD:LED_1206_3216Metric_ReverseMount_Hole1.8x2.4mm" H 10450 5600 50  0001 C CNN
F 3 "~" H 10450 5600 50  0001 C CNN
F 4 "32828059657" H 10450 5600 50  0001 C CNN "N° Fournisseur"
F 5 "754-1158-1-ND" H 10450 5600 50  0001 C CNN "N° Digikey"
	1    10450 5600
	-1   0    0    -1  
$EndComp
$Comp
L archive:Device_R R11
U 1 1 5EEE993B
P 10800 5600
F 0 "R11" V 10625 5550 50  0000 L CNN
F 1 "330[Ω]" V 10700 5450 50  0000 L CNN
F 2 "Resistor_SMD:R_1206_3216Metric_Pad1.42x1.75mm_HandSolder" V 10730 5600 50  0001 C CNN
F 3 "~" H 10800 5600 50  0001 C CNN
F 4 "32859526036" H 10800 5600 50  0001 C CNN "N° Fournisseur"
F 5 "311-330FRCT-ND" H 10800 5600 50  0001 C CNN "N° Digikey"
	1    10800 5600
	0    -1   1    0   
$EndComp
$Comp
L archive:power_GNDD #PWR0128
U 1 1 5EEE9941
P 11000 5600
F 0 "#PWR0128" H 11000 5350 50  0001 C CNN
F 1 "GNDD" H 11004 5445 50  0000 C CNN
F 2 "" H 11000 5600 50  0001 C CNN
F 3 "" H 11000 5600 50  0001 C CNN
	1    11000 5600
	0    -1   1    0   
$EndComp
Wire Wire Line
	10950 5600 11000 5600
Wire Wire Line
	10650 5600 10600 5600
Wire Wire Line
	10300 5600 10250 5600
$Comp
L archive:Device_LED D8
U 1 1 5EEE994A
P 10450 5975
F 0 "D8" H 10500 6150 50  0000 R CNN
F 1 "Rouge SMD" H 10675 6075 50  0000 R CNN
F 2 "LED_SMD:LED_1206_3216Metric_ReverseMount_Hole1.8x2.4mm" H 10450 5975 50  0001 C CNN
F 3 "~" H 10450 5975 50  0001 C CNN
F 4 "32828059657" H 10450 5975 50  0001 C CNN "N° Fournisseur"
F 5 "754-1158-1-ND" H 10450 5975 50  0001 C CNN "N° Digikey"
	1    10450 5975
	-1   0    0    -1  
$EndComp
$Comp
L archive:Device_R R12
U 1 1 5EEE9950
P 10800 5975
F 0 "R12" V 10625 5925 50  0000 L CNN
F 1 "330[Ω]" V 10700 5825 50  0000 L CNN
F 2 "Resistor_SMD:R_1206_3216Metric_Pad1.42x1.75mm_HandSolder" V 10730 5975 50  0001 C CNN
F 3 "~" H 10800 5975 50  0001 C CNN
F 4 "32859526036" H 10800 5975 50  0001 C CNN "N° Fournisseur"
F 5 "311-330FRCT-ND" H 10800 5975 50  0001 C CNN "N° Digikey"
	1    10800 5975
	0    -1   1    0   
$EndComp
$Comp
L archive:power_GNDD #PWR0129
U 1 1 5EEE9956
P 11000 5975
F 0 "#PWR0129" H 11000 5725 50  0001 C CNN
F 1 "GNDD" H 11004 5820 50  0000 C CNN
F 2 "" H 11000 5975 50  0001 C CNN
F 3 "" H 11000 5975 50  0001 C CNN
	1    11000 5975
	0    -1   1    0   
$EndComp
Wire Wire Line
	10950 5975 11000 5975
Wire Wire Line
	10650 5975 10600 5975
Wire Wire Line
	10300 5975 10250 5975
$Comp
L archive:Device_LED D9
U 1 1 5EEE995F
P 10450 6350
F 0 "D9" H 10500 6525 50  0000 R CNN
F 1 "Rouge SMD" H 10675 6450 50  0000 R CNN
F 2 "LED_SMD:LED_1206_3216Metric_ReverseMount_Hole1.8x2.4mm" H 10450 6350 50  0001 C CNN
F 3 "~" H 10450 6350 50  0001 C CNN
F 4 "32828059657" H 10450 6350 50  0001 C CNN "N° Fournisseur"
F 5 "754-1158-1-ND" H 10450 6350 50  0001 C CNN "N° Digikey"
	1    10450 6350
	-1   0    0    -1  
$EndComp
$Comp
L archive:Device_R R13
U 1 1 5EEE9965
P 10800 6350
F 0 "R13" V 10625 6300 50  0000 L CNN
F 1 "330[Ω]" V 10700 6200 50  0000 L CNN
F 2 "Resistor_SMD:R_1206_3216Metric_Pad1.42x1.75mm_HandSolder" V 10730 6350 50  0001 C CNN
F 3 "~" H 10800 6350 50  0001 C CNN
F 4 "32859526036" H 10800 6350 50  0001 C CNN "N° Fournisseur"
F 5 "311-330FRCT-ND" H 10800 6350 50  0001 C CNN "N° Digikey"
	1    10800 6350
	0    -1   1    0   
$EndComp
$Comp
L archive:power_GNDD #PWR0130
U 1 1 5EEE996B
P 11000 6350
F 0 "#PWR0130" H 11000 6100 50  0001 C CNN
F 1 "GNDD" H 11004 6195 50  0000 C CNN
F 2 "" H 11000 6350 50  0001 C CNN
F 3 "" H 11000 6350 50  0001 C CNN
	1    11000 6350
	0    -1   1    0   
$EndComp
Wire Wire Line
	10950 6350 11000 6350
Wire Wire Line
	10650 6350 10600 6350
Wire Wire Line
	10300 6350 10250 6350
$Comp
L archive:Device_LED D10
U 1 1 5EEE9974
P 10450 6725
F 0 "D10" H 10500 6900 50  0000 R CNN
F 1 "Rouge SMD" H 10675 6825 50  0000 R CNN
F 2 "LED_SMD:LED_1206_3216Metric_ReverseMount_Hole1.8x2.4mm" H 10450 6725 50  0001 C CNN
F 3 "~" H 10450 6725 50  0001 C CNN
F 4 "32828059657" H 10450 6725 50  0001 C CNN "N° Fournisseur"
F 5 "754-1158-1-ND" H 10450 6725 50  0001 C CNN "N° Digikey"
	1    10450 6725
	-1   0    0    -1  
$EndComp
$Comp
L archive:Device_R R14
U 1 1 5EEE997A
P 10800 6725
F 0 "R14" V 10625 6675 50  0000 L CNN
F 1 "330[Ω]" V 10700 6575 50  0000 L CNN
F 2 "Resistor_SMD:R_1206_3216Metric_Pad1.42x1.75mm_HandSolder" V 10730 6725 50  0001 C CNN
F 3 "~" H 10800 6725 50  0001 C CNN
F 4 "32859526036" H 10800 6725 50  0001 C CNN "N° Fournisseur"
F 5 "311-330FRCT-ND" H 10800 6725 50  0001 C CNN "N° Digikey"
	1    10800 6725
	0    -1   1    0   
$EndComp
$Comp
L archive:power_GNDD #PWR0131
U 1 1 5EEE9980
P 11000 6725
F 0 "#PWR0131" H 11000 6475 50  0001 C CNN
F 1 "GNDD" H 11004 6570 50  0000 C CNN
F 2 "" H 11000 6725 50  0001 C CNN
F 3 "" H 11000 6725 50  0001 C CNN
	1    11000 6725
	0    -1   1    0   
$EndComp
Wire Wire Line
	10950 6725 11000 6725
Wire Wire Line
	10650 6725 10600 6725
Wire Wire Line
	10300 6725 10250 6725
Wire Wire Line
	10300 7125 10250 7125
Wire Wire Line
	10300 7475 10250 7475
Wire Wire Line
	10650 7475 10600 7475
Wire Wire Line
	10950 7475 11000 7475
$Comp
L archive:power_GNDD #PWR0132
U 1 1 5EEF8C96
P 11000 7475
F 0 "#PWR0132" H 11000 7225 50  0001 C CNN
F 1 "GNDD" H 11004 7320 50  0000 C CNN
F 2 "" H 11000 7475 50  0001 C CNN
F 3 "" H 11000 7475 50  0001 C CNN
	1    11000 7475
	0    -1   1    0   
$EndComp
$Comp
L archive:Device_R R16
U 1 1 5EEF8C90
P 10800 7475
F 0 "R16" V 10625 7425 50  0000 L CNN
F 1 "330[Ω]" V 10700 7325 50  0000 L CNN
F 2 "Resistor_SMD:R_1206_3216Metric_Pad1.42x1.75mm_HandSolder" V 10730 7475 50  0001 C CNN
F 3 "~" H 10800 7475 50  0001 C CNN
F 4 "32859526036" H 10800 7475 50  0001 C CNN "N° Fournisseur"
F 5 "311-330FRCT-ND" H 10800 7475 50  0001 C CNN "N° Digikey"
	1    10800 7475
	0    -1   1    0   
$EndComp
$Comp
L archive:Device_LED D12
U 1 1 5EEF8C8A
P 10450 7475
F 0 "D12" H 10500 7650 50  0000 R CNN
F 1 "Rouge SMD" H 10675 7575 50  0000 R CNN
F 2 "LED_SMD:LED_1206_3216Metric_ReverseMount_Hole1.8x2.4mm" H 10450 7475 50  0001 C CNN
F 3 "~" H 10450 7475 50  0001 C CNN
F 4 "32828059657" H 10450 7475 50  0001 C CNN "N° Fournisseur"
F 5 "754-1158-1-ND" H 10450 7475 50  0001 C CNN "N° Digikey"
	1    10450 7475
	-1   0    0    -1  
$EndComp
Wire Wire Line
	10650 7125 10600 7125
Wire Wire Line
	10950 7125 11000 7125
$Comp
L archive:power_GNDD #PWR0133
U 1 1 5EEF8C81
P 11000 7125
F 0 "#PWR0133" H 11000 6875 50  0001 C CNN
F 1 "GNDD" H 11004 6970 50  0000 C CNN
F 2 "" H 11000 7125 50  0001 C CNN
F 3 "" H 11000 7125 50  0001 C CNN
	1    11000 7125
	0    -1   1    0   
$EndComp
$Comp
L archive:Device_R R15
U 1 1 5EEF8C7B
P 10800 7125
F 0 "R15" V 10625 7075 50  0000 L CNN
F 1 "330[Ω]" V 10700 6975 50  0000 L CNN
F 2 "Resistor_SMD:R_1206_3216Metric_Pad1.42x1.75mm_HandSolder" V 10730 7125 50  0001 C CNN
F 3 "~" H 10800 7125 50  0001 C CNN
F 4 "32859526036" H 10800 7125 50  0001 C CNN "N° Fournisseur"
F 5 "311-330FRCT-ND" H 10800 7125 50  0001 C CNN "N° Digikey"
	1    10800 7125
	0    -1   1    0   
$EndComp
$Comp
L archive:Device_LED D11
U 1 1 5EEF8C75
P 10450 7125
F 0 "D11" H 10500 7300 50  0000 R CNN
F 1 "Rouge SMD" H 10675 7225 50  0000 R CNN
F 2 "LED_SMD:LED_1206_3216Metric_ReverseMount_Hole1.8x2.4mm" H 10450 7125 50  0001 C CNN
F 3 "~" H 10450 7125 50  0001 C CNN
F 4 "32828059657" H 10450 7125 50  0001 C CNN "N° Fournisseur"
F 5 "754-1158-1-ND" H 10450 7125 50  0001 C CNN "N° Digikey"
	1    10450 7125
	-1   0    0    -1  
$EndComp
Wire Notes Line
	13500 8050 13500 4975
Text Notes 8450 4975 0    100  ~ 0
Affichage Clavier
Wire Notes Line
	1125 1425 4075 1425
Text Notes 8450 7125 0    50   ~ 0
Enclenchement /\nDéclenchement\nAffichage Clavier
Wire Notes Line
	9175 7125 8450 7125
$Comp
L archive:power_GNDD #PWR0134
U 1 1 5EE61D48
P 9025 7425
F 0 "#PWR0134" H 9025 7175 50  0001 C CNN
F 1 "GNDD" H 9029 7270 50  0000 C CNN
F 2 "" H 9025 7425 50  0001 C CNN
F 3 "" H 9025 7425 50  0001 C CNN
	1    9025 7425
	1    0    0    -1  
$EndComp
$Comp
L archive:Jumper_SolderJumper_2_Open JP2
U 1 1 5EE6302C
P 8800 7350
F 0 "JP2" H 8800 7525 50  0000 C CNN
F 1 "Jumper à souder" H 8800 7450 50  0000 C CNN
F 2 "Jumper:SolderJumper-2_P1.3mm_Open_TrianglePad1.0x1.5mm" H 8800 7350 50  0001 C CNN
F 3 "~" H 8800 7350 50  0001 C CNN
	1    8800 7350
	1    0    0    -1  
$EndComp
Wire Wire Line
	8575 7425 8575 7350
Wire Wire Line
	8575 7350 8650 7350
$Comp
L archive:power_GND #PWR0135
U 1 1 5EE7292E
P 8575 7425
F 0 "#PWR0135" H 8575 7175 50  0001 C CNN
F 1 "GND" H 8580 7252 50  0000 C CNN
F 2 "" H 8575 7425 50  0001 C CNN
F 3 "" H 8575 7425 50  0001 C CNN
	1    8575 7425
	1    0    0    -1  
$EndComp
Wire Wire Line
	9025 7425 9025 7350
Wire Wire Line
	9025 7350 8950 7350
Wire Notes Line
	9175 7125 9175 7650
Text Notes 11250 4975 0    100  ~ 0
Clavier
$Bitmap
Pos 14650 6525
Scale 0.700000
Data
89 50 4E 47 0D 0A 1A 0A 00 00 00 0D 49 48 44 52 00 00 03 C4 00 00 05 04 08 02 00 00 00 95 F6 4E 
2E 00 00 00 03 73 42 49 54 08 08 08 DB E1 4F E0 00 00 20 00 49 44 41 54 78 9C EC DD 7B 5C 4C F9 
FF 07 F0 CF 28 92 E4 92 6F 4B 2C 09 49 2C B9 6E 74 71 4D AC CE 68 73 5B B9 54 42 D2 CD FD 52 C8 
12 B9 E4 5A 44 25 45 92 55 24 33 EC 16 4B 54 08 B1 58 9B 44 84 B6 12 91 54 2E 53 F3 FB E3 EC 9E 
DF 6C C8 34 CD CC 99 99 5E CF C7 3E 1E 7B E6 CC B9 BC 72 BA BC E7 9C CF 85 43 00 00 00 00 00 A0 
96 84 42 21 21 A4 01 DB 31 00 00 00 00 00 94 95 BA E8 0B 1E 8F 47 51 14 5B 51 40 16 38 1C 0E F9 
F7 93 13 A8 1E 5C 5F D5 86 EB AB DA 70 7D 55 1B AE AF 6A A3 AF 2F ED 9F 3B D3 1E 1E 1E 84 10 2E 
97 7B EA D4 29 76 42 01 00 00 00 00 28 9B 7F 8A E9 A0 A0 20 77 77 77 42 08 45 51 A7 4F 9F 66 35 
12 00 00 00 00 80 72 F8 FF 36 D3 BB 76 ED 72 73 73 23 84 50 14 F5 EB AF BF B2 17 09 00 00 00 00 
40 39 FC A7 03 E2 EE DD BB 5D 5D 5D 85 42 21 97 CB 4D 4C 4C 64 2B 13 00 00 00 00 80 52 A8 3E 9A 
C7 9E 3D 7B E6 CC 99 53 59 59 49 51 54 52 52 12 2B 99 00 00 00 00 00 94 C2 67 86 C6 DB BB 77 AF 
8B 8B 8B 40 20 A0 28 EA CC 99 33 F2 CF 04 00 00 00 00 A0 14 3E 3F CE 74 48 48 C8 EC D9 B3 3F 7E 
FC 48 51 D4 D9 B3 67 E5 9C 09 00 00 00 00 40 29 7C 71 D2 96 D0 D0 D0 99 33 67 7E F8 F0 81 CB E5 
9E 3B 77 4E 9E 99 00 00 00 00 00 94 42 4D 33 20 EE DB B7 CF D9 D9 F9 DD BB 77 14 45 9D 3F 7F 5E 
6E 99 00 00 00 00 00 94 C2 57 A6 13 0F 0F 0F 9F 31 63 46 45 45 05 45 51 C9 C9 C9 72 89 04 00 00 
00 00 A0 1C BE 52 4C 13 42 F6 EF DF EF E4 E4 54 5E 5E 4E 51 D4 85 0B 17 E4 90 09 00 00 00 00 40 
29 7C BD 98 26 84 44 44 44 38 38 38 94 95 95 71 B9 DC 94 94 14 59 67 02 00 00 00 00 50 0A 62 15 
D3 84 90 03 07 0E 4C 9F 3E BD B4 B4 94 A2 A8 D4 D4 54 99 66 02 00 00 00 00 50 0A E2 16 D3 84 90 
83 07 0F 4E 9B 36 ED CD 9B 37 14 45 A5 A5 A5 C9 2E 13 00 00 00 00 80 52 A8 45 31 4D 08 89 8A 8A 
9A 32 65 4A 49 49 09 45 51 97 2F 5F 96 51 26 00 00 00 00 00 A5 50 BB 62 9A 10 12 1D 1D 6D 6F 6F 
FF FA F5 6B 8A A2 AE 5C B9 22 8B 4C 00 00 00 00 00 4A A1 D6 C5 34 21 E4 F0 E1 C3 93 27 4F 2E 2E 
2E A6 28 2A 3D 3D 5D EA 99 00 00 00 00 00 94 82 24 C5 34 21 24 26 26 E6 A7 9F 7E 7A F9 F2 25 45 
51 57 AF 5E 95 6E 26 00 00 00 00 00 A5 20 61 31 4D 08 39 72 E4 C8 C4 89 13 5F BC 78 41 51 D4 F5 
EB D7 A5 98 09 00 00 00 00 40 29 48 5E 4C 13 42 8E 1E 3D 3A 61 C2 84 A2 A2 22 8A A2 32 32 32 A4 
95 09 00 00 00 00 40 29 D4 A9 98 26 84 C4 C6 C6 8E 1F 3F BE B0 B0 90 A2 A8 1B 37 6E 48 25 13 00 
00 00 00 80 52 A8 6B 31 4D 08 89 8B 8B 1B 37 6E 5C 41 41 01 45 51 37 6F DE AC FB 01 01 00 00 00 
00 94 82 14 8A 69 42 C8 B1 63 C7 7E FC F1 C7 FC FC 7C 2E 97 7B EB D6 2D A9 1C 13 00 00 00 00 40 
C1 49 A7 98 26 84 C4 C7 C7 DB DA DA E6 E5 E5 51 14 75 FB F6 6D 69 1D 16 00 00 00 00 40 61 49 AD 
98 26 84 9C 38 71 62 EC D8 B1 CF 9E 3D A3 28 EA CE 9D 3B 52 3C 32 00 00 00 00 80 02 92 66 31 4D 
08 49 48 48 E0 72 B9 4F 9F 3E A5 28 EA CF 3F FF 94 EE C1 01 00 00 00 00 14 8A 94 8B 69 42 C8 C9 
93 27 6D 6C 6C 9E 3C 79 C2 E5 72 FF FA EB 2F A9 1F 1F 00 00 00 00 40 41 48 BF 98 26 84 F0 F9 FC 
31 63 C6 3C 7E FC 98 A2 A8 CC CC 4C 59 9C 02 00 00 00 00 80 75 32 29 A6 09 21 7C 3E FF 87 1F 7E 
78 F4 E8 11 45 51 F7 EE DD 93 D1 59 00 00 00 00 00 58 24 AB 62 9A C3 E1 F0 78 BC D1 A3 47 E7 E4 
E4 50 14 95 95 95 25 A3 13 01 00 00 00 00 B0 45 56 C5 34 21 44 4D 4D 8D C7 E3 59 5B 5B 3F 7C F8 
90 CB E5 66 67 67 CB EE 5C 00 00 00 00 00 F2 27 C3 62 9A 10 A2 AE AE CE E7 F3 47 8E 1C 99 9D 9D 
4D 51 D4 83 07 0F 64 7A 3A 00 00 00 00 00 79 92 6D 31 4D 08 69 D8 B0 21 9F CF B7 B2 B2 BA 7F FF 
3E 45 51 0F 1F 3E 94 F5 19 01 00 00 00 00 E4 43 E6 C5 34 21 A4 51 A3 46 3C 1E 6F F8 F0 E1 59 59 
59 14 45 E5 E4 E4 C8 E1 A4 00 00 00 00 00 B2 26 8F 62 9A 10 D2 B8 71 63 3E 9F 3F 6C D8 B0 7B F7 
EE 71 B9 DC C7 8F 1F CB E7 BC 00 00 00 00 00 B2 23 A7 62 9A 10 A2 A9 A9 C9 E7 F3 87 0E 1D FA D7 
5F 7F 51 14 95 9B 9B 2B B7 53 03 00 00 00 00 C8 82 FC 8A 69 42 48 93 26 4D F8 7C FE 90 21 43 EE 
DE BD 4B 51 D4 93 27 4F E4 79 76 00 00 00 00 00 E9 92 6B 31 4D 08 D1 D2 D2 E2 F1 78 96 96 96 7F 
FE F9 27 97 CB 7D F6 EC 99 9C 03 00 00 00 00 00 48 8B BC 8B 69 42 88 B6 B6 36 9F CF B7 B0 B0 B8 
7D FB 36 45 51 79 79 79 F2 CF 00 00 00 00 00 50 77 2C 14 D3 84 90 66 CD 9A F1 F9 7C 73 73 F3 5B 
B7 6E 51 14 F5 F7 DF 7F B3 12 03 00 00 00 00 A0 2E D8 29 A6 09 21 CD 9B 37 E7 F3 F9 66 66 66 7F 
FC F1 07 45 51 F9 F9 F9 6C 25 01 00 00 00 00 90 0C 6B C5 34 21 A4 45 8B 16 3C 1E 6F E0 C0 81 37 
6F DE E4 72 B9 85 85 85 2C 86 01 00 00 00 00 A8 2D 36 8B 69 42 88 8E 8E 0E 9F CF 37 35 35 CD C8 
C8 A0 28 EA F9 F3 E7 EC E6 01 00 00 00 00 10 1F CB C5 34 21 A4 55 AB 56 7C 3E FF FB EF BF BF 7E 
FD 3A 45 51 45 45 45 6C 27 02 00 00 00 00 10 0B FB C5 34 21 E4 7F FF FB 1F 8F C7 1B 30 60 C0 B5 
6B D7 28 8A 7A F1 E2 05 DB 89 00 00 00 00 00 BE 4E 21 8A 69 42 C8 37 DF 7C C3 E3 F1 FA F5 EB 77 
F5 EA 55 2E 97 5B 5C 5C CC 76 22 00 00 00 00 80 AF 50 94 62 9A 10 D2 BA 75 6B 3E 9F DF B7 6F DF 
2B 57 AE 50 14 F5 EA D5 2B B6 13 01 00 00 00 00 D4 44 81 8A 69 42 48 9B 36 6D F8 7C 7E 9F 3E 7D 
2E 5F BE 4C 51 D4 EB D7 AF D9 4E 04 00 00 00 00 F0 45 8A 55 4C 13 42 F4 F4 F4 78 3C 5E EF DE BD 
2F 5D BA 44 51 54 49 49 09 DB 89 00 00 00 00 00 3E 4F E1 8A 69 42 48 BB 76 ED 78 3C 5E AF 5E BD 
D2 D2 D2 B8 5C 6E 69 69 29 DB 89 00 00 00 00 00 3E 43 11 8B 69 42 C8 B7 DF 7E CB E7 F3 7B F6 EC 
99 92 92 42 51 D4 DB B7 6F D9 4E 04 00 00 00 00 50 9D 82 16 D3 84 90 F6 ED DB F3 F9 FC EF BE FB 
EE E2 C5 8B 14 45 95 95 95 B1 9D 08 00 00 00 00 E0 3F 14 B7 98 26 84 74 E8 D0 81 C7 E3 75 EF DE 
FD C2 85 0B 14 45 95 97 97 B3 9D 08 00 00 00 00 E0 FF 29 74 31 4D 08 E9 D8 B1 23 9F CF 37 36 36 
4E 4E 4E E6 72 B9 EF DE BD 63 3B 11 00 00 00 00 C0 3F 14 BD 98 26 84 18 18 18 F0 F9 FC 6E DD BA 
9D 3B 77 8E A2 A8 F7 EF DF B3 9D 08 00 00 00 00 80 10 A5 28 A6 09 21 9D 3A 75 E2 F3 F9 46 46 46 
BF FF FE 3B 45 51 1F 3E 7C 60 3B 11 28 AE E7 CF 9F DB DA DA 72 38 1C 0E 87 E3 E7 E7 C7 76 1C 90 
90 50 28 2C 2C 2C 3C 7E 3C 7E D1 E2 C5 14 97 DB CD B8 BB 41 A7 CE 06 9D 3A 1B 76 35 1A FD C3 98 
45 8B 17 1F 3F 1E 5F 58 58 28 14 0A D9 4E 0A 92 A8 AA AA CA CC CC DC B1 63 87 9D 9D 5D B7 6E DD 
E8 1F D8 56 AD 5A 0D 1F 3E DC C7 C7 27 39 39 B9 A2 A2 82 ED 8C 20 13 42 A1 70 E7 CE 9D 9C 7F 8D 
1E 3D FA E5 CB 97 6C 87 02 B1 3C 78 F0 A0 7F FF FE 9C 3A 48 4B 4B 63 FB 8B 90 09 75 B6 03 88 AB 
73 E7 CE 3C 1E CF C6 C6 E6 EC D9 B3 5C 2E 97 CF E7 37 6C D8 90 ED 50 A0 70 2A 2B 2B 0F 1C 38 70 
F2 E4 49 B6 83 80 E4 AA AA AA D2 D2 D2 82 76 ED BE 76 ED DA A7 EF 0A 04 82 AC AC AC AC AC AC E3 
C7 E3 09 21 C3 87 0D 5B B0 60 41 8F 1E DD 39 1C 8E DC 93 82 24 AA AA AA 2E 5C B8 B0 69 D3 A6 C4 
C4 C4 6A 6F 15 17 17 9F 3F 7F FE FC F9 F3 1B 36 6C D0 D7 D7 77 71 71 99 3D 7B B6 AE AE 2E 2B 39 
41 46 2E 5E BC B8 7D FB 76 B6 53 80 24 FE FE FB EF 8C 8C 0C B6 53 28 22 E5 B8 33 4D 33 34 34 E4 
F3 F9 5D BA 74 49 4A 4A E2 72 B9 95 95 95 6C 27 02 85 93 9A 9A BA 7B F7 6E B6 53 80 E4 F2 F2 F2 
E6 BA B9 39 38 3A 7D B6 92 FE D4 B9 F3 E7 ED C6 8D F3 5B B7 0E 03 68 2A 85 E2 E2 62 4F 4F CF E1 
C3 87 7F 5A 49 57 93 9B 9B BB 62 C5 0A 4B 4B CB B8 B8 B8 AA AA 2A F9 C4 03 59 2B 28 28 08 08 08 
C8 CD CD 65 3B 08 48 E2 F1 E3 C7 6C 47 50 50 CA 54 4C 13 42 BA 76 ED CA E7 F3 3B 77 EE 9C 98 98 
48 51 14 7E C3 82 A8 8C 8C 8C 65 CB 96 E1 D7 B4 F2 BA 77 EF DE 74 07 C7 A4 A4 33 B5 DA 4B 20 10 
44 44 44 BA B9 7B 3C 7F FE 5C 46 C1 40 2A 0A 0B 0B 9D 9D 9D 83 83 83 C5 DF 25 2B 2B CB D9 D9 79 
EB D6 AD 02 81 40 76 C1 40 3E 2A 2A 2A D6 AF 5F 7F EA D4 29 B6 83 80 24 2A 2B 2B EF DD BB C7 76 
0A 05 A5 64 C5 34 21 C4 C8 C8 88 CF E7 77 EA D4 E9 B7 DF 7E A3 28 0A 2D 26 81 96 91 91 E1 EE EE 
9E 9E 9E CE 76 10 90 D0 FD EC 6C 37 77 8F 47 8F 1E 49 B6 7B 4A 4A CA A6 CD 9B 31 80 A6 C2 7A F5 
EA 95 A7 A7 67 42 42 42 6D 77 2C 2D 2D F5 F3 F3 3B 7A F4 28 7E DB 2B 35 A1 50 18 1F 1F 7F E0 C0 
01 B6 83 80 84 DE BE 7D 9B 9D 9D CD 76 0A 05 A5 7C C5 34 21 A4 5B B7 6E 3C 1E AF 63 C7 8E BF FE 
FA 2B 97 CB 65 3B 0E B0 4C 28 14 A6 A5 A5 CD 9C 39 13 95 B4 F2 2A 2F 2F 0F 09 09 F9 B4 92 36 32 
32 DA B8 C1 3F 2D 35 E5 7E D6 BD 47 39 0F 1F E5 3C FC EB EE 9F BF 9E 3E E5 E5 E5 F9 69 53 DA E3 
C7 E3 F7 ED 0B 17 A0 01 98 E2 A9 AC AC DC B7 6F 5F 6C 6C 6C B5 F5 A3 46 8D 4A 48 48 78 FE FC 79 
65 65 A5 50 28 FC F8 F1 E3 D3 A7 4F F7 ED DB D7 B3 67 4F D1 CD 4A 4B 4B 7D 7C 7C D0 58 53 A9 65 
64 64 F8 F8 F8 94 96 96 B2 1D 04 24 54 54 54 24 FA 2B DA CA CA EA F9 F3 E7 C2 5A 32 37 37 67 F1 
4B 90 1D A5 2C A6 09 21 DD BB 77 E7 F3 F9 FA FA FA A7 4E 9D 42 3D 5D 9F 09 04 82 98 98 98 A9 53 
A7 DE BA 75 8B ED 2C 20 B9 E4 E4 E4 93 27 79 A2 6B 34 34 34 FC FC D6 9E 4C 38 F1 D3 4F 3F B5 6D 
DB 96 E9 70 AC A9 A9 D9 AD 5B B7 05 F3 E7 9F FB FD AC 83 83 43 B5 E3 1C 8E 89 B9 97 89 07 91 0A 
E7 EE DD BB 11 11 11 A2 6B 74 74 74 F6 EF DF 9F 90 90 30 76 EC 58 5D 5D DD 06 0D 1A 10 42 D4 D5 
D5 BF FD F6 DB 99 33 67 A6 A5 A5 2D 5F BE 5C 74 FB DC DC DC A8 A8 28 0C 8D AA A4 0A 0B 0B D7 AD 
5B 87 36 78 4A AD 5A EF C3 CE 9D 3B 37 6D DA 94 C5 3C 0A 45 59 8B 69 42 48 8F 1E 3D F8 7C 7E 87 
0E 1D F8 7C FE D8 B1 63 D9 8E 03 2C 28 2A 2A F2 F6 F6 9E 3A 75 2A 7E 47 2B B5 F2 F2 72 1E 8F 2F 
DA 28 B6 79 F3 E6 A1 21 7B A7 4E 99 D2 A8 51 A3 2F ED D5 B4 69 D3 55 AB 56 7A 79 79 8A AE 2C 2C 
2C 4C 48 48 C0 CD 69 85 52 59 59 19 17 17 97 99 99 C9 AC D1 D6 D6 0E 0A 0A 72 72 72 D2 D0 D0 F8 
EC 2E DA DA DA 3F FF FC B3 B7 B7 B7 E8 CA 33 67 CE 3C 78 F0 40 B6 59 41 06 04 02 41 58 58 98 04 
2D 7C 40 A1 54 EB 7D A8 AF AF AF A9 A9 C9 52 16 85 A3 C4 C5 34 21 E4 BB EF BE E3 F1 78 ED DB B7 
E7 F1 78 B6 B6 B6 6C C7 01 F9 A9 AA AA 3A 7B F6 AC 8D 8D CD 96 2D 5B D8 CE 02 75 F5 E8 D1 E3 6B 
D7 AF 8B AE 99 33 C7 C5 D2 D2 F2 AB A3 DD A9 AB A9 CD 71 71 E1 72 29 D1 95 E9 57 AF BE 7C F1 42 
FA 29 41 52 85 85 85 29 29 29 A2 6B 5C 5C 5C C6 8F 1F 5F F3 F5 D5 D0 D0 98 3D 7B B6 A9 A9 29 B3 
26 33 33 F3 CF 3F FF 94 55 4A 90 99 B8 B8 B8 CD 9B 37 33 2F CD CC CC 58 0C 03 92 F9 B4 F7 61 8F 
1E 3D D8 0A A3 80 94 BB 98 26 84 F4 EA D5 8B C7 E3 B5 6B D7 EE E4 C9 93 76 76 76 6C C7 01 99 13 
0A 85 B7 6E DD 9A 36 6D DA C8 91 23 AB 8D 9E 66 6D 6D 8D CF 54 CA E8 EE 5F 77 45 67 6D E8 D1 A3 
FB 8F B6 B6 62 8E 1B DD A4 49 13 47 47 47 2D 2D 2D 66 4D 4E 4E 4E 7E 7E BE F4 53 82 A4 EE DE BD 
9B 9C 9C CC BC D4 D3 D3 9B 34 69 D2 97 EE 49 8B 6A D7 AE 5D B5 C2 EB FE FD FB 52 8F 07 32 45 4F 
CD C3 34 95 9E 38 71 62 B5 06 3C A0 14 AA F5 3E 34 34 34 EC D8 B1 23 7B 71 14 8E D2 17 D3 84 10 
13 13 13 3E 9F DF B6 6D DB 13 27 4E 8C 1B 37 8E ED 38 20 43 05 05 05 33 66 CC E8 DD BB 77 4C 4C 
4C B5 B7 9C 9D 9D 0F 1C 38 D0 AF 5F 3F 56 82 81 C4 84 42 E1 83 07 0F 45 D7 F4 EF DF 5F F7 9B 6F 
C4 3F 42 47 7D FD 4E 9D 3A 31 2F CB CA CA 8A 5F BD 92 5A 3E A8 B3 EB FF 7D EC 60 6E 6E 6E 64 64 
24 CE 8E 8D 1A 35 6A D9 B2 A5 6C 42 81 3C BC 79 F3 66 E3 C6 8D 4C D7 70 13 13 93 35 6B D6 E8 E8 
E8 B0 9B 0A 24 50 AD F7 A1 BE BE BE 9E 9E 1E 8B 79 14 8D 2A 14 D3 84 90 DE BD 7B F3 F9 7C 3D 3D 
BD F8 F8 F8 F1 E3 C7 B3 1D 07 64 A5 A4 A4 E4 8F 3F FE A8 B6 D2 C8 C8 28 3A 3A 3A 38 38 B8 4D 9B 
36 AC A4 82 BA 78 F7 EE DD F3 C2 42 D1 35 DD BB 77 57 57 53 13 FF 08 4D 9A 34 E9 64 60 20 BA E6 
05 9A 79 28 92 25 4B 96 3C 7D FA F4 EC D9 B3 9B 36 6D A2 28 AA 57 AF 5E CD 9A 35 63 3B 14 C8 9C 
40 20 D8 B3 67 CF C1 83 07 E9 97 DA DA DA 4B 97 2E ED D6 AD 1B BB A9 40 32 85 85 85 E8 7D 58 03 
A5 99 4E FC AB FA F4 E9 C3 E3 F1 28 8A 3A 7E FC F8 84 09 13 E2 E2 E2 D8 4E 04 F2 E0 E0 E0 B0 66 
CD 1A 3C 6F 52 5E 9A 9A 9A 01 01 9B 17 2C 5C 70 E7 F6 9D 9B 7F DC BC 76 F5 DA 37 BA B5 B8 2D FD 
59 0D D5 55 E7 37 9B 0A A0 C7 E8 F8 F6 DB 6F 47 8C 18 B1 74 E9 52 F1 77 AC A8 A8 C8 CB CB 13 5D 
D3 B5 6B 57 69 A7 03 59 49 4B 4B DB B3 67 0F F3 52 9C 86 F2 A0 B0 1E 3E FC CF F3 43 F4 3E AC 46 
A5 FE E4 F4 EB D7 8F C7 E3 D9 D8 D8 1C 3B 76 6C D2 A4 49 47 8F 1E 65 3B 11 C8 90 9D 9D DD CA 95 
2B FB F4 E9 83 DF CE CA AE 61 C3 86 FA 1D 3A E8 77 E8 40 51 36 12 EC 5E 5E 5E 9E F3 DF 01 AA DB 
B6 6D 2B A5 68 C0 A6 EC EC EC 8B 17 2F 32 2F 8D 8D 8D BF FB EE 3B 16 F3 80 F8 B2 B3 B3 45 E7 A3 
B5 B5 B5 5D B2 64 89 38 0D E5 41 01 A1 F7 E1 57 A9 48 33 0F 46 FF FE FD F9 7C BE AE AE 6E 6C 6C 
EC 4F 3F FD C4 76 1C 90 09 3B 3B BB 94 94 94 B8 B8 B8 BE 7D FB A2 92 86 C7 B9 B9 39 39 39 CC 4B 
FD 0E 1D BE A9 4D 93 6B 50 4C 85 85 85 BE BE BE A2 03 EA 8D 19 33 A6 4B 97 2E 2C 46 02 31 95 95 
95 ED D8 B1 83 69 2A AD AF AF BF 60 C1 82 D6 AD 5B B3 9B 0A 24 F6 A5 DE 87 42 A1 B0 A0 A0 20 3C 
3C DC DE DE BE 5B B7 6E 1C 0E 87 C3 E1 74 EB D6 CD CE CE 6E C7 8E 1D 99 99 99 55 55 55 AC 85 96 
2F 95 BA 33 4D 1B 30 60 00 9F CF B7 B1 B1 39 7A F4 28 87 C3 39 72 E4 08 DB 89 40 6A DA B6 6D 7B 
FA F4 69 3D 3D 3D D4 D0 40 13 54 56 FE F6 EB 6F 65 65 65 CC 1A 63 63 63 FC D9 56 6A 55 55 55 97 
2E 5D F2 F3 F3 4B 4A 4A 62 56 9A 9A 9A CE 99 33 07 B7 36 15 9F 50 28 3C 7C F8 70 70 70 30 B3 66 
C1 82 05 83 07 0F 66 31 12 D4 D1 A7 BD 0F DB B4 69 93 99 99 19 10 10 10 17 17 57 6D 56 CB AC AC 
AC AC AC AC 13 27 4E 10 42 2C 2D 2D 7D 7D 7D 87 0F 1F 4E CF CA A4 C2 54 F3 CB FB FE FB EF 79 3C 
9E 8E 8E CE 2F BF FC 62 6F 6F CF 76 1C 90 1A 6D 6D ED B6 6D DB A2 92 06 C6 BD CC 7B 3C 3E 5F 74 
CD 98 31 63 9A 34 69 C2 56 1E 90 98 40 20 78 F6 EC 59 54 54 D4 D0 A1 43 2D 2D 2D 45 2B 69 23 23 
A3 CD 9B 37 1B 1A 1A B2 18 0F C4 74 F1 E2 C5 F5 EB D7 33 2F DD DC DC 66 CD 9A 85 5F DA 4A AD 5A 
EF 43 5D 5D DD 3D 7B F6 98 9A 9A 46 44 44 D4 3C 3F 7C 4A 4A CA C8 91 23 67 CF 9E 5D 50 50 20 FB 
98 6C 52 C1 3B D3 B4 81 03 07 D2 F7 A7 8F 1C 39 D2 A0 41 83 E8 E8 68 B6 13 01 80 94 95 96 96 06 
ED 0A 2A 14 19 0C A4 67 CF 9E DF 7F 3F 80 C5 48 50 5B F7 EE DD 9B 34 69 D2 9D 3B 77 BE B4 01 45 
51 01 01 01 18 05 42 29 14 16 16 6E DF BE 9D 69 2A 6D 6A 6A EA E1 E1 21 3A 0C 3C 28 A3 6A BD 0F 
3F 1D 9A B6 66 FB F7 EF CF CA CA 0A 0F 0F 17 73 4C 4C 65 A4 9A 77 A6 69 83 06 0D E2 F3 F9 2D 5A 
B4 38 7C F8 F0 B4 69 D3 D8 8E 03 00 D2 24 A8 AC DC 17 1E 9E 94 74 86 59 A3 AE AE EE E4 E8 88 36 
1E CA E5 E5 CB 97 5F AA A4 F5 F4 F4 0E 1C 38 10 17 17 87 4A 5A 29 BC 7F FF 3E 20 20 80 99 36 5C 
5B 5B DB DB DB DB D8 D8 98 DD 54 50 47 9F F6 3E 94 40 5A 5A 9A A3 A3 A3 68 17 08 15 A3 CA C5 34 
21 C4 CC CC 8C CF E7 37 6F DE 3C 3A 3A 7A FA F4 E9 6C C7 01 00 E9 10 54 56 46 EC DF 1F 1C BC 47 
74 E5 D8 B1 DC D1 A3 47 B1 15 09 24 F3 EC D9 B3 2F BD 95 9F 9F EF EB EB EB ED ED 9D 93 93 23 14 
0A E5 99 0A 6A 4B 28 14 1E 3B 76 2C 34 34 94 59 B3 62 C5 0A 1B 1B 49 C6 E7 01 85 52 AD F7 21 C3 
D2 D2 32 32 32 32 27 27 A7 BC BC 5C F8 AF D2 D2 D2 9C 9C 9C C8 C8 48 4B 4B CB 6A DB A7 A7 A7 AF 
5E BD FA 95 8A CE A8 A5 E2 C5 34 21 C4 DC DC 9C C7 E3 69 6B 6B 1F 3A 74 C8 D1 D1 91 ED 38 00 50 
57 82 CA CA 98 98 98 CD 01 5B 04 02 01 B3 D2 D4 D4 74 D9 D2 A5 68 2D AD 74 5E BF 7E 5D C3 BB B9 
B9 B9 DB B7 6F EF DD BB F7 CA 95 2B 6B 6E 9D 09 EC BA 77 EF DE E6 CD 9B 99 6B 64 6B 6B EB E4 E4 
A4 8E 11 DF 95 5F B5 DE 87 E4 DF 89 D2 CE 9C 39 E3 E8 E8 68 60 60 20 3A E0 74 D3 A6 4D 0D 0C 0C 
1C 1D 1D CF 9C 39 13 15 15 A5 AF AF 2F BA 63 6C 6C 6C 5C 5C 9C 4A 7E 30 AE 17 DF E8 96 96 96 74 
FB E9 83 07 0F 72 38 9C C8 C8 48 B6 13 01 80 84 E8 7B D2 D5 2A 69 03 03 83 B5 6B D7 60 44 3C 65 
F4 E6 CD 1B 37 37 B7 BE 7D FB 76 EE DC 99 10 F2 F7 DF 7F A7 A6 A6 9E 3E 7D 9A 69 77 4B 08 29 2D 
2D F5 F7 F7 CF CE CE 0E 0A 0A 42 33 1E 05 54 54 54 B4 62 C5 8A 5B B7 6E D1 2F F5 F5 F5 57 AE 5C 
89 2B A5 1A BA 74 E9 92 9C 9C 9C 95 95 75 E9 D2 A5 D4 D4 D4 E7 CF 9F 07 05 05 7D 75 C4 77 0D 0D 
8D 69 D3 A6 B5 6F DF DE D1 D1 51 F4 67 39 26 26 66 CC 98 31 ED DA B5 93 71 6A 96 08 EB 81 E4 E4 
64 BA 1B 84 93 93 13 DB 59 E4 A7 FE 5C 5F DA DA B5 6B 45 BF B1 D7 AE 5D CB 76 22 D9 AA 6F D7 F7 
FD FB F7 3B 76 EC EC 62 D8 B5 A3 41 27 E6 3F 93 DE 7D 52 D3 D2 D8 8E 26 13 F5 ED FA 32 CA CB CB 
A3 A2 A2 3E ED AE 34 73 E6 CC 92 92 12 B6 D3 49 8D 6A 5C DF 8F 1F 3F 6E DC B8 91 B9 46 DA DA DA 
D1 D1 D1 55 55 55 5F DA 3E 35 35 55 F4 9A 8E 1A 35 EA C5 8B 17 F2 0C 2C 37 AA 71 7D EB A2 AA AA 
6A C7 8E 1D D5 7E 8A 8F 1D 3B C6 76 2E E9 10 BD BE AA DF CC 83 31 64 C8 10 3E 9F DF A4 49 93 C8 
C8 48 67 67 67 B6 E3 00 40 ED BC 7D FB 76 BD FF 86 1D 3B 77 8A DE 93 6E DE BC F9 EE DD BB CC CD 
CC 58 0C 06 52 A7 A9 A9 39 6D DA B4 C4 C4 C4 6A 8D 6E C3 C3 C3 23 22 22 84 AA F8 98 58 79 9D 3A 
75 4A 74 2C BC E9 D3 A7 DB DA DA 62 2C 3C 20 84 70 38 9C B1 63 C7 9A 9A 9A 8A AE 4C 4D 4D FD F0 
E1 03 5B 91 64 A4 1E 15 D3 84 90 A1 43 87 F2 78 BC C6 8D 1B 47 44 44 CC 9A 35 8B ED 38 00 20 AE 
C2 C2 C2 85 8B 16 1D 3C 78 50 74 65 BB 76 ED C2 42 43 50 49 AB 2A 7D 7D FD 80 80 80 6A 7F 89 63 
63 63 45 9F 1A 03 BB 32 33 33 37 6C D8 C0 34 95 1E 36 6C 98 8F 8F 0F C6 C2 03 46 BB 76 ED CC FE 
FB 2B FA CE 9D 3B 25 25 25 6C E5 91 91 FA 55 4C 13 42 86 0F 1F CE E7 F3 35 34 34 C2 C3 C3 67 CF 
9E CD 76 1C 00 F8 BA FB D9 D9 73 5C E7 9E 39 73 56 74 A5 81 81 C1 AE A0 C0 01 03 30 AA B4 2A 33 
36 36 F6 F4 F4 14 5D 93 96 96 76 FB F6 6D B6 F2 80 A8 B2 B2 B2 ED DB B7 8B 4E 1B BE 7A F5 6A 95 
6D 0E 0B 12 69 D4 A8 51 EF DE BD 45 D7 14 15 15 15 17 17 B3 95 47 46 EA 5D 31 4D 08 19 31 62 04 
9F CF 6F D4 A8 D1 BE 7D FB 5C 5C 5C D8 8E 03 00 5F 24 14 0A 53 53 53 A7 4D 9B CE F4 6D A2 99 98 
98 EC 0B 0B AD F6 3B 1A 54 D2 B0 61 C3 86 0E 1D 2A BA E6 CA 95 2B 95 95 95 2C C5 81 7F 54 56 56 
06 07 07 87 85 85 31 6B E6 CE 9D 6B 6E 6E CE 62 24 50 4C 7A 7A 7A A2 2F 9F 3F 7F FE F6 ED 5B B6 
C2 C8 48 7D 2C A6 09 21 56 56 56 7C 3E BF 61 C3 86 61 61 61 73 E6 CC 61 3B 0E 00 7C C6 87 0F 1F 
42 43 C3 66 38 CF 2C 2A 2A 12 5D 3F 72 A4 55 F8 BE B0 4E 9D 3A B1 15 0C E4 49 47 47 A7 7B F7 EE 
A2 6B 8A 8B 8B 55 AF CD A5 D2 79 FD FA F5 EF BF FF 2E BA 66 F9 F2 E5 0D 1B 36 E4 7C 8D 85 85 85 
E8 5E 89 89 89 FF FB DF FF 44 37 70 75 75 AD A8 A8 90 EF 57 03 32 54 6D C4 D2 FC FC FC 77 EF DE 
B1 15 46 46 EA 69 31 4D 08 19 39 72 24 8F C7 53 53 53 0B 0D 0D 9D 3B 77 2E DB 71 00 E0 3F 0A 0B 
0B 3D 3C 3D 37 6E DA 24 DA DD 90 10 E2 E0 E0 B0 6D EB D6 56 AD 5A B1 15 0C E4 AC 71 E3 C6 6D DA 
B4 11 5D F3 F8 F1 E3 F2 F2 72 B6 F2 00 40 5D F4 EC D9 53 F5 7E 81 D7 DF 62 9A 10 32 6A D4 28 3E 
9F DF A0 41 83 BD 7B F7 BA B9 B9 B1 1D 07 00 FE 71 FB F6 6D 07 07 C7 6A 8D A4 35 34 34 D6 AF 5B 
B7 6A D5 CA A6 4D 9B B2 15 0C 24 F0 F6 ED DB CC CC CC C3 87 0F BB BB BB 0F 1B 36 2C 23 23 83 ED 
44 00 20 3F 8F 1F 3F 16 7D D9 A8 51 23 D5 9B CD A7 5E 17 D3 84 90 D1 A3 47 F3 F9 7C 0E 87 B3 67 
CF 1E 77 77 77 B6 E3 00 D4 77 42 A1 F0 CC 99 B3 0E 8E 4E F7 FF 3B 81 6D BB 76 ED 0E 44 46 D8 DB 
4F 56 57 53 63 2B 1B 48 20 37 37 77 D4 A8 51 DD BB 77 9F 3A 75 6A 70 70 70 72 72 F2 BD 7B F7 6A 
75 84 77 EF DE 15 14 14 88 AE 69 DF BE BD E8 A4 6B 00 20 23 0F 1E 3C E8 DF BF BF 68 23 9C 5F 7E 
F9 A5 B6 07 79 F2 E4 89 E8 CB 36 6D DA E0 CE B4 0A FA E1 87 1F 78 3C 1E 21 24 38 38 D8 C3 C3 83 
ED 38 00 F5 97 50 28 8C 8F 3F E1 E9 E5 55 6D E0 24 13 13 93 FD FB C3 4D 4D 4D 31 78 AD D2 69 D1 
A2 45 DB B6 6D 45 D7 A4 A4 A4 D4 AA 45 6C 71 71 F1 5F 7F FD 25 BA 46 57 57 57 43 43 43 3A F9 00 
E0 CB 74 75 75 0D 0C 0C 44 D7 DC BA 75 AB 56 DD 7F 4B 4A 4A 6E DC B8 21 BA A6 57 AF 5E CD 9A 35 
93 4E 3E 85 81 62 9A 10 42 6C 6C 6C E8 7A 7A F7 EE DD 5E 5E 5E 6C C7 01 A8 8F E8 4A DA 67 C5 8A 
F7 EF DF 8B AE E7 72 A9 88 FD FB BB 1A 1A B2 15 0C EA A2 69 D3 A6 86 FF BD 76 17 2F 5E CC FE EF 
63 87 9A 5D BB 76 AD 5A CB 90 1E 3D 7A A8 E1 01 05 DB 5A B5 6A F5 DB 6F BF 49 30 6F DC 57 67 40 
DC BB 77 2F 9E 3C 28 88 4F 7F 7E CF 9D 3B 57 ED 4E 73 CD 6E DD BA 95 96 96 26 BA 66 E0 C0 81 AA 
F7 F3 8B 62 FA 1F 14 45 9D 3C 79 92 10 12 14 14 34 6F DE 3C B6 E3 00 D4 3B 97 2E 5F 5E EB E7 57 
AD 92 76 71 99 BD 79 D3 A6 96 2D 5B B0 95 0A EA 48 4D 4D 6D C4 88 11 DA DA DA CC 9A CC CC CC 5F 
7E F9 A5 5A BF D2 2F 29 2C 2C 8C 88 88 60 E6 04 21 84 98 9A 9A 9A 61 9A 1E 00 B9 50 53 53 1B 38 
70 A0 E8 9A F4 F4 F4 93 27 4F 8A 39 0B E9 9B 37 6F C2 C3 C3 F3 F3 F3 99 35 56 56 56 2A 39 39 00 
8A E9 FF C7 E5 72 13 12 12 08 21 81 81 81 F3 E7 CF 67 3B 0E 40 3D 72 3F 3B 7B D5 2A DF 6A AD 3B 
BC BC 3C 97 2C 59 D2 B8 71 63 B6 52 81 54 F4 ED DB D7 CA CA 4A 74 4D 50 50 D0 99 33 67 BE FA F7 
B8 AC AC 6C ED DA B5 F4 AF 65 86 B5 B5 75 87 0E 1D A4 9F 12 00 3E 67 C0 80 01 D5 7E 7E B7 6F DF 
7E F1 E2 C5 AF EE 28 10 08 F6 EC D9 53 6D DA DA 49 93 26 55 1B 9C 47 35 A0 98 FE 8F B1 63 C7 C6 
C7 C7 13 42 76 EE DC B9 70 E1 42 B6 E3 00 D4 0B 15 15 15 61 61 61 8F 1E 3D 12 5D E9 E5 E5 E9 E9 
E9 89 EE 86 2A A0 65 CB 96 93 26 4D 12 BD 39 5D 5A 5A 3A 77 EE DC D3 A7 4F 57 55 55 7D 69 AF 82 
82 02 2F 2F AF E0 E0 60 D1 95 A6 A6 A6 D3 A7 4F 57 BD 67 C4 00 0A 4B 4F 4F CF C9 C9 49 74 4D 6E 
6E EE BC 79 F3 D2 D2 D2 6A F8 3C 5C 54 54 E4 ED ED BD 7C F9 72 D1 95 76 76 76 3F FE F8 A3 4A 76 
7D 41 31 5D DD 8F 3F FE 78 FC F8 71 42 C8 F6 ED DB 17 2D 5A C4 76 1C 00 D5 77 FE FC F9 13 27 FE 
73 F7 D1 D2 D2 72 86 93 13 2A 69 95 C1 E5 72 A7 4F 9F 2E BA 26 37 37 97 A2 A8 69 D3 A6 25 27 27 
BF 7C F9 92 AE AA 85 42 61 49 49 C9 D5 AB 57 E7 CF 9F DF A3 47 8F FD FB F7 8B EE A2 AD AD 3D 7F 
FE 7C 43 B4 9E 07 90 2F 2E 97 EB E0 E0 20 BA E6 D6 AD 5B 3F FC F0 83 93 93 93 E8 CF 2F 21 E4 ED 
DB B7 7F FE F9 A7 9F 9F DF 80 01 03 B6 6C D9 22 BA 8B BE BE FE A2 45 8B 74 75 75 E5 97 5B 8E 54 
6D A8 3F A9 B0 B3 B3 3B 76 EC D8 F8 F1 E3 B7 6D DB C6 E1 70 AA 7D 43 00 80 14 BD 7E FD FA C8 2F 
47 AB B5 A0 4D 49 49 E9 D3 B7 9F C4 C7 DC B4 69 E3 A4 89 13 EB 1C 0D A4 46 4B 4B CB D7 D7 37 2F 
2F AF 5A 9B 8D 98 98 98 98 98 18 71 8E A0 AD AD ED EF EF 3F 61 C2 04 D9 04 04 80 2F 6A D6 AC D9 
F2 E5 CB B3 B2 B2 D2 D3 D3 99 95 A5 A5 A5 07 0F 1E AC D6 8A E3 4B 74 74 74 36 6E DC A8 C2 BD 1D 
70 67 FA F3 C6 8D 1B 17 17 17 47 08 D9 BA 75 EB 92 25 4B D8 8E 03 A0 B2 B2 B2 B2 2E 5F BE CC 76 
0A 90 B9 D6 AD 5B EF DC B9 D3 C6 C6 46 82 7D 75 74 74 82 82 82 5C 5D 5D 55 6F AE 07 00 A5 60 6C 
6C 7C E0 C0 01 73 73 73 09 F6 D5 D7 D7 0F 0B 0B FB E9 A7 9F 54 B2 81 07 0D C5 F4 17 8D 1F 3F FE 
E8 D1 A3 84 90 2D 5B B6 2C 5B B6 8C ED 38 00 AA 29 35 2D 4D CC 81 1D 40 D9 E9 EB EB 1F 3C 78 70 
F1 E2 C5 B5 DA 6B C0 80 01 3C 1E CF C1 C1 01 95 34 00 8B 8C 8C 8C E2 E2 E2 9C 9D 9D 6B B5 97 B5 
B5 F5 89 13 27 C6 8D 1B A7 C2 95 34 41 31 5D B3 89 13 27 D2 93 FD 6C DE BC B9 5A 3B 7A 00 A8 BB 
8A 8A 8A A7 4F 9E B2 9D 02 E4 47 47 47 67 D3 A6 4D 29 29 29 76 76 76 5F DD B8 67 CF 9E 91 91 91 
E7 CF 9F 37 33 33 53 ED BF C4 00 4A A1 4D 9B 36 61 61 61 E7 CE 9D 1B 35 6A D4 57 37 EE D9 B3 67 
74 74 F4 89 13 27 7A F7 EE 2D 87 6C EC C2 07 FD AF 98 34 69 92 50 28 9C 3C 79 F2 A6 4D 9B 38 1C 
CE 86 0D 1B D8 4E 04 A0 3A 3E 7E FC F8 B2 B8 98 ED 14 20 57 0D 1A 34 B0 B0 B0 30 37 37 7F F6 EC 
59 52 52 52 6A 6A EA BD 7B F7 AE 5C B9 42 BF DB A7 4F 1F 23 23 23 33 33 B3 11 23 46 74 ED DA 15 
77 A3 01 14 4A 83 06 0D 86 0D 1B 36 64 C8 90 A7 4F 9F 9E 3D 7B F6 D3 9F 5F 7D 7D FD 21 43 86 58 
5B 5B D7 AB 9F DF 7F 3E EB 8B 39 FE 76 BD 75 E4 C8 11 7B 7B 7B 42 88 B7 B7 B7 BF BF 3F DB 71 6A 
81 BE 9D 83 EB AB AA 70 7D 55 1B AE AF 6A C3 F5 55 6D B8 BE AA 4D F4 FA A2 99 87 58 26 4F 9E 1C 
1D 1D 4D 08 D9 B0 61 C3 CA 95 2B D9 8E 03 00 00 00 00 0A 01 C5 B4 B8 A6 4C 99 72 E8 D0 21 42 C8 
FA F5 EB 57 AD 5A C5 76 1C 00 00 00 00 60 1F 8A E9 5A 98 3A 75 6A 54 54 14 21 64 DD BA 75 BE BE 
BE 6C C7 01 00 00 00 00 96 A1 98 AE 9D 69 D3 A6 D1 43 94 FB F9 F9 AD 5E BD 9A ED 38 00 00 00 00 
C0 26 14 D3 B5 36 7D FA F4 C8 C8 48 42 C8 DA B5 6B D7 AC 59 C3 76 1C 00 00 00 00 60 0D 8A 69 49 
38 3A 3A 46 44 44 10 42 7E FE F9 E7 B5 6B D7 B2 1D 07 00 00 00 00 D8 81 62 5A 42 4E 4E 4E FB F7 
EF 27 84 AC 5E BD DA CF CF 8F ED 38 00 00 00 00 C0 02 14 D3 92 9B 31 63 C6 BE 7D FB 08 21 BE BE 
BE EB D6 AD 63 3B 0E 00 00 00 00 C8 1B 8A E9 3A 99 39 73 66 58 58 18 21 64 D5 AA 55 CA 35 99 0B 
00 00 00 00 D4 1D 8A E9 BA 9A 35 6B 56 68 68 28 21 64 C5 8A 15 98 6C 1C 00 00 00 A0 5E 41 31 2D 
05 B3 67 CF 0E 09 09 21 84 F8 F8 F8 6C DC B8 91 ED 38 00 00 00 00 20 27 28 A6 A5 C3 C5 C5 65 CF 
9E 3D 84 10 6F 6F EF 4D 9B 36 B1 1D 07 00 00 00 00 E4 01 C5 B4 D4 B8 BA BA 06 07 07 13 42 96 2F 
5F 1E 10 10 C0 76 1C 00 00 00 00 90 39 14 D3 D2 34 77 EE DC DD BB 77 13 42 96 2E 5D BA 65 CB 16 
B6 E3 00 00 00 00 80 6C A1 98 96 32 37 37 B7 5D BB 76 11 42 96 2C 59 B2 75 EB 56 B6 E3 00 00 00 
00 80 0C A1 98 96 3E 77 77 F7 C0 C0 40 42 C8 E2 C5 8B B7 6D DB C6 76 1C 00 00 00 00 90 15 14 D3 
32 E1 E9 E9 B9 73 E7 4E 42 C8 A2 45 8B 76 EC D8 C1 76 1C 00 00 00 00 90 09 14 D3 B2 E2 E5 E5 45 
97 D1 0B 16 2C A0 0B 6B 00 00 00 00 50 31 28 A6 65 68 DE BC 79 DB B7 6F 27 84 CC 9F 3F 9F 6E F8 
01 00 00 00 00 AA 04 C5 B4 6C CD 9F 3F 9F EE 86 38 6F DE 3C BA 63 22 00 00 00 00 A8 0C 14 D3 32 
B7 70 E1 42 7A 98 3C 4F 4F 4F 7A E0 3C 00 00 00 00 50 0D 28 A6 E5 61 D1 A2 45 F4 34 2E 1E 1E 1E 
F4 C4 2E 00 00 00 00 A0 02 50 4C CB C9 E2 C5 8B 37 6F DE 4C 08 71 77 77 A7 27 1E 07 00 00 00 00 
65 87 62 5A 7E 96 2C 59 B2 71 E3 46 42 88 9B 9B 5B 48 48 08 DB 71 00 00 00 00 A0 AE 50 4C CB D5 
B2 65 CB 36 6C D8 40 08 71 75 75 0D 0D 0D 65 3B 0E 00 00 00 00 D4 09 8A 69 79 5B BE 7C B9 BF BF 
3F 21 64 CE 9C 39 61 61 61 6C C7 01 00 00 00 00 C9 A1 98 66 81 B7 B7 F7 FA F5 EB 09 21 2E 2E 2E 
FB F6 ED 63 3B 0E 00 00 00 00 48 08 C5 34 3B 7C 7C 7C FC FC FC 08 21 B3 67 CF DE BF 7F 3F DB 71 
00 00 00 00 40 12 28 A6 59 B3 72 E5 CA B5 6B D7 12 42 66 CE 9C 19 11 11 C1 76 1C 00 00 00 00 A8 
35 14 D3 6C 5A B5 6A D5 9A 35 6B 08 21 CE CE CE 91 91 91 6C C7 01 00 00 00 80 DA 41 31 CD 32 5F 
5F DF D5 AB 57 13 42 66 CC 98 71 E0 C0 01 B6 E3 00 00 00 00 40 2D A0 98 66 DF CF 3F FF EC EB EB 
4B 08 71 72 72 8A 8A 8A 62 3B 0E 00 00 00 00 88 0B C5 B4 42 58 B3 66 CD AA 55 AB 08 21 0E 0E 0E 
87 0E 1D 62 3B 0E 00 00 00 00 88 05 C5 B4 A2 58 BB 76 ED CA 95 2B 09 21 D3 A7 4F 8F 8E 8E 66 3B 
0E 00 00 00 00 7C 1D 8A 69 05 E2 E7 E7 E7 E3 E3 43 08 99 36 6D DA E1 C3 E3 1E 8F 94 00 00 20 00 
49 44 41 54 87 D9 8E 03 00 00 00 00 5F 81 62 5A B1 AC 5F BF DE DB DB 9B 10 32 75 EA D4 23 47 8E 
B0 1D 07 00 00 00 00 6A 82 62 5A E1 F8 FB FB 2F 5F BE 9C 10 62 6F 6F FF CB 2F BF B0 1D 07 00 00 
00 00 BE 08 C5 B4 22 DA B0 61 C3 B2 65 CB 08 21 93 27 4F 3E 7A F4 28 DB 71 00 00 00 00 E0 F3 50 
4C 2B A8 8D 1B 37 2E 59 B2 84 10 F2 D3 4F 3F C5 C6 C6 B2 1D 07 00 00 00 00 3E 03 C5 B4 E2 DA BC 
79 F3 E2 C5 8B 09 21 93 26 4D 3A 76 EC 18 DB 71 00 00 00 00 A0 3A 14 D3 0A 2D 20 20 60 D1 A2 45 
84 90 09 13 26 1C 3F 7E 9C ED 38 00 00 00 00 F0 1F 28 A6 15 DD 96 2D 5B 16 2E 5C 48 08 19 3F 7E 
7C 7C 7C 3C DB 71 00 00 00 00 E0 FF A1 98 56 02 5B B7 6E 9D 3F 7F 3E 21 64 DC B8 71 09 09 09 6C 
C7 01 00 00 00 80 7F A0 98 56 0E DB B7 6F 9F 37 6F 1E 21 E4 C7 1F 7F 3C 79 F2 24 DB 71 00 00 00 
00 80 10 14 D3 4A 64 C7 8E 1D 5E 5E 5E 84 10 5B 5B 5B 1E 8F C7 76 1C 00 00 00 00 40 31 AD 54 76 
EE DC E9 E9 E9 49 08 19 3B 76 2C 9F CF 67 3B 0E 00 00 00 40 7D 87 62 5A C9 04 06 06 BA BB BB 13 
42 B8 5C EE E9 D3 A7 D9 8E 03 00 00 00 50 AF A1 98 56 3E BB 76 ED 72 73 73 23 84 50 14 F5 EB AF 
BF B2 1D 07 00 00 00 A0 FE 42 31 AD 94 76 EF DE 3D 77 EE 5C A1 50 48 51 D4 6F BF FD C6 76 1C 00 
00 00 80 7A 0A C5 B4 B2 0A 0E 0E 9E 33 67 4E 55 55 15 45 51 89 89 89 6C C7 01 00 00 00 A8 8F 50 
4C 2B B1 BD 7B F7 BA B8 B8 54 56 56 72 B9 DC 33 67 CE B0 1D 07 00 00 00 A0 DE 41 31 AD DC 42 42 
42 66 CF 9E FD F1 E3 47 8A A2 CE 9E 3D CB 76 1C 00 00 00 80 FA 05 C5 B4 D2 0B 0D 0D 9D 35 6B D6 
87 0F 1F 28 8A FA FD F7 DF D9 8E 03 00 00 00 50 8F A0 98 56 05 61 61 61 CE CE CE EF DF BF E7 72 
B9 E7 CE 9D 63 3B 0E 00 00 00 40 7D 81 62 5A 45 84 87 87 CF 98 31 A3 A2 A2 82 CB E5 26 27 27 B3 
1D 07 00 00 00 A0 5E 40 31 AD 3A F6 EF DF EF E4 E4 54 5E 5E 4E 51 D4 85 0B 17 D8 8E 03 00 00 00 
A0 FA 50 4C AB 94 88 88 08 47 47 C7 B2 B2 32 8A A2 2E 5E BC C8 76 1C 00 00 00 00 15 87 62 5A D5 
44 46 46 4E 9F 3E FD ED DB B7 5C 2E 37 25 25 85 ED 38 00 00 00 00 AA 8C 43 FF 4F 28 14 B2 9B 03 
A4 6B FA F4 E9 87 0E 1D 6A DE BC 79 49 49 09 C1 F5 55 5D 1C 0E 87 E0 FA AA 2E 5C 5F D5 86 EB AB 
DA 70 7D 55 9B E8 F5 E5 B0 1D 06 00 00 00 00 40 F9 D0 C5 34 9A 79 00 00 00 00 00 48 48 9D FE 1F 
1E 43 A8 2A 3C 66 52 6D B8 BE AA 0D D7 57 B5 E1 FA AA 36 5C 5F D5 46 5F 5F 1A EE 4C 03 00 00 00 
00 48 08 C5 34 00 00 00 00 80 84 50 4C 03 00 00 00 00 48 08 C5 34 00 00 00 00 80 84 50 4C 03 00 
00 00 00 48 08 C5 34 00 00 00 00 80 84 50 4C 03 00 00 00 00 48 08 C5 34 00 00 00 00 80 84 50 4C 
03 00 00 00 00 48 08 C5 34 00 00 00 00 80 84 50 4C 03 00 00 00 00 48 08 C5 34 00 00 00 00 80 84 
50 4C 03 00 00 00 00 48 08 C5 34 00 00 00 00 80 84 50 4C 03 00 00 00 00 48 08 C5 34 00 00 00 00 
80 84 50 4C 03 00 00 00 00 48 08 C5 34 00 00 00 00 80 84 50 4C 03 00 00 00 00 48 08 C5 34 00 00 
00 00 80 84 50 4C 03 00 00 00 00 48 08 C5 34 00 00 00 00 80 84 50 4C 03 00 00 00 00 48 08 C5 34 
00 00 00 00 80 84 50 4C 03 00 00 00 00 48 08 C5 34 00 00 00 00 80 84 50 4C 03 00 00 00 00 48 08 
C5 34 00 00 00 00 80 84 50 4C 03 00 00 00 00 48 08 C5 34 00 00 00 00 80 84 50 4C 03 00 00 00 00 
48 08 C5 34 00 00 00 00 80 84 50 4C 03 00 00 00 00 48 08 C5 34 00 00 00 00 80 84 50 4C 03 00 00 
00 00 48 08 C5 34 00 00 00 00 80 84 50 4C 03 00 00 00 00 48 08 C5 34 00 00 00 00 80 84 50 4C 03 
80 74 3C 78 F0 C0 C2 72 B0 41 A7 CE 35 FF F7 BD E9 C0 29 53 A7 06 EF D9 F3 E4 C9 53 A1 50 58 C3 
01 5F BD 7A 65 37 6E 3C BD D7 D1 D8 D8 4F 37 48 4F 4F 67 0E 3B C7 D5 B5 B4 B4 54 CC A8 47 63 63 
E9 BD 2C 2C 07 3F 78 F0 40 92 AF 56 D5 55 54 54 B8 BA BA 72 38 1C 0E 87 E3 EA EA 5A 51 51 21 E6 
8E 2F 5F BE 1C 3D 7A 34 BD A3 9F 9F 5F 0D EF 4A 40 F4 80 45 45 45 E3 C6 8D A3 D7 37 6B D6 EC F0 
E1 C3 35 7F 3B 31 04 02 C1 A6 4D 9B 98 1D 8F 1C 39 22 E6 97 A6 1A C4 BC 04 1D 3B 76 1C 39 72 E4 
D2 A5 4B 4F 9D 3A F5 E6 CD 1B 69 1D 56 9C 2B 5B 83 8A 8A 8A E4 E4 64 1F 1F 9F E1 C3 87 B7 6A D5 
8A DE B7 6F DF BE 33 66 CC 88 8D 8D 7D F5 EA 55 9D FF 79 00 24 81 62 1A 00 E4 AA A8 A8 E8 F2 E5 
2B 01 01 5B 86 0C 1D EA E1 E9 55 58 58 28 95 C3 26 25 9D 39 7E 3C 5E CC 72 0A 54 80 AE AE AE 8F 
8F 8F BE BE 3E 21 A4 B4 B4 74 DD BA 75 77 EE DC 11 67 C7 73 E7 CE AD 5F BF 9E 5E F6 F4 F4 9C 30 
61 82 0C 53 2A AD DC DC DC B3 67 CF 06 04 04 50 14 65 60 60 B0 62 C5 8A A2 A2 22 16 F3 14 15 15 
F9 FB FB 1B 1B 1B 0F 1B 36 6C C3 86 0D E7 CF 9F 2F 2E 2E A6 DF BA 79 F3 66 64 64 E4 A4 49 93 BA 
74 E9 C2 7A 4E A8 9F 50 4C 03 00 6B 4E 9F 3E ED E0 E0 98 9D 2D 9D 7B C3 61 FB F6 65 67 67 4B E5 
50 A0 14 FA F5 EB B7 62 C5 0A 7A 39 33 33 73 DD BA 75 5F BD 37 99 99 99 E9 EB EB 4B 3F C4 B0 B5 
B5 F5 F2 F2 52 57 57 97 79 50 25 57 5C 5C EC EF EF 6F 67 67 77 E3 C6 0D F9 9F BD AA AA 2A 2E 2E 
CE D2 D2 72 C5 8A 15 B9 B9 B9 35 6C C9 6E 4E A8 CF 50 4C 03 00 9B EE 67 67 6F D9 BA 45 FC 16 1A 
35 C8 CB CB DB B5 7B 77 79 79 79 DD 0F 05 4A 81 C3 E1 4C 99 32 65 F6 EC D9 F4 CB D8 D8 D8 7D FB 
F6 55 56 56 7E 69 FB 37 6F DE 6C DC B8 31 3D 3D 9D 10 A2 AF AF BF 60 C1 82 D6 AD 5B CB 29 AB F2 
4B 4B 4B 73 73 73 CB CC CC 94 E7 49 05 02 C1 D6 AD 5B 9D 9D 9D B3 B2 B2 C4 DC 85 CE 99 91 91 21 
D3 60 00 A2 50 4C 03 80 F4 1D 89 39 FC 28 E7 E1 A7 FF E5 3C 7C 70 EB 8F 9B BF 9E 3E 35 67 8E 8B 
86 86 06 BD F1 B9 73 E7 53 52 52 A4 72 5E 1E 8F CF E3 F3 D1 D8 43 29 AC 5D BB 56 58 4B AB 56 AD 
AA 76 10 2D 2D AD 05 0B 16 98 9A 9A D2 2F 77 EF DE 9D 9A 9A FA D9 D3 09 04 82 3D 7B F6 1C 3C 78 
90 7E B9 62 C5 8A C1 83 07 CB EE AB 53 0A 35 5C 82 D2 D2 D2 9C 9C 9C C8 C8 48 4B 4B 4B 66 FB F4 
F4 74 6F 6F EF AF 36 CD 92 CA 95 25 84 08 85 C2 A3 47 8F FA F9 F9 31 1F B6 B5 B5 B5 ED ED ED F9 
7C 7E 41 41 C1 C7 8F 1F 99 A8 E9 E9 E9 1E 1E 1E DA DA DA 4C 4E 3F 3F 3F 69 35 21 03 F8 2A 14 D3 
00 20 3F 74 97 AF 6E DD BA 2D 5F B6 2C 3C 7C 5F F3 E6 CD 09 21 02 81 20 29 E9 8C F8 5D DC 6A 16 
14 B4 0B 8D 3D EA 95 6E DD BA 79 79 79 D1 85 54 6E 6E 6E 40 40 40 41 41 C1 A7 9B 5D BC 78 71 E7 
CE 9D F4 B2 9B 9B DB 94 29 53 38 1C 8E 5C 83 2A 95 A6 4D 9B 1A 18 18 38 3A 3A 26 26 26 6E D9 B2 
85 A9 53 13 12 12 F6 EF DF 5F C3 ED 7F 29 BA 74 E9 92 8F 8F 0F 53 49 5B 5B 5B 27 27 27 47 47 47 
DB D8 D8 B4 6E DD 9A 69 9F D3 B4 69 D3 EF BF FF 3E 30 30 F0 DC B9 73 E6 E6 E6 F2 CF 09 80 62 1A 
00 D8 61 6A 6A 3A F1 DF BE 5F D9 0F 1E 94 94 7C 7D C4 80 1A 8C 18 31 82 FE E3 9A 97 97 17 12 1A 
8A C6 1E F5 07 87 C3 B1 B3 B3 73 74 74 A4 5F 9E 3A 75 2A 28 28 48 20 10 88 6E 93 99 99 E9 E3 E3 
93 9F 9F 4F 08 31 35 35 F5 F0 F0 D0 D2 D2 62 21 AB 12 D2 D4 D4 9C 37 6F 1E D3 36 9D 10 12 15 15 
75 EF DE 3D 59 9F F7 CD 9B 37 A1 A1 A1 4C 23 E9 89 13 27 1E 3C 78 B0 6F DF BE 5F FA 08 C4 E1 70 
FA F7 EF 1F 16 16 C6 3C A6 90 4F 4E 00 82 62 1A 00 D8 A2 AE A6 66 D8 D5 90 5E 2E 29 29 79 FB B6 
4E CD A6 A7 D8 4F 1E 3B 96 4B 2F 9F 3C C9 3B 75 FA 34 1A 7B D4 1F 9A 9A 9A 8B 16 2D 62 EE 4A 06 
05 05 9D 3A 75 8A 79 B7 AC AC 6C D7 AE 5D 74 53 69 6D 6D 6D 6F 6F 6F 63 63 63 76 82 2A 27 75 75 
75 0F 0F 0F 37 37 37 FA 65 66 66 66 62 62 A2 AC 7F BE AE 5D BB 16 1F 1F 4F 2F 9B 9A 9A AE 5F BF 
5E 9C 06 EE C6 C6 C6 9E 9E 9E F4 72 66 66 66 52 52 92 0C 23 02 FC 0B C5 34 00 B0 4F 53 53 93 69 
42 2D 19 2D 2D AD 39 2E 2E ED DA B5 23 FF B4 8E DD 9B 8D 01 A4 EB 93 8E 1D 3B FA FA FA D2 AD 11 
4A 4B 4B 37 6C D8 40 B7 F6 11 0A 85 FB F6 ED 0B 0E 0E A6 37 5B BA 74 A9 8D 8D 0D 9B 41 95 93 96 
96 96 A3 A3 A3 9E 9E 1E FD F2 F2 E5 CB E2 0C 3E 2D B1 0F 1F 3E 9C 3A 75 8A 69 E0 E1 E9 E9 69 68 
68 28 E6 BE 63 C6 8C B1 B3 B3 23 84 18 19 19 BD 7C F9 52 5A ED C7 00 6A 80 62 1A 00 D8 21 A8 AC 
CC BE FF 4F E3 66 03 83 8E 3A 3A 3A 75 3C A0 A1 A1 A1 A7 A7 07 BD FC E8 D1 A3 90 90 10 34 F6 A8 
57 86 0F 1F BE 74 E9 52 7A 39 3D 3D 3D 30 30 B0 A2 A2 E2 D2 A5 4B DB B7 6F A7 57 DA DA DA CE 9E 
3D 1B 63 E1 49 A6 47 8F 1E A3 46 8D A2 97 B3 B2 B2 E8 36 33 32 F2 E2 C5 8B 9B 37 6F D2 CB 66 66 
66 16 16 16 E2 EF DB B2 65 CB 4D 9B 36 BD 78 F1 82 1E 2D 51 53 53 53 36 19 01 FE 1F 8A 69 00 60 
47 7A 7A 7A 6C 5C 1C BD 6C 69 69 59 F7 36 AC 1C 0E 87 4B 51 5C 2E 45 BF 3C 79 92 F7 DB 6F 89 75 
3C 26 28 11 75 75 F5 D9 B3 67 DB DA DA D2 2F 0F 1C 38 70 E0 C0 81 AD 5B B7 D2 ED 6E F5 F5 F5 97 
2C 59 82 B1 F0 24 A6 A5 A5 D5 AB 57 2F 7A F9 CE 9D 3B 4F 9F 3E 95 DD B9 9E 3C 79 C2 8C 6D 67 6A 
6A CA DC 11 17 93 A1 A1 21 3D 3F A2 0C A2 01 7C 06 3E A0 03 80 5C 95 95 95 3D 7D FA F4 44 42 42 
64 E4 81 F7 EF DF 13 42 7A F4 E8 6E 35 62 84 54 0E DE A4 49 13 0F 77 F7 1B 37 6E E6 E5 E5 09 04 
82 5D BB 77 9B 98 F4 EA DC B9 B3 54 0E 5E 6F 85 84 84 84 84 84 B0 9D 42 2C AD 5B B7 5E B2 64 C9 
1F 7F FC 91 9B 9B 5B 5A 5A 3A 77 EE 5C E6 AD 75 EB D6 99 99 99 B1 98 4D 05 7C F7 DD 77 CC B2 4C 
EF 4C 3F 7C F8 90 69 E3 61 64 64 D4 A8 51 23 D9 9D 0B A0 EE 70 67 1A 00 A4 6F B2 FD 14 83 4E 9D 
3F FB DF 77 3D 7B FD 30 C6 26 24 24 94 AE A4 75 75 75 BD BD BD 6B 7B E7 A9 06 86 86 86 B3 67 CD 
A2 97 1F 3D 7A B4 37 24 04 8D 26 15 93 AF AF 2F A7 36 FC FC FC C4 39 AC 99 99 D9 82 05 0B AA AD 
74 73 73 B3 B3 B3 C3 AD CA 3A 6A D2 A4 09 B3 5C C3 64 84 75 BF B2 CF 9F 3F 67 96 D1 5B 14 14 1F 
8A 69 00 60 CD 80 01 03 0E 1D 8A 32 97 EA FD 42 0E 87 33 6E 9C 9D B5 F5 48 FA E5 89 13 09 BF FE 
FA 9B 14 8F 0F 0A 8E C3 E1 CC 98 31 C3 C1 C1 81 59 63 6A 6A 3A 7F FE 7C 8C 85 57 77 DA DA DA E2 
77 04 AC 8B B7 6F DF 32 CB 6A 6A 6A 72 38 23 40 5D A0 98 06 00 D6 3C 7B F6 2C 25 25 45 EA DD 04 
B5 B5 B5 3D 3D 3C E9 D6 B1 02 81 20 24 24 24 F7 C9 13 E9 9E 02 14 59 65 65 A5 E8 E3 88 82 82 82 
BF FF FE 9B C5 3C 2A 43 43 43 43 F4 E6 34 00 D0 50 4C 03 00 6B F2 F3 F3 D7 AD 5B 6F 67 37 4E EA 
73 2B F4 E8 D1 7D AE AB 2B BD 7C 3F 3B 3B 34 34 F4 C3 87 0F D2 3D 45 FD 31 67 CE 9C F2 F2 72 31 
E7 85 7E F1 E2 05 33 E6 03 2B 04 02 41 68 68 68 6C 6C 2C B3 A6 86 69 11 A1 56 5E BD 7A 95 93 93 
C3 76 0A 00 85 83 62 1A 00 A4 EF 48 CC E1 47 39 0F 3F FB DF FD AC 7B E9 57 2E 87 87 EF 1B 3E 6C 
18 BD F1 FD EC 6C 37 77 8F 87 0F 1F 4A 31 00 87 C3 B1 B5 1D 6B 69 69 49 BF 3C 7A 34 F6 EC D9 B3 
52 3C 3E D4 DD DA B5 6B C5 2C D0 69 AB 56 AD 12 E7 B0 A2 D3 86 33 3E 3B 2D 22 D4 56 65 65 25 D3 
2F B0 86 11 06 EB 7E 65 F5 F5 F5 99 65 0C 70 09 8A AF 3E 16 D3 CF 9F 3F B7 B5 B5 AD 55 8F 16 00 
90 96 86 0D 1B 7E F3 CD 37 C3 87 0D 0B 0B 0B DD B8 71 03 FD 27 F9 D1 A3 47 FB 23 22 A4 7B F3 B8 
45 8B 16 0B E6 CF 6B DE BC 39 21 44 20 10 EC DC 19 88 C6 1E 2A 4F 74 DA 70 13 13 13 1E 8F F7 A5 
69 11 41 02 CF 9E 3D 63 96 3B 74 E8 20 BB 13 89 F6 48 C6 BD 70 50 7C F5 AE 98 AE AC AC 3C 70 E0 
C0 C9 93 27 D9 0E 02 50 DF 35 68 D0 60 2C 97 6B 33 66 0C FD F2 C2 85 8B 4F A4 5D EC F6 EE DD 7B 
CE 1C 17 7A 19 8D 3D 54 5E B5 69 C3 E9 C9 0E 97 2C 59 22 3A 2D 62 66 66 26 DB 31 95 95 50 28 A4 
27 95 A4 B5 6F DF 5E 76 E7 6A DD BA 35 D3 D3 31 2B 2B AB B6 3F B6 6F DF BE E5 F3 F9 8F 1F 3F C6 
B3 08 90 8F 7A 57 4C A7 A6 A6 EE DE BD 9B ED 14 00 40 08 21 9A 9A 9A 03 07 9A D2 CB 79 79 79 4F 
A4 3D 0D 04 87 C3 B1 9F 3C 59 B4 B1 47 6A 5A 9A 74 4F 01 0A A2 DA B4 E1 D3 A7 4F A7 9F 40 DA D8 
D8 78 7A 7A D2 2B D3 D3 D3 77 ED DA 55 56 56 C6 5E 4C 25 F6 FA F5 EB 1B 37 6E D0 CB FD FA F5 6B 
DB B6 AD EC CE A5 AF AF 6F 62 62 42 2F 5F BA 74 29 2F 2F AF 56 BB E7 E4 E4 2C 5C B8 D0 C0 C0 A0 
75 EB D6 87 0F 1F 96 41 40 80 FF A8 5F C5 74 46 46 C6 B2 65 CB 6A 18 1D 13 00 E4 AC 81 C8 B8 57 
2F 5E BC 90 FA F1 AB 35 F6 D8 B6 6D 9B 4C 27 9B 00 B6 5C BC 78 91 99 36 DC DC DC 7C C9 92 25 F4 
58 78 EA EA EA 9E 9E 9E 36 36 36 F4 5B C1 C1 C1 F1 F1 F1 42 A1 90 B5 A0 4A EB C6 8D 1B 4C C7 83 
9E 3D 7B 4A 71 6C F8 4F 35 6B D6 8C 29 A6 D3 D3 D3 CF 9E 3D 2B FE 25 AB AC AC 3C 75 EA 14 7D 13 
5D 43 43 C3 C8 C8 48 56 29 01 FE 55 8F 8A E9 8C 8C 0C 77 77 77 FA 09 20 00 28 88 AA CA 4A 59 9F 
A2 67 AF 5E CE 33 66 D0 CB 77 EF FE 15 B6 6F 9F E0 23 1E FE AA 94 82 82 82 80 80 00 FA 46 89 9E 
9E DE DA B5 6B 3B 76 EC C8 BC DB A6 4D 9B 25 4B 96 30 7D DA FC FD FD EF DC B9 C3 4A 4E E5 55 56 
56 F6 CB 2F BF 30 BD 0F 2D 2C 2C 64 3A 6E 37 87 C3 B1 B6 B6 66 EA F5 F0 F0 70 F1 07 FC B9 7B F7 
6E 54 54 14 BD 6C 6E 6E DE A5 4B 17 99 44 04 10 51 2F 8A 69 A1 50 98 96 96 36 73 E6 4C 54 D2 00 
0A A5 B4 B4 F4 7C 72 32 F3 B2 5D BB 76 B2 38 8B BA 9A DA D4 A9 53 CC 06 0D A2 5F 46 45 1D 3A 1E 
7F 5C 16 27 02 56 94 95 95 F9 F9 F9 31 9D 0B E7 CD 9B 37 78 F0 E0 6A DB 98 9B 9B 33 53 8B 67 66 
66 FE FC F3 CF 45 45 45 72 4D A9 CC AA AA AA E2 E2 E2 C2 C2 C2 E8 97 E6 E6 E6 23 46 8C 90 F5 49 
7B F6 EC 39 76 EC 58 7A 39 3D 3D DD DB DB BB B0 B0 F0 AB 7B 15 16 16 FA FA FA 32 2D E3 ED ED ED 
E9 A7 52 00 32 A5 FA C5 B4 40 20 88 89 89 99 3A 75 EA AD 5B B7 D8 CE 02 00 FF 4F 50 59 B9 2F 3C 
3C 29 E9 0C FD B2 4B 97 2E 1D 64 D6 A5 A9 55 AB 56 5E 5E 9E 4C 63 8F 8C 8C 1B 32 3A 11 C8 99 50 
28 4C 48 48 60 EE 44 DA D9 D9 39 3B 3B 7F 3A 6A 9B BA BA BA B3 B3 B3 9D 9D 1D FD 32 3E 3E 7E FF 
FE FD E8 9D 26 8E B2 B2 B2 6D DB B6 31 ED CE 09 21 13 27 4E 14 1D BA 4E 46 34 35 35 67 CD 9A C5 
9C 28 21 21 61 FC F8 F1 E9 E9 E9 55 55 55 9F DD 5E 28 14 DE B8 71 C3 C1 C1 21 21 21 81 C9 39 EC 
DF F1 37 01 64 4A C5 8B E9 A2 A2 22 6F 6F EF A9 53 A7 A2 9D B4 A2 A9 AA AA CA CC CC DC BC 79 F3 
E8 D1 A3 5B B5 6A 45 8F 54 38 68 D0 A0 55 AB 56 65 64 64 7C E9 D7 A5 3C 65 65 65 F5 EE DD 9B 0E 
16 1D 1D CD 76 1C D5 21 14 0A 5F BF 7E 7D E1 C2 45 47 07 C7 C0 C0 20 66 FD E8 D1 A3 F4 64 D9 A5 
A9 5F FF FE 4C 63 0F 50 19 19 19 19 3E 3E 3E 74 F3 03 63 63 E3 9F 7F FE 59 57 57 F7 B3 5B EA EA 
EA FA F8 F8 30 C5 D9 9E 3D 7B D2 D0 1B F5 0B 84 42 61 49 49 49 66 66 E6 CE 9D 3B 07 0D 1A B4 64 
C9 12 A6 81 87 9D 9D DD 94 29 53 38 1C 8E 1C 62 F4 E9 D3 C7 DD DD 9D 79 99 96 96 36 70 E0 40 5B 
5B DB F8 F8 F8 67 CF 9E D1 9F 85 84 42 E1 AB 57 AF 92 93 93 9D 9C 9C 86 0E 1D 9A 94 94 44 6F AC 
AF AF 3F 6F DE BC 96 2D 5B CA 21 A7 4C 55 54 54 24 27 27 FB F8 F8 0C 1F 3E 9C F9 5B D9 B7 6F DF 
19 33 66 C4 C6 C6 BE 7A F5 EA AB 47 F0 F3 F3 A3 F7 72 75 75 15 9D 19 54 7C 69 69 69 9C 3A 10 F3 
07 ED EA D5 AB 6D DB B6 A5 77 69 DB B6 ED D5 AB 57 C5 8C F7 F2 E5 CB D1 A3 47 8B 19 A6 59 B3 66 
83 07 0F 9E 31 63 C6 91 23 47 9E 3F 7F 2E C1 BF C6 67 7D 71 D0 75 65 57 55 55 75 EE DC 39 1F 1F 
9F 6B D7 AE B1 9D 05 AA 7B FA F4 E9 CA 95 2B 0F 1E 3C 58 6D FD 95 2B 57 AE 5C B9 B2 6E DD 3A 8A 
A2 02 02 02 BA 75 EB C6 4A 3C A8 BB C9 F6 53 6A B5 7D 57 43 C3 09 13 26 A8 8B 74 46 94 3A 75 35 
B5 C9 93 7F BA 74 F9 32 9A 7B 29 08 5F 5F 5F 5F 5F DF DA EE 95 9A 9A CA 0C 1D 5D 58 58 B8 6E DD 
3A FA 5E 89 B6 B6 F6 CA 95 2B 7B F6 EC 59 C3 BE FD FA F5 5B B1 62 85 8B 8B 0B F9 77 5A 44 23 23 
A3 36 6D DA 48 14 5F 15 D4 F6 12 98 9A 9A AE 5F BF FE 4B 1F 57 24 3E 2C 4D F4 CA D2 D4 D4 D4 DC 
DC DC 5E BF 7E ED EF EF CF AC E4 F3 F9 7C 3E BF E6 43 E9 EB EB 6F DB B6 CD CC CC AC B6 19 14 4A 
51 51 51 58 58 58 68 68 E8 A7 77 03 6F DE BC 79 F3 E6 CD C8 C8 48 1D 1D 1D 57 57 D7 F9 F3 E7 7F 
F5 A2 28 B8 CA CA 4A 3E 9F CF F4 0E CF CF CF 4F 4A 4A 1A 30 60 80 D4 3F B6 95 96 96 A6 A4 A4 A4 
A4 A4 44 46 46 6A 6B 6B 7B 7A 7A 2E 5F BE 9C 1E 3D B3 2E 54 F0 CE B4 50 28 BC 75 EB D6 B4 69 D3 
46 8E 1C 59 AD 92 B6 B6 B6 B6 B5 B5 65 2B 18 D0 32 33 33 27 4E 9C F8 69 25 2D 8A CF E7 4F 9E 3C 
F9 F2 E5 CB 72 4B 05 2C D2 D5 D5 F5 5D ED AB 2F CB 39 20 68 DF 7C F3 8D A7 A7 07 DA 50 AA 06 81 
40 10 16 16 C6 3C D3 77 74 74 B4 B3 B3 AB F9 4F 2F 87 C3 99 32 65 CA EC D9 B3 E9 97 98 16 B1 56 
AC AD AD A3 A2 A2 8C 8D 8D E5 79 52 2D 2D 2D 5F 5F DF C0 C0 40 F1 CB 1D 23 23 A3 BD 7B F7 7E F5 
9B 41 91 D1 8D D4 2D 2D 2D 57 AC 58 51 F3 73 F5 E2 E2 62 7F 7F 7F 3B 3B 3B 66 D4 42 25 F5 FC F9 
F3 6A 7F F1 2F 5C B8 50 50 50 20 D3 93 96 96 96 FA FB FB 2F 5F BE BC EE C3 65 AA 5A 31 5D 50 50 
30 63 C6 8C DE BD 7B C7 C4 C4 54 7B CB D9 D9 F9 C0 81 03 FD FA F5 63 25 18 D0 0A 0B 0B BD BD BD 
C5 B9 35 78 EB D6 AD 25 4B 96 3C 7E FC 58 F6 A1 80 4D D6 D6 23 E3 62 63 CD E5 75 0F C9 D4 D4 D4 
D1 D1 41 3E E7 02 D9 11 0A 85 47 8F 1E DD BC 79 33 FD 72 D8 B0 61 CB 97 2F D7 D4 D4 FC EA 8E 5A 
5A 5A 0B 16 2C 30 35 FD 67 74 F3 A0 A0 A0 B8 B8 38 19 06 55 09 F4 8D DE E3 C7 8F 33 13 A9 C8 93 
86 86 86 87 87 47 4A 4A 8A BD BD 7D CD 5B 6A 6B 6B 2F 5B B6 2C 25 25 85 7E E8 2F 9F 78 52 27 10 
08 B6 6E DD EA EC EC 9C 95 95 25 E6 2E 69 69 69 6E 6E 6E 19 19 19 32 0D 26 53 97 2F 5F A6 07 5E 
B4 B7 B7 1F 3D 7A 34 21 E4 EC D9 B3 F2 B9 A1 16 1C 1C BC 6F DF BE 3A 0E 97 A9 6A C5 74 49 49 C9 
1F 7F FC 51 6D A5 91 91 51 74 74 74 70 70 70 7D 7E 9C A7 08 84 42 E1 C9 93 27 99 3B 49 46 46 46 
81 81 81 4F 9F 3E FD F8 F1 A3 50 28 FC F8 F1 E3 83 07 0F 16 2F 5E CC DC 81 48 4B 4B DB BF 7F 7F 
A5 EC 87 4E 03 79 52 57 57 37 32 32 1A 3D 6A D4 D6 2D 5B AE 5C BE B4 77 CF 9E 0E 1D 64 38 95 5A 
F5 B3 AB A9 4D B1 B7 EF 8F 0F D5 4A EE DE BD 7B 81 81 81 74 43 5E 7D 7D FD D5 AB 57 8B 3F 14 4C 
B7 6E DD BC BC BC 98 69 11 77 EC D8 81 69 11 3F 65 64 64 F4 E3 8F 3F 6E DA B4 29 3D 3D FD FE FD 
FB 0B 16 2C 90 E9 58 78 35 E3 70 38 26 26 26 D1 D1 D1 F9 F9 F9 31 31 31 4E 4E 4E 03 07 0E 64 DE 
ED D3 A7 8F 93 93 53 4C 4C CC 83 07 0F 36 6E DC A8 D4 0D 1E E8 4F 89 7E 7E 7E 4C 23 75 6D 6D 6D 
7B 7B 7B 3E 9F 5F 50 50 40 FF AD 14 0A 85 A5 A5 A5 E9 E9 E9 1E 1E 1E CC 9F CB F4 F4 74 3F 3F 3F 
71 06 3C A9 A3 D4 D4 54 61 2D 55 6B BD F3 A9 F7 EF DF 5F B8 70 81 5E 1E 32 64 C8 C8 91 23 E9 65 
1E 8F 57 DB 7B C6 6B D7 AE AD 39 4C 79 79 79 4E 4E CE B6 6D DB 44 07 20 8F 89 89 91 CE 9D BB DA 
FE D3 28 AC 7B F7 EE 31 23 BD D3 1C 1C 1C 1E 3D 7A C4 6C B0 76 ED DA 5A FD BB 2B 3B 85 BA BE C5 
C5 C5 4C 6F 7A 1B 1B 9B C7 8F 1F 7F BA 4D 55 55 D5 E9 D3 A7 99 4E 42 43 87 0E CD CB CB 93 7F 54 
E1 7F BF 97 0E 1D 3A C4 4A 86 AF 52 A8 EB 0B 52 87 EB AB DA 70 7D 55 9B 04 D7 37 35 35 55 74 A4 
14 6B 6B 6B BA 47 FE 67 37 AE AA AA BA 76 ED 9A 68 A9 EA EF EF 2F 10 08 AA 6D C6 94 3D 73 E6 CC 
29 2F 2F 97 E0 0B 49 4D 4D 65 4E 21 41 31 FD 55 7F FE F9 27 DD 7C 48 4F 4F EF FA F5 EB E9 E9 E9 
F4 10 E3 7A 7A 7A E9 E9 E9 5F DD FD C5 8B 17 A3 46 8D AA 6D 51 F7 D7 5F 7F 31 4F A8 08 21 C7 8E 
1D AB 6D 6C D1 EB AB 6A 77 A6 45 D9 D9 D9 65 64 64 44 46 46 8A 8E DE 0F 2C CA C9 C9 B9 72 E5 0A 
21 44 5B 5B DB CB CB EB B3 83 2B 71 38 9C D1 A3 47 7B 79 79 D1 2F 33 32 32 9E 3C 79 22 D7 94 00 
00 00 72 F7 E6 CD 1B D1 EE 86 74 E7 A2 BE 7D FB 7E A9 C9 0A 87 C3 E9 DF BF 7F 58 58 18 53 14 46 
45 45 89 3F BB 8D E2 48 4D 4D A5 9F 0E 99 98 98 E8 EB EB 1B 1A 1A D2 4F 1E E8 6E 88 42 D9 CC 57 
6A 6C 6C BC 7A F5 6A E6 E5 ED DB B7 EB 72 22 D5 2C A6 ED EC EC 52 52 52 E2 E2 E2 6A F8 2E 04 F9 
CB CB CB A3 FB EA 76 EA D4 A9 86 61 4A 39 1C 8E 95 95 15 DD 38 AF B4 B4 14 C3 1A 02 00 80 CA BB 
76 ED 5A 7C 7C 3C BD 4C 0F 9C D2 BA 75 EB AF EE 65 6C 6C CC 8C 02 9E 99 99 C9 0C 0E A8 2C 5E BD 
7A 95 98 98 48 2F 0F 18 30 A0 65 CB 96 2D 5B B6 B4 B4 B4 A4 D7 C8 B4 1B 62 A7 4E 9D 98 E7 CF 05 
05 05 EF DE BD 93 F8 50 AA 56 4C B7 6D DB F6 F4 E9 D3 C7 8E 1D B3 B0 B0 68 D0 40 D5 BE 3A 65 37 
76 EC 58 FA 81 C8 1F 7F FC 21 DA 5C E9 53 1A 1A 1A 4D 9A 34 A1 97 AB F5 B5 8F 8E 8E 16 1D 32 53 
28 14 3E 7E FC 78 F3 E6 CD 56 56 56 CD 9A 35 E3 70 38 DD BA 75 9B 31 63 C6 99 33 67 DE BF 7F 5F 
73 9E 4F F7 ED DB B7 EF BA 75 EB 70 2F 1C 00 00 E4 E9 C3 87 0F A7 4E 9D 62 9A 4A 7B 7A 7A 8A DF 
DD 73 CC 98 31 74 13 4A 23 23 A3 97 2F 5F 4A 36 98 34 5B B2 B3 B3 99 47 D6 43 86 0C 51 53 53 23 
84 8C 18 31 82 FE F2 E5 D6 0D B1 8E 54 6D 9C 69 6D 6D ED BA 8F 17 08 AC 13 0A 85 CC BC 2D 35 B4 
D2 79 F3 E6 CD BA 75 EB 82 82 82 98 5F 40 84 90 AC AC AC AC AC AC C8 C8 48 6B 6B EB 9D 3B 77 7E 
69 B0 EA D2 D2 D2 8D 1B 37 56 DB 97 1E BC 73 FB F6 ED DB B6 6D EB DF BF BF 74 BE 18 00 00 80 1A 
BD 78 F1 E2 E6 CD 9B F4 B2 99 99 99 85 85 85 F8 FB B6 6C D9 72 D3 A6 4D 61 61 61 3A 3A 3A CA F5 
34 5E 74 78 69 2B 2B AB BE 7D FB D2 EB 3B 77 EE 6C 6E 6E 9E 9D 9D 4D 08 E1 F1 78 A3 46 8D 92 45 
FF D7 EB D7 AF 33 73 63 B7 69 D3 A6 71 E3 C6 12 1F 0A F7 6E 41 11 DD BF 7F FF CE 9D 3B 84 10 33 
33 B3 6F BF FD F6 B3 DB 14 17 17 2F 5E BC D8 DF DF 5F B4 1A 16 95 94 94 E4 E4 E4 44 FF 34 56 53 
54 54 E4 EE EE FE A5 7D 8B 8B 8B 3D 3D 3D 0F 1C 38 A0 08 13 31 02 00 80 CA 7B F2 E4 09 33 B6 9D 
A9 A9 29 DD 03 4F 7C 86 86 86 F4 FC 88 32 88 26 43 85 85 85 29 29 29 F4 B2 85 85 45 8B 16 2D E8 
65 2D 2D 2D 2B 2B 2B 7A 39 31 31 F1 EE DD BB 52 3F 75 46 46 46 50 D0 FF 4F C1 DB AB 57 AF BA FC 
EB A1 98 06 85 53 56 56 C6 B4 1B EB DF BF FF 97 06 34 8C 8D 8D 3D 74 E8 10 21 C4 DE DE 3E 25 25 
E5 FD FB F7 42 A1 F0 FD FB F7 89 89 89 03 06 0C A0 B7 49 4F 4F 8F 8B 8B AB 36 B8 9E 40 20 D8 B1 
63 47 54 54 14 FD 92 A2 A8 0B 17 2E D0 7D 9C E9 01 7A 28 8A 2A 2D 2D 0D 08 08 A0 0B 7A 00 00 00 
99 7A F8 F0 21 73 73 C7 C8 C8 A8 51 A3 46 EC E6 91 8F 2B 57 AE 24 27 27 13 42 0C 0D 0D AD AC AC 
44 CB 59 33 33 33 BA 63 65 7E 7E 3E 9F CF 97 CA 20 B9 55 55 55 AF 5E BD BA 7A F5 EA FC F9 F3 AD 
AD AD 99 29 2F 86 0D 1B 26 3A B2 87 04 50 4C 83 62 11 0A 85 09 09 09 C7 8E 1D 23 84 E8 E9 E9 8D 
1F 3F 5E 43 43 A3 86 ED FD FD FD 23 22 22 2C 2C 2C E8 5F 3D 8D 1A 35 B2 B6 B6 8E 8B 8B 1B 36 6C 
18 BD C1 C5 8B 17 5F BD 7A 25 BA CB A5 4B 97 22 22 22 E8 E5 B9 73 E7 1E 3E 7C 78 F0 E0 C1 F4 74 
0F 8D 1A 35 1A 3C 78 F0 D1 A3 47 7F FE F9 67 19 7C 71 00 00 00 9F F1 FC F9 73 66 59 CE D3 4C D6 
8A 85 85 05 A7 36 D2 D2 D2 BE 74 A8 8A 8A 0A A6 BB A4 B9 B9 79 E7 CE 9D 45 DF 6D D7 AE 1D 33 21 
FC E5 CB 97 45 FF 7D 6A E0 EB EB 5B 43 18 35 35 35 1D 1D 1D 53 53 D3 9D 3B 77 16 17 17 D3 BB 68 
6B 6B BB B8 B8 88 3F 50 FD 67 A1 98 06 C5 72 F1 E2 45 1F 1F 1F FA 03 FA 8C 19 33 CC 6A 9C 18 6F 
E2 C4 89 AE AE AE 9F 56 DB 1D 3A 74 F8 E9 A7 9F E8 E5 BC BC BC 17 2F 5E 30 6F 7D F8 F0 E1 C4 89 
13 74 0B 2D 1B 1B 1B 5F 5F DF 4F 1B D9 6B 6A 6A 2E 58 B0 C0 C1 01 F3 E4 01 00 80 3C BC 7D FB 96 
59 A6 3B E1 A9 BC 9C 9C 9C 8B 17 2F D2 CB 16 16 16 D5 5A 45 37 6A D4 E8 87 1F 7E A0 97 65 D7 0D 
51 5B 5B 7B D5 AA 55 13 26 4C A8 E3 71 50 4C 83 02 F9 F3 CF 3F 97 2D 5B 46 8F 85 67 6B 6B EB E5 
E5 A5 AE 5E 53 1F D9 11 23 46 B4 6C D9 F2 B3 6F 7D F7 DD 77 F4 C2 9D 3B 77 5E BE 7C C9 AC CF CF 
CF 67 9E EC D8 D9 D9 7D A9 0D 49 B3 66 CD 1C 1C 1C D0 99 15 00 00 40 16 98 E1 A5 4D 4D 4D 87 0F 
1F FE E9 06 DF 7D F7 1D D3 72 5A 82 D9 10 BF 6A C0 80 01 C7 8F 1F 5F B4 68 51 CD 95 86 38 50 4C 
83 A2 C8 C8 C8 98 35 6B 16 5D E9 9A 9A 9A 6E D8 B0 E1 AB 43 6C 32 15 F3 A7 1A 37 6E FC D9 0E 1C 
F9 F9 F9 74 4B 68 43 43 43 A6 69 F5 67 19 1B 1B F7 C3 A4 D3 00 00 00 D2 26 3A BC B4 A9 A9 69 DB 
B6 6D 3F DD A6 4D 9B 36 43 86 0C A1 97 A5 D8 0D 71 E0 C0 81 2B 57 AE BC 7A F5 EA A5 4B 97 AC AC 
AC A4 32 8C 32 8A 69 60 9F 50 28 4C 4E 4E 9E 3A 75 2A 5D 49 9B 98 98 6C DF BE FD AB 8D C6 4C 4C 
4C FE F7 BF FF 7D E9 DD A6 4D 9B 7E F3 CD 37 9F AE 67 3A 79 B4 6B D7 AE 86 DD 09 21 2D 5B B6 AC 
79 30 6C 00 00 00 A9 10 9D C8 AC BC BC 9C C5 24 35 AB ED 74 E2 A2 B3 9D 8B FA EB AF BF CE 9E 3D 
4B 2F 07 06 06 36 6E DC F8 D3 26 CE 0D 1A 34 58 B5 6A 15 BD 8D 98 DD 10 3F 9D 4E FC E3 C7 8F B7 
6F DF 66 DA 6D EA E8 E8 4C 9A 34 69 F9 F2 E5 03 06 0C A8 FB 0D 69 06 8A 69 60 59 55 55 55 5C 5C 
9C 93 93 53 56 56 16 21 C4 D4 D4 34 3C 3C 7C D0 A0 41 32 3A 1D D3 89 41 43 43 A3 E6 AE 8D 8D 1A 
35 D2 D1 D1 91 51 0C 00 00 00 86 E8 A3 D4 9C 9C 1C 16 93 C8 41 65 65 65 62 62 E2 97 86 B5 FD 92 
94 94 94 C2 C2 C2 DA 9E 4B 5D 5D BD 67 CF 9E E1 E1 E1 41 41 41 DA DA DA C5 C5 C5 0B 17 2E 1C 37 
6E DC 67 87 CD 95 18 8A 69 60 D3 FB F7 EF 77 EF DE 3D 73 E6 4C BA 9D B4 B9 B9 79 78 78 B8 4C 1B 
57 88 76 F2 A8 99 9A 9A 1A 3D C4 07 00 00 80 4C B5 6E DD 9A 99 F2 30 2B 2B EB C3 87 0F B5 DA FD 
ED DB B7 7C 3E FF F1 E3 C7 D5 E6 0C 56 4C A2 C3 4B 8B 2F 39 39 99 9E 2B 51 02 EA EA EA AE AE AE 
2B 56 AC A0 5F 26 25 25 79 78 78 48 B1 9E 46 31 0D AC 79 FA F4 E9 8C 19 33 BC BC BC E8 8F A7 13 
27 4E FC E5 97 5F 7A F4 E8 21 D3 93 36 6D DA 54 A6 C7 07 00 00 A8 2D 7D 7D 7D 13 13 13 7A F9 D2 
A5 4B 79 79 79 B5 DA 3D 27 27 67 E1 C2 85 06 06 06 AD 5B B7 3E 7C F8 B0 0C 02 4A 13 33 BC 74 6D 
D5 A5 1B A2 BA BA BA 87 87 87 9B 9B 1B FD 32 29 29 69 D9 B2 65 45 45 45 92 1D AD 1A 14 D3 C0 8E 
CB 97 2F 73 B9 DC 98 98 18 FA E5 F2 E5 CB C3 C3 C3 EB 38 D0 A3 38 98 86 D4 EF DF BF 7F FF FE 7D 
0D 5B BE 7B F7 AE A0 A0 40 D6 79 00 00 00 9A 35 6B C6 14 D3 E9 E9 E9 67 CF 9E 15 0A 85 62 EE 5B 
59 59 79 EA D4 29 FA 3E AB 86 86 86 82 F7 F6 11 1D 5E DA CA CA EA EF BF FF AE B9 D5 F5 BB 77 EF 
BC BC BC E8 ED EB D8 0D 51 4B 4B 6B FE FC F9 CC FC 2C F1 F1 F1 FB F7 EF 97 CA BD 7C 14 D3 20 6F 
42 A1 F0 DC B9 73 F6 F6 F6 B7 6E DD 22 84 E8 E8 E8 44 46 46 FA F9 F9 C9 67 1C BA CE 9D 3B D3 27 
CA CA CA A2 47 9B FE 92 8A 8A 0A BA F1 09 00 00 80 4C 71 38 1C 6B 6B 6B A6 E5 74 78 78 F8 BD 7B 
F7 C4 DC F7 EE DD BB CC 9C BE E6 E6 E6 5D BA 74 91 49 44 29 11 1D 5E 7A D0 A0 41 9F 1D 2A 40 94 
86 86 06 45 51 F4 72 DD 67 43 34 34 34 F4 F6 F6 66 EA 8D 3D 7B F6 D4 30 AD 8C F8 50 4C 83 BC 5D 
BC 78 D1 D9 D9 99 AE 53 8D 8C 8C 8E 1D 3B E6 E0 E0 20 C5 4E B5 35 EB D0 A1 03 DD 26 3B 3F 3F FF 
C2 85 0B 35 7C F4 CF CE CE BE 71 E3 86 7C 52 01 00 40 3D D7 B3 67 CF B1 63 C7 D2 CB E9 E9 E9 DE 
DE DE E2 F4 B7 2B 2C 2C F4 F5 F5 A5 07 6C 26 84 D8 DB DB 37 6F DE 5C 86 29 EB 2C 29 29 89 4E AB 
AD AD 3D 6A D4 28 71 66 A8 11 1D 70 5A B2 6E 88 A2 46 8F 1E ED E2 E2 42 2F E7 E6 E6 EE DC B9 B3 
EE 8D 3D 50 4C 83 5C E5 E5 E5 AD 59 B3 86 AE A4 4D 4D 4D A3 A3 A3 87 0E 1D CA E1 70 E4 16 A0 75 
EB D6 96 96 96 F4 F2 D1 A3 47 BF F4 D1 FF FD FB F7 47 8F 1E AD F9 D6 35 00 00 80 B4 68 6A 6A CE 
9A 35 8B 19 23 2F 21 21 61 FC F8 F1 E9 E9 E9 55 55 55 9F DD 5E 28 14 DE B8 71 C3 C1 C1 21 21 21 
81 5E 33 71 E2 C4 61 C3 86 C9 29 AE 44 5E BD 7A C5 74 3D B4 B2 B2 EA DE BD BB 38 7B 89 0E 38 5D 
97 6E 88 34 0D 0D 0D 0F 0F 0F 66 CC BE F8 F8 F8 C3 87 0F 8B DF A8 E6 B3 E4 74 3B 10 80 10 22 10 
08 82 83 83 CF 9F 3F 4F 08 D1 D7 D7 DF B4 69 93 FC 67 45 51 53 53 9B 30 61 42 5C 5C 5C 66 66 26 
FD D1 7F F7 C3 3B 77 C5 00 00 20 00 49 44 41 54 EE DD D5 DA 6A 0B 04 82 B0 B0 B0 D0 D0 50 39 67 
AB CF 1E 3C 78 E0 34 C3 F9 AB 7D 6E 74 75 75 BB 74 E9 6C 61 61 41 D9 50 ED DB 7F 5B C3 C7 B0 57 
AF 5E 39 CF 9C F5 C7 1F 7F 10 42 36 6D DA 38 69 E2 C4 6A 1B A4 A7 A7 4F B6 9F 42 2F 5B 5B 8F DC 
12 10 20 66 43 A3 A3 B1 B1 CB 96 2D 27 84 B4 6B D7 2E 32 62 BF 82 3F 51 65 45 45 45 85 B7 B7 4F 
C2 C9 93 84 10 DB B1 63 37 6C F0 17 73 60 1C D1 AB E6 EA 3A 67 D9 D2 A5 5F 7A 57 02 A2 07 7C F9 
F2 A5 97 D7 BC 4B 97 2F 13 42 D4 D5 D5 FD FD D7 4F 18 3F 5E 9C 4F F5 82 CA CA A0 A0 A0 C0 C0 20 
7A C7 4D 1B 37 8E 1B 67 27 59 1E 65 24 E6 25 68 DE BC 79 87 0E 1D 4C 7A F5 B2 B0 B0 30 33 1B F4 
D5 9F 2C 29 5E D9 1A BC 7B F7 EE FA F5 EB 67 7F FF FD FA F5 EB 0F 1E 3C A4 FB CC B4 6F DF BE 47 
F7 EE A3 46 8F 1A 3A 64 48 8B 16 2D 24 0B 20 45 7D FA F4 71 77 77 5F FA EF 97 93 96 96 36 70 E0 
40 8A A2 9C 9D 9D 07 0C 18 D0 A6 4D 1B 75 75 75 A1 50 F8 FA F5 EB 5B B7 6E 45 44 44 C4 C7 C7 33 
03 CC E9 EB EB CF 9B 37 EF 4B B3 02 2B 08 D1 E1 A5 2D 2C 2C C4 FC 37 A7 DB C0 04 07 07 D3 77 B8 
78 3C DE A8 51 A3 AA 4D 3F 5E 2B 1D 3B 76 F4 F0 F0 B8 7D FB 36 FD AF B7 7D FB 76 73 73 F3 FE FD 
FB 4B 7C 40 DC 99 06 F9 C9 CA CA 8A 8F 8F A7 97 73 73 73 E9 7B D2 5F E5 EA EA 5A 51 51 21 C5 18 
3D 7B F6 5C B9 72 25 FD FB 3D 21 21 C1 C6 C6 E6 D0 A1 43 AF 5E BD 22 84 08 04 82 3B 77 EE CC 9C 
39 D3 D3 D3 B3 B6 43 60 82 1C 14 15 15 5D BE 7C 25 20 60 CB 90 A1 43 3D 3C BD EA F8 B0 8F 91 94 
74 E6 F8 F1 F8 3A DE 99 00 25 D2 AA 55 AB C5 8B 17 D1 4F C3 05 02 C1 D6 AD DB EE DE FD 4B 9C 1D 
2F 5E BC 18 1C BC 87 5E 9E 3E 7D DA 58 DB B1 32 4C A9 B4 4A 4A 4A EE DC B9 73 28 3A DA 75 EE DC 
01 DF 9B AE F5 F3 7B F1 E2 05 8B 79 5E BC 78 B1 75 EB B6 81 83 CC A6 3B 38 1E 38 70 F0 EE DD BF 
98 DE E7 4F 9F 3E FD 2D 31 71 C1 82 85 03 07 99 B1 9E 93 10 A2 A6 A6 E6 E6 E6 E6 E3 E3 23 BA 92 
CF E7 8F 1B 37 AE 7D FB F6 0D 1B 36 A4 A7 32 D1 D1 D1 19 36 6C D8 C1 83 07 45 2B E9 6D DB B6 99 
99 99 D5 70 F0 90 90 90 26 4D 9A 88 F3 67 97 C3 E1 7C A9 25 B1 85 85 85 98 47 60 8C 1E 3D FA E5 
CB 97 E4 BF C3 4B EB E9 E9 0D 19 32 44 FC E7 D2 46 46 46 CC BD 64 A9 CC 86 C8 E5 72 27 4F 9E 4C 
2F E7 E6 E6 06 05 05 BD 79 F3 46 E2 A3 A1 98 06 F9 61 5A 4A B1 8B C3 E1 4C 9A 34 89 19 6F F2 D6 
AD 5B D3 A7 4F D7 D1 D1 E1 70 38 0D 1B 36 EC D5 AB D7 C1 83 07 09 21 2B 56 AC 70 72 72 62 33 28 
D4 E8 F4 E9 D3 0E 0E 8E D9 D9 0F A4 72 B4 B0 7D FB A4 3B 86 3F 28 B8 DE BD 7B 2F 98 3F 9F 5E 2E 
2C 2C DC 1C 10 F0 FA F5 EB 9A 77 B9 9F 9D BD 6E DD 7A BA EF BF A9 A9 A9 EB 9C 39 EA 62 34 F7 AC 
E7 DE BF 7F 1F 11 11 39 75 EA B4 DB B7 6F CB FF EC 55 55 55 09 27 4F 8E B1 A1 76 ED DE 5D 52 52 
52 C3 96 EC E6 14 A5 A5 A5 E5 EB EB 1B 18 18 28 7E A7 7C 23 23 A3 BD 7B F7 DA D9 D9 C9 B3 CD A4 
04 9E 3D 7B F6 FB EF BF D3 CB 56 56 56 5D BB 76 15 7F DF E6 CD 9B 8F 1E 3D 9A 5E AE 7B 37 44 42 
88 96 96 D6 82 05 0B 98 11 54 0E 1E 3C 78 F2 E4 49 89 6F A9 A0 98 06 39 29 2F 2F FF EB 2F B1 EE 
FD C8 81 BA BA FA A2 45 8B 0E 1F 3E FC D9 21 84 B4 B5 B5 FD FC FC 16 2E 5C 58 F3 14 89 C0 BA FB 
D9 D9 5B B6 6E 91 CA 33 84 BC BC BC 5D BB 77 2B F2 2C BE 20 5D 1C 0E 67 E2 C4 09 5C EE 3F A3 04 
A4 A4 A4 1C 3C 18 25 F8 F2 9F E7 D2 D2 D2 AD 5B B7 3E 7A F4 88 10 D2 BC 79 73 4F 4F 8F AF 8E 42 
00 8C FB D9 D9 F3 17 2C BC 2F DF CF AB 82 CA CA 5D BB 76 2F 5E BC 44 FC EE 65 74 4E 89 1B 9C 48 
0B DD A8 37 25 25 C5 DE DE BE E6 2D B5 B5 B5 97 2D 5B 96 92 92 32 7A F4 68 05 AF A4 09 21 19 19 
19 97 2E 5D A2 97 87 0C 19 52 DB 21 BC 06 0E 1C 68 6C 6C 4C 2F FF FE FB EF CF 9E 3D AB 63 9E 6E 
DD BA B9 BB BB 33 2F 77 ED DA F5 E0 81 84 77 67 D0 66 1A E4 A4 A2 A2 E2 E9 D3 A7 6C A7 F8 7F EA 
EA EA F6 F6 F6 36 36 36 7C 3E 3F 26 26 E6 D2 A5 4B C5 C5 C5 46 46 46 A3 46 8D 72 76 76 EE D5 AB 
D7 BB 77 EF D8 CE 58 4F 1D 89 39 CC 8C 03 2A 4A 28 14 96 96 96 FE FD F7 DF 27 12 12 22 23 0F D0 
0F 6A CF 9D 3B 9F 92 92 32 66 CC 98 BA 9F 97 C7 E3 9B 9B 9B 4F 9A 38 51 F1 FF 26 81 98 CD 64 6B 
D6 A4 49 13 0F 0F 8F 3F FF BC 4B 97 C8 FB 23 22 FA F5 EF 67 FE B9 07 E5 82 CA CA 7D E1 E1 49 49 
67 E8 97 0B E6 CF 37 1B 34 A8 8E 67 57 76 35 5C 82 B2 B2 B2 17 2F 5F A6 A5 A6 1D 8C 8A CA CA CA 
A2 57 3E 7A F4 C8 D7 77 75 E0 CE 1D 35 7F 08 91 CA 95 25 84 08 85 C2 F8 F8 F8 A0 5D BB 98 51 84 
D5 D5 D5 07 5B 5A 4E 9A 34 A9 6F DF 3E 2D 75 74 E8 A7 0A 65 65 65 F7 B2 B2 8E 1C 39 72 E2 44 02 
BD E5 A3 47 8F 36 6E DA FC D5 9C B2 C6 E1 70 4C 4C 4C A2 A3 A3 B7 6D DB 96 9C 9C 9C 98 98 78 EF 
DE 3D A6 E3 5D 9F 3E 7D 4C 4C 4C 46 8D 1A 35 7C F8 70 65 F9 50 57 56 56 C6 E3 F1 E8 65 63 63 E3 
81 03 07 D6 F6 08 5D BA 74 19 39 72 24 FD 7C FB D2 A5 4B 19 19 19 4C 67 4D C9 70 38 9C 09 13 26 
9C 39 73 26 36 36 96 10 92 9E 9E 1E 18 18 B8 79 F3 66 09 26 3F 46 31 0D 72 D2 AA 55 AB DF 7E FB 
AD EE C7 99 3A 75 EA D4 A9 53 BF BA 99 91 91 91 38 77 17 9A 35 6B 36 65 CA 94 29 53 A6 7C FA 96 
A6 A6 E6 DE BD 7B F7 EE DD 2B 49 4A 90 01 0E 87 D3 AC 59 B3 66 CD 9A 2D EF D6 CD D2 D2 D2 DD DD 
A3 A4 A4 44 20 10 24 25 9D 19 36 6C 98 54 E6 7E 0F 0A DA D5 A7 77 EF 5A 3D 7C 04 A5 66 D8 A5 CB 
DC B9 AE 3E 3E 2B 04 02 41 49 49 C9 8E ED 3B BA 74 EE DC BA 75 EB 6A 9B 5D 4A 4B 0B 0F DF 4F 2F 
8F 1B 67 37 71 E2 04 7C E2 AA 81 96 96 96 96 96 96 FE 94 0E E3 C6 D9 ED DB 17 BE 33 30 90 AE 53 
D3 D3 D3 A3 0E 1D 9A 37 6F 9E 1C 9A C7 5C BD 7A 75 FD 7A 7F A6 92 36 31 31 59 BB E6 E7 9E 3D 7B 
56 BB 70 5A 5A 5A FD FA F6 ED DB A7 CF 14 7B FB E5 CB BD E9 7B E7 F2 CC 59 33 0E 87 D3 A6 4D 9B 
C9 93 27 33 AD 7B 25 B0 6A D5 AA 55 AB 56 D5 25 86 B9 B9 B9 54 BA 94 44 44 44 44 44 44 48 BC BB 
86 86 C6 CE 9D 3B 77 EE DC 59 6D 7D 5D AA 8B 96 2D 5B 1E 3D 7A 54 E2 48 0C 34 F3 00 00 E5 63 6A 
6A 3A 71 C2 04 7A 39 FB C1 83 92 12 C9 3B 8E 10 42 46 8C 18 41 8F 74 9E 97 97 17 12 1A 8A C6 1E 
F5 07 87 C3 A1 6C 6C 7E FC D1 96 7E 79 3D 23 23 24 34 B4 5A 63 8F FB D9 D9 3F AF 59 4B 4F 62 6C 
60 60 30 67 CE 9C 26 4D 9A B0 90 55 09 35 6E DC D8 75 AE AB 9B DB 5C 66 4D 6C 6C DC 03 D9 37 F6 
28 2D 2D DD 1F 11 C1 34 92 B6 B4 B4 0C 0D D9 DB AB 57 AF 2F 7D 04 E2 70 38 7D FA F4 09 DA 15 64 
60 60 20 CF 9C A0 32 50 4C 03 80 F2 51 57 53 33 EC 6A 48 2F 97 94 94 BC 7D 5B A7 66 D3 53 EC 27 
8F 1D CB A5 97 4F 9E E4 9D 3A 7D 1A 23 7B D4 1F 9A 9A 9A 1E 1E 1E 5D 0D FF F9 76 8A 8A 3A 94 94 
98 C8 BC 5B 5E 5E 1E 12 12 42 B7 03 51 57 57 5F BC 68 21 B3 25 88 43 5D 4D 6D 8E 8B 0B 33 80 60 
61 61 E1 D9 DF 7F 97 F5 CF D7 8D 1B 37 CF 9D 3B 4F 2F 1B 18 18 AC F6 5D 25 4E 5B 88 AE 86 86 AE 
AE 73 E8 E5 C2 C2 C2 DF CF 9D 93 61 44 50 2D 28 A6 01 40 B9 69 6A 6A D6 B1 AB A8 96 96 D6 1C 17 
17 7A B8 71 81 40 B0 67 CF DE 6C 49 BB A1 80 32 D2 EF D0 61 D9 F2 65 F4 D3 09 81 40 B0 65 EB B6 
87 0F 1F 12 42 84 42 E1 81 83 07 8F 1F FF 67 40 4F 97 D9 B3 AD 47 8D 62 33 A8 72 6A D2 A4 C9 94 
29 53 98 51 81 D3 D3 AF CA 74 E0 D1 8F 1F 3F FE 96 98 C8 34 F0 70 75 9D D3 B9 73 67 31 F7 B5 1E 
39 92 6E 0D AF AB AB 5B 5C 5C 8C 9E 33 20 26 14 D3 00 A0 7C 04 95 95 D9 F7 FF 79 08 6B 60 D0 51 
47 47 A7 8E 07 34 34 34 F4 F4 F4 A0 97 1F 3D 7A 14 12 12 82 C6 1E F5 CA E0 C1 83 5D 66 CF A6 97 
1F 3D 7A B4 37 24 A4 A2 A2 E2 EA D5 AB 21 21 FF 4C DE 64 6A 6A EA E8 E8 C0 7A 23 5A 25 65 DC AD 
9B A5 85 05 BD FC F0 E1 C3 02 29 8D 10 FF 59 2F 5F 16 33 C3 DB 75 E9 D2 65 50 6D 3A BA B5 68 D1 
C2 CF 6F 6D C6 F5 6B E9 57 2E AF 5A B9 B2 71 E3 C6 B2 C9 08 AA 06 C5 34 00 28 9F F4 F4 F4 D8 B8 
38 7A D9 D2 D2 B2 2E 53 61 D1 38 1C 0E 97 A2 98 81 D2 4E 9E E4 FD F6 5B 62 CD BB 80 2A 51 57 53 
73 74 74 60 86 91 39 71 22 21 26 E6 48 60 60 10 DD EE B6 79 F3 E6 0B E6 CF 53 96 61 13 14 50 93 
26 4D BE EB F9 1D BD 9C 9F 9F 5F F7 41 CD 6A F0 EC D9 D3 FB F7 EF D3 CB FD FB F7 6F D3 A6 4D AD 
76 EF D4 A9 13 3D ED 80 0C A2 81 CA AA 77 A3 79 D4 BD 5B 2B 00 88 E9 E3 C7 8F 65 65 65 4D B5 B5 
A5 75 3F AF AC AC EC E9 D3 A7 A2 43 E3 F5 E8 D1 DD 6A C4 08 A9 1C BC 49 93 26 1E EE EE 37 6E DC 
CC CB CB 13 08 04 BB 76 EF 36 31 E9 25 FE 03 62 95 27 A8 AC 7C 5B 5A AA A5 A5 D5 B0 61 43 F1 F7 
4A 38 79 92 9E 57 5C F1 7D F3 CD 37 0B E6 CF 9B E3 3A 97 1E 25 C6 6F DD 3A E6 2D 6F EF E5 DF 7F 
FF 3D 8B D9 64 4A EA 3F A7 9F C5 8C 10 4C 08 79 2E CB 3B D3 39 8F 1E 31 6D 3C BA 1A 1A D6 EA DB 
15 40 32 F5 AE 98 06 00 B9 29 2B 2B 73 77 F7 68 DF BE BD AF EF 2A F1 07 40 98 6C FF 99 91 0A 3F 
4B 57 57 D7 DB DB 5B 4F 4F 4F D2 80 D5 19 1A 1A CE 9E 35 EB E7 35 6B C8 BF CF FA D7 AE 59 23 95 
41 F7 54 40 55 65 E5 86 0D 1B F3 0B 0A B6 04 6C 66 FD 1E ED DE BD 21 7B F7 86 88 BF BD 98 A3 17 
7F FF FD F7 73 E6 B8 6C DE 1C 20 BA 72 DC 38 3B 2E 45 A9 F0 AD 4A C9 7E 4E 6B 4B 4B E4 C8 B9 4F 
9E 7C 69 B3 BA 5F 59 D1 29 5A BA 1A 61 98 4B 90 07 34 F3 00 00 59 69 D1 A2 C5 D4 A9 53 8E 1D 3F 
BE 33 30 50 EA 5D 79 06 0C 18 70 E8 50 D4 67 A7 D8 90 18 87 C3 19 37 CE CE DA 7A 24 FD F2 C4 89 
84 5F 7F 95 C2 E0 E8 AA A1 51 A3 46 93 27 FF 74 FB F6 ED 75 EB D7 BF 7A F5 95 99 B7 95 14 87 C3 
99 36 75 2A F3 0D 40 08 31 30 30 70 9B 3B 57 B5 C7 C2 93 E9 CF 29 A3 69 53 ED 56 AD 5A C9 E8 E0 
A2 DE BE 7D CB 2C A3 8D 3B C8 07 8A 69 00 90 21 4B 4B CB E1 C3 87 85 86 86 6D DA BC 59 BA 5D FA 
9E 3D 7B 96 92 92 22 F5 6E 82 DA DA FF C7 DE DD C7 C5 98 FD FF 03 3F A3 F9 4A DA 89 B2 24 21 77 
49 AC 8D A5 AD 24 B9 A9 B4 D8 DA 3E CB DA B2 95 AC C8 5D B4 48 6A D9 FD 4A AD 7B 4A 42 7C 59 A5 
CD 62 25 B2 5F 4A 92 54 92 90 DB 72 6F DD 94 DC 44 63 BA D1 4C F3 FB E3 7C 3E D7 77 7E DD 8C 99 
AB 99 66 9A 5E CF C7 3E 1E 7B CD 74 CD 35 27 E7 3A CD 7B CE 79 9F 73 78 0B E6 2F A0 DB 76 08 85 
C2 9D 3B 77 4A E9 45 6B 6D 06 7F FE F9 BF FE E5 76 FC 78 F2 B2 A0 65 AF 5F BF 56 75 71 94 42 24 
12 55 56 FE 5F 40 F9 E6 CD 1B A5 CE 96 53 13 CA 6B A7 0C 6D ED B6 98 CF 07 9A 0A C1 34 00 28 11 
8F C7 F3 9B 3D BB 43 87 0E BF FF BE 6F C5 CA 95 0A EC D1 2C 2E 2E 5E BD 3A CC CD ED 5F 85 85 85 
8A BA 26 35 68 D0 C0 39 7E 7E F4 F8 CE DD BB 31 31 31 1F 3E 7C 50 EC 5B B4 50 5C 2D 2D 6F 6F EF 
FE A6 A6 A9 A9 A7 FD FD 17 3E 79 F2 E4 A3 2F 71 75 71 B9 75 F3 C6 C3 07 F7 65 F9 EF 72 FE A5 21 
43 86 34 C3 2F D2 18 A1 48 B4 F7 F7 DF 33 33 33 99 67 E8 B6 88 2F 34 3D 9E 56 5E 3B 65 BC 7D FB 
56 E3 FF 19 A1 D5 42 CE 34 00 28 D7 90 21 43 96 2F 0F 0A 0A 5A 7E E4 48 E2 93 27 4F 57 AF 0E 95 
BE ED C5 81 84 3F 98 45 15 EA A8 A9 A9 29 2B 2B BB 71 F3 66 FC FE F8 33 E9 E9 84 90 3B 77 EF CE 
9D 37 7F 57 CC 4E 05 CE 14 E4 70 38 AE AE 2E 69 67 CE D0 A0 EA E0 C1 43 B6 23 46 4C 98 30 41 51 
D7 6F D1 4C 7A F6 0C 09 09 9E 3B 6F 7E 76 4E 8E A7 97 F7 BA B5 6B 2C 2D 2D 9B 3F 9F 58 C6 1C 68 
79 49 6E 1B CE A0 DB 22 06 07 07 6B 76 CE 80 BC ED 54 5E 22 91 88 99 17 48 97 F4 6E 50 D3 6B D6 
A4 67 4F E6 58 80 05 2E A1 59 A0 67 1A 00 94 8B AE 3A 47 B7 40 CB CB CB FB EE BB A9 7F 1E 3C C8 
2E 35 F3 BF FE EB BF BA 74 E9 32 76 CC 98 5D BB 62 D6 AC F9 8D 7E 24 3F 7C F8 70 CF DE BD 8A ED 
3C EE D8 B1 63 C0 A2 85 1D 3A 74 20 84 08 85 C2 88 88 48 24 7B 30 46 D8 DA FE F8 E3 0C 42 C8 E3 
C7 8F A7 FD E0 19 15 B5 4D A9 7B 70 34 1B C9 6D C3 8D 8D 8D B7 6F 8F 6E 6C 5B 44 8D A4 C0 76 DA 
A0 E7 CF 9F 33 C7 3D 7A F4 50 D4 65 EB EB 62 68 C8 1C 3F 7E F4 58 79 6F 04 C0 40 CF 34 00 FC DB 
DA 75 EB E4 9A 47 CF CE BB 77 EF 82 82 96 6F DF BE 23 66 E7 8E FE FD 59 CE B5 6F D3 A6 8D CB D7 
5F E7 64 E7 D0 65 D7 32 32 CE FD F3 CF 3F FD FA F5 53 60 39 87 0C 19 C2 2C EC 40 93 3D 7E 59 B9 
B2 6D DB B6 0A 7C 0B A5 3A 78 E8 D0 B2 65 41 CA 7E 17 A1 50 B8 69 F3 E6 B8 FD FB D7 AF 5B 67 6F 
3F 4A D9 6F A7 3C 75 B6 0D 5F B8 D0 7F BC 93 53 AD 48 B4 70 51 80 50 28 A4 DB 22 F6 33 35 55 87 
BD C4 5B 50 3B 65 88 C5 E2 7B F7 EE 33 0F E9 6E A3 4A 62 D8 C5 B0 53 A7 4E 34 A7 FF CE DD BB 35 
35 35 72 AD 8E 27 10 08 32 CF 9F 37 37 37 37 36 36 D6 EC B1 08 50 20 04 D3 00 F0 6F 1D 3B 74 B4 
B0 B0 50 D2 C5 DF BC 79 C3 A4 D8 6A 6B 6B 8F 1D 3B A6 73 E7 26 2D AF A6 A3 A3 63 6D 6D 45 83 E9 
67 CF 9E FD F3 E4 89 62 83 69 0E 87 E3 FE FD F7 39 39 17 98 64 8F 71 E3 C6 8D 1D 33 46 81 6F A1 
54 9F E8 EA 2A AF 36 DF BF 7F 4F 37 DC 26 84 70 B9 DC E1 C3 86 F5 EB D7 82 17 E4 AE B3 6D B8 8B 
CB D7 13 27 4C E0 70 38 4E E3 C7 7B 7A FE B0 77 EF EF E4 3F FB 62 86 AE 5A A5 F2 95 3D 5A 56 3B 
A5 DE BD 7B 77 F5 EA 55 7A 6C D2 B3 67 37 C5 2D 67 59 5F 8F 1E DD CD CD CD CF 9F 3F 4F 08 C9 CD 
CD 7D 5E 5C 2C 99 F8 F1 51 8F 1E 3D FE F9 E7 15 AF 5F BF D6 D6 D6 0E 0D 5D 35 65 F2 64 A5 95 14 
34 07 82 69 00 F8 B7 D9 B3 67 CD 9E 3D 4B 19 57 2E 2D 2D F5 5F B8 88 7E 48 5B 5A 5A 2A 2A 1D B3 
8D 44 BF D1 AB 57 AF 9A 7E C1 3A 68 B2 C7 B5 6B D7 E8 2E 1E 9B 36 6D 32 1F 30 40 E1 EF A2 24 13 
26 4C 50 52 9E 77 45 45 C5 8A 95 2B 69 30 6D 62 62 A2 AA B4 69 05 CA CE C9 61 B6 0D EF 6F 6A EA 
EF EF 4F 23 66 AE 96 D6 EC 59 B3 AE 5F BB 7E 29 3F 9F 10 72 E4 48 E2 97 5F 7E F9 DD 94 29 AA FD 
65 5B 5C 3B 25 84 14 14 5C BB 98 97 47 8F CD CD CD 0D 25 32 31 14 8E C7 E3 7D 3E 78 30 0D A6 1F 
3E 7C 78 36 FD AC 97 97 A7 8C 55 26 14 89 4E 9E 3A 49 7B B5 B9 5C AE A9 42 BF 9F 83 06 43 CE 34 
00 28 57 65 65 E5 FA 0D 1B 72 73 73 B9 5C EE DC 39 73 62 F7 FD AE A8 4F E8 5A 91 48 21 D7 91 62 
F0 E7 9F CF F0 F1 A1 C7 37 6F DE DA B5 7B B7 B0 46 A8 EC 37 55 67 42 91 68 F7 EE FF A1 9D B8 FF 
FA 97 5B E2 91 23 5F 7E F9 65 8B 8E A4 5F BC 78 B1 65 F3 16 BA 6D B8 AE AE 6E 48 48 B0 64 47 A6 
A1 A1 E1 A2 80 45 34 7B 9E 10 B2 79 F3 96 9B 37 6F A9 A6 A0 4A A6 BC 76 5A 51 51 F1 D7 91 BF 98 
D9 87 23 6C 47 28 B5 77 9F C3 E1 8C 1D 37 56 57 57 97 3E DC 17 1B 7B F7 DE 3D 19 5F 5B 78 BB F0 
D0 A1 C3 F4 78 E8 D0 A1 7D FA F4 51 4A 11 41 E3 20 98 06 00 E5 FA DF FF 3D 79 F4 68 12 97 CB 5D 
B9 72 45 C0 4F 01 8A 5A 6B 96 CF E7 A7 9F 3D CB 3C 54 52 16 26 57 4B 6B DA 34 8F 11 36 36 F4 61 
5C DC FE 23 89 47 94 F1 46 2D 45 FE A5 4B 7B F6 EE 25 84 CC 9A E5 1B B6 7A B5 BE 7E 47 55 97 A8 
49 2A 2A 2A D6 AD 5F 4F 3B 9E 09 21 3F FE 38 63 84 AD 6D 9D 73 AC AC AC BC BD BD E8 F1 8B 17 2F 
7E FB ED 37 8D 5C 63 5B 49 ED B4 B6 B6 F6 E8 D1 A4 E3 C7 93 E9 C3 FE A6 A6 A3 46 29 3D B7 7E A0 
B9 B9 C3 B8 71 F4 F8 E1 C3 87 2B 57 FE 52 5A 5A FA D1 57 95 96 96 AE 0E 0B 63 D6 EF FB 6E CA 14 
3D 3D 3D 25 96 12 34 08 82 69 00 50 A2 E2 E2 E2 3D 7B F7 10 42 C2 C3 C3 7E 98 36 4D 51 13 7A 84 
22 D1 EE FF F9 9F 94 94 54 FA B0 5F BF 7E 3D 95 B6 3E 40 A7 4E 9D FC FD 17 30 2B 7B E4 E7 5F 56 
D2 1B A9 3F 3E 9F BF 67 EF DE 77 EF DE F9 FB 2F 58 BA 74 69 4B DF 83 43 2C 16 9F F8 FB EF 63 C7 
8E D3 87 23 6C 6C BC 3C 3D EB DF A2 5C 2D 2D 2F 4F 4F E6 0B 55 76 4E 4E 6C 5C 9C 50 F9 A3 22 CD 
49 49 ED B4 A2 A2 62 DB B6 E8 5F 7E FD 95 79 E6 1B B7 6F 94 D7 54 19 3A 3A 3A DE DE 5E CC 78 42 
6E 6E AE A7 A7 D7 A5 FC FC DA DA DA 06 CF 17 8B C5 D7 AE 5D 9B 35 DB 2F 37 37 97 3E 63 67 67 67 
67 37 52 D9 E5 04 8D 81 60 1A 00 94 45 2C 16 1F 4D 4A 2A 2A BA 13 1E 1E 36 F9 DB 6F 9B 9E 0C 20 
16 8B DF BE 7D 9B 91 71 CE DB CB 3B 32 72 2B F3 BC B3 F3 78 A3 6E DD 9A 78 71 29 86 0D 1F CE 24 
7B B4 66 99 99 99 67 CE A4 FB FB 2F 58 B0 60 81 06 2C 74 70 F5 EA D5 B0 B0 70 9A 7E 60 68 68 B8 
7C F9 F2 C6 F6 BB EE D4 A9 D3 92 25 8B 99 E0 6C DF BE 58 26 EA D2 00 8A 6D A7 62 B1 B8 BC BC FC 
CE DD BB DB 77 EC 70 70 74 DA B4 79 F3 FF 25 78 D8 D8 34 5B C6 B9 64 82 16 21 E4 CE DD BB 53 A6 
7C F7 BD BB 47 72 F2 89 E2 E2 62 FA 5D 88 FE 3D 39 7F FE BC DF 9C 39 DF 4E 9E 52 50 50 40 4F EE 
D0 A1 C3 BC B9 73 3A 76 6C D9 A3 2E D0 9C 30 01 11 00 94 E5 9F 27 4F 8E 1C 49 0C 5C BA C4 CD CD 
4D F6 4F D0 EF DD 3D E4 7A 97 FE A6 A6 93 27 4F 56 6A 6C C7 D5 D2 FA FE FB A9 D9 39 39 9A 14 42 
C9 EB ED DB B7 F1 F1 7F FC F0 C3 B4 D9 B3 66 A9 3C 92 DE B1 63 27 8B E5 E1 24 F7 03 2A 2D 2D 5D 
BB 6E 3D 4D 95 E6 72 B9 8B 17 FF 34 68 D0 40 29 AF 1D 32 64 48 C0 A2 45 BF FE F7 7F 93 FF 6C 8B 
D8 AF 6F 5F A5 4E A4 6B 36 EC DA A9 BC 55 D0 BB 77 EF 5F 7E FD A5 B1 AF 2B AC 2F 4B D5 DF E9 89 
AB A5 35 73 E6 8F 65 6F CB 7E FF 7D 1F F3 64 5E 5E 5E DE 7F E6 41 36 A6 43 87 0E A1 AB 56 7D F9 
E5 97 F2 96 01 5A 33 04 D3 00 A0 2C 26 3D 7B A6 A6 28 77 AB 8B CE 9D 3B AF FC 65 A5 5C 4B 5F B1 
D3 A5 4B 97 05 0B E6 17 16 16 D2 F0 AB 15 EA D8 B1 63 7C FC 7E 55 97 42 31 84 22 91 64 EF F2 37 
DF B8 4E 9A 38 51 7A 1C C9 E1 70 A6 4C 99 9C 7F 39 9F A6 FF 6A D2 B6 88 CD D0 4E 2D 2C 2C 36 6D 
DC D0 CC F3 F9 DA B7 6F BF 3C 28 A8 AB 61 D7 0D 1B 37 32 BD E3 D2 75 EE DC F9 B7 F0 B0 B1 63 C7 
B6 E8 39 B5 D0 FC 90 E6 01 00 2D 95 93 93 E3 E1 43 87 6C 47 8C 68 9E B7 93 9C 88 06 2D 97 58 2C 
4E 4C 4C 8C D9 B5 8B 3E 1C 34 68 E0 4F 01 01 3A 3A 3A 1F 7D 61 FB F6 ED E7 CF 9F DF BB 77 6F FA 
30 2E 6E FF B1 A4 63 4A 2C A8 46 E8 D0 A1 C3 92 25 8B FF 88 DF AF 92 95 31 DA B6 6D 3B 6B 96 6F 
E2 91 23 1F 5D 21 9E CB E5 7A 79 7A FE 7D 22 79 DC B8 71 88 A4 41 5E E8 99 06 80 16 83 CB E5 F6 
ED DB B7 77 AF 5E 8E 8E 8E B6 B6 23 BA 74 E9 D2 9C 1F 7B 5C 2D 2D 0F 77 F7 EC AC 6C 66 F1 07 68 
89 EE DE BB B7 7D FB 0E DA 55 D9 A1 43 87 E5 CB 97 1B C9 BC 87 88 69 BF 7E 73 E6 F8 05 07 87 D0 
6D 11 A3 B6 6D FB 6C F0 67 EA B0 2D A2 5A E9 DC B9 73 BF 7E 7D BF FC F2 4B 3B 3B BB CF 07 0F 96 
6B 03 42 85 E3 70 38 9F 7D 36 68 F7 EE 5D A5 A5 A5 59 59 D9 A9 A9 A9 77 EF DD 63 B6 1C EA D1 A3 
C7 A0 81 03 1D 1D 1D ED EC 46 76 EE DC 59 85 E5 84 16 ED DF 9F 43 62 B1 58 B5 E5 00 25 A1 A1 06 
EA 57 53 A1 7E 35 1B EA 57 B3 A1 7E 35 1B EA 57 B3 49 D6 2F D2 3C 00 00 00 00 00 58 42 30 0D 00 
00 00 00 C0 12 82 69 00 00 00 00 00 96 10 4C 03 00 00 00 00 B0 84 60 1A 00 00 00 00 80 25 04 D3 
00 00 00 00 00 2C 21 98 06 00 00 00 00 60 09 C1 34 00 00 00 00 00 4B 08 A6 01 00 00 00 00 58 42 
30 0D 00 00 00 00 C0 12 82 69 00 00 00 00 00 96 10 4C 03 00 00 00 00 B0 84 60 1A 00 00 00 00 80 
25 04 D3 00 00 00 00 00 2C 21 98 06 00 00 00 00 60 09 C1 34 00 00 00 00 00 4B 08 A6 01 00 00 00 
00 58 42 30 0D 00 00 00 00 C0 12 82 69 00 00 00 00 00 96 10 4C 03 00 00 00 00 B0 84 60 1A 00 00 
00 00 80 25 04 D3 00 00 00 00 00 2C 21 98 06 00 00 00 00 60 09 C1 34 00 00 00 00 00 4B 08 A6 01 
00 00 00 00 58 42 30 0D 00 00 00 00 C0 12 82 69 00 00 00 00 00 96 10 4C 03 00 00 00 00 B0 84 60 
1A 00 00 00 00 80 25 04 D3 00 00 00 00 00 2C 21 98 06 00 00 00 00 60 09 C1 34 00 00 00 00 00 4B 
08 A6 01 00 00 00 00 58 42 30 0D 00 00 00 00 C0 12 82 69 00 00 00 00 00 96 10 4C 03 00 00 00 00 
B0 84 60 1A 00 00 00 00 80 25 04 D3 00 00 00 00 00 2C 21 98 06 00 00 00 00 60 09 C1 34 00 00 00 
00 00 4B 08 A6 01 00 00 00 00 58 E2 A8 BA 00 00 00 00 00 00 2D 8F 58 2C 26 E8 99 06 00 00 00 00 
60 8D 4B FF 47 23 6B D0 3C 1C 0E 87 A0 7E 35 17 EA 57 B3 A1 7E 35 1B EA 57 B3 A1 7E 35 1B AD 5F 
0A 3D D3 00 00 00 00 00 2C 21 98 06 00 00 00 00 60 09 C1 34 00 00 00 00 00 4B 08 A6 01 00 00 00 
00 58 42 30 0D 00 00 00 00 C0 12 82 69 00 00 00 00 00 96 10 4C 03 00 00 00 00 B0 84 60 1A 00 00 
00 00 80 25 04 D3 00 00 00 00 00 2C 21 98 06 00 00 00 00 60 09 C1 34 00 00 00 00 00 4B 08 A6 01 
00 00 00 00 58 42 30 0D 00 00 00 00 C0 12 82 69 00 00 00 00 00 96 10 4C 03 00 00 00 00 B0 84 60 
1A 00 00 00 00 80 25 04 D3 00 00 00 00 00 2C 21 98 06 00 00 00 00 60 09 C1 34 00 00 00 00 00 4B 
08 A6 01 00 00 00 00 58 42 30 0D 00 00 00 00 C0 12 82 69 00 00 00 00 00 96 10 4C 03 00 00 00 00 
B0 84 60 1A 00 00 00 00 80 25 04 D3 00 00 00 00 00 2C 21 98 06 00 00 00 00 60 09 C1 34 00 00 00 
00 00 4B 08 A6 01 00 00 00 00 58 42 30 0D 00 00 00 00 C0 12 82 69 00 00 00 00 00 96 10 4C 03 00 
00 00 00 B0 84 60 1A 00 00 00 00 80 25 04 D3 00 00 00 A0 7A 62 B1 78 D7 AE 5D 9C FF 58 B0 60 41 
65 65 65 83 67 DE BE 7D DB DA DA 9A 9E 36 76 EC D8 67 CF 9E 35 73 51 A1 BE F2 F2 72 6F 6F 6F 5A 
29 7A 7A 7A 07 0E 1C 68 F0 34 B1 58 FC C7 1F 7F E8 E9 E9 D1 33 43 42 42 84 42 61 33 17 55 E1 10 
4C 03 00 00 80 EA 71 38 1C 0F 0F 0F 5F 5F 5F FA 70 DF BE 7D 29 29 29 F5 4F 13 08 04 51 51 51 B9 
B9 B9 84 10 23 23 A3 9F 7F FE D9 D8 D8 B8 59 0B 0A 0D D1 D3 D3 0B 0A 0A B2 B0 B0 20 84 F0 F9 FC 
A8 A8 A8 47 8F 1E D5 3F AD B0 B0 30 32 32 92 CF E7 13 42 26 4E 9C B8 60 C1 02 2E 97 DB CC 45 55 
38 04 D3 00 00 00 A0 16 74 75 75 03 02 02 AC AC AC 08 21 7C 3E 7F FD FA F5 75 02 32 B1 58 9C 98 
98 18 1D 1D 4D 1F 2E 5C B8 70 D4 A8 51 CD 5F 4E 68 D0 80 01 03 02 03 03 79 3C 1E 21 24 2B 2B 2B 
2A 2A AA BA BA 5A F2 04 81 40 B0 79 F3 66 FA 45 C8 C4 C4 64 E9 D2 A5 5D BB 76 55 4D 59 15 0A C1 
34 00 00 00 A8 8B 01 03 06 F8 FB FB 37 16 90 5D BF 7E 3D 3C 3C 9C 1E BB BA BA 4E 9F 3E 5D 03 FA 
35 35 06 87 C3 71 75 75 F5 F4 F4 A4 0F 63 62 62 4E 9E 3C C9 FC 94 26 78 EC DA B5 8B 3E 9C 33 67 
8E AD AD AD 0A 4A A9 04 08 A6 41 95 84 42 61 5E 5E 5E 68 68 E8 C4 89 13 7B F5 EA 45 33 A8 7A F5 
EA 35 71 E2 C4 D0 D0 D0 BC BC BC 8F A6 52 BD 7E FD DA D9 D9 99 BE 30 3E 3E BE FE 09 59 59 59 4C 
06 9E B7 B7 77 79 79 B9 8C 65 8B 8F 8F A7 AF 1A 32 64 48 51 51 91 DC BF 5B 6B 22 16 8B 9F 3C 79 
B2 73 E7 4E 77 77 F7 2F BE F8 82 FE BB 75 EA D4 C9 D9 D9 39 34 34 F4 FA F5 EB EC 52 E2 84 42 E1 
AD 5B B7 B6 6C D9 E2 EA EA CA EE F6 68 EC B2 4D BC EB 34 1E 73 F3 B3 E6 E7 E7 D7 58 B6 EB C5 8B 
17 BB 75 EB 46 4F EB D6 AD DB C5 8B 17 65 2C 15 DA 72 2B C1 E1 70 DC DC DC BC BD BD E9 C3 98 98 
98 8C 8C 0C 7A 5C 56 56 B6 7A F5 EA DB B7 6F 93 FF F4 6B 1A 1A 1A AA AC A0 D0 10 5D 5D DD 45 8B 
16 31 63 0B 11 11 11 4C 46 7B 7E 7E 7E 58 58 18 3D 76 73 73 9B 31 63 86 A6 7D 11 12 83 86 52 DB 
FA 15 89 44 A9 A9 A9 96 96 96 D2 EF 4C 4B 4B CB D4 D4 54 91 48 D4 D8 75 5E BD 7A 35 7E FC 78 7A 
F2 FE FD FB EB 9F 70 FE FC 79 C9 0B C6 C4 C4 D4 D6 D6 CA 52 C2 FD FB F7 D3 97 58 58 58 14 16 16 
B2 FF 55 95 49 E5 F5 2B 12 89 CE 9C 39 33 69 D2 24 E9 F5 68 67 67 27 BD 1E EB A8 AA AA 3A 7C F8 
F0 47 6F 8F C1 83 07 FF F1 C7 1F 55 55 55 B2 97 56 21 77 5D B3 51 55 FD 32 37 3F 6B B3 67 CF AE 
A8 A8 A8 7F 65 A1 50 B8 62 C5 0A C9 33 43 43 43 65 6C 92 9A D7 96 55 55 BF 2D C2 9D 3B 77 68 40 
46 08 19 33 66 CC D3 A7 4F 85 42 E1 BA 75 EB 98 1B 60 CB 96 2D 32 DE 00 AA D2 9A EB 37 21 21 81 
8E 2D 10 42 82 83 83 6B 6A 6A 4A 4B 4B DD DC DC E8 33 26 26 26 79 79 79 AA 2E 63 53 49 D6 2F 69 
CD 95 DD 1A A8 67 FD BE 7F FF 3E 38 38 58 F6 0F E6 E0 E0 E0 F7 EF DF 37 78 29 79 83 69 0B 0B 8B 
5B B7 6E C9 52 48 B5 FD 00 96 A4 DA FA 2D 2E 2E 9E 31 63 86 8C 95 C8 E3 F1 42 43 43 1B 0C B0 EA 
B8 7F FF 3E F3 37 57 16 93 26 4D BA 72 E5 CA 47 2F AB C0 BB AE D9 A8 AA 7E 95 17 4C 3F 7F FE DC 
C1 C1 41 F2 4C 07 07 87 E7 CF 9F CB 52 2A CD 6B CB AA AA 5F 76 DE BF 7F 4F A7 06 AE 5A B5 4A C6 
97 D4 D4 D4 9C 3F 7F DE DF DF 7F E8 D0 A1 F4 97 35 33 33 9B 3E 7D FA A9 53 A7 64 F9 53 70 F4 E8 
51 26 20 0B 0D 0D 4D 4D 4D 35 31 31 A1 0F BD BC BC DE BD 7B D7 B4 5F 48 E9 5A 56 FD 2A 56 55 55 
D5 E2 C5 8B E9 BF 80 91 91 D1 A9 53 A7 D6 AC 59 C3 34 5E D9 BF 09 AB 33 C9 FA 25 AD B9 B2 5B 03 
35 AC DF 9A 9A 1A C9 46 25 A3 F9 F3 E7 37 F8 C7 57 DE 60 9A 10 E2 EB EB 2B 4B 90 A4 B6 1F C0 92 
54 58 BF 85 85 85 2C D2 DD 7E FD F5 57 E9 1F A2 D9 D9 D9 74 32 B8 5C 4C 4C 4C D2 D2 D2 A4 FC 75 
56 EC 5D D7 6C 68 31 9A FF 7D 95 17 4C FF F5 D7 5F F4 04 77 77 77 67 67 67 7A FC D7 5F 7F C9 52 
2A CD 6B CB AA AA 5F 16 6A 6B 6B E3 E3 E3 69 68 2B 63 30 7D E5 CA 15 29 63 56 66 66 66 87 0E 1D 
92 3E FE 53 53 53 C3 7C 01 36 30 30 E8 D1 A3 07 53 8F 32 7E 8F 52 AD 16 54 BF CA F0 F4 E9 D3 31 
63 C6 D0 7F 84 1E 3D 7A 18 18 18 C8 D5 6C D5 9F 64 FD 92 56 5E D9 1A 4F 0D EB 37 37 37 D7 C8 C8 
88 F9 93 3A 7E FC F8 A4 A4 A4 92 92 92 9A 9A 1A 7A 42 4D 4D 4D 49 49 49 52 52 12 13 25 13 42 78 
3C DE D1 A3 47 EB 5F 8D 45 30 4D 08 89 8B 8B FB E8 D7 62 B5 FD 00 96 A4 AA FA 2D 29 29 71 75 75 
95 FC 27 1D 3C 78 F0 DA B5 6B AF 5F BF CE E7 F3 E9 39 35 35 35 4F 9E 3C 89 8D 8D 95 4C AB E0 F1 
78 F1 F1 F1 8D FD E3 DF BA 75 8B 19 D8 65 3E 71 D7 AC 59 73 FD FA 75 26 32 AB AE AE 7E F0 E0 C1 
96 2D 5B 06 0F 1E 2C 79 A6 89 89 C9 D9 B3 67 1B 2B B0 62 EF BA 66 A3 86 ED B7 B0 B0 90 F9 B6 D3 
60 8B 93 A2 AA AA CA DF DF 9F BE 76 C7 8E 1D 1B 37 6E A4 C7 D3 A7 4F 97 E5 C3 55 F3 DA B2 1A D6 
6F 63 CE 9E 3D CB F4 0A CB 12 4C D7 6F CB F5 49 FF 6B 40 15 17 17 4F 9C 38 51 DE 57 A9 89 16 54 
BF 4A 92 96 96 26 F9 87 97 10 62 65 65 D5 22 BE 08 C9 42 B2 7E 09 2A 5B B3 A9 5B FD 0A 85 C2 E5 
CB 97 33 7F 13 23 23 23 A5 24 BC 56 55 55 ED DE BD 9B 19 E6 73 73 73 7B F3 E6 4D 9D 73 D8 05 D3 
B2 74 6C A8 ED 07 B0 24 95 D4 6F 45 45 C5 FC F9 F3 25 3F DB D6 AF 5F 2F 25 18 7A FF FE FD AA 55 
AB 98 7A 6C EC DF 53 32 A3 8E 10 62 60 60 B0 69 D3 26 29 97 AD AA AA DA B3 67 0F D3 DB 41 FE 93 
58 59 FF 4C 85 DF 75 CD 46 DD DA AF B8 69 C1 F4 8D 1B 37 CC CD CD 09 21 46 46 46 97 2E 5D 62 BE 
E1 18 19 19 E5 E6 E6 7E F4 E5 9A D7 96 D5 B0 7E 1B 94 91 91 61 66 66 C6 FC 9B 7F 34 98 AE D3 96 
A5 30 37 37 2F 28 28 90 7E 35 C9 38 9E 10 32 77 EE DC 96 D2 AF D9 52 EA 57 79 EA 0C 09 B6 A0 2F 
42 B2 90 AC 5F AC E6 01 CD AA BC BC FC DA B5 6B F4 D8 C3 C3 63 E6 CC 99 DA DA DA 8D 9D AC AD AD 
ED ED ED 1D 18 18 48 1F 9E 3E 7D FA D6 AD 5B 4D 79 F7 1F 7E F8 81 06 49 05 05 05 51 51 51 02 81 
A0 29 57 6B B5 32 33 33 F7 ED DB 47 8F 0D 0C 0C 62 62 62 16 2F 5E AC AB AB DB D8 F9 BA BA BA CB 
97 2F 0F 09 09 A1 0F 0B 0A 0A E2 E3 E3 45 22 91 E4 39 62 B1 F8 8F 3F FE 48 4C 4C A4 0F 2D 2C 2C 
8E 1D 3B B6 68 D1 22 29 97 D5 D6 D6 F6 F1 F1 49 4E 4E 66 62 BB F4 F4 F4 D8 D8 D8 3A 57 26 AA BE 
EB 80 71 FE FC 79 BA 0E 83 85 85 85 89 89 89 A9 A9 A9 B5 B5 35 21 A4 B8 B8 38 25 25 85 F9 70 92 
05 DA 72 F3 A8 AD AD 3D 74 E8 90 97 97 97 5C AB A0 1C 3B 76 8C 69 CB 06 06 06 A1 A1 A1 FF FC F3 
8F 48 24 AA AD AD 7D F5 EA D5 9E 3D 7B 98 D0 FC F6 ED DB 87 0F 1F AE DF 66 25 75 ED DA B5 63 C7 
8E CC C3 9E 3D 7B 4A 69 BF A0 56 B8 5C 6E F7 EE DD 99 87 06 06 06 C6 C6 C6 1C 0E 47 85 45 52 12 
04 D3 D0 AC 5E BF 7E 5D 52 52 42 8F ED EC EC 74 74 74 A4 9F CF E5 72 DD DC DC 68 6F 16 9F CF BF 
71 E3 46 53 DE FD 87 1F 7E 60 D6 BF 8C 8B 8B 4B 4A 4A 92 EB F3 1B 08 21 02 81 20 21 21 81 6E 5E 
45 08 09 0A 0A 9A 32 65 CA 47 FF 38 72 B9 5C 1F F5 2D 18 19 00 00 20 00 49 44 41 54 1F 1F 17 17 
17 FA 30 2D 2D ED E9 D3 A7 92 27 3C 7E FC F8 D0 A1 43 F4 D8 C8 C8 68 D3 A6 4D B6 B6 B6 B2 FC CD 
B5 B1 B1 D9 B4 69 13 33 92 18 17 17 57 58 58 58 E7 1C D5 DE 75 40 95 95 95 9D 3A 75 8A 1E 5B 5A 
5A EA EB EB EB EB EB DB D9 D9 D1 67 32 32 32 98 3A 92 05 DA 72 33 E0 F3 F9 2B 56 AC F8 F1 C7 1F 
1F 3F 7E 2C FB AB DE BD 7B C7 2C 2D 6C 62 62 72 E8 D0 A1 90 90 90 1E 3D 7A B4 69 D3 86 AE 98 E9 
E3 E3 73 F8 F0 61 26 09 A4 FE 5F 03 49 02 81 20 32 32 B2 A0 A0 80 79 26 22 22 E2 DC B9 73 AC 7E 
21 68 6E B7 6F DF DE BA 75 2B F3 F0 F1 E3 C7 EB D7 AF 97 AB A5 B7 14 08 A6 A1 59 75 E8 D0 41 5F 
5F 9F 1E 4B EF 8D 60 74 EF DE 7D D0 A0 41 F4 B8 B4 B4 B4 29 EF FE C9 27 9F CC 9F 3F 9F D9 EC 34 
32 32 B2 7E E0 05 D2 15 16 16 32 21 91 8B 8B 8B B7 B7 B7 96 96 96 2C 2F EC D2 A5 0B 5D 38 96 C7 
E3 E9 E8 E8 D4 F9 7B 9A 95 95 95 95 95 45 8F 7D 7C 7C E4 DA D2 6C D4 A8 51 3E 3E 3E F4 F8 F6 ED 
DB F5 F7 1F 56 ED 5D 07 D4 DD BB 77 2F 5C B8 40 08 E1 F1 78 F6 F6 F6 F4 B6 19 37 6E 9C A9 A9 29 
21 E4 F4 E9 D3 39 39 39 B2 5F 0D 6D 59 A9 84 42 61 6A 6A EA B8 71 E3 C2 C3 C3 E9 37 67 7B 7B 7B 
66 32 99 74 F7 EE DD 63 DA 72 48 48 C8 98 31 63 EA 7F 2B FE EC B3 CF 98 D4 AF EC EC 6C C9 58 59 
92 58 2C 4E 4A 4A 8A 8B 8B 93 7C B2 B8 B8 78 D3 A6 4D 1A 19 90 69 18 C9 5D DF 19 27 4E 9C D8 BD 
7B B7 E6 AD E5 AF C9 C1 B4 58 2C 2E 29 29 39 70 E0 C0 BC 79 F3 C6 8E 1D DB A9 53 27 BA 6E BF 9E 
9E DE A8 51 A3 E6 CD 9B 77 E0 C0 81 92 92 12 F4 67 34 A7 76 ED DA 31 9D 88 69 69 69 B2 6C BB D0 
A1 43 87 43 87 0E D1 B4 A4 3A 2B D4 B2 30 60 C0 80 25 4B 96 D0 E3 DC DC 5C 0C 10 CB EB D2 A5 4B 
C5 C5 C5 F4 78 F4 E8 D1 5D BA 74 91 FD B5 8E 8E 8E 77 EE DC 79 F5 EA D5 E9 D3 A7 25 27 27 55 56 
56 66 66 66 D2 63 23 23 23 57 57 57 B9 56 F2 E7 72 B9 53 A7 4E A5 1D C9 84 90 EC EC EC 77 EF DE 
49 9E A0 F2 BB 0E 44 22 51 72 72 32 BD 73 1C 1C 1C BE F8 E2 0B FA 7C DF BE 7D 99 35 61 8E 1F 3F 
2E 57 63 44 5B 56 92 AA AA AA 25 4B 96 38 39 39 E5 E5 E5 D1 67 E6 CE 9D BB 7F FF FE FE FD FB CB 
F2 F2 C2 C2 42 5A D1 E6 E6 E6 23 46 8C 68 6C 7C C9 D2 D2 92 59 24 F1 C2 85 0B 0D 7E CB 2D 2C 2C 
5C B7 6E 1D 8D E6 DD DC DC 0E 1D 3A 44 93 A7 4F 9C 38 B1 75 EB 56 CD 0B C8 34 89 F8 FF DF F5 3D 
3C 3C 9C D9 B7 72 DD BA 75 67 CE 9C 51 5D D1 94 42 33 83 E9 DA DA DA F4 F4 74 17 17 17 23 23 23 
77 77 F7 E8 E8 E8 F4 F4 F4 37 6F DE D0 9F F2 F9 FC CC CC CC E8 E8 68 77 77 77 23 23 A3 69 D3 A6 
D1 09 10 AA 2D 73 2B C1 E3 F1 98 F9 82 B1 B1 B1 0B 16 2C 78 F0 E0 41 73 FE E3 D3 BD B5 E8 6A A9 
84 90 B8 B8 B8 E3 C7 8F 37 DB BB B7 74 55 55 55 4C F2 B1 91 91 91 5C FD C7 84 10 1E 8F 67 6A 6A 
DA B6 6D DB 3A CF 97 95 95 31 19 99 B6 B6 B6 92 53 9D 64 D4 BB 77 EF E1 C3 87 D3 E3 A2 A2 22 26 
DC 67 DE 57 B5 77 1D BC 78 F1 82 F9 BE 34 72 E4 48 26 05 56 57 57 97 89 A8 4E 9D 3A 75 F3 E6 4D 
D9 AF 89 B6 AC 24 62 B1 B8 AA AA 8A 1E D3 05 EC B6 6E DD DA A9 53 27 59 5E 2B 12 89 98 4A 1C 3E 
7C 78 CF 9E 3D 1B 3B B3 63 C7 8E CC 77 AA 6B D7 AE D5 FF 8A 5B 5E 5E BE 66 CD 1A DA 69 6D 62 62 
12 1C 1C FC CD 37 DF CC 99 33 87 FE 74 EB D6 AD 27 4E 9C 90 E7 D7 02 B9 09 85 C2 AC AC AC 85 0B 
17 DA D8 D8 D0 BE C8 01 03 06 B8 BB BB 1F 38 70 E0 A3 5D 12 92 BB BE 4F 99 32 C5 CF CF 6F C6 8C 
19 74 0D 28 3E 9F BF 6A D5 AA 47 8F 1E 29 BB FC CD 49 03 83 E9 27 4F 9E F8 F8 F8 8C 1D 3B 36 39 
39 59 96 F3 13 12 12 EC EC EC 7E FE F9 67 26 0D 14 94 6A C2 84 09 53 A6 4C A1 C7 B1 B1 B1 7D FB 
F6 75 71 71 D9 B9 73 E7 A3 47 8F 9A A7 A7 41 57 57 37 20 20 80 19 20 DE B2 65 CB DD BB 77 9B E1 
7D 35 80 40 20 B8 7F FF 3E 3D 36 33 33 AB B3 E6 11 6B C5 C5 C5 4C 30 6D 6A 6A FA C9 27 9F C8 7B 
05 1E 8F C7 EC 0A 71 FD FA F5 27 4F 9E D4 39 41 E5 77 5D 2B 77 E1 C2 85 B3 67 CF 12 42 4C 4D 4D 
1D 1C 1C 24 7B 2B 47 8C 18 41 87 29 8A 8B 8B 93 93 93 65 CC C3 A1 D0 96 95 87 2E A7 73 F1 E2 C5 
C9 93 27 B7 69 23 6B A8 50 5D 5D FD F2 E5 4B 7A DC A7 4F 1F 29 6D 99 C3 E1 D0 0C 1F 42 48 49 49 
C9 EB D7 AF 25 7F 2A 16 8B F7 EE DD 1B 1B 1B 4B 1F 86 84 84 0C 1B 36 8C CB E5 4E 9F 3E 9D 09 C8 
7E FB ED 37 54 B7 92 88 C5 E2 EC EC EC 11 23 46 8C 1C 39 32 32 32 92 26 68 11 42 8A 8A 8A 0E 1C 
38 E0 EE EE FE E5 97 5F FE F1 C7 1F D5 D5 D5 0D BE 5C 72 D7 77 73 73 F3 9F 7F FE 59 5F 5F DF D0 
D0 30 20 20 80 8E 2D 64 65 65 6D DC B8 B1 B2 B2 B2 D9 7E 23 65 D3 B4 60 FA C6 8D 1B 53 A6 4C 61 
5A A0 8C F8 7C 7E 78 78 F8 8F 3F FE F8 E2 C5 0B 25 15 0C 18 FA FA FA EB D7 AF 97 5C 38 29 39 39 
D9 CF CF AF 77 EF DE 06 06 06 0E 0E 0E A1 A1 A1 59 59 59 75 46 EA 15 6B C0 80 01 F3 E6 CD A3 C7 
B9 B9 B9 91 91 91 9A D4 AA 95 E7 FD FB F7 CC 77 CE 7E FD FA 49 4E B1 6F 0A 81 40 C0 F4 25 9B 98 
98 C8 98 84 5D 47 DF BE 7D 99 E3 FA 59 CE EA 70 D7 B5 5A 95 95 95 4C 22 BB AD AD AD 64 4D 11 42 
8C 8D 8D 47 8C 18 41 8F 73 72 72 E4 CD 50 47 5B 56 38 2D 2D AD 6F BF FD F6 CE 9D 3B 01 01 01 7A 
7A 7A 72 BD B6 B2 B2 92 F9 2A 6B 64 64 24 7D 0E 31 B3 CE C3 F3 E7 CF EB 34 BD EC EC EC CD 9B 37 
D3 63 2F 2F AF A9 53 A7 D2 4B 19 1A 1A FA FB FB D3 AF F1 A8 6E 25 11 8B C5 7F FE F9 E7 D7 5F 7F 
CD E4 F9 D4 57 54 54 34 6D DA B4 55 AB 56 D5 CF AD 12 89 44 BB 77 EF 66 26 94 07 04 04 30 7B 02 
D8 DA DA CE 9C 39 93 1E EF DB B7 2F 29 29 49 09 C5 57 0D 8D 0A A6 6F DF BE 3D 73 E6 CC 3A D9 EE 
B2 3B 74 E8 50 83 77 06 28 9C 89 89 49 5C 5C DC A6 4D 9B 24 17 09 26 84 F0 F9 FC B4 B4 B4 95 2B 
57 D2 81 60 6B 6B EB 88 88 88 67 CF 9E 29 BC 00 1C 0E 67 EA D4 A9 5E 5E 5E F4 A1 86 B5 6A E5 A9 
AA AA 62 1A 88 96 96 96 A2 56 38 92 EC 48 66 D1 2D 4D 49 0E 43 FF F3 CF 3F F5 4F 50 F9 5D D7 6A 
3D 78 F0 80 59 7E 61 E4 C8 91 75 96 3B 6C DB B6 ED 57 5F 7D 45 8F E5 9D 86 48 D0 96 95 A0 6D DB 
B6 8E 8E 8E 32 E6 75 D4 21 F9 7D FB A3 6D B9 53 A7 4E 34 CC 2A 2E 2E 66 12 4B 08 21 2F 5E BC 58 
BF 7E 3D 5D 42 C4 C2 C2 22 28 28 48 32 A6 1F 35 6A D4 DC B9 73 E9 F1 BE 7D FB 12 13 13 91 B2 A5 
58 A9 A9 A9 B3 66 CD A2 99 B1 96 96 96 F1 F1 F1 A5 A5 A5 74 AF CA 8A 8A 8A CC CC 4C 77 77 77 7A 
66 78 78 78 54 54 54 9D C1 BD F3 E7 CF 6F DB B6 8D 1E FB FA FA 7A 78 78 30 9F 14 5C 2E 77 E6 CC 
99 74 17 1E 3A 94 44 7B AF 35 80 E6 04 D3 0D CE 1B 25 84 D8 D9 D9 C5 C6 C6 3E 79 F2 A4 BA BA 9A 
4E 27 AA A8 A8 B8 7E FD FA 9A 35 6B EA A7 66 46 47 47 47 47 47 CB 35 CE 08 EC D0 F1 D9 87 0F 1F 
26 24 24 7C F3 CD 37 CC 1E 19 92 72 73 73 17 2D 5A 64 6E 6E 1E 14 14 C4 0C 1D 2A 8A 9E 9E DE E2 
C5 8B 99 E5 CF A2 A2 A2 34 2C 85 AB 35 6B 2C 73 43 E5 77 5D EB C4 2C 2F 6D 65 65 35 76 EC D8 FA 
27 7C F6 D9 67 4C E6 B4 BC D3 10 09 DA B2 3A 91 FC BE DD 60 FB 92 C4 E1 70 EA 27 90 08 85 C2 DF 
7F FF 9D 7E 23 E2 F1 78 81 81 81 03 06 0C 90 3C A1 4E 40 86 85 5C 14 EB D9 B3 67 6B D6 AC A1 DF 
88 7C 7D 7D 4F 9E 3C E9 E1 E1 D1 B9 73 67 5A 53 3A 3A 3A 23 47 8E 8C 8D 8D 65 76 B6 DA BE 7D FB 
D5 AB 57 99 97 BF 78 F1 62 F3 E6 CD F4 8B 90 95 95 55 40 40 40 9D 2F CF 5D BB 76 FD E9 A7 9F 98 
B1 05 8D 99 37 AC 39 C1 F4 E9 D3 A7 EB 2C A0 63 60 60 B0 67 CF 9E D4 D4 54 4F 4F CF EE DD BB 33 
D3 9E 74 74 74 3E FB EC B3 65 CB 96 E5 E5 E5 05 05 05 D5 B9 CE DE BD 7B E5 9A 04 03 4D A1 A7 A7 
F7 FD F7 DF 27 26 26 BE 7A F5 EA CA 95 2B 3B 76 EC 98 32 65 4A FD 8E C3 B5 6B D7 BA B9 B9 29 BC 
5E 06 0F 1E 1C 10 10 40 8F B3 B2 B2 A2 A2 A2 1A CB 00 83 96 45 FA 62 20 AA BD EB 5A 1B C9 E5 A5 
AD AC AC BA 75 EB 56 FF 9C AE 5D BB DA DB DB D3 63 79 A7 21 52 68 CB 6A 48 AE BE 6D E6 FB CF B9 
73 E7 22 22 22 E8 B1 A7 A7 A7 AB AB 6B FD 11 B0 AE 5D BB FA FB FB D3 60 2E 37 37 77 F3 E6 CD 9A 
11 90 A9 83 93 27 4F A6 A7 A7 13 42 26 4E 9C B8 6A D5 AA 3A 7F 18 29 2E 97 EB ED ED BD 60 C1 02 
42 C8 E3 C7 8F E3 E2 E2 68 73 13 0A 85 BB 76 ED 62 BE 08 F9 FB FB D7 F9 22 44 49 2E 66 1A 1D 1D 
AD 19 63 0B 1A 12 4C 0B 04 82 A3 47 8F 4A CE 20 A4 6B C5 4F 9F 3E 5D CA 56 49 3C 1E 2F 34 34 54 
72 AF 4B 22 DB 86 4C A0 70 6D DB B6 1D 32 64 C8 EC D9 B3 0F 1E 3C F8 F2 E5 CB 67 CF 9E C5 C7 C7 
4B F6 1D 66 65 65 CD 9E 3D 5B B1 1D 4E 1C 0E 67 F2 E4 C9 CC BC B4 98 98 18 66 AF 01 68 90 81 81 
41 E7 CE 9D E9 71 45 45 85 A2 A6 EE 7D B4 07 4B 16 92 13 98 A4 AC 21 20 49 25 77 5D 6B 73 EB D6 
AD D3 A7 4F D3 E3 C8 C8 C8 76 ED DA 71 EA 69 D3 A6 0D B3 FE 20 8B 69 88 04 6D 59 53 3C 7B F6 6C 
F5 EA D5 74 06 85 95 95 D5 FC F9 F3 1B DB 03 75 EC D8 B1 34 98 23 84 EC DA B5 4B 33 02 32 95 93 
DC 70 C7 DD DD BD 6B D7 AE 8D 9D C9 E5 72 5D 5D 5D 69 07 F3 A5 4B 97 E8 B2 DF 67 CE 9C 59 B7 6E 
1D 3D A1 B1 2F 42 F4 B5 73 E7 CE 65 96 2D DF B0 61 83 06 8C 2D 68 48 30 7D FF FE 7D 66 95 78 2A 
20 20 A0 C1 B5 E2 EB E0 72 B9 F3 E7 CF 67 16 57 A2 58 4C 82 01 05 6A D3 A6 4D B7 6E DD 3C 3C 3C 
12 13 13 6F DC B8 31 6B D6 2C FA 7C 56 56 D6 9E 3D 7B 14 FB 3D 47 5F 5F 3F 30 30 90 CE 2F E6 F3 
F9 EB D7 AF 47 E4 24 85 E4 82 CD 4F 9E 3C 51 D4 02 38 5D BA 74 61 E2 D7 BB 77 EF B2 FB 50 64 96 
19 A1 17 94 F7 E5 CD 79 D7 B5 1E 22 91 E8 D4 A9 53 F2 DE 27 99 99 99 2C E6 82 A3 2D B7 68 74 34 
C9 D8 D8 F8 CC 99 33 34 21 F3 C2 85 0B CC E2 F1 0D 9E 1F 16 16 26 FE 8F 1F 7E F8 41 23 37 A9 6E 
66 CC C2 4A A6 A6 A6 CC AC C1 C6 74 EF DE 9D E6 CA 66 67 67 D3 3D 2C 9D 9C 9C CA CB CB 69 8D 6C 
DB B6 AD B1 2F 42 E4 FF AF E8 AB 57 AF 4A A9 E8 96 42 43 82 E9 EB D7 AF 4B 2E 91 33 66 CC 98 C9 
93 27 CB D8 B4 74 75 75 67 CE 9C 29 B9 C8 D7 CD 9B 37 9F 3F 7F AE F8 52 82 FC 7A F6 EC B9 69 D3 
26 66 BA 89 F4 8D 67 D9 19 36 6C 18 06 88 65 D4 BE 7D 7B 66 02 7E FD E5 9C 65 71 F9 F2 E5 FA 8B 
66 18 19 19 31 7F B8 6F DE BC 29 CB A6 2A 75 54 56 56 4A 2E AE 67 68 68 28 EF 15 24 35 C3 5D D7 
4A 48 2E 2F 2D BB B3 67 CF 32 4B 71 C9 05 6D 59 AD 54 54 54 C8 7E 32 F3 87 05 54 E8 F5 EB D7 D7 
AF 5F 27 84 DC BD 7B D7 C2 C2 A2 FE 20 92 24 63 63 63 BA DE 25 91 C8 D2 69 B5 34 21 98 16 8B C5 
75 16 9B B4 B6 B6 96 32 3C 51 5F EF DE BD 99 AD 83 09 21 C5 C5 C5 CC 0E 2F A0 40 45 45 45 43 86 
0C A1 ED F0 CF 3F FF 94 F1 55 BA BA BA 1E 1E 1E B4 E7 F2 FA F5 EB 2C 02 38 E9 38 1C 8E 97 97 97 
E4 00 71 46 46 86 62 DF 42 63 68 69 69 59 5B 5B D3 E3 E2 E2 E2 8C 8C 0C B9 7A 91 45 22 D1 E1 C3 
87 E9 A2 19 6E 6E 6E CC F4 BE 2E 5D BA 30 C1 74 56 56 16 13 16 CB 4E 72 BD 08 0B 0B 0B DA 3D 49 
A9 E7 5D D7 4A 30 CB 4B CB 8B C5 34 44 82 B6 AC 06 78 3C 9E BE BE 3E 3D FE E8 00 AF 58 2C AE AD 
AD 55 7E A1 40 56 88 89 59 D3 84 60 BA AA AA 8A E6 EB 30 06 0D 1A 24 D7 52 B5 9F 7C F2 49 9D A5 
4F 91 E6 A1 0C 92 19 B7 05 05 05 B2 0F 9D 7F FA E9 A7 7D FA F4 21 84 F0 F9 7C 65 0C B8 D7 19 20 
5E B3 66 0D 56 46 6B 8C 99 99 19 DD 23 83 10 92 9C 9C 2C D7 18 CE BD 7B F7 FE FE FB 6F 7A DC BB 
77 EF 0E 1D 3A D0 63 1D 1D 1D 27 27 27 7A 5C 5C 5C 7C F0 E0 41 B9 3A 14 85 42 61 62 62 22 B3 C4 
92 8D 8D 8D E4 42 5A 6A 7B D7 69 3C C9 E5 A5 1D 1C 1C 9E 3F 7F 2E 96 AA AA AA CA DF DF 9F 9E CF 
6E 1A 22 41 5B 56 35 6D 6D 6D 66 9E D2 47 5B 0D D3 0F 6A 6A 6A AA 90 89 13 00 AA A2 09 C1 B4 8E 
8E 4E 64 64 E4 83 07 0F 8E 1C 39 12 12 12 32 6E DC B8 26 0E F2 92 8F AD 06 00 EC 48 7E 69 39 73 
E6 4C 83 8B 01 37 E8 DD BB 77 CA FE 7A 33 74 E8 50 66 EB 87 F4 F4 F4 E8 E8 68 6C 8C D7 A0 5E BD 
7A 31 0B 2F A4 A7 A7 EF DF BF 5F C6 7F 28 A1 50 18 1B 1B 4B 37 07 26 84 8C 1E 3D 5A 72 5F 71 1B 
1B 1B 66 71 B4 98 98 98 BF FE FA 4B F6 3E EF AC AC AC DD BB 77 D3 63 73 73 F3 F1 E3 C7 4B A6 78 
A9 F3 5D A7 D9 24 87 0B 6C 6C 6C 3E 9A C8 AE AD AD 3D 69 D2 24 7A CC 6E 1A 22 85 B6 AC 42 ED DB 
B7 EF D5 AB 17 3D 7E F0 E0 81 F4 56 CC 4C 1A D6 D3 D3 6B DF BE BD B2 CB 06 B2 1B 36 6C 18 9D BE 
22 A3 69 D3 A6 A9 BA C8 2A A6 09 C1 34 21 A4 6D DB B6 BD 7B F7 76 73 73 5B BD 7A F5 E9 D3 A7 99 
4F 65 19 BD 7F FF 5E 72 F6 12 41 FE 96 72 E8 E8 E8 D8 D9 D9 D1 E3 DC DC DC 0D 1B 36 C8 32 92 5B 
5D 5D 7D F0 E0 41 3A CE 6E 61 61 F1 E9 A7 9F 2A A3 6C 5A 5A 5A D3 A7 4F 67 76 C8 DB BA 75 EB C1 
83 07 95 F1 46 2D 9D B6 B6 F6 B7 DF 7E CB CC 31 08 0B 0B 3B 78 F0 E0 47 03 5F B1 58 7C F0 E0 C1 
AD 5B B7 D2 87 6E 6E 6E CC 9D 40 75 ED DA F5 BB EF BE A3 C7 7C 3E 3F 38 38 F8 E4 C9 93 B2 C4 D3 
39 39 39 0B 17 2E A4 CB 9A D2 2B D7 59 3F 5E 9D EF 3A CD 96 92 92 42 87 0B 78 3C DE F8 F1 E3 65 
19 2D 94 5C 70 9A DD 34 44 82 B6 AC 52 ED DA B5 63 72 2C 1F 3C 78 F0 FE FD 7B 29 27 33 83 0F 5D 
BB 76 65 B7 47 0C 28 16 F3 8D B7 BC BC 5C AE 94 77 D0 90 60 BA 89 1E 3E 7C 28 39 A4 38 6C D8 B0 
A6 F7 6D 43 83 46 8F 1E CD 2C 88 13 1D 1D ED EB EB 2B 3D 49 4B 20 10 AC 5B B7 2E 26 26 86 3E B4 
B7 B7 67 BA 3D 14 AE 73 E7 CE 8B 17 2F 66 06 88 99 84 04 A8 C3 CA CA CA C3 C3 83 1E F3 F9 7C 3F 
3F BF D5 AB 57 4B 99 35 28 10 08 36 6E DC E8 E7 E7 47 57 75 E0 F1 78 DE DE DE 4C 62 25 55 67 69 
B3 C7 8F 1F 4F 9D 3A 75 E3 C6 8D 52 02 DF EA EA EA BD 7B F7 4E 9A 34 89 E9 ED B6 B5 B5 F5 F5 F5 
AD 3F AC A4 CE 77 9D A6 2A 2B 2B 63 A6 1E 3A 38 38 0C 1C 38 50 96 57 49 2E 38 CD 7A 1A 22 41 5B 
56 1D 0E 87 C3 AC CC 70 ED DA 35 29 69 60 7C 3E 9F 49 CD EA DF BF BF 94 95 1F A0 D9 18 1A 1A 9A 
9A 9A 12 42 EE DE BD 4B 33 70 40 46 08 A6 89 48 24 4A 4E 4E 96 9C 60 34 78 F0 60 C9 C5 3D 40 81 
8C 8D 8D 67 CD 9A C5 A4 C7 25 24 24 7C FE F9 E7 DE DE DE 29 29 29 2F 5E BC 60 46 63 2B 2B 2B 1F 
3E 7C 18 11 11 61 63 63 B3 72 E5 4A 1A 84 99 98 98 7C F7 DD 77 52 16 0E 6F 3A 6B 6B 6B 66 80 18 
1A A3 AD AD 3D 7B F6 6C 2B 2B 2B FA 90 CF E7 AF 5C B9 F2 F3 CF 3F 0F 0D 0D CD CF CF 67 FA A2 3E 
7C F8 C0 54 E2 D2 A5 4B 99 F5 D1 BC BD BD 99 0C 69 49 FA FA FA FF FD DF FF 2D 79 D9 A5 4B 97 DA 
D8 D8 44 44 44 DC BE 7D BB B2 B2 52 F2 B2 DB B7 6F B7 B3 B3 9B 31 63 06 33 57 D8 C4 C4 24 2C 2C 
AC C1 A8 57 CD EF 3A 8D 24 B9 BC 34 9D 72 2A CB AB 38 1C 8E 93 93 13 F3 E7 97 DD 34 44 0A 6D 59 
55 CC CD CD 69 40 56 50 50 70 EE DC B9 C6 C6 97 AE 5C B9 C2 DC 21 C3 86 0D 93 4C FA 02 55 E9 D6 
AD 1B 93 14 77 FA F4 69 6C 85 23 37 D9 33 63 34 4F 41 41 41 9D 35 0E 69 BE A6 66 50 C3 FA AD A9 
A9 A9 B3 51 8E 8C D6 AC 59 53 53 53 53 E7 6A AF 5E BD 1A 3F 7E 3C 3D 61 FF FE FD F5 DF EE FC F9 
F3 CC 15 CE 9F 3F FF D1 E2 95 94 94 B8 BA BA 4A BE AF 85 85 45 61 61 A1 62 7E 79 45 53 61 FD 66 
67 67 33 33 11 65 E7 E9 E9 59 5A 5A 2A E5 B2 37 6E DC B0 B5 B5 95 F7 B2 26 26 26 7F FF FD 77 6D 
6D 6D 63 97 55 EC 5D D7 6C 68 19 54 F5 EE 0D 2A 2C 2C 64 EA BD C1 16 27 16 8B 85 42 21 B3 09 8B 
91 91 D1 A5 4B 97 64 BF FE DB B7 6F 27 4F 9E CC BC 36 37 37 97 F9 91 E6 B5 65 35 AC DF C6 54 54 
54 CC 9E 3D 9B 16 78 D5 AA 55 52 CE 2C 2F 2F F7 F4 F4 64 1A 66 5A 5A 5A FD 86 29 D9 CC CD CD CD 
6F DC B8 A1 CC B2 AB 4C 0B AA 5F AA B6 B6 76 E3 C6 8D B4 D8 3C 1E 2F 3E 3E 5E CA 1F D5 B4 B4 34 
FA BD B7 4E 3B 6D 3D 24 EB B7 B5 F7 4C 97 97 97 6F DC B8 91 19 6C 22 84 38 38 38 D8 D8 D8 A8 B0 
48 1A 8F CB E5 FA FB FB 87 86 86 CA 3E 7D 9B C7 E3 6D DD BA 75 F1 E2 C5 CD 30 31 D4 D0 D0 30 20 
20 40 72 6D 35 68 90 8D 8D CD 81 03 07 1A EC 63 6E CC DC B9 73 B7 6C D9 C2 AC AD D1 A0 41 83 06 
25 24 24 78 79 79 C9 7E 59 27 27 A7 A3 47 8F 7E F5 D5 57 52 96 96 57 F3 BB 4E C3 3C 7D FA 34 2D 
2D 8D 1E 3B 38 38 F4 EF DF 5F F6 D7 76 E8 D0 C1 D9 D9 99 1E 37 65 1A 22 41 5B 56 11 1E 8F C7 E4 
EA 3C 7E FC F8 9B 6F BE 09 0C 0C 7C F0 E0 01 0D CB 5E BF 7E BD 77 EF DE 6F BF FD 96 D9 67 6D C2 
84 09 FD FA F5 53 5D 79 E1 FF 70 38 9C 89 13 27 D2 6F CB 74 EE 4A 7A 7A BA B8 A1 B1 85 1B 37 6E 
04 07 07 D3 21 7D 17 17 97 8F EE F0 D2 5A A8 30 B4 57 A1 FA 9D 55 3C 1E 2F 21 21 41 D5 E5 52 24 
B5 AD DF DA DA DA FC FC 7C 66 92 90 14 6E 6E 6E F9 F9 F9 8D 7D 3F 56 78 CF B4 B8 DE 8D A1 6E BD 
59 92 54 5E BF EF DF BF 8F 8A 8A AA 33 E7 AF 3E 4B 4B CB D4 D4 54 91 48 24 E3 65 45 22 51 6A 6A 
6A 9D 49 8A F5 0D 1E 3C 38 3E 3E BE A2 A2 42 C6 CB 2A EA AE 6B 36 2A AF DF FA 64 E9 99 FE EB AF 
BF 98 7F C9 DD BB 77 CB FB 16 37 6E DC 60 46 0B 47 8C 18 F1 E8 D1 23 FA BC E6 B5 65 35 AC DF C6 
C8 DE 33 2D 16 8B 5F BC 78 E1 E2 E2 F2 D1 56 46 08 31 37 37 2F 28 28 68 9E 5F A1 F9 B5 A0 FA 65 
D4 D6 D6 C6 C7 C7 33 9D 0E 3C 1E 6F C9 92 25 F7 EE DD A3 03 74 35 35 35 0F 1F 3E FC ED B7 DF 0C 
0C 0C 5A 43 0D 4A 27 59 BF AD B7 C7 45 28 14 EE D8 B1 23 2C 2C 4C F2 49 4F 4F CF AF BF FE 5A 55 
45 6A 55 38 1C CE 17 5F 7C F1 D7 5F 7F 3D 7D FA 34 33 33 33 35 35 F5 FE FD FB 57 AF 5E A5 89 AA 
66 66 66 E6 E6 E6 4E 4E 4E 13 26 4C E8 D1 A3 47 9B 36 CD 3A 84 C2 E5 72 BD BD BD 33 33 33 4F 9C 
38 D1 9C EF DB 12 E9 EA EA CE 9B 37 CF D7 D7 F7 EA D5 AB A7 4E 9D BA 70 E1 C2 CD 9B 37 E9 DA 1A 
06 06 06 96 96 96 B6 B6 B6 CE CE CE 43 87 0E 95 AB 7F B7 4D 9B 36 0E 0E 0E 63 C7 8E 2D 2A 2A 3A 
75 EA 54 46 46 C6 ED DB B7 E9 66 2E 26 26 26 16 16 16 63 C6 8C 71 72 72 EA DF BF BF 5C 97 55 E7 
BB 4E 63 08 04 82 E3 C7 8F D3 63 73 73 73 66 97 1F D9 F5 EB D7 CF D1 D1 91 0E 18 66 67 67 E7 E7 
E7 B3 EE 5D 46 5B 56 89 2E 5D BA FC F4 D3 4F 05 05 05 CC 32 3B 0D E2 F1 78 3F FF FC 33 3A 35 D5 
0A 87 C3 F9 EE BB EF DE BC 79 13 1C 1C CC E7 F3 F9 7C FE 86 0D 1B 36 6C D8 D0 E0 C9 26 26 26 1B 
37 6E 44 0D FE 1F D5 46 F7 CD AF A6 A6 66 F7 EE DD 75 06 7C 5D 5D 5D 4B 4A 4A 54 5D 34 05 6B 9D 
F5 DB 7A A0 7E 35 1B EA 57 B3 B5 A0 FA 95 AB 67 5A 2C 16 D7 D6 D6 66 65 65 59 5A 5A 36 16 75 98 
99 99 1D 3A 74 48 F6 D1 AA 96 A8 05 D5 6F 1D B5 B5 B5 69 69 69 52 AA 8F 10 32 69 D2 A4 2B 57 AE 
A8 BA A4 AA 24 59 BF AD B1 67 9A F6 49 D3 6F 5D CC 93 56 56 56 BF FD F6 1B 56 C4 03 00 00 68 22 
0E 87 33 62 C4 88 CC CC CC 73 E7 CE 1D 3D 7A 34 27 27 E7 CA 95 2B 84 10 33 33 B3 A1 43 87 BA BA 
BA 4E 98 30 41 72 A7 52 50 2B 1C 0E 67 EC D8 B1 99 99 99 39 39 39 89 89 89 17 2F 5E A4 EB 54 F2 
78 BC 2F BF FC D2 DE DE DE CD CD 6D E0 C0 81 18 BE 63 FC 7B BE 8E 58 E6 CD C6 5A BA EA EA EA 88 
88 88 D5 AB 57 4B 46 D2 26 26 26 FB F6 ED 63 E6 4C 68 12 3A 25 AB F5 D4 6F 6B 83 FA D5 6C A8 5F 
CD 86 FA D5 6C A8 5F CD 26 59 BF AD AB 67 9A CF E7 87 87 87 D7 99 74 A8 C1 91 34 00 00 00 00 28 
55 2B 0A A6 4B 4A 4A 02 03 03 E3 E2 E2 24 9F B4 B0 B0 D8 BE 7D 3B D6 C2 03 00 00 00 00 16 5A 4B 
30 5D 58 58 B8 70 E1 C2 94 94 14 C9 27 AD AC AC B6 6D DB 36 6C D8 30 55 95 0A 00 00 00 00 5A 34 
CD 0F A6 C5 62 71 46 46 86 9F 9F 1F 5D 57 8B E1 E4 E4 14 15 15 45 77 3D 05 00 00 00 00 60 41 C3 
67 62 56 57 57 47 45 45 B9 B8 B8 D4 89 A4 3D 3D 3D F7 EF DF 8F 48 1A 00 00 00 00 9A 42 93 7B A6 
1B 4C 92 26 84 04 05 05 05 07 07 CB BE AB 30 00 00 00 00 40 83 34 36 98 BE 7C F9 B2 BF BF 7F 56 
56 96 E4 93 06 06 06 9B 36 6D 9A 36 6D 9A 5C BB A6 01 00 00 00 00 34 48 03 63 4A B1 58 7C F2 E4 
C9 39 73 E6 D4 D9 C8 D4 C2 C2 62 DB B6 6D 23 46 8C A0 4B 03 02 00 00 00 00 34 91 A6 E5 4C 8B C5 
E2 3F FF FC F3 87 1F 7E A8 13 49 3B 39 39 1D 38 70 C0 D6 D6 16 91 34 00 00 00 00 28 8A 46 05 D3 
34 92 9E 37 6F DE 9B 37 6F 24 9F F7 F5 F5 4D 48 48 18 30 60 80 AA 0A 06 00 00 00 00 1A 49 A3 D2 
3C CE 9D 3B 17 14 14 54 27 92 FE F5 D7 5F 03 03 03 75 74 74 54 55 2A 00 00 00 00 D0 54 9A 13 4C 
DF BE 7D 7B D9 B2 65 75 B2 3B D6 AC 59 B3 78 F1 62 4C 37 04 00 00 00 00 65 D0 90 34 8F CA CA CA 
E8 E8 E8 DC DC 5C C9 27 11 49 03 00 00 00 80 52 69 48 30 9D 92 92 B2 6F DF 3E C9 67 A6 4C 99 32 
6B D6 2C 44 D2 A0 6C 67 CE 9C E9 D6 AD 9B 9F 9F 5F 65 65 A5 AA CB 02 CD 0D B5 AF 49 4A 4A 4A 26 
4D 9A 34 64 C8 90 3A 9B 7C 01 00 48 A7 09 C1 74 59 59 59 7C 7C 3C 9F CF 97 7C F2 D0 A1 43 06 06 
06 1C B6 E2 E3 E3 55 F5 EB 40 0B F2 E2 C5 8B C8 C8 C8 E2 E2 62 55 17 04 54 00 B5 AF 49 84 42 E1 
BE 7D FB 4E 9C 38 A1 EA 82 00 40 CB A3 09 C1 F4 AD 5B B7 4E 9E 3C A9 EA 52 40 AB F3 F2 E5 CB A5 
4B 97 26 25 25 A9 BA 20 A0 02 A8 7D 4D 22 14 0A 77 EC D8 11 16 16 A6 EA 82 00 40 8B A4 09 59 10 
E7 CE 9D AB D3 2D 0D A0 6C CF 9E 3D 0B 08 08 38 74 E8 90 AA 0B 02 2A 80 DA D7 24 D5 D5 D5 11 11 
11 AB 57 AF C6 E7 08 00 B0 D3 E2 83 E9 CA CA CA 3A 2B 78 00 28 95 58 2C CE C9 C9 59 B4 68 51 5E 
5E 9E AA CB 02 CD 0D B5 AF 61 4A 4A 4A 42 42 42 F6 EC D9 A3 EA 82 00 40 0B D6 E2 D3 3C 3E 7C F8 
F0 FA F5 6B 55 97 02 5A 8B 7F FE F9 27 30 30 D0 D9 D9 39 2F 2F 8F C7 E3 4D 9D 3A D5 D4 D4 54 D5 
85 82 66 82 DA D7 24 02 81 60 EF DE BD A3 47 8F A6 91 B4 93 93 D3 98 31 63 54 5D A8 E6 50 54 54 
34 64 C8 10 3A 3B 28 2B 2B 4B 81 57 2E 2B 2B 3B 71 E2 C4 BC 79 F3 6C 6C 6C 98 09 48 36 36 36 3E 
3E 3E 07 0E 1C 28 2D 2D 6D CA C5 3F 7C F8 90 9F 9F BF 65 CB 16 37 37 B7 01 03 06 D4 BF 7E 49 49 
89 58 2C 56 D4 EF D2 AA C4 C7 C7 D3 7F 4C 67 67 67 76 01 D5 EB D7 AF 9D 9D 9D E9 45 06 0E 1C 78 
ED DA 35 19 5F 28 79 37 B6 E8 B9 6A 2D BE 67 BA 43 87 0E 18 6C 85 E6 51 59 59 19 1E 1E BE 73 E7 
4E 42 88 99 99 D9 EA D5 AB 07 0D 1A E4 EE EE AE EA 72 41 73 40 ED 6B 98 A3 47 8F CE 98 31 83 10 
C2 E3 F1 16 2C 58 E0 EF EF FF CB 2F BF A4 A7 A7 AB BA 5C 2D D2 A3 47 8F 36 6E DC B8 6F DF BE FA 
A9 32 17 2E 5C B8 70 E1 C2 EF BF FF CE E3 F1 26 4F 9E BC 72 E5 CA 5E BD 7A C9 75 F1 D7 AF 5F FF 
FE FB EF 5B B7 6E 6D 70 14 9A B9 3E 21 C4 DD DD 7D D9 B2 65 9F 7F FE 39 87 C3 61 F9 9B 40 93 DD 
BE 7D 7B E3 C6 8D 5B B7 6E D5 D3 D3 53 75 59 9A 4F 8B EF 99 06 68 66 3C 1E 6F D9 B2 65 99 99 99 
93 27 4F 6E D3 06 2D A8 75 41 ED 6B 98 49 93 26 9D 3D 7B 76 F5 EA D5 AD EA 83 5F 81 AA AB AB F7 
EE DD 3B 6C D8 B0 A8 A8 28 E9 49 E7 7C 3E 9F 9E B9 79 F3 66 19 97 92 AC AD AD 3D 7C F8 B0 AD AD 
ED 92 25 4B 64 C9 E7 4C 48 48 B0 B3 B3 8B 8A 8A AA AE AE 96 F5 17 00 25 88 8D 8D 3D 76 EC 58 AB 
1A 28 68 F1 3D D3 00 CD 86 C3 E1 58 59 59 05 06 06 F6 EE DD 1B 3D 1F AD 0D 6A 5F C3 74 E9 D2 E5 
F4 E9 D3 F6 F6 F6 D8 8E 80 35 81 40 10 1E 1E 1E 1E 1E 2E FB 4B DE BC 79 F3 D3 4F 3F DD BD 7B 77 
ED DA B5 3C 1E 4F CA 99 EC 26 86 F2 F9 7C 7F 7F FF 8A 8A 0A 6C D9 A6 5A 1B 36 6C 18 36 6C 98 B9 
B9 B9 AA 0B D2 4C D0 B3 02 0A 26 14 0A F3 F2 F2 42 43 43 27 4E 9C D8 AB 57 2F 9A 0B D5 AB 57 AF 
89 13 27 86 86 86 E6 E5 E5 09 85 42 E9 57 A8 AC AC F4 F3 F3 A3 2F 0C 0D 0D AD 7F 82 AA D2 B3 DA 
B5 6B E7 E3 E3 D3 A7 4F 9F D6 10 4B 89 C5 E2 27 4F 9E EC DC B9 D3 DD DD FD 8B 2F BE A0 FF 68 9D 
3A 75 72 76 76 0E 0D 0D BD 7E FD FA 47 EB B1 B1 CB 96 94 94 1C 38 70 C0 C7 C7 87 B9 AC 9E 9E DE 
A8 51 A3 E6 CD 9B 77 E2 C4 89 F2 F2 72 16 97 6D FA 5D F7 51 2D BD F6 25 6F 7E 76 A4 EC 66 72 F1 
E2 C5 6E DD BA D1 D3 BA 75 EB 76 F1 E2 45 19 4B A5 C2 54 4B 47 47 C7 71 E3 C6 21 DE 62 4D 28 14 
46 45 45 D5 89 A4 A7 4C 99 92 9C 9C 5C 5A 5A 2A 12 89 C4 62 71 6D 6D ED 9B 37 6F D2 D3 D3 BD BC 
BC 24 43 E7 ED DB B7 07 05 05 09 04 02 29 17 DF B2 65 CB B2 65 CB 24 23 69 3B 3B BB E8 E8 E8 5B 
B7 6E F1 F9 7C B1 58 4C AF FF F6 ED DB DC DC DC 90 90 10 13 13 13 E6 CC B0 B0 B0 C3 87 0F 2B F4 
D7 05 F9 14 14 14 6C DE BC 59 4A 15 6B 26 31 68 A8 E6 AC 5F 91 48 94 9A 9A 6A 69 69 29 FD 66 B3 
B4 B4 4C 4D 4D A5 7F 6A 1B 54 51 51 31 7B F6 6C 7A F2 AA 55 AB EA 9F F0 EA D5 AB F1 E3 C7 33 17 
F4 F2 F2 7A F7 EE 9D 2C 25 2C 2C 2C B4 B0 B0 A0 AF DA BF 7F 3F FB 5F B5 DE 05 67 CF 9E 5D 51 51 
D1 F4 0B CA 4B 19 F5 2B 12 89 CE 9C 39 33 69 D2 24 E9 F5 68 67 67 27 BD 1E EB A8 AD AD BD 7A F5 
EA 47 93 8C 0D 0C 0C 82 83 83 4B 4B 4B 65 2F AD 42 EE 3A 16 9A A1 F6 15 58 BF 92 37 3F 3B 16 16 
16 85 85 85 F5 AF 2C 14 0A 57 AC 58 21 79 66 68 68 68 6D 6D AD 2C A5 52 9F B6 CC FC D9 69 EC D7 
54 06 05 D6 AF EC 24 FF E9 CE 9F 3F CF FA 3A 09 09 09 92 F1 F1 A4 49 93 F2 F3 F3 A5 D4 FB FD FB 
F7 DD DC DC 24 EF 93 98 98 98 C6 CE 4F 4B 4B 33 32 32 92 6C BF 29 29 29 35 35 35 52 CA 53 5A 5A 
BA 64 C9 12 E6 25 63 C6 8C 79 FA F4 29 EB DF 4E 21 54 52 BF 2C EC DF BF 9F 16 75 FC F8 F1 AF 5E 
BD 62 71 85 3A 0D 99 11 17 17 27 FD 4F 81 C2 1B 72 73 92 AC 5F F4 4C 83 62 08 04 82 15 2B 56 38 
3A 3A 7E 74 C9 B0 BC BC 3C 47 47 C7 15 2B 56 28 EA 3B 6B 2B 4C CF 52 9E 92 92 12 5F 5F DF B1 63 
C7 26 27 27 4B 3F 33 33 33 F3 5F FF FA 57 78 78 B8 2C E9 8F 02 81 60 F5 EA D5 76 76 76 09 09 09 
D2 CF 7C F3 E6 4D 78 78 38 3D F3 A3 DD C9 2A BC EB 80 51 5A 5A 9A 93 93 23 F9 4C 46 46 46 49 49 
09 8B 4B A1 2D B7 14 8F 1E 3D 92 4C 92 0E 0A 0A FA E3 8F 3F E8 58 53 63 2F E9 D3 A7 4F 5C 5C 5C 
70 70 30 F3 CC B6 6D DB EE DC B9 53 FF CC D2 D2 D2 88 88 08 66 6F 51 57 57 D7 C4 C4 44 47 47 47 
E9 C3 08 9D 3B 77 FE ED B7 DF D6 AC 59 43 1F A6 A7 A7 63 37 37 95 70 76 76 B6 B2 B2 A2 C7 51 51 
51 85 85 85 AA 2D 4F F3 40 30 0D 0A D0 E0 78 9F 74 E1 E1 E1 41 41 41 32 4E 43 F9 A8 0D 1B 36 B4 
92 16 AB 54 45 45 45 93 27 4F 96 7D CD 5D 3E 9F BF 62 C5 8A 75 EB D6 49 AF C7 97 2F 5F CE 99 33 
67 E5 CA 95 B2 E7 3E 16 15 15 79 78 78 AC 5F BF 5E CA 44 22 95 DF 75 40 E5 E4 E4 9C 3E 7D 9A 10 
E2 EE EE EE EC EC 4C 08 39 7D FA 74 9D F0 5A 76 68 CB EA 4F 2C 16 27 25 25 31 CB EA F9 FA FA FE 
FC F3 CF D2 13 A0 29 5D 5D DD E0 E0 60 5F 5F 5F FA B0 A0 A0 20 3E 3E 5E 24 12 D5 39 ED FC F9 F3 
C7 8E 1D A3 C7 56 56 56 BF FD F6 9B B1 B1 B1 2C 05 E3 72 B9 B3 66 CD 62 FA BF CF 9F 3F 8F 2F CF 
CD CF C6 C6 C6 DF DF 9F DE 0F B9 B9 B9 51 51 51 AD A1 16 10 4C 83 02 5C BE 7C 39 22 22 82 79 38 
7E FC F8 A4 A4 A4 92 92 12 66 54 AE A6 A6 A6 A4 A4 24 29 29 49 72 24 68 DF BE 7D 29 29 29 0A 29 
40 2B 4D CF 52 A8 17 2F 5E 2C 5B B6 4C 72 DD D9 C1 83 07 AF 5D BB F6 FA F5 EB 4C 86 62 4D 4D CD 
93 27 4F 62 63 63 25 D3 2A 36 6E DC 98 98 98 D8 58 6F A2 40 20 F8 F5 D7 5F E3 E2 E2 98 67 78 3C 
9E 9F 9F 5F 7A 7A FA 9B 37 6F E8 08 A0 48 24 2A 2D 2D 4D 4A 4A AA 93 5B 12 1C 1C BC 65 CB 96 C6 
FA A7 55 7E D7 B5 2C 66 66 66 57 AF 5E 6D 70 B0 52 32 B1 4A 4A CA CA D5 AB 57 CD CC CC EA 5C B6 
BA BA 3A 23 23 83 1E DB DB DB 3B 3A 3A D2 E3 E3 C7 8F B3 6B 8F 68 CB EA EF F5 EB D7 4C A7 AF B9 
B9 F9 FC F9 F3 75 75 75 65 7C AD AE AE EE FC F9 F3 99 79 69 69 69 69 4F 9F 3E 95 3C 41 20 10 1C 
3F 7E 9C 1E F3 78 BC E5 CB 97 CB 35 89 4D 5F 5F FF 87 1F 7E A0 C7 EF DE BD 7B FB F6 AD EC AF 05 
85 E0 70 38 AE AE AE DF 7F FF 3D 7D 18 17 17 97 94 94 A4 F1 C3 4D 08 A6 A1 A9 44 22 D1 D1 A3 47 
E9 90 1C 8F C7 8B 8C 8C 4C 4A 4A 72 71 71 31 34 34 64 46 E5 B8 5C AE A1 A1 A1 8B 8B 4B 52 52 D2 
EE DD BB E9 77 56 3E 9F BF 6F DF BE B2 B2 32 85 14 63 D7 AE 5D 52 42 3A E9 98 25 EB EB 6B D1 CB 
C8 CB AE B2 B2 72 F5 EA D5 49 49 49 F4 21 8F C7 5B BF 7E 7D 4E 4E 4E 60 60 E0 67 9F CF 10 26 28 
00 00 20 00 49 44 41 54 7D F6 C9 27 9F D0 E7 B9 5C 6E F7 EE DD 3D 3D 3D D3 D3 D3 57 AD 5A C5 D4 
E3 BA 75 EB 1A 1C AE 15 89 44 D1 D1 D1 D1 D1 D1 CC 33 5E 5E 5E D7 AE 5D DB BE 7D FB E8 D1 A3 F5 
F5 F5 E9 A0 70 9B 36 6D 3A 77 EE EC E2 E2 72 EC D8 B1 BC BC 3C 5B 5B 5B E6 FC B0 B0 B0 33 67 CE 
34 78 65 45 DD 75 A8 FD A6 B8 77 EF 5E 6A 6A 2A 21 C4 C8 C8 68 F8 F0 E1 23 47 8E A4 A9 AE A7 4E 
9D BA 79 F3 26 BB 6B 36 A5 2D 4B 99 67 E9 E7 E7 87 41 09 85 28 2A 2A 62 BE 75 3B 3A 3A D6 FF 8A 
25 DD C0 81 03 99 CE E3 EC EC EC 82 82 02 C9 9F DE BF 7F 9F B9 B8 83 83 C3 A8 51 A3 E4 2D DE 88 
11 23 52 52 52 DE BC 79 73 E4 C8 11 19 BB B4 41 B1 74 75 75 03 02 02 68 32 34 9F CF 8F 8C 8C D4 
F8 E1 26 04 D3 D0 54 E5 E5 E5 CC 1C 7C 0F 0F 8F 99 33 67 6A 6B 6B 37 76 B2 B6 B6 B6 B7 B7 77 60 
60 20 7D 78 FA F4 E9 5B B7 6E 35 E5 DD 5B 67 7A 96 C2 65 66 66 EE DB B7 8F 1E 1B 18 18 C4 C4 C4 
2C 5E BC 58 4A 6F 93 AE AE EE F2 E5 CB 43 42 42 E8 C3 C6 86 6B AF 5C B9 B2 6D DB 36 7A 4C 43 DE 
98 98 18 29 5B 36 70 38 9C E1 C3 87 27 26 26 7A 7A 7A D2 67 F8 7C FE B6 6D DB EA EF 9D A6 DA BB 
0E 18 E7 CF 9F BF 7D FB 36 21 C4 C2 C2 C2 C4 C4 C4 D4 D4 D4 DA DA 9A 10 52 5C 5C 9C 92 92 22 57 
40 8C B6 DC 52 DC B8 71 83 49 D9 1A 37 6E 9C 94 A6 D7 20 2E 97 3B 7A F4 68 E6 E1 E5 CB 97 25 EF 
93 AB 57 AF DE BD 7B 97 1E 8F 1F 3F 5E 5F 5F 5F DE E2 75 ED DA D5 D1 D1 91 C5 0B 41 81 06 0C 18 
C0 CC 07 CD CD CD 8D 8E 8E D6 EC AF B2 08 A6 A1 A9 5E BF 7E CD 4C 36 B2 B3 B3 D3 D1 D1 91 7E 3E 
97 CB 75 73 73 A3 23 77 7C 3E FF C6 8D 1B 4D 79 F7 D6 99 9E A5 58 02 81 20 21 21 41 72 2E D1 94 
29 53 A4 4C 24 A2 B8 5C AE 8F 8F 8F 8B 8B 0B 7D 58 7F B8 B6 BA BA FA C0 81 03 CC 56 0B 81 81 81 
73 E6 CC 91 E5 73 B7 73 E7 CE EB D6 AD 9B 38 71 22 7D 78 EC D8 31 66 D8 97 A1 DA BB 0E A8 B2 B2 
B2 53 A7 4E D1 63 4B 4B 4B 7D 7D 7D 7D 7D 7D 3B 3B 3B FA 8C BC D3 10 D1 96 5B 84 0F 1F 3E 30 2B 
24 9A 9A 9A CA BB 9D 21 D5 BF 7F FF 11 23 46 D0 E3 07 0F 1E BC 7F FF 9E 1E 8B 44 22 E6 4B 14 1D 
EB 68 6A 71 41 45 38 1C 8E 9B 9B 1B 93 1F BF 6F DF 3E 66 E4 53 23 21 98 86 A6 EA D0 A1 03 D3 07 
50 BF 6F B2 41 DD BB 77 1F 34 68 10 3D AE DF E9 28 17 85 A4 67 4D 9B 36 AD B1 B5 6F A6 4D 9B D6 
94 E2 B5 08 85 85 85 4C 48 E4 E2 E2 E2 ED ED AD A5 A5 25 CB 0B BB 74 E9 E2 ED ED 4D 08 E1 F1 78 
3A 3A 3A 75 22 A7 47 8F 1E D1 79 69 84 90 31 63 C6 F8 F8 F8 C8 BE A6 6F D7 AE 5D 99 B8 8A 10 72 
F2 E4 C9 77 EF DE 49 9E A0 C0 BB AE 95 D7 7E 53 DC BD 7B F7 C2 85 0B 84 10 1E 8F 67 6F 6F 4F 6F 
9B 71 E3 C6 99 9A 9A 12 F9 A7 21 2A A4 2D 4B 49 0D DF B1 63 C7 47 BF 74 C1 47 09 85 42 E6 8B B7 
B1 B1 F1 A7 9F 7E CA E2 22 1D 3B 76 EC D6 AD 1B 3D 2E 2D 2D FD F0 E1 03 3D AE AE AE 7E F9 F2 25 
3D 36 33 33 93 5C 1D 0F 5A 1C C9 FC 78 3E 9F BF 65 CB 16 66 CC 41 F3 20 98 86 A6 6A D7 AE 1D F3 
27 2F 2D 2D 4D 96 4D 37 3A 74 E8 70 E8 D0 21 FA 09 57 67 85 5A 16 5A 61 7A 96 62 5D BA 74 89 59 
85 6A F4 E8 D1 5D BA 74 91 FD B5 8E 8E 8E 77 EE DC 79 F5 EA D5 E9 D3 A7 99 31 7A E6 B2 4C 36 E4 
A4 49 93 98 CF 4E 19 59 5B 5B 33 89 95 59 59 59 F7 EE DD 93 FC A9 CA EF 3A 10 89 44 C9 C9 C9 F4 
CE 71 70 70 F8 E2 8B 2F E8 F3 7D FB F6 65 B2 DE E5 9D 86 88 B6 AC FE 2A 2B 2B 9F 3C 79 42 8F B5 
B5 B5 E5 CD F1 A0 DA B6 6D DB A9 53 27 7A FC EA D5 2B 66 0E 83 42 2E 0E EA 63 F0 E0 C1 01 01 01 
F4 38 37 37 37 32 32 52 53 93 3D 10 4C 43 53 F1 78 3C 66 B5 84 D8 D8 D8 05 0B 16 3C 78 F0 A0 99 
A7 EE B6 B6 F4 2C 05 AA AA AA 62 92 8F 8D 8C 8C E4 9D EE C3 E3 F1 4C 4D 4D DB B6 6D 5B E7 79 91 
48 C4 CC 3F 33 32 32 B2 B7 B7 FF 68 DE 48 1D 7A 7A 7A CC 40 70 71 71 71 9D D9 6C EA 70 D7 B5 72 
2F 5E BC C8 CC CC A4 C7 23 47 8E EC D8 B1 23 3D D6 D5 D5 75 70 70 A0 C7 2C A6 21 A2 2D B7 36 42 
A1 50 C6 C1 A5 3A A4 4C 1D 66 34 B8 87 2E 34 1B 0E 87 33 75 EA 54 2F 2F 2F FA 50 83 17 53 42 30 
0D 0A 30 61 C2 84 29 53 A6 D0 E3 D8 D8 D8 BE 7D FB BA B8 B8 EC DC B9 F3 D1 A3 47 4D DF C6 59 16 
AD 2D 3D 4B 81 04 02 C1 FD FB F7 E9 B1 02 C7 55 DF BF 7F CF 8C E8 B1 BE EC F0 E1 C3 99 17 16 16 
16 D6 F9 C4 55 F9 5D D7 CA 5D B8 70 E1 EC D9 B3 84 10 53 53 53 07 07 07 C9 2F 4B 23 46 8C A0 C3 
14 C5 C5 C5 C9 C9 C9 72 85 4A 68 CB AD 0D 97 CB 95 31 AF 0C 5A 22 3D 3D BD C5 8B 17 33 C9 1E EB 
D7 AF 7F F4 E8 91 AA 0B A5 78 08 A6 41 01 F4 F5 F5 D7 AF 5F 2F B9 55 6C 72 72 B2 9F 9F 5F EF DE 
BD 0D 0C 0C 1C 1C 1C 42 43 43 B3 B2 B2 EA A4 BD 2A 56 AB 4A CF 52 A0 F7 EF DF 33 19 90 FD FA F5 
63 FA 17 9B E8 C3 87 0F CC 0A AF 3D 7A F4 90 65 43 87 FA 3E FD F4 D3 DE BD 7B D3 E3 37 6F DE 30 
89 95 94 3A DC 75 AD 56 65 65 25 D3 C3 64 6B 6B DB B7 6F 5F C9 9F 1A 1B 1B 33 A3 0A 39 39 39 F2 
CE 8B 40 5B 56 67 5C 2E 97 5D 73 96 F4 E1 C3 87 D7 AF 5F D3 E3 4F 3F FD 94 99 FF D0 B6 6D 5B 26 
CD AC BA BA 5A CA 9E 4D D0 82 0C 1E 3C 98 59 C9 3E 2B 2B 2B 2A 2A 4A F3 6A 16 C1 34 28 86 89 89 
49 5C 5C DC A6 4D 9B 0C 0C 0C 24 9F E7 F3 F9 69 69 69 2B 57 AE A4 03 C1 D6 D6 D6 11 11 11 CF 9E 
3D 53 46 19 5A 4F 7A 96 02 55 55 55 31 59 AD 5A 5A 5A F2 26 63 34 E6 CD 9B 37 CC 44 A2 F6 ED DB 
CB 3E F5 50 D2 27 9F 7C C2 7C 6C 3F 7D FA B4 AA AA AA CE 09 EA 70 D7 B5 4E 0F 1E 3C 38 77 EE 1C 
3D 1E 39 72 64 9D 55 14 DB B6 6D FB D5 57 5F D1 63 76 BB 21 A2 2D AB 2D 6D 6D 6D 26 DE 7D FE FC 
39 D3 CC E5 F2 F6 ED DB E7 CF 9F D3 E3 2E 5D BA 30 79 62 DA DA DA CC 8C C6 67 CF 9E BD 7A F5 AA 
C9 E5 05 D5 E3 70 38 5E 5E 5E CC 40 62 4C 4C 8C E6 ED F4 8E 60 1A 14 86 4E 1E 7A F8 F0 61 42 42 
C2 37 DF 7C D3 60 EF 45 6E 6E EE A2 45 8B CC CD CD 83 82 82 D8 FD 15 96 A2 F5 A4 67 B5 42 42 A1 
B0 B6 B6 B6 FE F3 2A BF EB 5A 27 66 79 69 2B 2B AB B1 63 C7 D6 3F E1 B3 CF 3E 63 32 A7 59 EC 86 
88 B6 AC B6 DA B5 6B D7 AF 5F 3F 7A 7C FD FA F5 06 77 6B FA A8 A7 4F 9F 5E BF 7E 9D 1E 77 EF DE 
BD 7D FB F6 F4 B8 6D DB B6 CC 16 30 77 EF DE 65 CE 69 50 63 EB F0 BC 7A F5 4A 72 D3 53 50 07 FA 
FA FA 81 81 81 26 26 26 44 43 93 3D 10 4C 83 82 E9 E9 E9 7D FF FD F7 89 89 89 AF 5E BD BA 72 E5 
CA 8E 1D 3B A6 4C 99 52 BF E3 70 ED DA B5 6E 6E 6E AC F7 48 93 F2 EE CD 99 9E C5 AC C3 85 55 B7 
94 8D CB E5 B6 69 D3 E8 DF 2B 95 DC 75 AD B6 F6 25 97 97 B6 B2 B2 6A 70 9D 96 AE 5D BB DA DB DB 
D3 63 76 BB 21 36 73 5B D6 D1 D1 D9 B1 63 47 63 BB A6 83 A4 2F BF FC 92 F9 D6 9A 96 96 26 EF 90 
BD 48 24 3A 75 EA 14 93 5D 66 6D 6D 2D 99 33 3D 74 E8 50 66 A6 C4 E9 D3 A7 B1 D6 B8 C6 18 36 6C 
18 33 DC 94 95 95 B5 6B D7 2E 4D 9A DC 82 60 1A 94 A5 6D DB B6 43 86 0C 99 3D 7B F6 C1 83 07 5F 
BE 7C F9 EC D9 B3 F8 F8 78 C9 BE C3 AC AC AC D9 B3 67 2B FC 03 B2 35 A4 67 29 90 81 81 41 E7 CE 
9D E9 71 45 45 85 A2 FE BA B5 6B D7 4E CA 06 8A 32 92 CC E7 EE DE BD 7B BB 76 ED 3E FA 12 55 DD 
75 AD CA AD 5B B7 98 15 C4 23 23 23 DB B5 6B 57 7F 15 85 36 6D DA 30 EB 0F B2 98 86 48 A1 2D AB 
A7 81 03 07 32 C3 0E 49 49 49 D2 FB 8F EB BB 73 E7 CE B1 63 C7 E8 B1 95 95 D5 E0 C1 83 25 7F CA 
6C A2 49 08 39 75 EA 54 6E 6E 6E 93 CB 0B 6A A1 4E B2 C7 D6 AD 5B CF 9C 39 A3 DA 22 29 10 82 69 
68 0E 6D DA B4 E9 D6 AD 9B 87 87 47 62 62 E2 8D 1B 37 66 CD 9A 45 9F CF CA CA DA B3 67 0F BB 75 
91 1A D3 1A D2 B3 14 48 72 C1 E6 27 4F 9E 30 C1 6B 13 E9 E9 E9 31 93 8A EE DF BF CF EC 70 26 97 
57 AF 5E 3D 7C F8 90 1E 1B 18 18 D4 5F 80 4F BA E6 BC EB 5A 8F 3A DD 8A 32 CA CC CC 7C F1 E2 85 
BC EF 85 B6 AC 9E F4 F5 F5 99 0D 4A 1F 3F 7E BC 7A F5 6A D9 2B 57 20 10 44 45 45 31 2B D0 3B 39 
39 F5 EC D9 B3 B1 8B 17 17 17 47 46 46 B2 B8 73 40 3D E9 EB EB 2F 5C B8 90 49 F6 58 B3 66 4D 9D 
7D 73 5B 2E 04 D3 D0 DC 7A F6 EC B9 69 D3 A6 B9 73 E7 D2 87 F5 B7 A1 6E 3A 8D 4F CF 52 A0 F6 ED 
DB 77 EF DE 9D 1E 17 15 15 31 BB B7 C8 EE F2 E5 CB F5 17 CD D0 D5 D5 ED DF BF 3F 3D BE 79 F3 E6 
3F FF FC C3 A2 6C 85 85 85 4C 79 4C 4C 4C 9A B2 7E 56 33 DC 75 AD 84 E4 F2 D2 B2 3B 7B F6 2C DD 
2B 51 5E 68 CB EA C9 D9 D9 79 CC 98 31 F4 38 29 29 69 C5 8A 15 6F DE BC F9 E8 AB 04 02 41 78 78 
78 74 74 34 7D 68 6E 6E 3E 79 F2 E4 FA ED FA EB AF BF 76 71 71 61 2E FE E3 8F 3F 3E 7E FC 58 F6 
B2 BD 7F FF BE A2 A2 42 F6 F3 A1 39 59 5B 5B CF 9B 37 8F 1E A7 A7 A7 87 86 86 6A 46 65 21 98 86 
26 29 2A 2A 1A 32 64 08 1D D8 FD F3 CF 3F 65 7C 95 AE AE AE 87 87 07 1D 79 BF 7E FD 3A 8B 00 EE 
A3 34 3B 3D 4B 81 B4 B4 B4 98 41 D5 E2 E2 E2 8C 8C 0C B9 B6 3E 11 89 44 87 0F 1F A6 8B 66 B8 B9 
B9 31 D3 FB DA B6 6D 3B 6C D8 30 D6 97 25 84 08 04 02 26 97 C0 C8 C8 68 F8 F0 E1 CC 8F D4 F6 AE 
6B 0D 98 E5 A5 E5 C5 62 1A 22 85 B6 AC 86 8C 8D 8D 17 2E 5C C8 64 4F ED DA B5 CB DD DD FD F2 E5 
CB 52 9A F9 83 07 0F 3C 3D 3D C3 C3 C3 99 67 66 CF 9E 5D 27 C7 83 EA D2 A5 CB C2 85 0B 99 11 B3 
13 27 4E 8C 1F 3F 7E FF FE FD 1F 5D D1 A5 B4 B4 74 E3 C6 8D F6 F6 F6 2C BE EF 41 F3 D0 D2 D2 9A 
3E 7D 3A B3 A4 69 46 46 86 66 2C 7C 89 60 1A 9A 44 32 E3 B6 A0 A0 40 F6 A1 F3 4F 3F FD B4 4F 9F 
3E 84 10 3E 9F AF 8C 01 77 CD 4E CF 52 2C 33 33 33 BA 81 33 21 24 39 39 99 59 B2 4A 16 F7 EE DD 
FB FB EF BF E9 71 EF DE BD 3B 74 E8 C0 FC 88 D9 B9 83 10 72 E4 C8 11 B9 FA 96 08 21 B9 B9 B9 CC 
2C 37 6B 6B 6B 7A B7 50 6A 7B D7 69 3C C9 E5 A5 1D 1C 1C 9E 3F 7F DE E0 72 0A 8C AA AA 2A 7F 7F 
7F 7A 3E BB 69 88 04 6D 59 5D 4D 9C 38 31 24 24 84 79 98 92 92 32 7A F4 E8 E9 D3 A7 A7 A4 A4 BC 
7C F9 92 AE BD 23 16 8B CB CA CA CE 9E 3D 3B 67 CE 9C 21 43 86 24 26 26 32 E7 CF 9D 3B 77 E6 CC 
99 8D AD C5 39 6A D4 A8 E0 E0 60 26 58 2F 2A 2A F2 F4 F4 1C 3A 74 E8 8A 15 2B 2E 5E BC 58 56 56 
C6 AC ED F3 FE FD FB 87 0F 1F C6 C5 C5 B9 B9 B9 F5 EB D7 6F C9 92 25 CC 9F 1A 1E 8F C7 2C B4 07 
EA A3 73 E7 CE 8B 17 2F A6 C3 4D 1A 03 C1 34 34 C9 27 9F 7C C2 EC D7 70 E6 CC 19 D9 47 F3 DF BD 
7B 27 EF 56 0E F2 D2 E0 F4 2C C5 EA D5 AB 17 B3 F0 42 7A 7A FA FE FD FB 65 EC F9 13 0A 85 B1 B1 
B1 4C FA E3 E8 D1 A3 25 D3 9A 7B F6 EC E9 E4 E4 44 8F B3 B2 B2 D6 AF 5F 2F 7B C7 E4 8B 17 2F 22 
23 23 99 CE E3 89 13 27 32 19 D8 44 BD EF 3A CD 26 B9 BC B4 8D 8D 0D B3 DE 70 63 B4 B5 B5 27 4D 
9A 44 8F 59 4F 43 24 68 CB 4A 33 72 E4 C8 8F EE C8 4D F9 F9 F9 D5 E9 18 E6 72 B9 8B 16 2D 5A BB 
76 2D 13 F2 F2 F9 FC D8 D8 D8 F1 E3 C7 77 E9 D2 85 2E 5A DF A6 4D 1B 03 03 83 31 63 C6 EC D8 B1 
43 32 CF DE D7 D7 37 34 34 54 CA 1C 65 2E 97 EB E7 E7 B7 79 F3 66 C9 C5 2E 8B 8A 8A 56 AF 5E 6D 
65 65 65 60 60 40 AF CF E1 70 78 3C 5E 9F 3E 7D BC BC BC 8E 1E 3D 2A F9 16 96 96 96 47 8F 1E F5 
F3 F3 53 D8 3F 56 2B 70 EA D4 A9 4F 3F FD 54 C6 5B 22 3E 3E 9E F5 1B 59 59 59 CD 99 33 47 81 25 
57 39 04 D3 D0 24 3A 3A 3A 76 76 76 F4 38 37 37 77 C3 86 0D B2 04 4C D5 D5 D5 07 0F 1E A4 A1 92 
85 85 85 F2 3A 0F 34 35 3D 4B B1 B4 B5 B5 BF FD F6 5B 66 50 35 2C 2C EC E0 C1 83 1F CD CA 10 8B 
C5 07 0F 1E DC BA 75 2B 7D E8 E6 E6 C6 DC 09 94 96 96 D6 E4 C9 93 E9 D2 66 84 90 E8 E8 E8 0D 1B 
36 C8 B2 F5 C6 CB 97 2F 97 2E 5D CA 6C 22 3D 66 CC 18 67 67 67 C9 13 D4 FC AE D3 60 29 29 29 74 
79 69 1E 8F 37 7E FC 78 59 B2 D8 25 17 9C 66 37 0D 91 42 5B 56 43 DA DA DA 3F FD F4 D3 CE 9D 3B 
65 5F 4C 90 C7 E3 6D D8 B0 21 22 22 A2 CE CA 95 F5 71 B9 DC 19 33 66 9C 3C 79 D2 D2 D2 52 AE 52 
19 18 18 84 86 86 9E 38 71 62 EC D8 B1 8A DA 85 0A 14 8B CB E5 4E 9F 3E DD D5 D5 55 D5 05 51 18 
04 D3 D0 54 A3 47 8F 66 66 A2 44 47 47 FB FA FA 4A 9F 21 24 10 08 D6 AD 5B 17 13 13 43 1F DA DB 
DB F7 EA D5 4B 49 65 D3 D4 F4 2C 85 B3 B2 B2 F2 F0 F0 A0 C7 7C 3E DF CF CF 6F F5 EA D5 E5 E5 E5 
8D 9D 2F 10 08 36 6E DC E8 E7 E7 47 BB 82 78 3C 9E B7 B7 B7 64 E7 31 25 B9 B4 19 21 E4 D7 5F 7F 
FD F1 C7 1F A5 DC 1E 62 B1 F8 D2 A5 4B 6E 6E 6E 71 71 71 F4 19 1E 8F B7 70 E1 42 63 63 E3 3A 67 
AA F3 5D A7 A9 CA CA CA 98 54 54 07 07 87 81 03 07 CA F2 2A C9 05 A7 59 4F 43 24 68 CB EA 8A CB 
E5 BA BB BB 67 66 66 06 07 07 4B 8F 8F 79 3C 9E 8F 8F CF D5 AB 57 7F FA E9 27 19 D7 65 E7 70 38 
23 46 8C C8 C8 C8 38 78 F0 60 9D EF EA 0D 32 31 31 09 0B 0B BB 71 E3 C6 CF 3F FF CC 64 82 81 7A 
32 34 34 0C 08 08 D0 98 64 0F 04 D3 D0 54 C6 C6 C6 B3 66 CD 62 06 E3 12 12 12 3E FF FC 73 6F 6F 
EF 94 94 94 17 2F 5E 30 09 03 95 95 95 0F 1F 3E 8C 88 88 B0 B1 B1 59 B9 72 25 0D C2 4C 4C 4C BE 
FB EE 3B 6D 6D 6D E5 15 4F 23 D3 B3 14 4E 5B 5B 7B F6 EC D9 4C 8A 33 9F CF 5F B9 72 E5 E7 9F 7F 
1E 1A 1A 9A 9F 9F CF 2C 6C F7 E1 C3 07 A6 12 97 2E 5D CA 0C AA 7A 7B 7B 33 19 1D 92 38 1C CE CC 
99 33 99 35 34 08 21 09 09 09 C3 86 0D 5B B4 68 51 56 56 56 59 59 19 ED FF AE AD AD 7D F9 F2 E5 
89 13 27 A6 4E 9D 6A 69 69 99 95 95 C5 9C 1F 12 12 C2 AC 93 25 49 CD EF 3A 8D 24 B9 BC 34 9D 72 
2A CB AB 38 1C 8E 93 93 13 33 EE C1 7A 1A 22 41 5B 56 63 9D 3B 77 0E 0B 0B 7B F8 F0 61 72 72 F2 
DC B9 73 ED EC EC 98 B6 69 6D 6D 3D 77 EE DC E4 E4 E4 C7 8F 1F EF D9 B3 A7 4F 9F 3E F2 F6 16 EB 
E8 E8 4C 99 32 E5 EC D9 B3 8F 1E 3D DA BD 7B F7 F4 E9 D3 99 39 D3 84 90 A1 43 87 7E FF FD F7 91 
91 91 37 6F DE BC 77 EF 5E 70 70 30 73 B3 81 9A B3 B5 B5 9D 39 73 A6 AA 4B A1 50 D2 27 91 40 CB 
D5 3C F5 5B 53 53 B3 66 CD 1A 16 37 DE 9A 35 6B 6A 6A 6A EA 5C AD A2 A2 82 E9 CE 5C B5 6A 55 FD 
B7 93 DC 2D B6 C1 13 64 29 DE FE FD FB 15 F3 CB AB 94 62 EB 37 3B 3B 9B 99 89 28 3B 4F 4F CF D2 
D2 52 29 97 2D 2F 2F 5F B0 60 01 8B DB E3 D7 5F 7F AD A8 A8 68 EC B2 8A BD EB D4 13 2D B0 B2 DF 
45 B2 C5 CD 9E 3D BB C1 7F 73 A1 50 C8 6C C2 62 64 64 74 E9 D2 25 D9 AF FF F6 ED DB C9 93 27 33 
AF CD CD CD 65 7E D4 CA DB 72 F3 D4 2F A8 0A EA 57 B3 49 D6 2F 7A A6 41 01 B8 5C AE BF BF 7F 68 
68 A8 E4 64 11 E9 78 3C DE D6 AD 5B 17 2F 5E CC E5 72 95 5A 36 A2 89 E9 59 4A 62 63 63 73 E0 C0 
81 06 FB 98 1B 33 77 EE DC 2D 5B B6 48 1F 51 E5 F1 78 6B D7 AE DD B4 69 D3 47 B3 24 19 26 26 26 
F1 F1 F1 21 21 21 52 86 83 D5 FC AE D3 30 4F 9F 3E 4D 4B 4B A3 C7 0E 0E 0E CC 22 E2 B2 E8 D0 A1 
03 93 F5 DE 94 69 88 04 6D 19 00 D4 12 82 69 50 0C 1D 1D 9D 90 90 90 B3 67 CF 32 49 8D 52 B8 B9 
B9 9D 3D 7B 76 DE BC 79 CD 16 D3 68 58 7A 96 F2 0C 18 30 E0 C8 91 23 51 51 51 1F 9D 51 64 69 69 
99 9A 9A BA 75 EB 56 59 42 64 1D 1D 9D 80 80 80 FC FC 7C 1F 1F 1F E9 B1 AF 81 81 41 70 70 70 4E 
4E 8E 87 87 C7 47 6F 0F 35 BF EB 34 49 7E 7E 7E 76 76 36 3D B6 B7 B7 97 FD 0B 0C 65 6D 6D CD 4C 
45 6D E2 8E 39 68 CB 00 A0 6E F0 A1 02 0A C3 E1 70 BE F8 E2 8B BF FE FA EB E9 D3 A7 99 99 99 A9 
A9 A9 F7 EF DF BF 7A F5 2A 4D 54 35 33 33 33 37 37 77 72 72 9A 30 61 42 8F 1E 3D DA B4 69 EE 2F 
72 34 3D 8B 19 AA 86 C6 E8 EA EA CE 9B 37 CF D7 D7 F7 EA D5 AB A7 4E 9D BA 70 E1 C2 CD 9B 37 E9 
D2 AD 06 06 06 96 96 96 B6 B6 B6 CE CE CE 43 87 0E 95 37 2A ED D5 AB D7 9E 3D 7B D6 AC 59 73 E6 
CC 99 53 A7 4E 15 16 16 D2 E9 68 3C 1E 6F C8 90 21 23 47 8E 74 72 72 B2 B4 B4 94 B2 60 56 7D 6A 
7E D7 69 06 81 40 70 FC F8 71 7A 6C 6E 6E 2E 99 B1 2A A3 7E FD FA 39 3A 3A D2 95 40 B2 B3 B3 F3 
F3 F3 9B 12 0D A3 2D 03 80 5A F9 F7 3C 00 B1 9C 9B 93 41 4B 41 A7 7A A0 7E 35 15 EA 57 B3 A1 7E 
35 1B EA 57 B3 A1 7E 35 9B 64 FD A2 9F 06 00 00 00 00 80 25 04 D3 00 00 00 00 00 2C 21 98 06 00 
00 00 00 60 09 C1 34 00 00 00 00 00 4B 08 A6 01 00 00 00 00 58 42 30 0D 00 00 00 00 C0 12 82 69 
00 00 00 00 00 96 10 4C 03 00 00 00 00 B0 84 60 1A 00 00 00 00 80 25 04 D3 00 00 00 00 00 2C 21 
98 06 00 00 00 00 60 09 C1 34 00 00 00 00 00 4B 08 A6 01 00 00 00 00 58 42 30 0D 00 00 00 00 C0 
12 82 69 00 00 00 00 00 96 10 4C 03 00 00 00 00 B0 84 60 1A 00 00 00 00 80 25 04 D3 00 00 00 00 
00 2C 21 98 06 00 00 00 00 60 09 C1 34 00 00 00 00 00 4B 08 A6 01 00 00 00 00 58 42 30 0D 00 00 
00 00 C0 12 82 69 00 00 00 00 00 96 10 4C 03 00 00 00 00 B0 84 60 1A 00 00 00 00 80 25 04 D3 00 
00 00 00 00 2C 21 98 06 00 00 00 00 60 09 C1 34 00 00 00 00 00 4B 08 A6 01 00 00 00 00 58 42 30 
0D 00 00 00 00 C0 12 82 69 00 00 00 00 00 96 10 4C 03 00 00 00 00 B0 84 60 1A 00 00 00 00 80 25 
04 D3 00 00 00 00 00 2C 21 98 06 00 00 00 00 60 09 C1 34 00 00 00 00 00 4B 08 A6 01 00 00 00 00 
58 E2 A8 BA 00 00 00 00 00 00 2D 8F 58 2C 26 E8 99 06 00 00 00 00 60 8D 4B FF 47 23 6B D0 3C 1C 
0E 87 A0 7E 35 17 EA 57 B3 A1 7E 35 1B EA 57 B3 A1 7E 35 1B AD 5F 0A 3D D3 00 00 00 00 00 2C 21 
98 06 00 00 00 00 60 09 C1 34 00 00 00 00 00 4B 08 A6 01 00 00 00 00 58 42 30 0D 00 00 00 00 C0 
12 82 69 00 00 00 00 00 96 10 4C 03 00 00 00 00 B0 84 60 1A 00 00 00 00 80 25 04 D3 00 00 00 00 
00 2C 21 98 06 00 00 00 00 60 09 C1 34 00 00 00 00 00 4B 08 A6 01 00 00 00 00 58 42 30 0D 00 00 
00 00 C0 12 82 69 00 00 00 00 00 96 10 4C 03 00 00 00 00 B0 84 60 1A 00 00 00 00 80 25 04 D3 00 
00 00 00 00 2C 21 98 06 00 00 00 00 60 09 C1 34 00 00 00 00 00 4B 08 A6 01 00 00 00 00 58 42 30 
0D 00 00 00 00 C0 12 82 69 00 00 00 00 00 96 10 4C 03 00 00 00 00 B0 84 60 1A 00 00 00 00 80 25 
04 D3 00 00 00 00 00 2C 21 98 06 00 00 00 00 60 09 C1 34 00 00 00 00 00 4B 08 A6 41 C5 3E A8 25 
55 FF AB 00 00 68 A0 B2 B2 B2 7F FD EB 5F 1C 0E C7 DA DA FA E1 C3 87 0D 9E 53 5C 5C EC E8 E8 C8 
E1 70 FC FC FC 2A 2B 2B 9B B9 84 00 2C 20 98 06 00 00 80 E6 A0 AF AF 6F 67 67 47 08 C9 CD CD BD 
72 E5 4A 83 E7 DC BA 75 2B 37 37 97 10 62 67 67 A7 A3 A3 D3 AC E5 03 60 05 C1 34 00 00 A8 A3 CA 
CA CA 94 94 14 1F 1F 9F 01 03 06 70 38 1C 0E 87 33 7A F4 E8 75 EB D6 FD F3 CF 3F AA 2E 1A B0 37 
6E DC 38 53 53 53 42 48 46 46 46 75 75 75 9D 9F 8A 44 A2 8C 8C 0C 3E 9F 6F 61 61 31 7C F8 70 55 
14 10 40 6E 08 A6 01 00 40 ED 5C BD 7A F5 9B 6F BE 19 3F 7E FC EF BF FF 5E 54 54 44 9F CC C8 C8 
58 B6 6C D9 67 9F 7D B6 75 EB D6 FA 71 18 B4 08 BD 7B F7 B6 B6 B6 26 84 E4 E6 E6 3E 7F FE BC CE 
4F 4B 4B 4B 73 72 72 08 21 D6 D6 D6 3D 7B F6 54 41 F9 00 E4 87 60 1A 00 00 D4 CB ED DB B7 FD FC 
FC 52 52 52 1A FC 29 9F CF F7 F7 F7 DF B2 65 8B 50 28 6C E6 82 41 D3 F1 78 3C 7B 7B 7B D2 48 A6 
07 72 3C A0 25 42 30 0D 00 00 6A A4 B2 B2 32 22 22 82 46 54 A3 47 8F FE FB EF BF DF BF 7F 2F 16 
8B 6B 6A 6A AE 5D BB E6 E5 E5 45 4F 8B 88 88 C8 CE CE 56 69 49 81 25 6B 6B 6B 73 73 73 52 2F D3 
03 39 1E D0 42 21 98 06 00 00 35 72 EB D6 AD 63 C7 8E 11 42 5C 5D 5D 0F 1C 38 F0 D5 57 5F E9 EA 
EA 12 42 B8 5C EE E0 C1 83 77 EC D8 F1 F3 CF 3F 13 42 8A 8B 8B 4F 9E 3C 29 12 89 54 5C 5C 90 5F 
9F 3E 7D 46 8D 1A 45 EA 65 7A 30 39 1E F6 F6 F6 BD 7A F5 52 55 F1 00 E4 85 60 1A 00 00 D4 C8 A5 
4B 97 8A 8B 8B 09 21 F3 E6 CD 33 34 34 AC F3 53 1D 1D 9D 19 33 66 58 59 59 11 42 AE 5D BB 56 5E 
5E AE 82 22 42 D3 E8 E8 E8 38 39 39 91 7A 99 1E 4C 8E 87 BD BD BD B6 B6 B6 CA CA 07 20 27 04 D3 
00 00 A0 2E 44 22 D1 E3 C7 8F 09 21 16 16 16 8D CD 3F 33 34 34 1C 3C 78 30 21 44 28 14 D6 D6 D6 
36 6B F9 40 41 86 0E 1D 4A BF 11 31 99 1E 4C 8E 87 95 95 D5 D0 A1 43 55 5D 40 00 39 20 98 06 75 
91 90 90 A0 2D BF 49 93 26 BD 7E FD BA CE A5 B2 B3 B3 59 5C CA D2 D2 F2 CE 9D 3B 2A F9 DD 01 80 
D2 D2 D2 0A 0F 0F 17 8B C5 57 AF 5E 35 33 33 53 75 71 40 59 BA 75 EB 46 83 E9 4B 97 2E 95 94 94 
10 89 1C 0F 2B 2B AB 6E DD BA A9 B8 7C 00 F2 40 30 0D 00 00 2D C9 CB 97 2F 6F DD BA 45 08 E9 D1 
A3 07 16 7C 68 A1 B4 B5 B5 C7 8D 1B 47 08 C9 CE CE 2E 28 28 20 C8 F1 80 96 0C C1 34 00 00 B4 24 
E7 CF 9F A7 EB 78 58 5B 5B B7 6F DF 5E D5 C5 69 75 CA CB CB BD BD BD E9 36 3A 7A 7A 7A 07 0E 1C 
68 F0 34 B1 58 FC C7 1F 7F E8 E9 E9 D1 33 43 42 42 EA 2C 65 38 7C F8 F0 D1 A3 47 13 42 CE 9E 3D 
5B 59 59 89 1C 0F 68 B9 10 4C 83 3A FA E5 97 5F AA 65 93 9C 9C DC A9 53 27 29 97 F2 F5 F5 7D FB 
F6 AD 2C 97 CA CB CB EB DF BF 7F B3 FD 8E 00 C0 C2 A3 47 8F B6 6F DF 4E 08 19 33 66 8C B3 B3 B3 
AA 8B D3 1A E9 E9 E9 05 05 05 59 58 58 10 42 F8 7C 7E 54 54 D4 A3 47 8F EA 9F 56 58 58 18 19 19 
C9 E7 F3 09 21 13 27 4E 5C B0 60 01 97 CB 95 3C C1 D0 D0 D0 C6 C6 86 10 72 E5 CA 95 BB 77 EF E6 
E5 E5 11 E4 78 40 CB C4 FD F8 29 00 00 CA 57 56 56 96 94 74 EC 7F 4F 9E 2C 2A 2A 7A F7 EE 5D 13 
AF 66 64 64 F4 FB EF 7B FB 9B 9A 2A A4 6C A0 26 04 02 C1 FA F5 EB B3 B2 B2 78 3C DE AC 59 B3 8C 
8D 8D 55 5D A2 56 6A C0 80 01 81 81 81 7E 7E 7E 7C 3E 3F 2B 2B 2B 2A 2A 2A 2C 2C 4C 32 37 43 20 
10 6C DE BC 99 A6 6D 98 98 98 2C 5D BA B4 6B D7 AE 75 2E A2 A5 A5 35 6E DC B8 A8 A8 A8 FC FC FC 
93 27 4F D2 64 0F E4 78 40 4B 84 9E 69 00 50 B1 0F 1F 3E EC DA BD DB 66 84 ED 7F AF 5A 75 F1 E2 
C5 A6 47 D2 84 10 E3 6E DD BA 74 EE DC F4 EB 80 FA 10 08 04 81 81 81 D1 D1 D1 84 90 90 90 90 C9 
93 27 AB BA 44 AD 17 87 C3 71 75 75 F5 F4 F4 A4 0F 63 62 62 4E 9E 3C C9 FC 94 26 78 EC DA B5 8B 
3E 9C 33 67 8E AD AD 6D 83 D7 19 38 70 A0 95 95 15 9F CF DF B2 65 4B 71 71 31 72 3C A0 85 42 30 
0D 00 AA 54 51 51 B1 72 E5 2F E1 E1 BF 49 6E 84 D6 74 3D 4D 7A 62 6A 9A 26 11 08 04 21 21 21 34 
92 9E 3B 77 EE FC F9 F3 EB E4 0C 40 33 D3 D5 D5 5D B4 68 11 5D 91 83 CF E7 47 44 44 3C 7B F6 8C 
FE 28 3F 3F 3F 2C 2C 8C 1E BB B9 B9 CD 98 31 A3 B1 CA EA DA B5 2B DD 5A 9C AE 2C 8E 1C 0F 68 A1 
10 4C 03 80 CA 54 54 54 AC 58 B9 F2 CF 83 07 15 7E E5 3E 7D FA 60 B0 58 63 BC 79 F3 26 20 20 20 
22 22 82 10 32 67 CE 9C 35 6B D6 D0 3D 11 41 B5 4C 4D 4D 17 2D 5A C4 E3 F1 08 21 E9 E9 E9 D1 D1 
D1 42 A1 F0 E5 CB 97 E1 E1 E1 74 B1 70 13 13 93 E0 E0 E0 CE 8D 8F 11 71 38 1C 27 27 27 23 23 23 
FA 10 39 1E D0 42 E1 9B 3D 00 A8 86 50 24 DA 19 13 73 E4 48 22 21 64 C8 90 21 B3 7C 67 5A 59 59 
E9 EB EB 57 56 56 2E 0B 0A 4A 4E 3E 41 08 F1 F5 F5 5D 1E B4 8C C3 E1 D4 79 ED C3 87 0F 7D 7C 66 
3C FE E7 1F 42 88 A3 A3 C3 E6 4D 9B 10 5D 69 AA 67 CF 9E 05 04 04 1C 3A 74 88 10 B2 70 E1 C2 B0 
B0 30 D4 B5 FA 70 73 73 BB 74 E9 D2 C6 8D 1B 09 21 7B F7 EE B5 B7 B7 BF 72 E5 4A 62 62 22 FD 69 
48 48 C8 B0 61 C3 A4 5F A1 6F DF BE 96 96 96 C7 8E 1D 43 8E 07 B4 5C 08 A6 01 40 35 72 73 73 77 
EE 8C 21 84 CC 9A E5 1B B0 68 51 BB 76 ED E8 F3 E5 E5 FC 07 0F 1E D2 63 F3 01 66 F5 23 69 42 C8 
8D 1B 37 69 24 4D 08 31 33 33 43 74 A5 91 C4 62 71 76 76 F6 BC 79 F3 E8 D4 B4 5F 7F FD 35 30 30 
10 D9 3B 6A 45 5B 5B 3B 20 20 E0 F2 E5 CB E9 E9 E9 C5 C5 C5 33 67 CE 14 08 04 F4 47 BE BE BE 1E 
1E 1E 0D B6 5F 49 E5 E5 E5 2F FE 1F 7B F7 1D D7 D4 F5 FE 01 FC 44 52 10 30 65 A9 80 A8 88 08 88 
0B B1 2A 4B DC 22 15 17 5A FD 8A AD 5A AC 03 D1 D6 52 57 5D 6D 15 F7 C2 81 03 B5 0E 14 B5 0E 70 
60 AB 40 1D 4C E3 56 54 44 40 44 6A 81 B0 84 08 11 4C C8 EF 8F D3 DE 5F CA 08 21 26 04 C2 E7 FD 
EA EB D5 73 2F 37 D7 27 1C 92 3C 39 F7 B9 E7 E4 E4 10 42 9C 9D 9D 71 47 69 A3 23 10 08 96 2E 5D 
76 E1 E2 45 42 88 99 99 D9 91 C3 87 3A 75 EA A4 EA A0 54 00 65 1E 00 A0 1A CE 4E 4E BB 76 EE 5C 
B8 70 C1 A2 45 8B 98 4C 9A 10 F2 D7 5F 99 74 29 4A 5D 5D 5D 0B 0B 8B AA 0F FC F0 E1 43 7C 42 02 
B3 D9 C5 D6 B6 1E A2 05 D9 BD 79 F3 66 F0 E0 C1 74 76 E1 0E 1D 3A C4 C5 C5 55 7B 98 50 28 DC B8 
71 23 EB 5F 07 0E 1C 10 8B C5 92 3F 0D 0E 0E 1E 3D 7A F4 A3 47 8F 0C 0D 0D 8F 1C 39 B2 7C F9 72 
64 D2 0D 90 99 99 D9 8A 15 2B 68 A9 46 66 66 66 41 41 01 21 C4 C1 C1 C1 CF CF 4F 96 6F B9 F1 F1 
F1 5C 2E 97 C3 E1 78 78 78 68 6A 6A 2A 3D 5C 00 25 40 32 0D 00 AA C1 62 B1 86 0D 1B 3A D7 D7 97 
AD A1 21 B9 3F 35 35 95 2E EE 60 6E 6E 6E 62 62 5A F5 81 D9 D9 D9 77 EF DE A5 6D 53 53 53 CB 26 
39 10 D2 90 49 66 57 19 19 19 3B 76 EC 28 2C 2C AC 7A 58 5C 5C 1C 9D 31 9A 54 19 C5 14 0A 85 FB 
F6 ED FB F6 DB 6F 0B 0A 0A 6C 6C 6C CE 9D 3B 37 75 EA 54 DC 71 D8 60 F5 EF DF 7F FE FC F9 CC 26 
87 C3 F9 EE BB EF 3A 77 EE 5C EB 03 8B 8B 8B 23 22 22 08 21 43 87 0E ED D5 AB 97 12 43 04 50 26 
24 D3 D0 10 AD 5A B5 4A 4B 36 27 4F 9E 94 7E AA 03 07 0E E8 EB EB CB 72 AA 75 EB D6 D5 CF B3 03 
29 3E 7C F8 F0 E8 71 22 6D 77 EC 68 F1 E9 A7 9C AA C7 A4 A4 A6 A6 A6 A6 D2 36 A6 C0 6B 98 24 B3 
AB 33 67 CE 04 07 07 4B 8E 3A 13 42 B2 B3 B3 37 6F DE 4C 6F 53 AB 34 8A 29 16 8B 4F 9F 3E BD 6C 
D9 32 BA 1E 5E 48 48 C8 C0 81 03 6B AD 16 00 15 62 B3 D9 6D DB B6 65 36 0D 0D 0D CD CC CC 6A EA 
32 A1 50 F8 FE FD 7B 42 48 61 61 E1 B6 6D DB 82 83 83 09 21 1E 1E 1E 06 06 06 F5 13 2D 80 C2 21 
99 06 80 06 84 CF E7 BF 78 91 4C DB 1D 3A 74 A8 BA 58 B4 58 2C BE 77 F7 1E B3 D9 C9 CA 0A 05 D3 
0D 10 9B CD FE FA EB AF C7 8C 19 43 37 03 02 02 EE DD FB FF 5E 13 0A 85 BB 76 ED BA 7C F9 32 A9 
6E 14 33 35 35 95 AE 9C 67 6E 6E BE 71 E3 C6 5A EF 60 03 95 4B 4A 4A DA B5 6B 17 B3 99 91 91 B1 
79 F3 E6 EC EC EC 6A 0F 4E 4B 4B 73 74 74 64 B1 58 86 86 86 AB 56 AD 22 58 CC B2 31 D3 D6 D6 DE 
BE 3D 20 FD 65 5A FA CB B4 D8 98 E8 A6 59 30 4D 90 4C 03 40 83 92 95 95 9D 91 F1 CF 9D 85 D5 DE 
DA CF E7 F3 1F 27 26 32 9B 76 3D BA 7F F2 C9 27 F5 14 1C D4 85 B1 B1 F1 A2 45 8B CC CD CD 09 21 
19 19 19 BB 76 ED 2A 2E 2E A6 3F BA 7C F9 32 93 7B 4D 9B 36 CD D3 D3 93 19 C5 14 8B C5 97 2E 5D 
A2 2B E7 65 64 64 D0 31 69 29 6A 2A C8 86 7A 53 52 52 12 18 18 48 BB 8C 71 F9 F2 E5 83 07 0F D2 
7A AD 4A 5A B6 6C 29 B9 1A A2 B9 B9 F9 CF 3F FF 8C 5B 0F A1 51 43 09 1A 34 44 3F FF FC F3 B2 65 
CB 14 72 AA 99 33 67 6E DE BC 19 F7 2D 35 16 AF 5F 67 E4 E7 E7 13 42 4C 4D 4D 25 2F 1C 33 B2 73 
72 D2 D2 D2 68 9B CD 66 37 D9 81 90 46 C1 D1 D1 71 EE DC B9 8B 17 2F 26 84 04 07 07 F7 EB D7 6F 
C6 8C 19 A9 A9 A9 EB D7 AF E7 F3 F9 84 10 17 17 97 05 0B 16 48 BE 3C F3 F3 F3 23 23 23 55 16 31 
D4 91 58 2C 0E 0B 0B A3 8B E9 10 42 68 B1 1C 7D F7 DE B4 69 53 DF BE 7D DD DC DC 2A 3D 44 47 47 
C7 DE DE FE F9 F3 E7 7C 3E 7F CC 98 31 7E 7E 7E DD BB 77 AF E7 B0 41 0E 5C 2E 77 92 D7 64 39 1E 
E8 E3 33 7B C9 E2 C5 0A 8F A7 41 41 32 0D 00 0D 85 58 2C 7E F0 F0 11 6D D7 54 0C 9D 96 9A 4A 17 
4B 23 84 58 5B 5B B7 6D DB AE FE E2 83 3A D2 D0 D0 98 31 63 C6 9D 3B 77 E8 2C D1 BB 77 EF EE D9 
B3 E7 91 23 47 E8 28 26 87 C3 F9 E9 A7 9F 3A 74 E8 20 F9 90 FC FC 7C A6 7F A1 E1 4B 4C 4C 64 EE 
36 99 30 61 82 8F 8F 4F 79 79 39 97 CB BD 70 E1 02 9F CF 5F BD 7A B5 B5 B5 75 A5 2E D6 D6 D6 5E 
BF 7E FD FA F5 EB 55 10 2E 80 72 A0 CC 03 00 1A 0A 3E 9F 9F 94 94 44 DB D5 16 43 8B C5 E2 27 4F 
9E 32 9B 35 DD A1 08 0D 87 81 81 C1 8A 15 2B 6C 6D 6D 09 21 8F 1E 3D 9A 34 69 D2 B1 63 C7 E8 8F 
16 2F 5E 3C 78 F0 E0 4A C7 DB D8 D8 3C 7C F8 50 2C 33 17 17 97 FA 7E 4A F0 AF C2 C2 C2 35 6B D6 
D0 D7 AC AD AD ED 8A 15 2B 0C 0C 0C 8C 8D 8D FD FC FC 68 79 4F 5C 5C DC D6 AD 5B 05 02 81 AA 23 
05 50 2E 8C 4C 03 40 43 F5 C7 D0 F0 00 00 20 00 49 44 41 54 C1 E3 F1 D2 D3 FF 59 AE C5 DA CA AA 
6A 31 74 69 69 69 4A 6A 0A B3 59 ED 1D 8A D0 D0 74 EF DE 7D D9 B2 65 53 A6 4C 21 84 BC 7C F9 92 
EE 1C 33 66 CC CC 99 33 31 DB 5D E3 25 12 89 0E 1E 3C 48 AF 39 10 42 24 AB 35 5C 5C 5C 66 CC 98 
B1 72 E5 4A 42 C8 D1 A3 47 5D 5C 5C 26 4D 9A A4 B2 40 41 41 1C 1C 1C D2 5F A6 A9 3A 8A 06 4A 9D 
DF C8 2A 2A 2A 52 53 53 A3 FE FC 33 36 36 36 35 35 2D 37 37 97 10 A2 A5 A5 D5 A9 93 65 EF DE BD 
87 0E 19 D2 BB 77 6F C9 A5 22 00 40 B5 52 52 52 DE BC 79 43 DB D6 36 D6 55 0F 28 28 28 48 4F 7F 
C5 6C 62 F1 E1 46 81 C5 62 79 7A 7A FA FA FA 32 95 B5 E6 E6 E6 7E 7E 7E C6 C6 C6 AA 0D 0C 3E 46 
6C 6C EC EE DD BB 69 BB D2 34 E1 6C 36 7B C6 8C 19 B7 6E DD BA 7C F9 32 9F CF DF BE 7D BB 9D 9D 
9D 2D 16 57 02 F5 A5 9E 65 1E 15 15 15 31 31 31 E3 BF 98 30 DC FD F3 CD 9B B7 24 24 DC A2 99 34 
21 A4 AC AC EC E9 D3 67 47 8F 06 4F 99 3A CD D1 C9 79 EB D6 6D 79 79 79 AA 8D 16 00 08 21 42 91 
88 7B FB 36 6D 9B B7 6F DF C6 B4 9A E5 5A FE FE FB EF 57 AF 5E D1 76 4D 77 28 42 03 D4 BC 79 73 
C9 CE 32 31 31 69 DD BA B5 0A E3 81 8F 94 93 93 13 10 10 50 ED 34 E1 94 89 89 C9 0F 3F FC 40 17 
EE E1 72 B9 81 81 81 CC 32 E3 A0 4E 04 02 C1 F7 DF FB 59 74 B4 B4 E8 68 D9 CF B5 3F B3 02 40 53 
A3 86 C9 74 61 E1 DB 45 8B 17 4F 9D F6 F5 C3 87 0F A5 1F 59 54 54 14 B8 7B F7 08 8F 91 17 2E 5E 
AC A8 A8 A8 9F F0 00 A0 5A C5 45 45 89 FF CE 79 D7 AE 7D 7B 23 23 A3 AA C7 3C 7B 96 C4 4C B6 85 
E5 5A 1A 91 D8 D8 D8 A0 A0 20 66 93 CB E5 06 04 04 20 BB 6A A4 84 42 E1 81 03 07 2E 5C B8 40 A4 
2E 76 D8 BF 7F 7F 6F 6F 6F DA DE B3 67 4F 58 58 58 A5 85 7B 00 D4 86 BA 25 D3 3C 1E 6F 8E AF 6F 
68 68 98 EC 0F C9 CD CD 5D B8 70 51 60 E0 6E A1 48 A4 BC C0 00 40 BA 94 94 94 C7 FF AE 7D 68 69 
D9 51 A7 CA DD 87 1F 3E 7C 78 91 F2 FF 05 D3 5D BB 75 6D C1 C1 DD 87 8D 80 E4 28 26 E3 C0 81 03 
C8 AE 1A A9 6B D7 AE 6D DA B4 89 B6 A7 4C 99 32 66 CC 98 6A 17 3B 64 B3 D9 BE BE BE 83 06 0D A2 
9B 5B B6 6C 79 FE FC 79 FD 45 09 50 8F D4 AA 66 FA ED DB B7 0B 17 2D AE 34 75 BC 2C 84 42 E1 AE 
C0 40 D3 36 A6 5F 8C 1F 8F 45 6B 01 EA 9F 58 2C 8E 8E 8E 61 46 9D BB 74 E9 C2 D6 D0 A8 74 8C 40 
20 F8 EB AF BF 98 4D F3 F6 E6 55 8F 81 86 A6 D2 28 66 40 40 C0 C3 87 0F 03 03 03 09 21 EB D6 AD 
EB D1 A3 47 8F 1E 3D 54 1D 23 D4 8D 9B 9B 1B B3 FE 8E 74 66 66 66 D7 AE 5D 53 76 3C 00 2A A7 3E 
23 D3 42 91 28 38 F8 58 4C 4C 4C A5 FD 3D 7B F6 DC B3 3B F0 CE 6D 6E 5A 6A 4A FA CB B4 94 94 17 
F1 71 B1 AB 57 AF 32 FD 6F 45 A6 50 28 5C BB 76 5D AD 95 21 00 A0 0C 3C 1E 2F 26 36 96 B6 75 75 
75 AD AD AC AA 1E 53 5A 2A 28 28 28 60 36 CD 3B 98 D7 53 70 F0 11 24 47 31 67 CD 9A F5 D5 57 5F 
F9 FA FA 3A 38 38 10 42 92 92 92 D6 AC 59 53 58 58 A8 D2 00 01 40 7E 58 4E 9C 52 9F 64 FA 79 D2 
F3 13 27 4F 4A EE D1 D2 D2 F2 F7 5F FD DB A9 93 9F 7F FE 79 CB 96 2D 9B 35 6B 46 08 61 6B 68 98 
9A 9A 4E F9 EA AB 88 AB 57 A6 4E 9D 2A 79 7C 51 51 D1 A9 53 BF 95 97 97 D7 6B DC 00 40 C8 ED DB 
77 98 82 69 73 73 73 13 93 6A EE 3E 7C F7 8E 5F 54 54 C4 6C EA 4A 4C 8A 57 5A 5A BA 6E DD 7A 5C 
44 6E 68 5E BD 7A B5 7A F5 6A BA D8 E1 A0 41 83 FC FC FC B4 B4 B4 3A 77 EE FC DD 77 DF 71 38 1C 
42 C8 99 33 67 0E 1E 3C 28 42 89 1D 00 34 66 6A 92 4C 0B 45 A2 0B 17 2E E4 E4 E4 30 7B D8 6C B6 
BF FF EA 2F 27 4F D6 D4 D4 AC F6 21 2D 5A B4 58 BE 6C E9 B4 69 FF C9 A7 6F 46 47 33 D3 A0 82 0A 
AD 5A B5 4A 4B 66 F1 F1 F1 52 4E 75 E0 C0 01 7D 7D 7D 19 4F 75 F2 BF DF C7 A0 7E 94 96 96 FE FE 
FB EF CC 66 E7 CE 36 06 06 FA B2 3F 5C 28 12 05 ED DF 7F E0 E0 C1 15 2B 57 32 F3 F6 80 CA 09 04 
82 AD 5B B7 C6 C5 C5 11 42 38 1C CE 8F 3F FE 68 66 66 46 08 61 B1 58 63 C6 8C 61 26 1E DE BD 7B 
F7 AD 5B B7 54 19 28 00 C0 C7 51 93 64 3A 2F 37 2F 3E 21 41 72 CF C4 89 13 C6 8C 1E 2D BD 00 5A 
53 53 D3 DB DB DB C2 C2 82 D9 93 93 93 C3 2C C0 06 00 F5 E3 16 97 1B F5 E7 9F CC 66 B7 AE DD B4 
B4 B4 AA 1E A6 A1 A1 21 59 24 7D F3 66 74 79 79 79 4E 4E CE 2F BF FC B2 73 E7 AE 56 AD 5A F9 F9 
F9 B5 C2 FC 1E 0D 83 58 2C 0E 0B 0B 3B 7A F4 28 DD AC B4 D8 A1 AE AE AE 9F 9F 9F 9D 9D 1D 21 24 
23 23 63 F3 E6 CD 92 43 21 00 00 8D 8B 9A 24 D3 CF 92 9E 3D 7B F6 8C D9 D4 D5 D5 1D 37 6E 5C 4D 
63 D2 92 DA 98 9A D2 EA 3D 86 E4 74 01 00 A0 6C 3C 1E 6F FF FE 03 CC AD 87 6C 36 BB 4B 97 EA 17 
77 30 36 36 96 5C F7 61 EF BE 7D 36 9D 6D 1D 9D 9C 43 42 4E 98 99 99 ED 0E DC E5 E2 EC 5C 1F 11 
83 0C 9E 3F 7F BE 73 E7 4E 5A E0 51 ED 62 87 9D 3B 77 5E B8 70 21 6D 5F B8 70 E1 C8 91 23 CC DF 
00 00 40 E3 A2 26 B3 79 3C 78 F0 40 72 D3 DE DE DE 4A B6 2A F8 4F 3E F9 44 5F 5F 4F 39 41 41 DD 
78 79 79 79 79 79 29 E4 54 CE CE CE 65 65 65 0A 39 15 28 95 40 20 D8 BC 65 8B E4 0C 3C D6 D6 D6 
E6 E6 1D AA 3D 58 47 47 E7 EB AF A7 25 DC BA 25 59 39 4D 08 71 76 72 DA B0 61 7D BB 76 ED 94 1A 
2A C8 AE A4 A4 24 20 20 80 76 6B 4D 8B 1D B2 58 AC D1 A3 47 4F 9D 3A 35 38 38 98 10 B2 63 C7 8E 
3E 7D FA 48 8E 5E 03 00 34 16 6A 32 32 3D 7F FE FC F8 B8 D8 A3 47 0E CF 9F FF 5D 9F 3E 7D BA 75 
EB CA C1 04 B4 00 0D 5E 51 51 F1 B3 67 FF 29 AC EA D1 A3 87 91 91 61 4D C7 F7 ED DB 37 F8 E8 11 
57 57 57 36 9B AD A5 A5 E5 EA EA 7A F0 C0 FE C3 87 0F 21 93 6E 38 C4 62 F1 89 13 27 0E 1C 38 40 
37 E7 CC 99 E3 E2 E2 52 ED 91 9F 7E FA E9 82 05 0B E8 D5 86 AC AC AC 6D DB B6 65 67 67 D7 5F A0 
00 00 0A F2 4F 49 71 93 9D 39 5F 20 10 2C 5D BA EC C2 C5 8B CC 9E 6D 5B B7 78 7A 7A AA 30 24 C5 
A2 55 E3 0D B9 7F 1B E6 F4 29 B2 D4 08 35 04 0D BF 7F E1 63 A0 7F D5 1B FA 57 BD A1 7F D5 9B 64 
FF AA C9 C8 B4 DC D2 D2 5E DE 92 B8 C4 5C A9 28 13 00 00 00 00 40 8A 26 9D 4C F3 78 BC 35 6B D7 
4A DE 45 3E 64 C8 E0 8E 1D 3B AA 30 24 00 00 00 00 68 44 9A 68 32 5D 51 51 71 EB 16 77 D6 6C 1F 
C9 3B 9F 2C 2C 2C A6 7B 7B 37 96 EB FB 00 00 00 00 A0 72 6A 32 9B 87 8C 84 22 51 2E 8F 17 1D 1D 
7D F8 C8 D1 E4 E4 64 C9 1F B5 6A D5 CA DF 7F B5 A5 A5 A5 AA 62 03 00 00 00 80 46 A7 49 24 D3 2F 
52 52 BE FE DA 3B 2B 2B AB A6 03 FA F4 E9 B3 66 8D BF B5 95 55 7D 46 05 00 00 00 00 8D 5D 93 48 
A6 0B 0B 0A 6A CA A4 75 75 75 57 2C 5F 26 E3 0A 2F 00 00 00 00 00 92 9A 44 CD F4 DF 7F FF 5D D3 
8F 4A 4A 4A 36 6C DC F4 F3 2F AB 5E BD 7A 85 F9 6B 00 00 00 00 A0 4E 9A C4 C8 F4 DB B7 45 52 7E 
5A 54 54 74 EA D4 A9 B3 67 CF 4E 99 F2 D5 0F 7E 7E 2D 5A B4 A8 B7 C0 80 34 9E 19 9D 01 00 00 00 
AA 6A 12 8B B6 EC DC B9 2B E3 75 86 9D 9D 9D 65 C7 8E 84 90 BF B3 B2 E2 E3 13 AE 5F BF 5E 69 51 
62 42 88 AB AB EB 96 CD 9B 5A B7 6E AD 8A 30 95 02 93 C6 AB 37 F4 AF 7A 43 FF AA 37 F4 6F 76 76 
CE 37 33 66 CC 9B EB FB F9 E7 9F AB 3A 16 C5 43 FF AA 37 C9 FE 6D 12 C9 74 B5 DE BF 7F 7F F1 D2 
A5 2D 5B B6 E6 E6 E6 4A EE F7 F0 F0 58 BF 6E AD DA AC 46 8E 17 B3 7A 43 FF AA 37 F4 AF 7A 43 FF 
3E 7D FA EC 9B 19 33 02 77 ED EC DD BB B7 AA 63 51 3C F4 AF 7A C3 0A 88 84 10 D2 BC 79 F3 89 13 
26 9C 3B 7B A6 F7 67 9F 49 EE BF 7C F9 F2 F1 90 10 FC F5 03 00 00 28 D5 DB A2 B7 CD B5 B4 8C 8C 
8C 54 1D 08 C0 47 69 BA C9 34 D5 AE 5D BB B5 EB D6 5A 58 58 48 EE 3C 1F 76 FE 75 66 A6 AA 42 02 
00 00 68 0A 32 5F BF 6E D5 AA 95 81 81 81 AA 03 01 F8 28 4D 3D 99 26 84 58 5B 59 F9 F8 CC 96 DC 
F3 22 25 E5 D9 D3 A7 AA 8A 07 00 00 A0 29 C8 78 FD DA CC CC 4C 4B 4B 4B D5 81 00 7C 14 24 D3 84 
10 D2 DF B5 7F 97 2E 5D 24 F7 70 6F DF 16 8A 44 AA 8A 07 00 00 40 25 0A 0B 0B C7 8D 1B C7 62 B1 
1C 1D 1D D3 D3 D3 AB 3D 26 2B 2B 6B D8 B0 61 2C 16 CB C7 C7 47 20 10 C8 F7 0F 09 04 82 AC BF B3 
4C DB 98 6A 6B 6B 7F 44 BC 00 AA 87 64 9A 10 42 0C 0C F4 3B 77 B6 91 DC F3 B6 F0 ED 87 F2 72 55 
C5 03 00 00 A0 12 06 06 06 AE AE AE 84 10 2E 97 FB E0 C1 83 6A 8F 79 F6 EC 19 97 CB 25 84 B8 BA 
BA CA 9D 0A BF 7F FF 3E E3 F5 EB 4A 65 96 00 8D 11 92 69 42 08 D1 D2 D2 AA 34 1D 5E C6 EB D7 EF 
DF BF 57 55 3C 00 00 00 AA 32 64 C8 10 2B 2B 2B 42 C8 CD 9B 37 CB CA CA 2A FD 54 24 12 DD BC 79 
93 CF E7 DB D9 D9 7D CC 2C 1C 6F DF BE 2D 2C 28 30 33 33 FB A8 58 01 1A 00 35 49 A6 4B 4A 4A 5E 
A4 A4 9C 39 7B 76 C1 C2 85 1E 23 47 3D 7C F8 50 D5 11 C1 47 11 08 04 3E 3E 3E 2C 79 55 BD F2 98 
9F 9F EF EE EE 2E F7 09 FD FD FD 55 F5 AB 00 68 0A 4A 4A 4A 66 CD 9E BD 7B CF 1E 55 07 02 84 10 
62 61 61 E1 E8 E8 48 08 E1 72 B9 55 97 10 E6 F1 78 09 09 09 84 10 47 47 C7 F6 ED DB CB FD AF E4 
E7 E7 57 88 C5 AD 5A B5 FA 98 50 01 1A 02 75 58 01 31 33 33 73 FA 37 33 52 53 53 99 3D 2F 52 52 
7A F6 EC 29 FB 19 CA CA CA 78 3C 9E E4 9E B6 6D 71 4B 04 00 40 3D E1 F3 DF BD 79 F3 F7 E7 EE EE 
AA 0E 04 08 21 84 C3 E1 0C 18 30 E0 D8 B1 63 B4 D2 A3 52 25 86 42 6A 3C 08 21 B9 B9 B9 FA FA FA 
46 86 86 1F 1B 2E 80 AA A9 43 32 AD A7 A7 67 62 62 22 99 4C C7 C7 C5 8F 1A 39 52 F6 17 79 61 E1 
DB E7 CF 93 25 F7 18 19 19 69 22 99 06 00 A8 17 C5 FC 62 3E 9F DF AE 5D 3B 55 07 02 FF 70 74 74 
B4 B5 B5 4D 4A 4A BA 79 F3 A6 87 87 07 33 BA A4 A8 1A 0F 42 C8 CB F4 74 13 13 E3 E6 CD 9B 2B 22 
DE 26 6D E3 A6 4D FB F6 05 31 9B DD BB 77 3F B0 3F C8 D8 D8 58 C6 87 D3 75 28 9F 3D 7B C6 EC F1 
F1 99 BD 64 F1 E2 5A 1F 28 16 8B 79 3C 5E 5C 5C 7C 64 64 E4 D3 67 CF 32 33 33 09 21 6C 36 DB D2 
D2 B2 6B D7 2E 6E C3 DC 9C 9D 9D 64 59 02 AF B0 B0 70 FA 37 33 6A AD 29 D0 D3 D3 6B DF BE BD 5D 
8F 1E FD FA F5 93 F1 CC F5 46 1D 92 69 1D 5D 5D 4B CB 8E B1 B1 B1 CC 9E 5B 5C 6E 5A DA CB 6E DD 
BA CA 78 86 FB F7 EF BD 78 F1 42 72 4F 97 2E 5D D8 1A 1A 8A 8C 12 00 6A 50 AE D0 9B 7D 35 35 35 
15 78 36 A8 1F B9 B9 B9 CD 58 2C 2C DE D1 70 74 EC D8 B1 7F FF FE 49 49 49 B4 D2 83 19 9C 66 6A 
3C 06 0C 18 D0 A1 43 07 B9 CF FF E1 C3 87 BF FE 7A D3 A6 4D 1B 2D 24 D3 8A 96 98 98 F8 F4 D9 33 
D9 93 E9 67 49 CF 24 33 69 59 88 C5 E2 A7 4F 9F 05 04 04 5C BB 7E BD D2 8F 84 42 61 72 72 72 72 
72 72 68 68 98 96 96 D6 E4 C9 5E BE 73 E6 B4 6C D9 B2 4E E7 AF 56 51 51 51 62 62 62 62 62 E2 F1 
90 10 C5 9E F9 E3 A9 43 CD 34 5B 43 63 D0 C0 41 6C F6 FF 7F 31 C8 C9 C9 09 0D 0B 95 71 6E 3B 1E 
8F 17 7C EC B8 50 28 64 F6 58 58 58 38 38 38 28 3E 50 90 CB EC D9 B3 4B 4B 4B C5 75 B1 6F DF 3E 
29 D7 25 56 AF 5E 5D A7 B3 89 C5 E2 95 2B 57 D6 E7 53 06 68 6A DE BC 79 63 60 68 A8 AF AF AF EA 
40 E0 1F DA DA DA 6E 6E 6E A4 CA 9C 1E 4C 8D C7 80 01 03 3E A6 18 B2 BC BC 3C 3F 3F CF BC BD 39 
C6 AD 94 21 3A 3A 5A C6 14 48 28 12 45 47 47 D7 E9 E4 A5 A5 A5 9B 36 6F F6 1C 37 AE 6A 26 5D 49 
59 59 D9 E1 C3 47 46 78 8C 3C 7B F6 9C 62 A7 1B A6 67 FE F2 CB AF 1E 3F 7E AC C0 D3 CA 4D 1D 92 
69 42 88 9D 5D 8F BE 7D FA 48 EE 39 76 EC F8 F5 6B D7 6B 5D 15 BC B4 B4 74 E3 A6 4D F4 AD 81 31 
64 F0 60 DC 5F 0C 00 50 6F D2 D3 D3 CD DB B7 C7 15 FF 06 C5 DE DE 9E 8E 2B 31 73 7A 30 35 1E 0E 
0E 0E F6 F6 F6 1F 73 72 5A 25 6F 62 22 EB E8 29 D4 C9 9D 3B 77 F3 72 F3 64 39 32 3F 2F EF FE FD 
EA 27 40 AC FE F8 FC FC EF FD FC F6 ED 0B 92 1C 82 94 2E 37 37 77 D1 E2 C5 3B 76 EC 50 EC 45 48 
42 C8 8B 94 94 EF FD 7E 78 91 92 A2 D8 D3 CA 41 4D 92 69 7D 7D FD F1 E3 C7 4B 0E 4E 0B 85 C2 45 
8B 17 47 44 44 56 54 54 D4 F4 A8 9C 9C 9C 45 8B 97 84 86 86 49 EE B4 B0 B0 98 34 E9 7F F8 AE 0C 
00 50 3F B0 78 47 C3 D4 A6 4D 1B 9A 4C DF BD 7B 37 3B 3B 9B 48 D4 78 38 38 38 B4 69 D3 E6 63 4E 
5E CC 2F 16 08 04 A6 A6 A6 0A 09 15 28 63 63 63 1B 1B 1B 42 C8 B3 67 CF 9E 25 C9 54 B9 F1 FC 79 
72 52 52 12 21 C4 C6 C6 A6 D6 CA 90 D2 D2 D2 75 EB D7 47 46 46 31 7B D8 6C F6 D8 31 63 8E 05 1F 
7D 70 FF DE CB B4 D4 F4 97 69 69 A9 29 77 6E 73 F7 EC 0E EC F3 DF 21 CE C0 C0 DD BB F7 EC A9 75 
7C DA C7 67 76 FA CB B4 6A FF 7B 92 F8 F8 C6 8D EB 6B D7 AC A1 CF 91 4A 4F 4F FF E9 A7 9F 2B CD 
21 51 FF D4 24 99 26 84 B8 BB 0F 1F 3D 7A 94 E4 9E A2 A2 22 9F 39 73 66 CE 9C 15 1B 1B 5B 58 58 
48 B3 6A B1 58 5C 5C 5C 7C EF FE FD 1F 7F 5C 3A 60 E0 A0 DF 7F FF 5D F2 21 6C 36 7B DE DC B9 96 
96 96 F5 1A 3A 00 40 13 56 56 56 F6 E6 CD 1B F3 8F 98 64 0D 94 41 4B 4B 6B C8 90 21 84 90 F8 F8 
F8 47 8F 1E 11 C5 D5 78 10 42 72 73 73 35 34 34 50 25 AF 58 A6 A6 A6 C3 86 0E A5 ED C8 C8 A8 0F 
1F 3E 48 3F 5E 28 12 C5 C6 C6 D2 31 E6 61 43 87 4A FF 6E 23 14 89 0E 1E FC 55 72 FC D1 CD 6D D8 
9F 51 51 01 01 DB FA F5 EB A7 AF AF CF 62 B1 08 21 CD 9A 35 6B D9 B2 E5 E7 9F 7F FE DB A9 93 A1 
E7 CE 5A 5B 59 31 C7 EF D9 B3 B7 AE 25 25 92 74 75 75 CD DB B7 9F 3C D9 EB 7C 58 E8 82 1F 7E 60 
C6 4F B9 5C EE B1 E3 C7 55 BB 6A B5 FA 24 D3 3A 3A 3A 4B 16 2F AE 5A EB 7C ED FA F5 29 53 A7 F5 
FA AC B7 65 27 2B 8B 8E 96 1D 2D 3B D9 F5 B4 FF E2 8B 09 BF 9D 3E 5D 69 2E 7A 36 9B BD 78 D1 C2 
D1 63 46 D7 63 D4 00 00 4D 5D 61 61 61 6E 6E 6E 3B 24 D3 0D 4F EF DE BD 07 0E 1C 48 08 B9 71 E3 
86 40 20 90 B1 C6 A3 B4 B4 F4 C0 C1 83 BF FD F6 9B 94 4A CB 37 6F DE E8 EB E9 31 13 32 64 65 65 
8D 1C 35 CA A2 A3 A5 45 47 CB 9E F6 BD 2A D5 5E 32 84 22 51 C0 F6 ED F4 30 8B 8E 96 47 8F 06 D7 
5A CC D9 D4 F4 EB E7 42 EB 54 99 EB 09 52 14 17 15 DD 7F 70 9F 10 62 6C 6C EC E8 58 CB AD 62 89 
8F 1F 1F 3A 7C 98 B6 D9 6C F6 8F 4B 96 EC DA B9 B3 7D FB 1A 67 E0 61 B1 58 F6 F6 F6 27 4E 84 0C 
1B F6 4F 7E 2F 14 0A 83 82 F6 E7 E6 E6 CA FE 74 AA D5 BC 79 73 9F 39 3E BE BE 73 98 3D 67 CE 9C 
4D 55 69 B1 87 FA 24 D3 84 90 D6 AD 5B 6F DE B4 B1 F7 67 9F C9 F1 58 2D 2D AD 55 BF FC E2 3D 7D 
3A 0A 3C 00 00 EA 53 51 51 51 33 0D 0D 2C DE D1 00 19 1B 1B 3B 39 39 11 42 1E 3C 78 90 92 92 72 
E7 CE 1D 22 B5 C6 A3 BC BC FC EC D9 73 43 87 B9 AD 5B B7 3E E4 C4 49 29 17 DF D3 D3 D3 DB 9B B7 
67 0A 7B 4C 4D 4D 17 2F 5A A4 AB AB 4B 08 29 2A 2A DA BD 67 EF DB B7 6F AB 3E 8A CB E5 1E 3D 1A 
4C DB A3 46 8D 9C 30 E1 0B 3A 1A 0A 8C 76 ED DA D1 2C 28 35 35 F5 C9 93 27 D2 0F 4E 49 49 79 FC 
38 91 10 62 DF B3 A7 F4 F5 77 CA CB CB CF 9E 3B 57 54 54 44 37 67 CD 9C F9 CD 8C 6F 64 99 3A C9 
C8 C8 C8 7F F5 6A 26 31 BB 7D FB F6 95 AB 57 65 79 22 D2 B1 35 34 66 CF 9A 35 6E 9C 27 DD CC C9 
C9 89 FA F3 4F 15 7E B3 52 AB 64 9A 10 D2 AE 5D BB FD FB F7 7F F9 E5 E4 3A 3D CA DC DC 3C F8 E8 
11 2F AF 49 C8 A4 01 00 EA 59 56 56 96 B6 B6 F6 A7 9C 4F 55 1D 08 54 A6 A1 A1 31 64 C8 10 0E 87 
73 EF DE BD 2B 57 AE D0 62 8F 6A 6B 3C 84 22 D1 B5 EB D7 DD 86 BB AF 58 B9 B2 6F 9F 3E 16 16 16 
89 89 89 11 91 91 D5 9E 96 56 C9 B7 6E DD 5A F2 3C CE 2E 2E DF 7C 33 9D B6 63 62 62 4E 9E 3A 55 
29 37 CA C9 C9 D9 1E B0 9D E6 73 16 16 16 F3 E6 CD D3 D1 D1 51 E0 93 55 0F DA DA DA CE 2E CE B4 
1D 1D 13 2B A5 D2 43 2C 16 47 47 C7 D0 1A 0F 67 17 E7 16 2D 5A 48 39 ED EB D7 AF 6F DE FC A7 42 
A3 6B D7 2E 5F 7D F5 A5 EC F9 92 B1 B1 F1 1C DF 39 4C 55 46 44 44 64 71 71 B1 8C 8F 95 42 47 47 
67 F2 E4 C9 F4 0B 18 21 84 CB BD CD E7 F3 3F FE B4 F2 51 B7 64 9A 10 62 60 A0 BF 7A D5 AA 93 27 
4E 38 3B 39 D5 7A B0 A9 A9 E9 DA 35 6B 7E BF 1C DE B7 6F 5F 7C C1 05 00 A8 7F 2F D3 D3 CD CC DA 
70 38 D2 3E CB 41 55 BA 74 E9 E2 E0 E0 C0 E7 F3 B7 6F DF 9E 95 95 55 53 8D 47 E2 E3 C7 3F FE B8 
74 40 FF FE 51 91 11 01 01 DB A6 4D 9D 4A 08 39 73 E6 6C 4E 4E 4E D5 83 69 95 7C A5 85 15 D9 1A 
1A 5F 4E 9E CC D4 6A 06 05 ED 97 5C C5 43 28 12 05 ED DF 7F F7 DE 3D 42 08 9B CD 9E 33 C7 C7 AA 
53 27 05 3E 4D 75 E2 E0 E0 40 7F B7 5C 2E F7 EF AC AC 9A 0E 2B 2C 2C BC C5 BD 45 08 31 32 32 EA 
65 DF 4B FA 39 EF 3F 78 F0 E6 CD 1B DA 76 77 77 37 31 31 A9 53 48 7D 7A F7 1E 3C 78 10 6D 3F 78 
F0 E0 E5 CB 97 75 7A 78 4D 6C 3B 77 76 ED D7 8F B6 D3 D2 D2 B2 AB FB 63 AB 1F 6A 98 4C 13 42 9A 
35 6B E6 E8 E8 70 FC F8 B1 D8 98 E8 55 AB 7E 71 1F 3E 5C F2 9E C2 76 ED DA 0D 1A 38 F0 C7 25 4B 
AE FC F1 7B 74 F4 CD C9 93 BD F0 ED B6 21 0B 0A 0A D2 D1 D1 61 C9 CC C7 C7 47 20 10 48 39 E1 4F 
3F FD 24 FB D9 58 2C 96 BF BF 7F BD 3D 59 80 A6 46 28 12 E5 E6 E6 62 F1 8E 06 CB C4 C4 64 C0 80 
01 84 90 AC AC 2C 52 73 8D 47 F7 1E 3D A2 22 23 56 AD FA A5 6D DB B6 2C 16 6B E0 A0 81 D6 56 56 
89 89 89 37 AB BB E1 8C 56 C9 57 BD E5 B4 75 EB D6 7E DF CF D7 D3 D3 23 84 14 15 15 ED 0B 0A 62 
C6 1A 23 AE 5E 3D 76 EC 38 6D 8F 1D 3B 66 A4 87 07 C6 BF 6A 62 6A 62 D2 A7 77 6F 42 48 7A 7A FA 
E3 47 35 4E C3 CC D4 78 F4 EA 65 DF A1 83 B9 94 13 0A 45 22 66 55 17 5D 5D DD 7E 2E 2E 75 FD E5 
73 38 1C 47 07 47 DA 2E 29 29 79 FE FC 79 9D 1E 5E 13 1D 1D 9D 6E DD BB D1 76 56 56 D6 5F 7F FD 
A5 90 D3 CA 41 3D 93 69 8A C5 62 99 99 99 4D 9D 32 65 EF DE 3D 51 91 11 CC EC 2A D1 37 6F 1C 3A 
F4 EB EC D9 B3 6C 6C 6C 50 D7 01 00 A0 42 65 EF DF FF FD F7 DF AD 5A B5 C2 BB 71 C3 C4 62 B1 DC 
DC DC 98 79 1E 6A 9A C7 83 AD A1 F1 E9 A7 FF 5F A8 D3 BE 5D BB B1 9E 63 09 21 17 CE 5F A8 5A FD 
5C 54 54 C4 FE E4 93 6A A7 F2 F8 AC 77 EF E9 DE DE B4 1D 11 11 19 1A 1A 26 16 8B D3 D2 D2 B6 6C 
DD 46 0B 12 AC AD AC E6 CD 9B 87 59 14 A5 D0 D4 D4 EC F7 EF 78 6D 6C 6C 6C B5 B3 3B 8B C5 E2 3B 
77 EF D2 5F A9 93 A3 13 53 2C 51 AD D2 92 92 B4 B4 7F C6 92 CD CD CD 4D 4C E4 99 D0 D0 DE BE 27 
F3 AF 3C 4F 4E 56 D4 E4 1B B6 B6 B6 4C 9B 87 91 69 00 00 68 82 DE BF 7F 9F 9D 9D D3 F1 BF 57 FC 
A1 41 B1 B4 B4 A4 73 06 CB BE 56 0B 8B C5 1A 31 62 84 85 85 45 7C 42 42 4C 4C 6C A5 9F 66 65 65 
E9 E8 E8 18 18 18 54 7D 20 5B 43 63 EA D4 29 AE AE AE 74 F3 C0 C1 83 0F 1E 3C DC B3 77 6F 7A 7A 
3A 21 84 CD 66 2F F9 71 09 66 51 AC 55 CF 9E 76 9D 3A 75 22 84 DC B9 7B 37 AB BA 39 3D 8A 8A 8A 
12 E2 13 08 21 46 46 46 7D FB F6 95 7E B6 0F 1F 3E 30 B7 1E CA 5D 91 65 64 64 C4 7C 25 7B 5B F8 
F6 83 82 16 70 D1 95 A8 2C C8 78 FD 5A 21 E7 94 03 92 69 00 00 50 99 FC 82 82 77 EF DE 61 F1 8E 
86 AC B8 B8 98 96 3E 3B 3B 3B CB BE 3C 70 FB 76 ED E8 64 0B A7 4E 9D AA 34 38 FD 32 3D DD 5C 62 
2A 8F 4A F4 F5 F5 17 2F 5A 44 17 10 79 F3 E6 CD 8C 99 33 2E 5E BC 44 7F 34 6B E6 CC FE FD FB CB 
FD 44 9A 0E 13 13 93 DE 52 2B 3D D2 5E BE 7C F4 F8 31 91 A1 C6 83 10 52 58 58 58 50 50 40 DB 3A 
DA 3A CD 9A C9 93 3A B6 68 D1 82 B9 C7 F1 CD 9B 37 95 E6 26 96 5B 8B 16 9C 86 30 5B 39 92 69 68 
E8 66 CF 9E 5D 5A 5A 2A 96 D9 BE 7D FB A4 5F 01 5C BD 7A B5 EC 67 13 8B C5 2B 57 AE AC B7 27 0B 
A0 4E CA CB CB 2F 5E BA B4 7D C7 0E 29 97 74 0B 0B 0A 2A 44 22 5A 26 4B 08 E1 F3 F9 B3 7D 7C E8 
2C C2 56 D6 36 95 56 A8 65 88 C5 E2 33 67 CF 5A 59 DB D0 23 57 FB FB AB 76 C9 06 F5 16 1F 1F CF 
E5 72 39 1C 8E 87 87 87 2C B3 A1 51 2C 16 CB 7D F8 70 33 33 B3 DB 77 EE C4 C7 C7 33 FB 69 95 BC 
A9 69 1B 29 6F D4 5D BB 76 F1 F3 FB 9E B6 0B 0B DF D2 6A 04 07 07 87 69 D3 A6 A2 1C 48 16 9F 7C 
F2 49 7F D7 1A 2B 3D C4 62 71 42 42 42 49 49 09 91 A1 C6 43 19 84 22 91 A2 A6 B1 D3 D2 D2 6C DE 
00 6E B7 40 32 0D F5 24 3F 3F DF DD DD 5D CA 7D 7E EE EE EE F9 F9 F9 AA 0E 13 00 14 A0 A2 A2 E2 
C6 8D 9B A3 C7 8C 9D 3F FF FB 53 A7 7E 93 B2 9E 42 C6 EB D7 AD 5A B5 62 AE F8 73 38 9C 05 3F FC 
40 87 3F 85 42 61 50 50 50 B5 97 6E 53 52 53 F7 EE DD 47 73 AC DE 9F 7D 36 7B D6 2C E4 58 4A 52 
5C 5C 1C 11 11 41 08 19 3A 74 68 AF 5E B5 CC F9 50 49 07 0B 8B CF DD DD 85 42 E1 85 8B 17 99 5B 
09 69 95 BC A9 89 89 94 9B D8 58 2C D6 A8 91 23 99 59 84 09 21 7A 7A 7A DF 7E 3B AF 75 EB D6 72 
3D 89 A6 C8 DE BE 57 97 2E 5D 08 21 71 F1 F1 AF FF FB 22 E2 F3 F9 5C EE 6D 22 5B 8D 87 32 B0 35 
34 14 75 FF E8 DB B7 6F AB 9D 31 A6 9E 21 99 06 80 06 4A 2C 16 67 64 64 EC DA B5 6B FC F8 F1 56 
56 56 5A 5A 5A 5A 5A 5A 0E 0E 0E F3 E7 CF 8F 8A 8A 92 3E 67 0B A8 4A 45 45 C5 83 07 0F 26 79 4D 
9E 39 6B 96 59 9B 36 BD 3F FB 2C 27 27 E7 DC B9 D0 9A 46 8E D3 D3 D3 CD CC CC 24 EF 69 B3 B2 B2 
9A 3F FF 3B 3A 2B ED 8B 94 94 FD FB F7 57 1A 57 2B 2D 2D 0D 0C 0C A4 45 B4 7A 7A 7A DF FB 7D 4F 
4B 02 40 51 84 42 E1 FB F7 EF 09 21 85 85 85 DB B6 6D 0B 0E 0E 26 84 78 78 78 54 5B E5 2C 05 5B 
43 63 FC F8 71 C6 C6 C6 D7 AE 5D BF 73 F7 2E DD 49 AB E4 CD 6B 2B 2D D0 D4 D2 92 9C 36 C4 D0 D0 
10 CB FA D4 49 CB 56 2D FB F4 E9 4D 08 79 F3 E6 CD FD 07 0F 24 7F F4 F2 E5 CB 07 0F 1E 10 42 6C 
6D 6D DB B5 6B 5B EB A9 B4 B4 B4 3E FE 8E CF 77 EF DE BD 7B F7 8E B6 2B BD E4 3F 86 48 24 A2 5F 
AA 09 21 CC 54 D6 F5 0F C9 34 00 34 44 19 19 19 33 66 CC B0 B6 B6 5E B8 70 61 78 78 38 33 B2 F2 
F0 E1 C3 7D FB F6 79 78 78 0C 1D 3A F4 DA B5 6B 15 15 15 AA 8D 13 2A C9 FC EB AF 65 CB 57 B4 34 
32 BA 1C 7E E9 E0 C1 03 74 B1 86 4B E1 E1 D5 0E 4E 97 95 95 F1 78 3C D3 36 A6 92 1F D5 2C 16 CB 
63 C4 88 D1 A3 47 D1 CD D3 A7 CF 44 45 45 31 3F 15 8B C5 67 CE 9C BD 74 29 9C 6E 4E 9B 36 95 99 
99 18 14 25 2D 2D CD D1 D1 91 C5 62 19 1A 1A AE 5A B5 8A 10 32 68 D0 20 77 77 77 39 4E D5 C9 CA 
6A C4 88 CF 85 42 E1 99 D3 67 4A 4B 4B 09 21 F9 05 05 E5 E5 E5 C6 AD 6B F9 FE C3 E5 72 99 B9 F0 
08 21 E9 E9 E9 81 81 81 F4 0C 20 0B B6 86 C6 A0 81 83 68 7E 19 1F 17 2F 39 FA 10 17 1F 4F 6B 3C 
1C 1D 1D 24 E7 60 A9 09 87 C3 D1 FF B7 10 EB 65 7A BA 7C BD 90 9F 9F 9F F5 EF A4 D7 FA 06 FA 9F 
C8 5C 2F 24 DD DF 7F FF CD B4 DB B5 AB 71 6D 73 65 43 32 0D F5 C4 C8 C8 E8 CA 95 2B 52 4A 93 AF 
5C B9 D2 10 6E 23 00 95 13 8B C5 D1 D1 D1 23 47 8E 3C 7E FC B8 94 C3 EE DE BD 3B 71 E2 C4 A0 A0 
20 66 58 02 1A 82 F6 ED DA 9D 3C 11 B2 7B 77 A0 B5 B5 35 8B C5 EA 65 6F EF E4 E4 94 93 93 73 F9 
F7 DF AB 0E 4E 0B 04 82 D7 19 AF 2D AA 4C E5 A1 A3 A3 E3 3B 67 0E DD 2F 14 0A F7 EC DD CB 7C 0C 
3F 7C F8 30 60 FB 76 DA 76 76 72 9A 3A 65 0A 0A 3C 14 AE 65 CB 96 92 AB 72 98 9B 9B FF FC F3 CF 
B2 DF 7A 28 89 AD A1 31 6A E4 48 3D 3D BD A8 3F FF BC 73 E7 2E 21 A4 B0 A0 40 24 12 7D FA 29 47 
CA A3 78 3C DE AE 5D 81 CC 0C 12 D4 A5 4B E1 97 C2 C3 55 B8 64 74 A3 D3 B9 B3 0D 9D 39 EE EE BD 
7B CC 92 2B C5 C5 C5 B7 6E 71 09 21 BA BA BA 2E CE CE B2 9C 47 57 57 B7 93 95 15 6D BF 7C F9 32 
33 33 53 8E 60 5E A4 A4 D0 0C 9E 10 62 DE DE 5C 21 2F 5B B1 58 9C 9A 9A C6 6C CA F7 27 AA 10 48 
A6 01 A0 61 89 89 89 F9 E6 9B 6F 5E BC 78 41 08 E1 70 38 7E 7E 7E F7 EF DF E7 F3 F9 65 65 65 02 
81 20 25 25 65 CD 9A 35 86 86 86 84 10 3E 9F BF 72 E5 CA B3 67 CF E2 F3 B5 E1 60 B1 58 FA FA FA 
4C 41 A4 BE BE FE A4 FF 4D 64 B3 D9 97 2F FF CE 7C 9C 33 F8 7C FE DB A2 A2 6A 67 3A B3 B4 B4 9C 
37 77 2E 1D 57 7B FA F4 D9 81 83 07 85 22 51 7E 7E FE 96 2D 5B 69 8E A5 A7 A7 B7 70 E1 02 7C 03 
57 06 1D 1D 1D 7B 7B 7B 73 73 73 43 43 43 6F 6F EF 4B 97 2E D1 75 5B E4 D3 B5 6B D7 E1 6E 6E 42 
A1 30 2C 2C 4C 20 10 64 BC 7E 6D 62 62 C2 DC 72 5A 95 50 24 3A 7A 34 98 CB E5 12 42 D8 6C F6 EA 
D5 AB BE F8 62 3C FD 51 40 C0 F6 A7 4F 9F C9 1D 49 53 63 D4 B2 A5 43 DF BE 84 90 37 6F DE 24 DC 
BA 45 77 66 66 FE 95 94 94 44 08 B1 B7 B7 EF D8 B1 A3 2C E7 F9 E4 93 4F EC ED 7B D2 76 49 49 49 
6C 5C 5C 5D DF 72 4B 4B 4B AF 5F BB 4E DB BA BA BA CC D9 3E 52 51 51 11 B3 4C A6 79 FB F6 6D 54 
37 29 10 92 69 00 68 40 FE FE FB EF 35 6B D6 D0 A2 8E 1E 3D 7A 5C BC 78 71 FD FA F5 5D BB 76 A5 
73 08 34 6B D6 AC 7D FB F6 0B 17 2E 3C 79 F2 64 FB F6 ED 09 21 7C 3E 3F 28 28 E8 B5 EA A6 17 85 
5A 39 3B 3B F7 ED D3 27 3D 3D FD D2 A5 4B 95 3E 83 F3 F3 F3 45 22 91 81 A1 61 B5 0F 1C 39 D2 63 
E2 C4 09 B4 7D FA F4 99 E8 E8 E8 E0 63 C7 E2 13 12 E8 1E BF EF BF EF D9 53 31 1F C9 50 89 B6 B6 
F6 FA F5 EB 5F BD 7A 95 9F 9F 7F E8 D0 A1 EE DD BB 7F CC D9 34 35 35 27 FE 6F A2 AE AE 6E D4 9F 
7F DE 7F F0 20 3D 3D BD 75 EB 56 52 4A 66 A3 A3 A3 F7 1F 38 40 DB 13 27 4E F8 DF C4 89 33 67 CE 
A4 97 29 72 72 72 36 6D DE 5C 75 15 18 A8 16 5B 43 A3 5F BF 7E 4C A5 07 2D CF B8 7D FB 36 BD D7 
5F C6 1A 0F 8A 59 A2 9C 10 72 E9 E2 A5 D7 75 1C 9C BE 7B F7 6E 4C EC 3F D3 8D DB F5 E8 D1 A1 43 
87 3A 3D BC 26 8F 1E 3D BE 7D E7 0E 6D DB DA DA AA F0 DE 09 24 D3 00 D0 50 88 C5 E2 D0 D0 D0 9B 
37 6F 12 42 4C 4C 4C 36 6F DE EC EC EC 5C F5 A6 6F 16 8B 35 60 C0 00 5A CA 49 08 89 8F 8F BF 70 
E1 42 7D C7 0A 32 D3 D7 D7 9F 34 69 12 21 24 34 34 AC D2 67 70 56 56 56 8B 16 2D 8C 6A 48 A6 35 
35 35 E7 CD 9D DB B5 6B 17 42 48 49 49 C9 F7 DF FB 05 05 ED A7 3F 1A 35 6A E4 84 09 5F 60 41 E9 
C6 A2 8B AD ED D0 21 43 4A 4A 4A 42 8E 87 A4 A7 A7 B7 69 D3 A6 A6 64 3A E3 F5 EB 8D 1B 36 D2 DA 
AD AE 5D BB CC 9B 3B 57 53 53 D3 AA 53 A7 39 73 7C 68 52 18 13 13 13 1C 7C 0C 33 21 CA A8 7B F7 
6E 3D 7A 74 27 84 3C 78 F8 F0 F5 EB D7 25 25 25 09 B7 12 48 5D 6A 3C 28 33 33 B3 21 83 07 D3 F6 
8B 94 94 9D 3B 77 CA 5E 39 CD E3 F1 F6 EC DD C7 D4 78 B8 7F EE AE AF AF 5F 87 E7 50 83 D2 D2 D2 
73 A1 E7 98 32 3F 67 17 67 1D 89 05 5C EA 19 92 69 00 68 28 72 72 72 2E 5F BE 4C DB E3 C7 8F 77 
72 72 AA E9 48 16 8B 35 78 F0 E0 C1 FF BE B9 27 24 24 54 2A AF 84 06 C5 D1 D1 A1 6F DF BE E9 E9 
E9 BF FF FE BB E4 E0 74 76 76 8E 94 C5 3B 08 21 A6 A6 A6 8B 17 2D A2 F3 E0 D2 52 1F 42 88 85 85 
C5 BC 79 F3 54 F8 C1 09 75 A5 AD AD 3D 61 E2 04 5D 5D DD 3F AE 5C B9 7A 35 A2 A6 05 2F 05 02 41 
60 60 E0 8B 94 14 42 08 9B CD FE E1 87 1F E8 6A 3E F4 9E D4 CF 3F FF E7 0E C8 43 87 0F DF FB 77 
6E 10 90 CE C0 C0 C0 D1 C1 91 10 92 93 93 73 E7 EE DD CC CC CC C7 8F 13 49 5D 6A 3C 28 B6 86 C6 
98 31 63 98 A1 DF D0 D0 B0 1D 3B 77 D2 29 5F A4 CB CF CF 5F B1 72 25 2D DA 21 84 74 ED DA 65 E8 
90 21 75 7E 1A 55 54 54 54 9C 3F 7F 81 B9 11 D9 DA CA 4A B5 AB F9 20 99 86 86 2E 28 28 48 47 47 
47 CA 04 D5 D5 0A 09 09 A9 E9 84 3F FD F4 53 5D CF C6 62 B1 E2 E2 E2 EA F3 59 37 4D 4F 9F 3E BD 
76 ED 1A 6D 0F 1E 3C 58 FA DC 49 86 86 86 DD BA 75 A3 ED 57 AF 5E E5 E5 E5 29 3D 3E 90 57 AB 56 
AD 46 8E F4 20 84 5C BE 7C 39 FB DF C5 8D 85 22 51 C6 EB 0C 23 23 23 4D A9 1D ED EC E2 F2 CD 37 
D3 99 4D 36 9B 3D 67 8E 8F 55 A7 4E 4A 0D 18 14 CE BE 67 4F D7 7E FF 2C 23 22 39 E7 1D 43 2C 16 
87 5F BE 7C FE FC 3F 57 99 2A 2D 76 A8 A3 A3 33 6F EE 5C 7A 87 59 51 51 51 C0 F6 1D 3C 1E 4F F9 
51 37 7A 2C 16 6B F0 90 C1 F4 EB 68 7C 5C 7C 7C 7C 02 9D 95 D9 C1 A1 2F 87 23 ED 1E D0 AA BA 76 
ED 32 6D DA 54 66 73 FF FE 03 73 E7 CE 7B FD BA C6 7A 0F B1 58 FC E0 C1 83 C9 93 BF 8C 8C FC 67 
36 1E 36 9B ED 3B 67 CE C7 2F 77 5A 5A 5A BA 7B F7 9E 9F 7F F9 85 D9 33 D6 73 6C 7B D5 4D E5 41 
90 4C 03 40 C3 F1 F4 E9 53 DA 30 31 31 A9 F6 E3 56 92 A6 A6 26 33 EB ED FD FB F7 1B C2 BC FD 20 
85 DB B0 61 DD BB 77 7F FA F4 59 44 44 24 1D 9C 2E 2F 2B CB CF CF AF F5 BE 7E B6 86 86 E4 4D FA 
BA BA BA 6D DA B4 41 81 47 A3 A3 A3 A3 33 69 D2 24 36 9B 6D 66 66 56 ED 6D A3 92 0B F1 54 BB D8 
A1 95 95 D5 B7 DF CE A3 6D 2E 97 1B 72 E2 04 8A 3D 64 61 D9 6A 95 7A 32 00 00 20 00 49 44 41 54 
B1 A3 5D 8F 1E 84 90 EB 37 6E 6C DF B1 83 10 A2 AB AB EB E4 E4 54 D7 17 11 8B C5 9A 36 75 AA E4 
4A 3A D7 AE 5F 77 1B 3E FC C7 1F 97 72 B9 DC B7 6F DF D2 D7 75 45 45 45 5E 5E DE D5 AB 11 D3 BE 
F6 1E 37 FE 8B 17 12 73 62 FA FA CE 71 1B 3E 5C BE 67 21 16 8B 8B 8B 8B 5F A4 A4 EC DD B7 6F E8 
30 B7 6D 01 01 FF 5F E0 E1 E4 34 71 C2 04 D5 BE 27 A8 6C 82 6B 00 00 49 EF DF BF 4F 4B FB 67 92 
A3 EC EC 6C 29 35 1E D0 18 B5 6E DD 7A FC B8 71 89 89 89 E7 42 43 DD DD 87 1B 1B 1B 0B 04 82 8C 
8C D7 9E 9E 9E D2 1F F8 22 25 65 DF BE 20 66 B3 A8 A8 68 7B C0 F6 4E 96 96 58 A8 A5 D1 E9 D5 CB 
7E F0 E0 41 3C 5E 6E D5 64 BA D2 42 3C D5 2E 76 C8 62 B1 46 7C FE F9 B5 6B D7 22 22 22 09 21 BF 
FE 7A E8 B3 5E BD 54 7B 71 BF 51 D0 D3 D3 73 72 76 8A 4F 48 28 2B 2B A3 85 52 76 3D 7A 58 D6 A5 
C6 83 A1 A3 A3 B3 EA 97 5F 34 9A 69 9C 39 7B 96 EE 29 2B 2B FB ED F4 E9 DF 4E 9F AE F5 B1 B3 66 
CD 9C E3 E3 53 EB 8C 78 FB F6 05 49 BE DE 6B 65 61 61 F1 F3 2F 3F AB 7C 56 1F 8C 4C 03 40 83 20 
16 8B 45 18 67 52 5F 2C 16 6B E0 A0 81 D6 56 56 89 89 89 11 91 91 84 90 C2 C2 C2 D2 D2 52 43 A9 
8B EA 95 96 96 06 05 05 D1 1C 8B 71 F7 DE 3D DC 82 D6 18 71 38 9C 31 A3 47 77 30 37 6F DE BC B9 
E4 7E D9 17 E2 E1 70 38 DF CE FB 96 7E 8F 2A 29 29 D9 B5 2B 10 97 A4 6A C5 62 B1 9C 9C 9C 68 A5 
07 E5 E4 EC 24 65 6A 42 E9 5A B4 68 B1 7A F5 AA 85 0B 17 C8 BE 84 A1 9E 9E DE A6 4D 1B 17 2D 5A 
54 A9 DF 3F 9E 9D 9D DD C1 03 FB AD FF 9D 03 5B 85 30 32 0D 0D 91 B6 B6 F6 BE 7D FB F6 ED DB A7 
A8 13 D2 25 63 14 75 36 00 90 43 FB 76 ED 46 8D 1E B5 75 EB B6 F0 F0 CB EE C3 87 E7 E7 E7 B3 58 
2C 29 43 4A 62 B1 F8 52 78 78 68 68 18 DD 9C 37 6F 2E 21 24 30 70 37 21 64 FF 81 03 9F F5 FE 6C 
F0 A0 41 F5 13 39 28 8A B3 B3 73 41 61 61 A5 A4 8A C5 62 4D 9B 36 55 B2 1E 57 8A 6E DD BA DE 4A 
88 57 4E 74 6A CB AA 53 27 7B 7B FB D8 D8 58 22 6F 8D 87 A4 E6 CD 9B CF F5 F5 1D 35 72 D4 86 0D 
1B 22 A3 A2 A4 2C 9B A5 A5 A5 35 79 B2 D7 EC 59 B3 14 7E 1D 49 4F 4F 6F E6 CC 19 DE 5F 7F DD 40 
6E 44 46 32 0D 00 0D 4E 8F 1E 3D 42 42 42 AC AD AD 55 1D 08 28 12 8B C5 1A 35 6A 54 68 68 D8 ED 
DB B7 AF DF B8 41 08 D1 D7 D3 93 72 17 D4 D3 A7 CF 02 02 FE 59 EC D0 D5 D5 F5 9B E9 D3 CB CB CB 
EF DC B9 CB E5 72 85 42 E1 C6 0D 1B 2D 2D 2D AB 5D F0 05 1A 2C 7D 7D FD FF 4D 9C 88 92 F7 7A F6 
E9 A7 9F 3A 3A 3A D0 64 5A EE 1A 8F 4A DA B7 6F B7 67 CF EE DC DC DC 98 98 D8 C8 C8 C8 94 D4 54 
5A A7 C7 66 B3 2D 2D 2D 1D 1D 1D 86 0E 19 D2 AB 57 2F 05 26 BB AD 5A B5 EA D4 C9 B2 6F DF BE AE 
AE AE 3D BA 77 FF E4 93 4F 14 75 E6 8F F7 CF 1F 34 D6 0F 53 57 F4 3D 0B FD AB AE D4 A3 7F CB CB 
CB 09 21 02 81 60 D1 A2 45 07 0E 1C 20 84 74 EA D4 E9 D4 A9 53 F2 2D 15 41 97 77 51 0F EA D1 BF 
92 84 22 D1 8E 1D 3B 02 03 77 3B 3B 39 B5 6D DB 56 28 12 AE 5B BB B6 DA EB C5 6F DF BE FD 6E FE 
F7 31 31 31 84 10 63 63 E3 83 07 0E 74 EB D6 95 10 12 17 1F 3F 77 EE 3C 3A 13 E2 17 5F 8C 5F BD 
6A 95 94 99 F5 1A 38 F5 EB 5F 90 84 FE 55 6F 92 FD 8B 9A 69 00 68 10 B4 B5 B5 99 19 3C 52 53 53 
33 32 32 54 1B 0F 28 03 5B 43 63 CC E8 D1 66 66 66 F1 09 09 A7 CF 9C A9 69 F1 0E A1 48 14 1C 7C 
8C 66 D2 84 90 39 3E 3E 74 E9 16 42 88 83 83 C3 97 93 27 D3 F6 F9 F3 17 FE F8 03 E5 5B 00 A0 62 
48 A6 01 A0 A1 E8 D1 A3 07 D3 BE 76 ED 1A BD F1 1C D4 4C 07 0B 8B CF DD FF 59 7D A3 5D 0D 53 C3 
72 B9 DC 43 87 0F D3 76 A5 C5 0E D9 1A 1A 53 A7 4E E9 FD D9 67 84 10 A1 50 18 B8 7B B7 E4 DC 5B 
00 00 F5 0F C9 34 00 34 14 3D 7A F4 60 66 C4 FB F3 CF 3F 5F BC 78 A1 DA 78 40 19 D8 1A 1A E3 C7 
8F A3 37 24 55 5B F1 CC E3 F1 76 ED 0A A4 85 1C D5 2E 76 68 6C 6C FC ED B7 F3 E8 EC 04 E9 E9 E9 
41 41 41 B2 AF 6C 0C 00 A0 70 48 A6 01 A0 A1 30 33 33 1B 31 62 04 6D 3F 7F FE 7C EF DE BD 25 25 
25 AA 0D 09 94 A1 93 95 D5 88 11 9F 57 BB 78 87 50 24 3A 7A 34 98 2E 3E 2C 65 B1 43 67 17 97 89 
13 27 D0 76 68 68 D8 A5 F0 70 54 A6 02 80 AA 20 99 06 80 86 42 43 43 E3 AB AF BE 1A 30 60 00 DD 
FC F5 D7 5F 17 2D 5A 94 9B 9B 2B E5 21 C5 C5 C5 A7 4E 9D 0A 0F 0F AF 97 00 41 31 D8 1A 1A A3 46 
8E 6C DB B6 6D D5 64 3A 3A 3A 7A FF 81 03 B4 3D 7A F4 28 8F 11 23 AA 9D F9 81 AD A1 31 73 C6 0C 
A6 90 7A D7 AE C0 14 14 7B 00 80 8A 60 36 0F 35 87 BB 89 D5 9B 7A F4 2F 9D CD 83 11 13 13 E3 EB 
EB CB D4 78 58 5B 5B CF 9C 39 73 F4 E8 D1 6D DA B4 A1 33 75 08 04 82 82 82 82 07 0F 1E 5C B9 72 
E5 DC B9 73 05 05 05 47 8E 1C F1 F2 F2 A2 C7 63 36 8F 46 A1 BC BC FC F4 99 33 E3 3C 3D 1B C8 34 
B1 2A A1 C6 FD 0B 04 FD AB EE 24 FB 17 C9 B4 9A C3 8B 59 BD A9 47 FF 56 4A A6 09 21 B7 6E DD FA 
F6 DB 6F 1F 3F 7E 2C E3 19 90 4C 37 46 42 A1 50 43 43 A3 29 4F 39 AC DE FD 0B E8 5F F5 86 A9 F1 
00 A0 41 73 74 74 FC FD F7 DF 97 2C 59 62 68 68 28 FD C8 7E FD FA 9D 38 71 62 EC D8 B1 F5 13 18 
28 10 9B CD 6E CA 99 34 00 A8 0D 8C 4C AB 39 7C 33 56 6F EA D1 BF 55 47 A6 19 85 85 85 D7 AE 5D 
BB 72 E5 4A 72 72 32 BD 29 8D 10 E2 E0 E0 60 63 63 33 64 C8 90 7E FD FA 99 99 99 55 4A C8 30 32 
0D 8D 05 FA 57 BD A1 7F D5 1B CA 3C 9A 10 BC 98 D5 9B 7A F4 AF 94 64 5A 0E 48 A6 A1 B1 40 FF AA 
37 F4 AF 7A 43 99 07 00 00 00 00 80 02 20 99 06 00 00 00 00 90 13 92 69 00 00 00 00 00 39 21 99 
06 00 00 00 00 90 13 92 69 00 00 00 00 00 39 21 99 06 00 00 00 00 90 13 92 69 00 00 00 00 00 39 
21 99 06 00 00 00 00 90 13 92 69 00 00 00 00 00 39 B1 55 1D 00 00 34 75 EA B4 66 21 00 00 34 35 
18 99 06 00 00 00 00 90 13 92 69 00 00 00 00 00 39 21 99 06 00 00 00 00 90 13 92 69 00 00 00 00 
00 39 21 99 06 00 00 00 00 90 13 92 69 00 00 00 00 00 39 21 99 06 00 00 00 00 90 13 92 69 00 00 
00 00 00 39 21 99 06 00 00 00 00 90 13 92 69 00 00 00 00 00 39 21 99 06 00 00 00 00 90 13 92 69 
00 00 00 00 00 39 21 99 06 00 00 00 00 90 13 92 69 00 00 00 00 00 39 21 99 06 00 00 00 00 90 13 
92 69 00 00 00 00 00 39 21 99 06 00 00 00 00 90 13 92 69 00 00 00 00 00 39 21 99 06 00 00 00 00 
90 13 92 69 00 00 00 00 00 39 21 99 06 00 00 00 00 90 13 4B D5 01 00 00 00 00 00 34 3E 62 B1 98 
60 64 1A 00 00 00 00 40 6E 6C FA 3F 9A 59 83 FA 61 B1 58 04 FD AB BE D0 BF EA 0D FD AB DE D0 BF 
EA 0D FD AB DE 68 FF 52 18 99 06 00 00 00 00 90 13 92 69 00 00 00 00 00 39 21 99 06 00 00 00 00 
90 13 92 69 00 00 00 00 00 39 21 99 06 00 00 00 00 90 13 92 69 00 00 00 00 00 39 21 99 06 00 00 
00 00 90 13 92 69 00 00 00 00 00 39 21 99 06 00 00 00 00 90 13 92 69 00 00 00 00 00 39 21 99 06 
00 00 00 00 90 13 92 69 00 00 00 00 00 39 21 99 06 00 00 00 00 90 13 92 69 00 00 00 00 00 39 21 
99 06 00 00 00 00 90 13 92 69 00 00 00 00 00 39 21 99 06 00 00 00 00 90 13 92 69 00 00 00 00 00 
39 21 99 06 00 00 00 00 90 13 92 69 00 00 00 00 00 39 21 99 06 00 00 00 00 90 13 92 69 00 00 00 
00 00 39 21 99 06 00 00 00 00 90 13 92 69 00 00 00 00 00 39 21 99 06 00 00 00 00 90 13 92 69 00 
00 00 00 00 39 21 99 06 00 00 00 00 90 13 92 69 00 00 00 00 00 39 21 99 06 00 00 00 00 90 13 92 
69 00 00 00 00 00 39 21 99 06 00 00 00 00 90 13 92 69 00 00 00 00 00 39 21 99 06 00 00 00 00 90 
13 92 69 00 00 00 00 00 39 21 99 06 00 00 00 00 90 13 92 69 00 00 00 00 00 39 21 99 06 00 00 00 
00 90 13 92 69 00 00 00 00 00 39 21 99 86 FA C3 E3 F1 4E 9D 3A E5 ED ED ED E4 E4 C4 FA 97 93 93 
93 B7 B7 F7 A9 53 A7 78 3C 5E 4D 0F CC CF CF 77 77 77 67 7D 9C B8 B8 38 29 B1 09 85 C2 67 CF 9E 
6D DF BE 7D CC 98 31 1D 3A 74 A0 0F E9 D0 A1 83 87 87 87 BF BF FF 9D 3B 77 84 42 A1 12 7E 25 F0 
1F C9 C9 C9 3D 7B F6 94 A3 73 43 42 42 54 1D 3B D4 59 59 59 59 64 64 E4 DC B9 73 7B F5 EA 45 FB 
B1 73 E7 CE DE DE DE 11 11 11 02 81 40 D5 D1 C1 47 11 08 04 11 11 11 DE DE DE 9D 3B 77 66 B1 58 
9F 7E FA E9 D0 A1 43 37 6D DA F4 FA F5 6B 55 87 06 A0 34 62 50 53 0D A4 7F 79 3C DE 92 25 4B 38 
1C 8E 94 3F 42 0E 87 B3 64 C9 12 1E 8F 57 F5 E1 79 79 79 C3 87 0F FF C8 3F F2 D8 D8 D8 6A 63 7B 
FF FE FD D9 B3 67 FB F4 E9 23 FD E1 DD BB 77 3F 71 E2 C4 FB F7 EF 95 FC AB AA 9B 06 D2 BF 8A F2 
FC F9 73 3B 3B 3B 39 3A F7 F8 F1 E3 AA 8E 5D 29 D4 AC 7F 25 DD BB 77 CF C5 C5 A5 A6 0E ED D3 A7 
CF 9F 7F FE 59 51 51 A1 EA 30 95 4B 2D FB B7 A2 A2 22 2E 2E AE A6 77 54 0E 87 B3 6C D9 B2 E2 E2 
62 55 87 59 1F D4 B2 7F 81 21 D9 BF 18 99 06 A5 4B 48 48 18 36 6C D8 C6 8D 1B F9 7C BE 94 C3 F8 
7C FE C6 8D 1B 87 0D 1B 96 90 90 50 6F B1 BD 7C F9 D2 CB CB EB 8B 2F BE B8 73 E7 8E F4 23 13 13 
13 27 4F 9E FC C5 17 5F 3C 7C F8 B0 7E 62 03 50 57 37 6F DE 1C 37 6E 9C 94 8B 45 77 EE DC 99 30 
61 C2 6F BF FD C6 7C 62 41 A3 20 16 8B 7F FB ED B7 51 A3 46 D5 F4 8E CA E7 F3 D7 AD 5B E7 E5 E5 
95 91 91 51 CF B1 01 28 0F 92 69 50 AE A4 A4 24 3F 3F BF 47 8F 1E C9 78 FC A3 47 8F BC BC BC A4 
97 64 28 4A 42 42 C2 B8 71 E3 C2 C2 C2 64 7F 48 78 78 F8 D8 B1 63 AF 5D BB 86 CF F8 86 C3 C1 C1 
A1 57 AF 5E AA 8E 02 64 95 92 92 B2 64 C9 92 5A 73 A9 82 82 82 1F 7F FC F1 DE BD 7B F5 13 15 28 
44 74 74 F4 8F 3F FE 58 50 50 20 FD B0 CB 97 2F FB F9 F9 E5 E6 E6 D6 4F 54 00 CA 86 64 1A 94 A8 
AC AC 6C DF BE 7D 5C 2E 97 6E 1A 1A 1A AE 5A B5 2A 31 31 91 CF E7 33 17 4A F8 7C 7E 62 62 E2 AA 
55 AB 0C 0D 0D E9 61 19 19 19 3B 76 EC 28 2C 2C 64 CE 63 64 64 74 E5 CA 95 9A 2E B5 AC 5E BD 9A 
1E 36 7C F8 F0 BC BC BC 9A 0E AB 74 4D B9 6A 96 6F 63 63 B3 61 C3 86 C4 C4 C4 D2 D2 52 FA 90 B2 
B2 B2 97 2F 5F 6E DF BE BD 7B F7 EE CC 61 19 19 19 D3 A7 4F 8F 8E 8E 56 D2 2F AD 29 B3 B1 B1 79 
F8 F0 61 AD 17 D7 2A 2A 2A 42 42 42 68 D5 90 B9 B9 F9 C6 8D 1B 6D 6D 6D 55 1D 3B C8 44 24 12 1D 
3B 76 8C 79 4F 70 73 73 8B 8A 8A 7A FB F6 2D ED D9 D2 D2 52 2E 97 EB E5 E5 45 7F 9A 91 91 71 EC 
D8 B1 B2 B2 32 D5 C5 0B 75 C0 E3 F1 B6 6D DB C6 7C 4D EA D3 A7 4F 68 68 68 5E 5E 1E 2D D7 E1 F3 
F9 37 6F DE 1C 39 72 24 FD 69 58 58 D8 89 13 27 30 2A 01 6A A5 D6 4F 2F 68 A4 54 DB BF 8F 1E 3D 
B2 B2 B2 A2 31 B8 B9 B9 25 25 25 49 39 38 2D 2D CD C3 C3 83 F9 9B 3C 77 EE 9C 8C FF 8A 8C C9 B4 
24 1E 8F E7 E9 E9 C9 FC 5B 86 86 86 DB B6 6D 7B F7 EE 5D 4D C7 BF 7F FF FE D0 A1 43 4C BA 4F 08 
19 34 68 D0 5F 7F FD 25 63 84 CA D3 34 5F BF 37 6E DC 30 37 37 A7 CF 7D FB F6 ED 6A 5C 59 AB 7E 
FD 5B 50 50 C0 BC CC 3D 3C 3C B2 B2 B2 AA 1E F3 EE DD BB 99 33 67 D2 63 3E FB EC B3 94 94 94 FA 
8F B3 7E A8 59 FF 9E 3B 77 8E 79 87 1C 33 66 4C 76 76 76 D5 63 DE BD 7B E7 EB EB 4B 8F 71 70 70 
78 F9 F2 65 FD C7 59 6F D4 AC 7F A1 12 C9 FE C5 C8 34 28 51 52 52 52 4A 4A 0A 21 C4 D4 D4 74 F9 
F2 E5 9D 3B 77 96 72 70 C7 8E 1D 37 6F DE CC DC 7F A6 BC 3B FA C5 62 F1 89 13 27 98 EA 0E 3B 3B 
BB 8B 17 2F 7E FF FD F7 BA BA BA 35 3D 44 4B 4B CB DB DB 3B 3C 3C 9C 09 EF FA F5 EB C1 C1 C1 22 
91 48 19 11 82 14 39 39 39 01 01 01 74 F4 6B E6 CC 99 33 66 CC 60 B1 58 AA 0E 0A 64 C5 E3 F1 FE 
FA EB 2F DA F6 F2 F2 32 31 31 A9 7A 8C AE AE EE B4 69 D3 E8 95 87 7B F7 EE E5 E4 E4 D4 6B 88 20 
97 F2 F2 F2 D8 D8 58 DA B6 B3 B3 5B BF 7E BD B1 B1 71 D5 C3 74 75 75 BF FB EE 3B FA 46 CA E5 72 
AF 5D BB 56 AF 51 02 28 07 92 69 50 A2 97 2F 5F D2 46 8F 1E 3D BA 76 ED 5A EB F1 D6 D6 D6 A3 47 
8F A6 ED E4 E4 64 C9 4A 0F 05 CA C8 C8 38 73 E6 0C 6D 9B 9A 9A 6E DB B6 CD C5 C5 45 96 84 CC C9 
C9 69 DB B6 6D A6 A6 A6 74 F3 D8 B1 63 CF 9F 3F 57 46 84 50 13 A1 50 B8 73 E7 CE 0B 17 2E 10 42 
EC EC EC FC FC FC A4 7C 05 82 06 AE 43 87 0E 35 FD A8 65 CB 96 1D 3B 76 AC C7 58 E0 63 F1 F9 FC 
67 CF 9E D1 F6 88 11 23 AC AD AD 6B 3A D2 C2 C2 62 F0 E0 C1 B4 7D E7 CE 1D 4C 83 08 6A 00 C9 34 
28 91 99 99 19 6D 88 44 A2 8A 8A 8A 5A 8F D7 D0 D0 E8 DD BB 37 6D 17 16 16 4A 9F FD 43 6E 71 71 
71 CC 0D 8E DE DE DE FD FB F7 97 FD B1 FD FB F7 F7 F6 F6 A6 ED A4 A4 A4 88 88 08 C5 C7 07 35 BB 
76 ED DA AE 5D BB 68 7B E1 C2 85 D2 AF 75 40 03 C4 E1 70 0C 0C 0C 68 FB C9 93 27 35 1D 96 97 97 
47 BF 8A 9B 9A 9A 36 6F DE BC 9E 82 83 8F 90 97 97 97 9D 9D 4D DB 5D BB 76 D5 D0 D0 A8 E9 48 4D 
4D 4D 1B 1B 1B DA 4E 4B 4B 7B F7 EE 5D 7D C4 07 A0 4C 48 A6 41 89 98 41 5C 2E 97 FB E0 C1 03 59 
1E 32 7A F4 68 5A 81 F4 F0 E1 43 E6 0D 57 81 04 02 41 4C 4C 0C 13 DE 98 31 63 D8 6C B6 EC 0F 67 
B3 D9 FF FB DF FF 98 DB DD E2 E3 E3 8B 8A 8A 14 1E 24 54 8B C7 E3 ED DE BD 9B 7E C5 9A 30 61 82 
87 87 07 0A 3C 1A 9D 96 2D 5B DA DB DB D3 F6 A5 4B 97 98 F4 4B 52 49 49 C9 89 13 27 68 47 3B 3A 
3A 62 88 BA D1 91 72 CD 81 6A D1 A2 05 6D E4 E6 E6 D6 3A F5 07 34 34 99 99 99 DB 02 02 4A 4B 4B 
65 39 98 C7 E3 6D DE BC 25 3F 3F 5F D9 51 A9 16 92 69 50 22 3B 3B 3B 5A B6 C1 E7 F3 BF FB EE BB 
E3 C7 8F AB FC 8A 5E 61 61 61 72 72 32 6D BB B8 B8 C8 91 AF 5B 58 58 30 C3 E7 C9 C9 C9 59 59 59 
8A 8C 0F 6A 20 16 8B 2F 5C B8 70 F1 E2 45 42 88 A9 A9 E9 BC 79 F3 98 01 4E 68 44 34 35 35 BF FE 
FA 6B FA 75 F4 F2 E5 CB 33 67 CE 8C 8E 8E 66 C6 26 CB CB CB 1F 3F 7E EC EB EB BB 67 CF 1E 42 08 
87 C3 99 36 6D 1A 3A BA D1 A9 35 CD 62 7A FC D1 A3 47 79 79 79 CA 8F 08 14 26 33 33 F3 87 1F 16 
EC DA 15 B8 F2 A7 9F 6A ED 68 1E 8F B7 70 D1 E2 3D 7B F7 2E 5D B6 4C BD F3 69 24 D3 A0 44 AD 5B 
B7 9E 3E 7D 3A BD 91 28 39 39 79 CA 94 29 B6 B6 B6 4B 97 2E BD 71 E3 86 AA 06 74 B3 B2 B2 98 64 
DA CA CA 8A 19 20 91 1D 87 C3 61 86 D6 12 13 13 33 33 33 15 19 1F D4 20 23 23 E3 E8 D1 A3 B4 3D 
79 F2 64 07 07 07 D5 C6 03 72 EB DE BD FB 9E 3D 7B E8 F7 D8 F0 F0 F0 01 03 06 70 38 1C BA 9C B8 
96 96 96 9D 9D 5D 70 70 30 21 84 C3 E1 AC 5B B7 4E 72 86 1F 68 C8 64 2C E0 21 84 94 97 97 33 6F 
C2 D0 B8 14 14 14 2C 5D BA EC EE BD 7B 84 90 D0 D0 30 E9 F9 74 7E 7E FE 8A 95 2B E9 A5 E0 C8 C8 
28 7F FF 35 32 0E 66 37 46 48 A6 41 B9 3C 3C 3C 76 ED DA 25 39 87 F4 86 0D 1B 06 0D 1A A4 AF AF 
DF B9 73 67 6F 6F EF 13 27 4E BC 7A F5 4A 28 14 D6 4F 3C 25 25 25 CC 58 B2 B9 B9 B9 94 C2 3E 29 
2C 2D 2D 99 36 8F C7 53 4C 64 50 33 B1 58 1C 1A 1A 4A 2B DD 6D 6D 6D A7 4E 9D AA A5 A5 A5 EA A0 
40 4E 2C 16 6B E0 C0 81 31 31 31 FE FE FE 92 D3 4D 4A 9A 3A 75 2A 97 CB 9D 3B 77 6E 9D AA B0 40 
85 F4 F5 F5 3B 75 EA 44 DB 37 6E DC 90 F2 C6 F8 FC F9 F3 2B 57 AE 30 9B EA 3D 60 A9 66 0C 0C 0C 
66 CD 9A A9 A7 A7 47 37 A5 E4 D3 F9 F9 F9 4B 97 2D 8B 8C 8C A2 9B 16 16 16 5F 7F 3D 4D 47 47 A7 
FE 62 AD 5F 48 A6 41 B9 D8 6C F6 D4 A9 53 23 23 23 99 B9 FA 19 C9 C9 C9 47 8E 1C F9 F2 CB 2F 2D 
2C 2C 8C 8D 8D A7 4F 9F 7E E3 C6 0D 65 2F D0 20 39 90 2C C7 B0 34 65 64 64 C4 B4 5F BF 7E FD B1 
31 41 6D 5E BD 7A 75 FA F4 69 DA F6 F4 F4 EC D2 A5 8B 6A E3 81 8F 54 56 56 16 15 15 75 FA F4 E9 
9A EA 65 E9 A4 69 6A 3C 8E A5 7E 74 74 74 1C 1D 1D 69 FB E2 C5 8B BF FE FA 6B B5 6F E6 6F DE BC 
F9 E9 A7 9F 92 92 92 98 3D 4A BA D1 1C 94 81 C5 62 B9 BA BA EE DC B1 5D 7A 3E 5D 35 93 DE B6 75 
4B CF 9E 3D EB 3B DC 7A 84 64 1A 94 8E C5 62 F5 EA D5 EB C2 85 0B 89 89 89 2B 56 AC A8 B6 4C B9 
A0 A0 E0 F0 E1 C3 83 06 0D 72 75 75 8D 8A 8A 92 65 EA 8F 06 A2 DE C6 D4 9B 2C B1 58 7C F1 E2 45 
BA 66 9E B9 B9 B9 A7 A7 27 46 2B 1B B5 DC DC DC 99 33 67 4E 9E 3C 39 31 31 B1 A6 63 92 93 93 E7 
CD 9B 37 65 CA 94 5A 57 1D 87 86 63 C8 90 21 CC 42 B3 CB 96 2D F3 F6 F6 8E 8D 8D A5 E5 D1 62 B1 
38 3F 3F FF C4 89 13 9E 9E 9E 74 6A 4B 68 A4 6A CD A7 9B 60 26 4D 90 4C 43 BD 69 D6 AC 59 B7 6E 
DD FC FD FD 93 92 92 B2 B2 B2 FE F8 E3 8F A5 4B 97 32 C5 C7 8C 3B 77 EE 8C 1B 37 6E CB 96 2D 8D 
65 0D 61 24 76 CA 96 9D 9D 1D 1E 1E 4E DB 63 C6 8C 91 5C DA 1D 1A 9D 92 92 92 5F 7E F9 E5 D8 B1 
63 74 93 96 73 94 96 96 D2 39 7C E8 72 E2 DE DE DE F4 46 8B B0 B0 B0 45 8B 16 29 69 BE 79 50 38 
73 73 73 5F 5F 5F DA 77 84 90 93 27 4F BA BA BA D2 82 F8 66 CD 9A B5 6C D9 F2 CB 2F BF BC 73 E7 
0E 21 64 DC B8 71 CC E2 B8 ED DA B5 53 59 C4 20 97 6A F3 E9 D5 AB FD 4B 4B 4B 9B 66 26 4D 90 4C 
43 FD 63 B1 58 26 26 26 EE EE EE EB D6 AD BB 7F FF 3E FD F8 94 1C B1 E6 F3 F9 4B 96 2C D9 B7 6F 
1F B3 5C A7 02 31 6F F4 1F 43 B2 C8 AF 7D FB F6 1F 7F 42 90 E2 C9 93 27 51 51 51 84 10 0E 87 33 
7A F4 68 54 4B 37 6A 51 51 51 4C 26 BD 61 C3 86 5F 7F FD B5 6F DF BE DA DA DA 74 8F B6 B6 76 DF 
BE 7D 0F 1E 3C B8 67 CF 1E FA 52 3D 73 E6 4C 68 68 A8 CA C2 85 BA 60 B1 58 13 27 4E 5C BE 7C B9 
F4 C3 7C 7D 7D 97 2D 5B C6 94 CF CA 77 E3 0A A8 56 D5 7C FA B7 D3 A7 FD 7E F8 C1 EF 87 05 4D 30 
93 26 4D 36 99 16 8B C5 7B F7 ED B3 E8 68 49 FF F3 1C 37 1E 83 1F AA 42 3F 3E FD FD FD 1F 3D 7A 
14 1A 1A CA A4 D4 41 41 41 CC 7A 5A 0A D4 BA 75 6B 26 9F 4E 49 49 91 2F 5F 4F 4B 4B 93 3C A1 62 
22 83 EA 94 97 97 FF F1 C7 1F B4 ED E2 E2 C2 2C E7 0E 8D 91 40 20 F8 E3 8F 3F 68 8D AC A7 A7 E7 
AC 59 B3 AA BD B0 D3 AC 59 B3 09 13 26 30 AB 23 5D B9 72 05 B3 B9 37 16 6C 36 7B C1 82 05 47 8E 
1C A9 F6 D6 52 0E 87 B3 7A F5 EA 4D 9B 36 31 F7 AB 70 38 1C 24 D3 8D 54 D5 7C 3A 22 22 92 59 C6 
A1 49 65 D2 A4 C9 26 D3 F1 09 09 41 41 FB 55 1D 05 FC 87 96 96 96 A7 A7 67 50 50 90 B9 B9 39 51 
DA FA 82 A6 A6 A6 4C 9D C0 D3 A7 4F 8B 8B 8B EB 7A 06 81 40 20 39 B9 9E B1 B1 B1 22 E3 83 FF CA 
CA CA A2 D5 D2 84 90 61 C3 86 49 DE FA 09 8D 8E E4 2C EF C3 87 0F 97 32 81 B4 96 96 16 73 CB F2 
A3 47 8F 50 39 DD 88 B0 D9 EC 69 D3 A6 25 25 25 ED DA B5 6B C8 90 21 74 F0 C2 DE DE DE DF DF FF 
F1 E3 C7 2B 56 AC D0 D5 D5 2D 2C 2C A4 2B 5C 76 EC D8 11 F3 88 37 5E 55 F3 69 AA A9 65 D2 A4 69 
26 D3 39 39 39 DB 03 B6 63 A8 43 D9 FC FD FD E9 DC B1 23 47 8E 94 7D E0 BF 6F DF BE EE EE EE B4 
9D 9A 9A FA FE FD 7B C5 46 D5 BA 75 6B 26 99 8E 8B 8B 93 63 BA D3 97 2F 5F 46 47 47 D3 B6 9D 9D 
1D 4D FD 41 49 1E 3D 7A 14 1F 1F 4F 08 31 35 35 ED D7 AF 1F 96 3C 6C D4 F8 7C 3E F3 56 C0 2C 23 
5A 93 76 ED DA D1 97 6A 4A 4A 0A 26 7C 68 74 5A B7 6E 3D 6F DE BC A8 A8 A8 E2 E2 62 B1 58 7C FF 
FE FD 15 2B 56 74 E8 D0 81 BE 84 D3 D2 D2 68 9F 9A 98 98 B4 6C D9 52 D5 C1 82 FC 58 2C 96 8D 8D 
8D D5 BF B3 22 52 DD BA 75 B5 B6 B6 56 55 48 2A D1 E4 92 69 81 40 B0 65 EB 56 3A E5 38 28 15 93 
65 BE 78 F1 42 F6 95 4D B4 B5 B5 CD CC CC 68 5B 24 12 29 BC 6C 5A 5B 5B DB CD CD 8D B6 B3 B2 B2 
4E 9F 3E 5D A7 3B 1D 85 42 61 58 58 18 33 AF 93 93 93 D3 A7 9F 7E AA D8 08 81 21 12 89 6E DD BA 
45 DB 76 76 76 58 56 BA 49 A1 77 AD A9 3A 0A 50 BC F2 F2 F2 7B FF 7E 04 5B 5A 5A EA EA EA AA 36 
1E F8 18 3C 1E 6F D1 E2 25 95 72 AA 4B 97 C2 65 59 1F 51 9D 34 AD B7 2A B1 58 1C 7E F9 F2 F9 F3 
98 97 A7 3E 58 5A 5A D2 0B 7C 29 29 29 51 51 51 32 A6 C5 65 65 65 CA 5E 5D D6 C9 C9 69 E8 D0 A1 
B4 BD 7F FF FE 73 E7 CE C9 9E B2 C7 C5 C5 1D 3C 78 90 B6 6D 6D 6D 87 0F 1F 8E B1 52 E5 29 2E 2E 
7E FC F8 31 6D BB B8 B8 A0 C6 A3 B1 6B DE BC 39 93 39 49 CE 34 5C AD D7 AF 5F 3F 7A F4 88 A0 AC 
56 ED BC 79 F3 86 5E 6E 22 84 F4 E8 D1 A3 79 F3 E6 AA 8D 07 E4 46 57 0B 67 EA A4 B5 B5 B5 99 BB 
20 6A 5D 1F 51 CD 34 AD 64 FA E1 C3 87 6B D7 AE C3 C4 C0 F5 C3 C6 C6 86 99 73 74 E7 CE 9D 4C 69 
84 74 89 89 89 CC 2C A4 6D DB B6 55 C6 FB AC 89 89 C9 C4 89 13 69 9B CF E7 2F 5B B6 EC CA 95 2B 
B2 E4 D3 09 09 09 F3 E7 CF 67 CA 37 3D 3D 3D AB 9D 33 1B 14 25 33 33 F3 C5 8B 17 B4 DD A3 47 0F 
7C 6F 69 EC F4 F5 F5 DB B4 69 43 DB B7 6E DD 2A 29 29 A9 E9 48 A1 50 78 E3 C6 0D DA EE DE BD BB 
A9 A9 69 3D 84 07 1F 29 20 20 80 96 F6 0D 1B 36 8C 59 68 B6 AA F8 F8 78 7A 23 84 AD AD 6D BF 7E 
FD EA 31 40 50 A4 4A 99 B4 85 85 45 C8 F1 63 BF 1E 3C 20 CB FA 88 EA A7 09 25 D3 3C 1E 6F E3 A6 
CD 28 95 AE 37 46 46 46 E3 C6 8D A3 ED 8C 8C 8C 69 D3 A6 1D 3F 7E 5C 4A 4D 85 58 2C BE 7B F7 EE 
F7 DF 7F 4F B3 55 53 53 53 37 37 37 65 E4 4F 2C 16 EB 8B 2F BE 98 30 61 02 13 DB FF FE F7 BF AD 
5B B7 4A F9 68 2F 2B 2B 3B 7C F8 F0 C8 91 23 E9 50 19 21 C4 C5 C5 65 E6 CC 99 98 64 5A A9 5E BD 
7A 95 92 92 42 08 E9 DE BD 7B 53 AB C0 53 4B 7A 7A 7A CE CE CE B4 7D EE DC B9 53 A7 4E 55 3B B4 
21 16 8B 4F 9F 3E BD 6B D7 2E BA D9 BB 77 6F 13 13 93 FA 8B 12 E4 D5 AD 5B 37 DA 88 8A 8A 0A 0E 
0E AE B6 73 9F 3C 79 C2 F4 EC B0 61 C3 3A FD B7 D6 16 1A 8B AA 99 F4 B6 AD 5B EC ED ED 65 59 1F 
51 2D 35 95 64 5A 28 12 1D 3D 1A CC 4C 0B 00 F5 80 C5 62 8D 1D 3B D6 D3 D3 93 6E 66 64 64 4C 99 
32 A5 4F 9F 3E 3B 76 EC 48 4A 4A A2 CB 62 11 42 2A 2A 2A F2 F3 F3 6F DC B8 F1 F5 D7 5F 0F 1E 3C 
38 2E 2E 8E EE 1F 3F 7E BC F2 96 E7 30 30 30 58 B5 6A 95 83 83 03 DD E4 F3 F9 8B 16 2D 72 72 72 
A2 B1 09 04 02 BA BF BC BC 3C 3D 3D 7D EF DE BD AE AE AE D3 A7 4F 67 96 3E 36 37 37 5F BB 76 6D 
87 0E 1D 94 14 1E 50 4F 9F 3E A5 8D 36 6D DA B4 6A D5 4A B5 C1 80 42 78 7A 7A D2 0B 56 7C 3E 7F 
C6 8C 19 9E 9E 9E 17 2F 5E CC CF CF A7 97 86 CA CB CB 9F 3C 79 B2 78 F1 62 1F 1F 1F 7A 83 9A A9 
A9 E9 F8 F1 E3 31 B9 78 A3 D0 AD 5B 37 A6 82 6E ED DA B5 4B 97 2E 4D 4B 4B A3 29 35 ED D9 D5 AB 
57 0F 18 30 80 59 CD 74 CA 94 29 E8 D9 C6 A8 DA 4C 9A CE DD 21 E3 7A E3 6A 4B AC EE CE 9D 0B ED 
64 65 DD C1 A2 23 FD 6F E8 30 37 A6 DD C1 A2 E3 58 CF 71 05 05 05 AA 8E 51 29 54 DE BF CF 9E 3D 
63 72 56 D9 39 38 38 3C 7B F6 4C C6 7F 62 F5 EA D5 F4 51 C3 87 0F CF CB CB 93 3D B6 27 4F 9E 30 
85 28 B2 33 37 37 FF FD F7 DF 2B 2A 2A E4 FA 7D 28 98 CA FB 57 79 04 02 81 AF AF 2F 7D 82 B3 67 
CF 66 16 C9 6B 52 D4 AF 7F 2B 2A 2A 42 42 42 64 5F 3B 69 C3 86 0D 1F 3E 7C 50 75 D4 CA A2 66 FD 
5B 51 51 B1 7F BF AC 73 CE 6E DF BE BD 81 BC 8B 2A 8F 9A F5 2F 95 93 93 33 65 EA 34 26 7D 1A 34 
78 C8 83 07 0F 2A 1D 53 51 51 71 F3 E6 4D BB 9E F6 CC 61 3F 2C 58 50 52 52 A2 92 80 95 47 B2 7F 
9B C4 C8 F4 8B 94 94 C0 DD BB 99 4B 4E AE AE AE 3F FC E0 A7 DA 90 9A 0E 5B 5B DB 3D 7B F6 D4 29 
67 75 73 73 3B 76 EC 58 AD 33 67 7D BC AE 5D BB 9E 3C 79 72 EA D4 A9 B2 3F C4 CD CD ED FC F9 F3 
9F 7F FE 39 EA 77 95 AD AC AC 8C C7 E3 D1 B6 99 99 19 B3 48 1E 34 6A 74 91 BC 75 EB D6 C9 92 4F 
CF 9F 3F 7F DE BC 79 28 A6 6A 2C 58 2C D6 E4 C9 93 99 EF C0 52 AC 5B B7 CE C7 C7 07 EF A2 8D 4E 
41 41 C1 8F 3F 2E AD 75 65 96 6A C7 A7 7F FE E5 17 E6 AA AF FA 51 FF 64 9A CF E7 6F DD BA 35 3D 
3D 9D 6E 9A 99 99 AD 58 BE CC 10 B3 C4 D7 A3 5E BD 7A 5D BD 7A 75 DB B6 6D B5 4E C9 6C 6E 6E BE 
6D DB B6 D0 D0 50 2B 2B AB FA 89 AD 5D BB 76 87 0F 1F 8E 8C 8C 74 75 75 95 7E 64 F7 EE DD 43 42 
42 CE 9F 3F DF A4 26 A2 57 21 A1 50 C8 CC 2E 8C 65 26 D5 09 9B CD F6 F5 F5 0D 0D 0D ED D3 A7 4F 
4D C7 98 9B 9B 1F 39 72 64 E3 C6 8D 98 37 AD 71 D1 D5 D5 DD B2 65 8B BF BF 7F 4D 5F 96 6C 6C 6C 
4E 9C 38 B1 68 D1 22 14 78 34 46 06 06 06 23 47 8E A4 7D 27 7D 65 96 4A F9 B4 9E 9E DE D8 B1 63 
D5 78 4C 44 CD BF F1 0B 45 A2 83 BF FE 1A 11 11 49 37 D9 6C F6 FC F9 DF 59 59 59 DD BE 7D 5B B5 
81 35 35 BA BA BA 7E 7E 7E 3E 3E 3E F7 EF DF BF 76 ED 1A 97 CB 4D 4D 4D A5 0B A6 70 38 9C 9E 3D 
7B DA DB DB 7B 7A 7A F6 E9 D3 A7 FE 3F 3B 9B 35 6B 36 74 E8 D0 C1 83 07 27 27 27 5F BD 7A F5 E6 
CD 9B 49 49 49 34 36 73 73 73 3B 3B BB 41 83 06 B9 B9 B9 59 5B 5B 63 84 AC 3E E5 E5 E5 65 67 67 
D3 36 B3 F8 30 A8 07 FA A2 73 71 71 89 89 89 39 79 F2 E4 A3 47 8F 1E 3C 78 40 08 B1 B1 B1 B1 B7 
B7 1F 33 66 CC 88 11 23 30 83 7B 23 A5 AD AD BD 7C F9 F2 AF BE FA EA F4 E9 D3 11 11 11 B7 6F DF 
E6 F3 F9 E6 E6 E6 0E 0E 0E 9E 9E 9E E8 D9 46 8D C5 62 79 7A 8E 25 84 04 05 05 6D DC B8 41 FA D0 
12 93 4F 2F 5B BE 62 E3 C6 0D 2E FF DE 7C AC 96 FE B9 C8 22 56 F4 D2 18 0D 44 5C 7C FC DC B9 F3 
98 19 3C 26 4F F6 FA F9 A7 9F 34 35 35 B9 5C EE 24 AF C9 CC 61 3D 7B F6 3C F4 EB 41 B5 5C D4 94 
5E 47 53 D7 FE 05 F4 AF 7A 43 FF AA 37 F4 AF 7A 53 D7 FE 15 8B C5 7C 3E 5F C6 2F 45 62 B1 B8 BC 
BC 5C 2D 2F 44 48 F6 AF 3A 97 79 A4 A5 A5 AD 5C F9 13 93 49 3B 38 38 CC FF EE 3B 4D 4D 4D D5 46 
05 00 00 00 D0 48 B1 58 2C D9 2F 2F B0 58 2C B5 CC A4 2B 51 DB 64 BA B4 B4 74 CF DE BD 4C A9 B4 
9E 9E DE B7 DF CE 43 E5 25 00 00 00 00 28 90 7A 26 D3 62 B1 F8 CC 99 B3 A1 A1 61 CC 9E D9 B3 67 
39 3B 39 A9 30 24 00 00 00 00 50 3F EA 99 4C C7 27 24 04 6C DF CE 6C 8E 1B E7 39 6D EA 54 CC C2 
03 00 00 00 00 8A A5 86 C9 34 8F C7 DB B5 2B 90 29 95 B6 B0 B0 98 3D 7B B6 8E 8E 8E 6A A3 02 00 
00 00 00 F5 A3 6E C9 74 79 79 F9 8E 9D 3B 99 65 C3 D9 6C F6 C2 05 3F 58 D7 D7 A4 C5 00 00 00 00 
D0 A4 A8 55 32 2D 16 8B 2F 5C BC 78 FA F4 19 66 8F AF EF 1C B7 E1 C3 55 18 12 00 00 00 00 A8 31 
B5 4A A6 53 52 52 76 EC D8 C9 2C 1B EE E0 E0 F0 E5 E4 C9 6C 0D 0D D5 46 05 00 00 00 00 EA 4A 7D 
92 E9 FC FC FC 55 AB 56 BF 79 F3 86 6E EA E9 E9 2D 59 BC 08 73 E1 01 00 00 00 80 F2 A8 49 32 2D 
14 89 82 8F 1D 8B 4F 48 A0 9B 6C 36 7B F9 F2 65 D2 17 BA 04 00 00 00 00 F8 48 6A 92 4C 47 5C BD 
BA 67 CF 5E 66 73 F4 E8 51 1E 23 46 60 2E 3C 00 00 00 00 50 2A 75 48 A6 5F A4 A4 6C D9 BA 8D 29 
95 EE DA B5 CB C2 05 0B 30 17 1E 00 00 00 00 28 5B A3 4F A6 4B 4B 4B 03 03 03 25 97 0D 5F BA 74 
A9 A9 A9 A9 6A A3 02 00 00 00 80 A6 A0 71 27 D3 42 91 E8 E0 C1 5F 2F 5D 0A 67 F6 4C 9B 36 D5 C1 
C1 41 85 21 01 00 00 00 40 D3 F1 4F 55 B1 58 2C 56 6D 1C F2 29 2C 2C 9C FE CD 8C 87 0F 1F 2A FC 
CC 63 46 8F 5E BF 7E 9D B6 B6 B6 C2 CF 5C CF 68 E1 78 23 ED 5F A8 15 FA 57 BD A1 7F D5 1B FA 57 
BD A1 7F D5 9B 64 FF 36 EE 91 69 00 00 00 00 00 15 42 32 0D 00 00 00 00 20 27 24 D3 00 00 00 00 
00 72 42 32 0D 4A 24 10 08 7C 7C 7C 58 32 73 72 72 F2 F2 F2 0A 0A 0A CA CC CC AC 6B 9D 99 58 2C 
CE CC CC 0C 0A 0A F2 F2 F2 EA D5 AB 17 3D A1 91 91 91 BB BB BB BF BF 7F 62 62 22 33 79 62 4D 92 
93 93 7B F6 EC 49 1F 18 17 17 F7 11 CF BB E9 BA 7D FB 76 9B 36 6D E8 EF B0 4D 9B 36 B7 6F DF 96 
F1 81 21 21 21 32 FE 85 78 7B 7B 9F 39 73 A6 B8 B8 58 8E F0 04 02 C1 8D 1B 37 96 2D 5B 36 78 F0 
60 23 23 23 7A CE 5E BD 7A D1 73 16 16 16 CA 71 4E 75 25 E3 8B D7 C8 C8 68 F0 E0 C1 73 E7 CE 3D 
75 EA 14 8F C7 53 D4 69 6B E2 E3 E3 23 10 08 24 4F 18 17 17 27 DF A9 DC DD DD F3 F3 F3 95 F6 FB 
6B F4 C4 62 71 76 76 F6 C5 8B 17 E7 CE 9D DB BF 7F FF 4F 3F FD 94 FE DE 3A 74 E8 E0 E1 E1 E1 EF 
EF 7F FB F6 ED F2 F2 F2 5A CF 23 D9 41 75 7A 5F 65 DE 13 7A F6 EC 99 9C 9C 5C E9 A7 92 7F 48 FE 
FE FE 75 7B 6E 50 BF F2 F3 F3 DD DD DD E5 FB 33 68 64 C4 4D CC AD 5B B7 3A 58 74 64 FE 1B EB 39 
AE A0 A0 40 D5 41 29 85 6A FB B7 B4 B4 74 F6 EC D9 F2 FD 4D 4E 9F 3E 3D 2B 2B 4B 96 7F 45 24 12 
5D BB 76 6D E4 C8 91 D2 4F E8 EA EA 1A 19 19 29 12 89 6A 3A CF F3 E7 CF ED EC EC E8 C1 B1 B1 B1 
8A FB 35 28 51 83 7A FD 0A 85 C2 95 2B 57 4A FE CE FD FD FD 2B 2A 2A 64 79 EC F1 E3 C7 EB F4 E7 
5D C4 31 EF 00 00 20 00 49 44 41 54 61 68 68 18 18 18 F8 FE FD 7B 19 63 E3 F1 78 6B D7 AE 35 37 
37 97 7E CE 65 CB 96 F1 78 BC 8F F8 1D 28 98 0A FB 57 8E 17 2F 87 C3 F1 F6 F6 4E 4F 4F 57 EC 69 
25 CD 9E 3D BB B4 B4 54 F2 84 B1 B1 B1 F2 9D 6A F8 F0 E1 79 79 79 CA FD 25 D6 86 46 A2 DA 18 AA 
12 89 44 31 31 31 9E 9E 9E B5 FE 0E 6D 6C 6C 02 03 03 DF BD 7B 27 E5 6C 92 1D 54 A7 F7 55 E6 3D 
C1 CE CE EE F9 F3 E7 95 7E 2A F9 87 B4 7A F5 6A 79 9E A7 F2 35 CC FE AD 7F 79 79 79 C3 87 0F 97 
EF CF A0 21 93 EC 5F 8C 4C 43 03 75 E8 D0 21 1F 1F 9F 9C 9C 1C E9 87 65 67 67 CF 9C 39 73 F0 E0 
C1 E1 E1 E1 D2 8F 8C 89 89 19 37 6E DC BA 75 EB 2A 8D 6C 81 A2 F0 78 BC 84 84 04 C9 3D 37 6F DE 
CC CE CE 56 C6 BF 55 50 50 30 6F DE BC 25 4B 96 94 94 94 48 3F B2 A2 A2 E2 EC D9 B3 AE AE AE CB 
97 2F CF C8 C8 90 7E CE 75 EB D6 79 7A 7A DE BF 7F 5F A1 C1 36 15 7C 3E FF F0 E1 C3 EE EE EE 57 
AE 5C 11 63 06 83 C6 89 BE A3 BA BA BA 86 85 85 D5 7A 70 72 72 F2 BC 79 F3 C6 8D 1B F7 FC F9 F3 
7A 88 0D A0 C1 42 32 0D 0D D7 85 0B 17 36 6F DE 5C 56 56 56 D3 01 C9 C9 C9 5F 7C F1 C5 A1 43 87 
64 3C 21 9F CF 5F B9 72 E5 A6 4D 9B 90 4F 2B 43 42 42 42 54 54 14 21 C4 CB CB CB DD DD 9D 10 12 
15 15 55 29 BD 56 AC 1D 3B 76 9C 38 71 42 4A DE 26 14 0A B7 6E DD 3A 7D FA F4 AA 97 89 6B 12 17 
17 E7 EB EB 7B EF DE 3D 05 C5 D8 E4 24 27 27 FB F8 F8 44 47 47 AB 3A 10 A8 B3 A7 4F 9F D6 E9 1D 
95 8A 88 88 F8 FA EB AF 93 92 92 94 14 15 40 C3 87 64 1A EA 49 D5 EB B3 95 94 95 95 65 66 66 06 
07 07 F7 E9 D3 87 79 D4 89 13 27 1E 3D 7A 54 ED 09 73 72 72 96 2C 59 22 59 7D D5 BD 7B F7 8D 1B 
37 26 26 26 F2 F9 7C 7A CE 0F 1F 3E 54 3D E7 D6 AD 5B C3 C2 C2 30 72 A6 58 65 65 65 37 6F DE A4 
ED 01 03 06 0C 1B 36 8C B6 2F 5D BA 54 EB E0 B1 24 29 17 DF 3F 7C F8 90 9B 9B 7B FD FA 75 2F 2F 
2F E6 F8 A3 47 8F D6 34 DE 2C 16 8B 4F 9F 3E ED EF EF CF E7 F3 E9 1E 0E 87 E3 E5 E5 15 1E 1E 9E 
9D 9D FD E1 C3 07 7A 5A 3E 9F CF E5 72 E7 CD 9B C7 E1 70 E8 61 5C 2E D7 DF DF BF D6 AB 22 4D 87 
94 17 6F 69 69 69 66 66 66 68 68 A8 64 9D 55 46 46 C6 92 25 4B 6A CD AE 6A 7D 4F A8 6A DF BE 7D 
52 A6 FF AF D3 E5 E3 2B 57 AE 18 19 19 29 EC 77 D4 F8 25 25 25 7D F3 CD 37 92 EF A8 86 86 86 73 
E7 CE BD 7A F5 AA E4 EB 85 BE 51 87 84 84 48 F6 38 97 CB 5D BE 7C 79 6E 6E AE 2A 02 07 50 3D 24 
D3 D0 50 68 6A 6A B6 6D DB 76 CA 94 29 97 2E 5D 1A 33 66 0C DD 99 95 95 45 3F 20 2B 1D 2C 10 08 
D6 AC 59 73 E1 C2 05 BA C9 E1 70 36 6F DE 9C 90 90 B0 78 F1 E2 6E DD BA B5 68 D1 82 EE 67 B3 D9 
F4 9C D7 AF 5F 5F BD 7A 35 CD 96 F8 7C FE A6 4D 9B 5E BC 78 51 5F CF AC 49 48 4D 4D 8D 8C 8C 24 
84 98 9A 9A F6 EE DD BB 5F BF 7E A6 A6 A6 84 90 AB 57 AF 3E 7D FA 54 21 FF 04 9B CD 6E D9 B2 E5 
C0 81 03 83 83 83 37 6C D8 40 77 C6 C5 C5 D5 74 3B 4B 7C 7C FC B2 65 CB 98 4C DA CD CD ED C6 8D 
1B 21 21 21 1E 1E 1E C6 C6 C6 6C 36 9B EE 6F D1 A2 45 DF BE 7D 77 EE DC 79 ED DA 35 17 17 17 BA 
F3 C2 85 0B 87 0E 1D 12 89 44 0A 89 5C 8D 69 6B 6B B7 6D DB D6 D3 D3 33 2C 2C 2C 24 24 84 A9 4A 
E7 72 B9 3B 76 EC C0 25 A0 C6 A2 A4 A4 24 20 20 80 CB E5 D2 4D 0E 87 B3 64 C9 92 27 4F 9E 04 06 
06 BA B9 B9 49 BE 5E E8 1B F5 E4 C9 93 2F 5C B8 10 11 11 C1 DC 67 12 16 16 76 FE FC F9 AA EF D5 
00 4D 01 92 69 68 70 8C 8D 8D 7F FE F9 67 2B 2B 2B BA 99 94 94 54 F5 23 39 26 26 E6 E8 D1 A3 B4 
6D 68 68 B8 7F FF FE 05 0B 16 E8 EA EA D6 74 4E 5D 5D DD A5 4B 97 2E 5F BE 9C 6E 3E 7A F4 28 24 
24 04 A9 92 02 C5 C6 C6 D2 91 48 3B 3B 3B 73 73 73 2B 2B 2B 47 47 47 42 48 56 56 56 44 44 84 62 
3F 62 D9 6C F6 D4 A9 53 87 0E 1D 4A 37 9F 3E 7D 5A B5 2B 8B 8B 8B F7 EF DF CF 0C 5A 4F 98 30 21 
38 38 98 4E F3 52 ED 39 59 2C 56 EF DE BD 0F 1C 38 E0 E0 E0 40 F7 1C 3B 76 0C 95 A0 B2 63 B3 D9 
5E 5E 5E EB D6 AD 63 06 F8 4F 9C 38 11 1F 1F AF DA A8 40 46 E7 CF 9F 3F 70 E0 00 6D 73 38 9C 3D 
7B F6 AC 5B B7 8E 7E 1F AE 49 B3 66 CD 86 0D 1B 76 F2 E4 49 E6 25 73 FA F4 69 25 DD 23 01 D0 C0 
21 99 86 86 A8 7D FB F6 1D 3B 76 A4 ED CC CC CC 4A C9 74 49 49 C9 C9 93 27 99 11 C7 1F 7F FC 71 
C2 84 09 35 25 49 0C 36 9B ED ED ED 3D 7A F4 68 BA F9 E7 9F 7F FE F5 D7 5F 8A 0E BC 89 2A 2C 2C 
BC 7A F5 2A 6D F7 E9 D3 C7 C0 C0 C0 C0 C0 C0 D5 D5 95 EE 51 C6 6D 88 FA FA FA 96 96 96 B4 5D 50 
50 50 75 8A AE 3B 77 EE 30 77 50 39 38 38 AC 5D BB D6 D8 D8 B8 D6 D3 DA DA DA 7E FB ED B7 B4 9D 
94 94 14 11 11 A1 B8 90 D5 1F 8B C5 9A 38 71 22 F3 95 95 CF E7 5F BC 78 51 CA 3D 0F D0 40 14 16 
16 9E 3B 77 8E D9 5C BE 7C F9 A4 49 93 9A 35 93 29 3D B0 B5 B5 5D BC 78 31 6D 73 B9 DC 67 CF 9E 
29 25 44 50 17 A6 A6 A6 CD 9B 37 57 75 14 8A 87 64 1A 1A 9F E7 CF 9F 33 A9 DB E8 D1 A3 A7 4D 9B 
A6 A1 A1 21 CB 03 5B B7 6E 3D 6D DA 34 42 08 87 C3 D1 D6 D6 C6 20 8A A2 A4 A4 A4 DC BA 75 8B 10 
C2 E1 70 06 0C 18 40 BB 63 C8 90 21 F4 F2 82 B2 6F 43 D4 D1 D1 A9 F4 07 50 5E 5E 7E F9 F2 65 E6 
EB D6 B7 DF 7E CB 5C E8 A8 D5 88 11 23 E8 A4 60 36 36 36 F9 F9 F9 28 54 A8 13 36 9B 3D 71 E2 44 
66 A8 F2 EE DD BB 78 95 35 7C F7 EF DF A7 B7 0E 13 42 26 4C 98 30 6B D6 2C A6 A8 43 16 83 06 0D 
A2 2F 19 43 43 43 E9 13 E6 40 63 14 11 11 C1 CC 32 3E 6E DC B8 9A 2A E3 73 72 72 C6 8E 1D 4B 0F 
EB D2 A5 CB E3 C7 8F 99 1F 35 6B D6 8C F9 8B 6A DD BA 35 53 87 A9 4E 90 4C 43 43 F4 F4 E9 53 E6 
A5 D8 AE 5D BB 4A B7 1C DD BD 7B 37 2B 2B 8B B6 07 0E 1C D8 BA 75 6B D9 CF 3C 6C D8 B0 17 2F 5E 
E4 E5 E5 45 45 45 31 1F F9 F0 31 44 22 51 78 78 38 ED 91 A1 43 87 F6 EA D5 8B EE B7 B4 B4 64 4A 
90 EB 7A 1B 62 AD DE BE 7D 9B 96 96 46 DB 36 36 36 9A 9A 9A 92 3F CD CB CB 7B F0 E0 01 6D 3B 3B 
3B F7 EB D7 4F F6 33 1B 18 18 6C DC B8 31 2F 2F 2F 29 29 69 CD 9A 35 52 6E 77 83 6A B5 6F DF DE 
CD CD 8D B6 E3 E3 E3 91 5D 35 70 22 91 E8 CF 3F FF 64 BE 79 4E 9A 34 C9 C0 C0 A0 4E 67 30 30 30 
F8 EE BB EF 9E 3E 7D 9A 9A 9A 3A 7D FA 74 25 C4 08 AA 34 78 F0 60 E6 E2 43 58 58 58 B5 13 28 09 
85 C2 23 47 8E 30 77 31 2D 5B B6 AC 7B F7 EE CC 4F 9B 37 6F DE B6 6D DB FA 89 56 55 90 4C 43 83 
93 91 91 B1 69 D3 26 26 5D B6 B5 B5 95 4C 68 DE BF 7F CF E4 D9 A6 A6 A6 FD FB F7 AF D3 C9 39 1C 
8E 95 95 55 A5 DC 0B 3E 46 4E 4E 4E 4C 4C 0C 6D F7 EB D7 4F 5F 5F 9F B6 75 75 75 99 B2 66 05 DE 
86 48 08 11 0A 85 C1 C1 C1 74 2C CD D6 D6 B6 6A AE FC FA F5 6B 66 6E 3B 07 07 07 E9 A5 9F 55 59 
59 59 D1 F5 11 15 12 6D 53 A3 A1 A1 D1 BB 77 6F 66 13 33 A6 35 70 05 05 05 77 EE DC A1 ED 81 03 
07 D2 5B 1D EA 6A E0 C0 81 5D BA 74 A9 D3 78 36 34 16 6C 36 7B E6 CC 99 CC AC 00 01 01 01 55 67 
0E 8D 8E 8E DE B1 63 07 6D FB FA FA 7A 7A 7A D6 F4 FE D9 AA 55 2B 43 43 43 E5 45 AB 2A 4D F4 4F 
DF C1 C1 21 FD 65 9A AA A3 80 FF 27 16 8B 8B 8B 8B 33 33 33 C3 C2 C2 7E FD F5 57 66 34 CB D6 D6 
76 E8 D0 A1 92 2F CB 92 92 12 C9 21 C9 BA E6 49 A0 70 B7 6E DD BA 71 E3 06 21 C4 CA CA AA 52 67 
39 3B 3B 3B 38 38 70 B9 DC AC AC AC F0 F0 F0 CF 3E FB 4C C6 82 9C 6A 55 54 54 14 16 16 26 26 26 
EE DF BF FF E4 C9 93 74 A7 A7 A7 A7 8D 8D 4D A5 23 D3 D2 D2 98 91 B6 AA E3 D6 A0 6C 1D 3A 74 B0 
B2 B2 4A 49 49 21 E4 FF D8 BB FB B8 18 B3 FF 7F E0 D7 A8 87 41 3B ED 2A 77 AD B5 13 36 C9 6E 42 
FA 54 D2 2A DB 8D 5D 3E 6C 16 4B BB 92 DB 6C 52 B2 EB AE 95 B5 4A C8 12 45 EE 45 A9 7C B0 DA 6C 
F6 E3 6E B7 6C 85 91 24 A1 52 9B 46 48 29 61 BA A5 9A DF 1F E7 F3 3B 8F F9 4E 35 4D 57 33 4D 33 
5E CF 7F 9C 99 B9 E6 9A 93 33 D7 75 BD E7 5C EF 73 0E 43 D6 31 C5 2F 93 4E AB B8 B8 98 9E 6F 47 
8E 1C D9 AB 57 2F E5 7D 56 9B EE 11 41 E7 D1 B7 6F 5F 5F 5F DF 5B B7 6E 09 85 42 D2 DB B5 6F DF 
3E 7A 07 E3 F1 E3 C7 81 81 81 A4 FF CB D2 D2 D2 CB CB 4B 6A 32 00 2D 2D AD 1E 3D 7A D0 B2 9C E9 
F8 EA 45 03 FF 24 E8 9C F6 ED DB D7 A3 47 0F 4E 0B BA 74 E9 F2 DE 7B EF 99 9A 9A AE 5B B7 4E F2 
BE F0 DC B9 73 3F FE F8 63 C9 FD 54 56 56 D2 38 E9 A3 8F 3E A2 FD A0 A0 12 35 35 35 74 94 9E 8D 
8D 0D 1D 14 48 F4 EF DF 7F CC 98 31 A4 7C F5 EA D5 D2 D2 D2 56 77 78 FE FC F9 5E BD 7A 35 FB 25 
D1 D2 D2 EA D5 AB 97 BD BD 3D 8D A4 A7 4F 9F EE ED ED DD B4 3F 4C F2 83 4C 4C 4C 58 FF 75 C0 0E 
97 CB A5 D7 CE A7 4F 9F D6 D6 D6 36 BB 99 EC 73 42 53 8B 17 2F 96 9D C2 3E 76 EC 58 85 EC E7 AD 
F2 E2 C5 0B F2 B3 87 C1 2F 4F 68 D9 D8 B1 63 97 2C 59 42 CA 27 4F 9E 3C 75 EA 14 49 F6 A8 AB AB 
0B 09 09 49 4C 4C 64 18 86 C7 E3 2D 5B B6 AC E9 29 B7 6B D7 AE 6D CD 1D 52 3B 08 A6 A1 F3 F2 F1 
F1 F1 F4 F4 94 EA CB AC AD AD A5 D9 B7 5A 5A 5A E8 F1 52 AD 82 82 02 BA D6 DD D8 B1 63 A5 3A 24 
BA 76 ED FA F9 E7 9F 93 B2 62 87 21 F2 78 3C 3F 3F BF 43 87 0E 35 3B 47 47 65 65 25 2D B7 A7 2F 
1C D8 E1 F1 78 1A 7F ED D4 18 45 45 45 B4 AC 91 23 C3 40 21 B4 B4 B4 DC DD DD C9 48 53 86 61 42 
42 42 B2 B2 B2 18 86 89 8B 8B DB BF 7F 3F 79 72 D1 A2 45 74 83 96 18 1A 1A D2 5F DA 9A 04 C1 34 
74 46 C6 C6 C6 D1 D1 D1 5B B6 6C 91 31 75 34 74 06 74 7A 69 4B 4B CB F1 E3 C7 37 DD E0 93 4F 3E 
A1 99 D3 0A 1C 86 28 12 89 6E DF BE 7D E3 C6 8D C6 C6 46 85 EC 10 14 88 CB E5 72 B9 5C 55 D7 02 
14 AC BC BC 7C C2 84 09 B2 7B FD 47 8C 18 91 9B 9B AB EA 9A 82 52 F4 EE DD DB CF CF 8F 2C CC 94 
9D 9D BD 6B D7 AE B4 B4 B4 1D 3B 76 90 7B C5 F6 F6 F6 BE BE BE 2D 1D F8 6D 9A 27 40 1D 21 98 86 
4E 64 E4 C8 91 DE DE DE 89 89 89 19 19 19 AE AE AE B8 1E 77 72 92 D3 4B 5B 5A 5A BE FF FE FB 4D 
B7 E9 D7 AF DF B8 71 E3 48 59 B1 C3 10 13 12 12 C6 8F 1F BF 6C D9 32 9A F6 03 9D 44 45 45 45 59 
59 99 AA 6B 01 9D 4E 9B D6 7B 3F 76 EC 98 AA EB 0B D2 CC CD CD E9 44 F2 C7 8F 1F 9F 39 73 26 59 
35 D3 C0 C0 60 ED DA B5 FD FB F7 6F E9 8D F4 A6 87 A6 DE 4F 46 30 0D 1D C4 C3 C3 A3 BA BA 5A F2 
5C D9 D0 D0 F0 CF 3F FF FC F0 C3 0F 64 C9 34 1E 8F E7 E4 E4 B4 76 ED 5A 3B 3B 3B 19 F3 91 E9 E9 
E9 F5 EE DD 9B 94 AB AB AB EB EB EB 3B E8 0F 80 26 EE DD BB 47 A7 A7 0D 0D 0D ED D6 AD 5B D3 9E 
AA 2E 5D BA F8 FB FB 93 6D C8 30 44 D9 0B 4F 3A 3B 3B 97 95 95 B5 74 7D 15 89 44 05 05 05 47 8E 
1C B1 B0 B0 20 DB 87 85 85 F9 F9 F9 49 A5 C0 D2 45 AD 19 86 A9 AE AE 56 E4 DF 0C 72 68 68 68 A0 
07 A6 8C 6B 67 D3 73 82 6C 7B F7 EE 95 3D 53 A1 9C B1 5A AB FB 79 AB 48 76 19 4A E6 47 01 34 C5 
E1 70 5C 5D 5D 17 2E 5C C8 30 0C 39 1B 93 E7 7D 7C 7C E4 9C 59 AB 5F BF 7E 58 B4 05 40 91 BA 74 
E9 32 68 D0 A0 E0 E0 E0 23 47 8E F0 F9 7C 91 48 B4 65 CB 16 47 47 47 D9 99 B5 DD BA 75 A3 33 78 
14 15 15 A1 57 52 55 1A 1A 1A CE 9F 3F DF D6 FF FF E4 E4 E4 92 92 12 D6 1F FA CE 3B EF 0C 1C 38 
70 CE 9C 39 7F FE F9 E7 77 DF 7D 47 9E 3C 7A F4 A8 D4 52 85 92 73 BC D0 D3 3D 74 98 8A 8A 0A FA 
DF AE A9 D7 4E 8D A1 A7 A7 47 8F 17 A1 50 28 FB B7 2E 80 8E 8E 8E AF AF AF E4 2A 0D 53 A6 4C 71 
77 77 97 3D 31 E2 80 01 03 94 5F 35 55 42 30 0D 2A C6 E1 70 5C 5C 5C 82 82 82 48 FF 74 66 66 E6 
77 DF 7D 27 23 9E EE D1 A3 07 9D FE 3D 37 37 97 4E 47 2D BF 9B 37 6F A6 A6 A6 BE 7C F9 92 75 9D 
81 F9 BF D3 4B CB 2F 29 29 89 AC 95 D8 4E 3C 1E CF C7 C7 C7 CC CC 8C 61 18 91 48 F4 DF FF FE 57 
B2 73 BA 6F DF BE 74 C9 C3 DC DC DC A6 8B 8D CB 56 59 59 99 90 90 50 58 58 88 FB 1E EC 48 4E 4D 
28 79 97 00 3A 21 03 03 03 3A B9 64 46 46 46 45 45 45 4B 5B EA EB EB 9F 3B 77 0E 29 19 A0 AF AF 
2F 39 F2 BB 7F FF FE AD 0E 5D A5 03 C1 35 75 90 2B 82 69 50 3D 0E 87 33 63 C6 0C 9A 89 95 99 99 
E9 EB EB 4B 67 6B 92 A2 A5 A5 45 97 15 28 2E 2E BE 7C F9 B2 B8 C9 6A 4C 32 34 34 34 9C 3A 75 8A 
AC 2D E2 E2 E2 D2 D2 CA A8 D0 2A 3A BD 74 5B 29 6A 18 E2 80 01 03 68 B2 47 6E 6E AE 64 10 C0 E7 
F3 49 9C CD 30 CC 95 2B 57 1E 3F 7E DC A6 3D 17 14 14 2C 5F BE 7C E0 C0 81 7D FB F6 8D 89 89 69 
7F 55 DF 2A 75 75 75 D7 AF 5F 27 65 1E 8F 37 64 C8 10 D5 D6 07 64 D3 D7 D7 1F 3E 7C 38 29 A7 A6 
A6 66 66 66 AA B6 3E D0 C9 D5 D7 D7 47 44 44 9C 39 73 86 3E 13 1E 1E 1E 17 17 27 E7 85 58 53 47 
22 22 98 86 4E 41 5B 5B 7B DE BC 79 74 56 1D 81 40 B0 63 C7 8E 96 42 2E 63 63 63 1A 2A 25 24 24 
3C 79 F2 44 FE 0F CA CF CF FF E3 8F 3F 48 79 E0 C0 81 EF BE FB 6E 3B 6A FD F6 92 9C 5E DA C1 C1 
E1 C9 93 27 B2 B3 54 6B 6B 6B BD BD BD C9 F6 8A 1A 86 48 66 9E 26 E5 8A 8A 0A C9 84 13 5D 5D 5D 
FA 0D 11 08 04 97 2E 5D 92 FF 17 57 43 43 C3 D9 B3 67 C9 6F 39 2E 97 DB 74 45 18 90 2D 3F 3F FF 
E2 C5 8B A4 6C 69 69 89 9E E9 4E 8E CB E5 D2 21 C2 22 91 E8 3F FF F9 8F A2 A6 DC 01 8D 94 9A 9A 
BA 67 CF 1E A9 27 7F F9 E5 97 9C 9C 1C 19 EF EA D5 AB 17 3D 27 6B 24 04 D3 D0 59 48 4E BB C3 30 
4C 54 54 54 7C 7C 7C B3 31 90 A1 A1 21 3D FB 27 26 26 1E 3B 76 4C CE DB F1 64 19 6A DA F5 62 67 
67 87 15 0A D8 91 9C 5E DA DA DA BA D5 CE 06 2E 97 3B 69 D2 24 52 96 67 18 A2 3C C4 62 71 4B 3B 
E1 70 38 4E 4E 4E 34 13 F4 D0 A1 43 B2 4F F4 92 EE DE BD 1B 15 15 45 CA 36 36 36 1F 7D F4 51 3B 
EB F9 56 A9 AF AF 8F 8B 8B A3 4B 88 CB F3 DD 00 95 B3 B6 B6 A6 F3 57 1E 3F 7E BC A5 13 2F C0 D3 
A7 4F B7 6E DD 4A 16 56 B3 B4 B4 3C 73 E6 0C 49 9E CE CC CC DC BC 79 F3 AB 57 AF 5A DD 83 A6 9E 
10 10 4C 43 27 62 6E 6E EE EB EB 4B CA 22 91 28 34 34 34 3F 3F BF E9 66 5C 2E F7 AB AF BE A2 A1 
D2 C6 8D 1B 4F 9C 38 D1 EA D9 5F 2C 16 9F 38 71 22 2C 2C 8C 3C 74 71 71 B1 B5 B5 55 5C DD DF 2E 
17 2E 5C 20 01 13 8F C7 73 76 76 96 67 61 14 C9 09 A7 DB 39 0C 91 C8 CF CF 4F 4D 4D 25 E5 DE BD 
7B EB E9 E9 49 BE 6A 6A 6A 3A 79 F2 64 52 16 08 04 6B D6 AC 91 E7 13 4B 4A 4A D6 AD 5B 47 63 C1 
59 B3 66 E1 DE 85 FC C4 62 71 52 52 52 78 78 38 79 C8 E7 F3 27 4F 9E 8C 45 73 3A 3F 03 03 03 77 
77 77 52 16 89 44 8B 17 2F 3E 7C F8 B0 FC 03 06 1A 1B 1B 65 64 5A 83 C6 A8 AF AF 0F 0B 0B 3B 7B 
F6 2C C3 30 3C 1E 6F CD 9A 35 93 26 4D F2 F6 F6 26 E3 9D 22 23 23 23 22 22 5A BA 10 1B 1B 1B DF 
BA 75 4B 2C 16 3B 3A 3A 76 68 A5 3B 0A 82 69 E8 44 38 1C 8E 9B 9B DB F4 E9 D3 C9 43 81 40 B0 6F 
DF BE BA BA BA A6 5B 5A 5A 5A BA BA BA 92 32 39 FB 07 06 06 CA F8 59 5C 55 55 B5 6D DB B6 C5 8B 
17 93 64 00 1E 8F 37 67 CE 1C 2C D2 C6 4E 45 45 05 1D 7A E8 E0 E0 30 6C D8 30 79 DE 25 39 E1 74 
FB 87 21 4A 45 BD A6 A6 A6 52 51 6F F7 EE DD 17 2C 58 40 6F 74 C4 C7 C7 7F F5 D5 57 02 81 A0 A5 
45 5E C4 62 F1 CD 9B 37 DD DC DC E2 E3 E3 C9 33 D3 A7 4F B7 B7 B7 6F 4F 25 DF 2A 75 75 75 D1 D1 
D1 0B 16 2C A0 63 82 A7 4D 9B 66 6A 6A AA DA 5A 81 9C BE FC F2 4B 32 DF 19 C3 30 22 91 68 C1 82 
05 F3 E7 CF 2F 28 28 90 DD 49 51 5F 5F 9F 9C 9C 3C 6D DA B4 A5 4B 97 76 48 35 41 95 CE 9E 3D 4B 
7B A3 96 2E 5D 3A 71 E2 44 0E 87 33 65 CA 94 D9 B3 67 93 27 43 42 42 AE 5C B9 A2 BA 0A AA 12 82 
69 E8 5C 7A F6 EC E9 E3 E3 43 63 A0 FD FB F7 9F 3B 77 AE E9 66 5C 2E D7 C3 C3 83 CE CE 23 12 89 
D6 AD 5B 37 7C F8 F0 80 80 80 F4 F4 74 3A 5B EA EB D7 AF 1F 3C 78 B0 73 E7 4E 6B 6B EB 15 2B 56 
D0 B4 DA 39 73 E6 38 39 39 29 FF AF D1 4C 92 D3 4B 93 A1 9C F2 BC 4B 2A F5 82 DD 30 C4 FA FA FA 
47 8F 1E 1D 3A 74 C8 D1 D1 91 46 BD 06 06 06 5F 7E F9 65 D3 8C 9D 91 23 47 2E 59 B2 84 3E 4C 4D 
4D B5 B2 B2 9A 32 65 4A 5C 5C DC A3 47 8F 48 C7 9B 58 2C AE A8 A8 48 4A 4A 72 77 77 B7 B3 B3 A3 
89 E0 7C 3E DF C7 C7 07 3F B7 5A 55 59 59 F9 E0 C1 83 A3 47 8F 3A 3A 3A CE 9E 3D 9B DC FF 65 18 
C6 D2 D2 D2 C3 C3 03 EB 2E A9 0B 1D 1D 9D 15 2B 56 48 9E 15 23 23 23 47 8C 18 31 75 EA D4 98 98 
98 47 8F 1E D1 D9 72 EA EB EB CB CA CA 52 53 53 FD FD FD 3F F9 E4 93 4F 3F FD 34 2E 2E 8E BE AB 
57 AF 5E 1A B9 58 34 E4 E5 E5 6D DA B4 89 2E 76 E8 E9 E9 49 E6 C2 D3 D1 D1 F1 F2 F2 22 F9 D0 42 
A1 70 DB B6 6D 6F F5 B0 7E 79 26 BA 07 75 A4 DA F6 AD AE AE F6 F0 F0 20 75 90 7F 81 86 37 6F DE 
04 04 04 D0 2F A7 BD BD FD A3 47 8F 9A DD F2 CA 95 2B 2C C6 34 CC 9E 3D BB B4 B4 B4 E9 DE 72 72 
72 58 EC AD AD 0B 4F 28 56 C7 B7 6F 7D 7D 3D 5D 84 C5 C0 C0 E0 C6 8D 1B F2 BF F7 C5 8B 17 D3 A6 
4D A3 EF 15 08 04 F4 A5 F6 4C AD F5 FD F7 DF D7 D6 D6 36 FB 89 95 95 95 7E 7E 7E 6D DD 21 9F CF 
FF F5 D7 5F 1B 1B 1B DB FB 9F D5 6E 1D DF BE 94 E4 C1 CB E2 3F 30 29 29 49 E1 BB 25 8E 1D 3B 26 
B9 C3 94 94 14 FA 52 9B 16 D8 EB 0C 54 D8 BE CD 2A 2C 2C 9C 38 71 22 BB 76 E1 F1 78 AB 56 AD 2A 
2F 2F 97 DA 27 EB 06 A2 E7 04 33 33 B3 9C 9C 1C A9 57 25 BF 48 1B 36 6C 68 EF 5F AE 1C 9D AD 7D 
59 AB AC AC F4 F4 F4 24 7F 8E 81 81 C1 9F 7F FE 29 F9 6A 63 63 23 1D 67 C2 30 CC E6 CD 9B DF BC 
79 23 B9 41 59 59 99 B3 B3 B3 FA 1E A7 2D 91 6C 5F F4 4C 43 A7 A3 AD AD BD 60 C1 02 7A 4E 4F 4C 
4C 8C 88 88 68 36 81 CF DA DA FA F8 F1 E3 6D EA 63 F6 F4 F4 DC B1 63 07 5D 43 11 DA EA D1 A3 47 
7F FE F9 27 29 3B 38 38 B4 69 E2 B3 77 DF 7D 77 C2 84 09 A4 AC A8 61 88 D3 A7 4F 5F B1 62 45 4B 
3D A0 3A 3A 3A EB D6 AD 0B 0D 0D 25 59 7D F2 30 36 36 DE BB 77 AF 8B 8B 8B 46 AE 79 DB 01 CC CC 
CC 62 63 63 69 4A 0F A8 11 3E 9F 1F 1B 1B EB E7 E7 27 FF F1 42 38 3B 3B C7 C7 C7 07 05 05 49 0D 
5D 00 0D 20 16 8B E3 E3 E3 69 B8 DC 74 B1 43 B2 58 04 4D 13 DA B3 67 0F 1D CD F2 F6 40 30 0D 9D 
51 BF 7E FD E8 B0 06 86 61 0E 1E 3C 28 10 08 9A DD 72 E8 D0 A1 A7 4F 9F DE B5 6B 57 AB 53 98 59 
58 58 5C BC 78 31 2C 2C 0C A7 FB F6 48 4F 4F A7 59 71 E3 C6 8D 6B EB 45 D7 CA CA CA C4 C4 84 94 
FF FC F3 CF 47 8F 1E B1 AE 89 9E 9E DE F6 ED DB 23 22 22 24 97 0F 68 8A CB E5 7A 79 79 25 27 27 
CF 9A 35 4B F6 0E 49 D7 5A 72 72 F2 84 09 13 10 49 B3 A0 A7 A7 E7 E7 E7 77 F1 E2 45 6B 6B 6B 55 
D7 05 58 E2 F1 78 81 81 81 B7 6E DD F2 F1 F1 91 E7 54 39 69 D2 A4 4B 97 2E 25 24 24 D8 DB DB 77 
E9 82 88 42 03 E5 E4 E4 04 07 07 93 04 8F 96 16 3B 24 C9 1E E4 DC 2E 14 0A B7 6E DD FA F4 E9 53 
15 D4 55 75 64 2D FF 08 A0 42 E3 C6 8D 5B B4 68 D1 B6 6D DB 98 FF 9F 89 35 64 C8 90 66 7B 94 75 
74 74 96 2C 59 B2 70 E1 C2 5B B7 6E 9D 3F 7F FE DA B5 6B 77 EF DE 25 B9 9B 7A 7A 7A 16 16 16 36 
36 36 13 26 4C 18 39 72 A4 EC F5 4E A1 55 55 55 55 BF FF FE 3B 29 9B 98 98 D0 D5 73 E4 F7 D1 47 
1F 39 3A 3A 92 81 83 57 AE 5C 49 4F 4F 6F D3 3C C4 7C 3E DF C8 C8 C8 C2 C2 C2 C9 C9 C9 C2 C2 42 
47 47 47 9E 77 71 38 1C 33 33 B3 E8 E8 E8 ED DB B7 27 25 25 9D 3F 7F 3E 27 27 87 8E 80 1C 39 72 
A4 99 99 99 B3 B3 F3 F8 F1 E3 35 75 DA 26 E5 E1 F3 F9 1F 7F FC B1 85 85 85 9D 9D 9D FC 2D 02 9D 
19 87 C3 19 34 68 D0 8E 1D 3B 36 6E DC 98 96 96 96 94 94 94 96 96 26 79 52 35 33 33 1B 3D 7A F4 
B8 71 E3 C6 8C 19 83 71 05 9A ED D5 AB 57 9B 37 6F 26 F3 C9 F2 F9 7C 5F 5F DF 96 3A 2F 4C 4D 4D 
7D 7D 7D 17 2D 5A C4 30 CC D9 B3 67 0F 1E 3C B8 7A F5 EA B7 E7 9A FB BF DE 17 31 26 95 D4 50 A4 
83 0D ED AB A9 D0 BE 9A 0D ED AB D9 D0 BE 9A 0D ED AB D9 24 DB 17 37 65 00 00 00 00 00 58 42 30 
0D 00 00 00 00 C0 12 82 69 00 00 00 00 00 96 10 4C 03 00 00 00 00 B0 84 60 1A 00 00 00 00 80 25 
04 D3 00 00 00 00 00 2C 21 98 06 00 00 00 00 60 09 C1 34 00 00 00 00 00 4B 08 A6 01 00 00 00 00 
58 42 30 0D 00 00 00 00 C0 12 82 69 00 00 00 00 00 96 10 4C 03 00 00 00 00 B0 84 60 1A 00 00 00 
00 80 25 04 D3 00 00 00 00 00 2C 21 98 06 00 00 00 00 60 09 C1 34 00 00 00 00 00 4B 08 A6 01 00 
00 00 00 58 42 30 0D 00 00 00 00 C0 12 82 69 00 00 00 00 00 96 10 4C 03 00 00 00 00 B0 84 60 1A 
00 00 00 00 80 25 04 D3 00 00 00 00 00 2C 21 98 06 00 00 00 00 60 09 C1 34 00 00 00 00 00 4B 08 
A6 01 00 00 00 00 58 42 30 0D 00 00 00 00 C0 12 82 69 00 00 00 00 00 96 10 4C 03 00 00 00 00 B0 
84 60 1A 00 00 00 00 80 25 04 D3 00 00 00 00 00 2C 21 98 06 00 00 00 00 60 09 C1 34 00 00 00 00 
00 4B 08 A6 01 00 00 00 00 58 42 30 0D 00 00 00 00 C0 12 82 69 00 00 00 00 00 96 10 4C 03 00 00 
00 00 B0 84 60 1A 00 00 00 00 80 25 04 D3 00 00 00 00 00 2C 21 98 06 00 00 00 00 60 09 C1 34 00 
00 00 00 00 4B 08 A6 01 00 00 00 00 58 E2 A8 BA 02 00 00 00 00 00 EA 47 2C 16 33 E8 99 06 00 00 
00 00 60 4D 9B FC 43 22 6B D0 3C 1C 0E 87 41 FB 6A 2E B4 AF 66 43 FB 6A 36 B4 AF 66 43 FB 6A 36 
D2 BE 04 7A A6 01 00 00 00 00 58 42 30 0D 00 00 00 00 C0 12 82 69 00 00 00 00 00 96 10 4C 03 00 
00 00 00 B0 84 60 1A 00 00 00 00 80 25 04 D3 00 00 00 00 00 2C 21 98 06 00 00 00 00 60 09 C1 34 
00 00 00 00 00 4B 08 A6 01 00 00 00 00 58 42 30 0D 00 00 00 00 C0 12 82 69 00 00 00 00 00 96 10 
4C 03 00 00 00 00 B0 84 60 1A 00 00 00 00 80 25 04 D3 00 00 00 00 00 2C 21 98 06 00 00 00 00 60 
09 C1 34 00 00 00 00 00 4B 08 A6 01 00 00 00 00 58 42 30 0D 00 00 00 00 C0 12 82 69 00 00 00 00 
00 96 10 4C 03 00 00 00 00 B0 84 60 1A 00 00 00 00 80 25 04 D3 00 00 00 00 00 2C 21 98 06 00 00 
00 00 60 09 C1 34 00 00 00 00 00 4B 08 A6 01 00 00 00 00 58 42 30 0D 00 00 00 00 C0 12 82 69 00 
00 00 00 00 96 10 4C 03 00 00 00 00 B0 84 60 1A 00 00 00 00 80 25 04 D3 00 00 00 00 00 2C 21 98 
06 00 00 00 00 60 09 C1 34 00 00 00 00 00 4B 08 A6 01 00 00 00 00 58 42 30 0D 00 00 00 00 C0 12 
82 69 00 00 00 00 00 96 10 4C 03 00 00 00 00 B0 84 60 1A 00 00 00 00 80 25 04 D3 00 00 00 00 00 
2C 21 98 86 CE 22 35 35 95 23 37 43 43 43 47 47 47 3F 3F BF A4 A4 A4 9A 9A 1A 55 D7 1D 3A 48 43 
43 C3 D6 AD 5B C9 77 20 3A 3A 5A D5 D5 01 96 AA AB AB 17 2E 5C 28 CF 91 3E 61 C2 84 F2 F2 72 55 
D7 17 D8 7B F5 EA D5 F1 E3 C7 67 CD 9A 35 74 E8 50 D2 A6 D6 D6 D6 FE FE FE D9 D9 D9 62 B1 58 D5 
B5 03 50 0C 04 D3 A0 96 84 42 E1 A5 4B 97 36 6D DA 64 6F 6F 3F 72 E4 C8 53 A7 4E 35 36 36 AA BA 
52 A0 74 29 29 29 BB 77 EF 56 75 2D A0 BD AA AA AA 0A 0B 0B 55 5D 0B 50 AE FA FA FA D8 D8 D8 7F 
FD EB 5F B3 66 CD 3A 7E FC 78 6E 6E 2E 79 FE DA B5 6B 81 81 81 C3 86 0D F3 F2 F2 7A FE FC B9 6A 
2B 09 A0 10 08 A6 41 ED E5 E6 E6 CE 9B 37 EF F8 F1 E3 72 F6 73 D4 D4 D4 94 97 97 A3 3F 5B ED 14 
16 16 FE F8 E3 8F 42 A1 50 D5 15 81 F6 2A 2E 2E 46 3B 6A B6 9A 9A 9A 8D 1B 37 BA BA BA D2 18 BA 
A9 F0 F0 F0 79 F3 E6 95 94 94 74 64 C5 00 94 01 C1 34 68 02 91 48 E4 E7 E7 97 9E 9E 2E CF C6 A7 
4F 9F EE D5 AB D7 E9 D3 A7 95 5D 2B 50 A0 AA AA AA AD 5B B7 A6 A6 A6 AA BA 22 A0 00 85 85 85 79 
79 79 AA AE 05 28 4B 43 43 C3 AE 5D BB D6 AF 5F DF EA 96 F1 F1 F1 A1 A1 A1 F5 F5 F5 CA AF 14 80 
12 21 98 86 CE 28 25 25 45 DC B2 C6 C6 C6 17 2F 5E 08 04 02 2F 2F 2F 1E 8F 47 DE 22 14 0A A3 A2 
A2 EA EA EA 54 5B 73 50 06 B1 58 1C 17 17 17 1E 1E AE EA 8A 80 62 DC BD 7B 97 14 7C 7D 7D EB EA 
EA 64 1C EC E7 CE 9D D3 D7 D7 57 6D 6D A1 AD 32 32 32 68 3A 96 9E 9E DE CF 3F FF 9C 95 95 45 1A 
FA CD 9B 37 F9 F9 F9 3F FC F0 03 3D 75 47 44 44 DC BC 79 53 75 95 05 50 00 04 D3 A0 7E 38 1C CE 
BB EF BE FB AF 7F FD 2B 34 34 74 EF DE BD F4 A4 2C 10 08 9E 3C 79 A2 DA BA 81 32 FC FD F7 DF 6B 
D7 AE 65 18 A6 4F 9F 3E B4 B9 41 4D D5 D6 D6 3E 7A F4 88 94 8D 8D 8D BB 76 ED AA DA FA 80 62 D5 
D5 D5 45 45 45 91 34 1E 1E 8F 17 16 16 E6 EF EF FF C9 27 9F 90 86 D6 D6 D6 1E 3C 78 70 70 70 30 
3D 75 17 17 17 E3 8E 13 A8 3B 04 D3 A0 C6 38 1C CE 8C 19 33 BE FB EE 3B F2 50 20 10 14 15 15 A9 
B6 4A A0 70 25 25 25 21 21 21 42 A1 D0 C0 C0 20 34 34 74 CC 98 31 AA AE 11 B4 8B 48 24 BA 7F FF 
3E 29 9B 98 98 A8 B6 32 A0 70 F9 F9 F9 17 2F 5E 24 E5 95 2B 57 CE 98 31 83 C3 E1 48 6D C3 E1 70 
BE FA EA AB B9 73 E7 92 87 F7 EE DD AB AE AE EE D0 5A 02 28 14 82 69 50 6F DA DA DA C3 87 0F A7 
0F 11 4C 6B 98 9A 9A 9A C0 C0 C0 F8 F8 78 86 61 7C 7C 7C EC EC EC 54 5D 23 68 2F 3A FA D0 DC DC 
FC FD F7 DF 57 75 75 40 C1 52 52 52 B2 B3 B3 19 86 B1 B4 B4 FC E6 9B 6F B4 B5 B5 9B DD 8C CB E5 
EE DC B9 93 24 F3 1C 38 70 A0 47 8F 1E 1D 5B 4D 00 45 6A FE 5B 0E 00 A0 72 24 55 FA E8 D1 A3 0C 
C3 4C 9F 3E 7D D1 A2 45 98 00 51 03 94 94 94 90 D1 87 C3 86 0D EB DB B7 AF AA AB 03 8A 54 5B 5B 
7B FB F6 6D 52 1E 3F 7E FC 87 1F 7E A8 DA FA 00 74 0C F4 4C 83 7A AB A9 A9 49 4E 4E A6 0F 07 0C 
18 A0 C2 CA 80 62 65 65 65 05 06 06 8A 44 22 4B 4B CB 9F 7F FE B9 67 CF 9E AA AE 11 28 C0 9D 3B 
77 48 61 D0 A0 41 3A 3A 3A 85 85 85 81 81 81 A3 46 8D E2 70 38 FA FA FA FF FE F7 BF F7 EF DF 8F 
85 5A D4 94 64 0E 8F 95 95 95 96 96 96 6A EB 03 D0 31 10 4C 83 1A AB AF AF 8F 89 89 89 89 89 21 
0F 2D 2D 2D 11 4C 6B 8C 92 92 92 75 EB D6 65 67 67 F3 78 3C 6F 6F EF A1 43 87 AA BA 46 A0 00 B5 
B5 B5 F9 F9 F9 A4 CC E7 F3 43 42 42 86 0F 1F EE EF EF 9F 91 91 C1 30 CC F3 E7 CF 13 12 12 3C 3C 
3C 6C 6C 6C 62 63 63 31 63 9A DA 29 2F 2F 27 F3 46 1B 18 18 F4 EF DF 9F 61 18 B1 58 5C 58 58 18 
1C 1C 6C 67 67 47 57 40 0C 0C 0C 2C 2C 2C C4 0A 88 A0 31 90 E6 01 EA E7 F5 EB D7 15 15 15 02 81 
E0 C0 81 03 09 09 09 F4 F9 CF 3E FB 0C C1 B4 66 A8 AF AF 3F 70 E0 00 49 95 5E BA 74 69 B3 63 98 
40 1D 55 55 55 FD F3 CF 3F A4 FC E3 8F 3F 16 17 17 37 BB 59 6E 6E AE AB AB 6B 61 61 E1 F2 E5 CB 
B9 5C 6E 07 56 10 DA A5 BC BC 3C 2B 2B 8B 61 98 3E 7D FA BC F3 CE 3B 22 91 68 F3 E6 CD 61 61 61 
22 91 88 6E 73 ED DA B5 6B D7 AE 05 07 07 AF 58 B1 62 F9 F2 E5 3A 3A 3A AA AB 2F 80 62 20 98 86 
CE 68 EC D8 B1 6D 7D 8B A5 A5 A5 BB BB 7B 4B 83 5D 40 BD 9C 3A 75 2A 38 38 98 61 98 29 53 A6 78 
7B 7B A3 59 35 C6 B3 67 CF E8 FC 95 2D 45 D2 94 9F 9F 5F 8F 1E 3D BC BD BD F1 53 4A 5D D0 49 39 
B4 B5 B5 2B 2A 2A B6 6D DB 76 E0 C0 81 66 B7 14 89 44 EB D6 AD 2B 2A 2A DA BC 79 B3 9E 9E 5E 07 
D6 11 40 F1 90 E6 01 9A C0 D8 D8 38 38 38 D8 C8 C8 48 D5 15 01 05 C8 CE CE DE B1 63 87 48 24 E2 
F3 F9 2B 56 AC C0 18 35 4D 52 54 54 44 7A 2E 19 86 31 36 36 0E 0D 0D 2D 2A 2A 7A F3 E6 0D 99 D5 
A1 BA BA 3A 33 33 53 72 31 A6 7D FB F6 D1 ED A1 F3 2B 2D 2D 25 85 1E 3D 7A 44 46 46 B6 14 49 53 
07 0E 1C D8 B6 6D 1B F2 79 40 DD 21 98 06 B5 E7 E6 E6 76 EE DC B9 4F 3F FD 54 D5 15 01 05 A8 A8 
A8 F8 E9 A7 9F 04 02 01 C3 30 81 81 81 98 55 5A C3 D0 D1 87 4E 4E 4E BF FD F6 DB D2 A5 4B 3F F8 
E0 03 7A E7 A1 7B F7 EE C3 87 0F 97 5C 8C 29 3B 3B FB D4 A9 53 0D 0D 0D 2A AB 31 B0 92 9C 9C BC 
67 CF 1E 86 61 F4 F4 F4 82 83 83 1F 3F 7E DC D0 D0 20 16 8B EB EA EA F2 F2 F2 FC FD FD E9 EF A5 
B0 B0 B0 CB 97 2F AB B4 B2 00 ED 85 60 1A D4 92 9E 9E DE A4 49 93 C2 C3 C3 1F 3E 7C 78 E4 C8 11 
43 43 43 55 D7 08 14 A0 BE BE 7E FF FE FD 27 4F 9E 64 18 C6 D3 D3 D3 C5 C5 05 F7 F7 35 8C AF AF 
2F E9 84 3E 7F FE 7C 4B 83 4A A5 56 F4 48 4E 4E 26 63 DA 40 ED 58 5A 5A 5E BE 7C 79 C5 8A 15 EF 
BF FF 7E 97 2E 5D 18 86 E9 DA B5 EB 47 1F 7D F4 F3 CF 3F C7 C6 C6 1A 18 18 30 0C 23 12 89 CE 9C 
39 53 57 57 A7 EA CA 02 B0 87 60 1A 3A A3 94 94 14 F1 FF 55 59 59 99 90 90 60 61 61 41 36 18 3C 
78 B0 8F 8F 8F 87 87 C7 80 01 03 10 6F 69 8C BF FF FE 7B E7 CE 9D 0C C3 D8 D8 D8 AC 58 B1 02 23 
93 DE 5A 5C 2E 77 D2 A4 49 A4 9C 9B A2 77 82 7A 00 00 20 00 49 44 41 54 9B DB 6A 76 35 74 42 7C 
3E 7F CB 96 2D 9F 7C F2 49 D3 97 38 1C 8E B3 B3 33 FD BD 74 E3 C6 8D A7 4F 9F 76 6C ED 00 14 49 
03 83 E9 FC FC FC D1 A3 47 73 DA 21 35 35 55 D5 7F 04 48 D3 D1 D1 99 38 71 E2 D9 B3 67 67 CF 9E 
CD 30 4C 5A 5A 9A A3 A3 A3 BF BF 7F 55 55 95 AA AB 06 8A 91 9D 9D ED E7 E7 57 5C 5C CC E7 F3 37 
6E DC 88 BB 0D 6F B9 01 03 06 98 9A 9A 32 0C 53 5C 5C 8C C3 5C 5D D0 E4 0D 86 61 26 4C 98 F0 AF 
7F FD AB A5 2D B5 B5 B5 9D 9D 9D 49 39 2B 2B 0B BF 97 D4 4B 74 74 B4 EC 38 2A 3A 3A 5A D5 75 EC 
50 1A 18 4C 3F 79 F2 24 3D 3D 5D D5 B5 00 A5 E8 DD BB F7 D6 AD 5B A7 4C 99 42 1E 06 05 05 05 05 
05 E1 42 AB 19 6E DE BC 49 52 A5 85 42 21 9D 92 56 4A AF 5E BD CE 9F 3F 4F B6 FF F6 DB 6F DF DA 
13 F7 DB 80 C3 E1 90 C4 00 86 61 8A 8A 8A 54 5B 19 90 93 BE BE 3E 2D F3 F9 FC EE DD BB CB D8 B8 
6F DF BE 66 66 66 0C C3 88 44 22 C9 B9 F3 00 D4 8E 06 06 D3 85 85 85 AA AE 02 28 51 DF BE 7D 37 
6D DA 64 69 69 49 1E 06 05 05 85 87 87 63 7C 12 80 06 C3 FC F1 EA 42 5F 5F 9F DC 4F 60 18 86 2C 
DA 22 27 3A 0D 08 80 3A D2 B4 60 BA A1 A1 21 27 27 47 D5 B5 00 E5 32 31 31 59 B6 6C 19 BD 9F B8 
7B F7 EE 94 94 14 D5 56 09 00 14 AB B2 B2 92 04 58 3C 1E AF 6B D7 AE AA AE 0E C8 45 5F 5F 9F CE 
65 99 93 93 23 BB 9B 43 2C 16 37 36 36 92 32 D2 BA D4 CB 37 DF 7C 23 96 E9 9B 6F BE 51 75 1D 3B 
94 A6 05 D3 95 95 95 79 79 79 AA AE 05 28 9D 8B 8B CB A2 45 8B 48 59 28 14 86 84 84 60 BC 3F 40 
27 27 39 A0 A5 D5 CC 9C 5B B7 6E 91 3C 5A 53 53 53 32 ED 03 74 7E 3C 1E 6F C8 90 21 A4 9C 96 96 
26 BB BF 99 4E 3A 6E 64 64 24 99 6C 0D A0 76 34 2D 98 7E F6 EC D9 83 07 0F E8 43 07 07 87 D2 D2 
52 D9 BF 9F 9A B2 B1 B1 51 E1 9F 00 F2 E0 72 B9 5E 5E 5E B4 A5 E2 E3 E3 23 23 23 91 EC A1 D6 5A 
ED EA 10 8B C5 65 65 65 74 D0 D2 B1 63 C7 DE DA 5E 10 35 D5 BB 77 EF 81 03 07 92 F2 A5 4B 97 64 
8C 76 A8 A8 A8 38 7B F6 2C 29 8F 1E 3D BA 5F BF 7E 1D 51 3F 68 B7 6E DD BA 8D 1A 35 8A 94 2F 5D 
BA 94 90 90 20 16 8B 9B DD B2 AE AE 2E 21 21 81 94 CD CC CC F8 7C 7E 07 55 11 40 09 34 2D 98 96 
1A 7D 38 78 F0 E0 77 DE 79 47 85 F5 01 E5 31 34 34 5C B1 62 85 64 B2 47 46 46 86 6A AB 04 00 32 
E8 EA EA 5A 5B 5B 93 F2 AF BF FE 1A 1F 1F DF 6C A4 55 57 57 B7 77 EF DE B8 B8 38 86 61 78 3C DE 
E4 C9 93 B9 5C 6E 87 56 14 DA 61 FC F8 F1 74 4C CB C6 8D 1B 13 13 13 9B B6 72 63 63 E3 C9 93 27 
23 22 22 C8 43 6B 6B 6B 5D 5D DD 0E AD 25 80 42 69 5A 30 2D 35 FA B0 D5 D1 C4 A0 D6 9C 9C 9C E6 
CC 99 43 CA 42 A1 30 38 38 B8 A2 A2 42 B5 55 02 80 96 90 D9 85 4D 4C 4C 18 86 11 89 44 8B 17 2F 
5E B9 72 65 7E 7E FE EB D7 AF C9 06 95 95 95 29 29 29 73 E7 CE F5 F3 F3 23 CF B8 BA BA 62 15 4C 
F5 62 68 68 38 6B D6 2C 52 16 0A 85 D3 A7 4F FF E5 97 5F 9E 3C 79 42 D2 A3 5F BF 7E 7D E7 CE 9D 
55 AB 56 79 7A 7A 92 19 3C 6C 6C 6C A6 4E 9D 8A E5 02 40 AD 69 54 30 DD 74 F4 E1 C7 1F 7F AC AA 
CA 40 07 E8 DE BD BB A7 A7 27 99 5C 89 61 98 93 27 4F 9E 3A 75 AA A5 BB 8A 00 A0 72 C3 86 0D F3 
F0 F0 20 65 91 48 F4 CB 2F BF 18 19 19 71 B9 5C 92 48 CD E3 F1 6C 6D 6D 63 63 63 C9 06 96 96 96 
3E 3E 3E E8 10 51 2F 1C 0E 67 E6 CC 99 74 02 D3 E7 CF 9F AF 5C B9 B2 7F FF FE 5A 5A 5A 1C 0E 87 
CB E5 9A 9A 9A FE F2 CB 2F 24 92 E6 F1 78 9E 9E 9E C8 F1 00 75 A7 51 C1 B4 D4 E8 43 23 23 23 0C 
10 D6 78 43 87 0E FD E1 87 1F E8 C3 DD BB 77 63 3A 17 80 4E 8B C3 E1 2C 5A B4 68 FD FA F5 AD 6E 
69 66 66 16 12 12 42 BA B1 41 BD F4 ED DB 77 E7 CE 9D 13 27 4E 6C 75 CB 1F 7F FC 71 C6 8C 19 E8 
96 06 75 A7 51 C1 B4 D4 E8 43 3E 9F 8F 31 E0 1A 8F C3 E1 4C 9E 3C D9 CD CD 8D 3C CC CC CC 0C 0F 
0F AF A9 A9 A1 1B C8 3F 2A 11 E3 17 01 3A 40 F7 EE DD 57 AF 5E 1D 1D 1D 6D 6C 6C DC D2 36 2E 2E 
2E A7 4F 9F A6 09 D6 A0 76 F8 7C 7E 64 64 E4 AA 55 AB 5A 9A A6 C3 D8 D8 38 26 26 E6 FB EF BF D7 
D6 D6 EE E0 BA 01 28 9C 46 05 D3 25 25 25 18 7D F8 16 D2 D5 D5 5D BA 74 29 BD 51 78 F4 E8 D1 F8 
F8 78 FA EA C9 93 27 7F FC F1 C7 67 CF 9E C9 D8 C3 C3 87 0F 57 AC 58 71 E2 C4 09 E5 56 14 00 18 
86 61 18 2E 97 EB EA EA 7A FD FA F5 D8 D8 D8 99 33 67 D2 A8 DA CA CA 6A ED DA B5 37 6E DC 38 75 
EA D4 A0 41 83 54 5B 49 68 27 3D 3D BD 4D 9B 36 DD BE 7D 3B 24 24 64 D2 A4 49 7A 7A 7A 0C C3 F0 
F9 FC 19 33 66 C4 C6 C6 5E BF 7E 7D D6 AC 59 88 A4 41 33 68 D4 F7 F8 9F 7F FE 91 7C 88 D1 87 EA 
C5 C6 C6 86 75 BA F3 E8 D1 A3 5B 5A F9 72 C0 80 01 EB D7 AF DF BB 77 EF DA B5 6B 17 2F 5E 2C F5 
95 A8 AA AA DA BF 7F 7F 60 60 E0 80 01 03 66 CC 98 C1 EE D3 A1 C3 E8 EB EB 9F 3B 77 4E D5 B5 00 
C5 D0 D5 D5 9D 39 73 E6 CC 99 33 55 5D 11 50 16 0E 87 63 68 68 B8 6C D9 B2 65 CB 96 A9 BA 2E 00 
4A A4 39 3D D3 18 7D 08 CD B2 B1 B1 89 8E 8E 36 32 32 5A BE 7C F9 37 DF 7C 23 14 0A E9 4B 39 39 
39 53 A7 4E 5D BE 7C B9 91 91 D1 A1 43 87 2C 2C 2C 54 58 4F 00 00 00 50 47 9A D3 33 DD D2 E8 43 
B1 58 5C 52 52 72 F6 EC D9 4B 97 2E 65 64 64 E4 E6 E6 32 0C 63 6C 6C 6C 62 62 32 6E DC 38 67 67 
67 63 63 E3 2E 5D 34 E7 47 05 34 65 6E 6E BE 7B F7 EE 25 4B 96 C4 C5 C5 DD BB 77 6F C4 88 11 0C 
C3 FC FE FB EF 01 01 01 B9 B9 B9 96 96 96 07 0F 1E FC E4 93 4F 54 5D 4D 00 00 00 50 3F FF 1B 42 
AB 01 B3 89 E5 E7 E7 CF 9C 39 93 E6 4C 3B 38 38 44 47 47 97 97 97 6F DD BA F5 D4 A9 53 64 16 9E 
66 D9 DA DA AE 5B B7 6E FC F8 F1 1A 19 52 93 51 D2 1A D0 BE ED 77 F9 F2 E5 39 73 E6 48 F6 4C 33 
0C 63 69 69 B9 7B F7 6E 73 73 73 55 D5 AA 9D D0 BE 9A 0D ED AB D9 D0 BE 9A 0D ED AB D9 24 DB 57 
73 C2 47 A9 D1 87 BD 7B F7 DE B3 67 8F A5 A5 65 44 44 84 8C 48 9A 61 98 E4 E4 64 47 47 C7 85 0B 
17 3E 7D FA 54 F9 D5 04 95 F9 F4 D3 4F 83 82 82 24 87 96 F3 F9 FC 2D 5B B6 A8 6F 24 0D 00 00 00 
2A A7 39 69 1E 52 A3 0F E9 B4 FF 72 3A 7C F8 70 6E 6E EE A1 43 87 64 CC D6 04 6A 8D C3 E1 CC 98 
31 A3 A8 A8 68 F5 EA D5 E4 19 5F 5F DF 4F 3F FD 54 B5 B5 02 00 00 00 B5 A6 21 3D D3 4D 47 1F B2 
90 9A 9A 3A 67 CE 9C EC EC 6C 85 54 09 3A 21 6D 6D ED 39 73 E6 90 A5 04 A6 4F 9F EE E6 E6 86 C5 
02 00 00 00 A0 3D 34 24 98 96 1A 7D 48 D9 DA DA 1E 39 72 A4 A0 A0 A0 BA BA 5A FC FF 89 44 A2 82 
82 82 23 47 8E D8 DA DA 4A 6D 2F 10 08 7E FA E9 A7 8A 8A 8A 0E A9 35 A8 40 BF 7E FD 16 2E 5C C8 
E7 F3 BD BC BC 7A F6 EC A9 EA EA 00 00 00 80 7A D3 90 01 88 52 A3 0F 19 86 31 36 36 5E B7 6E DD 
57 5F 7D C5 E5 72 5B 7A 57 5D 5D DD C9 93 27 D7 AE 5D 2B 35 28 6D FF FE FD 0B 16 2C D0 8C 3E 4B 
0C 80 68 AA A6 A6 26 3B 3B FB E3 8F 3F 96 F1 DD 50 17 68 5F CD 86 F6 D5 6C 68 5F CD 86 F6 D5 6C 
92 ED AB 21 C1 34 C3 30 95 95 95 B9 B9 B9 57 AE 5C 49 49 49 29 2D 2D 0D 0B 0B 93 73 B2 B3 A6 93 
3C D8 DB DB 47 45 45 F5 EF DF 5F 69 95 ED 38 38 98 35 1B DA 57 B3 A1 7D 35 1B DA 57 B3 A1 7D 35 
9B 66 06 D3 AC 89 C5 E2 D0 D0 50 A9 F5 99 7E FD F5 D7 A9 53 A7 AA AA 4A 0A 84 83 59 B3 A1 7D 35 
1B DA 57 B3 A1 7D 35 1B DA 57 B3 69 E6 D4 78 AC 71 38 9C C9 93 27 5B 5A 5A 4A 3E 99 92 92 F2 FA 
F5 6B 55 55 09 00 00 00 00 D4 02 82 69 86 61 98 FE FD FB 8F 19 33 46 F2 99 AC AC AC 97 2F 5F AA 
AA 3E 00 00 00 00 A0 16 10 4C 33 0C C3 74 ED DA 95 2C 31 4D 3D 7B F6 EC F9 F3 E7 AA AA 0F 00 00 
00 00 A8 05 04 D3 FF 63 60 60 20 F9 B0 B4 B4 B4 B2 B2 52 55 95 01 00 00 00 00 B5 80 60 FA 7F 7A 
F4 E8 21 F9 B0 B8 B8 B8 B6 B6 56 55 95 01 00 00 00 00 B5 80 60 BA 79 A6 A6 A6 FA FA FA AA AE 05 
00 00 00 00 74 6A 08 A6 FF A7 B0 B0 50 F2 61 D7 AE 5D B5 B5 B5 55 54 17 00 00 00 00 50 0F 9A 10 
4C E7 E7 E7 8F 1E 3D 9A 23 E1 3F FF F9 4F 5B 77 F2 F0 E1 43 C9 87 FD FA F5 43 CF 34 00 00 00 00 
C8 A6 09 C1 74 EF DE BD 07 0E 1C 28 F9 4C 66 66 66 43 43 83 FC 7B 78 F9 F2 E5 CD 9B 37 25 9F 19 
3E 7C B8 AE AE AE 62 EA 07 F2 49 4D 4D E5 C8 CD D0 D0 D0 D1 D1 D1 CF CF 2F 29 29 A9 A6 A6 46 D5 
75 87 D6 49 B6 6F 6A 6A AA D4 AB D1 D1 D1 E4 A5 09 13 26 94 97 97 CB B3 C3 EC EC 6C 2B 2B 2B BA 
4F 37 37 B7 67 CF 9E D1 57 03 02 02 C8 F3 8B 17 2F C6 37 A4 55 F4 BF 8B 70 74 74 2C 2E 2E 96 FF 
ED 4F 9E 3C B1 B7 B7 97 DC 43 40 40 80 D4 36 E5 E5 E5 13 26 4C 20 AF 0E 1B 36 EC F6 ED DB 72 EE 
3C 37 37 77 C4 88 11 E4 8D D1 D1 D1 F2 BC A5 BE BE FE DE BD 7B 3B 76 EC 98 32 65 8A A1 A1 21 3D 
69 4C 9C 38 31 20 20 20 2D 2D AD BE BE 5E FE BF 4E 5D D0 83 48 36 5D 5D DD 4F 3F FD 74 EE DC B9 
C7 8F 1F 2F 2D 2D 6D D3 47 88 C5 E2 A7 4F 9F 1E 3F 7E 7C EE DC B9 A3 46 8D 92 DC E1 92 25 4B CE 
9E 3D 5B 51 51 21 CF 7E 6A 6A 6A 16 2F 5E 2C D7 B9 9E C3 E1 70 38 D6 D6 D6 B3 66 CD DA B7 6F 5F 
51 51 91 FC 6B A0 34 36 36 66 67 67 EF D8 B1 C3 C5 C5 65 E8 D0 A1 64 57 FA FA FA E3 C7 8F 57 ED 
B5 43 F2 58 50 6A 7B 31 8A 3B 16 24 EB DC F4 E8 96 41 F6 F1 2B 79 5D 98 33 67 CE AB 57 AF E4 DC 
2D FD B6 8F 18 31 22 37 37 57 C6 6E 65 18 35 6A 94 8B 8B 4B 70 70 B0 C2 CE 09 62 75 56 5F 5F BF 
66 CD 1A C9 3F C7 D2 D2 B2 A0 A0 40 FE 3D 5C BE 7C 59 6A 36 8F F8 F8 78 E5 55 B8 23 A9 51 FB A6 
A4 A4 B0 FB F6 1A 1B 1B 9F 3C 79 B2 A1 A1 41 D5 7F 81 0A A8 69 FB A6 A4 A4 48 BD 7A EC D8 31 F2 
92 B3 B3 73 59 59 59 AB 7B BB 77 EF 9E E4 42 4B 0B 17 2E 2C 2F 2F 97 DC 60 C3 86 0D E4 25 0F 0F 
8F EA EA 6A 45 FE 25 1D A8 C3 DA 97 FE 77 51 17 2E 5C 90 FF ED 17 2E 5C 90 7A FB 86 0D 1B A4 B6 
29 2B 2B 73 76 76 A6 1B B8 B9 B9 BD 7C F9 52 9E 9D E7 E4 E4 98 99 99 91 77 1D 3B 76 4C F6 C6 B5 
B5 B5 A7 4E 9D B2 B0 B0 90 7D D2 30 35 35 8D 89 89 A9 AD AD 95 FF 6F 54 06 C5 B6 2F 3D 88 E4 C7 
E3 F1 56 AD 5A 25 75 EC 34 AB B1 B1 F1 D6 AD 5B B3 66 CD 6A 75 87 5E 5E 5E 0F 1E 3C 90 BD B7 EA 
EA 6A 0F 0F 8F B6 D6 96 98 37 6F 5E 71 71 71 AB B5 4D 4F 4F 9F 34 69 92 EC 5D 19 1B 1B 47 47 47 
2B EF 6B 40 3E A5 E9 F3 52 C7 82 FC 78 3C 9E 9F 9F DF AB 57 AF E4 F9 74 C5 1E 0B 92 75 6E 7A 74 
CB 20 FB F8 95 BA EE EF DF BF BF B1 B1 51 9E DD D2 6F BB 99 99 59 4E 4E 8E EC DD CA 83 C5 39 81 
BC 91 94 35 A1 67 5A 4B 4B CB CA CA 4A F2 19 81 40 70 E6 CC 19 B1 7C BF 5F 5F BD 7A 75 E8 D0 21 
C9 6E 18 07 07 87 56 BF 7F D0 79 E4 E6 E6 CE 9B 37 EF F8 F1 E3 72 B6 78 63 63 E3 CB 97 2F 1B 1B 
1B 95 5D 31 50 92 EC EC EC B9 73 E7 0A 04 02 F2 70 E1 C2 85 9B 37 6F D6 D3 D3 53 6D AD 34 4C 62 
62 A2 9C F7 F7 1A 1A 1A 12 13 13 DB BA FF C8 C8 48 F9 CF D2 72 2A 28 28 98 35 6B D6 B4 69 D3 D2 
D2 D2 64 6F 99 95 95 E5 EA EA 3A 6D DA B4 5B B7 6E 29 B0 02 6A 47 24 12 6D D9 B2 65 DE BC 79 25 
25 25 B2 37 5B BB 76 AD AD AD 6D 6C 6C 6C AB 3B DC B5 6B 97 B9 B9 F9 EE DD BB EB EA EA 14 5A D9 
FF 39 7C F8 F0 E2 C5 8B 65 54 B8 BE BE 7E F7 EE DD 76 76 76 09 09 09 B2 77 95 9B 9B FB CD 37 DF 
2C 5C B8 50 F2 A6 56 67 26 12 89 82 82 82 56 AF 5E 5D 55 55 25 7B 4B 35 3D 16 76 EF DE 9D 93 93 
A3 92 8F 26 FF 0F CB 97 2F 67 B7 C6 88 26 04 D3 0C C3 58 58 58 38 38 38 48 3E 13 12 12 F2 F7 DF 
7F B7 FA C6 FA FA FA 3D 7B F6 44 46 46 4A 3E 39 63 C6 8C 7E FD FA 29 B8 8A A0 4C 22 91 C8 CF CF 
2F 3D 3D 5D 9E 8D 6F DC B8 F1 D9 67 9F DD B9 73 47 D9 B5 02 65 90 8A A4 BF FB EE BB 6D DB B6 21 
92 56 B8 AB 57 AF CA 0E B0 A8 D2 D2 D2 56 2F D8 CD FA E5 97 5F 14 78 E1 BC 7A F5 EA D4 A9 53 E3 
E2 E2 E4 7F 4B 42 42 C2 97 5F 7E F9 D7 5F 7F 29 36 A6 57 3B F1 F1 F1 81 81 81 2D E5 3C 94 94 94 
CC 9F 3F 3F 28 28 48 24 12 C9 B9 C3 E7 CF 9F 7B 79 79 AD 58 B1 42 FE B7 B4 49 7C 7C FC D6 AD 5B 
9B 0D D6 C5 62 F1 89 13 27 FC FC FC E4 FF E8 A8 A8 28 0F 0F 0F 75 89 A7 19 86 09 0F 0F 3F 78 F0 
A0 8C 2F AD FA 1E 0B 99 99 99 21 21 21 AD FE 54 50 9E F0 F0 70 7F 7F 7F 16 15 D0 90 60 DA C0 C0 
C0 DD DD 5D F2 19 A1 50 E8 E3 E3 93 9A 9A 2A E3 9B F1 EC D9 B3 35 6B D6 AC 5E BD 5A F2 49 17 17 
97 2F BF FC 92 C3 E1 28 A9 AA 20 8F A6 69 00 92 1A 1B 1B 5F BC 78 21 10 08 BC BC BC 78 3C 1E 79 
8B 50 28 8C 8A 8A 6A B5 2F A4 AA AA EA E0 C1 83 E9 E9 E9 91 91 91 4A EA 38 01 E5 91 8A A4 3D 3D 
3D B7 6E DD 4A BF 03 D0 7E 26 26 26 B6 B6 B6 0C C3 24 25 25 DD BD 7B 57 9E B7 DC BB 77 8F B4 88 
AD AD AD 89 89 89 FC 9F A5 C0 0B 67 76 76 B6 AF AF 6F 66 66 26 7D C6 D8 D8 78 F3 E6 CD 59 59 59 
34 C9 A7 AE AE AE A0 A0 60 C7 8E 1D A6 A6 A6 74 33 A1 50 38 6F DE 3C 79 7A 5E D4 48 B3 37 BE 25 
CF 9F CF 9F 3F FF E3 8F 3F 24 33 0D 8E 1E 3D 7A E5 CA 95 A6 BB 2A 29 29 F1 F0 F0 38 79 F2 24 7D 
46 4F 4F CF C7 C7 47 20 10 BC 78 F1 82 DC 91 6F 68 68 28 2D 2D 8D 8F 8F 97 4A AB 08 0B 0B 93 A7 
0F B5 D5 44 AC BA BA BA A2 A2 A2 C8 C8 48 C9 3B C6 31 31 31 92 CD 4D 15 16 16 86 86 86 D2 48 DA 
C2 C2 22 32 32 B2 A8 A8 A8 AE AE 8E EC AD A1 A1 A1 AC AC 2C 31 31 51 32 65 25 2E 2E 2E 26 26 46 
25 71 64 AB 29 13 D5 D5 D5 05 05 05 DB B7 6F 37 36 36 A6 EF 8A 8D 8D 95 9A 82 8C 52 F7 63 E1 C0 
81 03 71 71 71 0A 6C 8B 96 C2 89 86 86 86 E7 CF 9F DF B8 71 63 C3 86 0D 7C 3E 9F 6E 1F 1E 1E BE 
6B D7 2E 96 29 D4 B2 DB 52 2D BC 7C F9 D2 CD CD 4D EA EF E2 F1 78 6E 6E 6E 89 89 89 65 65 65 34 
A7 56 24 12 65 65 65 49 FD F7 11 7C 3E 5F 76 18 A7 76 D4 A8 7D 65 E7 D4 36 AB B1 B1 31 3A 3A 9A 
C6 52 AD E6 CA 4B 6E CF E3 F1 62 63 63 15 54 77 95 D1 98 F6 95 27 67 3A 27 27 C7 C6 C6 86 EE C4 
C7 C7 A7 B2 B2 B2 A5 8F 43 CE 74 9B D0 FF 2E 67 67 E7 8D 1B 37 92 B2 AF AF 2F 0D 41 5A 52 5F 5F 
EF EF EF 4F B6 DF B8 71 A3 8C AC CA 96 F2 44 A3 A2 A2 64 67 49 B6 9A 33 5D 5A 5A EA E2 E2 42 77 
A8 A7 A7 B7 7D FB 76 19 DF 8D DA DA DA C3 87 0F 4B DE CD B0 B7 B7 7F F4 E8 91 EC BF 54 19 14 DB 
BE B2 B3 48 9B 2A 2F 2F 5F B8 70 21 FD 4F 68 DA DC 6F DE BC D9 BC 79 B3 64 63 79 7A 7A 3E 79 F2 
A4 A5 1D 92 4C 65 27 27 27 C9 B7 34 9B 05 2B 99 33 2D FF 11 FA F4 E9 D3 29 53 A6 D0 3D 6F DB B6 
AD E9 9E F7 EE DD 4B 37 58 BD 7A B5 8C F4 E2 86 86 86 84 84 04 1A 06 B4 75 A8 95 3C 5A 6A 5F 76 
F9 C7 52 03 45 7E FD F5 D7 A6 DB 28 EF 58 E8 98 9C 69 FA 05 BE 77 EF 9E EC DD CA 9F 33 2D 4F 38 
F1 F0 E1 43 C9 1F 57 06 06 06 97 2F 5F 6E F5 5D 92 ED AB 21 3D D3 0C C3 E8 EA EA AE 5E BD 5A F2 
AB C6 30 8C 48 24 8A 8C 8C B4 B7 B7 EF D5 AB 97 96 96 16 19 BF C9 E3 F1 4C 4D 4D D7 AD 5B 27 14 
0A 25 37 D6 D3 D3 DB BC 79 F3 98 31 63 3A B6 E2 C0 1E 87 C3 99 31 63 C6 77 DF 7D 47 1E 0A 04 82 
A2 A2 22 19 DB FF FD F7 DF F4 F6 9F 48 24 DA B1 63 47 76 76 76 47 54 14 DA 2D 37 37 77 FE FC F9 
74 1A 10 1F 1F 9F 8D 1B 37 EA E8 E8 A8 B6 56 1A 69 DC B8 71 E4 E2 27 10 08 5A 9D D3 A3 A2 A2 82 
E4 78 98 98 98 C8 7F F2 9C 30 61 02 3D 57 EF DA B5 AB 3D C9 1E 62 B1 38 26 26 86 DE D1 36 33 33 
3B 73 E6 CC B2 65 CB 64 7C 37 B8 5C EE DC B9 73 13 12 12 E8 35 3E 31 31 31 32 32 B2 4D 73 40 69 
00 3D 3D 3D 2F 2F 2F 7A 33 21 2B 2B EB E5 CB 97 92 1B DC BA 75 6B CF 9E 3D A4 CC E3 F1 C2 C2 C2 
76 EE DC 29 35 58 5F 12 99 1E E1 D8 B1 63 B3 67 CF A6 4F EE DE BD FB FE FD FB 0A A9 70 DF BE 7D 
7F FA E9 27 23 23 23 F2 30 3B 3B 5B 2A 35 A5 B6 B6 96 CE 12 33 79 F2 64 5F 5F 5F 19 B7 AD BA 74 
E9 F2 C5 17 5F 04 06 06 92 87 02 81 A0 D9 BE F9 CE C3 C4 C4 E4 A7 9F 7E A2 0F 6F DF BE 2D FE BF 
DD B7 EA 7E 2C 7C FB ED B7 A4 BD 32 33 33 77 ED DA D5 91 C9 1E 03 06 0C 08 09 09 A1 3F D5 8A 8B 
8B 23 22 22 DA 54 01 CD 09 A6 19 86 31 31 31 39 7A F4 A8 64 DF 95 FC F8 7C FE 81 03 07 BE FE FA 
6B 24 78 A8 17 6D 6D ED E1 C3 87 D3 87 32 82 E9 EC EC EC 55 AB 56 49 FE 82 12 08 04 6B D6 AC 91 
33 31 14 54 48 2A 92 F6 F3 F3 43 24 AD 3C 7C 3E 9F 0C E9 BE 72 E5 4A B3 77 D2 25 E5 E6 E6 92 76 
B1 B4 B4 94 9A A2 54 06 6B 6B 6B 6F 6F 6F 72 E1 14 08 04 ED B9 70 0A 85 42 9A 84 60 60 60 B0 7D 
FB 76 1B 1B 1B 79 4E E3 D6 D6 D6 DB B7 6F A7 A1 61 54 54 94 AA 46 3E A9 90 91 91 D1 A7 9F 7E 4A 
CA CF 9E 3D 93 1C 7A 55 57 57 17 15 15 45 4F 98 3F FE F8 E3 E2 C5 8B E5 59 CB AC 77 EF DE 5B B7 
6E A5 71 49 66 66 66 74 74 B4 A2 82 B3 0F 3F FC 70 D0 A0 41 A4 5C 54 54 24 15 4C D7 D4 D4 D0 0A 
8F 1E 3D BA 4F 9F 3E B2 F7 C6 E1 70 3E FB EC 33 3A E0 EA EE DD BB 9D FC 07 D5 A0 41 83 68 D4 FB 
F4 E9 D3 DA DA 5A C9 57 D5 FD 58 F8 F6 DB 6F E9 CF B0 A8 A8 28 32 A9 5A 87 7D 7A DF BE 7D 37 6D 
DA 44 7F E4 9F 3F 7F 5E CE 3C 37 42 A3 82 69 86 61 8C 8D 8D 4F 9D 3A 35 6F DE BC 36 BD CB C9 C9 
E9 B7 DF 7E 9B 3A 75 2A 22 69 4D F5 F8 F1 E3 35 6B D6 08 04 02 1E 8F 47 02 05 2B 2B 2B 1E 8F 17 
1F 1F EF E1 E1 81 78 BA 33 CB CB CB F3 F6 F6 A6 91 F4 FA F5 EB D7 AE 5D 8B 48 5A 79 BA 77 EF 4E 
D2 A6 19 86 49 4A 4A 7A FD FA 75 4B 5B 8A C5 E2 C4 C4 44 72 AB 67 EC D8 B1 EF BC F3 8E 9C 1F C1 
E1 70 A6 4C 99 32 73 E6 4C F2 B0 3D 17 CE D4 D4 54 FA DD 98 3B 77 2E 0D 0D E5 41 A6 EF 25 E5 EC 
EC EC A6 13 FC 69 BC EE DD BB F7 EF DF 9F 94 33 33 33 CB CA CA E8 4B F9 F9 F9 17 2F 5E 24 E5 89 
13 27 CE 99 33 47 FE 55 81 FB F6 ED EB ED ED 4D 83 B3 E4 E4 E4 8E 39 C7 72 B9 5C FA A1 24 B1 B3 
D5 B7 E8 EB EB D3 BC E1 E7 CF 9F CB F8 B6 77 7E EA 7E 2C BC F3 CE 3B 5E 5E 5E E4 D7 82 48 24 0A 
0D 0D ED E0 98 7E E8 D0 A1 33 66 CC 20 E5 E2 E2 E2 A6 EB 21 C8 A0 69 C1 34 C3 30 FD FA F5 3B 70 
E0 C0 5F 7F FD 25 CF 3C 8E A6 A6 A6 D1 D1 D1 BF FD F6 DB 88 11 23 3A A0 6E A0 70 35 35 35 C9 C9 
C9 F4 E1 80 01 03 9A 6E F3 F8 F1 E3 25 4B 96 C4 C7 C7 1B 1B 1B 9F 38 71 62 C9 92 25 0C C3 78 7A 
7A 1E 3E 7C D8 D8 D8 38 3E 3E 7E E9 D2 A5 88 A7 3B A7 BC BC 3C 2F 2F 2F 7A 66 5F BF 7E FD CA 95 
2B BB 77 EF AE DA 5A 69 BC 31 63 C6 90 1E 9A 2B 57 AE 3C 7E FC B8 A5 CD CA CB CB C9 F5 C6 C8 C8 
A8 AD D3 89 EA E8 E8 F8 FA FA B6 F3 C2 29 79 F8 1B 18 18 4C 99 32 45 FE 80 8F 61 18 6D 6D ED AF 
BF FE 9A E6 39 5C B9 72 45 2A CF E1 AD 62 64 64 24 99 14 91 92 92 42 B3 E0 5C 5C 5C DA 3A C3 95 
A5 A5 25 BD 04 CB 3F 98 B5 55 77 EF DE A5 89 1C 03 06 0C 90 3A 15 70 B9 DC DE BD 7B 93 F2 DF 7F 
FF FD E4 C9 93 56 77 D8 B5 6B D7 ED DB B7 93 B4 D7 BD 7B F7 76 F2 73 CB 8D 1B 37 E8 CD A2 7E FD 
FA 75 EB D6 8D BE A4 19 C7 C2 D0 A1 43 7F F8 E1 07 52 6E E7 3D 2B 16 38 1C 8E B3 B3 33 FD 4F B8 
77 EF 5E 75 75 B5 9C EF D5 C0 60 9A 61 98 2E 5D BA D8 DB DB FF F1 C7 1F 85 85 85 07 0F 1E 74 77 
77 97 9C 88 7A E4 C8 91 5F 7E F9 65 48 48 C8 DD BB 77 6F DE BC E9 EA EA DA C9 8F 1F 68 49 7D 7D 
7D 4C 4C 4C 4C 4C 0C 79 68 69 69 D9 34 98 16 0A 85 1E 1E 1E F1 F1 F1 6E 6E 6E 17 2F 5E 24 6B 38 
31 0C D3 A5 4B 97 69 D3 A6 9D 3B 77 CE CD CD ED E4 C9 93 F3 E7 CF 97 CA A1 07 95 93 8A A4 C9 04 
AB 38 5A 3B C0 FB EF BF 4F 82 69 81 40 90 91 91 D1 D2 66 34 C7 C3 CA CA 4A FE 1C 0F 4A EA C2 19 
1E 1E DE D6 15 E9 2A 2A 2A E8 E2 67 36 36 36 92 D3 1D C8 69 E0 C0 81 A3 47 8F 26 E5 DC DC DC 36 
AD FB A8 01 44 22 51 5E 5E 1E 29 EB EA EA F6 E8 D1 83 94 25 93 8F 59 FC 52 62 18 46 47 47 47 72 
BE DA 1B 37 6E B4 BB B2 8C 50 28 0C 0E 0E A6 6D 64 62 62 22 75 36 D0 D2 D2 9A 30 61 02 E9 9C 4E 
4C 4C 5C BC 78 F1 8D 1B 37 34 66 49 81 F4 F4 F4 B0 B0 30 FA 70 F8 F0 E1 92 F7 D2 35 E3 58 E0 70 
38 2E 2E 2E 74 5C 6C 54 54 D4 EF BF FF DE 91 15 F8 E0 83 0F 3E FE F8 63 52 CE CF CF 7F F1 E2 85 
9C 6F D4 CC 60 9A E8 D2 A5 0B 9F CF 9F 3F 7F 7E 44 44 C4 D5 AB 57 E9 00 CC 9B 37 6F C6 C5 C5 2D 
5B B6 6C D8 B0 61 6D FA E9 06 9D C4 EB D7 AF 4B 4A 4A CE 9C 39 E3 E2 E2 B2 60 C1 02 3A 0B D2 67 
9F 7D D6 34 98 4E 49 49 E1 70 38 C9 C9 C9 11 11 11 4D 5F 35 34 34 8C 88 88 B8 78 F1 E2 AB 57 AF 
58 2F C1 08 CA 20 15 49 6F D8 B0 61 F9 F2 E5 5C 2E 57 B5 B5 7A 4B 70 B9 DC 71 E3 C6 91 F2 E5 CB 
97 5B 9A D0 57 20 10 90 A3 CF C6 C6 86 C5 04 85 52 17 CE A3 47 8F C6 C7 C7 B7 69 0F C5 C5 C5 34 
80 30 32 32 92 3F CF 84 E2 F1 78 23 47 8E 24 E5 AC AC 2C D9 23 98 35 4F 6E 6E 2E 9D 0A 6D E0 C0 
81 B4 5B B7 AA AA EA 9F 7F FE 21 E5 21 43 86 34 7B C7 AF 55 A6 A6 A6 74 B0 A0 50 28 64 B7 76 B7 
58 2C 7E F9 F2 E5 9D 3B 77 02 02 02 C6 8D 1B 77 F6 EC 59 F2 BC 89 89 89 83 83 43 D3 CC 4C 4B 4B 
4B 57 57 57 52 4E 48 48 B0 B0 B0 B0 B3 B3 DB B1 63 C7 9D 3B 77 D4 31 85 A3 B1 B1 B1 A2 A2 E2 FA 
F5 EB CB 96 2D 73 72 72 A2 B3 82 DA DB DB 4B 4D B7 A0 31 C7 82 D4 3D AB 1D 3B 76 D0 DF 7B 1D E0 
9D 77 DE A1 5F DA F2 F2 72 F9 97 37 47 28 09 9D D1 D8 B1 63 DB FA 16 4B 4B 4B 77 77 F7 A6 BF 8E 
FE FD EF 7F CF 9A 35 AB 4B 97 16 7F 37 76 E9 D2 C5 C1 C1 C1 D6 D6 56 49 EB 0B 00 0B 42 A1 D0 D7 
D7 57 32 6F 2F 23 23 E3 D5 AB 57 F4 62 0F CA 66 6E 6E 3E 66 CC 98 2B 57 AE 08 04 82 27 4F 9E 34 
ED 78 7E F1 E2 05 F9 FD 69 64 64 64 6D 6D CD EE 53 74 74 74 BC BC BC 48 46 01 B9 70 9A 9B 9B D3 
8B 59 AB AA AA AA 68 FF 19 9F CF D7 D2 D2 62 51 87 C1 83 07 D3 72 69 69 29 8B 3D A8 29 A1 50 B8 
7E FD 7A 7A 47 CE DA DA 5A 57 57 97 94 CB CA CA 9E 3E 7D 4A CA 1F 7C F0 81 64 3A 81 FC 7A F5 EA 
D5 BF 7F 7F 12 09 3D 7A F4 A8 B6 B6 B6 D9 DB 4A FB F6 ED DB B7 6F 5F 5B 77 3E 77 EE 5C DA 83 28 
89 CB E5 FA F9 F9 D5 D4 D4 84 87 87 93 67 92 93 93 69 FE 83 95 95 95 BD BD BD 9D 9D 9D B9 B9 B9 
9E 9E 5E 67 18 25 B5 6E DD BA 75 EB D6 B5 E9 2D 3C 1E 6F D1 A2 45 34 D9 9D D0 A4 63 61 E8 D0 A1 
4B 96 2C 59 B4 68 11 C3 30 02 81 20 34 34 34 38 38 B8 63 EE 49 6A 69 69 D1 0F CA CA CA 2A 2F 2F 
97 F3 8D 9A DC 33 0D 6F 0F 63 63 E3 E0 E0 E0 66 AF C1 BA BA BA 32 22 69 8A CB E5 F6 EA D5 4B 09 
55 83 36 2B 2C 2C 5C B2 64 09 ED 82 22 E2 E2 E2 0E 1F 3E CC 72 22 7D 68 3B 03 03 03 D9 99 1E 79 
79 79 D7 AE 5D 63 D8 E6 78 50 A6 A6 A6 BE BE BE A4 4C 2E 9C F2 77 61 4A 76 9E B1 E8 8A 23 F4 F5 
F5 69 F9 E1 C3 87 EC 76 A2 46 6A 6A 6A B2 B3 B3 43 42 42 9C 9D 9D E9 51 66 66 66 36 71 E2 C4 66 
83 CB FE FD FB B3 8B 63 B8 5C 2E BD 95 54 5F 5F AF C0 74 0B 1F 1F 1F 4F 4F CF 96 E2 45 32 B9 72 
74 74 74 D3 54 87 6B D7 AE 6D DA B4 C9 D9 D9 B9 57 AF 5E 26 26 26 81 81 81 B9 B9 B9 1D 39 65 44 
FB F1 78 3C 7F 7F FF 69 D3 A6 49 3D AF 49 C7 02 87 C3 F9 FA EB AF E9 CA 21 2C EE 59 B5 47 AB 93 
C0 34 0B C1 34 A8 3D 37 37 B7 73 E7 CE B5 69 E4 32 74 5A 39 39 39 F3 E7 CF 27 D7 78 1E 8F E7 ED 
ED 4D EF 66 6E DC B8 51 2A C2 06 E5 E9 DA B5 AB 9D 9D 1D 29 37 CD F4 20 CB 22 90 9E 30 76 39 1E 
54 D3 0B A7 0A 67 D5 D0 8C 5F 6B 99 99 99 43 87 0E E5 B4 A0 47 8F 1E C3 86 0D 5B BE 7C 39 CD 0A 
60 18 66 C9 92 25 43 86 0C 51 61 9D E5 64 6C 6C 1C 1D 1D BD 65 CB 16 D9 F3 F9 70 B9 5C 57 57 D7 
8C 8C 8C F3 E7 CF CF 9E 3D 5B 72 51 12 2A 37 37 D7 DF DF 7F E8 D0 A1 EE EE EE 2D AD 26 D8 D9 58 
58 58 9C 3E 7D FA FB EF BF EF 80 0C 55 D5 1E 0B BA BA BA DF 7F FF 3D 19 0B 28 12 89 76 ED DA D5 
61 6D C4 EE A7 08 82 69 50 4B 7A 7A 7A 93 26 4D 0A 0F 0F 7F F8 F0 E1 91 23 47 0C 0D 0D 55 5D 23 
50 0C A1 50 48 86 AB F3 78 BC 90 90 90 6D DB B6 6D D8 B0 81 C4 6A 22 91 68 D3 A6 4D 58 67 A7 C3 
8C 1E 3D 9A C4 D3 97 2F 5F 96 BA 92 BD 7A F5 EA EA D5 AB 4C FB 72 3C 28 A9 0B E7 D6 AD 5B 55 15 
DC BC 9D A3 68 FC FC FC 5C 5D 5D 95 9A F3 A0 AD AD 2D CF 1D C2 96 8C 1C 39 D2 DB DB 3B 31 31 31 
23 23 C3 D5 D5 55 CE B1 13 DD BB 77 77 72 72 8A 8C 8C 2C 29 29 C9 C9 C9 89 8E 8E 9E 33 67 4E D3 
95 8F 23 23 23 27 4C 98 90 94 94 D4 69 BB A8 AD AC AC D6 AE 5D 7B FD FA F5 2B 57 AE 38 38 38 B4 
E7 7F 52 7E 2A 3F 16 24 EF 59 A5 A6 A6 EE DA B5 AB D9 C1 1B 0A C7 AE 4B 1E C1 34 74 46 4D D7 FF 
AC AC AC 24 A3 49 C8 06 83 07 0F F6 F1 F1 F1 F0 F0 18 30 60 40 67 C8 7B 03 C5 22 91 34 99 DA 76 
FC F8 F1 2B 57 AE 24 CF 0B 04 82 CD 9B 37 CB 3F 28 04 DA A3 6F DF BE 24 50 CE CC CC 94 9A 8D 21 
3F 3F 9F CC E3 61 66 66 D6 34 3A 61 C1 D4 D4 94 AE 2F 2D FF 85 B3 3D 3D E2 94 64 5A E4 87 1F 7E 
D8 FE 1D AA 11 D2 D1 BB 6E DD 3A 19 1D BD 8F 1F 3F 66 37 76 B0 AE AE 8E 36 A2 8C C4 EB A6 CB 89 
37 34 34 FC F3 CF 3F 3F FC F0 03 69 5F 1E 8F E7 E4 E4 B4 76 ED 5A 3B 3B 3B 76 09 27 DA DA DA C6 
C6 C6 AE AE AE 47 8E 1C 79 F0 E0 41 59 59 59 42 42 82 64 8F 75 6E 6E AE BB BB 7B 7A 7A 3A 8B 9D 
B7 53 D3 A5 B9 DF BC 79 73 FB F6 6D 7A AF 46 4F 4F 6F C6 8C 19 AB 57 AF B6 B0 B0 90 11 E0 2A FB 
58 E8 DA B5 2B BB FC 07 D6 38 1C CE B4 69 D3 A6 4F 9F 4E 1E EE DF BF FF DC B9 73 1D F0 B9 B4 4B 
9E C7 E3 C9 9F 7A 8E 60 1A D4 83 8E 8E CE C4 89 13 CF 9E 3D 4B 56 48 4A 4B 4B 73 74 74 F4 F7 F7 
EF C8 49 28 A1 63 F0 78 BC F0 F0 F0 B9 73 E7 92 2B 87 B6 B6 F6 C2 85 0B E9 82 6A 91 91 91 7B F6 
EC D1 8C DB F1 9D 9C 96 96 D6 67 9F 7D 46 2E D2 C9 C9 C9 92 11 D5 DF 7F FF 4D 72 3C C6 8C 19 F3 
EE BB EF B6 FF B3 38 1C 8E 9B 9B 5B 5B 2F 9C 7D FA F4 A1 31 44 5E 5E 1E BB 9E 45 3A 6D 05 C3 36 
5D 52 BD 18 1B 1B 4F 9C 38 F1 A7 9F 7E 92 D1 D1 DB AB 57 2F 3A B1 34 19 3B C8 E2 83 CA CA CA E8 
24 E5 52 93 22 CB D6 A5 4B 97 41 83 06 05 07 07 1F 39 72 84 CF E7 8B 44 A2 2D 5B B6 38 3A 3A 92 
9B 21 ED C4 E1 70 F4 F5 F5 27 4E 9C 18 19 19 79 FF FE FD 75 EB D6 91 AF 90 50 28 DC BD 7B 77 67 
B8 A0 68 6B 6B 9B 9A 9A 1E 3A 74 28 2C 2C 8C C7 E3 3D 7F FE 7C F9 F2 E5 53 A7 4E 95 3D A9 85 B2 
8F 05 6D 6D 6D 3A 73 62 87 E9 D9 B3 E7 CA 95 2B C9 CF F5 8E B9 67 55 5B 5B 4B 87 DE 0E 1A 34 A8 
67 CF 9E 72 BE 11 C1 34 A8 13 A9 85 6A 83 82 82 82 82 82 3A C3 E9 0F 14 85 44 D2 AE AE AE 92 B7 
32 FB F6 ED BB 62 C5 0A DA 03 BA 67 CF 9E 36 AD 4D 05 AC 0D 1B 36 8C E4 AC 5F BB 76 8D DE FD 7C 
F9 F2 E5 95 2B 57 18 86 31 30 30 50 E0 58 05 16 17 4E 03 03 03 BA 7C DD DD BB 77 59 DC B2 A8 A9 
A9 91 9C 50 AC 6F DF BE 6D DD 43 27 64 66 66 96 93 93 23 6E 41 4E 4E 4E 42 42 C2 FA F5 EB 65 74 
F4 EA E8 E8 D0 89 1D EE DF BF CF 6E 96 B4 FC FC 7C 1A FF 8D 1A 35 AA AD B7 10 C9 CC 89 41 41 41 
24 46 CC CC CC FC EE BB EF 14 12 4F 53 FA FA FA FE FE FE 3F FE F8 23 79 78 FE FC F9 CE B3 A4 BC 
B6 B6 F6 E2 C5 8B 69 DD 2E 5C B8 E0 E5 E5 25 23 9E EE C8 63 A1 A6 A6 46 FE 75 D7 C5 62 31 1D 7B 
CA 62 8E 45 73 73 F3 8E 4C F6 A8 AC AC 2C 28 28 20 E5 DE BD 7B 37 9B 6D DF 2C 04 D3 A0 66 FA F6 
ED BB 69 D3 26 3A 28 2D 28 28 28 3C 3C 5C FE 03 1B 54 4E 6A A1 35 29 63 C6 8C F9 FC F3 CF 9B 26 
05 8E 19 33 86 9E 52 85 42 E1 AA 55 AB 3A 72 F2 D1 B7 56 9F 3E 7D 68 A6 07 9D 88 9D E6 B5 DB D8 
D8 7C F4 D1 47 0A FC 38 A9 0B E7 81 03 07 64 DF 82 E8 D3 A7 0F 0D 20 52 53 53 25 47 D4 C9 A9 A0 
A0 80 4E B4 AC A8 94 15 0D D0 AD 5B B7 E1 C3 87 93 72 5E 5E 5E 5A 5A 5A 5B F7 50 53 53 43 07 92 
5A 5A 5A D2 66 6A 13 0E 87 33 63 C6 0C 1A 50 66 66 66 FA FA FA B6 74 E0 97 97 97 93 35 B9 38 1C 
CE A6 4D 9B E4 FC 08 6D 6D ED 2F BF FC 92 CC 6A 5C 5C 5C 9C 9F 9F CF A2 9E 4A A2 AD AD ED E5 E5 
E5 E9 E9 49 1E 5E B8 70 61 D5 AA 55 CF 9E 3D 6B 76 63 65 1F 0B 1C 0E 87 E6 3C 3C 7B F6 4C FE 88 
B6 B4 B4 34 2B 2B 8B 94 59 4C D8 D7 F4 9E D5 E5 CB 97 DB BA 13 F9 15 14 14 D0 35 26 87 0C 19 22 
7F F2 0C 82 69 50 3F 26 26 26 CB 96 2D A3 DF F2 DD BB 77 63 BD 15 D5 CA DD FC E5 C8 00 00 20 00 
49 44 41 54 CB CB 0B 08 08 70 71 71 19 35 6A 54 AB 7D C6 3D 7A F4 60 B1 F6 0A 87 C3 59 B0 60 01 
5D E0 43 20 10 EC D8 B1 03 37 25 94 4D 4B 4B 6B DC B8 71 E4 58 4B 49 49 21 FF E1 57 AF 5E 25 01 
8D A2 72 3C 28 A9 0B 67 58 58 D8 5F 7F FD 25 63 7B 32 C2 8C 94 8B 8B 8B 4F 9C 38 D1 A6 5E AB FA 
FA FA B8 B8 38 3A A4 55 72 A2 65 18 3B 76 2C 5D 57 39 3A 3A BA A5 55 E5 1B 1A 1A 82 83 83 77 EE 
DC 29 B5 41 5A 5A DA 99 33 67 48 D9 C9 C9 89 75 32 BA B6 B6 F6 BC 79 F3 5C 5C 5C C8 43 19 07 7E 
F7 EE DD 69 C7 27 99 B6 5C CE 8F 90 CC 69 E9 6C F9 63 3A 3A 3A CB 96 2D A3 9D 47 32 66 08 55 F6 
B1 D0 AD 5B 37 FA BF D4 A6 A5 01 E9 3E CD CC CC D8 CD 3F 2B 75 CF 6A F3 E6 CD 2D 7D 1B DB A9 A1 
A1 21 21 21 81 4E D7 3D 6A D4 A8 36 E4 26 29 A3 42 00 CA E6 E2 E2 42 66 74 67 18 46 28 14 86 84 
84 94 94 94 A8 B6 4A 6F B3 86 86 86 93 27 4F FE F6 DB 6F 19 19 19 8F 1E 3D 6A 76 9B 96 9E 97 1F 
59 19 8B 5E 57 C2 C3 C3 0F 1E 3C D8 69 07 E0 6B 0C 33 33 33 1B 1B 1B 86 61 04 02 41 61 61 A1 48 
24 22 BF 97 14 9B E3 41 F5 EC D9 D3 C7 C7 47 F2 C2 29 FB 9B 63 6D 6D 4D 97 AD DE BF 7F FF AF BF 
FE 2A FF 57 22 35 35 F5 E0 C1 83 A4 6C 62 62 E2 EC EC 8C D1 CC D4 47 1F 7D E4 E8 E8 48 CA 89 89 
89 11 11 11 CD C6 70 25 25 25 FF FD EF 7F 97 2D 5B 66 62 62 B2 7A F5 6A D2 6F 5A 52 52 B2 7D FB 
76 12 94 98 98 98 4C 9B 36 8D DD 1A 22 44 EF DE BD FD FC FC 68 47 69 54 54 54 7C 7C 7C D3 56 EE 
DE BD 3B DD E6 D2 A5 4B F2 4F FB F3 EA D5 2B F9 43 C3 8E 67 64 64 B4 66 CD 1A DA 79 24 23 C9 4D 
D9 C7 02 9D 3C 31 3D 3D 5D CE FF DE AA AA 2A 32 1B 3D D3 C6 AC 09 29 23 47 8E 5C B2 64 09 29 27 
26 26 86 87 87 2B E3 67 CF FD FB F7 E9 2F 40 13 13 13 2B 2B 2B F9 DF 8B 60 1A D4 12 97 CB F5 F2 
F2 22 D7 78 86 61 E2 E3 E3 23 23 23 91 EC A1 2A 1C 0E 87 26 66 64 66 66 36 6D 08 B1 58 4C 6F CE 
B6 E7 94 3A 74 E8 50 6F 6F 6F 7A 5D 09 09 09 A1 F7 25 41 49 F4 F5 F5 C9 81 96 9D 9D 4D 32 A7 C9 
CC 1E 0A CF F1 A0 AC AC AC 24 2F 9C 01 01 01 D5 D5 D5 2D 6D DC AF 5F BF 19 33 66 90 B2 48 24 F2 
F3 F3 3B 77 EE 9C 3C 31 C4 D5 AB 57 7D 7C 7C E8 FA 7F 2E 2E 2E 4D D7 F8 78 9B 71 B9 DC D9 B3 67 
D3 F0 34 38 38 78 FB F6 ED 4D 3B 3B EF DF BF 4F 26 C1 20 C3 04 6D 6D 6D A3 A3 A3 FD FD FD E9 2A 
1B 1E 1E 1E EC 72 3C 24 49 E6 FF 88 44 A2 D0 D0 D0 A6 F9 18 1C 0E C7 DE DE 9E 9C 1C 8A 8B 8B 83 
82 82 E4 E9 61 11 8B C5 67 CE 9C 21 CB 74 F3 78 BC CE 39 CB EA 84 09 13 24 3B 8F 76 EE DC D9 6C 
B2 87 B2 8F 05 13 13 13 B2 32 9A 48 24 0A 0B 0B 93 E7 BF 37 35 35 F5 D7 5F 7F 25 65 53 53 53 D6 
37 B2 B4 B4 B4 DC DD DD E9 0D 8A B0 B0 B0 13 27 4E B0 DB 55 4B 44 22 D1 F6 ED DB 69 8E C7 17 5F 
7C D1 A6 F3 1B 82 69 50 57 86 86 86 2B 56 AC 90 4C F6 68 76 9D 36 E8 00 7D FA F4 F9 E0 83 0F 48 
F9 8F 3F FE B8 7F FF BE D4 06 64 CC 13 29 1B 1A 1A CA 5E 70 41 06 0E 87 F3 D5 57 5F 49 5E 57 7E 
FE F9 67 25 DD F2 03 82 C3 E1 38 39 39 19 18 18 30 0C 93 92 92 92 9C 9C 4C 3A A5 94 97 14 21 75 
E1 BC 7C F9 B2 8C FC 78 A9 F9 B3 84 42 E1 D7 5F 7F BD 6D DB 36 19 29 40 75 75 75 11 11 11 93 26 
4D A2 17 4E 1B 1B 9B 85 0B 17 AA 7C 62 DD CE 66 C4 88 11 DF 7D F7 1D 29 8B 44 A2 55 AB 56 79 7A 
7A 4A DD 28 B0 B3 B3 2B 2E 2E 4E 48 48 B0 B5 B5 65 18 26 37 37 F7 DB 6F BF 3D 70 E0 00 79 D5 D3 
D3 73 C1 82 05 ED EF EF 97 CA FF 11 08 04 FB F6 ED 6B 1A D9 9B 9A 9A D2 AF 4D 7C 7C BC 9B 9B DB 
CD 9B 37 65 44 93 75 75 75 47 8E 1C D9 B0 61 03 79 E8 E0 E0 30 6C D8 B0 76 56 55 19 A4 3A 8F E2 
E2 E2 62 62 62 9A FE 5D CA 3E 16 06 0F 1E 2C D9 81 B5 62 C5 0A 3A F1 45 53 62 B1 38 35 35 75 E5 
CA 95 24 DF 86 C7 E3 4D 9C 38 B1 6B D7 AE F2 FE CD 4D F4 EE DD FB FB EF BF A7 F7 AC FE F8 E3 0F 
D6 BB 6A AA B0 B0 D0 C3 C3 83 F6 CD F3 F9 FC 99 33 67 B6 29 1D 11 C1 34 A8 31 27 27 A7 39 73 E6 
90 B2 50 28 0C 0E 0E AE A8 A8 50 6D 95 DE 4E BA BA BA A3 46 8D 22 E5 CC CC CC 39 73 E6 5C B8 70 
E1 F5 EB D7 0C C3 54 55 55 9D 3D 7B 76 CE 9C 39 A4 EF 87 61 98 D1 A3 47 B7 67 8A 25 2E 97 EB EB 
EB 6B 6F 6F 4F 1E 26 26 26 62 46 17 65 33 32 32 22 77 3C CF 9C 39 13 14 14 C4 30 8C 81 81 C1 D8 
B1 63 95 97 14 21 79 E1 6C 55 CF 9E 3D 7F FE F9 67 9A FF 23 12 89 56 AC 58 61 6D 6D BD 73 E7 CE 
EC EC 6C 3A A3 DF EB D7 AF 1F 3C 78 B0 67 CF 1E 5B 5B DB 79 F3 E6 3D 7F FE 9C 3C CF E7 F3 37 6E 
DC D8 39 BB 24 55 4B 6A 00 1C C3 30 87 0F 1F 36 33 33 5B B6 6C D9 F5 EB D7 5F BE 7C 49 E2 39 2E 
97 3B 7A F4 68 1F 1F 1F 73 73 73 C9 B7 CF 9E 3D 7B C3 86 0D AC 7F 39 4B 91 CC FF 61 5A 98 3C 51 
57 57 77 D1 A2 45 74 9B 0B 17 2E 98 9B 9B 4F 9E 3C 39 2E 2E EE D1 A3 47 E4 8C C4 30 CC EB D7 AF 
1F 3D 7A 14 15 15 E5 E8 E8 48 BF 09 3C 1E 6F C6 8C 19 F2 4F 85 D6 C1 0C 0D 0D BD BC BC 24 6F CA 
35 3B 2B B6 52 8F 05 1D 1D 9D 59 B3 66 D1 3A 44 45 45 59 59 59 05 04 04 DC B9 73 87 EE B9 BE BE 
BE A4 A4 E4 C2 85 0B EE EE EE 9F 7F FE 39 8D D1 5D 5C 5C E8 32 11 AC 49 DE B3 6A BF FA FA FA B2 
B2 B2 D4 D4 D4 65 CB 96 99 9B 9B C7 C6 C6 D2 97 96 2C 59 32 72 E4 48 36 3B 6D 69 0E 1D 50 77 6A 
D4 BE 92 83 08 9B 2E DA D2 92 7B F7 EE 91 81 D8 C4 FE FD FB 1B 1B 1B 65 BF E5 D8 B1 63 0C C3 1C 
3B 76 AC DD 55 56 BD CE D3 BE 69 69 69 F2 84 3E 36 36 36 0F 1E 3C 68 FA 76 D2 28 0C C3 38 3B 3B 
97 95 95 B5 FA 71 49 49 49 F4 E3 78 3C 5E 74 74 B4 54 BB D3 DE A6 36 91 FF 8B D7 31 3A AC 7D E9 
7F 57 B3 FF FF 8D 8D 8D DB B6 6D 93 FC 8F 72 71 71 79 FE FC B9 D4 66 65 65 65 CE CE CE 64 83 A6 
4B 51 C8 7E B5 A9 37 6F DE 6C DE BC 59 AA 81 64 1C B6 77 EE DC A1 DD 66 F2 E3 F3 F9 7F FC F1 47 
AB 27 0D 25 51 6C FB D2 83 48 F6 D4 78 6D 55 5A 5A 4A 66 F7 6F 2B 1E 8F 17 1A 1A 5A 5B 5B DB 74 
9F D5 D5 D5 74 8D 9E A6 8B B6 B4 E4 CD 9B 37 01 01 01 74 FF F6 F6 F6 8F 1E 3D 92 DA A6 B1 B1 31 
3A 3A 9A C5 0A 26 9E 9E 9E 95 95 95 0A F8 FF 92 D0 52 FB B6 F5 58 20 2A 2B 2B E9 08 6C 86 61 DC 
DC DC C8 EF 99 A6 94 77 2C 34 7B 54 B6 CA D2 D2 F2 DE BD 7B CD EE B0 AD D7 FD A7 4F 9F D2 B9 71 
89 66 BF ED ED 99 93 40 FE 6F 02 D9 9E 94 D1 33 0D EA 6D E8 D0 A1 3F FC F0 03 7D B8 7B F7 EE CE 
33 51 E8 5B 45 F2 8E 70 4B 78 3C 9E A7 A7 A7 42 66 1F B3 B1 B1 91 BC 01 ED E7 E7 47 66 3E 06 65 
E0 70 38 63 C7 8E 25 99 1E C4 D8 B1 63 DF 7B EF 3D A5 7E A8 B6 B6 B6 BB BB BB D4 85 53 86 8F 3F 
FE 38 36 36 96 AE 1B 27 0F 27 27 A7 DF 7E FB ED F3 CF 3F C7 B8 43 19 7A F7 EE BD 67 CF 9E 0D 1B 
36 B4 35 42 15 89 44 DE DE DE 8B 16 2D 62 37 4D 75 53 DA DA DA 0B 16 2C 98 38 71 22 79 D8 EC B0 
48 32 9B 5E 58 58 58 9B 06 66 F8 F9 F9 05 07 07 2B AA 13 5D 49 C8 08 6C DA 79 14 19 19 79 E6 CC 
19 71 73 49 2C CA 3B 16 C8 CD 0A 3F 3F 3F F9 F7 6C 63 63 13 1E 1E 4E 67 86 69 A7 BE 7D FB FA FA 
FA 2A 6F 0A 4B D6 DF 04 04 D3 A0 DE 38 1C CE E4 C9 93 E9 59 23 33 33 33 3C 3C 9C DD E2 B7 D0 1E 
DA DA DA CB 96 2D 0B 0D 0D 6D E9 8A 6B 6C 6C 7C E2 C4 89 59 B3 66 29 24 70 91 9A 30 4B 28 14 6E 
DD BA 15 33 BA 28 8F B1 B1 31 ED EB 52 76 8E 07 D5 D6 0B E7 80 01 03 22 22 22 2E 5E BC 48 F2 77 
65 30 35 35 8D 8E 8E FE ED B7 DF 46 8C 18 D1 EE 6A 6A 3E 1D 1D 9D B5 6B D7 26 27 27 BB B9 B9 B5 
1A 52 4F 9A 34 69 EE DC B9 74 B3 C8 C8 48 47 47 C7 63 C7 8E 29 E4 B4 DC AF 5F 3F C9 21 C8 07 0F 
1E A4 F9 63 94 B6 B6 F6 9C 39 73 D2 D3 D3 25 AB D1 12 5B 5B DB 8B 17 2F 06 04 04 74 F2 48 9A 18 
3A 74 A8 64 9E C3 AE 5D BB 5A 9A 18 5B 79 C7 82 8E 8E 4E 40 40 C0 C5 8B 17 5B 4D DB E0 F1 78 AB 
56 AD 8A 8B 8B A3 49 80 0A 21 D9 93 A2 40 ED FC 26 20 98 06 B5 A7 AB AB BB 74 E9 52 7A C5 3D 7A 
F4 28 1D 48 0E 1D 89 CB E5 2E 5D BA F4 CE 9D 3B 5B B6 6C A1 CB 50 F3 F9 FC 19 33 66 C4 C6 C6 5E 
BF 7E 9D 2C A9 A0 A8 8F EB DD BB F7 FA F5 EB 69 87 47 7C 7C FC D6 AD 5B 95 BA 38 D6 DB EC DD 77 
DF 1D 33 66 0C 29 5B 59 59 91 41 FD 1D C0 C6 C6 66 C1 82 05 F2 6F DF A5 4B 17 07 07 87 A4 A4 A4 
7B F7 EE 85 84 84 7C F9 E5 97 74 5E 02 3E 9F 3F 79 F2 E4 90 90 90 BB 77 EF DE BC 79 D3 D5 D5 B5 
A5 F5 FF A0 29 0E 87 63 66 66 76 E4 C8 91 FB F7 EF C7 C6 C6 BA BB BB D3 A4 52 1E 8F 67 6B 6B EB 
EE EE 1E 1B 1B 5B 5C 5C 7C E6 CC 99 43 87 0E 25 25 25 4D 9A 34 89 6C 90 9B 9B 3B 7B F6 EC D3 A7 
4F 2B A4 26 E3 C6 8D 93 1C 82 BC 6D DB B6 66 A7 B6 30 34 34 3C 7C F8 70 7E 7E 7E 7C 7C BC A7 A7 
A7 BD BD 3D ED AB E6 F3 F9 5F 7C F1 C5 96 2D 5B EE DE BD FB D7 5F 7F 39 38 38 34 5D 25 AA 73 92 
1A 62 28 10 08 42 43 43 5B FA 95 A2 BC 63 81 EC F9 CA 95 2B D7 AF 5F DF B2 65 8B E4 9E 19 86 B1 
B2 B2 22 5F 86 FC FC FC CD 9B 37 F7 EE DD 9B ED 9F DB 3C F2 63 89 DE A0 68 0F 52 D5 83 07 0F 16 
16 16 26 25 25 B5 E7 9B F0 BF 0B 5B B3 77 0A 40 03 90 D8 05 ED 2B 29 3A 3A FA DB 6F BF 3D 76 EC 
D8 37 DF 7C A3 EA BA B4 17 DA 57 B3 A1 7D 35 9B 66 B7 6F 5D 5D DD E9 D3 A7 37 6D DA 94 95 95 E5 
E0 E0 10 19 19 29 99 29 F4 36 D0 EC F6 05 C9 F6 C5 4C 40 00 00 00 A0 60 5C 2E 77 D6 AC 59 53 A7 
4E BD 7A F5 6A 6D 6D ED DB 16 49 C3 5B 05 C1 34 00 00 00 28 05 97 CB B5 B3 B3 53 75 2D 00 94 4B 
3D F2 84 00 00 00 00 00 3A 21 04 D3 00 00 00 00 00 2C 21 98 06 00 00 00 00 60 09 C1 34 00 00 00 
00 00 4B 08 A6 01 00 00 00 00 58 C2 3C D3 1A 0E F3 5C 36 25 14 0A 1F 3C 78 30 70 E0 40 E5 2D 49 
DA 61 D0 BE 9A 0D ED AB D9 D0 BE 9A 0D ED AB D9 24 DB 17 C1 B4 86 C3 C1 AC D9 D0 BE 9A 0D ED AB 
D9 D0 BE 9A 0D ED AB D9 24 DB 17 69 1E 00 00 00 00 00 2C 21 98 06 00 00 00 00 60 09 C1 34 00 00 
00 00 00 4B 08 A6 01 00 00 00 00 58 42 30 0D 00 00 00 00 C0 12 82 69 00 00 00 00 00 96 10 4C 03 
00 00 00 00 B0 84 60 1A 00 00 00 00 80 25 04 D3 00 00 00 00 00 2C 21 98 06 00 00 00 00 60 09 C1 
34 00 00 00 00 00 4B 08 A6 01 00 00 00 00 58 42 30 0D 00 00 00 00 C0 12 82 69 00 00 00 00 00 96 
10 4C 03 00 00 00 00 B0 84 60 1A 00 00 00 00 80 25 04 D3 00 00 00 00 00 2C 21 98 06 00 00 00 00 
60 09 C1 34 00 00 00 00 00 4B 08 A6 01 00 00 00 00 58 42 30 0D 00 00 00 00 C0 12 82 69 00 00 00 
00 00 96 10 4C 03 00 00 00 00 B0 84 60 1A 00 00 00 00 80 25 04 D3 00 00 00 00 00 2C 21 98 06 00 
00 00 00 60 09 C1 34 00 00 00 00 00 4B 08 A6 01 00 00 00 00 58 42 30 0D 00 00 00 00 C0 12 82 69 
00 00 00 00 00 96 10 4C 03 00 00 00 00 B0 84 60 1A 00 00 00 00 80 25 8E AA 2B 00 00 00 00 00 A0 
7E C4 62 31 83 9E 69 00 00 00 00 00 D6 B4 C9 3F 24 B2 06 CD C3 E1 70 18 B4 AF E6 42 FB 6A 36 B4 
AF 66 43 FB 6A 36 B4 AF 66 23 ED 4B A0 67 1A 00 00 00 00 80 25 04 D3 00 00 00 00 00 2C 21 98 06 
00 00 00 00 60 09 C1 34 00 00 00 00 00 4B 08 A6 01 00 00 00 00 58 42 30 0D 00 00 00 00 C0 12 82 
69 00 00 00 00 00 96 10 4C 03 00 00 00 00 B0 84 60 1A 00 00 00 00 80 25 04 D3 00 00 00 00 00 2C 
21 98 06 00 00 00 00 60 09 C1 34 00 00 00 00 00 4B 08 A6 01 00 00 00 00 58 42 30 0D 00 00 00 00 
C0 12 82 69 00 00 00 00 00 96 10 4C 03 00 00 00 00 B0 84 60 1A 00 00 00 00 80 25 04 D3 00 00 00 
00 00 2C 21 98 06 00 00 00 00 60 09 C1 34 00 00 00 00 00 4B 08 A6 01 00 00 00 00 58 42 30 0D 00 
00 00 00 C0 12 82 69 00 00 00 00 00 96 10 4C 03 00 00 00 00 B0 84 60 1A 00 00 00 00 80 25 04 D3 
00 00 00 00 00 2C 21 98 06 00 00 00 00 60 09 C1 34 00 00 00 00 00 4B 08 A6 01 00 00 00 00 58 42 
30 0D 00 00 00 00 C0 12 82 69 00 00 00 00 00 96 10 4C 03 00 00 00 00 B0 84 60 1A 00 00 00 00 80 
25 04 D3 00 00 00 00 00 2C 21 98 06 00 00 00 00 60 09 C1 34 00 00 00 00 00 4B 08 A6 01 00 00 00 
00 58 42 30 0D 00 00 00 00 C0 12 82 69 68 B3 FA FA FA B4 B4 B4 80 80 80 89 13 27 1A 1A 1A 72 38 
1C 0E 87 63 68 68 38 71 E2 C4 80 80 80 B4 B4 B4 FA FA FA 66 DF 28 12 89 DC DC DC C8 F6 9F 7F FE 
79 59 59 99 EC 0F 7A F9 F2 E5 F4 E9 D3 39 FF DF F4 E9 D3 5F BE 7C 29 FB 2D 42 A1 D0 C6 C6 86 6C 
1F 18 18 28 16 8B 5B DA F2 F4 E9 D3 74 CF 56 56 56 0F 1E 3C 68 F5 0F 27 52 53 53 39 F2 B1 B6 B6 
9E 35 6B D6 BE 7D FB 8A 8A 8A 64 D4 04 E4 54 5F 5F 1F 18 18 C8 E1 70 16 2F 5E 5C 53 53 A3 EA EA 
40 BB 88 C5 E2 A2 A2 A2 3D 7B F6 4C 99 32 85 9E 46 46 8D 1A E5 E3 E3 93 94 94 54 57 57 A7 EA 0A 
82 02 94 97 97 C7 C4 C4 7C FD F5 D7 A4 89 F5 F5 F5 27 4C 98 10 1C 1C FC F0 E1 43 55 57 0D 40 09 
C4 A0 A1 14 DB BE 0D 0D 0D 17 2F 5E B4 B0 B0 90 FD 75 B2 B0 B0 B8 78 F1 62 43 43 83 D4 DB 1B 1B 
1B 03 02 02 C8 36 46 46 46 99 99 99 B2 3F 2E 33 33 D3 C8 C8 88 EE 56 9E B7 A4 A4 A4 F0 78 3C B2 
FD 85 0B 17 5A DA AC B2 B2 D2 DD DD 5D B2 CE C7 8E 1D 93 F3 3F 21 25 25 85 C5 21 E6 E6 E6 F6 F0 
E1 43 39 3F 42 7E 6F D5 F1 9B 94 94 C4 E7 F3 19 86 F1 F0 F0 A8 AE AE 56 75 75 3A 82 A6 B6 6F 79 
79 F9 AA 55 AB E8 A1 DA EC 39 24 35 35 B5 B1 B1 51 D5 35 55 2E 4D 6D 5F B1 58 FC E6 CD 9B 98 98 
18 63 63 E3 66 DB 97 C7 E3 F9 F9 F9 BD 7A F5 4A D5 D5 54 2E 0D 6E 5F 10 FF DF F6 45 CF 34 C8 AB 
AA AA CA DF DF DF D1 D1 31 2D 2D 4D F6 96 69 69 69 8E 8E 8E FE FE FE 55 55 55 92 CF 73 38 9C E1 
C3 87 93 72 5E 5E 5E 76 76 B6 EC FD 64 67 67 E7 E5 E5 D1 87 79 79 79 59 59 59 B2 DF 72 FD FA 75 
91 48 C4 30 CC 98 31 63 86 0C 19 D2 D2 66 85 85 85 02 81 40 F2 99 4B 97 2E 49 D5 56 B1 22 23 23 
A7 4F 9F DE EA 9F 0C 2D C9 CE CE 5E B5 6A 95 50 28 54 75 45 A0 BD 4A 4A 4A E6 CD 9B B7 65 CB 16 
72 A8 36 2B 2D 2D CD D5 D5 35 2E 2E 4E 8C 5B 3A 6A A8 BE BE 7E DB B6 6D AE AE AE B9 B9 B9 CD 6E 
20 12 89 82 82 82 E6 CF 9F 5F 52 52 D2 C1 75 03 50 06 04 D3 20 97 FA FA FA 5D BB 76 05 05 05 C9 
FF 96 A0 A0 A0 D5 AB 57 4B DD 8E 37 34 34 A4 9D CD D9 D9 D9 32 AE 94 0D 0D 0D 99 99 99 A4 3C 72 
E4 48 52 48 4F 4F 7F FD FA 75 4B 6F A9 A9 A9 A1 E7 EE C1 83 07 EB E9 E9 35 BB 99 58 2C 3E 7F FE 
3C 89 6B 17 2C 58 30 66 CC 18 86 61 CE 9F 3F 7F F7 EE 5D 39 FF 34 76 04 02 C1 8F 3F FE F8 EC D9 
33 A5 7E 8A 46 CA CD CD 5D B8 70 A1 D4 EF 1F 50 47 55 55 55 1B 36 6C 88 8F 8F 6F 75 4B A1 50 B8 
7C F9 F2 F4 F4 F4 0E A8 15 28 D6 A9 53 A7 36 6E DC D8 EA 66 27 4F 9E DC BA 75 2B 52 7A 40 03 20 
98 06 B9 DC BC 79 73 E7 CE 9D F4 A1 B3 B3 73 7C 7C FC D3 A7 4F DF BC 79 43 EE 71 BC 79 F3 E6 E9 
D3 A7 F1 F1 F1 CE CE CE 74 B3 A3 47 8F 5E B8 70 41 72 3F 03 06 0C A0 1D C6 77 EF DE 7D F5 EA 55 
4B 9F 58 51 51 91 91 91 C1 30 8C 99 99 99 87 87 07 B9 23 9C 91 91 21 23 D3 BA A2 A2 82 06 D3 23 
47 8E 6C E9 26 F2 8B 17 2F 68 AA C6 E4 C9 93 47 8F 1E CD 30 4C 71 71 71 42 42 42 43 43 83 AC FF 
85 26 52 52 52 64 DC 03 12 89 44 C9 C9 C9 B3 66 CD A2 DB C7 C5 C5 9D 39 73 A6 4D 1F F1 96 13 8B 
C5 A9 A9 A9 5F 7F FD 75 6A 6A AA AA EB 02 0A 90 9A 9A 1A 15 15 45 CA 7A 7A 7A 3F FF FC 73 5E 5E 
5E 5D 5D 9D 58 2C 6E 68 68 78 FC F8 71 70 70 30 FD 19 2C 14 0A 77 EF DE AD D4 5B 46 A0 70 C5 C5 
C5 87 0E 1D 22 B7 1D 78 3C 9E 97 97 57 66 66 26 6D E2 7F FE F9 E7 87 1F 7E A0 27 E7 98 98 18 DA 
69 02 A0 F6 94 98 54 02 2A A5 90 F6 AD AF AF 5F B3 66 0D D9 15 8F C7 0B 0D 0D AD AD AD 6D 69 E3 
DA DA DA 83 07 0F D2 73 A5 8B 8B CB F3 E7 CF E9 AB 75 75 75 BE BE BE E4 25 73 73 F3 BC BC BC 96 
F6 73 E3 C6 0D 03 03 03 86 61 66 CF 9E 9D 93 93 63 67 67 47 3E 5D 46 FC 7A F5 EA 55 F2 B9 B2 37 
BB 74 E9 12 D9 6C CC 98 31 85 85 85 BF FE FA 2B A9 8F A5 A5 65 41 41 41 AB FF 1B 92 39 D3 B2 83 
69 A2 BA BA 7A FD FA F5 F4 2D D3 A6 4D 7B F1 E2 45 AB EF 92 93 66 1F BF B5 B5 B5 BB 76 ED 6A 7A 
87 01 39 D3 6A AA B6 B6 D6 DB DB 9B 1E 6E 37 6E DC 68 76 B3 1B 37 6E 58 5A 5A 92 CD E4 19 29 A1 
BE 34 AC 7D 09 7A 46 E5 F1 78 D1 D1 D1 4D 13 DF 1B 1B 1B A3 A3 A3 E9 35 22 20 20 40 53 93 E3 35 
B2 7D 9B B5 61 C3 86 B7 ED E4 2C 46 CE 34 B4 D5 AB 57 AF 6E DF BE 4D CA AE AE AE 0B 16 2C E0 72 
B9 2D 6D CC E5 72 E7 CC 99 B3 72 E5 4A F2 F0 D2 A5 4B F7 EE DD A3 AF 76 ED DA 75 C4 88 11 A4 9C 
9E 9E 2E 63 0E 8D 1B 37 6E 14 17 17 33 0C 33 64 C8 10 43 43 43 92 E9 21 12 89 AE 5F BF DE D2 5B 
32 33 33 49 77 88 B9 B9 F9 C0 81 03 9B DD A6 A1 A1 E1 CF 3F FF 24 9B 99 9A 9A F6 E9 D3 67 E4 C8 
91 E4 CA 2D 10 08 AE 5C B9 D2 D2 CE 59 EB DE BD FB 82 05 0B EC ED ED C9 C3 DC DC 5C F2 77 81 0C 
8D 8D 8D 37 6E DC 98 36 6D 9A 97 97 D7 F3 E7 CF 19 86 B1 B4 B4 9C 30 61 82 AA EB 05 ED F2 F4 E9 
D3 1B 37 6E 90 F2 FC F9 F3 47 8D 1A D5 EC 66 E6 E6 E6 F4 04 22 CF E0 0A E8 3C 5E BF 7E 4D BB 1B 
BE FA EA AB 29 53 A6 70 38 1C A9 6D 38 1C CE 94 29 53 BE FA EA 2B F2 50 28 14 62 72 1E 50 77 08 
A6 A1 75 E5 E5 E5 4F 9F 3E 25 65 5B 5B DB EE DD BB CB DE 5E 5B 5B DB C5 C5 C5 C4 C4 84 61 18 91 
48 74 E7 CE 1D C9 57 87 0C 19 42 FB 24 A4 5E A2 6A 6A 6A 48 8E 07 C3 30 96 96 96 5C 2E D7 DC DC 
9C 3C CC C8 C8 68 76 DC D2 EB D7 AF 25 73 3C 7A F5 EA D5 EC 9E 1F 3E 7C F8 D7 5F 7F 91 B2 85 85 
45 F7 EE DD FB F7 EF 4F D2 A6 19 A5 0D 43 7C FF FD F7 C7 8F 1F 4F CA 59 59 59 E5 E5 E5 0A FF 08 
0D F3 CB 2F BF 58 58 58 24 24 24 90 87 2E 2E 2E FF F9 CF 7F 68 33 81 9A 2A 2B 2B A3 BF 9F 87 0D 
1B D6 34 CC A2 AC AC AC C8 CD 28 86 61 0A 0A 0A 3A A0 6E A0 10 5D BB 76 DD BE 7D 3B E9 AB 8B 88 
88 D0 D1 D1 69 76 33 1D 1D 9D 41 83 06 91 72 71 71 31 D2 A6 41 DD 21 98 86 D6 BD FB EE BB 3D 7B 
F6 24 65 39 B3 8A 3F F8 E0 83 8F 3F FE 98 94 4B 4B 4B 25 5F FA F0 C3 0F 69 64 7C EF DE BD EA EA 
EA A6 6F 2F 2D 2D 25 13 77 D0 49 39 4C 4D 4D C9 C8 C5 DB B7 6F 3F 79 F2 A4 E9 5B 5E BE 7C 49 E7 
FA 30 37 37 EF DA B5 6B B3 15 CB C8 C8 20 E3 D8 4C 4C 4C AC AC AC 18 86 E9 DA B5 EB E7 9F 7F 4E 
5E 55 D2 30 44 0E 87 23 D9 53 5E 58 58 A8 F0 8F D0 30 F4 E2 AA A7 A7 B7 6B D7 AE D8 D8 58 32 29 
1E A8 35 73 73 F3 27 4F 9E 90 48 CB C6 C6 46 C6 96 5C 2E 97 DE FE 6A 69 DE 7A D0 0C 7C 3E BF D5 
0E 1A 80 4E 0E C1 34 B4 AE 5B B7 6E 24 7D 99 61 98 3F FF FC 53 C6 A8 41 EA DD 77 DF 3D 79 F2 24 
B9 6A FA FB FB 4B BE F4 DE 7B EF 7D F4 D1 47 A4 9C 9F 9F FF E2 C5 8B A6 6F BF 7F FF 3E C9 B8 20 
99 18 8C C4 C8 C5 CC CC CC 66 A7 5B 7A F8 F0 21 89 83 8D 8C 8C 4C 4D 4D 9B AD 55 55 55 D5 EF BF 
FF 4E CA 8E 8E 8E B4 1A 9F 7C F2 89 83 83 03 C3 76 18 62 5B 91 BF 08 64 E3 F1 78 AB 56 AD BA 73 
E7 CE 92 25 4B 64 A4 15 81 46 6A 6C 6C A4 87 21 ED C2 04 8D 41 C7 97 33 0C 33 6A D4 A8 6E DD BA 
A9 B6 3E 00 ED 84 60 1A 5A C7 E3 F1 E8 1C 1D 91 91 91 4B 97 2E 25 03 F5 D8 ED AD 47 8F 1E C3 86 
0D 23 E5 F4 F4 F4 A6 4B 61 89 C5 62 3A 09 DA C8 91 23 49 A7 85 AE AE 2E 9D A3 FA DA B5 6B 4D E3 
DD 9C 9C 1C 92 8B 6C 66 66 D6 52 2F E6 3F FF FC 43 27 85 18 37 6E 1C 0D D1 FA F5 EB 37 6E DC 38 
52 BE 70 E1 82 C2 57 E7 6A 68 68 A0 1D DE 3C 1E 4F C6 5A 15 40 D8 DA DA DE B9 73 67 F3 E6 CD F4 
57 1C BC 55 E8 6F 63 03 03 83 A1 43 87 AA BA 3A A0 48 75 75 75 7B F7 EE 8D 8B 8B 63 18 C6 DE DE 
1E 63 21 40 03 20 98 06 B9 7C F1 C5 17 D3 A7 4F 27 E5 C8 C8 C8 C1 83 07 4F 9E 3C 79 DF BE 7D 85 
85 85 2C 6E C2 7E F2 C9 27 A4 20 12 89 9A CE 8B F4 EA D5 2B F2 A4 81 81 01 99 B7 8E 61 18 2D 2D 
2D 92 95 C1 30 4C 46 46 46 45 45 85 E4 5B 5E BF 7E 4D E7 A3 35 32 32 7A E7 9D 77 9A 7E A8 58 2C 
BE 74 E9 12 59 05 C6 CE CE 8E EE 8D 61 18 0E 87 E3 E4 E4 44 E2 36 81 40 40 93 AA 15 A5 A8 A8 E8 
EF BF FF 26 65 53 53 53 04 88 AD B2 B3 B3 FB F0 C3 0F 55 5D 0B 50 8D 86 86 86 F8 F8 78 F2 DB D8 
CA CA 0A 3D D3 9A 41 2C 16 97 97 97 9F 39 73 66 CA 94 29 7E 7E 7E 0C C3 18 1B 1B AF 5F BF BE 7F 
FF FE AA AE 1A 40 7B 21 98 06 B9 F4 EC D9 73 EB D6 AD 2E 2E 2E F4 99 84 84 84 C5 8B 17 0F 1C 38 
50 4F 4F EF FF B1 77 EF 01 31 E5 FF FF C0 CF 54 5F 49 26 5B 2E 29 D6 C4 6E 92 65 13 31 A9 48 14 
ED DA 95 F6 83 A5 DD 88 8F 4B 72 DB D6 66 29 7C 7C 64 73 5B F7 E4 BA 2E 11 D6 E5 D3 66 B3 4B A2 
52 13 89 65 36 D4 94 AD 06 A9 74 B1 1A 49 4C CD EF 8F F7 F7 F3 FE 9D EF 4C 4D D3 68 9A 9A 9E 8F 
7F 9C 33 73 E6 78 4F 67 E6 CC EB BC CF EB FD 7A BB BB BB 87 86 86 0A 04 82 17 2F 5E A8 B2 B7 5E 
BD 7A D9 D9 D9 91 65 91 48 24 37 0F 8B 58 2C 26 C1 B4 5C 1F B3 8D 8D 0D 79 95 50 28 94 9B 09 AF 
A2 A2 82 0E F9 77 74 74 D4 D7 D7 57 FC 4F CB CA CA 2E 5F BE 4C 96 47 8C 18 61 6E 6E CE 7E D6 C6 
C6 86 26 71 A6 A4 A4 34 E1 30 C4 F2 F2 F2 B0 B0 30 DA 23 EE E0 E0 D0 BD 7B F7 A6 DA 39 80 EE 49 
49 49 89 8C 8C 24 CB FF F8 C7 3F E8 80 0D 68 A5 5E BD 7A 35 67 CE 1C 3D 3D BD 2E 5D BA 78 79 79 
5D BA 74 89 61 98 29 53 A6 FC F6 DB 6F 23 47 8E D4 76 EB 00 9A 00 82 69 50 15 8F C7 3B 76 EC D8 
D6 AD 5B E5 EA FE 4A 24 92 2B 57 AE AC 5E BD DA C5 C5 E5 BD F7 DE 73 74 74 DC B1 63 47 41 41 81 
92 5D 75 EF DE 9D 3D 0F A2 5C 12 76 46 46 06 E9 3F B6 B7 B7 67 FF 8E 5A 5A 5A 92 4C 8F C2 C2 42 
5A 60 8B 78 FA F4 E9 5F 7F FD C5 30 8C 9D 9D 9D 8D 8D 4D 9D FF A9 50 28 24 11 2D 97 CB 75 75 75 
95 0B B8 3B 75 EA 44 D2 A6 99 26 1A 86 F8 E6 CD 9B BC BC BC A3 47 8F 7A 7A 7A 1E 38 70 80 3C 68 
61 61 F1 8F 7F FC 03 19 C0 00 F5 61 CF 1B 3F 7D FA F4 CF 3F FF 5C DB 2D 82 77 55 55 55 F5 F8 F1 
63 F6 23 66 66 66 86 86 86 8F 1E 3D C2 E8 D2 D6 25 2A 2A 8A 53 97 D5 AB 57 93 0D F6 ED DB D7 A1 
43 07 C5 0D 42 43 43 B5 DB 72 4D 43 30 0D 8D 60 6C 6C 1C 18 18 98 97 97 77 F2 E4 C9 89 13 27 D6 
99 FB 9B 96 96 F6 CD 37 DF D8 DA DA 2E 5F BE BC BE A9 B3 3B 76 EC 48 83 E9 BF FE FA 8B 5D 9D 83 
9D B0 21 D7 C7 CC E5 72 E9 BC E2 77 EE DC 61 97 26 CD CC CC 24 F1 F7 C7 1F 7F 6C 69 69 A9 F8 3F 
B2 CB 4B BB BB BB D7 59 E0 D6 C5 C5 85 94 F3 53 7D 18 A2 8B 8B 4B 9D 67 16 0E 87 63 68 68 D8 A7 
4F 1F 3F 3F BF F4 F4 74 BA FD CC 99 33 51 DF 0D A0 3E 05 05 05 2B 56 AC 20 43 26 F8 7C FE F2 E5 
CB 4D 4C 4C B4 DD 28 78 57 E5 E5 E5 26 26 26 21 21 21 1B 36 6C 08 08 08 B0 B1 B1 29 2F 2F 3F 76 
EC 98 9B 9B DB AC 59 B3 68 DD 55 80 D6 0B C1 34 34 9A 89 89 C9 D4 A9 53 A3 A3 A3 4B 4B 4B EF DC 
B9 B3 77 EF DE C9 93 27 2B 76 57 6F DC B8 D1 DB DB BB CE 2E 5E 7D 7D 7D 9A E6 91 93 93 C3 2E 15 
47 F6 C9 30 8C B5 B5 B5 95 95 95 DC 0B 87 0D 1B 46 22 F8 8C 8C 0C 5A 71 AF A6 A6 86 26 5E D7 37 
8B 38 BB BC 34 E9 41 57 DC A6 4F 9F 3E F4 9E A3 26 86 21 FA FA FA 7E F3 CD 37 06 06 06 4D BB 5B 
00 DD 20 16 8B E7 CD 9B 17 13 13 C3 30 0C 8F C7 DB B8 71 23 B9 B8 85 D6 CE DA DA FA F4 E9 D3 EB 
D6 AD FB FE FB EF 77 EF DE 7D EF DE BD D8 D8 58 72 0B F1 D8 B1 63 FE FE FE C5 C5 C5 DA 6E 23 40 
53 68 DE 29 18 A1 F9 34 DB F1 AD A9 A9 29 28 28 88 8A 8A 92 EB B1 76 76 76 CE CB CB 53 DC 9E CE 
16 CE 30 CC BF FE F5 2F 3A 9D 6C 4A 4A 0A 79 79 9D D3 6E 17 14 14 D0 A9 1C E2 E2 E2 C8 83 7F FF 
FD F7 A4 49 93 18 A5 B3 88 1F 3F 7E BC B1 5F 8A 83 07 0F D6 B9 2B F6 74 E2 2A 32 33 33 DB BA 75 
EB CB 97 2F D5 FB DB 2A D1 A6 BE BF 6D 70 C6 DA B6 73 7C EF DD BB 47 07 2D F0 78 BC 73 E7 CE E9 
EA 14 D3 6C 6D E7 F8 2A 4A 4C 4C A4 43 62 B6 6F DF AE 93 87 BB ED 1C DF 36 78 72 96 B5 B5 E9 C4 
AB AA AA 12 13 13 D7 AC 59 33 7E FC 78 2B 2B 2B 72 0B DE CA CA 6A FC F8 F1 A1 A1 A1 19 19 19 C8 
D9 6A 12 7A 7A 7A 96 96 96 3E 3E 3E D1 D1 D1 F7 EE DD 9B 3B 77 2E 79 5C 20 10 1C 3A 74 48 31 65 
A2 57 AF 5E 74 56 97 FB F7 EF D3 B4 E9 9B 37 6F 92 64 0C 3B 3B 3B C5 3B BC 5D BA 74 A1 99 1E 74 
F6 C4 C2 C2 42 52 79 BA BE 59 C4 2B 2B 2B E3 E3 E3 1B FB 8E 92 92 92 EA 9C 6A 51 45 3C 1E CF DD 
DD 3D 28 28 28 36 36 36 2F 2F 2F 30 30 B0 BE C9 C0 00 DA 32 99 4C 26 10 08 BE FA EA 2B 32 A4 81 
C7 E3 ED D9 B3 C7 DB DB 5B C9 FC 88 A0 03 46 8E 1C B9 78 F1 62 B2 1C 1B 1B 8B 64 0F 68 D5 74 F9 
8E 73 49 49 C9 81 03 07 F6 EF DF 2F 57 F9 81 61 18 B1 58 2C 16 8B 7F FB ED B7 D5 AB 57 0F 1D 3A 
34 2C 2C 6C F4 E8 D1 7A 7A BA 7F 69 D1 3C 7A F5 EA B5 75 EB 56 03 03 83 88 88 08 86 61 AE 5C B9 
F2 CF 7F FE 53 AE F6 33 97 CB ED DB B7 2F 89 71 F3 F2 F2 4A 4A 4A 3A 75 EA 24 91 48 D8 B3 88 2B 
FE 9A B6 6B D7 6E D0 A0 41 64 99 CC 9E D8 A1 43 87 EC EC 6C 32 F7 61 7D B3 88 B3 CB 4B AB 2E 3E 
3E 3E 33 33 73 D8 B0 61 4A B6 49 49 49 51 3E 91 1B 00 28 51 5B 5B 7B EE DC B9 A0 A0 20 72 96 B6 
B1 B1 D9 BB 77 AF AB AB 2B 22 69 9D C7 E1 70 DC DD DD AD AD AD 73 72 72 D2 D2 D2 C4 62 31 6A 86 
42 EB A5 9B E1 63 6D 6D ED 85 0B 17 46 8C 18 11 12 12 A2 18 49 CB 49 4F 4F F7 F0 F0 58 B4 68 51 
79 79 79 F3 34 AF 75 11 89 44 83 06 0D 22 3D FA 3F FF FC B3 8A AF 32 36 36 F6 F1 F1 A1 F9 CD A4 
64 2C 5B FB F6 ED E9 24 2C B7 6F DF CE CB CB 63 18 E6 E9 D3 A7 7F FE F9 27 C3 9A 45 5C D1 47 1F 
7D 44 CE B9 0F 1E 3C 28 29 29 91 C9 64 E4 25 0C C3 0C 1A 34 48 71 16 71 19 AB BC 74 A3 34 CF 6C 
88 00 6D 56 79 79 F9 F7 DF 7F 3F 65 CA 14 72 96 76 76 76 3E 77 EE DC A8 51 A3 10 49 B7 11 86 86 
86 1D 3A 74 60 18 46 22 91 D0 31 30 00 AD 91 0E 06 D3 52 A9 34 22 22 62 DA B4 69 75 4E 3A 5D 9F 
88 88 08 0C 83 A8 93 99 99 59 D7 AE 5D C9 B2 50 28 54 3D B8 EC D2 A5 0B 99 6D 41 22 91 D4 F9 2A 
F6 E8 22 92 B3 21 12 89 C8 50 42 3A 8B B8 22 1E 8F 47 06 2F 92 18 FD E5 CB 97 D9 D9 D9 0C C3 58 
58 58 D0 BC 11 36 76 79 69 3F 3F BF 06 13 97 CB CB CB 69 39 6D 4D 0C 43 04 00 86 61 72 72 72 A6 
4D 9B F6 E3 8F 3F 92 55 5F 5F DF B3 67 CF D6 F9 15 86 B6 80 5D 9D 09 A0 D5 D1 B5 60 5A 2A 95 6E 
DB B6 2D 38 38 58 8D 6C D7 33 67 CE AC 5D BB B6 09 67 EB D0 0D 1D 3B 76 FC E0 83 0F C8 F2 D5 AB 
57 55 0F 2E 5F BC 78 A1 BC B3 81 C7 E3 D1 3A 71 0F 1F 3E AC AA AA FA E3 8F 3F C8 2A 9D 45 5C 91 
A9 A9 29 49 9B 96 48 24 D9 D9 D9 C5 C5 C5 0F 1E 3C 60 EA 9F 45 9C 96 97 66 18 C6 C5 C5 A5 C1 C4 
65 53 53 53 3A 77 BA 26 66 43 04 80 7B F7 EE F9 FA FA C6 C5 C5 31 0C C3 E5 72 43 43 43 F7 ED DB 
87 C9 8C 74 C0 C3 87 0F 1D 1C 1C C8 9D CC 9F 7E FA 49 F9 C6 8F 1E 3D A2 85 98 7A F6 EC A9 F9 D6 
01 68 8A AE 05 D3 17 2E 5C 08 0D 0D 95 8B A4 47 8C 18 11 11 11 91 9B 9B 5B 5D 5D 2D 93 C9 6A 6A 
6A 9E 3D 7B F6 9F FF FC 67 C4 88 11 72 2F 3F 76 EC D8 AF BF FE DA 8C ED 6D 05 8C 8C 8C E8 1F 2A 
2D 2D ED C7 1F 7F 54 E5 7A A3 BA BA FA F4 E9 D3 24 BB C3 CE CE AE CE 54 66 33 33 33 1A A6 67 67 
67 3F 79 F2 84 D4 D1 63 CF 22 AE 88 3D AF 78 6E 6E 6E 41 41 01 A9 4B 2D 37 C3 0B F1 E6 CD 9B 0B 
17 2E D0 11 8D 2E 2E 2E 0D B6 9C 61 15 9C 66 DE 79 18 22 00 C8 C9 CC CC 9C 3D 7B 36 29 26 6D 66 
66 B6 77 EF DE E0 E0 E0 FA 2E 9E A1 75 E9 DA B5 2B 1D 05 7E E1 C2 85 E7 CF 9F D7 B7 65 65 65 E5 
99 33 67 C8 B2 93 93 13 82 69 68 D5 74 2A 98 CE CF CF DF BC 79 33 3B F4 E1 72 B9 07 0F 1E BC 7C 
F9 F2 FC F9 F3 7B F7 EE 4D 12 6A F5 F4 F4 BA 76 ED EA ED ED 7D F9 F2 E5 9D 3B 77 B2 EB B8 49 24 
92 9F 7E FA 49 31 C1 B7 8D 1B 35 6A 94 9B 9B 1B 59 8E 88 88 98 33 67 0E BB 32 B4 A2 CA CA CA 4D 
9B 36 ED DF BF 9F AC BA BA BA 2A 56 8C 66 18 A6 63 C7 8E 34 31 BA B8 B8 58 28 14 92 CC 9C FA FA 
98 29 3A AF 78 41 41 C1 B5 6B D7 C8 83 75 CE 22 5E 50 50 90 9A 9A AA BC 19 8A D8 05 A7 C9 30 44 
55 5E 05 00 67 75 62 53 00 00 20 00 49 44 41 54 0D AA A8 A8 D8 B0 61 03 89 A4 79 3C DE F1 E3 C7 
A7 4D 9B 86 C1 DF 3A C3 C4 C4 64 F8 F0 E1 64 39 3A 3A 7A FF FE FD 75 D6 CB 92 4A A5 E1 E1 E1 74 
6A 58 07 07 07 DC 97 00 5D A0 D9 5A 7C CD 42 2A 95 86 85 85 C9 BD AF 0D 1B 36 BC 7D FB 56 C9 AB 
6A 6A 6A F6 EE DD 2B F7 AA 98 98 98 66 6B B6 A6 35 D5 F1 3D 79 F2 24 FB AA 83 CB E5 4E 9F 3E FD 
D2 A5 4B 45 45 45 F4 2F FC EA D5 AB DC DC DC ED DB B7 0F 1C 38 90 6E C9 E3 F1 EA AB FD 2C 93 C9 
C8 04 0D C4 97 5F 7E 49 16 56 AC 58 21 95 4A 95 34 A6 A2 A2 C2 D7 D7 97 61 18 3B 3B BB B1 63 C7 
92 85 AC AC 2C C5 2D D9 E5 A5 CF 9D 3B A7 FA FB 3D 77 EE 1C 7D E1 AA 55 AB D8 ED 61 D7 99 56 F2 
D6 9A 87 CE 7C 7F 55 D1 06 4B 99 EA D8 F1 AD AD AD A5 D7 D8 5C 2E 37 2A 2A 4A 27 AB 0B AB 4E C7 
8E 2F 91 95 95 45 E7 E4 E2 72 B9 0B 17 2E 14 0A 85 F4 0B 2B 91 48 92 93 93 A7 4D 9B C6 FE 8D 48 
4F 4F D7 6E 9B 35 44 27 8F 2F 50 EC E3 AB 3B C1 74 6E 6E 2E 9F CF 67 C7 C4 01 01 01 AA 4C 93 C1 
1E 70 46 04 06 06 92 84 10 1D D0 54 C7 F7 ED DB B7 1B 36 6C 60 1A 4F F9 F5 8C 50 28 A4 F3 8A 53 
AA 5C CC 6C DD BA 95 FD 12 5F 5F DF 8A 8A 0A B9 6D 5E BE 7C E9 E7 E7 47 36 70 72 72 CA CF CF 57 
FD FD E6 E7 E7 D3 7C 6E 3E 9F 9F 9B 9B 4B 9F 42 30 AD 2D 08 A6 5B BB A7 4F 9F BA BB BB 37 F6 1C 
32 6E DC B8 D2 D2 52 6D B7 5D 23 74 EC F8 12 B5 B5 B5 51 51 51 75 CE 44 AB 48 B7 AF A9 74 F2 F8 
02 C5 3E BE BA 73 73 ED EA D5 AB E4 D6 21 61 6B 6B 3B 6F DE 3C 55 A6 C9 30 35 35 1D 3F 7E 3C FB 
91 8C 8C 8C 17 2F 5E 34 7D 13 5B 33 03 03 83 C5 8B 17 87 86 86 AA 78 8A 64 18 86 CB E5 EE DA B5 
6B E9 D2 A5 4A 26 D0 7E FF FD F7 E5 4A E0 D5 39 8B B8 22 3A AF 38 51 E7 2C E2 59 59 59 97 2E 5D 
22 CB AE AE AE 8D CA C9 EB D9 B3 E7 98 31 63 C8 32 86 21 02 34 89 F4 F4 74 35 A6 4F 82 D6 85 C3 
E1 4C 99 32 65 D5 AA 55 0D FE 58 70 B9 DC B0 B0 B0 29 53 A6 A0 18 22 B4 76 3A 12 4C 4B 24 92 A4 
A4 24 F6 23 93 26 4D 52 BD CA 92 8B 8B 0B BD 2D C5 30 4C 71 71 71 59 59 59 53 B6 4F 27 18 19 19 
85 84 84 24 26 26 CA 75 E4 D7 C9 DB DB 3B 31 31 71 C1 82 05 4A 22 69 86 61 8C 8D 8D E5 82 E9 06 
13 A6 89 DE BD 7B 0F 19 32 84 AE B2 97 09 99 4C 96 94 94 44 D2 DF B9 5C EE 98 31 63 14 33 AA 95 
D0 D7 D7 77 75 75 A5 3F 06 17 2F 5E C4 F5 15 C0 BB 90 C9 64 B4 5C 0F E8 36 03 03 83 A5 4B 97 1E 
3A 74 C8 C6 C6 A6 BE 6D 86 0E 1D FA CB 2F BF 34 F8 1B 01 D0 2A E8 C8 87 38 2F 2F EF C6 8D 1B 74 
D5 D6 D6 F6 CB 2F BF 54 3D 78 B2 B1 B1 B9 7B F7 AE 66 9A A6 53 38 1C CE E0 C1 83 CF 9D 3B F7 E4 
C9 93 E4 E4 E4 CB 97 2F FF F5 D7 5F 77 EF DE 25 83 3E 6D 6C 6C 6C 6D 6D C7 8E 1D FB E9 A7 9F BE 
FF FE FB AA 0C 2A 62 CF 68 48 D4 39 8B B8 22 33 33 B3 FE FD FB 27 26 26 32 0C E3 E4 E4 A4 18 7F 
17 15 15 FD FE FB EF 64 99 CF E7 F7 EF DF 5F B5 B7 F8 FF 0D 1E 3C D8 DD DD 3D 3A 3A 9A 61 18 81 
40 20 12 89 94 CF 86 08 00 4A BC 7E FD 1A 53 46 B7 1D 7A 7A 7A 93 26 4D FA E4 93 4F 12 13 13 CF 
9E 3D 7B FD FA 75 32 BE DC DE DE 7E C4 88 11 DE DE DE C3 87 0F 37 34 34 D4 76 33 01 9A C6 FF DE 
5B A1 C9 1F AD D4 F9 F3 E7 BD BC BC E8 AA AF AF EF EE DD BB 55 4F 48 D0 61 E4 F6 59 6B 3F BE 50 
1F 1C 5F DD 86 E3 AB DB 70 7C 75 1B 8E AF 6E 63 1F 5F 1D 49 F3 A0 85 DF 89 3A 33 68 01 00 00 00 
00 9A 96 2E 04 D3 AF 5E BD 92 9B 96 6F C0 80 01 DA 6A 0C 00 00 00 00 B4 1D BA 90 33 5D 55 55 F5 
F8 F1 63 BA 6A 6D 6D 6D 6E 6E 2E B7 41 5A 5A 5A 74 74 F4 CD 9B 37 49 6A B5 99 99 D9 D0 A1 43 9D 
9D 9D 3D 3D 3D ED ED ED 31 00 02 00 00 00 00 D4 A0 0B 41 64 69 69 29 7B 5C 8B 89 89 49 87 0E 1D 
C8 72 65 65 E5 91 23 47 76 ED DA 45 86 3E 50 E5 E5 E5 97 2E 5D BA 74 E9 D2 EA D5 AB 87 0E 1D 1A 
16 16 36 7A F4 68 CC C2 05 00 00 00 00 8D A2 0B E1 A3 4C 26 AB AD AD A5 AB 5D BA 74 31 35 35 65 
18 E6 EE DD BB 5F 7C F1 C5 C2 85 0B E5 22 69 39 E9 E9 E9 1E 1E 1E 73 E6 CC C1 48 73 00 00 00 00 
68 14 5D 08 A6 CB CA CA 32 32 32 E4 1E BC 76 ED DA D4 A9 53 E3 E2 E2 54 DC C9 A1 43 87 66 CC 98 
91 93 93 D3 D4 AD 03 00 00 00 00 9D A5 0B C1 B4 1C 2E 97 9B 9D 9D BD 6C D9 32 E5 1D D2 8A E2 E2 
E2 82 82 82 8A 8B 8B 35 D4 30 00 00 00 00 D0 31 3A 18 4C 97 95 95 AD 58 B1 82 4E 2D CE E5 72 FD 
FD FD 13 12 12 CA CB CB 6B 6B 6B 65 32 D9 DB B7 6F 8B 8A 8A 62 63 63 27 4F 9E 2C F7 DA 98 98 98 
75 EB D6 55 55 55 35 7B AB 01 00 00 00 A0 F5 D1 85 49 5B 04 02 81 8B 8B 4B 9D 4F 7D F6 D9 67 9B 
37 6F EE D7 AF 5F 9D CF D6 D6 D6 5E B9 72 25 28 28 88 5D A6 9A CB E5 9E 3D 7B 76 EC D8 B1 1A 69 
6B B3 43 D1 78 DD 86 E3 AB DB 70 7C 75 1B 8E AF 6E C3 F1 D5 6D 3A 38 69 4B 9D E6 CF 9F 7F E2 C4 
89 FA 22 69 86 61 F4 F4 F4 3C 3C 3C 0E 1C 38 60 67 67 47 1F 94 48 24 27 4F 9E AC AC AC 6C 96 36 
02 00 00 00 40 2B A6 B3 C1 B4 97 97 D7 BF FE F5 2F 55 E6 41 74 70 70 F8 EE BB EF D8 8F 5C BA 74 
29 2B 2B 4B 63 4D 03 00 00 00 00 1D A1 9B C1 34 97 CB 0D 08 08 90 9B BA A5 3E 1C 0E 67 CC 98 31 
EE EE EE F4 91 C2 C2 C2 5B B7 6E 69 AC 75 00 00 00 00 A0 23 74 33 98 76 76 76 1E 3C 78 B0 EA DB 
77 EF DE DD D9 D9 99 FD 88 48 24 7A F3 E6 4D 53 B7 0B 00 00 00 00 74 8A 2E 04 D3 5D BA 74 61 27 
3D 33 0C 63 6B 6B 6B 62 62 A2 FA 1E 38 1C 8E B5 B5 35 FB 91 57 AF 5E D5 D4 D4 34 4D FB 00 00 00 
00 40 47 E9 42 30 DD BE 7D 7B 63 63 63 F6 23 A6 A6 A6 ED DA B5 6B D4 4E AC AC AC D8 AB F9 F9 F9 
AF 5E BD 7A F7 B6 01 00 00 00 80 0E D3 85 60 DA C4 C4 84 CC 1F 0E 00 00 00 00 D0 9C 74 21 98 36 
36 36 EE DB B7 2F FB 91 E7 CF 9F 37 36 E3 59 AE 1F BA 5B B7 6E 8D ED DB 06 00 00 00 80 B6 46 17 
82 E9 76 ED DA D9 D8 D8 B0 1F C9 CC CC AC A8 A8 68 D4 4E 0A 0B 0B D9 AB 5C 2E F7 7F FE E7 7F 9A 
A0 71 00 00 00 00 A0 BB 74 21 98 66 18 C6 C1 C1 C1 C2 C2 82 AE 0A 85 C2 DC DC 5C D5 5F FE E6 CD 
9B BB 77 EF B2 1F F9 F0 C3 0F DB B7 6F DF 64 ED 6B B5 CA CA CA 3C 3D 3D 39 1C 0E 87 C3 89 8A 8A 
6A C2 3D 3F 7F FE FC 8B 2F BE E0 FC D7 D6 AD 5B D5 9B 26 AA B6 B6 36 33 33 73 FB F6 ED DE DE DE 
FD FA F5 23 7B EB DC B9 F3 E8 D1 A3 83 83 83 13 13 13 95 4C 0E 1F 15 15 C5 79 37 FE FE FE 6D 70 
F2 79 F6 A7 42 6D 02 81 80 EE 50 20 10 D4 F9 78 83 E8 11 1C 34 68 90 48 24 22 0F DE BC 79 D3 D2 
D2 92 3C FE C5 17 5F 3C 7F FE BC B1 6F 90 FD E1 F4 F0 F0 90 BB D2 6E 45 9E 3E 7D EA E6 E6 A6 FA 
67 55 2C 16 3B 3B 3B D3 63 F1 ED B7 DF 36 78 8B EF F6 ED DB F4 AF 4D 4E 11 A7 4E 9D 32 31 31 21 
8F 4C 9C 38 B1 B8 B8 58 C5 D6 66 66 66 3A 3A 3A D2 03 57 52 52 22 95 4A D7 AD 5B 47 DB 33 77 EE 
DC 46 4D A7 25 95 4A 43 42 42 E8 CB 37 6E DC 28 95 4A 99 77 FB 00 B3 3F 69 20 47 2A 95 A6 A7 A7 
AF 5A B5 6A E4 C8 91 E4 33 60 62 62 32 72 E4 C8 E0 E0 60 81 40 40 FE F8 75 92 3B 22 8D 3A 09 40 
73 62 9F AB F1 C5 61 D3 91 60 BA 4F 9F 3E 8E 8E 8E 74 B5 B0 B0 F0 F4 E9 D3 D5 D5 D5 2A BE BC A0 
A0 20 35 35 95 AE 72 B9 DC 61 C3 86 35 71 13 E1 FF FA E3 8F 3F E2 E3 E3 E9 EA E5 CB 97 CB CA CA 
1A B5 07 99 4C F6 C7 1F 7F 78 79 79 F5 EF DF 3F 30 30 F0 97 5F 7E A1 DF D5 F2 F2 F2 84 84 84 F5 
EB D7 BB B9 B9 D9 DB DB 9F 38 71 42 F5 0F 03 B4 76 36 36 36 B4 D2 E5 8D 1B 37 72 72 72 1A BB 07 
F6 87 F3 93 4F 3E E9 DE BD 7B 53 B6 AF 19 99 9A 9A D2 BB 76 22 91 A8 C1 EB 8A EC EC 6C F6 99 F0 
CE 9D 3B A5 A5 A5 CA 5F 92 95 95 45 2E 36 AC AD AD 07 0E 1C C8 30 8C B7 B7 F7 DC B9 73 C9 B3 31 
31 31 3B 77 EE 54 12 45 51 15 15 15 1B 36 6C 48 4B 4B 63 18 C6 D6 D6 76 CD 9A 35 5D BB 76 35 30 
30 98 39 73 A6 9B 9B 1B D9 E6 C0 81 03 D1 D1 D1 AA 5F 75 5F BD 7A 75 D7 AE 5D 64 D9 CB CB CB CF 
CF CF C0 C0 40 C5 D7 42 63 DD BD 7B D7 DB DB 7B D8 B0 61 EB D6 AD 4B 4E 4E 96 48 24 0C C3 48 24 
92 E4 E4 E4 F5 EB D7 BB B8 B8 38 39 39 5D BD 7A 15 73 6B 83 4E D2 91 60 FA BD F7 DE 73 71 71 61 
3F 72 E2 C4 09 15 AF 6E 6B 6A 6A CE 9E 3D 4B 4E E2 84 B3 B3 B3 5C DE 08 34 AD 9A 9A 9A A4 A4 24 
72 B6 25 04 02 81 50 28 54 7D 0F 52 A9 74 F7 EE DD A3 46 8D 8A 8D 8D 55 BE A5 48 24 FA EA AB AF 
E6 CC 99 53 52 52 A2 66 73 A1 55 E9 D4 A9 13 9D 83 A9 B0 B0 30 2E 2E AE 51 BF DF 35 35 35 57 AE 
5C 21 1F 4E 5B 5B DB 71 E3 C6 71 38 1C 8D 34 54 F3 8C 8C 8C E8 A9 EC F6 ED DB 8F 1E 3D 52 BE BD 
DC 64 55 B7 6F DF CE CB CB 53 B2 FD 9B 37 6F 6E DF BE 4D 96 ED EC EC 78 3C 1E C3 30 86 86 86 81 
81 81 34 02 DE B5 6B D7 85 0B 17 94 FF BF 52 A9 74 CF 9E 3D 91 91 91 0C C3 70 B9 DC 95 2B 57 92 
B8 9C 61 98 1E 3D 7A 2C 5F BE 9C CE 65 1B 1E 1E AE E2 F4 B4 45 45 45 3B 77 EE 24 C7 91 C7 E3 05 
06 06 AA 38 8D 17 34 96 4C 26 FB FD F7 DF 27 4E 9C A8 FC 6C 9C 9E 9E 3E 71 E2 C4 43 87 0E A9 72 
71 05 D0 BA E8 48 30 CD E1 70 C6 8F 1F CF AE 36 5D 58 58 18 1C 1C 9C 99 99 A9 FC 85 32 99 2C 29 
29 69 F7 EE DD EC 07 3D 3D 3D 3B 77 EE AC 91 86 02 C3 30 0C F3 E8 D1 A3 B8 B8 38 86 61 9C 9C 9C 
66 CF 9E CD 30 8C 44 22 39 7F FE BC 8A FD C7 32 99 EC F4 E9 D3 C1 C1 C1 EC 70 5C B9 63 C7 8E CD 
9B 37 0F F1 74 1B E1 E2 E2 62 6B 6B 4B 96 93 92 92 8A 8A 8A 54 7F ED A3 47 8F AE 5E BD 4A 96 3D 
3C 3C 3E FC F0 C3 A6 6F 5F 33 1A 30 60 00 59 90 48 24 D9 D9 D9 4A B6 94 48 24 E4 84 69 61 61 41 
42 70 89 44 72 F3 E6 4D 25 2F A9 A8 A8 A0 E7 58 6B 6B EB 8E 1D 3B 92 E5 1E 3D 7A AC 5C B9 92 A4 
DE 49 24 92 F5 EB D7 2B BF 3F 70 F5 EA D5 1F 7E F8 81 2C FB FA FA 7A 79 79 B1 2F 60 46 8F 1E BD 
68 D1 22 B2 9C 96 96 16 11 11 D1 60 BE 8A 54 2A 3D 78 F0 20 0D E2 17 2C 58 20 D7 DB 02 4D 28 23 
23 63 E9 D2 A5 62 B1 98 61 18 2E 97 BB 70 E1 42 A1 50 58 5D 5D 2D 93 C9 DE BE 7D 7B FF FE FD EF 
BE FB 8E 5C 0E 49 24 92 C0 C0 C0 B3 67 CF 6A BB C9 00 9A 21 6B FD 6A 6B 6B B7 6F DF 2E F7 BE EC 
EC EC 52 52 52 6A 6B 6B EB 7C 49 4D 4D CD E9 D3 A7 49 6F 0A E5 E6 E6 F6 E4 C9 93 66 6E BC E6 BC 
E3 F1 2D 2D 2D 1D 37 6E 1C D9 C9 F1 E3 C7 9B AA 55 E7 CE 9D 23 FB F4 F5 F5 BD 7C F9 32 F9 D1 B5 
B5 B5 BD 77 EF 9E 2A 2F CF CD CD E5 F3 F9 F4 90 0D 1D 3A 34 32 32 F2 F1 E3 C7 E4 F4 2D 93 C9 6A 
6A 6A 4A 4B 4B 13 12 12 A6 4D 9B C6 3E B8 DB B7 6F AF EF C3 20 27 2B 2B 8B 5E 9B 35 E1 1B 6F 72 
2D F0 FB BB 76 ED 5A D2 AA 71 E3 C6 95 96 96 AA F2 92 94 94 14 7A 8C 52 52 52 54 FF BF 8E 1F 3F 
4E BF E9 59 59 59 F4 F1 97 2F 5F FA F9 F9 91 A7 B8 5C 6E 7C 7C BC 1A FB 64 18 26 26 26 46 F5 17 
6A C2 BB 1F DF 9C 9C 9C 21 43 86 90 FD 04 06 06 D2 EF 88 22 FA 99 F7 F4 F4 DC B2 65 0B FD 86 56 
54 54 D4 F7 12 A1 50 48 A7 BB 92 FB 5B BD 7D FB 76 C3 86 0D F4 2F 19 10 10 F0 F2 E5 CB 3A 77 F2 
E0 C1 03 FA 75 AE EF F4 FB E4 C9 13 DA D5 CD E5 72 7F F9 E5 17 E5 EF FA CA 95 2B 74 14 CD E4 C9 
93 CB CB CB 95 6F AF C4 93 27 4F BC BC BC E8 1B D9 B0 61 C3 DB B7 6F D5 DE 9B 9C 16 F8 FD 6D AC 
57 AF 5E CD 9B 37 8F BC 11 1E 8F F7 DB 6F BF 29 9E 63 6B 6B 6B AF 5C B9 42 7F 6A 15 8F 32 FB 87 
A6 B1 27 81 96 4C 07 8E AF 9C EC EC 6C FA 6D AD EF 70 B7 1D EC E3 AB 23 3D D3 0C C3 70 38 1C 1F 
1F 1F 6F 6F 6F F6 83 42 A1 F0 93 4F 3E F1 F3 F3 4B 4C 4C 7C FE FC 39 79 F3 B5 B5 B5 25 25 25 E7 
CF 9F F7 F2 F2 9A 32 65 0A B9 9E 26 B8 5C EE DC B9 73 7B F4 E8 D1 DC AD 6F 4B 2A 2B 2B 7F FD F5 
57 B2 6C 6F 6F 3F 64 C8 10 92 EF 9E 99 99 79 E9 D2 25 99 0A 77 E4 E3 E2 E2 68 5A CE F2 E5 CB AF 
5C B9 E2 EB EB DB B3 67 4F 5A CD 50 4F 4F AF 73 E7 CE A3 46 8D 3A 7E FC 78 6C 6C 2C 3D 89 9F 3C 
79 32 3F 3F BF C9 DF 11 B4 34 C6 C6 C6 34 D3 43 22 91 5C B9 72 45 C5 09 4D 2B 2B 2B 69 B6 B4 BB 
BB FB D0 A1 43 35 D5 C4 E6 D2 B5 6B D7 DE BD 7B 93 E5 EC EC 6C 25 03 F8 44 22 11 49 B5 B2 B7 B7 
77 73 73 23 51 F2 9F 7F FE F9 F4 E9 D3 FA 5E 92 99 99 49 BA 9C ED EC EC E4 52 E3 0C 0C 0C FC FC 
FC 68 18 1A 11 11 51 67 BA 73 65 65 E5 B6 6D DB C8 D7 99 C7 E3 FD EB 5F FF AA F3 F4 CB 4E F6 90 
48 24 9B 37 6F 56 F2 45 2E 2A 2A DA BA 75 2B C9 E4 E6 F1 78 CB 96 2D 53 7B 22 82 E2 E2 E2 05 0B 
16 C4 C4 C4 90 D5 80 80 80 85 0B 17 22 F1 9A ED C1 83 07 E7 CF 9F 27 CB 81 81 81 64 1C A1 DC 36 
1C 0E C7 CD CD 2D 2C 2C 8C 1C C1 84 84 04 76 5E 25 B4 22 D6 D6 D6 07 0F 1E 24 F1 B4 58 2C 9E 3F 
7F 7E 42 42 82 2A BF DA 3A 4F 77 82 69 86 61 BA 76 ED BA 7E FD 7A 3A F6 88 90 48 24 91 91 91 6E 
6E 6E 66 66 66 7A 7A 7A 1C 0E 47 5F 5F BF 5B B7 6E 5E 5E 5E 8A 09 5E 21 21 21 93 26 4D 6A C6 26 
B7 45 7F FD F5 17 49 67 27 03 3D D9 F9 EE AA 0C 43 7C FD FA F5 9F 7F FE 49 96 27 4C 98 10 18 18 
48 F3 29 15 E9 E9 E9 7D FA E9 A7 EB D6 AD 23 AB 69 69 69 EC F1 55 A0 C3 9C 9C 9C 68 0F 4A 52 52 
D2 93 27 4F 54 79 55 56 56 D6 A5 4B 97 C8 72 AB 1E 7A 48 99 98 98 7C F4 D1 47 64 39 3B 3B FB F1 
E3 C7 75 6E 56 53 53 73 E3 C6 0D B2 FC D1 47 1F F5 E9 D3 87 F4 52 0B 85 C2 FA C6 E0 D7 D4 D4 D0 
71 0E 1F 7F FC B1 A5 A5 A5 DC 06 E6 E6 E6 41 41 41 F4 52 36 2C 2C 2C 23 23 83 BD 81 54 2A 0D 0F 
0F 3F 70 E0 00 59 9D 3F 7F BE DC D9 9B 8D 9D EC 21 10 08 0E 1C 38 50 67 EA AD 54 2A 3D 7A F4 28 
4D F0 08 09 09 A1 1D F3 8D 55 59 59 B9 76 ED 5A 1A 49 7B 79 79 AD 5E BD 5A 6E B6 5D B8 75 EB 16 
B9 6E E1 F3 F9 13 26 4C A8 6F 80 01 87 C3 19 3B 76 2C 3D BE F7 EF DF 6F BE 26 42 93 1A 30 60 C0 
EE DD BB 69 3C 3D 6B D6 2C C4 D3 8C 8E 05 D3 0C C3 D8 D8 D8 1C 3E 7C 78 EC D8 B1 6A BC 36 38 38 
18 BD 0E 9A 26 93 C9 E2 E3 E3 49 6F 16 9F CF EF D3 A7 0F 87 C3 71 75 75 25 F7 64 55 19 86 58 55 
55 45 6F 26 38 38 38 74 EB D6 4D F9 F6 1C 0E 67 CC 98 31 B4 9F F2 FE FD FB 2A 76 52 42 AB D6 A3 
47 0F 27 27 27 B2 9C 9A 9A 4A C7 C9 29 21 93 C9 92 92 92 48 64 D0 DA 87 1E 52 1C 0E 87 A6 8F E7 
E4 E4 D4 D7 A1 FB FC F9 F3 3B 77 EE 30 FF 2D CA 61 62 62 42 D3 9C 6E DC B8 51 E7 57 E6 E5 CB 97 
34 13 DA DE DE BE CE 6B 5A 27 27 A7 C0 C0 40 B2 9C 99 99 B9 6E DD 3A 76 45 11 81 40 B0 67 CF 1E 
B2 3C 79 F2 E4 B9 73 E7 2A 39 FD 1A 18 18 04 04 04 D0 64 8F C3 87 0F 5F BB 76 4D 71 33 F6 3E A7 
4F 9F FE E5 97 5F AA 77 10 49 A0 1F 11 11 41 56 F9 7C FE FA F5 EB 31 84 51 CE 9B 37 6F E8 B5 D6 
A0 41 83 94 5F 7C 1A 1B 1B D3 2B AB 82 82 82 FA 12 DF 2D 2C 2C 50 97 B6 85 1B 32 64 C8 B6 6D DB 
C8 29 82 C4 D3 75 7E 19 DB 14 5D 0B A6 19 86 B1 B6 B6 3E 79 F2 E4 77 DF 7D A7 FA 4B CC CC CC C2 
C3 C3 D1 EB D0 0C FE FE FB 6F 9A 20 3B 7C F8 70 12 0A F7 ED DB 97 04 BB AA 0C 43 34 34 34 A4 D9 
90 35 35 35 AA 5C 10 77 EE DC 99 16 07 28 2F 2F 6F EC EC 98 0D AA A8 A8 98 31 63 06 A9 A6 69 62 
62 72 EA D4 A9 3A 37 93 C9 64 27 4E 9C A0 25 78 43 42 42 30 AA 5D 73 DA B5 6B F7 C9 27 9F D0 D5 
A4 A4 A4 06 87 B7 16 15 15 FD FE FB EF 64 59 07 86 1E 52 B6 B6 B6 34 B3 F9 8F 3F FE A8 F3 2B 23 
16 8B C9 75 2C 29 CA C1 E1 70 68 BF FE 9D 3B 77 EA AC A9 57 58 58 48 02 29 25 B5 44 39 1C CE CC 
99 33 A7 4F 9F 4E 56 CF 9C 39 73 F0 E0 41 12 9A E7 E7 E7 87 84 84 90 0B 63 3B 3B BB 7F FF FB DF 
0D 26 63 F4 E8 D1 63 C9 92 25 24 6A 2F 2C 2C DC BA 75 AB DC D0 D2 92 92 92 1D 3B 76 D0 7D 2E 5F 
BE DC C4 C4 44 F9 3E EB 24 93 C9 4E 9F 3E 4D C7 44 F2 78 BC 8D 1B 37 D2 6B 12 A0 DA B5 6B 47 A6 
08 90 C9 64 7B F7 EE 35 32 32 52 B2 B1 54 2A A5 33 0D F7 E8 D1 83 BD B1 9E 9E 1E BD 8E EA D6 AD 
1B 1D C9 0A 2D D6 F0 E1 C3 F7 EC D9 43 E3 E9 19 33 66 24 25 25 69 BB 51 DA A4 83 C1 34 C3 30 66 
66 66 1B 37 6E 4C 4E 4E 96 4B A1 56 44 86 1E DF BE 7D 7B C1 82 05 86 86 86 CD D3 BC B6 8C 56 F0 
B5 B0 B0 F8 EC B3 CF F4 F5 F5 19 86 E1 72 B9 AE AE AE 64 83 CB 97 2F 3F 7C F8 50 C9 1E 0C 0D 0D 
BB 76 ED 4A 96 AF 5D BB A6 24 A1 93 6A D4 19 5F 0D 26 26 26 CB 97 2F 27 A7 15 89 44 12 1E 1E 5E 
67 FF 5F 56 56 16 AD D5 35 7E FC F8 45 8B 16 E1 36 88 46 0D 18 30 80 DE 91 48 4A 4A 6A 30 5D FE 
C1 83 07 24 95 93 CB E5 4E 98 30 41 67 4E 08 16 16 16 B4 47 30 37 37 F7 E5 CB 97 8A DB D0 9B F5 
76 76 76 24 00 ED DD BB 37 49 90 10 0A 85 EC 81 25 54 76 76 36 49 DB 18 32 64 08 4D CB 56 C4 FE 
76 30 0C B3 7B F7 EE 1B 37 6E 54 55 55 6D D9 B2 85 A6 7B 2D 5B B6 AC 5F BF 7E AA BC 17 4F 4F 4F 
5A C4 FA C2 85 0B C7 8E 1D A3 BD E6 E4 62 35 3A 3A BA B1 FB 54 74 ED DA 35 5A 2C 88 CB E5 86 85 
85 8D 1C 39 52 BD 5D 01 25 12 89 68 FF 25 BB F4 16 C3 30 ED DB B7 EF D9 B3 A7 36 1A 05 EA 1B 3E 
7C F8 CE 9D 3B C9 60 09 B1 58 3C 6F DE BC B6 DC 3F AD 9B C1 34 C3 30 7A 7A 7A 2E 2E 2E E7 CE 9D 
2B 2C 2C 3C 79 F2 A4 9F 9F 1F 7B 56 17 47 47 C7 80 80 80 D8 D8 58 B1 58 BC 6B D7 2E 2B 2B 2B ED 
B5 B4 0D 61 57 F0 75 74 74 A4 BD 65 0C C3 B8 B8 B8 90 D3 6B 83 C3 10 F5 F5 F5 3D 3D 3D 49 E7 74 
42 42 82 BF BF FF AD 5B B7 6A 6B 6B 35 DF 7C 65 FA F5 EB B7 6C D9 32 D2 67 26 10 08 C2 C3 C3 E5 
FA 41 E5 06 5A 05 05 05 E9 40 3E 6E 0B D7 AD 5B B7 E1 C3 87 93 65 A1 50 C8 AE 19 A2 A8 BA BA FA 
FC F9 F3 E4 C3 E9 EE EE 3E 78 F0 E0 E6 68 62 B3 E8 D4 A9 13 BD 33 F3 E0 C1 03 C5 29 09 AB AA AA 
48 8E 07 C3 30 7C 3E 9F E4 45 98 9B 9B F7 EF DF 9F 61 98 C2 C2 42 B9 FA D3 0C C3 C8 64 32 3A 74 
C1 DE DE BE 4B 97 2E 4A 1A C0 FE 76 88 C5 E2 1D 3B 76 FC F4 D3 4F 47 8F 1E 25 CF CE 98 31 C3 DB 
DB 5B C5 64 0C 43 43 C3 85 0B 17 D2 D4 DB DD BB 77 D3 96 67 64 64 EC DB B7 8F 2C 2B D6 D7 53 5D 
51 51 D1 E6 CD 9B E9 F5 43 48 48 C8 94 29 53 74 20 E1 47 BB C4 62 F1 9A 35 6B C8 5F 55 F9 D0 DE 
AE 5D BB 9A 99 99 35 63 D3 40 7D 23 47 8E DC B7 6F 1F B9 56 17 89 44 73 E7 CE 6D B3 F1 B4 CE 06 
D3 04 87 C3 E9 DE BD FB D4 A9 53 0F 1F 3E 7C FD FA 75 5A D0 E4 FA F5 EB BB 77 EF 1E 3F 7E BC DA 
A3 BC 41 0D EC 0A BE E3 C6 8D 63 FF F1 AD AC AC 68 E7 F4 EF BF FF AE BC 30 30 9F CF F7 F1 F1 21 
CB B1 B1 B1 43 87 0E 1D 35 6A D4 F6 ED DB EF DD BB D7 E4 29 1C 2A E2 70 38 5E 5E 5E BE BE BE 64 
75 FF FE FD 17 2F 5E A4 CF 92 3E 33 15 07 5A 41 53 D1 D7 D7 1F 37 6E 1C CD E5 4D 49 49 51 52 CB 
E2 E9 D3 A7 B4 C2 80 8B 8B CB 7B EF BD D7 1C 4D 6C 16 ED DA B5 63 4F DD A2 38 0F CB B3 67 CF 48 
1F B3 93 93 53 DF BE 7D C9 83 5C 2E D7 DE DE 9E 2C DF B9 73 47 2E C3 B5 A2 A2 82 0E 6F B0 B1 B1 
A1 85 74 EA C4 E1 70 BC BD BD 67 CC 98 41 56 CF 9C 39 B3 68 D1 22 7A 8B 26 24 24 A4 51 37 8B AC 
AC AC 82 82 82 68 68 BE 6B D7 AE 8A 8A 8A CA CA CA F0 F0 70 52 F4 9A CF E7 2F 5C B8 50 BD 9C BD 
CA CA CA D0 D0 50 3A 7E 11 E5 3B 9A 44 4E 4E CE DC B9 73 C9 5F 95 CB E5 06 05 05 D1 54 3D 42 5F 
5F BF 43 87 0E 74 59 4F 4F C7 23 13 5D E2 EA EA 7A F4 E8 51 1A 4F 2F 5E BC F8 FA F5 EB DA 6E 94 
16 E0 23 0B CD 27 35 35 95 4E 17 2C 37 87 82 A1 A1 E1 98 31 63 C8 72 5A 5A DA 83 07 0F 94 EC C7 
D0 D0 30 38 38 38 20 20 80 3E 92 9C 9C 1C 18 18 38 70 E0 40 43 43 C3 E1 C3 87 07 07 07 C7 C5 C5 
95 95 95 35 E7 10 63 63 63 E3 6F BE F9 86 64 9A 4A 24 92 1D 3B 76 14 14 14 90 A7 6E DF BE 4D F3 
2F BD BD BD 67 CD 9A 85 9F E7 E6 D1 BF 7F 7F 9A E9 21 10 08 FE FA EB AF FA B6 BC 7A F5 2A FD 70 
EA C6 D0 43 B6 01 03 06 D0 8B 8A 7B F7 EE C9 3D 4B 67 11 1F 38 70 20 7B 44 EF B0 61 C3 C8 AB 32 
32 32 9E 3D 7B C6 7E 49 51 51 11 19 7D 68 61 61 E1 E0 E0 D0 60 03 8C 8C 8C 96 2E 5D 2A 77 0D A9 
F6 2D 1A 76 B2 47 74 74 74 42 42 42 7C 7C 3C 19 AB C0 E5 72 BF F9 E6 1B F5 F2 9B E5 06 1D A2 7C 
47 93 B8 7D FB B6 AF AF 2F 99 A5 8B E4 CC 8C 1E 3D 5A 6E 9B 76 ED DA A1 63 AB F5 62 C7 D3 42 A1 
70 FE FC F9 6D 30 9E 46 30 0D CD 84 5D C1 97 CF E7 2B A6 D6 38 38 38 8C 1A 35 8A 51 6D 18 A2 99 
99 D9 D6 AD 5B A3 A2 A2 14 27 7E BF 71 E3 C6 FA F5 EB C7 8D 1B D7 A5 4B 17 5B 5B DB 75 EB D6 89 
44 A2 E6 89 AA AD AD AD BF F9 E6 1B 5A 4B 35 22 22 42 2A 95 96 94 94 84 85 85 91 FB 9B 3C 1E 2F 
38 38 98 E6 7C 83 A6 B1 0B 2F E6 E4 E4 5C B9 72 A5 CE CD 24 12 09 1D 3D A3 4B 43 0F A9 9E 3D 7B 
D2 4C 0F 91 48 C4 EE 66 96 C9 64 B4 4B DE DE DE 9E DD 49 4C D3 A6 53 53 53 E5 66 4F 7C F4 E8 11 
7B C0 A2 2A 6D B0 B2 B2 5A BD 7A 35 BB E8 87 DA 13 13 B2 93 3D 24 12 49 50 50 50 48 48 08 E9 EA 
9E 31 63 06 7B 8E 15 D5 C9 0D 3A 44 F9 8E 77 27 93 C9 12 13 13 BF FA EA 2B 3A 14 21 2C 2C CC DF 
DF 5F 79 57 82 95 95 15 ED A5 86 D6 62 E4 C8 91 87 0E 1D A2 F1 74 60 60 A0 2A 05 94 74 09 82 69 
68 26 B4 BC 34 C3 30 9F 7F FE B9 62 7F 8F B9 B9 F9 88 11 23 C8 72 83 C3 10 19 86 31 34 34 F4 F1 
F1 B9 73 E7 CE A5 4B 97 7C 7D 7D EB 4C B3 13 89 44 AB 56 AD EA D7 AF 9F 9F 9F 5F F3 4C D7 E2 ED 
ED 4D FB CC 0E 1F 3E 7C F5 EA D5 43 87 0E 91 41 51 CC BB 55 BD 05 35 B0 0B 2F 32 0C 93 9C 9C 5C 
67 61 8A CC CC 4C 72 A5 A7 63 43 0F 29 33 33 B3 0F 3E F8 80 2C 8B 44 22 F6 1F 81 26 6C 28 F6 31 
77 E9 D2 85 66 7A A4 A5 A5 B1 AF 48 69 16 B5 BD BD BD EA 7D 8A 72 B9 22 F9 F9 F9 AF 5F BF 6E DC 
3B F9 2F 76 B2 47 4E 4E 0E A9 5B EC EC EC BC 74 E9 52 F5 46 18 B3 07 1D A2 7C 47 93 B8 76 ED 9A 
9F 9F 1F 2D F9 B2 6D DB 36 25 91 74 83 45 4E A1 25 23 33 78 D0 D5 D7 AF 5F 6B 2B E5 52 5B 10 4C 
43 73 90 2B 2F 4D 7F A1 D9 D8 19 AE AA CF 86 68 64 64 34 76 EC D8 C8 C8 C8 E2 E2 E2 AC AC AC A8 
A8 A8 19 33 66 28 76 95 45 46 46 7A 7A 7A 26 26 26 6A BA 8B DA D0 D0 30 30 30 90 54 C3 2D 2C 2C 
9C 3D 7B F6 A6 4D 9B C8 53 73 E6 CC F1 F1 F1 D1 B1 FC 81 96 8F 16 5E 64 18 E6 C6 8D 1B B4 34 32 
25 93 C9 E2 E2 E2 48 2D 0B 1D 1B 7A 48 71 B9 5C 1A 1A 8A 44 22 F2 66 09 5A 14 CF C6 C6 46 2E 93 
B5 5D BB 76 F4 DA 4F 28 14 56 54 54 90 65 89 44 42 B2 93 19 86 71 74 74 64 FF 88 2A 91 99 99 B9 
7E FD 7A 12 AD 12 F5 4D 8B A8 A2 B1 63 C7 D2 3C 6C E6 BF C9 B8 EA 8D 26 CF CC CC FC FE FB EF C9 
ED 23 94 EF 68 12 EC 3F A9 99 99 D9 FE FD FB 95 A7 B7 D1 72 78 FA FA FA 38 49 B6 3A 49 49 49 33 
66 CC A0 37 60 77 EC D8 41 07 7F B7 11 08 A6 A1 39 94 95 95 5D BE 7C 99 2C A7 A5 A5 91 B9 5A 14 
B9 B8 B8 D0 DF DA 06 87 21 CA 31 30 30 B0 B1 B1 F1 F1 F1 39 72 E4 48 5E 5E 5E 69 69 69 6C 6C 2C 
BB C7 5A 24 12 F9 F9 F9 35 C3 BD A7 1E 3D 7A AC 5C B9 92 C4 25 8F 1F 3F 2E 2F 2F 67 18 86 CF E7 
07 06 06 22 FF B2 4E 5C 2E 97 5D DA A5 C9 77 4E C7 B6 16 16 16 C6 C6 C6 CA 4D 41 52 54 54 44 73 
3C 74 78 50 32 9D 07 B1 B0 B0 90 3D FF 5C 46 46 06 B9 C0 A8 B3 28 C7 C0 81 03 C9 A1 61 17 C8 2B 
2F 2F 27 D9 E7 8A B3 88 D7 87 5D CD 86 4D 71 5A 44 D5 19 19 19 2D 5C B8 90 16 59 9B 3F 7F FE F8 
F1 E3 D5 D8 4F 71 71 F1 8A 15 2B 68 DB 50 BE E3 DD 55 57 57 FF F4 D3 4F 34 BB 63 D7 AE 5D AA CF 
9E D3 BD 7B 77 4C DA D2 BA E0 5A 94 41 30 0D CD 43 28 14 D2 1C 0F 15 C5 C7 C7 2B 8E 94 52 11 87 
C3 E9 DC B9 F3 F8 F1 E3 23 23 23 B3 B3 B3 69 A6 A6 58 2C DE BD 7B B7 92 92 0E 4D 65 E4 C8 91 4B 
96 2C A1 AB 5C 2E 77 F1 E2 C5 6A 57 BD D5 79 86 86 86 1A CD 92 74 74 74 A4 FD B2 D7 AF 5F 97 1B 
4B 97 9E 9E 4E 72 3C EC EC EC D4 4B E1 6D 15 FA F6 ED 4B D3 A6 EF DE BD 4B 6E C2 BE 79 F3 86 5E 
5E 0E 19 32 44 B1 28 07 8F C7 23 D1 2A 7B F6 44 B1 58 4C 06 2C D6 39 8B B8 22 B9 69 C3 D7 AE 5D 
4B 6F D7 28 4E 8B D8 28 5D BA 74 A1 E3 17 3B 76 EC A8 C6 B8 5E B9 39 C3 51 BE A3 49 E4 E7 E7 D3 
11 32 8B 16 2D 52 E5 E2 E4 FD F7 DF D7 7C BB A0 E9 89 C5 E2 A0 A0 20 76 5A 7C DB BC 16 45 30 0D 
1A C7 2E 2F DD 28 B1 B1 B1 0D CE 5A D7 A0 CE 9D 3B AF 5A B5 2A 24 24 84 AC 5E BA 74 29 2B 2B EB 
1D F7 D9 20 03 03 03 F6 1C 04 66 66 66 3D 7A F4 68 83 E7 17 35 D0 39 D2 54 41 FB 98 95 D7 A6 ED 
D3 A7 0F ED 29 91 BB 48 AB AE AE A6 A3 12 5D 5D 5D 75 B8 E4 BC B9 B9 79 AF 5E BD C8 72 76 76 36 
B9 A4 2C 2D 2D 65 CF 22 AE F8 2A 13 13 13 DA A5 4D 67 4F A4 F1 77 7D B3 88 CB 61 4F F1 ED E5 E5 
35 77 EE DC D9 B3 67 4F 9E 3C 99 3C 72 E6 CC 99 FD FB F7 6B 65 36 50 94 EF D0 10 91 48 44 13 F1 
BD BC BC 54 B9 38 A1 C9 42 98 FE B0 15 29 2E 2E 5E B2 64 09 2D 25 19 12 12 D2 E0 00 53 5D 85 60 
1A 34 8E 5D 5E BA 51 14 87 21 96 95 95 79 7A 7A 92 9C 90 F5 EB D7 AB B8 1F 03 03 83 89 13 27 92 
0E B6 C2 C2 C2 06 87 36 BE BB CC CC CC 5D BB 76 D1 55 B1 58 BC 79 F3 E6 46 65 AD B4 29 FA FA FA 
F4 FC CB 4E E7 55 4E 26 93 E5 E6 E6 D2 3D 28 A9 4D 4B 12 EB E9 EA EF BF FF 4E 07 C7 3C 7C F8 90 
24 20 E9 EA D0 43 CA C4 C4 E4 E3 8F 3F 26 CB D9 D9 D9 8F 1F 3F 66 18 26 2F 2F 8F 44 C6 F5 15 E5 
E0 70 38 34 89 FC FE FD FB 15 15 15 55 55 55 64 48 19 C3 30 AA 8C A6 65 4F 1B CE E3 F1 02 03 03 
CD CD CD 4D 4D 4D 57 AE 5C 49 6F 17 EC D9 B3 A7 B1 77 AE DE 1D CA 77 68 0E CD 23 B2 B1 B1 69 EC 
D4 86 18 89 D8 5A E0 AE 0E 1B 82 69 D0 38 5A 5E 9A CB E5 C6 C7 C7 CB 1A 72 EE DC 39 F2 42 C5 61 
88 46 46 46 F4 6E 60 66 66 A6 EA BD DD EC DB C1 9A EE 03 23 F3 47 C8 A5 87 5E B8 70 E1 E0 C1 83 
5A E9 7E 6B F9 4C 4D 4D 69 B6 6E 56 56 96 5C 4E 73 7D 5E BE 7C 49 83 E9 06 CB 69 D9 DB DB 93 12 
E0 0C C3 A4 A6 A6 D2 12 E0 37 6E DC 20 63 E9 74 75 E8 21 A5 AF AF 4F 13 8D 68 CE C6 CD 9B 37 C9 
97 88 CE 22 AE C8 C6 C6 86 5C 88 E6 E5 E5 95 94 94 3C 7F FE 9C 04 D3 4E 4E 4E 0D 16 C5 AB AC AC 
DC BC 79 33 0D 94 03 03 03 E9 2D 82 81 03 07 06 07 07 93 65 AD 5C 6D A2 7C 87 E6 D0 13 9D A1 A1 
A1 8A 17 A8 5D BA 74 91 9B 63 1C 5A B2 CA CA CA B0 B0 30 7A 57 C7 D7 D7 77 CD 9A 35 6D F9 AE 0E 
82 69 D0 2C B9 F2 D2 64 82 62 E5 1C 1D 1D 49 C1 69 46 61 18 A2 91 91 11 FD FD 8E 8F 8F A7 25 05 
1A 54 51 51 F1 F7 DF 7F AB DE 6C B5 C9 64 B2 E8 E8 68 7A 8A 09 0B 0B 0B 0B 0B 23 CB 9B 36 6D 52 
AF 87 5E E7 19 1B 1B D3 C2 6D E9 E9 E9 72 39 CD F5 79 F4 E8 11 2D D0 D6 E0 A0 A5 5E BD 7A D1 A9 
22 D2 D2 D2 48 6E C3 F3 E7 CF E9 0D 4A 1D 1E 7A 48 7D F4 D1 47 B4 5E C7 FD FB F7 5F BD 7A 45 67 
47 A2 B3 88 2B B2 B4 B4 24 5D DA B7 6F DF 7E FA F4 E9 A3 47 8F 48 67 B6 DC 0C 2F 8A E4 BE 0B 73 
E6 CC 99 3D 7B 36 FD 5F C8 B4 88 74 EA A5 0B 17 2E EC DA B5 AB D9 AE 36 D9 43 A6 18 86 59 B7 6E 
5D 1B 1C 32 D5 0C BA 75 EB A6 7C 76 CC 3A 5F A2 A1 C6 40 53 21 F9 51 F4 A7 CD CB CB 6B F3 E6 CD 
6D 7C FE 04 04 D3 A0 59 59 59 59 97 2E 5D 22 CB AE AE AE AA CC 76 C6 2E 38 2D 97 E1 CA E1 70 DC 
DC DC 48 9A 66 61 61 61 58 58 58 71 71 71 83 3B 94 C9 64 E7 CF 9F A7 BD E3 1A CD 8B CD C8 C8 A0 
A7 98 C9 93 27 FB FB FB CF 9A 35 8B CC 22 21 91 48 D6 AE 5D DB 3C E5 AE 5B 97 F6 ED DB D3 0C 84 
F8 F8 F8 C8 C8 C8 06 83 2A A9 54 7A E2 C4 09 7A 35 35 78 F0 60 E5 29 E9 FA FA FA 63 C6 8C A1 09 
BE 49 49 49 D5 D5 D5 39 39 39 37 6E DC 60 18 86 CF E7 2B CE CA A6 7B 2C 2C 2C 68 F1 8D DC DC DC 
FC FC 7C 12 4C B3 67 11 57 C4 9E 57 3C 3F 3F 3F 3B 3B 9B F4 E6 CA CD F0 A2 E8 DA B5 6B 2B 57 AE 
24 CB 75 56 B3 31 36 36 5E B8 70 21 BD 63 B0 6B D7 AE B3 67 CF AA F9 DE 1A 43 EE DE 51 40 40 80 
B7 B7 37 86 34 34 A1 55 AB 56 91 DB 8C 91 91 91 AA 64 D5 33 0C 63 63 63 73 F7 EE 5D 99 4C E6 E1 
E1 A1 E9 E6 C1 BB 40 7E 54 9D 10 4C 83 06 C9 64 B2 A4 A4 24 92 05 6B 61 61 31 76 EC 58 55 7E B1 
D8 05 A7 19 85 61 88 03 07 0E F4 F6 F6 26 CB 31 31 31 D3 A7 4F A7 E3 A2 EA 54 5D 5D 7D E4 C8 91 
B5 6B D7 92 55 77 77 77 55 7A C7 D5 F3 FC F9 F3 C9 F8 6F 51 00 00 20 00 49 44 41 54 75 EB D6 91 
08 CF D6 D6 76 E5 CA 95 A6 A6 A6 E6 E6 E6 81 81 81 A4 43 5D 20 10 6C D9 B2 45 6E EA 0A 60 18 C6 
C5 C5 85 DE 64 FF E1 87 1F F6 EC D9 A3 64 EC 69 75 75 F5 9E 3D 7B 68 56 BA BB BB FB D0 A1 43 1B 
FC 2F FA F7 EF 4F E3 B6 B4 B4 B4 82 82 82 94 94 14 F2 E1 1C 3B 76 2C 1D 9C A7 C3 4C 4D 4D 69 30 
9D 9F 9F 7F FF FE FD 3A 67 11 57 44 E7 15 7F F0 E0 01 E9 D4 6F 70 16 F1 E2 E2 E2 6D DB B6 D1 6A 
59 F5 4D F1 6D 6B 6B 4B 27 0D 95 48 24 DB B7 6F 57 FD 76 93 7A E4 06 1D E2 F6 34 80 EA 64 32 D9 
CF 3F FF BC 68 D1 22 9A 1E B6 6D DB 36 E4 47 31 08 A6 41 A3 D8 E5 A5 1D 1D 1D 55 AF 25 DC BF 7F 
7F 3A D1 86 DC 30 44 13 13 93 B9 73 E7 D2 64 8F B8 B8 B8 21 43 86 4C 98 30 21 3A 3A FA C9 93 27 
74 60 D9 9B 37 6F 9E 3C 79 72 EC D8 31 0F 0F 8F 59 B3 66 91 62 CF 5C 2E 77 CA 94 29 1A BA 9B 5F 
53 53 73 F0 E0 C1 33 67 CE 90 D5 C0 C0 40 5A 1E C1 D9 D9 79 F6 EC D9 64 F9 E8 D1 A3 74 C4 06 50 
36 36 36 F4 1A 49 22 91 2C 5E BC D8 C3 C3 E3 D8 B1 63 4F 9E 3C A1 BD D4 55 55 55 79 79 79 47 8F 
1E F5 F0 F0 58 BC 78 31 CD 98 9F 32 65 8A 2A 77 3C BA 77 EF 4E 0B 4E A7 A5 A5 25 24 24 A4 A4 A4 
30 FF 2D 44 AD E2 CC 23 AD 9A 91 91 11 0D A6 C5 62 71 64 64 24 59 6E B0 8F 99 CE 2B 7E FB F6 ED 
E4 E4 64 A6 A1 59 C4 AB AB AB 37 6F DE 4C 3F E7 8B 16 2D 9A 34 69 52 7D 1B B3 27 0D 4D 4B 4B 0B 
0F 0F D7 5C F1 4A B9 4E 35 DC 9E 06 68 14 A1 50 B8 7C F9 72 F2 7B DA 36 27 67 69 40 83 63 C2 A0 
95 7A C7 E3 5B 5A 5A 3A 6E DC B8 C6 7E 9C C6 8D 1B 57 5A 5A 2A 93 C9 E2 E3 E3 69 07 F3 D6 AD 5B 
1B F5 5F 6F DD BA 95 EE 70 CB 96 2D B5 B5 B5 F4 A9 DA DA DA A8 A8 28 15 EF 1E B2 05 04 04 BC 7C 
F9 52 95 FF 3D 2B 2B 8B 8E 86 39 7E FC B8 2A 2F 49 4C 4C A4 E1 C5 9C 39 73 E4 FE A3 C2 C2 42 3A 
A3 04 9F CF 7F F0 E0 41 A3 FE 1A F5 69 81 DF 5F 7A 13 80 7E 0C 54 54 54 54 44 F2 61 34 74 4C 65 
32 59 5A 5A 1A 4D 1A A6 13 FE 79 7B 7B 97 97 97 AB F5 5E 35 AE C9 8F 6F 5C 5C 9C DC 1F D0 C2 C2 
E2 D6 AD 5B CA 5F 55 5D 5D 1D 18 18 C8 7E D5 8A 15 2B A4 52 69 9D 1B CB 7D 3D BD BC BC 8A 8A 8A 
94 EF FF C9 93 27 64 D2 50 E2 D8 B1 63 EC EF BB 12 EC 13 D4 DA B5 6B 1B DC FE D5 AB 57 F3 E6 CD 
6B EC 67 4C CE BC 79 F3 5E BD 7A A5 4A F3 1A D4 E4 C7 B7 25 60 9F 3C 55 FC 5B C9 FD D0 A4 A4 A4 
34 43 3B 9B 81 EE 1D 5F D2 01 A1 9E C6 FE 22 B4 7C EC E3 8B 9E 69 D0 94 37 6F DE 5C B8 70 81 74 
1F 5A 5B 5B 8F 19 33 A6 51 2F 1F 3B 76 2C BD 79 24 37 0C 91 C3 E1 4C 99 32 65 D7 AE 5D 4A 4A 0B 
2B 0A 0E 0E DE B4 69 93 86 EE E7 B2 6F 6A D7 99 1E DA BD 7B F7 6F BF FD 96 44 6F 9A EE 7E 6B A5 
CC CD CD 37 6F DE CC AE 61 D7 A0 80 80 80 D0 D0 50 D5 8F A9 B5 B5 B5 A3 A3 23 59 A6 B3 6A B7 85 
A1 87 14 ED 63 A6 14 67 11 57 C4 9E 57 9C 50 32 8B 78 56 56 D6 A6 4D 9B 68 95 8C A0 A0 A0 06 F3 
29 D9 93 86 32 EF 36 2D 22 00 40 F3 43 30 0D 9A 52 50 50 40 32 32 19 86 71 76 76 A6 E5 1A 54 64 
65 65 45 33 5C E3 E3 E3 D3 D3 D3 D9 CF 1A 18 18 CC 98 31 E3 F6 ED DB 33 67 CE 6C B0 8B 7A C4 88 
11 97 2F 5F 6E 54 D4 D5 28 52 A9 F4 C0 81 03 E4 A6 B6 92 C9 0E 47 8E 1C 39 73 E6 4C B2 1C 11 11 
11 1D 1D 2D AB 3F D5 BB 6D B2 B6 B6 FE CF 7F FE B3 75 EB D6 06 2F 93 6C 6C 6C A2 A2 A2 54 D9 92 
CD D4 D4 94 8E 6D 25 DA C8 D0 43 AA 6B D7 AE BD 7B F7 66 3F 52 E7 2C E2 8A E8 BC E2 64 B9 BE 01 
8B 64 6A 6E 32 61 07 C3 30 21 21 21 4E 4E 4E AA 34 8C 3D 69 68 66 66 E6 9A 35 6B 4A 4A 4A 54 79 
21 00 80 D6 21 98 06 4D B9 7A F5 2A 1D 2F EF E2 E2 D2 D8 40 D6 D8 D8 F8 F3 CF 3F A7 AB 57 AE 5C 
51 1C 91 66 65 65 75 E8 D0 A1 87 0F 1F C6 C4 C4 04 04 04 B8 B9 B9 D1 D0 8A C7 E3 7D FA E9 A7 1B 
37 6E BC 7F FF FE D5 AB 57 DD DD DD 95 4C EA F1 8E AE 5E BD 4A A7 47 F6 F5 F5 F5 F2 F2 AA 73 9C 
A5 81 81 01 69 24 59 FD F1 C7 1F 9B 61 2E C6 56 C7 D8 D8 38 30 30 30 2F 2F 2F 36 36 36 28 28 88 
7D 4C CD CC CC DC DC DC 56 AC 58 91 90 90 70 E7 CE 1D 1F 1F 1F 35 E6 58 19 33 66 0C 3B 77 BF 8D 
0C 3D A4 D8 33 1A 12 75 CE 22 AE E8 FD F7 DF A7 01 74 7D 9D D9 52 A9 F4 C8 91 23 EC 49 1C 7C 7C 
7C 54 AC 92 61 60 60 E0 E7 E7 47 F3 7C A2 A3 A3 0F 1D 3A 84 BA EC 00 D0 2A FC EF 69 0E 3D 64 BA 
8A FC 92 E1 F8 EA 2A 1C 5F DD 86 E3 AB DB 70 7C 75 1B 8E AF 6E 63 1F 5F F4 4C 03 00 00 00 00 A8 
09 C1 34 00 00 00 00 80 9A 10 4C 03 00 00 00 00 A8 09 C1 34 00 00 00 00 80 9A 10 4C 03 00 00 00 
00 A8 09 C1 34 00 00 00 00 80 9A 10 4C 03 00 00 00 00 A8 09 C1 34 00 00 00 00 80 9A 10 4C 03 00 
00 00 00 A8 09 C1 34 00 00 00 00 80 9A 10 4C 03 00 00 00 00 A8 09 C1 34 00 00 00 00 80 9A 10 4C 
03 00 00 00 00 A8 09 C1 34 00 00 00 00 80 9A 10 4C 03 00 00 00 00 A8 09 C1 34 00 00 00 00 80 9A 
10 4C 03 00 00 00 00 A8 09 C1 34 00 00 00 00 80 9A 10 4C 03 00 00 00 00 A8 09 C1 34 00 00 00 00 
80 9A 10 4C 03 00 00 00 00 A8 09 C1 34 00 00 00 00 80 9A 10 4C 03 00 00 00 00 A8 09 C1 34 00 00 
00 00 80 9A 10 4C 03 00 00 00 00 A8 09 C1 34 00 00 00 00 80 9A 10 4C 03 00 00 00 00 A8 09 C1 34 
00 00 00 00 80 9A 10 4C 03 00 00 00 00 A8 09 C1 34 00 00 00 00 80 9A 10 4C 03 00 00 00 00 A8 09 
C1 34 00 00 00 00 80 9A 10 4C 03 00 00 00 00 A8 09 C1 34 00 00 00 00 80 9A 10 4C 03 00 00 00 00 
A8 09 C1 34 00 00 00 00 80 9A 10 4C 03 00 00 00 00 A8 09 C1 34 00 00 00 00 80 9A 10 4C 03 00 00 
00 00 A8 09 C1 34 00 00 00 00 80 9A 10 4C 03 00 00 00 00 A8 89 A3 ED 06 00 00 00 00 00 B4 3E 32 
99 8C 41 CF 34 00 00 00 00 80 DA 0C C8 3F 24 B2 06 DD C3 E1 70 18 1C 5F DD 85 E3 AB DB 70 7C 75 
1B 8E AF 6E C3 F1 D5 6D E4 F8 12 E8 99 06 00 00 00 00 50 13 82 69 00 00 00 00 00 35 21 98 06 00 
00 00 00 50 13 82 69 00 00 00 00 00 35 21 98 06 00 00 00 00 50 13 82 69 00 00 00 00 00 35 21 98 
06 00 00 00 00 50 13 82 69 00 00 00 00 00 35 21 98 06 00 00 00 00 50 13 82 69 00 00 00 00 00 35 
21 98 06 00 00 00 00 50 13 82 69 00 00 00 00 00 35 21 98 06 00 00 00 00 50 13 82 69 00 00 00 00 
00 35 21 98 06 00 00 00 00 50 13 82 69 00 00 00 00 00 35 21 98 06 00 00 00 00 50 13 82 69 00 00 
00 00 00 35 21 98 06 00 00 00 00 50 13 82 69 00 00 00 00 00 35 21 98 06 00 00 00 00 50 13 82 69 
00 00 00 00 00 35 21 98 06 00 00 00 00 50 13 82 69 00 00 00 00 00 35 21 98 06 00 00 00 00 50 13 
82 69 00 00 00 00 00 35 21 98 06 00 00 00 00 50 13 82 69 00 00 00 00 00 35 21 98 06 00 00 00 00 
50 13 82 69 00 00 00 00 00 35 21 98 06 00 00 00 00 50 13 82 69 00 00 00 00 00 35 21 98 06 00 00 
00 00 50 13 82 69 00 00 00 00 00 35 21 98 06 00 00 00 00 50 13 82 69 00 00 00 00 00 35 21 98 06 
00 00 00 00 50 13 82 69 00 00 00 00 00 35 21 98 06 0D AA AA AA F2 F7 F7 E7 34 A4 73 E7 CE A3 47 
8F 5E B0 60 C1 A9 53 A7 9E 3D 7B D6 54 BB AD 8F BF BF 7F 55 55 15 7B 87 22 91 68 D0 A0 41 E4 59 
81 40 A0 B1 BF 07 34 8E 54 2A 15 08 04 4B 96 2C 19 3C 78 30 39 3A FD FA F5 9B 39 73 66 5C 5C 9C 
DC 11 04 80 56 4A 20 10 98 98 98 70 38 9C A8 A8 28 6D B7 A5 95 69 F2 9F C2 B2 B2 32 4F 4F 4F F2 
6C FF FE FD FF FC F3 4F 15 5B C2 FE 0D 65 1F C7 A8 A8 28 B5 9B 57 5F 23 5B 26 04 D3 A0 7D E5 E5 
E5 09 09 09 11 11 11 D3 A6 4D FB F0 C3 0F 67 CD 9A 95 9F 9F AF ED 46 81 96 DD BD 7B D7 DB DB DB 
C5 C5 65 E7 CE 9D 77 EE DC 21 0F 8A 44 A2 23 47 8E 8C 1B 37 CE DE DE FE EC D9 B3 B5 B5 B5 DA 6D 
24 00 BC A3 9B 37 6F 4A 24 12 6B 6B EB 81 03 07 6A BB 2D F0 FF 65 66 66 6E D9 B2 A5 A2 A2 42 DB 
0D 69 1D 10 4C 43 CB 22 91 48 0E 1F 3E EC E9 E9 79 F1 E2 45 99 4C A6 ED E6 80 76 64 66 66 FA FB 
FB C7 C6 C6 D6 B7 81 48 24 9A 35 6B D6 A9 53 A7 F0 21 01 68 BD 24 12 09 B9 54 B6 B3 B3 E3 F1 78 
DA 6E 0E FC 1F 91 91 91 E7 CF 9F 6F E1 E7 D8 AA AA AA 96 D0 75 8D 60 1A 5A 22 91 48 E4 EF EF 7F 
ED DA 35 6D 37 04 B4 A0 A4 A4 24 24 24 24 2D 2D 4D F9 66 12 89 64 DD BA 75 19 19 19 CD D3 2A 00 
68 72 4F 9F 3E 25 B9 04 C3 87 0F 37 31 31 D1 76 73 40 DE 8F 3F FE 98 95 95 A5 ED 56 D4 AB BA BA 
7A F9 F2 E5 EB D6 AD 93 4A A5 DA 6D 09 82 69 68 26 F3 E6 CD 7B F5 EA 95 AC 2E AF 5E BD 7A FC F8 
F1 7F FE F3 9F CF 3E FB 8C 6E 2F 16 8B BF FF FE FB CC CC 4C B5 77 5B 9F BD 7B F7 1A 19 19 69 F8 
ED 82 FA CE 9F 3F 1F 1D 1D 4D 96 CD CC CC 42 43 43 1F 3D 7A 54 53 53 53 5B 5B 5B 5A 5A 7A E8 D0 
21 1B 1B 1B F2 6C 66 66 E6 D9 B3 67 6B 6A 6A B4 D7 58 00 50 DF AD 5B B7 84 42 21 97 CB E5 F3 F9 
1C 0E 47 DB CD 69 C5 34 F4 53 28 14 0A B7 6D DB 56 59 59 A9 5E AB BE FA EA AB FA FE F7 AC AC 2C 
3B 3B 3B B2 D9 F1 E3 C7 D5 6B A4 40 20 38 73 E6 4C 54 54 D4 DD BB 77 D5 6B 61 53 41 30 0D DA 67 
64 64 D4 B3 67 4F 6F 6F EF E8 E8 E8 A8 A8 28 7A B3 2F 2D 2D 6D C7 8E 1D 2D E1 0E 0E 34 9B 17 2F 
5E 5C BC 78 91 2C F3 78 BC 33 67 CE 84 84 84 BC FF FE FB 7A 7A 7A 1C 0E A7 73 E7 CE 33 67 CE 3C 
7B F6 2C 9F CF 27 DB 5C B9 72 E5 C9 93 27 DA 6B 2F 40 9B C6 1E B2 D6 D8 11 84 6F DE BC B9 7D FB 
36 C3 30 43 86 0C E9 DD BB B7 66 1A 08 EF EA C0 81 03 D1 D1 D1 B2 96 97 EC 51 5C 5C BC 73 E7 CE 
C2 C2 42 B1 58 1C 16 16 56 52 52 A2 C5 C6 20 98 86 16 C4 C0 C0 60 DA B4 69 61 61 61 5C 2E 97 3C 
72 E2 C4 89 D4 D4 54 ED B6 0A 9A D3 C3 87 0F 69 41 95 90 90 10 37 37 37 C5 FE AA 01 03 06 AC 5D 
BB 96 7C 48 52 53 53 85 42 61 73 B7 12 00 DE 59 69 69 29 49 98 B6 B7 B7 EF D2 A5 8B B6 9B 03 FF 
87 A7 A7 27 ED B3 08 0F 0F 6F 69 C9 1E 95 95 95 6B D7 AE 8D 89 89 21 AB D1 D1 D1 87 0E 1D D2 62 
B2 07 82 69 68 59 38 1C CE 94 29 53 42 42 42 C8 AA 44 22 39 7F FE 7C 75 75 B5 76 5B 05 CD 26 2B 
2B AB B0 B0 90 61 18 5B 5B 5B 27 27 A7 FA EE FC 0E 1D 3A D4 DD DD 9D 2C DF B8 71 03 99 1E 00 AD 
4E 5E 5E 1E ED 99 6E D7 AE 9D B6 9B 03 FF C7 F0 E1 C3 17 2F 5E 4C FA 2C D2 D2 D2 C2 C3 C3 D5 4E 
F6 68 72 52 A9 34 3C 3C 3C 22 22 82 FD E0 0F 3F FC 70 FA F4 69 6D F5 A0 23 98 86 16 C7 C0 C0 60 
CA 94 29 F4 9A F8 D6 AD 5B 45 45 45 DA 6D 12 34 8F 9A 9A 9A FB F7 EF 93 65 07 07 87 5E BD 7A D5 
B7 E5 7B EF BD 37 78 F0 60 B2 FC E7 9F 7F A2 7E 13 40 AB 83 A2 78 2D 19 87 C3 F1 F2 F2 9A 3A 75 
2A 59 3D 76 EC 58 4C 4C 4C 4B 48 F6 A8 AD AD 3D 75 EA D4 0F 3F FC C0 FC B7 08 0C 8F C7 B3 B3 B3 
93 48 24 FE FE FE 27 4F 9E D4 4A 23 11 4C 43 4B D4 AB 57 AF B1 63 C7 92 E5 D4 D4 54 B1 58 AC DD 
F6 40 F3 A8 AE AE A6 79 6F 7D FA F4 E9 D8 B1 63 7D 5B 72 38 1C 6B 6B 6B B2 5C 54 54 54 56 56 D6 
1C ED 03 80 26 82 A2 78 2D 9F B1 B1 71 60 60 20 19 26 28 91 48 76 EE DC A9 F5 64 8F DA DA DA 13 
27 4E 04 04 04 48 24 92 80 80 80 D3 A7 4F F7 EB D7 AF 5F BF 7E C7 8F 1F 9F 35 6B 96 44 22 59 B4 
68 D1 CF 3F FF DC FC F1 34 82 69 68 89 F4 F5 F5 1D 1C 1C E8 6A 83 35 3D 40 37 54 55 55 3D 7E FC 
98 2C 5B 58 58 28 1F DD DF B3 67 4F B2 F0 F4 E9 D3 17 2F 5E 68 BC 71 00 D0 74 1E 3D 7A 74 EB D6 
2D 86 61 9C 9C 9C 3A 75 EA A4 ED E6 40 DD FA F5 EB F7 DD 77 DF 91 E5 B4 B4 B4 88 88 08 2D 96 04 
90 4A A5 87 0F 1F 0E 08 08 B0 B4 B4 3C 71 E2 C4 8E 1D 3B 3A 77 EE 4C 9E B2 B0 B0 88 88 88 88 8A 
8A EA DA B5 EB DC B9 73 9B 3F 7F 1A C1 34 B4 50 56 56 56 B4 EB B1 B0 B0 B0 25 DC 5D 02 4D 7B F9 
F2 A5 44 22 21 CB 4A BA A5 89 CE 9D 3B 93 BB C3 85 85 85 AF 5F BF D6 78 E3 00 A0 E9 DC BD 7B 37 
33 33 93 CB E5 0E 1B 36 4C DB 6D 81 7A 71 38 1C 6F 6F EF 39 73 E6 90 D5 A3 47 8F D2 31 7F CD EF 
C5 8B 17 D1 D1 D1 AB 56 AD 12 08 04 D3 A6 4D 33 30 30 60 3F 6B 68 68 E8 E3 E3 93 9C 9C BC 68 D1 
A2 E8 E8 E8 66 EE 61 41 30 0D 2D 94 A1 A1 61 87 0E 1D C8 72 51 51 51 7D D1 D2 BE 7D FB 3A 74 E8 
C0 51 99 BF BF 3F 6A ED B5 58 AF 5F BF A6 63 5C 68 45 97 FA 70 38 1C 3D 3D 9C C1 00 5A 1F 14 C5 
6B 72 9A FB 29 34 36 36 5E B8 70 A1 AD AD 2D C3 30 12 89 64 FB F6 ED 39 39 39 1A 7E 37 75 EB D4 
A9 D3 A9 53 A7 82 82 82 68 87 B4 A2 AE 5D BB FE F0 C3 0F 47 8F 1E 6D B0 3B A6 69 E1 A7 08 5A 28 
2E 97 6B 6A 6A AA ED 56 80 D6 28 39 5D 2A CA CF CF D7 58 43 00 80 A9 AA AA F2 F7 F7 57 8C C9 BA 
74 E9 72 E9 D2 25 B2 CD D7 5F 7F 5D 67 DC 46 8B 5D 52 28 8A D7 BA 0C 1C 38 30 30 30 90 2C A7 A5 
A5 ED DC B9 53 2B 7D 52 06 06 06 2A 86 C8 9D 3B 77 36 34 34 D4 74 7B D8 10 4C 43 0B 65 68 68 D8 
CC 5F 06 00 00 68 06 28 8A D7 BA 70 38 9C 2F BF FC 72 FA F4 E9 64 F5 E8 D1 A3 71 71 71 DA 6D 52 
4B 83 60 1A 5A A8 E7 CF 9F 97 96 96 6A BB 15 D0 3A C8 25 CF 01 40 4B 46 8A E2 D9 DA DA 0E 1A 34 
48 DB 6D 01 95 98 98 98 2C 5D BA 94 26 7B 6C DE BC 19 F7 03 D9 10 4C 43 0B 55 53 53 43 47 E3 EA 
EB EB D7 57 D8 61 DE BC 79 AF 5E BD 92 A9 6C EF DE BD 46 46 46 CD F8 3E 40 4D AF 5E BD 52 7D 63 
5A D9 03 00 34 C1 C8 C8 68 EF DE BD 8A 67 D4 D2 D2 D2 71 E3 C6 91 6D 8E 1F 3F 5E E7 59 D7 D9 D9 
99 BD AB 17 2F 5E 90 79 6D 95 D7 92 87 46 69 86 9F C2 81 03 07 CE 9B 37 8F 2C 0B 04 82 F0 F0 70 
CC A7 46 E9 42 30 5D 5F 2E D7 BB F0 F4 F4 44 E5 5A ED 7A FE FC 79 6E 6E 2E 59 EE DE BD 7B FB F6 
ED B5 DB 1E 68 06 EC 44 F9 67 CF 9E 29 DF 58 26 93 D5 D6 D6 6A BE 51 00 D0 94 C4 62 B1 50 28 64 
18 C6 DE DE 5E 6E 9C B1 40 20 50 FE D3 1C 1A 1A AA A5 56 03 C3 E1 70 A6 4F 9F 3E 79 F2 64 B2 BA 
7F FF FE 8B 17 2F 6A B7 49 2D 87 2E 04 D3 A0 93 FE FA EB 2F 5A 25 0D 25 FD DB 08 76 A2 7C 83 33 
84 97 95 95 65 64 64 30 0C 63 6D 6D DD 60 E9 0F 00 68 21 32 32 32 72 72 72 50 14 AF 35 32 35 35 
5D B6 6C 19 F9 45 46 B2 07 1B 82 69 68 89 AA AB AB 6F DE BC 49 96 B9 5C 6E DF BE 7D B5 DB 1E 68 
1E 1D 3A 74 B0 B2 B2 22 CB B9 B9 B9 CA 8B 8B D3 7B 47 26 26 26 B4 8A 22 00 B4 64 28 8A D7 DA 0D 
19 32 84 56 F6 10 08 04 07 0E 1C 68 E6 E9 51 5A 26 8C DA 81 96 E8 E1 C3 87 97 2F 5F 26 CB 7C 3E 
1F 3D D3 6D 44 FB F6 ED BB 77 EF 4E 96 73 73 73 5F BE 7C A9 A4 CB F9 FE FD FB 64 A1 7B F7 EE 8D 
AA A3 07 00 DA A2 BC 28 9E B3 B3 33 E6 E7 6A E1 48 B2 87 40 20 38 73 E6 0C C3 30 BB 76 ED 72 75 
75 C5 6F 34 7A A6 EB C0 E5 72 A7 4F 9F 6E 66 66 A6 ED 86 B4 51 52 A9 34 3A 3A 9A 4E 21 3E 7C F8 
F0 6E DD BA 69 B7 49 D0 3C 38 1C 0E 19 2D CE 30 CC 9F 7F FE F9 F4 E9 D3 FA B6 94 48 24 F4 13 D2 
B7 6F 5F 63 63 E3 E6 68 1F 00 BC 1B 14 C5 D3 01 A6 A6 A6 4B 96 2C A1 C9 1E 1B 36 6C 78 F2 E4 89 
B6 1B A5 65 BA 10 4C D7 37 CA 58 45 0F 1E 3C E0 F3 F9 EC 1D 86 84 84 4C 99 32 A5 BE F2 11 A0 51 
32 99 2C 31 31 31 22 22 82 AC F2 78 BC 09 13 26 E8 EB EB 6B B7 55 D0 6C 6C 6D 6D C9 34 F2 42 A1 
F0 DA B5 6B F5 75 53 DD B9 73 27 3E 3E 9E 2C E3 57 19 A0 55 90 C9 64 69 69 69 12 89 C4 CE CE CE 
C1 C1 41 DB CD 01 F5 39 3A 3A 2E 58 B0 80 2C 27 24 24 84 86 86 36 AA FE 92 EE D1 85 60 FA 5D 14 
17 17 AF 58 B1 22 2D 2D 8D 3E 12 10 10 B0 70 E1 42 94 AD D5 8A EA EA EA A8 A8 A8 D9 B3 67 17 16 
16 92 47 26 4D 9A 34 70 E0 40 ED B6 0A 9A 53 EF DE BD 1D 1D 1D C9 F2 0F 3F FC 90 90 90 A0 18 4F 
DF BF 7F 3F 38 38 98 7C 48 50 AA 16 A0 B5 A8 A8 A8 B8 7E FD 3A C3 30 1F 7F FC B1 A5 A5 A5 B6 9B 
03 EA D3 D7 D7 F7 F3 F3 F3 F6 F6 26 AB 49 49 49 DA 9A 63 BC 85 68 D3 C1 74 65 65 E5 DA B5 6B 63 
62 62 E8 23 5E 5E 5E AB 57 AF C6 2D E3 66 F6 F2 E5 CB BC BC BC A3 47 8F 7A 78 78 F8 FA FA 8A C5 
62 F2 38 9F CF 9F 37 6F 1E E6 41 6C 53 B8 5C AE AB AB 2B 59 16 8B C5 13 27 4E 5C B6 6C 59 6E 6E 
6E 6D 6D AD 4C 26 2B 2B 2B 3B 7C F8 F0 3F FE F1 0F 3A 41 F1 A7 9F 7E FA E1 87 1F 6A AF BD 00 6D 
5A E7 CE 9D 2F 5E BC 48 6E F3 7E F5 D5 57 CA 37 56 52 14 0F 5A 9D AE 5D BB 2E 5D BA 14 D9 D2 44 
DB 0D A6 65 32 D9 C1 83 07 69 3A 01 C3 30 3C 1E 2F 28 28 C8 DC DC 5C 8B AD D2 61 FB F6 ED EB D0 
A1 43 9D A5 43 B9 5C 6E 9F 3E 7D FC FC FC 92 93 93 E9 F6 3C 1E 6F E3 C6 8D E4 8E BF 7A BB 55 22 
2A 2A AA BE 1D BA B8 B8 A8 B8 13 7F 7F FF AA AA AA 26 FB 03 C1 7F 7D FE F9 E7 13 26 4C 20 CB 12 
89 E4 C7 1F 7F FC E0 83 0F F4 F5 F5 F5 F4 F4 BA 74 E9 32 6B D6 2C 91 48 44 9E B5 B5 B5 9D 3E 7D 
3A 2E B7 5A B5 B2 B2 32 4F 4F 4F F2 9D 42 81 7F DD 86 A2 78 9A D3 E4 3F 85 AA E0 F3 F9 F3 E7 CF 
6F AA B7 D0 AA B5 DD 60 3A 35 35 75 DB B6 6D EC 47 42 42 42 9C 9C 9C B4 D5 1E 60 B3 B3 B3 3B 79 
F2 24 ED A1 84 36 A5 5B B7 6E DF 7E FB 6D 83 1D 1E 5C 2E 77 E5 CA 95 C8 02 02 68 15 50 14 4F F7 
18 18 18 F8 F9 F9 79 79 79 69 BB 21 DA D7 46 83 E9 92 92 92 2D 5B B6 D0 74 02 86 61 A6 4F 9F FE 
E5 97 5F 72 30 E8 50 DB CC CC CC 82 83 83 2F 5F BE 3C 7C F8 70 6D B7 05 B4 66 E4 C8 91 27 4E 9C 
18 3A 74 68 7D 1B D8 D8 D8 1C 3A 74 68 EA D4 A9 F8 CE 02 B4 0A CA 8B E2 41 2B 65 6E 6E 1E 18 18 
88 64 8F B6 38 CC AE A6 A6 E6 C8 91 23 D1 D1 D1 F4 11 5B 5B DB A5 4B 97 9A 98 98 68 B1 55 6D 19 
8F C7 FB E8 A3 8F 86 0E 1D 3A 6A D4 A8 A1 43 87 22 67 1D 38 1C 8E 93 93 53 72 72 F2 B5 6B D7 7E 
F9 E5 97 EB D7 AF 93 9F 61 1B 1B 1B 7B 7B 7B 2F 2F AF 4F 3F FD 14 5F 58 80 56 84 16 C5 73 71 71 
41 F9 1D 5D E2 EC EC 3C 7B F6 EC 55 AB 56 69 BB 21 DA F4 BF 9D 3A 6D AA 4C FA AD 5B B7 26 4D 9A 
C4 EE 96 DE BE 7D FB E2 C5 8B 75 B2 8B 8B BC A9 36 75 7C DB 14 1C 5F DD 86 E3 AB DB 70 7C 75 1B 
8E AF A6 95 95 95 91 61 AF 51 51 51 CD 3F 75 17 FB F8 B6 B9 34 8F CA CA CA FD FB F7 B3 23 E9 09 
13 26 4C 9B 36 4D 27 23 69 00 00 00 00 D0 A8 36 17 4C C7 C7 C7 9F 3A 75 8A AE 72 B9 DC 05 0B 16 
60 82 3D 00 00 00 00 50 43 DB 0A A6 9F 3D 7B 76 E8 D0 21 89 44 42 1F F1 F1 F1 19 31 62 84 16 9B 
04 00 00 00 00 AD 57 DB 0A A6 7F FD F5 D7 F3 E7 CF D3 55 1E 8F 37 7B F6 6C 23 23 23 2D 36 09 00 
00 00 00 5A AF 36 14 4C 17 14 14 C8 D5 27 FF EA AB AF 30 11 31 00 00 00 00 A8 AD 0D 05 D3 17 2F 
5E 4C 48 48 A0 AB B6 B6 B6 5F 7E F9 A5 81 41 5B 2C 0E 08 00 00 00 00 4D A2 AD 04 D3 85 85 85 EC 
71 87 0C C3 78 7B 7B F7 EF DF 5F 5B ED 01 00 00 00 00 1D D0 56 FA 65 AF 5F BF 1E 1F 1F 4F 57 D1 
2D 0D 00 00 00 D0 7A 75 EC D8 71 CD 9A 35 64 41 BB 2D 69 13 D1 E4 F3 E7 CF E5 BA A5 3D 3C 3C 6C 
6C 6C B4 D5 1E 00 00 00 00 78 17 86 86 86 8E 8E 8E DA 6E 05 C3 B4 91 34 8F 3F FE F8 E3 E2 C5 8B 
74 95 CB E5 4E 98 30 C1 D0 D0 50 8B 4D 02 00 00 00 00 1D A0 FB C1 74 4D 4D 4D 52 52 12 BB B6 B4 
BB BB FB E0 C1 83 B5 D8 24 00 00 00 00 D0 0D BA 1F 4C 3F 7A F4 28 2E 2E 8E FD C8 F8 F1 E3 4D 4D 
4D B5 D5 1E 00 00 00 00 D0 19 BA 1F 4C DF B9 73 27 2D 2D 8D AE F2 F9 FC D1 A3 47 6B B1 3D 00 00 
00 00 A0 33 74 3C 98 AE AE AE 4E 4A 4A 62 3F C2 E7 F3 2D 2D 2D B5 D5 1E 00 00 00 00 D0 25 3A 1E 
4C 17 15 15 DD BA 75 8B FD C8 98 31 63 30 F4 10 00 00 00 00 9A 84 8E 07 D3 42 A1 30 35 35 95 AE 
3A 39 39 D9 D9 D9 69 B1 3D 00 00 00 00 A0 4B 74 39 98 AE A9 A9 B9 71 E3 06 FB 11 3E 9F 6F 61 61 
A1 AD F6 00 00 00 00 80 8E D1 E5 60 BA A2 A2 E2 CF 3F FF 64 3F 32 64 C8 90 76 ED DA 69 AB 3D 00 
00 00 00 A0 63 74 39 98 7E FC F8 71 76 76 36 5D B5 B6 B6 1E 38 70 A0 16 DB 03 8A A4 52 69 7A 7A 
7A 68 68 E8 F8 F1 E3 AD AC AC 38 1C 0E 87 C3 E9 D7 AF DF B4 69 D3 7E FA E9 A7 A2 A2 22 99 4C A6 
7C 0F A1 A1 A1 E4 55 FE FE FE 55 55 55 CD D3 EC B6 49 20 10 70 FE 6B C6 8C 19 15 15 15 2A BE 30 
2A 2A 8A BC 6A D0 A0 41 22 91 A8 51 CF 2A 41 0F BD A7 A7 67 59 59 59 7D CF 12 1E 1E 1E 85 85 85 
AA EF FC E9 D3 A7 6E 6E 6E EC 3D 84 86 86 AA FE F2 96 A0 CE 2F 97 95 95 D5 F8 F1 E3 43 43 43 D3 
D3 D3 A5 52 A9 F2 3D D0 43 A3 9C 89 89 C9 C8 91 23 67 CE 9C 79 EA D4 A9 67 CF 9E A9 D8 BC 9B 37 
6F 5A 5A 5A 92 3D 58 5A 5A DE BC 79 F3 5D DE AC 4C 26 7B FC F8 F1 BE 7D FB A6 4D 9B 36 78 F0 60 
B2 DB CE 9D 3B 7B 7A 7A 86 86 86 66 64 64 34 F8 66 D9 1F 6F 35 08 04 82 77 69 7F EB 75 F5 EA 55 
4B 4B CB C6 7E 79 05 02 81 89 89 09 87 C3 89 8A 8A D2 5C DB 74 43 59 59 99 A7 A7 27 FB C3 B6 7A 
F5 EA 9A 9A 1A D5 F7 70 F9 F2 E5 06 3F AE 4D FB F9 AF AA AA F2 F7 F7 27 4F 99 98 98 C8 95 27 56 
F1 CD 2A 9E 72 D9 BB 6D D4 2F BE F2 DD 36 09 5D 0E A6 F3 F3 F3 73 72 72 E8 AA 9D 9D 1D 8F C7 D3 
62 7B 80 AD B2 B2 72 CF 9E 3D 83 07 0F 1E 36 6C D8 EA D5 AB 7F FB ED 37 B1 58 4C 9E 12 89 44 A7 
4E 9D 9A 3D 7B 76 DF BE 7D FF F9 CF 7F E6 E7 E7 6B B5 A5 50 87 C8 C8 C8 9F 7F FE B9 C1 4B 9D 96 
23 3E 3E FE DE BD 7B AA 6F 7F FF FE FD C4 C4 44 8D 35 47 B3 6A 6B 6B E3 E3 E3 9D 9C 9C 14 BF 5C 
62 B1 F8 B7 DF 7E 5B BD 7A F5 B0 61 C3 9C 9C 9C E2 E3 E3 6B 6B 6B DF F1 BF 93 48 24 C9 C9 C9 47 
8E 1C 99 36 6D DA 87 1F 7E B8 7C F9 F2 F2 F2 72 E5 2F A9 A9 A9 89 8D 8D A5 97 37 85 85 85 71 71 
71 EA 7D 9C 6A 6B 6B 13 12 12 26 4C 98 D0 AB 57 2F 7F 7F FF 53 A7 4E DD B9 73 87 3C 55 5E 5E 7E 
E9 D2 A5 D5 AB 57 7F FC F1 C7 A3 47 8F 6E 92 37 0B 6C C5 C5 C5 3B 77 EE 6C D4 65 2A 71 F3 E6 4D 
89 44 82 1E 2E F5 24 27 27 17 17 17 AB B8 71 4D 4D 4D 42 42 82 46 DB A3 9C 44 22 D9 B0 61 43 41 
41 81 16 DB D0 0C 74 36 98 96 C9 64 7F FC F1 07 FB 11 6B 6B EB 8E 1D 3B 6A AB 3D 40 C9 64 B2 D4 
D4 54 37 37 B7 80 80 80 8C 8C 0C 25 5B 4A 24 92 C3 87 0F 7B 7A 7A 5E BC 78 B1 15 C5 6D 6D C4 EE 
DD BB B3 B2 B2 B4 DD 8A 46 48 48 48 50 B1 3B 47 EB 3F 3F EF A2 B2 B2 72 D5 AA 55 1E 1E 1E E9 E9 
E9 CA B7 4C 4F 4F F7 F0 F0 58 B5 6A 55 65 65 65 53 FD EF 12 89 64 E3 C6 8D B3 66 CD 52 FE 63 FF 
EC D9 B3 EB D7 AF B3 1F 49 4A 4A 2A 2A 2A 6A EC 7F 57 54 54 34 67 CE 9C D1 A3 47 C7 C6 C6 2A DF 
32 39 39 F9 8B 2F BE 08 0B 0B C3 FD AB A6 52 59 59 B9 76 ED DA 98 98 98 C6 BE 50 22 91 90 0B 1E 
F4 70 A9 27 31 31 F1 FE FD FB 2A 6E 5C 5C 5C 2C F7 5D 6B 7E 09 09 09 87 0F 1F 6E F0 EE 50 AB A6 
B3 C1 F4 CB 97 2F 73 73 73 D9 8F F4 EB D7 4F 5F 5F 5F 5B ED 01 42 26 93 FD FC F3 CF 9F 7F FE 79 
83 BF F4 94 48 24 F2 F7 F7 47 3C DD D2 08 85 C2 6D DB B6 35 61 1C A6 69 D7 AF 5F 57 B1 3B E7 D9 
B3 67 AA 7F 3E 5B 14 A9 54 1A 1E 1E 1E 16 16 A6 FA 4B C2 C2 C2 96 2F 5F DE B4 21 66 4C 4C CC BA 
75 EB 94 EC F3 FA F5 EB F1 F1 F1 0C C3 4C 9B 36 CD D3 D3 93 61 98 F8 F8 F8 C6 FE E4 8B 44 A2 49 
93 26 1D 3A 74 48 C5 ED 25 12 C9 AA 55 AB 36 6D DA 84 78 FA DD 55 56 56 86 84 84 44 44 44 A8 F1 
DA A7 4F 9F 92 E1 4C C3 87 0F 37 31 31 69 EA A6 B5 09 AA 77 0D 64 66 66 DE BE 7D 5B D3 ED 69 50 
44 44 C4 B5 6B D7 B4 DD 0A 0D D2 D9 60 BA BC BC FC AF BF FE A2 AB 5C 2E B7 6F DF BE 5A 6C 0F 10 
D7 AE 5D 93 BB 0B FC D9 67 9F 45 45 45 3D 7E FC B8 BA BA 5A 26 93 C9 64 B2 57 AF 5E 65 64 64 FC 
FB DF FF 36 33 33 23 DB 88 C5 E2 7F FF FB DF AD AB 1F B4 2D 38 70 E0 40 74 74 74 0B BF C8 B1 B5 
B5 1D 31 62 04 D3 98 EE 9C 07 0F 1E 90 69 53 47 8C 18 61 6B 6B AB D9 F6 35 A9 3F FE F8 63 C7 8E 
1D 74 75 DC B8 71 31 31 31 45 45 45 6F DF BE 25 5F AE B7 6F DF 16 15 15 C5 C4 C4 8C 1B 37 8E 6E 
76 F4 E8 51 E5 49 8D 76 76 76 59 59 59 B2 7A D4 D6 D6 96 97 97 FF F6 DB 6F 72 FB 64 97 25 65 63 
CF A5 E5 EA EA EA E1 E1 41 96 7F FD F5 57 D5 AF CD 8A 8B 8B BF FF FE 7B 76 A6 E6 C0 81 03 37 6E 
DC 98 91 91 21 91 48 E8 9B 7D FC F8 71 64 64 E4 D0 A1 43 E9 66 5B B6 6C 69 F0 43 9B 92 92 52 DF 
9B AD 8F B3 B3 B3 8A 2D D7 01 45 45 45 F3 E7 CF 67 7F D2 1A E5 D6 AD 5B 42 A1 90 CB E5 F2 F9 7C 
0E 87 D3 B4 6D D3 6D F4 8C A4 62 D7 40 4D 4D 4D 52 52 92 44 22 61 18 66 FC F8 F1 2A FE 2F 9A F8 
FC 17 16 16 6E DD BA 55 8D BB 4F AD 85 CE 06 D3 A5 A5 A5 79 79 79 74 B5 6F DF BE 5D BA 74 D1 62 
7B 80 61 98 9C 9C 9C EF BF FF 9E A6 6F DA D9 D9 C5 C5 C5 C5 C4 C4 F8 F8 F8 F4 EC D9 93 16 5A 31 
32 32 1A 30 60 C0 EA D5 AB D3 D3 D3 BD BD BD C9 83 69 69 69 3B 76 EC 40 97 52 4B F3 E3 8F 3F B6 
F0 8B 9C 5E BD 7A 91 BE 4F 86 61 7E FF FD F7 37 6F DE 28 DF 9E FD F3 E3 E9 E9 D9 AB 57 2F 8D 37 
B1 89 D4 D4 D4 FC F2 CB 2F 24 81 95 CB E5 EE DC B9 33 26 26 66 C2 84 09 E6 E6 E6 06 06 06 64 1B 
03 03 03 73 73 F3 09 13 26 C4 C4 C4 1C 3C 78 90 CB E5 32 0C 23 91 48 8E 1E 3D FA FC F9 73 F5 FE 
5F 0E 87 63 6A 6A FA C9 27 9F 9C 38 71 62 CE 9C 39 E4 41 89 44 72 E1 C2 85 3A FF DA 0F 1F 3E BC 
7C F9 32 C3 30 16 16 16 0E 0E 0E 2E 2E 2E A4 62 E9 A5 4B 97 54 BC DA A9 AA AA 5A B7 6E 1D 4D 30 
E0 72 B9 9B 37 6F BE 7E FD FA B2 65 CB 06 0C 18 40 D3 F9 0C 0C 0C 7A F6 EC E9 EB EB 9B 90 90 B0 
76 ED 5A FA 66 37 6D DA C4 1E 9B 0E AA 93 C9 64 A9 A9 A9 13 26 4C 38 76 EC 98 7A 7B 78 F3 E6 0D 
E9 28 1D 32 64 48 EF DE BD 9B B4 75 BA 6F E8 D0 A1 7C 3E 9F 61 98 C4 C4 44 B9 09 E9 EA 44 F3 A9 
6C 6D 6D 3F F9 E4 13 8D B7 4F A9 0B 17 2E 1C 3C 78 50 57 93 3D 74 36 98 2E 2F 2F 67 8F 8A E8 D2 
A5 8B A9 A9 A9 16 DB 03 52 A9 F4 C8 91 23 A4 C3 8F 61 18 67 67 E7 9F 7F FE D9 C3 C3 43 4F AF DE 
0F 61 9F 3E 7D F6 EC D9 E3 E5 E5 45 56 4F 9C 38 51 5F 5F 17 34 B3 AF BF FE 9A 84 26 42 A1 30 3C 
3C BC 85 27 7B B8 BA BA 92 D9 9A D2 D2 D2 1A 1C 2C F5 FC F9 73 92 E3 61 6B 6B EB E4 E4 D4 1C ED 
6B 22 EC 62 A0 3E 3E 3E B3 67 CF 56 32 DB AB A1 A1 E1 8C 19 33 96 2D 5B 46 56 E3 E3 E3 1F 3C 78 
F0 8E 0D 30 33 33 5B B8 70 21 ED CB CF C8 C8 78 F1 E2 85 E2 66 29 29 29 99 99 99 CC 7F 53 66 AD 
AD AD 1D 1D 1D 99 C6 0C 43 4C 4E 4E 3E 7A F4 28 FD 4F F7 EF DF BF 74 E9 52 63 63 E3 FA B6 37 36 
36 5E B1 62 45 48 48 08 59 15 0A 85 51 51 51 8D AA 87 00 0C C3 14 16 16 AE 58 B1 C2 D3 D3 93 7C 
41 B8 5C EE D7 5F 7F DD D8 9D 94 96 96 92 84 69 7B 7B 7B F4 70 35 D6 7B EF BD E7 EE EE 4E 96 13 
13 13 1B EC 1A C8 CD CD 25 BF B9 7C 3E FF C3 0F 3F D4 78 FB EA E2 E6 E6 E6 EA EA 4A 96 0F 1E 3C 
A8 AB 75 6F 74 36 98 96 FB C9 B4 B2 B2 EA D0 A1 83 B6 1A 03 0C C3 88 44 A2 E8 E8 68 B2 CC E3 F1 
36 6E DC 68 63 63 D3 E0 AB CC CD CD BF FD F6 5B D2 71 A5 A4 AF 0B 9A D9 D7 5F 7F ED EB EB 4B 96 
8F 1D 3B 16 13 13 D3 92 93 3D 78 3C 1E 09 D7 52 53 53 85 42 A1 F2 8D 45 22 11 39 DD F3 F9 FC D6 
D5 73 56 56 56 46 EF A2 8E 18 31 C2 C8 C8 48 F9 F6 06 06 06 DE DE DE 24 F6 95 48 24 8D AA 76 52 
1F 6B 6B EB 91 23 47 92 E5 92 92 12 C5 B2 1E CF 9F 3F BF 74 E9 12 59 1E 3A 74 A8 A9 A9 A9 A9 A9 
29 C9 C3 61 54 1B 86 58 59 59 79 F2 E4 49 72 EB 80 61 98 E5 CB 97 4F 9E 3C B9 C1 6C 01 03 03 83 
99 33 67 4E 98 30 81 AC 5E B9 72 E5 C9 93 27 2A BF 2D 60 6E DE BC 39 60 C0 80 8D 1B 37 92 BF BC 
8D 8D CD E9 D3 A7 FD FD FD 1B BB 9F BC BC 3C DA 33 8D 69 1F D4 E0 E0 E0 A0 62 D7 80 4C 26 4B 48 
48 20 C7 CB C5 C5 45 5B 05 18 FA F6 ED BB 6C D9 32 32 D2 54 2C 16 6F DB B6 4D F5 52 24 AD 88 CE 
06 D3 34 97 80 30 33 33 C3 F7 56 BB E2 E2 E2 48 77 14 C3 30 F3 E6 CD 23 C1 8D 2A F8 7C FE E4 C9 
93 19 86 E1 F1 78 95 95 95 F4 47 B4 49 9A 44 6A 9D 72 38 9C 2F BE F8 A2 A4 A4 A4 CE CD 8A 8B 8B 
27 4E 9C 48 36 EB DF BF BF DC 4C 40 6D 53 C7 8E 1D 17 2E 5C 48 CE E9 12 89 64 E7 CE 9D 2D 39 D9 
C3 C8 C8 88 86 6B CA BB 73 5A C8 CF 8F 7A 3A 75 EA 44 EF BF A9 D8 ED DA B3 67 CF 8F 3E FA 88 2C 
AB 5E 22 5A 09 23 23 A3 1E 3D 7A 90 65 A1 50 58 5A 5A 2A B7 41 4E 4E 0E 99 98 96 CB E5 BA BA BA 
92 41 E1 63 C6 8C B1 B6 B6 66 54 1B 86 98 95 95 45 C3 F1 09 13 26 CC 98 31 43 C5 91 FC AA B3 AD 
00 00 17 ED 49 44 41 54 E5 DD BA 75 9B 31 63 06 F9 AF 8D 8C 8C 74 38 7D 53 13 DE BE 7D 4B 2F 8D 
66 CD 9A 95 98 98 48 B3 A7 1A 45 B1 28 5E 41 41 C1 E8 D1 A3 C9 09 D6 CA CA AA BE 9E 4B A9 54 BA 
71 E3 46 5A D8 F8 C0 81 03 2D F9 02 5E 73 7A F5 EA A5 62 D7 40 59 59 19 F9 63 DA DA DA AA FE 83 
AB 09 2E 2E 2E B3 67 CF 26 CB 31 31 31 47 8E 1C D1 BD 64 0F DD 0C A6 65 32 99 DC 6F 89 91 91 11 
4A 79 68 11 AD 85 C4 30 8C 85 85 C5 D8 B1 63 55 3F 1C 86 86 86 41 41 41 05 05 05 B9 B9 B9 FB F6 
ED EB DC B9 73 53 B5 6A F4 E8 D1 F4 36 77 74 74 F4 89 13 27 14 CF CE 24 3B 85 66 67 06 07 07 A3 
30 2A D1 AF 5F BF EF BE FB 8E 2C A7 A5 A5 B5 F0 64 0F 27 27 27 92 6B 98 9A 9A AA A4 E2 29 FD F9 
B1 B6 B6 66 8F 5A 6B 15 DA B7 6F 4F EE E1 30 0C 73 E5 CA 15 55 66 D5 E9 D4 A9 D3 99 33 67 C8 10 
A2 55 AB 56 35 6D 7B AC AD AD 49 2E 10 C5 2E 2F ED EE EE 3E 78 F0 60 F2 F8 07 1F 7C 40 07 30 35 
38 0C F1 D6 AD 5B B4 43 6E D4 A8 51 DD BA 75 53 BD 49 1E 1E 1E D9 D9 D9 A5 A5 A5 F1 F1 F1 E4 F3 
00 8D F2 D9 67 9F A5 A7 A7 1F 38 70 A0 7B F7 EE 6A BC BC CE A2 78 3D 7A F4 58 B9 72 25 F9 E8 8A 
C5 E2 1D 3B 76 D4 99 BE 2F 10 08 F6 EC D9 43 96 E7 CC 99 E3 E3 E3 D3 36 07 2F 1A 19 19 8D 1D 3B 
96 2C 5F B9 72 A5 BA BA BA BE 2D E9 4D 36 07 07 07 ED 8E FD F8 9F FF F9 9F D9 B3 67 D3 11 90 7B 
F6 EC D1 BD 64 0F DD 0C A6 5F BF 7E 2D D7 EB 80 62 96 DA 55 5C 5C 4C 33 32 9D 9D 9D 1B 9B BC D5 
B3 67 4F 4B 4B 4B 25 D9 D5 EA 31 30 30 98 33 67 0E CD C9 DE B6 6D 9B 62 09 A1 6B D7 AE D1 41 EB 
01 01 01 DE DE DE 6D F3 0C AE 88 C3 E1 78 7B 7B D3 01 67 C7 8E 1D FB F5 D7 5F B5 DB 24 25 2C 2D 
2D 49 F0 94 96 96 46 AF EB 14 D1 9F 1F 47 47 C7 D6 95 E3 C1 30 0C 97 CB A5 F5 34 22 23 23 17 2D 
5A 94 9B 9B DB CC BD 77 12 89 84 4E 95 65 62 62 22 97 5C 57 5C 5C 9C 9C 9C 4C 96 5D 5C 5C DE 7B 
EF 3D B2 6C 6C 6C 4C 33 41 95 0F 43 7C FD FA 35 BD 35 64 61 61 41 53 4A 54 C4 E5 72 AD AD AD 71 
97 52 0D 16 16 16 A9 A9 A9 31 31 31 0E 0E 0E 6A 9F 8A 1F 3D 7A 44 86 CD 39 39 39 75 EA D4 89 3E 
3E 72 E4 C8 25 4B 96 90 E5 33 67 CE 44 46 46 CA 7D 6E 8B 8A 8A 36 6F DE 4C 6E 38 F3 F9 FC C0 C0 
40 25 29 F2 3A CF DE DE 9E 9E CD 9E 3E 7D 5A E7 36 EC 9B 6C CE CE CE 72 97 B5 CD AF 7B F7 EE 34 
63 93 5C 32 D5 77 2B B8 95 D2 CD 60 DA C8 C8 68 EF DE BD EC BA 2D D3 A7 4F D7 76 A3 DA B4 E2 E2 
62 1A A7 B6 A8 D9 73 CC CD CD 03 03 03 69 3A D7 A6 4D 9B D8 9D 22 05 05 05 EB D6 AD 23 DD 60 7C 
3E 7F E1 C2 85 6D F9 0C AE C8 D8 D8 38 30 30 90 26 7B 6C DF BE 9D 3D E7 68 8B 62 68 68 48 07 C1 
24 25 25 D5 D9 9D 23 93 C9 D2 D2 D2 5A CE CF 8F 1A 3E FD F4 53 92 13 C5 30 4C 64 64 E4 07 1F 7C 
30 61 C2 84 7D FB F6 E5 E7 E7 37 CF 7D 55 91 48 44 AB C9 F6 EE DD BB 6B D7 AE EC 67 6F DC B8 41 
E6 95 B4 B6 B6 76 77 77 67 5F 97 D2 5B 07 85 85 85 B1 B1 B1 F5 A5 A9 54 56 56 D2 9A A7 36 36 36 
B4 27 1E 34 AD 4F 9F 3E C3 87 0F 7F C7 1E 8D BB 77 EF 66 66 66 72 B9 DC 61 C3 86 B1 1F 37 30 30 
F0 F3 F3 AB AF 5F 43 2A 95 EE DA B5 EB C2 85 0B 0C C3 70 B9 DC C5 8B 17 F7 EB D7 EF 5D 9A D1 DA 
A9 D2 35 F0 F7 DF 7F 93 79 EB AC AD AD 87 0F 1F DE AC ED AB C7 C8 91 23 03 02 02 C8 72 74 74 F4 
91 23 47 74 69 10 B0 6E 06 D3 D0 D2 94 95 95 D1 E5 96 36 7B 8E 8B 8B CB 82 05 0B C8 F2 99 33 67 
CE 9E 3D 4B 3A 45 AA AB AB B7 6D DB 46 66 C2 E3 72 B9 DF 7C F3 4D EB 2A 39 DC 3C FA F5 EB 47 FF 
7A 69 69 69 3B 77 EE 6C B1 E5 0B 87 0C 19 42 AA 73 D4 D7 9D F3 F7 DF 7F A7 A4 A4 30 2D E9 E7 A7 
B1 4C 4D 4D 37 6F DE 4C 0B 4A 32 0C 13 1B 1B EB EF EF DF BB 77 6F 33 33 33 77 77 F7 D0 D0 50 81 
40 50 67 91 8D 77 27 16 8B D7 AC 59 43 C7 AB C8 4D C9 51 55 55 45 AB 59 3B 3B 3B 7F F0 C1 07 EC 
D7 F6 E8 D1 83 D6 4E B9 7E FD 7A 7D 09 DC 2F 5F BE A4 A3 26 3E FC F0 43 DA B7 DD B4 5C 5C 5C 38 
8D A1 7B F7 AC 35 41 79 51 3C 73 73 F3 A0 A0 20 DA AF B1 6B D7 2E 9A A7 74 E1 C2 85 5D BB 76 91 
E5 19 33 66 E0 F6 A0 A1 A1 E1 98 31 63 C8 72 7D 5D 03 74 70 82 1A 37 D9 34 F4 F9 27 83 80 DD DC 
DC C8 EA EE DD BB 49 0B 75 03 82 69 68 0E EC 51 83 2D 2A 92 66 18 46 5F 5F DF CF CF 8F C6 1F DB 
B6 6D 23 93 9C 47 47 47 EF DF BF 9F 3C 38 77 EE 5C 76 80 02 14 87 C3 F9 F2 CB 2F E9 9D 9F A3 47 
8F AA 31 BD 70 F3 B0 B0 B0 50 DE 9D F3 2E 3F 3F 2D 07 8F C7 3B 76 EC D8 D6 AD 5B E9 9C 47 84 44 
22 B9 72 E5 CA EA D5 AB 49 7E 85 A3 A3 E3 8E 1D 3B 94 A4 8F AB AE AA AA 2A 33 33 73 DB B6 6D E3 
C6 8D 23 DD 87 0C C3 D8 D9 D9 8D 1F 3F 9E 1D F4 E4 E6 E6 D2 4E 6B 17 17 17 B9 9B 3C ED DA B5 A3 
75 70 95 0C 43 7C FD FA 35 CD A8 D6 D7 D7 6F E3 41 55 EB D2 60 51 3C 47 47 47 7A 65 1E 19 19 F9 
F3 CF 3F CB 64 B2 9C 9C 9C F5 EB D7 D3 FB 45 4B 97 2E 6D B0 4C 4D 5B 60 67 67 A7 A4 6B 40 26 93 
A5 A4 A4 90 7B AA 2D EA 26 5B 8F 1E 3D 96 2F 5F 4E DA 23 16 8B B7 6C D9 A2 33 C9 1E 08 A6 01 98 
AE 5D BB 06 07 07 93 4E 91 CC CC CC F0 F0 F0 F4 F4 F4 ED DB B7 93 33 B8 9B 9B 5B 60 60 A0 92 92 
BD 6D 9C 89 89 C9 D2 A5 4B 69 85 B5 F0 F0 F0 FC FC 7C 6D 37 AA 0E ED DA B5 1B 35 6A 14 59 56 EC 
CE 69 B1 3F 3F 6A 20 E9 37 79 79 79 27 4F 9E 9C 38 71 62 9D EF 25 2D 2D 8D DC 6C 59 BE 7C 79 83 
BF 67 42 A1 B0 5F BF 7E F5 F5 4B 75 E8 D0 A1 7F FF FE DF 7E FB AD 48 24 A2 2F 59 B0 60 81 DC A4 
B3 B4 BC 34 9F CF 1F 3D 7A B4 E2 FF 32 60 C0 00 9A 39 DD A8 D9 10 A1 55 68 B0 28 9E BE BE FE EC 
D9 B3 69 9E D2 EE DD BB 6F DD BA B5 7D FB 76 52 29 99 CB E5 AE 5E BD DA CA CA AA 19 9B DC 72 29 
EF 1A 68 C9 37 D9 46 8F 1E BD 68 D1 22 B2 5C DF B8 FF D6 08 C1 34 00 C3 30 CC 90 21 43 E8 9C 0E 
A7 4E 9D 9A 3A 75 2A 39 83 5B 58 58 AC 5C B9 92 56 FB 82 3A 0D 1C 38 30 30 30 90 2C 0B 04 82 F0 
F0 70 25 63 CC B5 C8 C1 C1 81 C4 D3 49 49 49 72 11 7F 45 45 05 E9 0D 6D 81 3F 3F EA 31 31 31 99 
3A 75 6A 74 74 34 E9 11 DC BB 77 EF E4 C9 93 15 BB AB 37 6E DC E8 ED ED AD E2 D4 83 2A 0A 0E 0E 
96 2B B6 C0 2E 2F CD E7 F3 2D 2D 2D 15 5F D5 BD 7B 77 9A D7 AE FA 6C 88 D0 5A 90 A2 78 B6 B6 B6 
83 06 0D AA 6F 1B 53 53 D3 95 2B 57 92 2B 73 A1 50 38 75 EA 54 3A D5 E2 B2 65 CB EA BC 06 6B 9B 
D8 77 72 E2 E2 E2 E4 92 EB 72 73 73 5B EC 4D 36 03 03 83 80 80 00 9A EC 51 E7 B8 FF D6 08 C1 34 
34 87 F7 DF 7F 9F 2E BF 7C F9 52 8B 2D A9 0F 87 C3 F1 F1 F1 21 B5 29 24 12 49 6E 6E 2E 79 7C C9 
92 25 8D AD 18 D0 06 71 38 9C 49 93 26 D1 2E A5 FD FB F7 5F BC 78 51 C5 D7 36 AA B4 D9 3B 32 37 
37 27 81 B2 50 28 94 9B 8C F7 E1 C3 87 24 F3 8F 5D B4 4B 37 B4 6B D7 6E D0 A0 41 F3 E6 CD 3B 7D 
FA 74 49 49 49 41 41 41 54 54 14 BB C7 5A 20 10 CC 9B 37 AF 49 EE 27 D8 D8 D8 44 45 45 AD 5E BD 
5A 2E 8B E3 C1 83 07 F1 F1 F1 64 79 E7 CE 9D ED DB B7 57 EC E1 D6 D3 D3 A3 E5 F9 EA 1B 86 68 66 
66 46 07 35 BE 7A F5 4A 43 A3 2A 53 52 52 64 8D 41 EB FA 41 7D 5E BC 78 41 E6 AF 6D B0 4C DB C0 
81 03 83 83 83 C9 72 6E 6E 2E B9 3D E8 E5 E5 35 67 CE 1C 03 03 83 66 68 6A 6B F1 D1 47 1F 91 AE 
81 1B 37 6E 3C 7A F4 88 FD D4 B5 6B D7 C8 4D 36 7B 7B 7B 35 6E B2 69 FA F3 DF A3 47 8F 25 4B 96 
D0 64 0F B9 71 FF 4A B4 6B D7 4E AE 3B A0 E5 40 30 0D CD E1 BD F7 DE 23 93 32 30 0C 23 16 8B 5B 
E6 18 5E 72 73 9C 5D 7D D6 CB CB CB CF CF 0F 67 70 55 98 9A 9A D2 69 AE 24 12 C9 E6 CD 9B 55 0C 
CE 9A 73 6A 52 7D 7D FD 31 63 C6 90 93 78 72 72 32 BB 3B 87 FE FC C8 15 ED D2 31 7A 7A 7A 96 96 
96 3E 3E 3E D1 D1 D1 F7 EE DD 9B 3B 77 2E 79 5C 20 10 FC BF F6 EE 3F AA A9 FA FF 03 F8 5D E3 44 
44 D3 14 94 38 14 50 69 43 3A 42 48 9C 24 E8 80 1D 72 1C E5 44 4B E3 20 27 59 FF 28 08 C4 C1 43 
1C CB CE B1 02 A3 45 E0 C2 D5 B2 03 A6 71 24 0A D1 0E 84 1D C3 83 CC 44 6A 18 75 CC 13 1B 07 CE 
81 61 05 16 1A 39 7E 98 C0 F6 FD E3 7D BE EF CF FD 8C ED EE EE BA 2D C6 E7 F9 F8 87 3B B8 1B DB 
EE AF D7 7D FF 78 BD 3E F9 E4 13 61 07 A6 54 2A DD BC 79 F3 1B 6F BC D1 D1 D1 F1 D3 4F 3F 65 65 
65 59 8D 89 9A 9B 9B FB E6 9B 6F 9C 2D B7 74 FE FC F9 F9 95 D2 D8 B9 B4 AF 5C B9 E2 C2 12 4E E0 
56 46 A3 91 54 18 71 18 DE 89 44 22 B9 5C 4E D3 3E 30 0C 13 16 16 B6 7B F7 EE A0 A0 20 B7 BF 4B 
AF 12 14 14 44 6A 51 59 35 0D D0 FB 16 01 B9 23 3D 26 35 35 95 9E 7C 6C 26 43 B4 49 2C 16 2F D8 
11 F3 08 A6 C1 13 02 03 03 E9 48 89 FE FE 7E 67 1B A7 6F DD BA 75 FA F4 69 BD 5E EF EE 5A E2 01 
01 01 EC 53 76 48 48 C8 C2 C9 E2 B7 F0 C5 C6 C6 DE CE 60 8F A9 A9 29 FE EB B3 0B 33 3D F0 C0 03 
FC CF B0 91 91 91 E4 7E 89 DD 9C E3 15 97 1F 97 0B 0D 0D 3D 70 E0 00 8D 5A 38 2A 6C 47 47 47 1B 
0C 06 7B ED 52 06 83 A1 B5 B5 F5 CD 37 DF 4C 4E 4E B6 B9 21 D8 E9 A5 F9 D3 6A B5 F3 27 FB DF 7D 
F7 DD F7 DF 7F 3F 59 EE EB EB E3 2E A7 6C D3 8F 3F FE E8 BE 7C 26 60 CF E5 CB 97 FB FB FB E7 27 
C5 B3 E9 AE BB EE A2 5B 99 61 98 FB EE BB CF 93 FD 57 DE 42 2C 16 27 25 25 CD 6F 1A A0 9D 6C 02 
4A 3A 78 8C AF AF 6F 41 41 01 6D D2 16 30 D8 C3 A9 8E 29 B3 D9 4C AF 17 6E EA 78 44 30 0D 9E 10 
18 18 18 13 13 43 96 2F 5C B8 C0 9E A8 C4 C7 D8 D8 D8 BB EF BE 1B 19 19 19 18 18 A8 54 2A CD 66 
B3 1B DE 23 33 3B 3B 7B E4 C8 91 96 96 16 FA 1B 8D 46 F3 E5 97 5F 2E 8E E9 11 1E 20 12 89 B2 B3 
B3 D9 83 3D CE 9D 3B E7 F0 59 62 B1 98 5C 0F FA FB FB C7 C7 C7 79 FE AF E9 E9 69 9A 89 C2 A9 AC 
0E 2B 57 AE A4 23 3D C8 1C 1D 86 D5 6C B6 90 2F 3F DC FA FA FA 1E 7B EC 31 32 5E E2 8B 2F BE E0 
F9 2C 7F 7F FF AC AC 2C F2 FD 5F BE 7C 59 40 6C CA 07 4D 2F ED AC F9 D3 10 C5 62 31 2D 8C 3C 32 
32 72 EE DC 39 A7 0E CF B9 B9 B9 A6 A6 26 92 CF 44 2E 97 2F 9A 4C 02 0B 1C 77 52 BC F9 3A 3B 3B 
3F FE F8 63 FA 50 A7 D3 A9 54 2A 4C 48 9D 8F 36 0D 7C FB ED B7 74 68 22 2D 11 BA C0 3B D9 C2 C3 
C3 4B 4A 4A E8 60 0F 76 32 44 0E B4 A3 78 64 64 E4 E6 CD 9B 3C FF D7 B5 6B D7 68 37 97 9B F2 89 
21 98 06 4F B8 F3 CE 3B 63 63 63 C9 F2 C8 C8 48 73 73 B3 53 83 1D 3B 3A 3A C8 C5 D8 64 32 45 46 
46 BA BC 14 22 C1 2E 57 4B 55 56 56 1A 0C 06 77 FC BB 45 C9 6A B0 87 52 A9 74 98 7C 6D D9 B2 65 
0F 3D F4 10 59 26 D9 1E F8 18 1F 1F 1F 18 18 20 CB 21 21 21 FC 5B A6 D9 CD 39 9D 9D 9D E4 0A FD 
DD 77 DF 91 72 33 0B FC F2 C3 81 3D 98 F8 D2 A5 4B FC 07 6C 04 06 06 92 EF DF 64 32 B9 63 FC 15 
3B BD 74 4A 4A CA EF BF FF CE 3D FE F2 E6 CD 9B 85 85 85 64 7D 9B D3 10 A5 52 29 A9 13 C4 30 4C 
6B 6B AB BD 0A 70 36 0D 0C 0C 7C FD F5 D7 64 F9 C1 07 1F F4 D2 6D ED 75 1C 26 C5 63 BB 7A F5 AA 
4A A5 A2 D9 CA 89 9A 9A 1A B4 6B CC 47 9B 06 F4 7A 3D E9 C6 31 99 4C A4 59 DA 2B 3A D9 D8 83 3D 
68 32 44 EE A7 D0 01 F7 46 A3 91 FF CD FF 95 2B 57 48 C6 5B 86 61 DC 94 10 06 C1 34 78 08 AD 70 
C6 30 4C 7D 7D 3D FF 32 07 BF FD F6 DB E1 C3 87 E9 8B D0 EB A8 6B 59 95 AB 6D 69 69 21 EF F6 D2 
A5 4B 4A A5 92 CF 1D 33 10 31 31 31 34 59 6C 47 47 87 46 A3 E1 BE 71 5A B9 72 25 ED D2 FD FE FB 
EF 79 B6 3F E9 F5 7A DA 2D E8 6C B7 5D 74 74 34 E9 5E D4 E9 74 43 43 43 DE 75 F9 B1 E7 9E 7B EE 
A1 65 50 CE 9E 3D 6B 35 21 89 C3 DF 7F FF 6D AF 42 8A 4B B0 D3 4B C7 C7 C7 3B EC AF F7 F5 F5 4D 
4B 4B 23 CB 36 A7 21 86 87 87 D3 A4 1F 1D 1D 1D C7 8E 1D E3 79 67 3E 3B 3B 5B 57 57 47 BA 20 18 
86 49 4E 4E 46 5D 71 CF 70 98 14 8F 9A 9D 9D AD A9 A9 21 B9 EA 25 12 49 6D 6D 6D 41 41 01 F9 53 
79 79 39 8D 87 80 10 8B C5 32 99 8C DD 34 30 38 38 48 A2 6A AF E8 64 F3 F5 F5 CD C9 C9 A1 81 81 
4A A5 A2 87 A7 3D 0F 3F FC 30 ED C9 BC 78 F1 22 9F FF 32 37 37 47 87 99 AD 5D BB 36 20 20 E0 36 
DE B2 5D 08 A6 C1 43 42 43 43 69 B5 58 A3 D1 B8 67 CF 1E 3E CD 90 93 93 93 E5 E5 E5 A4 0C 21 C3 
30 5B B6 6C E1 9E 09 2E 8C 55 B9 DA D7 5E 7B 2D 2D 2D AD B0 B0 90 1C B4 75 75 75 47 8E 1C 41 A3 
08 4F 56 45 70 D4 6A 75 63 63 23 C7 FA 4B 96 2C 89 8A 8A 22 CB 27 4E 9C 68 6E 6E 76 F8 55 DF B8 
71 A3 AE AE 8E 4C 3E 0B 0E 0E 7E F4 D1 47 9D 7A 87 01 01 01 24 98 26 CD 39 C3 C3 C3 64 FA 8E 57 
5C 7E EC F1 F3 F3 23 B3 91 18 86 D1 E9 74 95 95 95 7C 6E 4B FE F9 E7 9F C6 C6 46 D2 C0 13 1D 1D 
ED B0 D5 50 80 B6 B6 36 72 A4 4B 24 12 99 4C C6 A7 8F 95 9D 70 7A FE 34 44 5F 5F DF 2D 5B B6 D0 
69 88 6F BF FD 76 63 63 A3 C3 7D C6 62 B1 34 36 36 D2 42 7A 72 B9 9C 7E 5D E0 56 16 8B 45 A7 D3 
99 4C A6 E8 E8 E8 C7 1F 7F 9C 7B E5 B3 67 CF 56 54 54 90 E5 9D 3B 77 BE F8 E2 8B 79 79 79 24 D8 
D2 EB F5 FB F7 EF E7 99 F6 E1 7F 87 54 2A 65 37 0D 5C BC 78 D1 BB 3A D9 56 AF 5E 5D 54 54 44 2E 
B5 7A BD FE AD B7 DE E2 6E 08 08 0D 0D A5 BD DC 35 35 35 7C A2 88 5F 7E F9 A5 A9 A9 89 2C 4B A5 
52 7A EA 70 2D 04 D3 E0 21 62 B1 78 DB B6 6D 74 C2 81 4E A7 93 CB E5 A7 4E 9D E2 68 55 1A 1A 1A 
DA B1 63 87 46 A3 21 0F 13 12 12 9E 7F FE 79 77 D4 3C 63 97 AB 7D F9 E5 97 49 E5 B6 F4 F4 F4 ED 
DB B7 93 5F AA 54 2A 32 41 0D F8 58 B1 62 45 71 71 31 1D EC 41 3B D6 6D 62 67 D8 30 99 4C 7B F7 
EE 6D 6A 6A E2 18 16 6F 32 99 DE 79 E7 9D BA BA 3A F2 50 26 93 45 44 44 38 F5 F6 44 22 D1 C6 8D 
1B C9 29 B5 B3 B3 F3 FC F9 F3 E4 8C 6C 55 FE DA EB 24 27 27 D3 EC AD 1A 8D 66 C7 8E 1D DC 09 55 
26 27 27 2B 2A 2A 68 99 CF A4 A4 24 97 77 80 FE F5 D7 5F B4 4D 28 25 25 25 32 32 92 CF B3 D8 09 
A7 6D 4E 43 7C E2 89 27 B2 B2 B2 C8 B2 C9 64 CA CD CD DD BF 7F 3F 47 F7 D1 E4 E4 64 55 55 55 6E 
6E 2E B9 01 93 48 24 0A 85 62 D9 B2 65 CE 7E 1C 10 80 66 70 8F 8A 8A B2 99 5F 9C 1A 1A 1A 2A 2D 
2D B5 2A 95 15 11 11 41 DB 35 8E 1F 3F 5E 5B 5B BB 30 93 41 FD 5B 02 02 02 9E 79 E6 19 86 61 F4 
7A 7D 7B 7B 3B 69 AC 0D 0E 0E F6 A2 74 8D E9 E9 E9 0A 85 82 2C D3 B3 B1 3D 34 87 09 F3 FF 95 A7 
B8 C7 61 1A 0C 86 92 92 12 FA 9A A9 A9 A9 6E BA C7 40 30 0D 9E 13 1E 1E 5E 50 50 40 F3 22 F5 F5 
F5 A5 A5 A5 3D FD F4 D3 9F 7E FA E9 E0 E0 20 CD D4 31 31 31 D1 DD DD 5D 54 54 14 1B 1B DB D0 D0 
40 7E 29 91 48 0A 0A 0A DC 31 DA 89 5D AE 76 C3 86 0D 79 79 79 64 8A 83 BF BF 7F 41 41 01 19 55 
B2 C8 0A 9F 7A 00 BB 32 B0 43 71 71 71 B4 25 DB 68 34 66 64 64 A4 A7 A7 B7 B4 B4 FC F9 E7 9F 34 
AA 9E 98 98 D0 EB F5 D5 D5 D5 09 09 09 4A A5 92 FC 52 22 91 6C DB B6 CD 2A A5 31 1F AB 57 AF 26 
F3 D8 5A 5A 5A CA CB CB 19 86 09 0E 0E 4E 4C 4C F4 EA F2 D4 21 21 21 3B 77 EE A4 C7 57 43 43 43 
54 54 94 42 A1 68 6B 6B BB 7A F5 2A BD 6B 9D 9E 9E 1E 1C 1C AC AE AE 8E 8F 8F DF B7 6F 1F D9 F3 
C3 C2 C2 32 32 32 5C 5E E6 93 9D 5E 9A 4C FB E3 F3 2C F6 DD 0E 63 6B 1A A2 55 EF B0 C9 64 DA B7 
6F 5F 54 54 54 59 59 59 4F 4F 0F 4D 16 74 EB D6 2D FA 49 4B 4A 4A 68 1E 3D 85 42 B1 71 E3 C6 DB 
FF 74 C0 07 CF A4 78 D3 D3 D3 55 55 55 64 C0 95 44 22 79 F5 D5 57 49 02 28 D2 AE 91 99 99 49 56 
FB F0 C3 0F E7 DF 5C FD 2F 13 89 44 89 89 89 E4 60 A9 AC AC 3C 7E FC 38 C3 30 EB D7 AF A7 B9 68 
17 3E 3F 3F BF C2 C2 42 76 52 5A 0E 62 B1 78 EB D6 AD A4 AC 0F C3 30 6D 6D 6D 09 09 09 45 45 45 
DD DD DD F4 C0 37 9B CD D7 AE 5D BB 70 E1 42 51 51 51 42 42 02 9D B3 B1 61 C3 86 D4 D4 54 77 7C 
84 FF 70 2A 41 37 78 91 85 B6 7D 67 66 66 D4 6A B5 B3 69 E4 25 12 89 5A AD 9E 99 99 99 FF 82 A5 
A5 A5 02 76 78 9A 94 7E 62 62 82 A6 06 0B 0E 0E 6E 6F 6F 67 BF B8 D9 6C A6 F5 B7 18 86 51 2A 95 
36 DF C3 BF C8 93 DB 97 E6 BE 60 F8 65 F5 1F 1D 1D A5 03 7B 08 8E 0C 6B BD BD BD 3C 4F A6 6C 1C 
5B 84 EE 18 32 99 6C 6C 6C CC EA AF 66 B3 B9 AA AA 8A FD 52 72 B9 FC FA F5 EB 56 AB 8D 8D 8D C9 
64 32 B2 42 69 69 29 8F 2F C9 C5 9C DD BE 33 33 33 F4 4E E3 F6 BF C9 63 C7 8E 39 DC 70 1C 66 67 
67 69 11 96 E0 E0 E0 1F 7E F8 81 FF 73 C7 C7 C7 B7 6E DD 4A 9F AB D3 E9 E6 AF D3 D5 D5 25 60 06 
C5 F6 ED DB FF F8 E3 8F F9 AF C6 DE BD 05 B0 B9 9B 39 44 9E EB EC B3 16 0E FA A5 71 EC 21 64 2F 
92 48 24 1C 27 0D B3 D9 5C 5F 5F 4F AF 0B 65 65 65 56 7B 63 6F 6F 2F DD D6 E9 E9 E9 A3 A3 A3 2E 
FE 24 EE E1 92 ED EB F0 2C 74 FD FA 75 DA 18 41 54 55 55 99 CD 66 AB D5 B8 4F E0 AE DD FF A7 A6 
A6 72 72 72 C8 9F 72 72 72 A6 A6 A6 B8 3F A3 D5 0E C0 F1 61 ED AD EC 50 58 58 98 56 AB 75 FC 75 
3B 83 BC 32 59 46 CB 34 78 14 29 25 7A F8 F0 61 FE 93 C6 96 2F 5F AE 56 AB 73 73 73 5D 5E 3C C5 
62 B1 34 37 37 D3 70 79 7E B1 43 52 3E 80 94 45 64 18 E6 A3 8F 3E E2 3F 6F 12 82 82 82 76 EF DE 
CD 73 43 AF 59 B3 46 A5 52 F1 8F 8D 24 12 49 59 59 59 61 61 A1 B0 BD 82 DD 9C 43 F0 6F 37 5D C8 
7C 7C 7C 0A 0B 0B CB CA CA F8 5F 69 C8 9D 6A 71 71 B1 CB 8F AF 5F 7F FD B5 BD BD 9D 2C A7 A4 A4 
3C F2 C8 23 FC 9F BB 74 E9 52 DA 86 64 AF 1A 62 7C 7C FC E7 9F 7F EE 54 1B 73 5E 5E DE FB EF BF 
4F D3 9E 80 BB F1 4C 8A 67 30 18 0E 1E 3C C8 51 EC 30 22 22 E2 95 57 5E 21 CB CD CD CD 47 8F 1E 
75 53 F1 4B 6F 74 EF BD F7 26 26 26 D2 87 DE D8 C9 66 35 AE D2 E1 CA 19 19 19 E5 E5 E5 FC CF 72 
52 A9 F4 D0 A1 43 6E 9D 5F 8E 60 1A 3C ED 8E 3B EE 78 E1 85 17 B4 5A 2D 7B C8 87 3D D9 D9 D9 3D 
3D 3D 0A 85 C2 1D 65 08 0D 06 43 45 45 05 3D 83 DB 2C 76 48 06 7B 90 4E 25 A3 D1 F8 DE 7B EF 8D 
8E 8E BA FC 9D 2C 56 09 09 09 BB 76 ED E2 B9 72 7C 7C FC 99 33 67 F6 EC D9 E3 70 AF 88 8B 8B 3B 
79 F2 E4 DE BD 7B 6F A7 1A 16 9D B8 C3 78 E7 E5 C7 1E 3F 3F BF D7 5F 7F 5D AB D5 5A 35 56 D9 24 
97 CB B5 5A 6D 7E 7E BE 3B 8E AF 9E 9E 1E 3A D3 80 A6 23 E4 6F FD FA F5 B4 33 D7 5E 41 99 88 88 
88 93 27 4F 7E F0 C1 07 52 A9 94 FB D5 E2 E2 E2 CE 9C 39 A3 56 AB 17 6C 39 E2 45 89 4F 52 BC C9 
C9 49 95 4A A5 D3 E9 18 FB C5 0E 45 22 D1 B3 CF 3E 9B 9D 9D 4D 1E 56 57 57 D3 14 31 20 12 89 92 
92 92 68 D3 80 77 8D F1 A0 C8 A5 96 67 FF A4 8F 8F 4F 7E 7E BE 56 AB A5 99 7F 38 64 67 67 9F 3E 
7D 3A 35 35 D5 AD 67 78 04 D3 F0 EF 08 0F 0F 57 AB D5 46 A3 B1 B5 B5 35 2F 2F EF A9 A7 9E A2 D7 
5A A9 54 9A 99 99 79 E8 D0 A1 E1 E1 E1 A3 47 8F BA 29 2B E4 8D 1B 37 94 4A 25 19 CC C7 5D AE 76 
ED DA B5 B4 B0 DF A9 53 A7 6A 6B 6B D1 28 C2 93 8F 8F 8F 42 A1 D8 BC 79 33 CF F5 57 AC 58 A1 54 
2A 07 06 06 1A 1A 1A AC F6 8A B0 B0 B0 4D 9B 36 95 96 96 76 77 77 77 75 75 A5 A4 A4 DC 66 BA F1 
A5 4B 97 3E F9 E4 93 64 D9 4B 2F 3F F6 88 44 A2 75 EB D6 9D 38 71 62 78 78 B8 BE BE FE A5 97 5E 
B2 3A BE 9E 7B EE 39 8D 46 33 34 34 D4 D4 D4 B4 6E DD 3A 77 5C 63 26 27 27 BF FA EA 2B B2 BC 66 
CD 1A 5A 69 85 BF 55 AB 56 91 99 55 0C C3 74 75 75 D9 2B 90 E6 EF EF 9F 9F 9F FF F3 CF 3F EB 74 
BA D2 D2 D2 4D 9B 36 D1 CE 90 E5 CB 97 CB 64 32 17 EE 33 E0 2C 9A 14 2F 31 31 D1 66 52 3C 8B C5 
F2 D9 67 9F D5 D4 D4 90 87 BB 76 ED B2 37 73 6E C9 92 25 C5 C5 C5 E4 FE 6A 64 64 E4 C0 81 03 68 
D7 A0 56 AD 5A 45 BF 37 EF ED 64 8B 88 88 A0 99 10 1D 22 67 B9 E6 E6 E6 DE DE DE 83 07 0F 66 66 
66 D2 C2 70 0C C3 C4 C4 C4 78 20 8A F8 AF F7 43 7E 58 90 F6 6B 91 22 97 49 6C DF C5 0A DB 77 71 
C3 F6 5D DC B0 7D 17 37 6C DF C5 8D BD 7D 71 9B 0E 00 00 00 00 20 10 82 69 00 00 00 00 00 81 10 
4C 03 00 00 00 00 08 84 60 1A 00 00 00 00 40 20 04 D3 00 00 00 00 00 02 21 98 06 00 00 00 00 10 
08 C1 34 00 00 00 00 80 40 08 A6 01 00 00 00 00 04 42 30 0D 00 00 00 00 20 10 82 69 00 00 00 00 
00 81 10 4C 03 00 00 00 00 08 84 60 1A 00 00 00 00 40 20 04 D3 00 00 00 00 00 02 21 98 06 00 00 
00 00 10 08 C1 34 00 00 00 00 80 40 08 A6 01 00 00 00 00 04 42 30 0D 00 00 00 00 20 10 82 69 00 
00 00 00 00 81 10 4C 03 00 00 00 00 08 84 60 1A 00 00 00 00 40 20 04 D3 00 00 00 00 00 02 21 98 
06 00 00 00 00 10 08 C1 34 00 00 00 00 80 40 08 A6 01 00 00 00 00 04 42 30 0D 00 00 00 00 20 10 
82 69 00 00 00 00 00 81 10 4C 03 00 00 00 00 08 84 60 1A 00 00 00 00 40 20 04 D3 00 00 00 00 00 
02 21 98 06 00 00 00 00 10 08 C1 34 00 00 00 00 80 40 08 A6 01 00 00 00 00 04 42 30 0D 00 00 00 
00 20 10 82 69 00 00 00 00 00 81 10 4C 03 00 00 00 00 08 84 60 1A 00 00 00 00 40 20 04 D3 00 00 
00 00 00 02 21 98 06 00 00 00 00 10 08 C1 34 00 00 00 00 80 40 08 A6 01 00 00 00 00 04 42 30 0D 
00 00 00 00 20 90 E8 DF 7E 03 00 00 00 00 00 DE C7 62 B1 30 68 99 06 00 00 00 00 10 4C 44 62 6A 
00 00 00 00 00 70 16 5A A6 01 00 00 00 00 04 FA 3F 51 AB 06 E2 F3 63 E9 D4 00 00 00 00 49 45 4E 
44 AE 42 60 82 
EndData
$EndBitmap
Wire Notes Line
	15800 4975 15800 8050
Wire Notes Line
	11250 8050 15800 8050
Wire Notes Line
	1075 4325 5375 4325
Wire Notes Line
	2900 4325 2900 7850
$Comp
L archive:Display_Character_WC1602A DS1
U 1 1 5F0F0527
P 11575 2250
F 0 "DS1" H 11675 3075 50  0000 C CNN
F 1 "LCD2004A" H 11800 3000 50  0000 C CNN
F 2 "Display:LCD2004A_TOP" H 11575 1350 50  0001 C CIN
F 3 "${KIPRJMOD}/documentation/WC1602A-SFYLYHTC06.pdf" H 12275 2250 50  0001 C CNN
F 4 "2034910175" H 11575 2250 50  0001 C CNN "N° Fournisseur"
F 5 "NHD-0420DZ-FL-YBW-33V3-ND" H 11575 2250 50  0001 C CNN "N° Digikey"
	1    11575 2250
	1    0    0    -1  
$EndComp
Wire Wire Line
	11575 1350 11575 1400
$Comp
L archive:Device_C C7
U 1 1 5F1092B0
P 11325 1400
F 0 "C7" V 11525 1350 50  0000 L CNN
F 1 "100[nF]" V 11450 1250 50  0000 L CNN
F 2 "Capacitor_SMD:C_1206_3216Metric_Pad1.42x1.75mm_HandSolder" H 11363 1250 50  0001 C CNN
F 3 "~" H 11325 1400 50  0001 C CNN
F 4 "33059508387" H 11325 1400 50  0001 C CNN "N° Fournisseur"
F 5 "399-C1206C104K5RAC7800CT-ND" H 11325 1400 50  0001 C CNN "N° Digikey"
	1    11325 1400
	0    -1   -1   0   
$EndComp
Wire Wire Line
	11475 1400 11575 1400
Connection ~ 11575 1400
Wire Wire Line
	11575 1400 11575 1450
$Comp
L archive:power_GND #PWR0136
U 1 1 5F11E315
P 11125 1400
F 0 "#PWR0136" H 11125 1150 50  0001 C CNN
F 1 "GND" V 11130 1272 50  0000 R CNN
F 2 "" H 11125 1400 50  0001 C CNN
F 3 "" H 11125 1400 50  0001 C CNN
	1    11125 1400
	0    1    1    0   
$EndComp
Wire Wire Line
	11125 1400 11175 1400
$Comp
L archive:power_GND #PWR0137
U 1 1 5F12A17C
P 11575 3300
F 0 "#PWR0137" H 11575 3050 50  0001 C CNN
F 1 "GND" H 11580 3127 50  0000 C CNN
F 2 "" H 11575 3300 50  0001 C CNN
F 3 "" H 11575 3300 50  0001 C CNN
	1    11575 3300
	1    0    0    -1  
$EndComp
Wire Wire Line
	11575 3300 11575 3050
$Comp
L archive:power_+3V3 #PWR0138
U 1 1 5F13614D
P 11575 1350
F 0 "#PWR0138" H 11575 1200 50  0001 C CNN
F 1 "+3V3" H 11590 1523 50  0000 C CNN
F 2 "" H 11575 1350 50  0001 C CNN
F 3 "" H 11575 1350 50  0001 C CNN
	1    11575 1350
	1    0    0    -1  
$EndComp
$Comp
L archive:power_GND #PWR0139
U 1 1 5F13731D
P 12000 3300
F 0 "#PWR0139" H 12000 3050 50  0001 C CNN
F 1 "GND" H 12005 3127 50  0000 C CNN
F 2 "" H 12000 3300 50  0001 C CNN
F 3 "" H 12000 3300 50  0001 C CNN
	1    12000 3300
	1    0    0    -1  
$EndComp
Wire Wire Line
	11975 2050 12000 2050
$Comp
L archive:power_+3V3 #PWR0140
U 1 1 5F14F45F
P 12000 1900
F 0 "#PWR0140" H 12000 1750 50  0001 C CNN
F 1 "+3V3" H 12015 2073 50  0000 C CNN
F 2 "" H 12000 1900 50  0001 C CNN
F 3 "" H 12000 1900 50  0001 C CNN
	1    12000 1900
	1    0    0    -1  
$EndComp
Wire Wire Line
	12000 1900 12000 1950
Wire Wire Line
	12000 1950 11975 1950
$Comp
L archive:Device_R_POT RV1
U 1 1 5F15BDF1
P 12550 1650
F 0 "RV1" H 12480 1696 50  0000 R CNN
F 1 "10[KΩ]" H 12480 1605 50  0000 R CNN
F 2 "Potentiometer_SMD:Potentiometer_Bourns_3224J_Horizontal" H 12550 1650 50  0001 C CNN
F 3 "~" H 12550 1650 50  0001 C CNN
F 4 "32962861159" H 12550 1650 50  0001 C CNN "N° Fournisseur"
F 5 "987-1008-1-ND" H 12550 1650 50  0001 C CNN "N° Digikey"
	1    12550 1650
	-1   0    0    -1  
$EndComp
Wire Wire Line
	12400 1650 12225 1650
$Comp
L archive:power_+3V3 #PWR0141
U 1 1 5F1688E7
P 12550 1350
F 0 "#PWR0141" H 12550 1200 50  0001 C CNN
F 1 "+3V3" H 12565 1523 50  0000 C CNN
F 2 "" H 12550 1350 50  0001 C CNN
F 3 "" H 12550 1350 50  0001 C CNN
	1    12550 1350
	1    0    0    -1  
$EndComp
Wire Wire Line
	12550 1350 12550 1500
$Comp
L archive:power_GND #PWR0142
U 1 1 5F19569E
P 12550 2550
F 0 "#PWR0142" H 12550 2300 50  0001 C CNN
F 1 "GND" H 12555 2377 50  0000 C CNN
F 2 "" H 12550 2550 50  0001 C CNN
F 3 "" H 12550 2550 50  0001 C CNN
	1    12550 2550
	1    0    0    -1  
$EndComp
Wire Wire Line
	12550 2550 12550 1800
$Comp
L archive:Interface_Expansion_PCF8574A U4
U 1 1 5F1A528C
P 9950 2550
F 0 "U4" H 10025 3225 50  0000 C CNN
F 1 "PCF8574A" H 10175 3150 50  0000 C CNN
F 2 "Package_SO:SOIC-16W_7.5x10.3mm_P1.27mm" H 9950 2550 50  0001 C CNN
F 3 "http://www.nxp.com/documents/data_sheet/PCF8574_PCF8574A.pdf" H 9950 2550 50  0001 C CNN
F 4 "1958961513" H 9950 2550 50  0001 C CNN "N° Fournisseur"
F 5 "568-1074-1-ND" H 9950 2550 50  0001 C CNN "N° Digikey"
	1    9950 2550
	1    0    0    -1  
$EndComp
$Comp
L archive:power_+3V3 #PWR0143
U 1 1 5F1B69D3
P 9950 1750
F 0 "#PWR0143" H 9950 1600 50  0001 C CNN
F 1 "+3V3" H 9965 1923 50  0000 C CNN
F 2 "" H 9950 1750 50  0001 C CNN
F 3 "" H 9950 1750 50  0001 C CNN
	1    9950 1750
	1    0    0    -1  
$EndComp
$Comp
L archive:Device_C C6
U 1 1 5F1B8E3F
P 9700 1800
F 0 "C6" V 9900 1750 50  0000 L CNN
F 1 "100[nF]" V 9825 1650 50  0000 L CNN
F 2 "Capacitor_SMD:C_1206_3216Metric_Pad1.42x1.75mm_HandSolder" H 9738 1650 50  0001 C CNN
F 3 "~" H 9700 1800 50  0001 C CNN
F 4 "33059508387" H 9700 1800 50  0001 C CNN "N° Fournisseur"
F 5 "399-C1206C104K5RAC7800CT-ND" H 9700 1800 50  0001 C CNN "N° Digikey"
	1    9700 1800
	0    -1   -1   0   
$EndComp
Wire Wire Line
	9850 1800 9950 1800
$Comp
L archive:power_GND #PWR0144
U 1 1 5F1B8E46
P 9500 1800
F 0 "#PWR0144" H 9500 1550 50  0001 C CNN
F 1 "GND" V 9505 1672 50  0000 R CNN
F 2 "" H 9500 1800 50  0001 C CNN
F 3 "" H 9500 1800 50  0001 C CNN
	1    9500 1800
	0    1    1    0   
$EndComp
Wire Wire Line
	9500 1800 9550 1800
Wire Wire Line
	9950 1850 9950 1800
Wire Wire Line
	9950 1800 9950 1750
Connection ~ 9950 1800
$Comp
L archive:power_GND #PWR0145
U 1 1 5F1DDEE2
P 9950 3300
F 0 "#PWR0145" H 9950 3050 50  0001 C CNN
F 1 "GND" H 9955 3127 50  0000 C CNN
F 2 "" H 9950 3300 50  0001 C CNN
F 3 "" H 9950 3300 50  0001 C CNN
	1    9950 3300
	1    0    0    -1  
$EndComp
Wire Wire Line
	9950 3300 9950 3250
Wire Wire Line
	10450 2150 10775 2150
Wire Wire Line
	11175 2250 10875 2250
Wire Wire Line
	10450 2350 10975 2350
Wire Wire Line
	11175 2450 11075 2450
Wire Wire Line
	10450 2550 11175 2550
Wire Wire Line
	11175 2650 10450 2650
Wire Wire Line
	10450 2750 11175 2750
Wire Wire Line
	11175 2850 10450 2850
$Comp
L archive:power_GND #PWR0146
U 1 1 5F2514C1
P 9325 2700
F 0 "#PWR0146" H 9325 2450 50  0001 C CNN
F 1 "GND" H 9325 2550 50  0000 C CNN
F 2 "" H 9325 2700 50  0001 C CNN
F 3 "" H 9325 2700 50  0001 C CNN
	1    9325 2700
	1    0    0    -1  
$EndComp
Wire Wire Line
	9450 2650 9325 2650
Wire Wire Line
	9325 2650 9325 2700
Wire Wire Line
	9450 2550 9325 2550
Wire Wire Line
	9325 2550 9325 2650
Connection ~ 9325 2650
Wire Wire Line
	9450 2450 9325 2450
Wire Wire Line
	9325 2450 9325 2550
Connection ~ 9325 2550
NoConn ~ 9450 2950
Text GLabel 9400 2150 0    50   BiDi ~ 0
LCD_SCL
Wire Wire Line
	9400 2150 9450 2150
Text GLabel 4500 6650 2    50   BiDi ~ 0
LCD_RS
Text GLabel 4500 6750 2    50   BiDi ~ 0
LCD_E
Text GLabel 9400 2250 0    50   BiDi ~ 0
LCD_SDA
Wire Wire Line
	9400 2250 9450 2250
Text GLabel 11125 1650 0    50   BiDi ~ 0
LCD_E
Text GLabel 11125 1850 0    50   BiDi ~ 0
LCD_RS
Wire Wire Line
	11125 1850 11175 1850
Wire Wire Line
	11125 1650 11175 1650
$Comp
L archive:power_GND #PWR0147
U 1 1 5F31CC23
P 11150 1750
F 0 "#PWR0147" H 11150 1500 50  0001 C CNN
F 1 "GND" V 11155 1622 50  0000 R CNN
F 2 "" H 11150 1750 50  0001 C CNN
F 3 "" H 11150 1750 50  0001 C CNN
	1    11150 1750
	0    1    1    0   
$EndComp
Wire Wire Line
	11150 1750 11175 1750
Wire Notes Line
	13100 1100 13100 3550
Wire Notes Line
	8950 3550 13100 3550
Wire Notes Line
	8950 1100 13100 1100
Text GLabel 9625 3775 0    50   BiDi ~ 0
LCD_SCL
Text GLabel 9625 3875 0    50   BiDi ~ 0
LCD_SDA
$Comp
L archive:Device_R R3
U 1 1 5F3D2C28
P 9825 3775
F 0 "R3" V 9675 3725 50  0000 L CNN
F 1 "10[KΩ]" V 9725 3650 50  0000 L CNN
F 2 "Resistor_SMD:R_1206_3216Metric_Pad1.42x1.75mm_HandSolder" V 9755 3775 50  0001 C CNN
F 3 "~" H 9825 3775 50  0001 C CNN
F 4 "32859526036" H 9825 3775 50  0001 C CNN "N° Fournisseur"
F 5 "311-10KERCT-ND" H 9825 3775 50  0001 C CNN "N° Digikey"
	1    9825 3775
	0    1    1    0   
$EndComp
$Comp
L archive:Device_R R4
U 1 1 5F3D3ECB
P 9825 3875
F 0 "R4" V 9975 3825 50  0000 L CNN
F 1 "10[KΩ]" V 9900 3750 50  0000 L CNN
F 2 "Resistor_SMD:R_1206_3216Metric_Pad1.42x1.75mm_HandSolder" V 9755 3875 50  0001 C CNN
F 3 "~" H 9825 3875 50  0001 C CNN
F 4 "32859526036" H 9825 3875 50  0001 C CNN "N° Fournisseur"
F 5 "311-10KERCT-ND" H 9825 3875 50  0001 C CNN "N° Digikey"
	1    9825 3875
	0    1    1    0   
$EndComp
$Comp
L archive:power_+3V3 #PWR0148
U 1 1 5F425592
P 10025 3775
F 0 "#PWR0148" H 10025 3625 50  0001 C CNN
F 1 "+3V3" V 10040 3903 50  0000 L CNN
F 2 "" H 10025 3775 50  0001 C CNN
F 3 "" H 10025 3775 50  0001 C CNN
	1    10025 3775
	0    1    1    0   
$EndComp
$Comp
L archive:power_+3V3 #PWR0149
U 1 1 5F4268A2
P 10025 3875
F 0 "#PWR0149" H 10025 3725 50  0001 C CNN
F 1 "+3V3" V 10040 4003 50  0000 L CNN
F 2 "" H 10025 3875 50  0001 C CNN
F 3 "" H 10025 3875 50  0001 C CNN
	1    10025 3875
	0    1    1    0   
$EndComp
Wire Wire Line
	10025 3875 9975 3875
Wire Wire Line
	9975 3775 10025 3775
Wire Wire Line
	9675 3775 9625 3775
Wire Wire Line
	9625 3875 9675 3875
Text Notes 8975 1275 0    50   ~ 0
IO Extender\nD0-D7\n
Text Notes 10700 1275 0    50   ~ 0
Écrant LCD\n20x4\n
Wire Notes Line
	8950 4100 10675 4100
Wire Notes Line
	10675 1100 10675 4100
Wire Notes Line
	8950 1100 8950 4100
Text Notes 8975 3650 0    50   ~ 0
Pull-Up I2C\n
Text Notes 8925 1075 0    100  ~ 0
Écran LCD
$Comp
L archive:Switch_SW_SPDT SW38
U 1 1 5F5E8F83
P 3775 2025
F 0 "SW38" H 3775 2310 50  0000 C CNN
F 1 "SK-12F14" H 3775 2219 50  0000 C CNN
F 2 "Button_Switch_THT:SW_CuK_OS102011MA1QN1_SPDT_Angled" H 3775 2025 50  0001 C CNN
F 3 "~" H 3775 2025 50  0001 C CNN
F 4 "32827322833" H 3775 2025 50  0001 C CNN "N° Fournisseur"
F 5 "Distrelek 135-11-185" H 3775 2025 50  0001 C CNN "N° Digikey"
	1    3775 2025
	-1   0    0    -1  
$EndComp
Wire Wire Line
	3575 1925 3100 1925
Wire Wire Line
	3100 1925 3000 2025
Wire Wire Line
	3000 2025 2150 2025
$Comp
L archive:power_GND #PWR0150
U 1 1 5F64B2B1
P 3500 2425
F 0 "#PWR0150" H 3500 2175 50  0001 C CNN
F 1 "GND" H 3505 2252 50  0000 C CNN
F 2 "" H 3500 2425 50  0001 C CNN
F 3 "" H 3500 2425 50  0001 C CNN
	1    3500 2425
	1    0    0    -1  
$EndComp
Wire Wire Line
	3500 2125 3575 2125
$Comp
L archive:Device_C C8
U 1 1 5F65DCF0
P 3000 2225
F 0 "C8" H 3000 2125 50  0000 L CNN
F 1 "100[nF]" H 3000 2300 50  0000 L CNN
F 2 "Capacitor_SMD:C_1206_3216Metric_Pad1.42x1.75mm_HandSolder" H 3038 2075 50  0001 C CNN
F 3 "~" H 3000 2225 50  0001 C CNN
F 4 "33059508387" H 3000 2225 50  0001 C CNN "N° Fournisseur"
F 5 "399-C1206C104K5RAC7800CT-ND" H 3000 2225 50  0001 C CNN "N° Digikey"
	1    3000 2225
	1    0    0    -1  
$EndComp
Wire Wire Line
	3000 2075 3000 2025
Connection ~ 3000 2025
$Comp
L archive:power_GND #PWR0151
U 1 1 5F67F9B4
P 3000 2425
F 0 "#PWR0151" H 3000 2175 50  0001 C CNN
F 1 "GND" H 3005 2252 50  0000 C CNN
F 2 "" H 3000 2425 50  0001 C CNN
F 3 "" H 3000 2425 50  0001 C CNN
	1    3000 2425
	1    0    0    -1  
$EndComp
Wire Wire Line
	3000 2425 3000 2375
Text Notes 5750 4975 0    100  ~ 0
Protections\n
Wire Notes Line
	8450 4975 8450 7650
$Comp
L archive:Device_C C9
U 1 1 5EDB00DD
P 6400 5350
F 0 "C9" V 6350 5425 50  0000 L CNN
F 1 "100[nF]" V 6350 5000 50  0000 L CNN
F 2 "Capacitor_SMD:C_1206_3216Metric_Pad1.42x1.75mm_HandSolder" H 6438 5200 50  0001 C CNN
F 3 "~" H 6400 5350 50  0001 C CNN
F 4 "33059508387" H 6400 5350 50  0001 C CNN "N° Fournisseur"
F 5 "399-C1206C104K5RAC7800CT-ND" H 6400 5350 50  0001 C CNN "N° Digikey"
	1    6400 5350
	0    -1   -1   0   
$EndComp
Text GLabel 6125 5275 0    50   Input ~ 0
ROW1
Text GLabel 6125 5625 0    50   Input ~ 0
ROW2
Text GLabel 6125 6000 0    50   Input ~ 0
ROW3
Text GLabel 6125 6400 0    50   Input ~ 0
ROW4
$Comp
L archive:Device_R R17
U 1 1 5EE02E99
P 6400 5200
F 0 "R17" V 6350 5325 50  0000 L CNN
F 1 "10[KΩ]" V 6350 4825 50  0000 L CNN
F 2 "Resistor_SMD:R_1206_3216Metric_Pad1.42x1.75mm_HandSolder" V 6330 5200 50  0001 C CNN
F 3 "~" H 6400 5200 50  0001 C CNN
F 4 "32859526036" H 6400 5200 50  0001 C CNN "N° Fournisseur"
F 5 "311-10KERCT-ND" H 6400 5200 50  0001 C CNN "N° Digikey"
	1    6400 5200
	0    -1   1    0   
$EndComp
$Comp
L archive:power_GND #PWR0152
U 1 1 5EE2918C
P 6775 5275
F 0 "#PWR0152" H 6775 5025 50  0001 C CNN
F 1 "GND" H 6780 5102 50  0000 C CNN
F 2 "" H 6775 5275 50  0001 C CNN
F 3 "" H 6775 5275 50  0001 C CNN
	1    6775 5275
	0    -1   -1   0   
$EndComp
Wire Notes Line
	5775 4975 15800 4975
Text Notes 5775 5050 0    50   ~ 0
Anti-Rebond\n
$Comp
L archive:Device_C C10
U 1 1 5F575C43
P 3575 4600
F 0 "C10" V 3775 4550 50  0000 L CNN
F 1 "100[nF]" V 3700 4450 50  0000 L CNN
F 2 "Capacitor_SMD:C_1206_3216Metric_Pad1.42x1.75mm_HandSolder" H 3613 4450 50  0001 C CNN
F 3 "~" H 3575 4600 50  0001 C CNN
F 4 "33059508387" H 3575 4600 50  0001 C CNN "N° Fournisseur"
F 5 "399-C1206C104K5RAC7800CT-ND" H 3575 4600 50  0001 C CNN "N° Digikey"
	1    3575 4600
	0    -1   -1   0   
$EndComp
$Comp
L archive:power_GND #PWR0112
U 1 1 5F575C4A
P 3375 4600
F 0 "#PWR0112" H 3375 4350 50  0001 C CNN
F 1 "GND" V 3380 4472 50  0000 R CNN
F 2 "" H 3375 4600 50  0001 C CNN
F 3 "" H 3375 4600 50  0001 C CNN
	1    3375 4600
	0    1    1    0   
$EndComp
Wire Wire Line
	3375 4600 3425 4600
$Comp
L archive:power_+3V3 #PWR0153
U 1 1 5F5BEDD3
P 3800 4550
F 0 "#PWR0153" H 3800 4400 50  0001 C CNN
F 1 "+3V3" H 3815 4723 50  0000 C CNN
F 2 "" H 3800 4550 50  0001 C CNN
F 3 "" H 3800 4550 50  0001 C CNN
	1    3800 4550
	1    0    0    -1  
$EndComp
Wire Wire Line
	3800 4550 3800 4600
Wire Wire Line
	3725 4600 3800 4600
Connection ~ 3800 4600
Wire Wire Line
	3800 4600 3800 4650
$Comp
L archive:Device_R_Small R18
U 1 1 5F667DAF
P 3500 2275
F 0 "R18" H 3550 2300 50  0000 L CNN
F 1 "10[KΩ]" H 3550 2225 50  0000 L CNN
F 2 "Resistor_SMD:R_1206_3216Metric_Pad1.42x1.75mm_HandSolder" H 3500 2275 50  0001 C CNN
F 3 "~" H 3500 2275 50  0001 C CNN
F 4 "32859526036" H 3500 2275 50  0001 C CNN "N° Fournisseur"
F 5 "311-10KERCT-ND" H 3500 2275 50  0001 C CNN "N° Digikey"
	1    3500 2275
	1    0    0    -1  
$EndComp
Wire Wire Line
	3500 2125 3500 2175
Wire Wire Line
	3500 2375 3500 2425
Wire Wire Line
	6550 5200 6600 5200
Wire Wire Line
	6600 5200 6600 5275
Wire Wire Line
	6600 5350 6550 5350
Wire Wire Line
	6775 5275 6600 5275
Connection ~ 6600 5275
Wire Wire Line
	6600 5275 6600 5350
Wire Wire Line
	6250 5200 6200 5200
Wire Wire Line
	6200 5200 6200 5275
Wire Wire Line
	6200 5350 6250 5350
Wire Wire Line
	6125 5275 6200 5275
Connection ~ 6200 5275
Wire Wire Line
	6200 5275 6200 5350
$Comp
L archive:Device_C C11
U 1 1 5F7C681C
P 6400 5700
F 0 "C11" V 6350 5775 50  0000 L CNN
F 1 "100[nF]" V 6350 5350 50  0000 L CNN
F 2 "Capacitor_SMD:C_1206_3216Metric_Pad1.42x1.75mm_HandSolder" H 6438 5550 50  0001 C CNN
F 3 "~" H 6400 5700 50  0001 C CNN
F 4 "33059508387" H 6400 5700 50  0001 C CNN "N° Fournisseur"
F 5 "399-C1206C104K5RAC7800CT-ND" H 6400 5700 50  0001 C CNN "N° Digikey"
	1    6400 5700
	0    -1   -1   0   
$EndComp
$Comp
L archive:Device_R R19
U 1 1 5F7C6823
P 6400 5550
F 0 "R19" V 6350 5675 50  0000 L CNN
F 1 "10[KΩ]" V 6350 5175 50  0000 L CNN
F 2 "Resistor_SMD:R_1206_3216Metric_Pad1.42x1.75mm_HandSolder" V 6330 5550 50  0001 C CNN
F 3 "~" H 6400 5550 50  0001 C CNN
F 4 "32859526036" H 6400 5550 50  0001 C CNN "N° Fournisseur"
F 5 "311-10KERCT-ND" H 6400 5550 50  0001 C CNN "N° Digikey"
	1    6400 5550
	0    -1   1    0   
$EndComp
Wire Wire Line
	6550 5550 6600 5550
Wire Wire Line
	6600 5550 6600 5625
Wire Wire Line
	6600 5700 6550 5700
Wire Wire Line
	6775 5625 6600 5625
Connection ~ 6600 5625
Wire Wire Line
	6600 5625 6600 5700
Wire Wire Line
	6250 5550 6200 5550
Wire Wire Line
	6200 5550 6200 5625
Wire Wire Line
	6200 5700 6250 5700
Wire Wire Line
	6125 5625 6200 5625
Connection ~ 6200 5625
Wire Wire Line
	6200 5625 6200 5700
$Comp
L archive:Device_C C12
U 1 1 5F7DF6C9
P 6400 6075
F 0 "C12" V 6350 6150 50  0000 L CNN
F 1 "100[nF]" V 6350 5725 50  0000 L CNN
F 2 "Capacitor_SMD:C_1206_3216Metric_Pad1.42x1.75mm_HandSolder" H 6438 5925 50  0001 C CNN
F 3 "~" H 6400 6075 50  0001 C CNN
F 4 "33059508387" H 6400 6075 50  0001 C CNN "N° Fournisseur"
F 5 "399-C1206C104K5RAC7800CT-ND" H 6400 6075 50  0001 C CNN "N° Digikey"
	1    6400 6075
	0    -1   -1   0   
$EndComp
$Comp
L archive:Device_R R20
U 1 1 5F7DF6D0
P 6400 5925
F 0 "R20" V 6350 6050 50  0000 L CNN
F 1 "10[KΩ]" V 6350 5550 50  0000 L CNN
F 2 "Resistor_SMD:R_1206_3216Metric_Pad1.42x1.75mm_HandSolder" V 6330 5925 50  0001 C CNN
F 3 "~" H 6400 5925 50  0001 C CNN
F 4 "32859526036" H 6400 5925 50  0001 C CNN "N° Fournisseur"
F 5 "311-10KERCT-ND" H 6400 5925 50  0001 C CNN "N° Digikey"
	1    6400 5925
	0    -1   1    0   
$EndComp
Wire Wire Line
	6550 5925 6600 5925
Wire Wire Line
	6600 5925 6600 6000
Wire Wire Line
	6600 6075 6550 6075
Wire Wire Line
	6775 6000 6600 6000
Connection ~ 6600 6000
Wire Wire Line
	6600 6000 6600 6075
Wire Wire Line
	6250 5925 6200 5925
Wire Wire Line
	6200 5925 6200 6000
Wire Wire Line
	6200 6075 6250 6075
Wire Wire Line
	6125 6000 6200 6000
Connection ~ 6200 6000
Wire Wire Line
	6200 6000 6200 6075
$Comp
L archive:Device_C C13
U 1 1 5F7FA1F9
P 6400 6475
F 0 "C13" V 6350 6550 50  0000 L CNN
F 1 "100[nF]" V 6350 6125 50  0000 L CNN
F 2 "Capacitor_SMD:C_1206_3216Metric_Pad1.42x1.75mm_HandSolder" H 6438 6325 50  0001 C CNN
F 3 "~" H 6400 6475 50  0001 C CNN
F 4 "33059508387" H 6400 6475 50  0001 C CNN "N° Fournisseur"
F 5 "399-C1206C104K5RAC7800CT-ND" H 6400 6475 50  0001 C CNN "N° Digikey"
	1    6400 6475
	0    -1   -1   0   
$EndComp
$Comp
L archive:Device_R R21
U 1 1 5F7FA200
P 6400 6325
F 0 "R21" V 6350 6450 50  0000 L CNN
F 1 "10[KΩ]" V 6350 5950 50  0000 L CNN
F 2 "Resistor_SMD:R_1206_3216Metric_Pad1.42x1.75mm_HandSolder" V 6330 6325 50  0001 C CNN
F 3 "~" H 6400 6325 50  0001 C CNN
F 4 "32859526036" H 6400 6325 50  0001 C CNN "N° Fournisseur"
F 5 "311-10KERCT-ND" H 6400 6325 50  0001 C CNN "N° Digikey"
	1    6400 6325
	0    -1   1    0   
$EndComp
Wire Wire Line
	6550 6325 6600 6325
Wire Wire Line
	6600 6325 6600 6400
Wire Wire Line
	6600 6475 6550 6475
Wire Wire Line
	6775 6400 6600 6400
Connection ~ 6600 6400
Wire Wire Line
	6600 6400 6600 6475
Wire Wire Line
	6250 6325 6200 6325
Wire Wire Line
	6200 6325 6200 6400
Wire Wire Line
	6200 6475 6250 6475
Wire Wire Line
	6125 6400 6200 6400
Connection ~ 6200 6400
Wire Wire Line
	6200 6400 6200 6475
$Comp
L archive:power_GND #PWR0158
U 1 1 5F066557
P 8125 6025
F 0 "#PWR0158" H 8125 5775 50  0001 C CNN
F 1 "GND" H 8130 5852 50  0000 C CNN
F 2 "" H 8125 6025 50  0001 C CNN
F 3 "" H 8125 6025 50  0001 C CNN
	1    8125 6025
	0    -1   -1   0   
$EndComp
$Comp
L archive:power_GND #PWR0157
U 1 1 5F04F902
P 8125 5650
F 0 "#PWR0157" H 8125 5400 50  0001 C CNN
F 1 "GND" H 8130 5477 50  0000 C CNN
F 2 "" H 8125 5650 50  0001 C CNN
F 3 "" H 8125 5650 50  0001 C CNN
	1    8125 5650
	0    -1   -1   0   
$EndComp
$Comp
L archive:power_GND #PWR0156
U 1 1 5F024AD8
P 8125 5275
F 0 "#PWR0156" H 8125 5025 50  0001 C CNN
F 1 "GND" H 8130 5102 50  0000 C CNN
F 2 "" H 8125 5275 50  0001 C CNN
F 3 "" H 8125 5275 50  0001 C CNN
	1    8125 5275
	0    -1   -1   0   
$EndComp
Text GLabel 7475 6025 0    50   Input ~ 0
ROW7
Text GLabel 7475 5650 0    50   Input ~ 0
ROW6
Text GLabel 7475 5275 0    50   Input ~ 0
ROW5
$Comp
L archive:Device_C C14
U 1 1 5F8AD55A
P 7750 5350
F 0 "C14" V 7700 5425 50  0000 L CNN
F 1 "100[nF]" V 7700 5000 50  0000 L CNN
F 2 "Capacitor_SMD:C_1206_3216Metric_Pad1.42x1.75mm_HandSolder" H 7788 5200 50  0001 C CNN
F 3 "~" H 7750 5350 50  0001 C CNN
F 4 "33059508387" H 7750 5350 50  0001 C CNN "N° Fournisseur"
F 5 "399-C1206C104K5RAC7800CT-ND" H 7750 5350 50  0001 C CNN "N° Digikey"
	1    7750 5350
	0    -1   -1   0   
$EndComp
$Comp
L archive:Device_R R22
U 1 1 5F8AD561
P 7750 5200
F 0 "R22" V 7700 5325 50  0000 L CNN
F 1 "10[KΩ]" V 7700 4825 50  0000 L CNN
F 2 "Resistor_SMD:R_1206_3216Metric_Pad1.42x1.75mm_HandSolder" V 7680 5200 50  0001 C CNN
F 3 "~" H 7750 5200 50  0001 C CNN
F 4 "32859526036" H 7750 5200 50  0001 C CNN "N° Fournisseur"
F 5 "311-10KERCT-ND" H 7750 5200 50  0001 C CNN "N° Digikey"
	1    7750 5200
	0    -1   1    0   
$EndComp
Wire Wire Line
	7900 5200 7950 5200
Wire Wire Line
	7950 5200 7950 5275
Wire Wire Line
	7950 5350 7900 5350
Wire Wire Line
	8125 5275 7950 5275
Connection ~ 7950 5275
Wire Wire Line
	7950 5275 7950 5350
Wire Wire Line
	7600 5200 7550 5200
Wire Wire Line
	7550 5200 7550 5275
Wire Wire Line
	7550 5350 7600 5350
Wire Wire Line
	7475 5275 7550 5275
Connection ~ 7550 5275
Wire Wire Line
	7550 5275 7550 5350
$Comp
L archive:Device_C C15
U 1 1 5F8C96FF
P 7750 5725
F 0 "C15" V 7700 5800 50  0000 L CNN
F 1 "100[nF]" V 7700 5375 50  0000 L CNN
F 2 "Capacitor_SMD:C_1206_3216Metric_Pad1.42x1.75mm_HandSolder" H 7788 5575 50  0001 C CNN
F 3 "~" H 7750 5725 50  0001 C CNN
F 4 "33059508387" H 7750 5725 50  0001 C CNN "N° Fournisseur"
F 5 "399-C1206C104K5RAC7800CT-ND" H 7750 5725 50  0001 C CNN "N° Digikey"
	1    7750 5725
	0    -1   -1   0   
$EndComp
$Comp
L archive:Device_R R23
U 1 1 5F8C9706
P 7750 5575
F 0 "R23" V 7700 5700 50  0000 L CNN
F 1 "10[KΩ]" V 7700 5200 50  0000 L CNN
F 2 "Resistor_SMD:R_1206_3216Metric_Pad1.42x1.75mm_HandSolder" V 7680 5575 50  0001 C CNN
F 3 "~" H 7750 5575 50  0001 C CNN
F 4 "32859526036" H 7750 5575 50  0001 C CNN "N° Fournisseur"
F 5 "311-10KERCT-ND" H 7750 5575 50  0001 C CNN "N° Digikey"
	1    7750 5575
	0    -1   1    0   
$EndComp
Wire Wire Line
	7900 5575 7950 5575
Wire Wire Line
	7950 5575 7950 5650
Wire Wire Line
	7950 5725 7900 5725
Wire Wire Line
	8125 5650 7950 5650
Connection ~ 7950 5650
Wire Wire Line
	7950 5650 7950 5725
Wire Wire Line
	7600 5575 7550 5575
Wire Wire Line
	7550 5575 7550 5650
Wire Wire Line
	7550 5725 7600 5725
Wire Wire Line
	7475 5650 7550 5650
Connection ~ 7550 5650
Wire Wire Line
	7550 5650 7550 5725
$Comp
L archive:Device_C C16
U 1 1 5F8E747C
P 7750 6100
F 0 "C16" V 7700 6175 50  0000 L CNN
F 1 "100[nF]" V 7700 5750 50  0000 L CNN
F 2 "Capacitor_SMD:C_1206_3216Metric_Pad1.42x1.75mm_HandSolder" H 7788 5950 50  0001 C CNN
F 3 "~" H 7750 6100 50  0001 C CNN
F 4 "33059508387" H 7750 6100 50  0001 C CNN "N° Fournisseur"
F 5 "399-C1206C104K5RAC7800CT-ND" H 7750 6100 50  0001 C CNN "N° Digikey"
	1    7750 6100
	0    -1   -1   0   
$EndComp
$Comp
L archive:Device_R R24
U 1 1 5F8E7483
P 7750 5950
F 0 "R24" V 7700 6075 50  0000 L CNN
F 1 "10[KΩ]" V 7700 5575 50  0000 L CNN
F 2 "Resistor_SMD:R_1206_3216Metric_Pad1.42x1.75mm_HandSolder" V 7680 5950 50  0001 C CNN
F 3 "~" H 7750 5950 50  0001 C CNN
F 4 "32859526036" H 7750 5950 50  0001 C CNN "N° Fournisseur"
F 5 "311-10KERCT-ND" H 7750 5950 50  0001 C CNN "N° Digikey"
	1    7750 5950
	0    -1   1    0   
$EndComp
Wire Wire Line
	7900 5950 7950 5950
Wire Wire Line
	7950 5950 7950 6025
Wire Wire Line
	7950 6100 7900 6100
Wire Wire Line
	8125 6025 7950 6025
Connection ~ 7950 6025
Wire Wire Line
	7950 6025 7950 6100
Wire Wire Line
	7600 5950 7550 5950
Wire Wire Line
	7550 5950 7550 6025
Wire Wire Line
	7550 6100 7600 6100
Wire Wire Line
	7475 6025 7550 6025
Connection ~ 7550 6025
Wire Wire Line
	7550 6025 7550 6100
$Comp
L archive:power_GND #PWR0154
U 1 1 5F94D3E8
P 6775 5625
F 0 "#PWR0154" H 6775 5375 50  0001 C CNN
F 1 "GND" H 6780 5452 50  0000 C CNN
F 2 "" H 6775 5625 50  0001 C CNN
F 3 "" H 6775 5625 50  0001 C CNN
	1    6775 5625
	0    -1   -1   0   
$EndComp
$Comp
L archive:power_GND #PWR0155
U 1 1 5F96CE99
P 6775 6000
F 0 "#PWR0155" H 6775 5750 50  0001 C CNN
F 1 "GND" H 6780 5827 50  0000 C CNN
F 2 "" H 6775 6000 50  0001 C CNN
F 3 "" H 6775 6000 50  0001 C CNN
	1    6775 6000
	0    -1   -1   0   
$EndComp
$Comp
L archive:power_GND #PWR0159
U 1 1 5F98C694
P 6775 6400
F 0 "#PWR0159" H 6775 6150 50  0001 C CNN
F 1 "GND" H 6780 6227 50  0000 C CNN
F 2 "" H 6775 6400 50  0001 C CNN
F 3 "" H 6775 6400 50  0001 C CNN
	1    6775 6400
	0    -1   -1   0   
$EndComp
$Comp
L archive:Device_C C17
U 1 1 5FAAAA6D
P 12225 1900
F 0 "C17" H 12075 1825 50  0000 L CNN
F 1 "100[nF]" H 11925 2000 50  0000 L CNN
F 2 "Capacitor_SMD:C_1206_3216Metric_Pad1.42x1.75mm_HandSolder" H 12263 1750 50  0001 C CNN
F 3 "~" H 12225 1900 50  0001 C CNN
F 4 "33059508387" H 12225 1900 50  0001 C CNN "N° Fournisseur"
F 5 "399-C1206C104K5RAC7800CT-ND" H 12225 1900 50  0001 C CNN "N° Digikey"
	1    12225 1900
	-1   0    0    1   
$EndComp
$Comp
L archive:power_GND #PWR0160
U 1 1 5FBA6F51
P 12225 2550
F 0 "#PWR0160" H 12225 2300 50  0001 C CNN
F 1 "GND" H 12230 2377 50  0000 C CNN
F 2 "" H 12225 2550 50  0001 C CNN
F 3 "" H 12225 2550 50  0001 C CNN
	1    12225 2550
	1    0    0    -1  
$EndComp
Wire Wire Line
	12225 2550 12225 2050
Wire Wire Line
	12225 1750 12225 1650
Connection ~ 12225 1650
Wire Wire Line
	12225 1650 11975 1650
Wire Notes Line
	8450 7650 11250 7650
Wire Notes Line
	5775 5000 5775 6625
$Comp
L archive:Device_Q_PNP_BEC Q1
U 1 1 60218976
P 6450 7125
F 0 "Q1" H 6641 7079 50  0000 L CNN
F 1 "BC856B" H 6641 7170 50  0000 L CNN
F 2 "Package_TO_SOT_SMD:SOT-23_Handsoldering" H 6650 7225 50  0001 C CNN
F 3 "~" H 6450 7125 50  0001 C CNN
F 4 "32959120963" H 6450 7125 50  0001 C CNN "N° Fournisseur"
F 5 "BC856BLT3GOSCT-ND" H 6450 7125 50  0001 C CNN "N° Digikey"
	1    6450 7125
	1    0    0    1   
$EndComp
$Comp
L archive:Device_R R25
U 1 1 6021D69A
P 6050 7125
F 0 "R25" V 6225 7075 50  0000 L CNN
F 1 "1[KΩ]" V 6150 6975 50  0000 L CNN
F 2 "Resistor_SMD:R_1206_3216Metric_Pad1.42x1.75mm_HandSolder" V 5980 7125 50  0001 C CNN
F 3 "~" H 6050 7125 50  0001 C CNN
F 4 "32859526036" H 6050 7125 50  0001 C CNN "N° Fournisseur"
F 5 "311-1.0KERCT-ND" H 6050 7125 50  0001 C CNN "N° Digikey"
	1    6050 7125
	0    -1   1    0   
$EndComp
Wire Wire Line
	6250 7125 6200 7125
$Comp
L archive:Device_R R26
U 1 1 6027876A
P 6550 7525
F 0 "R26" H 6625 7575 50  0000 L CNN
F 1 "10[KΩ]" H 6600 7500 50  0000 L CNN
F 2 "Resistor_SMD:R_1206_3216Metric_Pad1.42x1.75mm_HandSolder" V 6480 7525 50  0001 C CNN
F 3 "~" H 6550 7525 50  0001 C CNN
F 4 "32859526036" H 6550 7525 50  0001 C CNN "N° Fournisseur"
F 5 "311-10KERCT-ND" H 6550 7525 50  0001 C CNN "N° Digikey"
	1    6550 7525
	-1   0    0    -1  
$EndComp
$Comp
L archive:power_+3V3 #PWR0161
U 1 1 602960BC
P 6550 6875
F 0 "#PWR0161" H 6550 6725 50  0001 C CNN
F 1 "+3V3" H 6565 7048 50  0000 C CNN
F 2 "" H 6550 6875 50  0001 C CNN
F 3 "" H 6550 6875 50  0001 C CNN
	1    6550 6875
	1    0    0    -1  
$EndComp
Wire Wire Line
	6550 6875 6550 6925
$Comp
L archive:power_GND #PWR0162
U 1 1 602B7241
P 6550 7725
F 0 "#PWR0162" H 6550 7475 50  0001 C CNN
F 1 "GND" H 6550 7575 50  0000 C CNN
F 2 "" H 6550 7725 50  0001 C CNN
F 3 "" H 6550 7725 50  0001 C CNN
	1    6550 7725
	1    0    0    -1  
$EndComp
Wire Wire Line
	6550 7725 6550 7675
Wire Wire Line
	6550 7325 6550 7350
Text GLabel 5850 7125 0    50   Output ~ 0
P_COL1
Wire Wire Line
	5850 7125 5900 7125
Text GLabel 6650 7350 2    50   Output ~ 0
COL1
Wire Wire Line
	6650 7350 6550 7350
Connection ~ 6550 7350
Wire Wire Line
	6550 7350 6550 7375
$Comp
L archive:Device_Q_PNP_BEC Q2
U 1 1 603B3060
P 7925 7125
F 0 "Q2" H 8116 7079 50  0000 L CNN
F 1 "BC856B" H 8116 7170 50  0000 L CNN
F 2 "Package_TO_SOT_SMD:SOT-23_Handsoldering" H 8125 7225 50  0001 C CNN
F 3 "~" H 7925 7125 50  0001 C CNN
F 4 "32959120963" H 7925 7125 50  0001 C CNN "N° Fournisseur"
F 5 "BC856BLT3GOSCT-ND" H 7925 7125 50  0001 C CNN "N° Digikey"
	1    7925 7125
	1    0    0    1   
$EndComp
$Comp
L archive:Device_R R29
U 1 1 603B3067
P 7525 7125
F 0 "R29" V 7700 7075 50  0000 L CNN
F 1 "1[KΩ]" V 7625 6975 50  0000 L CNN
F 2 "Resistor_SMD:R_1206_3216Metric_Pad1.42x1.75mm_HandSolder" V 7455 7125 50  0001 C CNN
F 3 "~" H 7525 7125 50  0001 C CNN
F 4 "32859526036" H 7525 7125 50  0001 C CNN "N° Fournisseur"
F 5 "311-1.0KERCT-ND" H 7525 7125 50  0001 C CNN "N° Digikey"
	1    7525 7125
	0    -1   1    0   
$EndComp
Wire Wire Line
	7725 7125 7675 7125
$Comp
L archive:Device_R R30
U 1 1 603B306F
P 8025 7525
F 0 "R30" H 8100 7575 50  0000 L CNN
F 1 "10[KΩ]" H 8075 7500 50  0000 L CNN
F 2 "Resistor_SMD:R_1206_3216Metric_Pad1.42x1.75mm_HandSolder" V 7955 7525 50  0001 C CNN
F 3 "~" H 8025 7525 50  0001 C CNN
F 4 "32859526036" H 8025 7525 50  0001 C CNN "N° Fournisseur"
F 5 "311-10KERCT-ND" H 8025 7525 50  0001 C CNN "N° Digikey"
	1    8025 7525
	-1   0    0    -1  
$EndComp
$Comp
L archive:power_+3V3 #PWR0163
U 1 1 603B3075
P 8025 6875
F 0 "#PWR0163" H 8025 6725 50  0001 C CNN
F 1 "+3V3" H 8040 7048 50  0000 C CNN
F 2 "" H 8025 6875 50  0001 C CNN
F 3 "" H 8025 6875 50  0001 C CNN
	1    8025 6875
	1    0    0    -1  
$EndComp
Wire Wire Line
	8025 6875 8025 6925
$Comp
L archive:power_GND #PWR0164
U 1 1 603B307C
P 8025 7725
F 0 "#PWR0164" H 8025 7475 50  0001 C CNN
F 1 "GND" H 8025 7575 50  0000 C CNN
F 2 "" H 8025 7725 50  0001 C CNN
F 3 "" H 8025 7725 50  0001 C CNN
	1    8025 7725
	1    0    0    -1  
$EndComp
Wire Wire Line
	8025 7725 8025 7675
Wire Wire Line
	8025 7325 8025 7350
Text GLabel 7325 7125 0    50   Output ~ 0
P_COL2
Wire Wire Line
	7325 7125 7375 7125
Text GLabel 8125 7350 2    50   Output ~ 0
COL2
Wire Wire Line
	8125 7350 8025 7350
Connection ~ 8025 7350
Wire Wire Line
	8025 7350 8025 7375
$Comp
L archive:Device_Q_PNP_BEC Q3
U 1 1 603D3FA2
P 6625 8150
F 0 "Q3" H 6816 8104 50  0000 L CNN
F 1 "BC856B" H 6816 8195 50  0000 L CNN
F 2 "Package_TO_SOT_SMD:SOT-23_Handsoldering" H 6825 8250 50  0001 C CNN
F 3 "~" H 6625 8150 50  0001 C CNN
F 4 "32959120963" H 6625 8150 50  0001 C CNN "N° Fournisseur"
F 5 "BC856BLT3GOSCT-ND" H 6625 8150 50  0001 C CNN "N° Digikey"
	1    6625 8150
	1    0    0    1   
$EndComp
$Comp
L archive:Device_R R33
U 1 1 603D3FA9
P 6225 8150
F 0 "R33" V 6400 8100 50  0000 L CNN
F 1 "1[KΩ]" V 6325 8000 50  0000 L CNN
F 2 "Resistor_SMD:R_1206_3216Metric_Pad1.42x1.75mm_HandSolder" V 6155 8150 50  0001 C CNN
F 3 "~" H 6225 8150 50  0001 C CNN
F 4 "32859526036" H 6225 8150 50  0001 C CNN "N° Fournisseur"
F 5 "311-1.0KERCT-ND" H 6225 8150 50  0001 C CNN "N° Digikey"
	1    6225 8150
	0    -1   1    0   
$EndComp
Wire Wire Line
	6425 8150 6375 8150
$Comp
L archive:Device_R R34
U 1 1 603D3FB1
P 6725 8550
F 0 "R34" H 6800 8600 50  0000 L CNN
F 1 "10[KΩ]" H 6775 8525 50  0000 L CNN
F 2 "Resistor_SMD:R_1206_3216Metric_Pad1.42x1.75mm_HandSolder" V 6655 8550 50  0001 C CNN
F 3 "~" H 6725 8550 50  0001 C CNN
F 4 "32859526036" H 6725 8550 50  0001 C CNN "N° Fournisseur"
F 5 "311-10KERCT-ND" H 6725 8550 50  0001 C CNN "N° Digikey"
	1    6725 8550
	-1   0    0    -1  
$EndComp
$Comp
L archive:power_+3V3 #PWR0165
U 1 1 603D3FB7
P 6725 7900
F 0 "#PWR0165" H 6725 7750 50  0001 C CNN
F 1 "+3V3" H 6740 8073 50  0000 C CNN
F 2 "" H 6725 7900 50  0001 C CNN
F 3 "" H 6725 7900 50  0001 C CNN
	1    6725 7900
	1    0    0    -1  
$EndComp
Wire Wire Line
	6725 7900 6725 7950
$Comp
L archive:power_GND #PWR0166
U 1 1 603D3FBE
P 6725 8750
F 0 "#PWR0166" H 6725 8500 50  0001 C CNN
F 1 "GND" H 6725 8600 50  0000 C CNN
F 2 "" H 6725 8750 50  0001 C CNN
F 3 "" H 6725 8750 50  0001 C CNN
	1    6725 8750
	1    0    0    -1  
$EndComp
Wire Wire Line
	6725 8750 6725 8700
Wire Wire Line
	6725 8350 6725 8375
Text GLabel 6025 8150 0    50   Output ~ 0
P_COL3
Wire Wire Line
	6025 8150 6075 8150
Text GLabel 6825 8375 2    50   Output ~ 0
COL3
Wire Wire Line
	6825 8375 6725 8375
Connection ~ 6725 8375
Wire Wire Line
	6725 8375 6725 8400
$Comp
L archive:Device_Q_PNP_BEC Q4
U 1 1 604C25B2
P 8200 8150
F 0 "Q4" H 8391 8104 50  0000 L CNN
F 1 "BC856B" H 8391 8195 50  0000 L CNN
F 2 "Package_TO_SOT_SMD:SOT-23_Handsoldering" H 8400 8250 50  0001 C CNN
F 3 "~" H 8200 8150 50  0001 C CNN
F 4 "32959120963" H 8200 8150 50  0001 C CNN "N° Fournisseur"
F 5 "BC856BLT3GOSCT-ND" H 8200 8150 50  0001 C CNN "N° Digikey"
	1    8200 8150
	1    0    0    1   
$EndComp
$Comp
L archive:Device_R R27
U 1 1 604C25B9
P 7800 8150
F 0 "R27" V 7975 8100 50  0000 L CNN
F 1 "1[KΩ]" V 7900 8000 50  0000 L CNN
F 2 "Resistor_SMD:R_1206_3216Metric_Pad1.42x1.75mm_HandSolder" V 7730 8150 50  0001 C CNN
F 3 "~" H 7800 8150 50  0001 C CNN
F 4 "32859526036" H 7800 8150 50  0001 C CNN "N° Fournisseur"
F 5 "311-1.0KERCT-ND" H 7800 8150 50  0001 C CNN "N° Digikey"
	1    7800 8150
	0    -1   1    0   
$EndComp
Wire Wire Line
	8000 8150 7950 8150
$Comp
L archive:Device_R R28
U 1 1 604C25C1
P 8300 8550
F 0 "R28" H 8375 8600 50  0000 L CNN
F 1 "10[KΩ]" H 8350 8525 50  0000 L CNN
F 2 "Resistor_SMD:R_1206_3216Metric_Pad1.42x1.75mm_HandSolder" V 8230 8550 50  0001 C CNN
F 3 "~" H 8300 8550 50  0001 C CNN
F 4 "32859526036" H 8300 8550 50  0001 C CNN "N° Fournisseur"
F 5 "311-10KERCT-ND" H 8300 8550 50  0001 C CNN "N° Digikey"
	1    8300 8550
	-1   0    0    -1  
$EndComp
$Comp
L archive:power_+3V3 #PWR0167
U 1 1 604C25C7
P 8300 7900
F 0 "#PWR0167" H 8300 7750 50  0001 C CNN
F 1 "+3V3" H 8315 8073 50  0000 C CNN
F 2 "" H 8300 7900 50  0001 C CNN
F 3 "" H 8300 7900 50  0001 C CNN
	1    8300 7900
	1    0    0    -1  
$EndComp
Wire Wire Line
	8300 7900 8300 7950
$Comp
L archive:power_GND #PWR0168
U 1 1 604C25CE
P 8300 8750
F 0 "#PWR0168" H 8300 8500 50  0001 C CNN
F 1 "GND" H 8300 8600 50  0000 C CNN
F 2 "" H 8300 8750 50  0001 C CNN
F 3 "" H 8300 8750 50  0001 C CNN
	1    8300 8750
	1    0    0    -1  
$EndComp
Wire Wire Line
	8300 8750 8300 8700
Wire Wire Line
	8300 8350 8300 8375
Text GLabel 7600 8150 0    50   Output ~ 0
P_COL4
Wire Wire Line
	7600 8150 7650 8150
Text GLabel 8400 8375 2    50   Output ~ 0
COL4
Wire Wire Line
	8400 8375 8300 8375
Connection ~ 8300 8375
Wire Wire Line
	8300 8375 8300 8400
$Comp
L archive:Device_Q_PNP_BEC Q5
U 1 1 604E68B8
P 9675 8150
F 0 "Q5" H 9866 8104 50  0000 L CNN
F 1 "BC856B" H 9866 8195 50  0000 L CNN
F 2 "Package_TO_SOT_SMD:SOT-23_Handsoldering" H 9875 8250 50  0001 C CNN
F 3 "~" H 9675 8150 50  0001 C CNN
F 4 "32959120963" H 9675 8150 50  0001 C CNN "N° Fournisseur"
F 5 "BC856BLT3GOSCT-ND" H 9675 8150 50  0001 C CNN "N° Digikey"
	1    9675 8150
	1    0    0    1   
$EndComp
$Comp
L archive:Device_R R31
U 1 1 604E68BF
P 9275 8150
F 0 "R31" V 9450 8100 50  0000 L CNN
F 1 "1[KΩ]" V 9375 8000 50  0000 L CNN
F 2 "Resistor_SMD:R_1206_3216Metric_Pad1.42x1.75mm_HandSolder" V 9205 8150 50  0001 C CNN
F 3 "~" H 9275 8150 50  0001 C CNN
F 4 "32859526036" H 9275 8150 50  0001 C CNN "N° Fournisseur"
F 5 "311-1.0KERCT-ND" H 9275 8150 50  0001 C CNN "N° Digikey"
	1    9275 8150
	0    -1   1    0   
$EndComp
Wire Wire Line
	9475 8150 9425 8150
$Comp
L archive:Device_R R32
U 1 1 604E68C7
P 9775 8550
F 0 "R32" H 9850 8600 50  0000 L CNN
F 1 "10[KΩ]" H 9825 8525 50  0000 L CNN
F 2 "Resistor_SMD:R_1206_3216Metric_Pad1.42x1.75mm_HandSolder" V 9705 8550 50  0001 C CNN
F 3 "~" H 9775 8550 50  0001 C CNN
F 4 "32859526036" H 9775 8550 50  0001 C CNN "N° Fournisseur"
F 5 "311-10KERCT-ND" H 9775 8550 50  0001 C CNN "N° Digikey"
	1    9775 8550
	-1   0    0    -1  
$EndComp
$Comp
L archive:power_+3V3 #PWR0169
U 1 1 604E68CD
P 9775 7900
F 0 "#PWR0169" H 9775 7750 50  0001 C CNN
F 1 "+3V3" H 9790 8073 50  0000 C CNN
F 2 "" H 9775 7900 50  0001 C CNN
F 3 "" H 9775 7900 50  0001 C CNN
	1    9775 7900
	1    0    0    -1  
$EndComp
Wire Wire Line
	9775 7900 9775 7950
$Comp
L archive:power_GND #PWR0170
U 1 1 604E68D4
P 9775 8750
F 0 "#PWR0170" H 9775 8500 50  0001 C CNN
F 1 "GND" H 9775 8600 50  0000 C CNN
F 2 "" H 9775 8750 50  0001 C CNN
F 3 "" H 9775 8750 50  0001 C CNN
	1    9775 8750
	1    0    0    -1  
$EndComp
Wire Wire Line
	9775 8750 9775 8700
Wire Wire Line
	9775 8350 9775 8375
Text GLabel 9075 8150 0    50   Output ~ 0
P_COL5
Wire Wire Line
	9075 8150 9125 8150
Text GLabel 9875 8375 2    50   Output ~ 0
COL5
Wire Wire Line
	9875 8375 9775 8375
Connection ~ 9775 8375
Wire Wire Line
	9775 8375 9775 8400
Wire Notes Line
	5475 6625 5475 9000
Wire Notes Line
	5475 9000 11250 9000
Wire Notes Line
	11250 4975 11250 9000
Wire Notes Line
	5475 6625 8450 6625
Text Notes 5475 6700 0    50   ~ 0
Drive Collonnes
Wire Wire Line
	3800 7450 3800 7500
$Comp
L archive:Connector_TestPoint_Alt TP2
U 1 1 5ED89CBA
P 1575 9050
F 0 "TP2" V 1600 9250 50  0000 L CNN
F 1 "VDC" V 1525 9200 50  0000 L CNN
F 2 "TestPoint:TestPoint_Pad_1.5x1.5mm" H 1775 9050 50  0001 C CNN
F 3 "~" H 1775 9050 50  0001 C CNN
	1    1575 9050
	0    -1   -1   0   
$EndComp
$Comp
L archive:Connector_TestPoint_Alt TP3
U 1 1 5ED8CB0B
P 1575 9225
F 0 "TP3" V 1600 9425 50  0000 L CNN
F 1 "3V3" V 1525 9375 50  0000 L CNN
F 2 "TestPoint:TestPoint_Pad_1.5x1.5mm" H 1775 9225 50  0001 C CNN
F 3 "~" H 1775 9225 50  0001 C CNN
	1    1575 9225
	0    -1   -1   0   
$EndComp
$Comp
L archive:Connector_TestPoint_Alt TP4
U 1 1 5EDB0413
P 1575 9400
F 0 "TP4" V 1600 9600 50  0000 L CNN
F 1 "FTDI_Tx" V 1525 9550 50  0000 L CNN
F 2 "TestPoint:TestPoint_Pad_1.5x1.5mm" H 1775 9400 50  0001 C CNN
F 3 "~" H 1775 9400 50  0001 C CNN
	1    1575 9400
	0    -1   -1   0   
$EndComp
$Comp
L archive:Connector_TestPoint_Alt TP5
U 1 1 5EDD3F2F
P 1575 9575
F 0 "TP5" V 1600 9775 50  0000 L CNN
F 1 "FTDI_Rx" V 1525 9725 50  0000 L CNN
F 2 "TestPoint:TestPoint_Pad_1.5x1.5mm" H 1775 9575 50  0001 C CNN
F 3 "~" H 1775 9575 50  0001 C CNN
	1    1575 9575
	0    -1   -1   0   
$EndComp
$Comp
L archive:Connector_TestPoint_Alt TP6
U 1 1 5EE2218E
P 1575 9750
F 0 "TP6" V 1600 9950 50  0000 L CNN
F 1 "EN" V 1525 9900 50  0000 L CNN
F 2 "TestPoint:TestPoint_Pad_1.5x1.5mm" H 1775 9750 50  0001 C CNN
F 3 "~" H 1775 9750 50  0001 C CNN
	1    1575 9750
	0    -1   -1   0   
$EndComp
$Comp
L archive:Connector_TestPoint_Alt TP7
U 1 1 5EE45C93
P 2500 8875
F 0 "TP7" V 2525 9075 50  0000 L CNN
F 1 "P_COL1" V 2450 9025 50  0000 L CNN
F 2 "TestPoint:TestPoint_Pad_1.5x1.5mm" H 2700 8875 50  0001 C CNN
F 3 "~" H 2700 8875 50  0001 C CNN
	1    2500 8875
	0    -1   -1   0   
$EndComp
$Comp
L archive:Connector_TestPoint_Alt TP8
U 1 1 5EE69627
P 2500 9050
F 0 "TP8" V 2525 9250 50  0000 L CNN
F 1 "COL1" V 2450 9200 50  0000 L CNN
F 2 "TestPoint:TestPoint_Pad_1.5x1.5mm" H 2700 9050 50  0001 C CNN
F 3 "~" H 2700 9050 50  0001 C CNN
	1    2500 9050
	0    -1   -1   0   
$EndComp
$Comp
L archive:power_+3V3 #PWR0171
U 1 1 5EE8CEF6
P 1625 9225
F 0 "#PWR0171" H 1625 9075 50  0001 C CNN
F 1 "+3V3" V 1640 9353 50  0000 L CNN
F 2 "" H 1625 9225 50  0001 C CNN
F 3 "" H 1625 9225 50  0001 C CNN
	1    1625 9225
	0    1    1    0   
$EndComp
$Comp
L archive:Connector_TestPoint_Alt TP1
U 1 1 5EE8F1E0
P 1575 8875
F 0 "TP1" V 1600 9075 50  0000 L CNN
F 1 "GND" V 1525 9025 50  0000 L CNN
F 2 "TestPoint:TestPoint_Pad_1.5x1.5mm" H 1775 8875 50  0001 C CNN
F 3 "~" H 1775 8875 50  0001 C CNN
	1    1575 8875
	0    -1   -1   0   
$EndComp
$Comp
L archive:power_GND #PWR0172
U 1 1 5EEB29BE
P 1625 8875
F 0 "#PWR0172" H 1625 8625 50  0001 C CNN
F 1 "GND" V 1630 8747 50  0000 R CNN
F 2 "" H 1625 8875 50  0001 C CNN
F 3 "" H 1625 8875 50  0001 C CNN
	1    1625 8875
	0    -1   -1   0   
$EndComp
Wire Wire Line
	1625 8875 1575 8875
Wire Wire Line
	1575 9225 1625 9225
Wire Wire Line
	1600 9050 1575 9050
Text GLabel 1625 9400 2    50   Input ~ 0
FTDI_Tx
Text GLabel 1625 9575 2    50   Input ~ 0
FTDI_Rx
Wire Wire Line
	1625 9575 1575 9575
Wire Wire Line
	1575 9400 1625 9400
Text GLabel 1625 9750 2    50   Input ~ 0
EN
Wire Wire Line
	1625 9750 1575 9750
$Comp
L archive:Connector_TestPoint_Alt TP9
U 1 1 5F055D14
P 2500 9225
F 0 "TP9" V 2525 9425 50  0000 L CNN
F 1 "ROW_1" V 2450 9375 50  0000 L CNN
F 2 "TestPoint:TestPoint_Pad_1.5x1.5mm" H 2700 9225 50  0001 C CNN
F 3 "~" H 2700 9225 50  0001 C CNN
	1    2500 9225
	0    -1   -1   0   
$EndComp
Text GLabel 2550 8875 2    50   Input ~ 0
P_COL1
Text GLabel 2550 9050 2    50   Input ~ 0
COL1
Text GLabel 2550 9225 2    50   Input ~ 0
ROW1
Wire Wire Line
	2550 9225 2500 9225
Wire Wire Line
	2500 9050 2550 9050
Wire Wire Line
	2550 8875 2500 8875
$Comp
L archive:Connector_TestPoint_Alt TP10
U 1 1 5F119E3B
P 2500 9575
F 0 "TP10" V 2525 9775 50  0000 L CNN
F 1 "I2C_SCL" V 2450 9725 50  0000 L CNN
F 2 "TestPoint:TestPoint_Pad_1.5x1.5mm" H 2700 9575 50  0001 C CNN
F 3 "~" H 2700 9575 50  0001 C CNN
	1    2500 9575
	0    -1   -1   0   
$EndComp
$Comp
L archive:Connector_TestPoint_Alt TP11
U 1 1 5F192CCC
P 2500 9750
F 0 "TP11" V 2525 9950 50  0000 L CNN
F 1 "I2C_SDA" V 2450 9900 50  0000 L CNN
F 2 "TestPoint:TestPoint_Pad_1.5x1.5mm" H 2700 9750 50  0001 C CNN
F 3 "~" H 2700 9750 50  0001 C CNN
	1    2500 9750
	0    -1   -1   0   
$EndComp
Text GLabel 2550 9575 2    50   Input ~ 0
LCD_SCL
Text GLabel 2550 9750 2    50   Input ~ 0
LCD_SDA
Wire Wire Line
	2550 9750 2500 9750
Wire Wire Line
	2500 9575 2550 9575
Text GLabel 12225 1575 1    50   Input ~ 0
LCD_VO
Wire Wire Line
	12225 1575 12225 1650
$Comp
L archive:Connector_TestPoint_Alt TP12
U 1 1 5F23590B
P 3400 8875
F 0 "TP12" V 3425 9075 50  0000 L CNN
F 1 "LCD_VO" V 3350 9025 50  0000 L CNN
F 2 "TestPoint:TestPoint_Pad_1.5x1.5mm" H 3600 8875 50  0001 C CNN
F 3 "~" H 3600 8875 50  0001 C CNN
	1    3400 8875
	0    -1   -1   0   
$EndComp
Text GLabel 3450 8875 2    50   Input ~ 0
LCD_VO
Wire Wire Line
	3450 8875 3400 8875
$Comp
L archive:Connector_TestPoint_Alt TP13
U 1 1 5F2606A3
P 3400 9050
F 0 "TP13" V 3425 9250 50  0000 L CNN
F 1 "LCD_RS" V 3350 9200 50  0000 L CNN
F 2 "TestPoint:TestPoint_Pad_1.5x1.5mm" H 3600 9050 50  0001 C CNN
F 3 "~" H 3600 9050 50  0001 C CNN
	1    3400 9050
	0    -1   -1   0   
$EndComp
Text GLabel 3450 9050 2    50   Input ~ 0
LCD_RS
Wire Wire Line
	3450 9050 3400 9050
$Comp
L archive:Connector_TestPoint_Alt TP14
U 1 1 5F28834A
P 3400 9225
F 0 "TP14" V 3425 9425 50  0000 L CNN
F 1 "LCD_E" V 3350 9375 50  0000 L CNN
F 2 "TestPoint:TestPoint_Pad_1.5x1.5mm" H 3600 9225 50  0001 C CNN
F 3 "~" H 3600 9225 50  0001 C CNN
	1    3400 9225
	0    -1   -1   0   
$EndComp
Text GLabel 3450 9225 2    50   Input ~ 0
LCD_E
Wire Wire Line
	3450 9225 3400 9225
$Comp
L archive:Connector_TestPoint_Alt TP15
U 1 1 5F2B3272
P 3400 9400
F 0 "TP15" V 3425 9600 50  0000 L CNN
F 1 "LCD_D0" V 3350 9550 50  0000 L CNN
F 2 "TestPoint:TestPoint_Pad_1.5x1.5mm" H 3600 9400 50  0001 C CNN
F 3 "~" H 3600 9400 50  0001 C CNN
	1    3400 9400
	0    -1   -1   0   
$EndComp
$Comp
L archive:Connector_TestPoint_Alt TP16
U 1 1 5F2DB7AE
P 3400 9575
F 0 "TP16" V 3425 9775 50  0000 L CNN
F 1 "LCD_D1" V 3350 9725 50  0000 L CNN
F 2 "TestPoint:TestPoint_Pad_1.5x1.5mm" H 3600 9575 50  0001 C CNN
F 3 "~" H 3600 9575 50  0001 C CNN
	1    3400 9575
	0    -1   -1   0   
$EndComp
Wire Wire Line
	3450 9575 3400 9575
$Comp
L archive:Connector_TestPoint_Alt TP17
U 1 1 5F304372
P 3400 9750
F 0 "TP17" V 3425 9950 50  0000 L CNN
F 1 "LCD_D2" V 3350 9900 50  0000 L CNN
F 2 "TestPoint:TestPoint_Pad_1.5x1.5mm" H 3600 9750 50  0001 C CNN
F 3 "~" H 3600 9750 50  0001 C CNN
	1    3400 9750
	0    -1   -1   0   
$EndComp
Wire Wire Line
	3450 9750 3400 9750
$Comp
L archive:Connector_TestPoint_Alt TP18
U 1 1 5F32D3A0
P 3400 9925
F 0 "TP18" V 3425 10125 50  0000 L CNN
F 1 "LCD_D3" V 3350 10075 50  0000 L CNN
F 2 "TestPoint:TestPoint_Pad_1.5x1.5mm" H 3600 9925 50  0001 C CNN
F 3 "~" H 3600 9925 50  0001 C CNN
	1    3400 9925
	0    -1   -1   0   
$EndComp
Wire Wire Line
	3450 9925 3400 9925
Text GLabel 10775 2950 3    50   Input ~ 0
LCD_D0
Text GLabel 10875 2950 3    50   Input ~ 0
LCD_D1
Text GLabel 10975 2950 3    50   Input ~ 0
LCD_D2
Text GLabel 11075 2950 3    50   Input ~ 0
LCD_D3
Wire Wire Line
	10775 2950 10775 2150
Connection ~ 10775 2150
Wire Wire Line
	10775 2150 11175 2150
Wire Wire Line
	10875 2950 10875 2250
Connection ~ 10875 2250
Wire Wire Line
	10875 2250 10450 2250
Wire Wire Line
	10975 2950 10975 2350
Connection ~ 10975 2350
Wire Wire Line
	10975 2350 11175 2350
Wire Wire Line
	11075 2950 11075 2450
Connection ~ 11075 2450
Wire Wire Line
	11075 2450 10450 2450
Text GLabel 3450 9400 2    50   Input ~ 0
LCD_D0
Text GLabel 3450 9575 2    50   Input ~ 0
LCD_D1
Text GLabel 3450 9750 2    50   Input ~ 0
LCD_D2
Text GLabel 3450 9925 2    50   Input ~ 0
LCD_D3
Wire Wire Line
	3400 9400 3450 9400
Wire Notes Line
	1100 8775 3825 8775
Wire Notes Line
	3825 8775 3825 10050
Wire Notes Line
	3825 10050 1100 10050
Wire Notes Line
	1100 10050 1100 8775
Text Notes 2175 8775 2    100  ~ 0
Points de Test
Wire Notes Line
	2025 8775 2025 10050
Wire Notes Line
	2950 10050 2950 8775
$Comp
L archive:power_+VDC #PWR0173
U 1 1 5FA13E5F
P 1600 9050
F 0 "#PWR0173" H 1600 8950 50  0001 C CNN
F 1 "+VDC" V 1600 9250 50  0000 L CNN
F 2 "" H 1600 9050 50  0001 C CNN
F 3 "" H 1600 9050 50  0001 C CNN
	1    1600 9050
	0    1    1    0   
$EndComp
Wire Wire Line
	12000 3125 12000 3300
Text GLabel 4500 5350 2    50   BiDi ~ 0
LCD_BKL
Wire Wire Line
	4400 6750 4500 6750
$Comp
L archive:Device_Q_PNP_BEC Q6
U 1 1 5F0E4533
P 12100 2925
F 0 "Q6" H 12025 3150 50  0000 L CNN
F 1 "BC856B" H 11825 3075 50  0000 L CNN
F 2 "Package_TO_SOT_SMD:SOT-23_Handsoldering" H 12300 3025 50  0001 C CNN
F 3 "~" H 12100 2925 50  0001 C CNN
F 4 "32959120963" H 12100 2925 50  0001 C CNN "N° Fournisseur"
F 5 "BC856BLT3GOSCT-ND" H 12100 2925 50  0001 C CNN "N° Digikey"
	1    12100 2925
	-1   0    0    1   
$EndComp
$Comp
L archive:Device_R R36
U 1 1 5F1BF70D
P 12500 2925
F 0 "R36" V 12675 2875 50  0000 L CNN
F 1 "1[KΩ]" V 12600 2800 50  0000 L CNN
F 2 "Resistor_SMD:R_1206_3216Metric_Pad1.42x1.75mm_HandSolder" V 12430 2925 50  0001 C CNN
F 3 "~" H 12500 2925 50  0001 C CNN
F 4 "32859526036" H 12500 2925 50  0001 C CNN "N° Fournisseur"
F 5 "311-1.0KERCT-ND" H 12500 2925 50  0001 C CNN "N° Digikey"
	1    12500 2925
	0    -1   1    0   
$EndComp
Wire Wire Line
	12350 2925 12300 2925
Text GLabel 12700 2925 2    50   Input ~ 0
LCD_BKL
Wire Wire Line
	12650 2925 12700 2925
$Comp
L archive:Device_R R35
U 1 1 5F31EC64
P 12000 2400
F 0 "R35" H 12000 2250 50  0000 L CNN
F 1 "6[Ω]" H 12000 2150 50  0000 L CNN
F 2 "Resistor_SMD:R_1206_3216Metric_Pad1.42x1.75mm_HandSolder" V 11930 2400 50  0001 C CNN
F 3 "~" H 12000 2400 50  0001 C CNN
F 4 "32859526036" H 12000 2400 50  0001 C CNN "N° Fournisseur"
F 5 "311-6.20FRCT-ND" H 12000 2400 50  0001 C CNN "N° Digikey"
	1    12000 2400
	1    0    0    1   
$EndComp
Wire Wire Line
	12000 2050 12000 2250
Wire Wire Line
	12000 2725 12000 2550
$Comp
L projet-rescue:TPS63001-Regulator_Switching U2
U 1 1 5F484D47
P 5025 2225
F 0 "U2" H 5025 2850 50  0000 C CNN
F 1 "TPS63001DRCR" H 5025 2775 50  0000 C CNN
F 2 "Package_SON:Texas_DRC0010J_ThermalVias" H 5875 1675 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/tps63000.pdf" H 4725 2775 50  0001 C CNN
F 4 "296-19643-1-ND" H 5025 2225 50  0001 C CNN "N° Digikey"
	1    5025 2225
	1    0    0    -1  
$EndComp
$Comp
L projet-rescue:L-Device L1
U 1 1 5F489668
P 5025 1500
F 0 "L1" V 5215 1500 50  0000 C CNN
F 1 "2.2[μH]" V 5124 1500 50  0000 C CNN
F 2 "Inductor_SMD:L_Taiyo-Yuden_NR-24xx_HandSoldering" H 5025 1500 50  0001 C CNN
F 3 "~" H 5025 1500 50  0001 C CNN
F 4 "587-3544-1-ND" H 5025 1500 50  0001 C CNN "N° Digikey"
	1    5025 1500
	0    -1   -1   0   
$EndComp
Wire Wire Line
	5175 1500 5475 1500
Wire Wire Line
	5475 1500 5475 1825
Wire Wire Line
	5475 1825 5425 1825
Wire Wire Line
	4875 1500 4575 1500
Wire Wire Line
	4575 1500 4575 1825
Wire Wire Line
	4575 1825 4625 1825
Wire Wire Line
	5425 2025 5500 2025
Wire Wire Line
	5500 2025 5500 2225
Wire Wire Line
	5500 2225 5425 2225
$Comp
L archive:Device_CP1 C4
U 1 1 5F544BCB
P 5750 2375
F 0 "C4" H 5750 2275 50  0000 L CNN
F 1 "33[μF]" H 5750 2450 50  0000 L CNN
F 2 "Capacitor_SMD:C_1206_3216Metric_Pad1.42x1.75mm_HandSolder" H 5750 2375 50  0001 C CNN
F 3 "~" H 5750 2375 50  0001 C CNN
F 4 "33059508387" H 5750 2375 50  0001 C CNN "N° Fournisseur"
F 5 "399-4719-1-ND" H 5750 2375 50  0001 C CNN "N° Digikey"
	1    5750 2375
	1    0    0    -1  
$EndComp
$Comp
L archive:power_GND #PWR03
U 1 1 5F544BD1
P 5750 2950
F 0 "#PWR03" H 5750 2700 50  0001 C CNN
F 1 "GND" H 5755 2777 50  0000 C CNN
F 2 "" H 5750 2950 50  0001 C CNN
F 3 "" H 5750 2950 50  0001 C CNN
	1    5750 2950
	1    0    0    -1  
$EndComp
Wire Wire Line
	5750 2525 5750 2950
Wire Wire Line
	5500 2025 5750 2025
Wire Wire Line
	5750 2025 5750 2225
Connection ~ 5500 2025
$Comp
L archive:Device_CP1 C3
U 1 1 5F5A38C3
P 4200 2300
F 0 "C3" H 4200 2200 50  0000 L CNN
F 1 "10[μF]" H 4200 2375 50  0000 L CNN
F 2 "Capacitor_SMD:C_1206_3216Metric_Pad1.42x1.75mm_HandSolder" H 4200 2300 50  0001 C CNN
F 3 "~" H 4200 2300 50  0001 C CNN
F 4 "33059508387" H 4200 2300 50  0001 C CNN "N° Fournisseur"
F 5 "399-4788-1-ND" H 4200 2300 50  0001 C CNN "N° Digikey"
	1    4200 2300
	1    0    0    -1  
$EndComp
$Comp
L archive:power_GND #PWR01
U 1 1 5F5A38C9
P 4200 2950
F 0 "#PWR01" H 4200 2700 50  0001 C CNN
F 1 "GND" H 4205 2777 50  0000 C CNN
F 2 "" H 4200 2950 50  0001 C CNN
F 3 "" H 4200 2950 50  0001 C CNN
	1    4200 2950
	1    0    0    -1  
$EndComp
Wire Wire Line
	4625 2025 4550 2025
Wire Wire Line
	4550 2025 4550 2125
Wire Wire Line
	4550 2425 4625 2425
Wire Wire Line
	4625 2225 4550 2225
Connection ~ 4550 2225
Wire Wire Line
	4550 2225 4550 2425
Wire Wire Line
	4550 2125 4625 2125
Connection ~ 4550 2125
Wire Wire Line
	4550 2125 4550 2225
$Comp
L projet-rescue:GND-power #PWR02
U 1 1 5F664A07
P 5025 2950
F 0 "#PWR02" H 5025 2700 50  0001 C CNN
F 1 "GND" H 5030 2777 50  0000 C CNN
F 2 "" H 5025 2950 50  0001 C CNN
F 3 "" H 5025 2950 50  0001 C CNN
	1    5025 2950
	1    0    0    -1  
$EndComp
Wire Wire Line
	5025 2950 5025 2875
Wire Wire Line
	4925 2825 4925 2875
Wire Wire Line
	4925 2875 5025 2875
Connection ~ 5025 2875
Wire Wire Line
	5025 2875 5025 2825
Wire Wire Line
	4200 2150 4200 2025
Connection ~ 4550 2025
$Comp
L projet-rescue:+3V3-power #PWR04
U 1 1 5F793F3E
P 6200 2025
F 0 "#PWR04" H 6200 1875 50  0001 C CNN
F 1 "+3V3" V 6215 2153 50  0000 L CNN
F 2 "" H 6200 2025 50  0001 C CNN
F 3 "" H 6200 2025 50  0001 C CNN
	1    6200 2025
	0    1    1    0   
$EndComp
Wire Wire Line
	6200 2025 6125 2025
Connection ~ 5750 2025
Wire Wire Line
	4200 2450 4200 2950
Wire Wire Line
	4200 2025 4550 2025
Wire Wire Line
	3975 2025 4200 2025
Wire Notes Line
	4075 1225 6625 1225
Wire Notes Line
	6625 1225 6625 3175
Wire Notes Line
	6625 3175 4075 3175
Wire Notes Line
	4075 1225 4075 3175
Wire Notes Line
	1125 2675 4075 2675
Wire Notes Line
	4475 6600 4925 6600
NoConn ~ 4400 7050
NoConn ~ 4400 7150
Wire Wire Line
	4500 6650 4400 6650
Wire Wire Line
	4500 5350 4400 5350
Wire Notes Line
	4475 5275 4925 5275
Wire Notes Line
	4925 5275 4925 5400
Wire Notes Line
	4475 5400 4925 5400
Wire Notes Line
	4475 5275 4475 7025
Text Notes 4925 5400 0    50   ~ 0
Ecran LCD\nBacklight
$Comp
L archive:Device_LED D?
U 1 1 5F9E8C8B
P 6125 2325
F 0 "D?" V 6175 2475 50  0000 R CNN
F 1 "Rouge SMD" V 6100 2800 50  0000 R CNN
F 2 "LED_SMD:LED_1206_3216Metric_ReverseMount_Hole1.8x2.4mm" H 6125 2325 50  0001 C CNN
F 3 "~" H 6125 2325 50  0001 C CNN
F 4 "32828059657" H 6125 2325 50  0001 C CNN "N° Fournisseur"
F 5 "754-1158-1-ND" H 6125 2325 50  0001 C CNN "N° Digikey"
	1    6125 2325
	0    1    -1   0   
$EndComp
$Comp
L archive:Device_R R?
U 1 1 5F9E8C93
P 6125 2675
F 0 "R?" H 5975 2750 50  0000 L CNN
F 1 "330[Ω]" H 5800 2675 50  0000 L CNN
F 2 "Resistor_SMD:R_1206_3216Metric_Pad1.42x1.75mm_HandSolder" V 6055 2675 50  0001 C CNN
F 3 "~" H 6125 2675 50  0001 C CNN
F 4 "32859526036" H 6125 2675 50  0001 C CNN "N° Fournisseur"
F 5 "311-330FRCT-ND" H 6125 2675 50  0001 C CNN "N° Digikey"
	1    6125 2675
	-1   0    0    -1  
$EndComp
Wire Wire Line
	6125 2525 6125 2475
Wire Wire Line
	6125 2175 6125 2025
Connection ~ 6125 2025
Wire Wire Line
	6125 2025 5750 2025
$Comp
L archive:power_GND #PWR?
U 1 1 5FBAB8D9
P 6125 2950
F 0 "#PWR?" H 6125 2700 50  0001 C CNN
F 1 "GND" H 6130 2777 50  0000 C CNN
F 2 "" H 6125 2950 50  0001 C CNN
F 3 "" H 6125 2950 50  0001 C CNN
	1    6125 2950
	1    0    0    -1  
$EndComp
Wire Wire Line
	6125 2825 6125 2950
$EndSCHEMATC
