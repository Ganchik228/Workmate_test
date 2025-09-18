import csv
import argparse
import tabulate

def check_csv(file):
    if not file.endswith('.csv'):
        raise argparse.ArgumentTypeError("Можно использовать только CSV файлы")
    return file

class App:

    def __init__(self, files):
        self.files = files
    
    def read_files(self) -> list[dict]:
        rows = []
        for file in self.files:
            with open(file, 'r', encoding='utf-8') as f:
                csv_ = csv.DictReader(f)
                for row in csv_:
                    rows.append(row)
        return rows

    def print_files(self) -> None:
        for file in self.files:
            with open(file, 'r', encoding='utf-8') as f:
                csv_ = csv.DictReader(f)
                print(csv_)
                for row in csv_:
                    print(row)

    def students_performance(self) -> list[dict]:
        data = self.read_files()
        
        grades = {}
        for row in data:
            name = row['student_name']
            grade = int(row['grade'])
            grades.setdefault(name, []).append(grade)
            avg_grades = [{'student_name': name, 'grade': sum(grades_list)/len(grades_list)} 
                      for name, grades_list in grades.items()]
        avg_grades.sort(key=lambda x: x['grade'], reverse=True)
        print(tabulate.tabulate(avg_grades, headers='keys', tablefmt='grid'))
        return avg_grades


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--files', nargs='+', type=check_csv,required=True)

    parser.add_argument('--report', required=True, choices=['students-performance'])
    args = parser.parse_args()

    match args.report:
        case 'students-performance':
            app = App(args.files)
            rows = app.read_files()
            app.students_performance()