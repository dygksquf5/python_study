# This is a porject for understand how brute force flow works not for hack. So, DO NOT FOLLOW FOR PERSONAL REASON. THIS IS JUST FOR STUDY. 



# start main.py for Brute Force

<img width="1066" alt="Screenshot 2020-11-27 at 1 58 00 PM" src="https://user-images.githubusercontent.com/66229916/100412957-6c5c3f80-30b9-11eb-93ee-fcd121ce0744.png">


<img width="718" alt="Screenshot 2020-11-27 at 2 00 54 PM" src="https://user-images.githubusercontent.com/66229916/100412964-6fefc680-30b9-11eb-932a-8af9a27eec86.png">



# This is command for MAC ( find SSID ) 

    bash_command = "/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -s"
    subprocess.call(bash_command.split())
  
# Also you need a dict for efficient Brute_Force ( in this case, I already Know the password, thus I made .txt file on my own for Brute Force

  with(open("expect_password.txt", "w", encoding="utf8")) as text:
    a = "twosome"
    b = range(0,1000)
    for i in b:
        text.write("{0}{1} \n".format(a, i))

 
 # Finally you could find a profer password
 
 <img width="404" alt="Screenshot 2020-11-27 at 2 03 51 PM" src="https://user-images.githubusercontent.com/66229916/100412971-72eab700-30b9-11eb-9b85-c234f3bb059e.png">
