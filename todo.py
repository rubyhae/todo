import json
import os #시스템 내부에 접근할 수 있는 권한

TASK_FILE = 'tasks.json'

def load_task():
    if os.path.exists('tasks.json'):#파일이 있는 경우
        with open(TASK_FILE, 'r', encoding='utf-8') as file: #file > open(~~)
            return json.load(file) #json.load() 함수라고도 하지만 해당 형태는 메소드라고도 한다
    return []

def save_task(tasks): #add_task를 통해 전달받은 해야할 일을 파일에 저장하는 기능
    with open(TASK_FILE, 'w', encoding='utf-8') as file: #file = open(TASK_FILE, 'w', encoding='utf-8')
        json.dump(tasks, file, indent=4, ensure_ascii=False)

def add_task(task_name): #할일 추가하는 함수
    tasks = load_task() #파일이 있다면 불러옴
    task = {'name': task_name, 'completed':False} #입력한 데이터가 추가됨
    tasks.append(task)
    save_task(tasks)
    
def view_task(): #할 일 목록보기, merge 진행
    tasks = load_task()
    if not tasks: #tasks는 if문을 만났을 때 false를 판별
        print("현재 등록된 작업이 없습니다.")
    else :
        print("작업 목록:")
        for i, task in enumerate(tasks, start=1): #enumerate() 인덱스를 같이 반환함
        #enumerate() -> i = 1, task = {"name" : "파이썬 공부하기", "completed" : false }
            status = "완료" if task['completed'] else "미완료" #dict는 키값을 넣으면 value를 돌려준다
            print(f'{i}. {task["name"]} - {status}')


def complete_task(task_number): #complete_task 머지 진행
    tasks = load_task() #tasks = [{"name":"파이썬 공부하기", "completed":false}, ]
    if 1 <= task_number <= len(tasks): #없는 번호를 입력할 경우, 번호를 잘못 입력했다 다시 입력해
        tasks[task_number - 1]["completed"] = True #tasks[0] => [{"name":"파이썬 공부하기", "completed":false}]
        save_task(tasks)
        print(f'할 일 : {tasks[task_number-1]["name"]}이 완료되었습니다.')
    else :
        print("유효하지 않은 번호입니다. 다시 확인 후 입력해주세요.")

def delete_task(task_number): #delete_task 완성, 머지 진행
    tasks = load_task()
    if 1 <= task_number <= len(tasks):
        delete_tsk = tasks.pop(task_number-1) #index 값 넣어줘야함 / pop() 통해서 삭제 및 반환되고 삭제된 데이터가 delete_tsk에 담김
        save_task(tasks) 
        print(f'할 일 : {delete_tsk["name"]}이(가) 삭제되었습니다. ')
    else :
        print("유효하지 않은 번호입니다. 다시 확인 후 입력해주세요.")

def show_menu():
    print("작업 관리 애플리케이션") #메뉴를 보여주는 함수
    print("1. 할 일 추가") #해야할 일 추가
    print("2. 할 일 목록보기") #해야할일 목록 확인
    print("3. 할 일 완료") #할일 완료
    print("4. 할 일 삭제") #끝낸 목록 삭제
    print("5. 종료")

def main():
    while True:
        show_menu()
        choice = input("원하는 작업을 선택해주세요 (1~5): ")

        if choice == '1':
            task_name = input("추가할 작업을 입력해주세요.: ") #파이썬 공부하기
            add_task(task_name)
        elif choice == '2':
            view_task()
        elif choice == '3':
            task_number = int(input("완료할 작업 번호를 입력해주세요.: "))
            complete_task(task_number)
        elif choice == '4':
            task_number = int(input("완료할 작업 번호를 입력해주세요.: "))
            delete_task(task_number)
        elif choice == '5':
            print("시스템을 종료합니다.")
            break
        else:
            print("잘못 입력하셨습니다. 1번부터 5번까지의 기능 중 하나를 선택해주세요.")

main()