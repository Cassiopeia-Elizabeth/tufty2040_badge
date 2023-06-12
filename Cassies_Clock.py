from picographics import PicoGraphics, DISPLAY_TUFTY_2040 #Imports tufty 2040 display driver.
from pimoroni_i2c import PimoroniI2C #Imports I2C library for RTC.
from breakout_rtc import BreakoutRTC #Imports Breakout library for the RTC.
import time #Imports time moule.

PINS_BREAKOUT_GARDEN = {"sda": 4, "scl": 5}  # i2c pins 4, 5 for Breakout Garden
PINS_PICO_EXPLORER = {"sda": 20, "scl": 21}  # Default i2c pins for Pico Explorer
i2c = PimoroniI2C(**PINS_BREAKOUT_GARDEN)
rtc = BreakoutRTC(i2c)
display = PicoGraphics(display=DISPLAY_TUFTY_2040) #Set the display to RGB332.
WIDTH, HEIGHT = display.get_bounds() #Sets the useable area of the screen to 320 x 240.
display.set_backlight(1.0) #Sets the back light on the lcd to max brightness.

# 2bit Demichrome colour palette by Space Sandwich - https://lospec.com/palette-list/2bit-demichrome
LIGHTEST = display.create_pen(233, 239, 236)
LIGHT = display.create_pen(160, 160, 139)
DARK = display.create_pen(85, 85, 104)
DARKEST = display.create_pen(33, 30, 32)

HEADER1 = "Cassiopeia's Clock" #Title/header of clock.
HEADER2 = " Says it is: "
FOOTER = "You're Welcome!!!!" #Footer of clock.
TIME = "Time "
DATE = "Date "

BORDER_SIZE = 4
PADDING = 10
HEADER_HEIGHT = 70
FOOTER_HEIGHT = 50

def draw_badge():
    #Draw border.
    display.set_pen(LIGHTEST)
    display.clear()

    #Draw background.
    display.set_pen(DARK)
    display.rectangle(BORDER_SIZE, BORDER_SIZE, WIDTH - (BORDER_SIZE * 2), HEIGHT - (BORDER_SIZE * 2))

    #Draw Header Box.
    display.set_pen(DARKEST)
    display.rectangle(BORDER_SIZE, BORDER_SIZE, WIDTH - (BORDER_SIZE * 2), HEADER_HEIGHT)
    
    #Draw Footer.
    display.set_pen(DARKEST)
    display.rectangle(BORDER_SIZE, 186-BORDER_SIZE, WIDTH - (BORDER_SIZE * 2), FOOTER_HEIGHT)
    
    #Draw Header Text.
    display.set_pen(LIGHT)
    display.set_font("bitmap6")
    display.text(HEADER1, BORDER_SIZE + (2*PADDING), BORDER_SIZE + PADDING, WIDTH, 3)
    display.text(HEADER2, BORDER_SIZE + 60 , 42, WIDTH, 3)
    
    #Draw Footer text.
    display.set_pen(LIGHT)
    display.set_font("bitmap6")
    display.text(FOOTER, BORDER_SIZE + 35, 200, WIDTH, 3)
    
def draw_clock():
    #Set to 24 hours
    if rtc.is_12_hour():
        rtc.set_24_hour()
    rtc.enable_periodic_update_interrupt(True)
    
    
        
    if rtc.read_periodic_update_interrupt_flag():
        rtc.clear_periodic_update_interrupt_flag()
       
    #Set format of time and date.
        #display.update()
    if rtc.update_time():
     rtc_date = rtc.string_date()
    
    rtc_time = rtc.string_time()
    time_now = str(rtc_time)
    date_now = str(rtc_date)
    actual_time = TIME + str(time_now)
    actual_date = DATE + str(date_now)
       
       #Draw Clock and date.
           
    display.set_pen(LIGHTEST)
    display.set_font("bitmap8")
    display.text(actual_time, BORDER_SIZE+30, 90, WIDTH, 4)
    display.text(actual_date, BORDER_SIZE+10, 140, WIDTH, 4)
    display.update()
    #time.sleep(0.1)
                
    display.set_pen(DARK)
    display.set_font("bitmap8")
    display.text(actual_time, BORDER_SIZE+30, 90, WIDTH, 4)
    display.text(actual_date, BORDER_SIZE+10, 140, WIDTH, 4)
    #display.update()
           
           
           
           
           

while True:
    draw_badge()
    draw_clock()
    
    
    


