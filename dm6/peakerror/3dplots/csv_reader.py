f = open("/data/Lei_student/Hussain/ML/dm6/peakerror/40_summary.csv", "r")
o = open("/data/Lei_student/Hussain/ML/dm6/peakerror/40_mcc_llocal_qvalue.csv", "w")

for i in f.readlines():
    o.write(",".join([i.split(",")[4].replace("\n", ""), i.split(",")[8].replace("\n", ""), i.split(",")[6]]))
    o.write("\n")
