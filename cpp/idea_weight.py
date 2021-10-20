class RecommendedWeight:
    height = 0
    age = 0
    def __init__(self, height, age):
        self.height = height
        self.age = age
        
    def recommendWeight(self):
        return (self.height - 100 + self.age % 10) * 0.90
        
if __name__ == '__main__':
    height = float(input("Enter your height : "))
    age = float(input('Enter your age : '))
    rw = RecommendedWeight(height, age)
    print ("Your Recommended Weight : " + str(rw.recommendWeight()))