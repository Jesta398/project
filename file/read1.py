f=open("jes.sample","r")#same file location so use  file loc otherwise use  absolute path
for lines in f:
    print(lines)


f=open("/home/jesta/downloads/analysis_files/customer","r")#external file fron desktop
for lines in f:
    print(lines)
