class PlannerAgent:
    def plan(self, task):
        print("Planning task...")
        return f"Steps for {task}: step1 -> step2 -> step3"

class ExecutorAgent:
    def execute(self, plan):
        print("Executing plan...")
        return f"Done: {plan}"

class MultiAgentSystem:
    def __init__(self):
        self.planner = PlannerAgent()
        self.executor = ExecutorAgent()

    def run(self, task):
        plan = self.planner.plan(task)
        result = self.executor.execute(plan)
        return result

if __name__ == "__main__":
    system = MultiAgentSystem()
    task = input("Enter your task: ")
    result = system.run(task)
    print(result)
