from page_objct_final.demoqa_tests.model.pages.student_registration_page import StudentRegistrationForm


class StudentRegistrationSteps:
    def __init__(self):
        self.form = StudentRegistrationForm()

    def submit_form(self, last_name, subjects):
        # self.set_first_name(first_name).set_last_name(last_name).addSubjects(*subjects)
        self.form.last_name.type(last_name)
        self.form.subjects.autocomplete(*subjects)
        self.form.submit()
