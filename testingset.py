Ea = 57.0
Eb = 64.0
Ec = 85.0
Ed = 90.0

Pa = 61.0
Pb = 68.0
Pc = 81.0
Pd = 84.0

emosi = [58,68,64,57,77,98,91,50,95,27]
provo = [63,70,66,77,55,64,59,95,55,79]

for g in range(0, 10):
    #Input nilai Emosi dan Provokasi
    m = emosi[g]
    n = provo[g]

    #FUZZIFICATION
    #FK Emosi
    Elow = 0.0
    Enorm = 0.0
    Ehigh = 0.0
    if (m >= 0 and m <= Ea):
        Elow = 1
    elif (m > Ea and m < Eb):
        Elow = (-(m - Eb)) / (Eb - Ea)
        Enorm = (m - Ea) / (Eb - Ea)
    elif (m >= Eb and m <= Ec):
        Enorm = 1
    elif (m > Ec and m < Ed):
        Enorm = (-(m - Ed)) / (Ed - Ec)
        Ehigh = (m - Ec) / (Ed - Ec)
    elif (m >= Ed and m <= 100):
        Ehigh = 1

    #FK Provokasi
    Plow = 0.0
    Pnorm = 0.0
    Phigh = 0.0
    if (n >= 0 and n <= Pa):
        Plow = 1
    elif (n > Pa and n < Pb):
        Plow = (-(n - Pb)) / (Pb - Pa)
        Pnorm = (n - Pa) / (Pb - Pa)
    elif (n >= Pb and n <= Pc):
        Pnorm = 1
    elif (n > Pc and n < Pd):
        Pnorm = (-(n - Pd)) / (Pd - Pc)
        Phigh = (n - Pc) / (Pd - Pc)
    elif (n >= Pd and n <= 100):
        Phigh = 1

    #INFERENSI
    tidak = 0.0
    ya = 0.0
    if (Elow == 1) :
        if (Plow == 1) :
            tidak = 1
        elif (Plow != 0 and Pnorm != 0) :
            tidak = max(min(Elow, Plow),min(Elow, Pnorm))
        elif (Pnorm == 1) :
            tidak = 1
        elif (Pnorm != 0 and Phigh != 0) :
            tidak = min(Elow, Pnorm)
            ya = min(Elow, Phigh)
        elif (Phigh == 1) :
            ya = 1
    elif (Elow != 0 and Enorm !=0) :
        if (Plow == 1) :
            tidak = max(min(Elow, Plow),min(Enorm, Plow))
        elif (Plow != 0 and Pnorm != 0) :
            tidak = max(min(Elow,Plow),min(Elow,Pnorm),min(Enorm,Plow))
            ya = min(Enorm,Pnorm)
        elif (Pnorm == 1) :
            tidak = min(Elow,Pnorm)
            ya = min(Enorm,Pnorm)
        elif (Pnorm != 0 and Phigh != 0) :
            tidak = min(Elow,Pnorm)
            ya = max(min(Elow,Phigh),min(Enorm,Pnorm),min(Enorm,Phigh))
        elif (Phigh == 1) :
            ya = max(min(Elow,Phigh),min(Enorm,Phigh))
    elif (Enorm == 1) :
        if (Plow == 1) :
            tidak = 1
        elif (Plow != 0 and Pnorm != 0) :
            tidak = min(Enorm, Plow)
            ya = min(Enorm, Pnorm)
        elif (Pnorm == 1) :
            ya = 1
        elif (Pnorm != 0 and Phigh != 0) :
            ya = max(min(Enorm,Pnorm),min(Enorm,Phigh))
        elif (Phigh == 1) :
            ya = 1
    elif (Enorm != 0 and Ehigh != 0) :
        if (Plow == 1) :
            tidak = max(min(Enorm, Plow),min(Ehigh, Plow))
        elif (Plow != 0 and Pnorm != 0) :
            tidak = max(min(Enorm,Plow),min(Ehigh,Plow))
            ya = max(min(Enorm,Pnorm),min(Ehigh,Pnorm))
        elif (Pnorm == 1) :
            ya = max(min(Enorm,Pnorm),min(Ehigh,Pnorm))
        elif (Pnorm != 0 and Phigh != 0) :
            ya = max(min(Enorm,Pnorm),min(Enorm,Phigh),min(Ehigh,Pnorm),min(Ehigh,Phigh))
        elif (Phigh == 1) :
            ya = max(min(Enorm,Phigh),min(Ehigh,Phigh))
    elif (Ehigh == 1) :
        if (Plow == 1) :
            tidak = 1
        elif (Plow != 0 and Pnorm != 0) :
            tidak = min(Ehigh, Plow)
            ya = min(Ehigh, Pnorm)
        elif (Pnorm == 1) :
            ya = 1
        elif (Pnorm != 0 and Phigh != 0) :
            ya = max(min(Ehigh,Pnorm),min(Ehigh,Phigh))
        elif (Phigh == 1) :
            ya = 1

    #DEFUZZIFICATION
    y = 0.0
    nTidak = 40.0
    nYa = 60.0
    if (tidak == 0) :
        y = (ya * nYa)/ya
    elif (ya == 0) :
        y = (tidak * nTidak) / tidak
    else :
        y = ((ya * nYa)+(tidak * nTidak)) / (ya+tidak)

    if (y <= 50) :
        print 'B'+str(g+1)+' '+str(emosi[g])+' '+str(provo[g])+' Tidak'
    else :
        print 'B'+str(g+1)+' '+str(emosi[g])+' '+str(provo[g])+' Ya'
