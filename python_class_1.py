#question no. 1 (extracting the @ symbol and the domain from an email)
class EmailEvaluator:
    def __init__(self,email):
        self.email = email
    def evaluate(self):
        if "@" in self.email:
            print("@ find")
        else:
            print("@ not find")
    def domain(self):
        email = self.email
        if "@" in self.email:
            split_string = email.split("@")
            domainName = split_string[1]
            print(domainName)
email = input("enter your email : ")
EmailEvaluator(email).evaluate()
EmailEvaluator(email).domain()
#question no. 2 (converting the csv file into JSON file)
