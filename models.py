class Employee:
    def __init__(self, employee_id, full_name, email, phone,
                 department, job_title, salary, date_joined, status):

        self.employee_id = employee_id
        self.full_name = full_name
        self.email = email
        self.phone = phone
        self.department = department
        self.job_title = job_title
        self.salary = salary
        self.date_joined = date_joined
        self.status = status

    def to_dict(self):
        return {
            "employee_id": self.employee_id,
            "full_name": self.full_name,
            "email": self.email,
            "phone": self.phone,
            "department": self.department,
            "job_title": self.job_title,
            "salary": self.salary,
            "date_joined": self.date_joined,
            "status": self.status
                   }
