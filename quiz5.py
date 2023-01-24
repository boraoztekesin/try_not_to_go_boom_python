import sys

try:
    f = open(sys.argv[1], "r", encoding="utf-8")
    f2 = open(sys.argv[2], "r", encoding="utf_8")
    counter = 0
    c=[]
    d=[]
    for x in f.readlines():
        c.append(x.strip("\n"))
    for x in f2.readlines():
        d.append(x.strip("\n"))
    for aa in c:
        a1 = aa.split()
        print("------------")
        try:

            liste = []
            comp_list1 = d[counter]
            comp_list2 = comp_list1.split()
            a = []
            comp_list = []
            for i in a1:
                a.append(int(float(i)))
            for i in comp_list2:
                comp_list.append(int(i))
            div = a[0]
            nondiv = a[1]
            fr0m = a[2]
            to = a[3]
            if len(a) < 4 or len(a) > 4:
                raise IndexError
            for i in range(fr0m, to):
                if i % div == 0 and i % nondiv != 0:
                    liste.append(i)
            print("My results: ", liste)
            print("Results to compare: ",comp_list)
            assert liste.__eq__(comp_list)
        except ValueError:
            print("ValueError: only numeric input is accepted.")
            print("Given input ",a)
        except IndexError:
            print("IndexError: number of operands less than expected.")
            print("Given input ",a)
        except ZeroDivisionError:
            print("You can't divide by 0")
            print("Given input ",a)
        except AssertionError:
            print("results don't match.")
        except Exception as error:
            print("kaBOOM: run for your life!")
        else:
            print("Goool!!!")
        finally:
            counter += 1


except IndexError:
    print("IndexError : number of input files less than expected.")
except IOError:
    print("IOError : cannot open nonexistentfile.txt")
finally:
    print("- Game over -")
