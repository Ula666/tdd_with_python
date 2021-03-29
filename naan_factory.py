class NaanFactory:

    def make_dough(self, item1, item2):
        if item1 == "water" and item2 == "flour":
            return "dough"


    def bake_dough(self, item1):
        if item1 == "dough":
            return "naan"
