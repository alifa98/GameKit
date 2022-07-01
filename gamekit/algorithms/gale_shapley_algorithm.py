
# if women wi prefer man mj function return true
# this woman = w
# current engamement = m1
# new request = m
# if w prefers m over m1
def wPrefer(prefer, w, m, m1, Men):
    """

    if women wi prefer man mj function return true
    
    this woman = w
    current engamement = m1
    new request = m
    if w prefers m over m1

    wPrefer return True if this match was stable
    and return false if it was unstable

    """
    for i in range(Men):
        
        
        # preference of w:  ... m1, ..., m, ...
        if (prefer[w][i] == m1):
            return True
        # preference of w:  ... m, ..., m1, ...
        if (prefer[w][i] == m):
            return False



def stableMarriage(Men, Women, prefer):
    
    """
    
    input 
    number of men
    number of women
    prefer of people
    
    return woman's list
    
    """
    
    # allocated man to woman[i] store here
    wPartner = [-1 for i in range(Women)]
    
    # single man notificed by false value
    mFree = [False for i in range(Men)]
    
    # we work on men-proposing algorithm
    # so start with man-count
    freeCount = Men
    
    while (freeCount > 0):
        
        # pick up first false man
        # this = first single man
        this = 0
        while (this < Men):
            if (mFree[this] == False):
                break
            this += 1
        
        
        # request each woman of his preference
        request = 0
        while request < Women and mFree[this] == False:
            w = prefer[this][request]
        
            # if requested woman is free, so you can engage
            if (wPartner[w - Men] == -1):
                # matching better than unmatching
                wPartner[w - Men] = this
                mFree[this] = True
                freeCount -= 1
            # if requested woman engage, it's depend:
            else:
                
                # find partner of w
                m1 = wPartner[w - Men]
                
                # if w prefer 'this' over her current engagement m1:
                # break up with m1 :(
                # engage with this 
                if (wPrefer(prefer, w, this, m1, Men) == False):
                    wPartner[w - Men] = this
                    mFree[this] = True
                    mFree[m1] = False
                    
                # else: woman not prefere this to her current engaement
                # nothing happen
                else:
                    pass
                

                    
            request += 1
             
    return wPartner