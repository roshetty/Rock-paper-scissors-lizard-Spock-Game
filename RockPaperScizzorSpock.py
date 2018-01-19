Run (Accesskey R)
  
Save (Accesskey S)
  
Download
  
Fresh URL
  
Open LocalChoose File
  
Reset (Accesskey X)
 CodeSkulptor 
Docs
  
Demos
  
Viz Mode
 
1
# Rock-paper-scissors-lizard-Spock Game 
2
import random
3
?
4
?
5
#Converts name to numbers from (0-4)
6
def name_to_number(name):
7
    if name == "rock":
8
        number = 0
9
    elif name == "Spock":
10
        number = 1
11
    elif name == "paper":
12
        number = 2
13
    elif name == "lizard":
14
        number = 3
15
    elif name == "scissors":
16
        number = 4
17
    else:
18
        print "Wrong Choice"
19
    
20
    
21
    return number
22
?
23
#Converts numbers to name
24
def number_to_name(number):
25
    if number == 0:
26
        name ="rock"
27
    elif number == 1:
28
        name = "Spock"
29
    elif number == 2:
30
        name = "paper"
31
    elif number == 3:
32
        name = "lizard"
33
    else:
34
        name = "scissors"
35
    return name
36
    
37
    
38
#Computes the outcome
39
def rpsls(player_choice):
40
    print "Player chooses " , player_choice
41
    a = name_to_number(player_choice)
42
    b = random.randint(0,4)                  
43
    c = number_to_name(b)
44
    print "Computer chooses" , c
45
    d = (a - b)% 5
46
    
47
    if  d ==0: 
48
        print "Player and computer tie!\n\n"
49
    elif d == 1:
50
        print "Player wins!\n\n"
51
    elif d == 2:
52
        print "Player wins!\n\n"
53
    elif d == 3:
54
        print "Computer wins!\n\n"
55
    elif d == 4:
56
        print "Computer wins!\n\n"
57
    else:
58
        print"Something went wrong please check your code"
59
   
60
      
61
            
62
    
63
    
64
rpsls("rock")
65
rpsls("Spock")
66
rpsls("paper")

CodeSkulptor was built by Scott Rixner and is based upon CodeMirror and Skulpt.