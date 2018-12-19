Guy_age_dict = {18:10,19:10,20:15,21:20,22:25,23:30,24:35,25:35,26:40,27:40,28:45,29:50,30:60,31:70,32:80,33:90,34:90,35:100,36:100,37:100,38:100,39:100,40:100}

Guy_worthless_work_dict = {"allimony":1200,
                           "secretary":1800,
                           "administrative_assistant":1700,
                           "government_employee":2000}

Guy_worth_work_dict = {"lawyer":4000,
                       "Software Engineer":6000,
                       "Network Engineer":6000,
                       "Architect":8000,
                       "Medical Doctor":10000,
                       "Entrepeneur":20000}

Guy_worthless_degrees = {"Bachelor Gender Studies":80000,
                         "Bachelor Psychology":50000,
                         "Bachelor Communication":30000,
                         "Bachelor of Law Enforcement Studies":20000,
                         "Bachelor of International Studies":50000,
                         "Bachelor of Economics":30000}

Guy_worth_degrees = {"Bachelor Computer Science and Engineering":40000,
                     "Bachelor of Law":30000,
                     "Master of Law":50000,
                     "Bachelor of Architect":40000,
                     "Bachelor of Medicine":50000,
                     "Master of Medicine":70000}

Guy_ethnicities = ["Caucasian",
                    "African",
                    "Asian",
                    "Arabian",
                    "Europian",
                    "Latina"]

class Guy:
    def __init__(self,name,age,virgin,ethnicity,weight,height,ripped,girlfriend_count,income,work=None,diploma=None):
        if diploma == None:
            self.diploma = []
        else:
            self.diploma = []
            self.diploma += diploma
        if work == None:
            self.work = []
        self.depth = "{}{}".format(len(self.diploma) * 30000,"$")
        self.income = income
        self.name = str(name)
        self.age = int(age)
        self.ripped = bool(ripped)
        self.virgin = bool(virgin)
        self.girlfriend_count = int(girlfriend_count)
        self.ethnicity = str(ethnicity)
        self.weight = "{}{}".format(int(weight),"KG")
        self.height = "{} {}".format(int(height),"Centimeters")
    #     #self.bank_account = self.work
    #     self.married = bool(0)
    #     self.hotness = "{}{}".format((breast_cup_dict[self.breast_cup] + age_dict[self.age]) / 2,"%")
    # Attributen die elke man heeft.

    # instance specifieke attributen

    # functies, zoals trouwen, divorcen, werk een dag, uitgaan, hoer_neuken,
