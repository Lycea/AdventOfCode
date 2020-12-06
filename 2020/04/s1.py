from helper.helpers import  *

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
    print("s1")
    input=parse_by_nex_new_line(get_input("real_input.input"))
    check_passes()


