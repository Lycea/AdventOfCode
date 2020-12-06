from helper.helpers import  *
import re

input=""

def check_passes():
    ids = ["byr",
           "iyr",
           "eyr",
            "hgt",
            "hcl",
            "ecl",
            "pid",
            "cid"]

    valid_passes = 0

    print("iterating passports")
    for passport in input:
        valid_keys = 0

        key_vals = list(filter(None,passport.split(" ")))
        dict ={}
        found_ids=[]

        for pair in key_vals:
            raw_pair = pair.split(":")

            dict[raw_pair[0]]=raw_pair[1]
        print(dict)

        for key in dict:
            print(key,ids)
            if key in ids:

                if key == "byr":
                    if len(dict[key]) == 4 and  int(dict[key])>=1920 and int(dict[key])<=2002 :
                        pass
                    else:
                        continue

                elif key == "iyr":
                    if len(dict[key]) == 4 and int(dict[key]) >= 2010 and int(dict[key]) <= 2020 :
                        pass
                    else:
                        continue

                elif key == "eyr":
                    if len(dict[key]) == 4 and int(dict[key]) >= 2020 and int(dict[key]) <= 2030 :
                        pass
                    else:
                        continue

                elif key == "hgt":
                    #dff between in and cm
                    if dict[key].endswith("in"):
                        ins = int(dict[key].replace("in",""))
                        if ins >=59 and ins <=76:
                            pass
                        else:
                            continue

                    elif dict[key].endswith("cm"):
                        cm = int(dict[key].replace("cm", ""))
                        if cm >=150 and cm <=193:
                            pass
                        else:
                            continue
                    else:
                        continue

                elif key == "hcl":
                    if dict[key][0]!="#":
                        continue
                    else:
                        #TODO: check here if regex is ok
                        col=dict[key][1:]
                        result = re.match("[a-f,0-9]{6}",col)
                        if result:
                            print("match",result,col)
                            pass
                        else:
                            print("no match",col)
                            continue
                    pass

                elif key == "ecl":
                    cl_list =[
                        "amb","blu","brn","gry","grn","hzl","oth"
                    ]
                    if dict[key] not in cl_list:
                        print("Not a valid eyecl ",dict[key])
                        continue
                    pass

                elif key == "pid":
                    if len((dict[key])) != 9:
                        continue
                    pass

                elif key == "cid":
                    pass

                #found and valid
                found_ids.append(key)
                valid_keys += 1
                print(key, valid_keys)

        if "cid" not in found_ids:
            print("adding one sicne north pole cit...")
            valid_keys+=1

        if valid_keys==8:
            valid_passes+=1
            print("valid pass",dict)

    print(valid_passes)



    pass


def run():
    global input
    print("s2")
    input=parse_by_nex_new_line(get_input("real_input.input"))
    check_passes()


