import pandas as pd

def code_class_size(details_li: list, class_size:int, line:int, class_group_id: int):
    if class_size == 0:
        #print("Class Size 0 at", line, "with", class_size, "students")
        details_li[0] += 1
    elif 0 < class_size <= 10:
        #print("Class between 0 and 10 at", line, "with", class_size, "students")
        details_li[1] += 1
    elif 10 < class_size <= 20:
        #print("Class between 11 and 20 at", line, "with", class_size, "students")
        details_li[2] += 1
    elif 20 < class_size <= 30:
        #print("Class between 21 and 30 at", line, "with", class_size, "students")
        details_li[3] += 1
    elif 30 < class_size <= 40:
        #print("Class between 31 and 40 at", line, "with", class_size, "students")
        details_li[4] += 1
    elif 40 < class_size <= 50:
        #print("Class between 41 and 50 at", line, "with", class_size, "students")
        details_li[5] += 1
    elif 50 < class_size <= 60:
        details_li[6] += 1
    elif 60 < class_size <= 70:
        details_li[7] += 1
    elif 70 < class_size <= 80:
        details_li[8] += 1
    elif 80 < class_size <= 90:
        print("Class between 81 and 90 at", line, "with", class_size, "students")
        details_li[9] += 1
    else:
        print("Other class size:", class_size, "at line", line)
        details_li[len(details_li)-1] += 1

    #print(details_li)
    return details_li

def get_average(day_cls_sz_li):
    return sum(day_cls_sz_li) / len(day_cls_sz_li)

def get_data():

    df = pd.read_csv('class_nums.csv', header = None)

    mon_count, tue_count, wed_count, thu_count, fri_count = 0,0,0,0,0
    mon_details = [0] * 11
    tue_details = [0] * 11
    wed_details = [0] * 11
    thu_details = [0] * 11
    fri_details = [0] * 11

    class_size_li, mon_cls_sz_li, tue_cls_sz_li, wed_cls_sz_li, thu_cls_sz_li, fri_cls_sz_li = [], [], [], [], [], []


    for i in range(0, len(df.index)):
        day = df.iloc[i, 8]
        class_size = df.iloc[i, 5]
        class_group_id = df.iloc[i, 1]

        if day == "Monday": 
            mon_count += 1
            mon_details = code_class_size(mon_details, class_size, i, class_group_id)
            mon_cls_sz_li.append(class_size)
        elif day == "Tuesday": 
            tue_count += 1
            tue_details = code_class_size(tue_details, class_size, i, class_group_id)
            tue_cls_sz_li.append(class_size)
        elif day == "Wednesday": 
            wed_count  += 1
            wed_details = code_class_size(wed_details, class_size, i, class_group_id)
            wed_cls_sz_li.append(class_size)
        elif day == "Thursday": 
            thu_count += 1
            thu_details = code_class_size(thu_details, class_size, i, class_group_id)
            thu_cls_sz_li.append(class_size)
        elif day == "Friday": 
            fri_count += 1
            fri_details = code_class_size(fri_details, class_size, i, class_group_id)
            fri_cls_sz_li.append(class_size)
        else: print(i, "Dodgy day", day)

        class_size_li.append(class_size) 

    class_avg = get_average(class_size_li)

    print(mon_count, tue_count, wed_count, thu_count, fri_count)
    print(*mon_details)
    print(*tue_details)
    print(*wed_details)
    print(*thu_details)
    print(*fri_details)
    print("\n", class_avg)
    print(get_average(mon_cls_sz_li))
    print(get_average(tue_cls_sz_li))
    print(get_average(wed_cls_sz_li))
    print(get_average(thu_cls_sz_li))
    print(get_average(fri_cls_sz_li))

if __name__ == "__main__":
    get_data()