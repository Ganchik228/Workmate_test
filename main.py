import csv
import argparse
import tabulate



class App:

    def __init__(self, files):
        self.files = files

    @staticmethod
    def check_csv(file):
        if not file.endswith('.csv'):
            raise argparse.ArgumentTypeError("Можно использовать только CSV файлы")
        return file

    def read_files(self) -> list[dict]:
        rows = []
        for file in self.files:
            with open(file, 'r', encoding='utf-8') as f:
                csv_ = csv.DictReader(f)
                for row in csv_:
                    rows.append(row)
        return rows

    def students_performance(self) -> list[dict]:
        data = self.read_files()
        
        grades = {}
        for row in data:
            name = row['student_name']
            grade = float(row['grade'])
            grades.setdefault(name, []).append(grade)
        
        avg_grades = [{'student_name': name, 'grade': round(sum(grades_list)/len(grades_list), 2)} 
                    for name, grades_list in grades.items()]
        avg_grades.sort(key=lambda x: x['grade'], reverse=True)
        return avg_grades


def main(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('--files', nargs='+', type=App.check_csv, required=True)
    parser.add_argument('--report', required=True, choices=['students-performance'])
    args = parser.parse_args(args)

    match args.report:
        case 'students-performance':
            app = App(args.files)
            rows = app.read_files()
            grades = app.students_performance()
            print(tabulate.tabulate(grades, headers="keys", tablefmt="grid"))

if __name__ == "__main__":
    main()