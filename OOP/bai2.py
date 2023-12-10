class Job:
    def __init__(self, job_code, job_name, industry, salary):
        self.job_code = job_code
        self.job_name = job_name
        self.industry = industry
        self.salary = salary

    def evaluate(self):
        average_skill = sum(self.skills.values()) / len(self.skills)
        if average_skill > 9.0:
            return "Rất phù hợp"
        elif average_skill > 7.0:
            return "Phù hợp"
        elif average_skill > 5.0:
            return "Tạm được"
        elif average_skill > 3.0:
            lacking_skills = [
                skill for skill, rating in self.skills.items() if rating < 4.0
            ]
            return f"Cần bổ sung kiến thức, đặc biệt là: {', '.join(lacking_skills)}"
        else:
            return "Cần học lại kiến thức cơ bản"


class AI(Job):
    def __init__(
        self,
        job_code,
        job_name,
        industry,
        salary,
        python_skill,
        ml_skill,
        deep_skill,
        math_skill,
    ):
        super().__init__(job_code, job_name, industry, salary)
        self.python_skill = python_skill
        self.ml_skill = ml_skill
        self.deep_skill = deep_skill
        self.math_skill = math_skill

        self.skills = {
            "Python": python_skill,
            "ML": ml_skill,
            "Deep Learning": deep_skill,
            "Math": math_skill,
        }


class Backend(Job):
    def __init__(
        self,
        job_code,
        job_name,
        industry,
        salary,
        sql_skill,
        oop_skill,
        api_skill,
        java_skill,
    ):
        super().__init__(job_code, job_name, industry, salary)
        self.sql_skill = sql_skill
        self.oop_skill = oop_skill
        self.api_skill = api_skill
        self.java_skill = java_skill
        self.skills = {
            "SQL": sql_skill,
            "OOP": oop_skill,
            "API": api_skill,
            "Java": java_skill,
        }


class Frontend(Job):
    def __init__(
        self,
        job_code,
        job_name,
        industry,
        salary,
        html_skill,
        css_skill,
        nodejs_skill,
        ux,
        ui,
    ):
        super().__init__(job_code, job_name, industry, salary)
        self.html_skill = html_skill
        self.css_skill = css_skill
        self.nodejs_skill = nodejs_skill
        self.ux = ux
        self.ui = ui
        self.skills = {
            "HTML": html_skill,
            "CSS": css_skill,
            "Node.js": nodejs_skill,
            "UX": ux,
            "UI": ui,
        }


class Fullstack(Backend, Frontend):
    def __init__(
        self,
        job_code,
        job_name,
        industry,
        salary,
        sql_skill,
        oop_skill,
        api_skill,
        java_skill,
        html_skill,
        css_skill,
        nodejs_skill,
        ux,
        ui,
    ):
        Backend.__init__(
            self,
            job_code,
            job_name,
            industry,
            salary,
            sql_skill,
            oop_skill,
            api_skill,
            java_skill,
        )
        Frontend.__init__(
            self,
            job_code,
            job_name,
            industry,
            salary,
            html_skill,
            css_skill,
            nodejs_skill,
            ux,
            ui,
        )
        self.skills = {
            "SQL": sql_skill,
            "OOP": oop_skill,
            "API": api_skill,
            "Java": java_skill,
            "HTML": html_skill,
            "CSS": css_skill,
            "Node.js": nodejs_skill,
            "UX": ux,
            "UI": ui,
        }


# Sử dụng các lớp
ai_job = AI("AI001", "Data Scientist", "Data Science", 100000, 5, 4, 3, 5)
backend_job = Backend(
    "BE001", "Backend Developer", "Software Development", 90000, 4, 5, 4, 4
)
frontend_job = Frontend(
    "FE001", "Frontend Developer", "Software Development", 85000, 3, 4, 4, 5, 5
)
fullstack_job = Fullstack(
    "FS001",
    "Fullstack Developer",
    "Software Development",
    120000,
    5,
    5,
    4,
    4,
    4,
    5,
    4,
    4,
    3,
)


# In thông tin và đánh giá
print(ai_job.__dict__)
# print(ai_job.evaluate())

print(backend_job.__dict__)
# print(backend_job.evaluate())

print(frontend_job.__dict__)
# print(frontend_job.evaluate())

print(fullstack_job.__dict__)
# print(fullstack_job.evaluate())
