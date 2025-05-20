import random
LANES = [20, 30, 40, 50]
rt_lanes = []
lt_lanes = []
rt_cars_dic = {}
lt_cars_dic = {}

def random_lanes():
    for i in LANES:
        a = random.randint(0, 1)
        if a == 1:
            rt_lanes.append(i)
            rt_cars_dic[i] = []
        if a == 0:
            lt_lanes.append(i)
            lt_cars_dic[i] = []

random_lanes()

print(rt_lanes)
print(lt_lanes)
print(rt_cars_dic)
print(lt_cars_dic)
if rt_cars_dic[20] == []:
    print("Test")
rt_cars_dic[20].append(2)
rt_cars_dic[20].append(3)
rt_cars_dic[20].append(4)
rt_cars_dic[20].append(5)
print(rt_cars_dic)
print(rt_cars_dic[20][-1])
