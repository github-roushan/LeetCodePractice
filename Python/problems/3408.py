class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.taskList = SortedList(key = lambda tp: (tp[2], tp[1]))
        self.taskMap = {}
        for task in tasks:
            self.add(*task)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.taskMap[taskId] = (userId, taskId, priority)
        self.taskList.add((userId, taskId, priority))

        # print(list(self.taskList))

    def edit(self, taskId: int, newPriority: int) -> None:
        userId = self.taskMap[taskId][0]
        self.rmv(taskId)
        self.add(userId, taskId, newPriority)

    def rmv(self, taskId: int) -> None:
        task = self.taskMap[taskId]
        self.taskList.remove(task)

    def execTop(self) -> int:
        if not len(self.taskList):
            return -1
        task = self.taskList.pop()
        return task[0]

