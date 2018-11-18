def com_apart(apart):
    floor_person={}
    for key, floor in enumerate(apart):
        total=0
        for house in floor:
            total+=house
        floor_person[str(key+1)+"층"]=total
    return floor_person

apartment=[[2,3,2],[1,2,1],[3,2,2]]
print(com_apart(apartment))
