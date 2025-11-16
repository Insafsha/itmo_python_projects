from regex_task1 import solve_task1
from regex_task2 import solve_task2
from regex_task3 import solve_task3
from regex_extra import solve_extra

def main():
    solve_task1("data/task1-en.txt", "results/task1_result.txt")
    solve_task2("data/task2.html", "results/task2_result.txt")
    solve_task3("data/task3.txt", "results/task3_result.csv")
    solve_extra("data/task_add.txt", "results/task_add_result.txt")

    print("Готово! Все результаты сохранены в папке results/")

if __name__ == "__main__":
    main()
