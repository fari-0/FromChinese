def to_chinese_numeral(n):
    numerals = {
        10000:"万",
        1000:"千",
        100:"百",
        10:"十",   
        9:"九",
        8:"八",  
        7:"七",
        6:"六",
        5:"五",
        4:"四",
        3:"三",
        2:"二",
        1:"一",
    }
    sayilar=list(numerals)
    indexi=0
    n2=n
    cevir=[]
    kontrol=0
    sifir=0
    decikont=0
    if type(n)==float:
        decimal=str(n)[str(n).index("."):]
        decimal=decimal.replace(".","")
        n=str(n)[:str(n).index(".")]
        n=int(n)
        decikont+=1
    if n == 0:
        cevir.append("零")
        kontrol+=1
    if n<0:
        cevir.append("负")
        n=((n-n)-n)
    if n in range(10,20):
        cevir.append(numerals[10])
        n-=10
        if n!=0:
            cevir.append(numerals[n])
        kontrol+=1
    if kontrol==0:
        for sayi,cin in numerals.items():
            while n>=sayi:
                if n/sayi>=1 and n>9:
                    if sifir>sayilar[sayilar.index(sayi)-1]:
                        cevir.append("零")
                    cevir.append(numerals[(int(n/sayi))])
                    cevir.append(numerals[sayi])
                    n-=(int(n/sayi))*sayi
                    sifir=sayi
                elif n<=9:
                    if sifir>=11:
                        cevir.append("零")
                    cevir.append(numerals[sayi])
                    n-=sayi
                    sifir=sayi
                indexi+=1
            if n==0:break
        if cevir[0]=="零" and n2!=0:
            cevir.remove(cevir[0]) 
    if decikont==1:
        cevir.append("点")
        for d in str(decimal):
            if int(d)==0:
                cevir.append("零")
            else:cevir.append(numerals[int(d)])    
    print(n2)
    print("".join(cevir))
    
to_chinese_numeral(7418)