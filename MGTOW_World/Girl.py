import time
from Guy import Guy
#from Thot import Thot
from Alpha import Alpha
from Beta import Beta
from Government import Government

Girl_breast_cup_dict = {"":0,"A":20,"B":40,"C":60,"D":80,"DD":100,"E":60,"F":30}

Girl_age_dict = {18:100,19:100,20:95,21:95,22:90,23:90,24:85,25:85,26:80,27:80,28:75,29:70,30:60,31:50,32:45,33:40,34:35,35:30,36:25,37:20,38:15,39:10,40:1,41:1,42:1}

Girl_work_dict = {"allimony":1200,
                  "secretary":1800,
                  "administrative_assistant":1700,
                  "government_employee":2000,
                  "psychologist":2500,
                  "psychiatrist":3000,
                  "lawyer":4000}

Girl_worthless_degrees = {"Bachelor Gender Studies":80000,
                          "Bachelor Psychology":50000,
                          "Bachelor Communication":30000,
                          "Bachelor of Law Enforcement Studies":20000,
                          "Bachelor of International Studies":50000}

Girl_ethnicities = ["Caucasian",
                    "African",
                    "Asian",
                    "Arabian",
                    "Europian",
                    "Latina"]

class Girl:

    depth = 0
    wealth = 0
    bank_account = 0

    def __init__(self,
                 name,
                 age,virgin,
                 boyfriend_count,
                 breast_cup,
                 ethnicity,
                 weight,height,
                 income,
                 work=None,
                 diploma=None):

        if diploma == None:
            self.diploma = []
        else:
            self.diploma = []
            # Check if diploma_attribute is a list
            if isinstance(diploma,(list,)):
                for x in diploma:
                   if x in Girl_worthless_degrees:
                       self.diploma.append(x)
            # If not list, append directly to list
            elif diploma in Girl_worthless_degrees:
                self.diploma.append(diploma)
            else:
                print("NOTICE: Diploma attribute wrong format in constructor, setting to empty list")
        if work == None:
            self.work = []
            #self.work += "Allimony"
        #self.depth = "{}{}".format(len(self.diploma) * Girl_worthless_degrees.get(self.diploma),"$")
        self.depth = "{}{}".format(int(Girl.depth),"$")
        if self.diploma != []:
            depth = 0
            for d in self.diploma:
                depth += Girl_worthless_degrees.get(d)
            self.depth = "{}{}".format(int(depth),"$")
        self.income = income
        self.name = str(name)
        self.age = int(age)
        self.cock_mileage = int(boyfriend_count) * self.age
        self.virgin = bool(virgin)
        self.boyfriend_count = int(boyfriend_count)
        if breast_cup in Girl_breast_cup_dict:
            self.breast_cup = str(breast_cup)
        else:
            self.breast_cup = ""
        self.ethnicity = str(ethnicity)
        self.weight = "{}{}".format(int(weight),"KG")
        self.height = "{} {}".format(int(height),"Centimeters")
        #self.bank_account = self.work
        self.married = bool(0)
        self.hotness = "{}{}".format((Girl_breast_cup_dict[self.breast_cup] + Girl_age_dict[self.age]) / 2,"%")
        if self.cock_mileage == 0:
            self.SMV = self.hotness
        else:
            self.SMV = ((Girl_breast_cup_dict[self.breast_cup] + Girl_age_dict[self.age]) / 2) - ((self.cock_mileage * self.cock_mileage) / (self.cock_mileage * 100))
            if self.SMV <= 0:
                self.SMV = 0

    #def transmit_std(self):

    # functions like: leach, divorce_rape, get_useless_diploma, bare_child, false_allegation, abortion, work_out, monkey_branch
    def fuck(self,alpha,amount: int):
        if self.cock_mileage > 1000:
            print("Wow you dirty whore, if you keep this pace, you will reach maximum thothery and will need to freeze your eggs!""\n")
        self.cock_mileage += amount
        self.virgin = bool(0)
        time.sleep(2)
        print("Ah yes... you fucked " + alpha.name , str(amount) + " times, you dirty slut!")
        time.sleep(1)
        print("Congratulations " + self.name + "," + " your cock_milage has inceased with " + str(amount) + ", and is now at " + str(self.cock_mileage) + "!""")

    def fuck_chad(self,alpha,amount: int):
        #alphas = ["Tyrone", "Chad", "Badboy mo"]
        if isinstance(alpha, Alpha):
            self.fuck(alpha,amount)
            # if self.cock_mileage > 1000:
            #     print("Wow you dirty whore, if you keep this pace, you will reach maximum thothery and will need to freeze your eggs!""\n")
            # self.cock_mileage += amount
            # self.virgin = bool(0)
            # time.sleep(2)
            # print("Ah yes... you fucked " + alpha.name , str(amount) + " times, you dirty slut!")
            # time.sleep(1)
            # print("Congratulations " + self.name + "," + " your cock_milage has inceased with " + str(amount) + ", and is now at " + str(self.cock_mileage) + "!""")
        elif isinstance(alpha, Girl):
            print(self.name + " does not fuck with girls!" + "\n" + "Only Alpha guys who can shower me with money and cum please!""\n")
#        elif isinstance(alpha, Kech):
#            print(self.name + " does not fuck with THOTS!" + "\n" + "Only Alpha guys who can shower me with money and cum please!")
        elif isinstance(alpha, Beta):
            if self.age >= 35:
                print("Alright, you can have a piece of this ass. ""\n" "I'm a swinger and have hit the wall anyways!")
                time.sleep(1)
                self.fuck(alpha,amount)
                # if self.cock_mileage > 1000:
                #     print("Wow you dirty whore, if you keep this pace, you will reach maximum thothery and will need to freeze your eggs!""\n")
                #     time.sleep(1)
                # self.cock_mileage += amount
                # self.virgin = bool(0)
                # time.sleep(2)
                # print("Ah yes... you fucked " + alpha.name , str(amount) + " times, you dirty slut!")
                # time.sleep(1)
                # print("Congratulations " + self.name + "," + " your cock_milage has inceased with " + str(amount) + ", and is now at " + str(self.cock_mileage) + "!")
            else:
                print("Are you kidding me? " + self.name + " does not fuck with betas, sorry!" "\n" + "Maybe, just maybe, I will come to " + alpha.name + " later to marry him when I'm done having fun :)!""\n")

    # def leach(self,Guy):

    # def set_income
    # def set_diplomas
    # def set_bank_account
