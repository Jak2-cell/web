from pprint import pprint

solubility_table = open("solubility.csv")
s_text = solubility_table.read()
#print(s_text)
insolubility_table = open("insolubility.csv")
i_text = insolubility_table.read()

def take_data(x):
    v = (x.split('\n'))[0:]
    data = []
    new = []
    for i in v[:-1]:
        j = i.split(',')
        n = []
        for p in j[1:]:
            n.append(p)
        new = n[(len(j) - 2):]
        j.append(new[0])
        data.append(j)
    return data

s_unfiltered_table = take_data(s_text)
i_unfiltered_table = take_data(i_text)
def make_ion_dict(y):
    ion_d = {}
    int_list = []
    for i in y:
        int_list = []
        for e in i:
            int_list.append(e)
            ion_d[str(i[0])] = int_list[1:-1]
    return ion_d
    
s_filtered_dict = make_ion_dict(s_unfiltered_table)
i_filtered_dict = make_ion_dict(i_unfiltered_table)
#pprint(filtered_dict)


def create_reaction(a, b, c, d):
    list_results = ""
    coef = []
    back = []
    good_a = ""
    good_c = ""
    good_b = ""
    good_d = ""
    #For a
    if (ord(a[0]) > 48) and (ord(a[0]) < 58):
        coef.append(a[0])
    else:
        coef.append("1")
    #print(coef)
    if (ord(a[-1]) > 48) and (ord(a[-1]) < 58):
        back.append(a[-1])
    else:
        back.append("1")
    for i in str(a):
        if ((ord(i) > 64) and (ord(i) < 91)) or ((ord(i) > 96) and (ord(i) < 123)):
            good_a += i                  
    #print(good_a)
    
    #For c
    if (ord(c[0]) > 48) and (ord(c[0]) < 58):
        coef.append(c[0])
    else:
        coef.append("1")
    #print(coef)   
    if (ord(c[-1]) > 48) and (ord(c[-1]) < 58):
        back.append(c[-1])
    else:
        back.append("1")
    for i in str(c):
        if ((ord(i) > 64) and (ord(i) < 91)) or ((ord(i) > 96) and (ord(i) < 123)):
            good_c += i
    #print(good_c)
    
    #For b
    for i in str(b):
        if ((ord(i) > 64) and (ord(i) < 91)) or ((ord(i) > 96) and (ord(i) < 123)):
            good_b += i
    #print(good_b)
    #For d
    for i in str(d):
        if ((ord(i) > 64) and (ord(i) < 91)) or ((ord(i) > 96) and (ord(i) < 123)):
            good_d += i
    #print(good_d)
        
    a_prod = str(coef[0]) + good_c + str(back[0])
    c_prod = str(coef[1]) + good_a + str(back[1])
    
    a_prod = a_prod.replace("1", "")
    c_prod = c_prod.replace("1", "")
    
    #return(a_prod)
    #return(c_prod)
    
    list_results += (good_a + ",") 
    list_results += (good_b + ",")
    list_results += (good_c + ",")
    list_results += (good_d + ",")
    list_results += (a_prod + ",")
    list_results += (c_prod)
    list_results_list = (list_results).split(",")
    list_results_list.append(coef)
    return(list_results_list)
    

def get_list(dict):
    return dict.keys()

s_keys = get_list(s_filtered_dict)
i_keys = get_list(i_filtered_dict)
#pprint(s_keys)
#pprint(i_keys)
#Order is good_a, good_b, good_c, good_d, a_prod, c_prod
#print(create_reaction("K2", "SO4", "2Ag", "NO3"))
a_val = str(input("Insert first part of first reactant:"))
b_val = str(input("Insert second part of first reactant:"))
c_val = str(input("Insert first part of second reactant:"))
d_val = str(input("Insert second part of second reactant:"))
good_a = ((create_reaction(a_val, b_val, c_val, d_val))[0])
good_b = ((create_reaction(a_val, b_val, c_val, d_val))[1])
good_c = ((create_reaction(a_val, b_val, c_val, d_val))[2])
good_d = ((create_reaction(a_val, b_val, c_val, d_val))[3])
coefs = ((create_reaction(a_val, b_val, c_val, d_val)))[6]
ab_coef = coefs[0] 
cd_coef = coefs[1]
#print(cd_coef)

def find_insoluble(x, y):
    k = 0
    if x in s_keys:
        if y in s_filtered_dict[x]:
            k = 1
    if x in i_keys:
        if y not in i_filtered_dict[x]:
            k = 1
    if y in s_keys:
        if x in s_filtered_dict[y]:
            k = 1
    if y in i_keys:
        if x in i_filtered_dict[y]:
            k = 1
    return(k)
   
ksp = float(input("Ksp"))
exponent = float(input("10^-"))
Ksp_value = ksp* ((10**exponent)/ (10**(exponent*2)))
k_1 = find_insoluble(good_b,good_c)
k_2 = find_insoluble(good_a,good_d)
#print(k_1)
#print(k_2)

mole_amt_1 = float(input("Insert first molar amount:"))
mole_amt_2 = float(input("Insert second molar amount:"))

volume_1 = float(input("Insert first solution's volume:"))
volume_2 = float(input("Insert second solution's volume:"))

#if (k_1 == 1) or (k_2 == 1):
    #q = (mole_amt_1*volume_1/(volume_1+volume_2))**(int(ab_coef))
    #n = (mole_amt_2*volume_2/(volume_1+volume_2))**(int(cd_coef))
    #print(q)
    #print(n)
if ((k_1 == 1) or (k_2 == 1)) and ((volume_2/volume_1 == 2) or (volume_1/volume_2 == 2)):
    q = (mole_amt_1*volume_1/(volume_1+volume_2))**(int(ab_coef)) * (mole_amt_2*volume_2/(volume_1+volume_2))**(int(cd_coef))/2
elif ((k_1 == 1) or (k_2 == 1)) :
    q = (mole_amt_1*volume_1/(volume_1+volume_2))**(int(ab_coef)) * (mole_amt_2*volume_2/(volume_1+volume_2))**(int(cd_coef))
else:
    q = 0
if q == 0:
    print("Product not supported")
elif Ksp_value > q:
    print("We will not see a precipitate form")
    print ("Q =", q)
else:
    print("We will see a precipitate form")
    print ("Q =", q)