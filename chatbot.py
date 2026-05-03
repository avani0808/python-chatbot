import random 
print("---------------------Welcome To The ChatBox----------------------")
user = input("You : ").lower().strip()

if user in ["hy", "hey", "hello", "hi"] :
    print("Chatbot : Hey!, How are you buddy?")

elif user in ["i am fine, what about you",
              "i am fine, how are you?" ,
              "i am fine, you?" , 
              "i am fine, and you?",
              "i am fine how are you?" ]:
       print("ChatBot : I am handsome buddy!, Hahaha...😄\n "
       "         Tell me what's on your mind?")
elif user in ["i am fine",
               "fine"]:
     print("ChatBot : That's great. So what's going on buddy? ")

elif user in ["nothing",
              "nothing special"]:
     print("Chatbot : That's great. It's good to do nothing and just relax.")

elif user in ["what's your name?",
           "what is your name?",
           "what's your name"]:
     print("Well..i don't have any specific name," \
     "i am a chatbot. You can call me whatever you want😊")
elif user in ["who made you?",
          "who designed you?"]:
     print("I am a chatbot designed by a 1st year Btech student - Avani Sharma, as her first mini project😊. ")
elif user in ["i am sad",
             "i am not feeling well"]:
     print("Umm...First take a deep breath and tell me why are you sad or not feeling well. I will try to help to make you happy😊")
     reason = input("You : ").lower().strip()
     if reason in ["i am feeling demotivated",
                   "motivate me"]:
          print("Ahh...it happens with every one at a time. " \
          "Take a deep breath, give yourself some time.." \
          "you can do it ")
elif user in ["what can you do?",
             "what tasks can you perform?",
             "what features do you have?"]:
     print("I am built for multiple tasks such as : " \
     "(1) I can talk to you " \
     "(2) perform Basic maths calculation" \
     "(3) Crack jokes" \
     "(4) Motivate you "
     "Just say - ")
     task = input("You : ").lower().strip()
     if task in ["(1)",
                 "1",
                 "first" ,
                 "first one"]:
          print("Hi, i am a chatbot model. It feels nice talking to you.")
     elif task in ["(2)" ,
                    "2" ,
                    "two",
                    "second one"]:
          print("Which operation do you want me to perform-")
          print("(+,-,*, /)")
          operation = input("You : ").lower().strip()             
       
          if operation == "+":
               print("Select number of values to add (2,3 or 4):")
               select = input("You : ").lower().strip()
               if select == "2":
                    print("Enter values to add-")
                    a = int(input("a = "))
                    b = int(input("B = "))
                    add = a + b
                    print("Answer = ", add)

               elif select == "3":
                    print("Enter values to add-")
                    x = int(input("a = "))
                    y = int(input("b = "))
                    z = int(input("c = "))
                    print("Answer = ", x+y+z)

               elif select == "4":
                    print("Enter values to add-")
                    p = int(input("a = "))
                    q = int(input("b = "))
                    r = int(input("c = "))
                    s = int(input("d = "))
                    print("Answer = ", p+q+r+s)

          elif operation == "-":
               print("Enter the values to subtract")
               a = int(input("a = "))
               b = int(input("b = "))
               print("Answer = ", a-b)

          elif operation == "*":
               print("Enter values to multiply-")
               a = int(input("a = "))
               b = int(input("b = "))
               print("Answer = ", a*b)

          elif operation == "/":
               print("Enter values to divide -")
               a = int(input("a = "))
               b = int(input("b = "))
               print("Answer = ", a/b)

          else: print("Chatbot : Sorry, i didn't get it.") 

     elif task in ["(3)",
                    "3" ,
                    "third",
                    "third one"]:
          jokes = [
    "Teacher: Why didn’t you study?\nMe: I was testing my luck.",
    "Teacher: Why are you talking in class?\nMe: I was explaining the topic… to myself.",
    "Teacher: You should be serious about your future.\nMe: I am… I’m just scared of it.",
    "Teacher: What were you doing all day?\nMe: Planning to study."
]
          print(random.choice(jokes))  

     elif task in ["(4)" ,
                   "4" ,
                   "fourth" ,
                   "fourth one"]:
          print("It happens with everyone at a stage. Take a deep breath, give yourself some time and restart." \
          "You can do this.")
     else: 
          print("Chatbot: Sorry i didn't get it.")

          

                    











