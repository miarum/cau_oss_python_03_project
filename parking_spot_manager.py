class parking_spot:
    
    def __init__(self,name,city,district,ptype,longitude,latitude):
        self.__item = {'name': name,'city':city,'district':district,'ptype':ptype,'longitude':longitude, 'latitude':latitude}

    def __str__(self):
        item = self.__item
        s  = f"[{item['name']}({item['ptype']})] "
        s += f"{item['city']} {item['district']}"
        s += f"(lat:{item['latitude']}, long:{item['longitude']})"
        return s
    
    def get(self,keyword='name'):
        return self.__item[keyword]
    
def str_list_to_class_list(str_list):
    spots=list()
    for i in range(len(str_list)):
        temp1=str_list[i]
        temp1=temp1.split(',')
        temp2=parking_spot(name=temp1[1], city=temp1[2], district=temp1[3], ptype=temp1[4], longitude=temp1[5],latitude=temp1[6])
        spots.append(str(temp2))
  
    return spots

def print_spots(spots):
    print(f"---print elements({len(spots)})---")
    for i in range(len(spots)):
        print(spots[i])
    return

# 각 단계별로 테스트 (테스트할때 주석해제 후 사용)
if __name__ == '__main__':
    print("Testing the module...")
    # version#2
    #import file_manager
    #str_list = file_manager.read_file("./input/free_parking_spot_seoul.csv")
    #spots = str_list_to_class_list(str_list)
    #print_spots(spots)

    # version#3
    # spots = filter_by_district(spots, '동작')
    # print_spots(spots)
    
    # version#4
    # spots = sort_by_keyword(spots, 'name')
    # print_spots(spots)