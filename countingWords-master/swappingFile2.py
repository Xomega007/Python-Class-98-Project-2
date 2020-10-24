def swapFileData():
    file1 = input("enter files name:- ")
    file2 = input("enter files name:- ")


    with open(file1, 'r') as a:
    data = a.read()

	with open(file2, 'r') as b:
    data = b.read()

    with open(file1, 'w') as a:
    a.write(data)

    with open(file2, 'w') as b:
    b.write(data)

swapFileData()