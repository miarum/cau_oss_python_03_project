'''
주차장 정보와 관련된 처리를 하는 함수를 모아둔 모듈
'''
class parking_spot:
    '''
    주차장의 기본 정보를 정의하는 클래스
    '''
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
    '''
    정리되지 않은 리스트를 받아와 원소별로 자른다. 그후 각각을 ','을 기준으로 잘라 새로운 배열을 만든다.
    새로운 배열을 가지고 클래스 객체를 만들고 클래스의 str 함수를 통해 다시 나열한다.
    나열된 배열을 모두 더해(연결해) 배열을 리턴한다.
    '''
    spots=list()
    for i in range(len(str_list)):
        temp1=str_list[i]
        temp1=temp1.split(',')
        temp2=parking_spot(name=temp1[1], city=temp1[2], district=temp1[3], ptype=temp1[4], longitude=temp1[5],latitude=temp1[6])
        spots.append(str(temp2))
  
    return spots

def print_spots(spots):
    '''
    입력 받은 배열을 순서대로 출력한다.
    '''
    print(f"---print elements({len(spots)})---")
    for i in range(len(spots)):
        print(spots[i])
    return


def filter_by_name(spots, name):
    #이름을 기준으로 필터하는 함수
    spots = [i for i in spots if name in i]
    return spots

def filter_by_city(spots, city):
    #도시를 기준으로 필터하는 함수
    spots = [i for i in spots if city in i]
    return spots

def filter_by_district(spots, district):
    #구를 기준으로 필터하는 함수
    spots = [i for i in spots if district in i]
    return spots

def filter_by_ptype(spots, ptype):
    #종류를 기준으로 필터하는 함수
    spots = [i for i in spots if ptype in i]
    return spots

def filter_by_location(spots, locations):
    #미구현    
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