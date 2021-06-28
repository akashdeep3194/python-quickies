def gender(n,k):
    if n==1:
        return "M"
    if gender(n-1 ,int((k+1)/2)) == "M":
        if k%2 == 0:
            return "F"
        else:
            return "M"
    else:
        if k%2 == 0:
            return "M"
        else:
            return "F"
