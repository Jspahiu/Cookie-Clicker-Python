"""
Extra Things:
- Add a icon for the turtle window (FINSHED)
- Add a icon for the text boxes windows (FINSHED)

"""


import turtle as t
import tkinter as tk
import random
import time

# The Clicker/Cookie Upgrader
Cookies_Baked = 2000
Cookies_Increased_Size = 1
Clicker_Upgrade_Price = 15
Amount_Of_Clickers = 0
# Grandma Ugrade Stuff
Grandma_Upgrade_Price = 100
Amount_Of_Grandmas = 0
Amount_Grandmas_Make = 1
# Farm Ugrade Stuff
Farm_Upgrade_Price = 1000
Amount_Of_Farms = 0
Amount_Farm_Make = 10


Screen = t.Screen()
Screen.title("Cookie Clicker")
Screen.setup(1200,620)
Screen.bgpic("background.gif")


# Access the underlying tkinter.Tk instance
tk_screen = Screen.getcanvas().winfo_toplevel()

# Load an image file to be used as the icon
icon_image = tk.PhotoImage(file="icon.png")  # Replace "icon.png" with your icon file path

# Set the icon
tk_screen.iconphoto(True, icon_image)

def cookie_clicked(x,y):
    global Cookies_Baked, Cookies_Increased_Size
    Cookies_Baked += Cookies_Increased_Size
    drawer.clear()
    drawer.write(f"Cookies Baked: {Cookies_Baked}", move=False, align="center", font=("Arial", 40, "normal"))

# Draw Things Stuff (Size means the write size thing NEEDS TO BE INT)
def draw_menu(draw, text, size):
    global Clicker_Upgrade_Price
    draw.write(text, move=False, align="center", font=("Arial", size, "normal"))

# Cookie Clicker Upgrade for clicker
def clicker_upgrade(x,y):
    global Cookies_Increased_Size, Cookies_Baked, Clicker_Upgrade_Price, Amount_Of_Clickers
    if Cookies_Baked >= Clicker_Upgrade_Price:
        Cookies_Increased_Size += 1
        Cookies_Baked -= Clicker_Upgrade_Price
        Clicker_Upgrade_Price += 5
        Amount_Of_Clickers += 1
        drawer.clear()
        drawer.write(f"Cookies Baked: {Cookies_Baked}", move=False, align="center", font=("Arial", 40, "normal"))
        cookie_upgrader.clear()  # Clear the old upgrade price text
        cookie_upgrader.goto(200,200)
        draw_menu(cookie_upgrader, "Clicker Upgrade " + str(Clicker_Upgrade_Price) + " Cookies for each upgrade!)", 20)  # Draw the updated upgrade price
        cookie_upgrader.goto(220,150)

# Grandma Upgrade
def grandma_upgrade(x,y):
    global Cookies_Increased_Size, Cookies_Baked, Grandma_Upgrade_Price, Amount_Of_Grandmas
    if Amount_Of_Grandmas >= 1:
        # time.sleep(1)
        Total_Amount_Grandmas_Make = Amount_Of_Grandmas * Amount_Grandmas_Make
        Cookies_Baked += Total_Amount_Grandmas_Make
        drawer.clear()
        drawer.write(f"Cookies Baked: {Cookies_Baked}", move=False, align="center", font=("Arial", 40, "normal"))
    if Cookies_Baked >= Grandma_Upgrade_Price:
        Cookies_Baked -= Grandma_Upgrade_Price
        Grandma_Upgrade_Price += 10
        Amount_Of_Grandmas += 1
        drawer.clear()
        drawer.write(f"Cookies Baked: {Cookies_Baked}", move=False, align="center", font=("Arial", 40, "normal"))
        Grandma_Upgrader.clear()  # Clear the old upgrade price text
        Grandma_Upgrader.goto(220,80)
        draw_menu(Grandma_Upgrader, "Grandma Upgrade " + str(Grandma_Upgrade_Price) + " Cookies for each upgrade!)", 20)  # Draw the updated upgrade price
        Grandma_Upgrader.goto(220,20)

# Cookie Clicker Upgrade for clicker
def farm_upgrade(x,y):
    global Cookies_Increased_Size, Cookies_Baked, Farm_Upgrade_Price, Amount_Of_Farms, Amount_Farm_Make
    if Amount_Of_Farms >= 1:
        # time.sleep(1)
        Total_Amount_Farms_Make = Amount_Of_Farms * Amount_Farm_Make
        Cookies_Baked += Total_Amount_Farms_Make
        drawer.clear()
        drawer.write(f"Cookies Baked: {Cookies_Baked}", move=False, align="center", font=("Arial", 40, "normal"))
    if Cookies_Baked >= Farm_Upgrade_Price:
        Cookies_Baked -= Farm_Upgrade_Price
        Farm_Upgrade_Price += 20
        Amount_Of_Farms += 1
        drawer.clear()
        drawer.write(f"Cookies Baked: {Cookies_Baked}", move=False, align="center", font=("Arial", 40, "normal"))
        Farm_Upgrader.clear()  # Clear the old upgrade price text
        Farm_Upgrader.goto(220,-60)
        draw_menu(Farm_Upgrader, "Farm Upgrade " + str(Farm_Upgrade_Price) + " Cookies for each upgrade!)", 20)  # Draw the updated upgrade price
        Farm_Upgrader.goto(220,-120)


