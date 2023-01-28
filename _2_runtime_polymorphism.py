#runtime polymorphism-overriding
#overriding can only can be achieved in inhertitance
#if parent class method implemenation is not according to what you want then
#you can override it and write your own implementation in it
class dabba_tv:
    def color(self):
        print("B/W")
    def video(self):
        print("480p")
class flat_tv(dabba_tv):
    def additional_feature(self):
        print("smart tv")
    def color(self):       #overridden method
        print("colored Tv")
obj=flat_tv()
obj.color()

 