def typ_list(MyList):
    strings=[]
    integer=[]
    flo=[]
    
    for i in range(len(MyList)):
        if type(MyList[i])==str:
            strings.append(MyList[i])
        if type(MyList[i])==int:
            integer.append(MyList[i])

            
        if type(MyList[i])==float:
            flo.append(MyList[i])
                 

    return strings,integer,flo


strings,integer,flo=typ_list([10,'abc',3,'$',5.87])
print("Strings :",strings)
print("Integers :",integer)
print("Float :",flo)
        

