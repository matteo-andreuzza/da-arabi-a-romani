print("da arabi a romani - 1.0.2")
while True:
    def processo():
        def unita(n):
            if n == 1:
                return("I")
            elif  n == 0:
                return("")
            elif n == 2:
                return("II")
            elif n == 3:
                return("III")
            elif n == 4:
                return("IV")
            elif n == 5:
                return("V")
            elif n == 6:
                return("VI")
            elif n == 7:
                return("VII")
            elif n == 8:
                return("VIII")
            elif n == 9:
                return("IX")
        def decine(n):
            if n == 1:
                return("X")
            elif n == 0:
                return("")
            elif n == 2:
                return("XX")
            elif n == 3:
                return("XXX")
            elif n == 4:
                return("XL")
            elif n == 5:
                return("L")
            elif n == 6:
                return("LX")
            elif n == 7:
                return("LXX")
            elif n == 8:
                return("LXXX")
            elif n == 9:
                return("XC")
        def centinaia(n):
            if n == 1:
                return("C")
            elif n == 0:
                return("")
            elif n == 2:
                return("CC")
            elif n == 3:
                return("CCC")
            elif n == 4:
                return("CD")
            elif n == 5:
                return("D")
            elif n == 6:
                return("DC")
            elif n == 7:
                return("DCC")
            elif n == 8:
                return("DCCC")
            elif n == 9:
                return("CM")
        def migliaia(n):
            if n == 1:
                return("M")
            elif n == 0:
                return("")
            elif n == 2:
                return("MM")
            elif n == 3:
                return("MMM")
        if arabo < 4000:
            num = list(str(arabo))
            al = len(num)
            if al == 4:   
                u = int(num[3])
                d = int(num[2])
                c = int(num[1])
                m = int(num[0])
                #if u > 0:
                ciao = unita(u)
                #if d > 0:
                ciaa = decine(d)
                #if c > 0:
                ciae = centinaia(c)
                #if m > 0:ù
                ciai = migliaia(m)
                print(str(ciai) + str(ciae) + str(ciaa) + str(ciao))
            elif al == 3:
                u = int(num[2])
                d = int(num[1])
                c = int(num[0])
                ciao = unita(u)
                #if d > 0:
                ciaa = decine(d)
                #if c > 0:
                ciae = centinaia(c)
                #if m > 0:ù
                print(str(ciae) + str(ciaa) + str(ciao))
            elif al == 2:
                u = int(num[1])
                d = int(num[0])
                ciao = unita(u)
                #if d > 0:
                ciaa = decine(d)
                #if c > 0:
                print(str(ciaa) + str(ciao))
            elif al == 1:
                u = int(num[0])
                ciao = unita(u)
                print(str(ciao))
        else:
            print("i numeri romani possono essere generati correttamente solo fino a 3999, in una prossima versione forse riusciremo ad andare oltre")
    ins = input("inserisci numero arabo   ")
    rei = list('qazxswedcvfrtgbnhyujnmkiolp')
    rai = ins in rei
    if rai == False:
        arabo = int(ins)
        processo()
    else:
        print("inserisci un numero")