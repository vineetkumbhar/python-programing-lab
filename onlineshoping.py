#vineet kumbhar
#roll no. 32


from easygui import *
import sys
while 1:
     msgbox("online shopping!")
     msg ="which website do you want to use?"
     title = "online shopping websites"
     choices = ["amazon", "flipcart", "snap deal"]
     choice = choicebox(msg, title, choices)
     msgbox("You chose: " + str(choice), "website chosen")
    # note that we convert choice to string, in case
    # the user cancelled the choice, and we got None.
     if choice == "amazon":
      msg ="what you want to buy"
      title  ="wide range of online products"
      choices = ["cloths", "electronics", "kitchen appliances", "sports"]
      choice = choicebox(msg, title, choices)
     elif choice == "flipcart":
      msg ="what you want to buy"
      title  ="welcome to flipcart"
      choices = ["cloths", "kitchen appliances", "sports", "electronics", "automobile accesories"]
      choice = choicebox(msg, title, choices)

     elif choice == "snap deal":
      msg ="what you want to buy"
      title  ="welcome to sanp deal"
      choices = ["cloths", "kitchen appliances", "chimies", "electronics", "automobile accesories"]
      choice = choicebox(msg, title, choices)
      msgbox("You chose: " + str(choice), "website chosen")


     if choice == "cloths":
      msg ="which brand you want   to buy"
      title  ="brands available"
      choices = ["puma", "nike", "zara", "louise phillips"]
      choice = choicebox(msg, title, choices)

     if choice == "puma":
      msg = "which dealer you want to chose"
      title  ="diffrent dealer"
      choices = ["mukesh :-price 2,300 rs", "ramesh :- 2,100 rs", "jaya :- 2,500 rs"]
      choice = choicebox(msg, title, choices)


     elif choice == "nike":
      msg = "which dealer you want to chose"
      title  ="diffrent dealer"
      choices = ["blac jeans:-price 1,000 rs", "blue shorts :- 2,100 rs", "dark brown shirt:-  2,000 rs"]
      choice = choicebox(msg, title, choices)


     elif choice == "louise phillips":
      msg = "which dealer you want to chose"
      title  ="diffrent dealer"
      choices = ["harshit :-price 1,300 rs", "akash :- 2,100 rs", "hema :- 2,000 rs"]
      choice = choice1box(msg, title, choices)



     elif choice == "zara":
      msg = "which dealer you want to chose"
      title  ="diffrent dealer"
      choices = ["harsh :-price 4,300 rs", "ankit :- 3,100 rs", "sushma :- 4,500 rs"]
      choice = choicebox(msg, title, choices)



     if choice == "kitchen appliances":
      msg = "what you want to buy"
      title  ="what kitchen appliances  you want"
      choices = ["mixers ", "dinner set", "microwave ovens","water purifiers"]
      choice = choicebox(msg, title, choices)

      if choice == "mixers":
       msg = "which company you want"
       title  ="diffrent comapnies"
       choices = ["panasonic :- 2,400 ", "havels:-4,500", "bajaj :- 1500"]
       choice = choicebox(msg, title, choices)

      elif choice == "dinner set":
       msg = "what you want to buy"
       title  ="what which company   you want"
       choices = ["cello :- 1,400 ", "corelle:-4,500", "amazon basics :- 1500"]
       choice = choicebox(msg, title, choices)

      elif choice == "microwave ovens":
       msg = "what you want to buy"
       title  ="what which company   you want"
       choices = ["panasonic :- 8,400 ", "havels:-10,500", "bajaj :- 5,500"]
       choice = choicebox(msg, title, choices)

      elif choice == "water purifiers":
       msg = "what you want to buy"
       title  ="what which company   you want"
       choices = ["kent :- 22,400 ", "pure it:-42,500", "livpure :- 12,500"]
       choice = choicebox(msg, title, choices)


     if choice == "electronics":
      msg = "what you want to buy"
      title  ="what type of electronic device   you want"
      choices = ["computer ", "laptops", "mobile phones",]
      choice = choicebox(msg, title, choices)

      if choice == "computer":
       msg = "which company you want"
       title  ="diffrent comapnies"
       choices = ["hp :- 45,400 ", "asus:-65,500", "dell :- 85,500"]
       choice = choicebox(msg, title, choices)

      elif choice == "laptops":
       msg = "what you want to buy"
       title  ="what which company   you want"
       choices = ["asus i5 :- 65,400 ", "hp i7:-86,500", "dell i3 :- 35,500"]
       choice = choicebox(msg, title, choices)

      elif choice == "mobile phones":
       msg = "what you want to buy"
       title  ="what which company   you want"
       choices = ["one plus 6 :- 39,400 ", "samsung note 5:-50,500", " redmi note 5 :- 15,500 ", " vivo v9 :- 21,599"]
       choice = choicebox(msg, title, choices)

       msgbox("You chose: " + str(choice), "website chosen")


      msg = "Do you want to continue?"
      title = "Please Confirm"
     if ccbox(msg, title):     # show a Continue/Cancel dialog
        pass  # user chose Continue
     else:
        sys.exit(0)