def View_Sell(x,y):
    global Amount_Of_Grandmas, Amount_Of_Farms, Amount_Of_Clickers, Cookies_Baked, Farm_Upgrade_Price, Clicker_Upgrade_Price, Grandma_Upgrade_Price, Cookies_Increased_Size
    t.textinput("Viewer", f"You have {Amount_Of_Clickers} clicker upgrades, {Amount_Of_Grandmas} grandma upgrades, and {Amount_Of_Farms} farm upgrades")
    input2 = t.textinput("Sell", "Do you want to sell anything? y/n (made sure if choosed no, click cancel). If yes, please type what you want to sell").lower()
    if Amount_Of_Clickers >= 1 or Amount_Of_Grandmas >= 1 or Amount_Of_Farms >= 1:
            if "clicker" in input2:
                Amount_To_Sell = t.numinput("Sell", "How many you want to sell? (MAKE SURE ITS NOT DECIMAL OR ROUNDING OCCURS)", 1, 1, int(Amount_Of_Clickers))
                # print(Amount_Of_Clickers)
                Amount_To_Sell = round(int(Amount_To_Sell))
                Cookies_Increased_Size -= Amount_To_Sell
                Amount_Of_Clickers -= Amount_To_Sell
                Amount_Sell_Back = int(Clicker_Upgrade_Price/3.75) * Amount_To_Sell
                print(Amount_Sell_Back)
                Clicker_Upgrade_Price = Clicker_Upgrade_Price - 5 * Amount_To_Sell
                Cookies_Baked += Amount_Sell_Back
                # print(Amount_Of_Clickers)
                drawer.clear()
                drawer.write(f"Cookies Baked: {Cookies_Baked}", move=False, align="center", font=("Arial", 40, "normal"))
                cookie_upgrader.clear() 
                cookie_upgrader.goto(200,200)
                draw_menu(cookie_upgrader, "Clicker Upgrade " + str(Clicker_Upgrade_Price) + " Cookies for each upgrade!)", 20)  # Draw the updated upgrade price
                cookie_upgrader.goto(220,150)

            elif "grandma" in input2:
                if Amount_Of_Grandmas >= 1:
                    Amount_To_Sell = t.numinput("Sell", "How many you want to sell? (MAKE SURE ITS NOT DECIMAL OR ROUNDING OCCURS)", 1, 1, int(Amount_Of_Grandmas))
                    # print(Amount_Of_Clickers)
                    Amount_To_Sell = round(int(Amount_To_Sell))
                    Amount_Of_Grandmas -= Amount_To_Sell
                    Amount_Sell_Back = int(Grandma_Upgrade_Price/3.75) * Amount_To_Sell
                    print(Amount_Sell_Back)
                    Grandma_Upgrade_Price = Grandma_Upgrade_Price - 5 * Amount_To_Sell
                    Cookies_Baked += Amount_Sell_Back
                    # print(Amount_Of_Clickers)
                    drawer.clear()
                    drawer.write(f"Cookies Baked: {Cookies_Baked}", move=False, align="center", font=("Arial", 40, "normal"))
                    Grandma_Upgrader.clear()
                    Grandma_Upgrader.goto(220,80)
                    draw_menu(Grandma_Upgrader, "Grandma Upgrade " + str(Grandma_Upgrade_Price) + " Cookies for each upgrade!", 20)
                    Grandma_Upgrader.goto(220,20)
                else:
                    t.textinput("ERROR", "Sorry, you do not have any upgrades to sell this!")
                
        
            elif "farm" in input2:
                if Amount_Of_Farms >= 1:
                    Amount_To_Sell = t.numinput("Sell", "How many you want to sell? (MAKE SURE ITS NOT DECIMAL OR ROUNDING OCCURS)", 1, 1, int(Amount_Of_Farms))
                    # print(Amount_Of_Clickers)
                    Amount_To_Sell = round(int(Amount_To_Sell))
                    Amount_Of_Farms -= Amount_To_Sell
                    Amount_Sell_Back = int(Farm_Upgrade_Price/3.75) * Amount_To_Sell
                    print(Amount_Sell_Back)
                    Farm_Upgrade_Price = Farm_Upgrade_Price - 5 * Amount_To_Sell
                    Cookies_Baked += Amount_Sell_Back
                    # print(Amount_Of_Clickers)
                    drawer.clear()
                    drawer.write(f"Cookies Baked: {Cookies_Baked}", move=False, align="center", font=("Arial", 40, "normal"))
                    Farm_Upgrader.clear()
                    Farm_Upgrader.goto(220,-60)
                    draw_menu(Farm_Upgrader, "Farm Upgrade " + str(Farm_Upgrade_Price) + " Cookies for each upgrade!", 20)
                    Farm_Upgrader.goto(220,-120)
                else:
                    t.textinput("ERROR", "Sorry, you do not have any upgrades to sell this!")
            else:
                t.textinput("ERROR","ERROR: NOT A OPTION!")
    else:
        t.textinput("ERROR", "Sorry, you do not have any upgrades to sell this!")

