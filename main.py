import csv


class StudentFailException(Exception):
    pass


def calculate_average(grades):
    return sum(grades) / len(grades)


def main():
    with open('student_grades.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)  # skip header row
        for row in reader:
            name = row[0]
            grades = list(map(int, row[1:]))
            try:
                average = calculate_average(grades)
                if average < 70:
                    raise StudentFailException()
                else:
                    status = "Pass"
            except StudentFailException:
                status = "Fail"
            print(f"{name}: {average:.2f} ({status})")


if __name__ == '__main__':
    main()
