from generator import make_maze



def main():

    matrix = list()


    mz = make_maze()
    f = open('labirinto.txt','w')
    f.write(mz)
    f.close()

    matrix.append(f.readlines())

    print(matrix)


if __name__ == "__main__":
    main()