# Basic Drawer Stuff
drawer = t.Turtle()
drawer.penup()
drawer.speed(0)
drawer.goto(0,0)
drawer.hideturtle()

# Basic Cookie Stuff
cookie = t.Turtle()
cookie.speed(0)
cookie.penup()
cookie.goto(-330,-30)
Screen.addshape('Cookie_Clicker_Cookie.gif')
cookie.shape('Cookie_Clicker_Cookie.gif')

# Basic Cookies Baked Thing
drawer.goto(0,250)
drawer.write(f"Cookies Baked: {Cookies_Baked}", move=False, align="center", font=("Arial", 40, "normal"))

# The Cookie Upgrader Basics
cookie_upgrader = t.Turtle()
cookie_upgrader.penup()
cookie_upgrader.speed(0)
cookie_upgrader.goto(0,0)
Screen.addshape('Click_Here_Button.gif')
cookie_upgrader.shape('Click_Here_Button.gif')


# Menu Cookie Upgrader
cookie_upgrader.goto(200,200)
draw_menu(cookie_upgrader, "Clicker Upgrade " + str(Clicker_Upgrade_Price) + " Cookies for each upgrade!", 20)
cookie_upgrader.goto(220,150)

# The Grandma Upgrade Basics
Grandma_Upgrader = t.Turtle()
Grandma_Upgrader.penup()
Grandma_Upgrader.speed(0)
Grandma_Upgrader.goto(0,0)


# Menu Grandma Upgrader
Grandma_Upgrader.goto(220,80)
draw_menu(Grandma_Upgrader, "Grandma Upgrade " + str(Grandma_Upgrade_Price) + " Cookies for each upgrade!", 20)
Grandma_Upgrader.goto(220,20)
Screen.addshape('Click_Here_Button.gif')
Grandma_Upgrader.shape('Click_Here_Button.gif')

# The Farm Upgrade Basics
Farm_Upgrader = t.Turtle()
Farm_Upgrader.penup()
Farm_Upgrader.speed(0)
Farm_Upgrader.goto(0,0)

# Menu Grandma Upgrader
Farm_Upgrader.goto(220,-60)
draw_menu(Farm_Upgrader, "Farm Upgrade " + str(Farm_Upgrade_Price) + " Cookies for each upgrade!", 20)
Farm_Upgrader.goto(220,-120)
Screen.addshape('Click_Here_Button.gif')
Farm_Upgrader.shape('Click_Here_Button.gif')

# Amount of Things/Sell
Show = t.Turtle()
Show.penup()
Show.speed(0)
Show.goto(0,0)

Show.goto(220,-200)
draw_menu(Show, "View Upgrades and Sell Upgrades", 20)
Show.goto(220,-250)
Screen.addshape('Click_Here_Button.gif')
Show.shape('Click_Here_Button.gif')

# The While Loop that gets the grandma's working while even all the controls work!
while True:
    Screen.listen()
    cookie.onclick(cookie_clicked)
    cookie_upgrader.onclick(clicker_upgrade)
    Grandma_Upgrader.onclick(grandma_upgrade)
    Farm_Upgrader.onclick(farm_upgrade)
    Show.onclick(View_Sell)
    time.sleep(1)
    if Amount_Of_Grandmas >= 1:
        Total_Amount_Grandmas_Make = Amount_Of_Grandmas * Amount_Grandmas_Make
        Cookies_Baked =  Total_Amount_Grandmas_Make + Cookies_Baked
        drawer.clear()
        drawer.write(f"Cookies Baked: {Cookies_Baked}", move=False, align="center", font=("Arial", 40, "normal")) 
    if Amount_Of_Farms >= 1:
        Total_Amount_Farm_Make = Amount_Of_Farms * Amount_Farm_Make
        Cookies_Baked =  Total_Amount_Farm_Make + Cookies_Baked
        drawer.clear()
        drawer.write(f"Cookies Baked: {Cookies_Baked}", move=False, align="center", font=("Arial", 40, "normal"))   




t.done()