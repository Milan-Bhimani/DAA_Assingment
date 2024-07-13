class Solution:
    def average(self, salary: list[int]) -> float:
        min_salary = min(salary)
        max_salary = max(salary)
        total_salary = sum(salary)
        total_salary -= min_salary
        total_salary -= max_salary
        n = len(salary) - 2
        return total_salary / n