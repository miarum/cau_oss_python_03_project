"""
입력을 받고 해야 할 일을 구현한 모듈
출력, 필터, 정렬, 종류 기능이 있다
"""
def start_process(path):
    import file_manager
    import parking_spot_manager
    spots=parking_spot_manager.str_list_to_class_list(file_manager.read_file(path))
    while True:
        print("---menu---")
        print("[1] print")
        print("[2] filter")
        print("[3] sort")
        print("[4] exit")
        select = int(input('type:'))
        if select == 1:
            parking_spot_manager.print_spots(spots)
        elif select == 2:
            print("---filter by---")
            print("[1] name")
            print("[2] city")
            print("[3] district")
            print("[4] ptype")
            print("[5] location")
            select = int(input('type:'))
            if select == 1:
                keyword = input('type name:')
                spots=parking_spot_manager.filter_by_name(spots,keyword)
            elif select == 2:
                keyword = input('type city:')
                spots=parking_spot_manager.filter_by_city(spots,keyword)
            elif select == 3:
                keyword = input('type district:')
                spots=parking_spot_manager.filter_by_district(spots,keyword)
            elif select == 4:
                keyword = input('type ptype:')
                spots=parking_spot_manager.filter_by_ptype(spots,keyword)
            elif select == 5:
                min_lat = float(input('type min lat:'))
                max_lat = float(input('type max lat:'))
                min_lon = float(input('type min long:'))
                max_lon = float(input('type max long:'))
                location=[min_lat, max_lat, min_lon, max_lon]
                spots=parking_spot_manager.filter_by_location(spots,location)
            else:
                print("invalid input")
        elif select == 3:
            keywords = ['name', 'city', 'district', 'ptype', 'latitude', 'longitude']
            print("---sort by---")
            print(keywords)
            keyword = input('type keyword:')
            if keyword in keywords:
                print("not implemented yet")
                # fill this block
            else: print("invalid input")
        elif select == 4:
            print("Exit")
            break
        else:
            print("invalid input")