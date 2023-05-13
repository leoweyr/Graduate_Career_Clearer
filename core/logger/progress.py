class Progress:
    def __init__(self, name, target_steps=1):
        self.__m_name = name

        self.__m_target_steps = target_steps
        self.__m_completed_steps = 1

        self.__m_sub_progress_queue = []

    def __str__(self):
        if len(self.__m_sub_progress_queue) != 0:
            return f"[{self.__m_name} {self.__m_completed_steps}/{self.__m_target_steps}]" + str(self.__m_sub_progress_queue[self.__m_completed_steps - 1])
        else:
            return f"[{self.__m_name} {self.__m_completed_steps}/{self.__m_target_steps}]"

    def add_sub(self, progress):
        self.__m_sub_progress_queue.append(progress)
        self.__m_target_steps = len(self.__m_sub_progress_queue)

    def update(self, steps=1):
        if not self.state:
            if len(self.__m_sub_progress_queue) != 0:
                is_update = False
                completed_progress_count = 0
                for progress in self.__m_sub_progress_queue:
                    if not progress.state:
                        progress.update(steps)
                        is_update = True
                    if progress.state:
                        completed_progress_count += 1
                    if is_update:
                        break
                self.__m_completed_steps = completed_progress_count + 1
            else:
                self.__m_completed_steps += steps
        else:
            raise

    @property
    def state(self):
        if len(self.__m_sub_progress_queue) != 0:
            for progress in self.__m_sub_progress_queue:
                if not progress.state:
                    return False
        elif self.__m_completed_steps <= self.__m_target_steps:
            return False
        return True
