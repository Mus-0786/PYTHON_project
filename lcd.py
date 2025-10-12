#!/usr/bin/env python _
# -*- coding: utf-8 -*-
import time
import RPi.GPIO as GPIO
import sys
from threading import Thread
from pyfingerprint.pyfingerprint import PyFingerprint
#############GPIO configuration#######
GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
######################################
################## Global Variables #############
#Initialize Fingerprint Module object
try:
 fingerprint_module = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)
 if ( fingerprint_module.verifyPassword() == False ):
 raise ValueError('The given fingerprint sensor password is wrong!')
except:
 try:
 fingerprint_module = PyFingerprint('/dev/ttyUSB1', 57600, 0xFFFFFFFF, 0x00000000)
 if ( fingerprint_module.verifyPassword() == False ):
 raise ValueError('The given fingerprint sensor password is wrong!')
 except:
 try:
 fingerprint_module = PyFingerprint('/dev/ttyUSB2', 57600, 0xFFFFFFFF, 0x00000000)
 if ( fingerprint_module.verifyPassword() == False ):
 raise ValueError('The given fingerprint sensor password is wrong!')
 except:
 try:
 fingerprint_module = PyFingerprint('/dev/ttyUSB3', 57600, 0xFFFFFFFF, 0x00000000)
 if ( fingerprint_module.verifyPassword() == False ):
 raise ValueError('The given fingerprint sensor password is wrong!')
 except Exception as e:
 print('Exception message: ' + str(e))
 exit(1)
pass
 pass
 pass
 pass
'''
try:
 fingerprint_module = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)
 if ( fingerprint_module.verifyPassword() == False ):
 raise ValueError('The given fingerprint sensor password is wrong!')
except Exception as e:
 print('Exception message: ' + str(e))
 exit(1)
'''
################## Lcd defines #################
# Define GPIO to LCD mapping
LCD_RS = 13
LCD_E = 19
LCD_D4 = 6
LCD_D5 = 5
LCD_D6 = 21
LCD_D7 = 26
#configure GPIO as output
GPIO.setup(LCD_E, GPIO.OUT) # E
GPIO.setup(LCD_RS, GPIO.OUT) # RS
GPIO.setup(LCD_D4, GPIO.OUT) # DB4
GPIO.setup(LCD_D5, GPIO.OUT) # DB5
GPIO.setup(LCD_D6, GPIO.OUT) # DB6
GPIO.setup(LCD_D7, GPIO.OUT) # DB7
# Define some device constants
LCD_WIDTH = 16 # Maximum characters per line
LCD_CHR = True
LCD_CMD = False
LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line
# Timing constants
E_PULSE = 0.0005
E_DELAY = 0.0005
LCD_SCRL_DEL = 0.14529 #LCD scrolling delay
#LCD function to initialize, display character on it.
def lcd_init():
 # Initialise display
 lcd_byte(0x33,LCD_CMD) # 110011 Initialise
def lcd_byte(bits, mode):
 # Send byte to data pins
 # bits = data
 # mode = True for character or False for command
 GPIO.output(LCD_RS, mode) # RS
 # High bits
 GPIO.output(LCD_D4, False)
 GPIO.output(LCD_D5, False)
 GPIO.output(LCD_D6, False)
 GPIO.output(LCD_D7, False)
 if bits&0x10==0x10:
 GPIO.output(LCD_D4, True)
 if bits&0x20==0x20:
 GPIO.output(LCD_D5, True)
 if bits&0x40==0x40:
 GPIO.output(LCD_D6, True)
 if bits&0x80==0x80:
 GPIO.output(LCD_D7, True)
 # Toggle 'Enable' pin
 lcd_toggle_enable()
 # Low bits
 GPIO.output(LCD_D4, False)
 GPIO.output(LCD_D5, False)
 GPIO.output(LCD_D6, False)
 GPIO.output(LCD_D7, False)
 if bits&0x01==0x01:
 GPIO.output(LCD_D4, True)
 if bits&0x02==0x02:
 GPIO.output(LCD_D5, True)
 if bits&0x04==0x04:
 GPIO.output(LCD_D6, True)
 if bits&0x08==0x08:
 GPIO.output(LCD_D7, True)
 # Toggle 'Enable' pin
 lcd_toggle_enable()
def lcd_toggle_enable():
# Toggle enable
 time.sleep(E_DELAY)
 GPIO.output(LCD_E, True)
 time.sleep(E_PULSE)
 GPIO.output(LCD_E, False)
 time.sleep(E_DELAY)
def lcd_string(message,line):
 # Send string to display
 message = message.ljust(LCD_WIDTH," ")
 lcd_byte(line, LCD_CMD)
 for i in range(LCD_WIDTH):
 lcd_byte(ord(message[i]),LCD_CHR)
def lcd_string_scroll(message, line, SCL_DELAY):
 string = message.strip()
 string = " " + string
 #print "length = " + str(len(string))
 if line == 1:
 lcd_string(" ", line)
 for i in range(len(message)+1+16):
 lcd_string(string, line)
 time.sleep(SCL_DELAY)
 string = string[1:] + " "
 pass
 else:
 lcd_string(" ", line)
 for i in range(len(message)+1+16):
 lcd_string(string, line)
 time.sleep(SCL_DELAY)
 string = string[1:] + " "
 pass
################## End of Lcd defines #################
################## User function #######################
def delayms(time_in_msec):
 time.sleep( (time_in_msec/1000) )
 pass
def delaysec(time_in_sec):
 time.sleep(time_in_sec)
def enrollFingerInDB():
 print "Enroll your Finger into Fingerprint Database"
#========================== Start ============================

 try
