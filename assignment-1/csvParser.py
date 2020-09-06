# this file is for parser the winequality-white.csv file into winequality-white.csv 
# this way we can read with pandas by replace ';' with ','

def main():
    fileRead = open('winequality-white.csv', 'r')
    lines = fileRead.readlines()
    fileRead.close()

    fileWrite = open('winequality-whiteProper.csv', 'w')


    for line in lines:
        tokens = line.split(';')
        count = 0
        for token in tokens:
            if(count == 0):
                fileWrite.write(token)
                count = 1
            else:
                fileWrite.write(','+token)
    

if __name__=="__main__":
    main()