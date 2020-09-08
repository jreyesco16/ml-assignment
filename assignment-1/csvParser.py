# this file is for parser the winequality-white.csv file into winequality-white.csv 
# this way we can read with pandas by replace ';' with ','

def main():
    fileWrite = open('patients.csv', 'w')
    
    A1=[1,1,1,1,0,0,1,0,1,1,0,0,0,1,0,1,0,1,0,1,1, 0, 0,1,0,1,1,0,1,1,0] # healthy patients
    A2=[.70,.80,.65,.50,.30,.40,.60,.20,.70,.75,.40,.30,.50,.75,.45,.60,.30,.40,.50,.60,.90,.20,.15,.20,.70,.50,.60,.25,.85,.95,.15] #propability of patient health
    A3=[23,23,24,40,50,60,79,30,85,45,9,40,78,32,41,86,93,28,36,47,20,38,38,40,60, 39, 28, 49,50, 69, 78] # age of patient
    count = 0
    for i in range(0,len(A1)):
        if(count == 0):
            string = "\"prob of health\";\"age\";\"sick\"\n"
            fileWrite.write(string)
            count = 1
        else:
            string = str(A2[i])+";"+str(A3[i])+";"+str(A1[i])+"\n"
            fileWrite.write(string)
    

if __name__=="__main__":
    main()