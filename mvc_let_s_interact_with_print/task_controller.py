from task_model import TaskModel
from task_view import TaskView

class TaskController:


    ''' Constructor '''
    def __init__(self, master, model):
        if master.__class__.__name__ != "Tk":
            raise Exception("master is not a tk.TK()")

        if not isinstance(model, TaskModel):
            raise Exception("model is not a TaskModel")

        self.__model = model
        self.__view = TaskView(master)

        ''' Update taskview '''
        self.__view.update_title(model)

        ''' Link all callbacks from model to update view '''
        self.__model.set_callback_title(self.__view.update_title)

        ''' Link the button of view to update model '''
        self.__view.toggle_button.config(command = self.__model.toggle)
