import random

class Main:
    @classmethod
    def generateVariables(self, amountOfVars:int , amountOfDigits: int,listofXvars=None):
        variableList = []
        resultOfRow: int = 0
        for i in range(amountOfVars):
            variableList.append(((-1)**(round(random.random()+1)) * random.random() * (10 ** (amountOfDigits))).__floor__())
        if listofXvars is not None:
            for i in range(len(variableList)):
                resultOfRow += variableList[i] * listofXvars[i]
            variableList.append(resultOfRow)
        return variableList

    
    @classmethod
    def makeMatrics(self,amountOfVars:int,amountOfDigits:int):
        rows = [self.generateVariables(amountOfVars, amountOfDigits)]
        for i in range(amountOfVars):
            rows.append(self.generateVariables(amountOfVars, amountOfDigits, rows[0]))
        return rows


    @classmethod
    def renderMatrics(self,amountOfDigits:int, amountOfVars:int):
        rows = self.makeMatrics(amountOfVars, amountOfDigits)
        XValues = rows[0]
        rows.pop(0)
        matricsString = ""
        for i in rows:
            matricsString += "\n        "
            for e in i:
                if i.index(e) is (amountOfVars):
                    matricsString += "|"
                matricsString += " " + str(e) + " "
        print(matricsString)
        print(self.listToMatrics(rows))
        return XValues


    @classmethod
    def start(self):
        result = self.renderMatrics(int(input("How many Digit should each Variable have?\n")), int(input("How many Variables should the Matrics have? \n\n\n")))
        input("")
        print(result) 


    @classmethod
    def listToMatrics(self,matricList) -> str:
        s_latexMatrics: str = "{"
        for i in matricList:
            s_latexMatrics += "{"
            for e in i:
                s_latexMatrics += str(e)
                if i.index(e) != (len(i)-1):
                    s_latexMatrics += ","
            s_latexMatrics += "}" 
            if matricList.index(i) is not (len(matricList)-1):
                s_latexMatrics += ","

        return (s_latexMatrics + "}")





if __name__ == "__main__":
    Main.start()
