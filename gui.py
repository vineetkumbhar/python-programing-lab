

from easygui import *
import sys
while 1:
     msgbox("online shopping!")

     msg ="which website do you want to use?"
     title = "online shopping websites"
     choices = ["amazon", "flipcart", "snap deal", "mynntra"]
     choice = choicebox(msg, title, choices)
     msgbox("You chose: " + str(choice), "website chosen")


    # note that we convert choice to string, in case
    # the user cancelled the choice, and we got None.


     if choice == "amazon":
      msg ="what you want to buy"
      title  ="wide range of online products"
      choices = ["cloths", "electronics", "kitchen appliances", "sports", "automobile accesories"]
      choice = choicebox(msg, title, choices)


     elif choice == "flipcart":
      msg ="what you want to buy"
      title  ="welcome to flipcart"
      choices = ["cloths", "kitchen appliances", "sports", "electronics", "automobile accesories"]
      choice = choicebox(msg, title, choices)

     elif choice == "snap deal":
      msg ="what you want to buy"
      title  ="welcome to sanp deal"
      choices = ["cloths", "kitchen appliances", "sports", "electronics", "automobile accesories"]
      choice = choicebox(msg, title, choices)
    


     if choice == "cloths":
      msg ="which brand you want   to buy"
      title  ="brands available"
      choices = ["puma", "nike", "vip", "zara", "us polo", "peter england", "louise phillips"]
      choice = choicebox(msg, title, choices)
 
     elif choice == "electronics":
      msg = "what you want to buy"
      title  ="what type of electronic devices you want"
      choices = ["mobile", "TV", "laptops","computer", "headphones"]
      choice = choicebox(msg, title, choices)
      msgbox("You chose: " + str(choice), "website chosen")
   
     if choice == "puma":
      msg = "which dealer you want to chose"
      title  ="diffrent dealer"
      choices = ["mukesh :-price 2,300 rs", "ramesh :- 2,100 rs", "jaya :- 2,500 rs"]
      choice = choicebox(msg, title, choices)
      msgbox("You chose: " + str(choice), "website chosen")  


      msg = "Do you want to continue?"
      title = "Please Confirm"
     if ccbox(msg, title):     # show a Continue/Cancel dialog
        pass  # user chose Continue
     else:
        sys.exit(0)

