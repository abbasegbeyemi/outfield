from psolv_ch_4.psolv_ch_4_ADT import Queue
from random import randint


# Computer lab with two printers
# On average 10 students in the lab
# Students pring papers ranging from 1 -20 pages
# printer (mode 1) low quality but 10 pages per minute
# printer (mode 2) higher quality but 5 pages per minute

# We generate real world representations of th emain players in the lab
class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeremaining = 0

    def tick(self):
        if self.currentTask is not None:
            self.timeremaining -= 1

            if self.timeremaining <= 0:
                self.currentTask = None

    def busy(self):
        return True if self.currentTask is not None else False

    def start_next(self, new_task):
        self.currentTask = new_task
        self.timeremaining = new_task.get_pages() * 30 / self.pagerate


class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = randint(0, 20)

    def get_stamp(self):
        return self.timestamp

    def get_pages(self):
        return self.pages

    def wait_time(self, current_time):
        return current_time - self.timestamp


def simulation(num_seconds, pages_per_minute, num_students):
    printer_queue = Queue()
    printer = Printer(pages_per_minute)
    waiting_times = []

    for current_second in range(num_seconds):

        if new_print_task(num_students):
            task = Task(current_second)
            printer_queue.enqueue(task)

        if (not printer.busy()) and (not printer_queue.isEmpty()):
            next_task = printer_queue.dequeue()
            waiting_times.append(next_task.wait_time(current_second))
            printer.start_next(next_task)

        printer.tick()

    average_wait = sum(waiting_times) / len(waiting_times)

    print(f"Average wait is {average_wait:0.2f}secs | tasks remaining {printer_queue.size():3d}")


def new_print_task(students):
    # Average time between tasks is dependent on the number of students
    time_int = 3600//(students * 2)
    num = randint(0, time_int)
    return True if num == time_int else False


if __name__ == '__main__':
    print("5 pages per minute")
    for i in range(10):
        simulation(3600, 5, 40)

    print("10 pages per minute")
    for i in range(10):
        simulation(3600, 10, 40)
