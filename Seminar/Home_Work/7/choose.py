def new_data(result_choose, result_enter, data_get):
    if result_enter == 1:
        if len(data_get) > 1:
            index = data_get[-2].rfind('_')
            last_index = int(data_get[-2][index + 1:-2])
            array = list(map(lambda item: (item + f"_{last_index + 1}*\n\n"), result_choose.split()))
            return ''.join(data_get) + ''.join(array)
        else:
            array = list(map(lambda item: (item + f"_1*\n\n"), result_choose.split()))
            return ''.join(array)
    elif result_enter == 2:
        if len(result_choose) > 1:
            search_string = result_choose.split()
            for i in range(len(data_get)):
                if data_get[i].find(search_string[0]) > -1:
                    data_get[i] = search_string[1] + data_get[i][-4:]
                    break
    elif result_enter == 3:
        print(data_get)
        print_data = []
        for i in range(len(data_get)):
            if data_get[i].find(result_choose) > -1:
                find_data = data_get[i].split('_')
                data_print = list(filter(lambda x: x.find(find_data[1]) != -1, data_get))
                for j in range(len(data_print)):
                    data_print[j] = data_print[j][:-4]
                print(' '.join(data_print))
    #         output = data_get[i]
    #         output_list[i] = output.replace('\n', '')
    #     print(output_list)
    return ''.join(data_get)


