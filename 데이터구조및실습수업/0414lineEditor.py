class ArrayList():
    pass

class myLineEditor:
    def __init__(self):
        self.list = ArrayList()
    def input(self):
        pos = int(input("입력행 번호 :"))
        string = input("입력행 내용 :")
        self.list.insert(pos, string)
    def delete(self):
        pos = int(input("삭제행 번호 :"))
        self.list.delete(pos)
    def replace(self):
        pos = int(input("변경행 번호 :"))
        string = input("변경행 내용 :")
        self.list.replace(pos, string)
    def printAll(self):
        print('Line Editor')
        for i in range(self.list.size()):
            print(f"{i}", end=" ")
            print(self.list.getEntry(line))
        print()
    def readMode(self):
        filename = 'test.txt'
        infile = open(filename, "r")
        lines = infile.readlines()
        for line in lines:
            self.list.insert(self.list.size(), self.list.rstrp('\n'))
        infile.close()
    def writeMode(self):
        filename = 'test.txt'
        outfile = open(filename, 'w')
        for i in range(self.list.size()):
            outfile.write(self.list.getEntry(i)+'\n')
        outfile.close()

myLE = myLineEditor()
while True:
    command = input()
    if command == 'i':
        myLE.input()
    elif command == 'd':
        myLE.delete()
    elif command == 'r':
        myLE.replace()
    elif command == 'q':
        break
    elif command == 'p':
        myLE.printAll()
    elif command == 'l':
        myLE.readMode()
    elif command == 's':
        myLE.writeMode()
