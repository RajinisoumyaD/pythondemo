class DailyChecklist:
    def __init__(self):
        self.checklist = []
        self.completed_tasks = []
        self.incomplete_tasks = []

    def add_task(self, task):
        self.checklist.append(task)
        print(f'Task "{task}" added to checklist.')

    def mark_completed(self, task):
        if task in self.checklist:
            self.checklist.remove(task)
            self.completed_tasks.append(task)
            print(f'Task "{task}" marked as completed.')
        else:
            print(f'Task "{task}" not found in checklist.')
    def end_of_day_review(self):
        self.incomplete_tasks.extend(self.checklist)
        self.checklist.clear()
        print("Day's review completed.")
        print("Completed Tasks:", self.completed_tasks)
        print("Incomplete Tasks:", self.incomplete_tasks)
# Example Usage
checklist = DailyChecklist()
checklist.add_task("Finish coding project")
checklist.add_task("Read a chapter of a book")
checklist.add_task("Exercise for 30 minutes")
checklist.mark_completed("Finish coding project")
checklist.mark_completed("Exercise for 30 minutes")
checklist.end_of_day_review()