from Guy import Guy

class Beta(Guy):

    # attributen van Guy inherriten, maar ook Beta attributen toevoegen
    def __init__(self,name,age,virgin,ethnicity,weight,height,ripped,girlfriend_count,income,work=None,diploma=None):
        super().__init__(name,age,virgin,ethnicity,weight,height,ripped,girlfriend_count,income,work=None,diploma=None)
