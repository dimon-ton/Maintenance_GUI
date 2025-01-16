import csv


def write_csv(record_list):
    with open('test.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(record_list)


record = ['2024-06-08 16.12', 'a', 'b', 'c', 'd', 'e']
write_csv(record)