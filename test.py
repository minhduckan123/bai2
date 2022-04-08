import csv


csv_file = open("./random.csv", "w", newline="")
spam_writer = csv.writer(csv_file)
spam_writer.writerow(['Spam'] * 5 + ['Baked Beans'])
spam_writer.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])