# print("          Tell me if you want to - \n "
# "          (i) Hear a joke😂 \n "
# "          (ii) Motivate youself👍🏻\n " 
# "          (iii) Solve Basic Maths🥸\n " 
# "          (iv) Just talk😄 \n " 
# "           Just say-")






      
    # copy 1
#     print("---------------------Welcome To The ChatBox----------------------")
# user = input("You : ").lower().strip()

# if user in ["hy", "hey", "Hello", "Hi"] :
#     print("Chatbot : Hey!, How are you buddy?")
# else : 
#     print("Chatbot : Sorry, i didn't get it.")

# greet = input("You : ").lower().strip()
# if greet in ["i am fine, what about you",
#               "i am fine, how are you?" ,
#               "i am fine, you?" , 
#               "i am fine, and you?",
#               "i am fine how are you?" ]:
#        print("ChatBot : I am handsome buddy!, Hahaha...😄\n "
#        "         Tell me what's on your mind?")
# elif greet in ["i am fine",
#                "Fine"]:
#      print("ChatBot : That's great. So what's going on buddy? ")
# else :
#       "Sorry, i didn't get it.\n "

# ask = input("You : ").lower().strip()
# if ask in ["What's your name?",
#            "what is your name?",
#            " what's your name"]:
#      print("Well..i don't have any specific name," \
#      "i am a chatbot. You can call me what you want😊")
# elif ask in ["Who made you?",
#           "Who designed you?"]:
#      print("I am a chatbot designed by a 1st year Btech student - Avani Sharma, as her first mini project ")
# elif ask in ["I am sad",
#              "I am not feeling well"]:
#      print("Umm...First take a deep breathe and tell me why are sad or not feeling well. I will try to help to to make you happy")
#      reason = input("You : ")
#      if reason == "I am feeling demotivated" or "motivate me":
#           print("Ahh...it happens with every one at a time. " \
#           "Take a deep breathe, give youself some time.." \
#           "you can do it ")
# elif ask in ["what can you do?",
#              "What tasks can you perform?",
#              "What features do you have?"]:
#      print("I am built for multiple tasks such as : " \
#      "(1) I can talk to you " \
#      "(2) perform Basic maths calculation" \
#      "(3) Crack jokes" \
#      "(4) Motivate you "
#      "Just say - ")
#      task = input("You : ").lower().strip()
#      if task in ["(1)",
#                  "1",
#                  "first" ,
#                  " First one"]:
#           print("Hi, i am a chatbot model. It feels nice talking to you.")
#      elif task in ["(2)" ,
#                     "2" ,
#                     "Two",
#                     "Second one"]:
#           print("Which operation do you want me to perform-" \
#           "+ or - or * or /")
#           operation = input("You : ").lower().strip()
#           if operation == "+":
#                print("Select Number of values to add-" \
#                "2" \
#                "3" \
#                "4")
#                select = input("You : ").lower().strip()
#                if select == "1":
#                     print("Enter values to add-")
#                     a = input("a = ")
#                     b = input("B = ")
#                     add = a + b
#                     print("Answer = ", add)

#                elif select == "3":
#                     print("Enter values to add-")
#                     x = input("a = ")
#                     y = input("b = ")
#                     z = input("c = ")
#                     print("Answer = ", x+y+z)

#                elif select == "4":
#                     print("Enter values to add-")
#                     p = input("a = ")
#                     q = input("b = ")
#                     r = input("c = ")
#                     s = input("d = ")
#                     print("Answer = ", p+q+r+s)

#           elif operation == "-":
#                print("Enter the values to subrtact")
#                a = input("a = ")
#                b = input("b = ")
#                print("Answer = ", a-b)

#           elif operation == "*":
#                print("Enter values to multiply-")
#                a = input("a = ")
#                b = input("b = ")
#                print("Answer = ", a*b)

#           elif operation == "/":
#                print("Enter values to divide -")
#                a = input("a = ")
#                b = input("b = ")
#                print("Answer = ", a/b)

#      elif task in ["(3)",
#                     "3" ,
#                     "third",
#                     "third one"]:
#           print("Joke")  

#      elif task in ["(4)" ,
#                    "4" ,
#                    "fourth" ,
#                    "fourth one"]:
#           print("It happend with everyone at a stage. Take a deep breathe, give yourself some time and restart." \
#           "You can do this.")
