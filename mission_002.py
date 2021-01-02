import json

f = open("input.txt", "r")
data = f.read()

def toDecimal(binary):
    result = 0
    idx = len(binary) -1
    for i in list(binary):
        result+= (int(i) * (2**idx))
        idx-=1
    return result

def analyze(jdata):
    readings = jdata['readings']
    for r in readings:
        print('time == ' + str(r['time']))
        contaminants = r['contaminants']
        count=0
        for c in contaminants:
            count+=contaminants[c]
        print('total == ' + str(count))

str_data =''
for d in data.split(' '):
    str_data+=chr(toDecimal(d))

#fw = open("report.txt", "a")
#fw.write(str_data)
#fw.close()

def getCsvHeaders(jdata):
    headers = 'time;'
    for j in jdata:
        headers+=j['date']+';'
    return headers

jdata = json.loads(str_data)
report = getCsvHeaders(jdata)

contaminantsNames = []

report+='\n'
idx=0
while idx < 24:
    timeAdded = False
    for j in jdata:
        r = j['readings'][idx]
        if not timeAdded:
            report+=str(r['time'])+';'
            timeAdded=True
        contaminants = r['contaminants']
        count=0
        for c in contaminants:
            if not c in contaminantsNames:
                contaminantsNames.append(c)
            count+=contaminants[c]
        report+=str(count)+';'
    report+='\n'
    idx+=1

for c in contaminantsNames:
    report+='\n'+'contaminant : ' + c + '\n'
    report+=getCsvHeaders(jdata)+'\n'
    idx=0
    while idx < 24:
        timeAdded = False
        for j in jdata:
            r = j['readings'][idx]
            if not timeAdded:
                report+=str(r['time'])+';'
                timeAdded=True
            contaminants = r['contaminants']
            if c in contaminants:
                count=contaminants[c]
                report+=str(count)+';'
        report+='\n'
        idx+=1
    report+='\n'


fcsv = open("report.csv", "a")
fcsv.write(report)
fcsv.close()
print('done.')

print(bytearray.fromhex('4B554E47524144').decode())
