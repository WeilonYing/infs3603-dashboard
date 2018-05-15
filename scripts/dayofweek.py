import csv
import datetime

dayarray = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday']

with open('dates.csv', newline='') as csvfile:
    with open('output.csv', 'w') as outputfile:
        reader = csv.reader(csvfile)
        output_fields = ['dayNum', 'dayOfWeek']
        writer = csv.DictWriter(outputfile, fieldnames=output_fields, delimiter=',')
        for row in reader:
            date = datetime.datetime.strptime(row[0], "%d-%b-%y")
            daynum = date.weekday()
            writer.writerow({'dayNum': str(daynum), 'dayOfWeek': dayarray[daynum]})

