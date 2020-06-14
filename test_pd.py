import unittest
import pd 
import datetime
class TestSched(unittest.TestCase):

    def setUp(self):
        self.patients = [pd.Patient("Bob"), pd.Patient("Tom"), pd.Patient("John")]
        self.doctors = [pd.Doctor("Jim"), pd.Doctor("Pam"), pd.Doctor("Sam")]
        self.sched = pd.Schedule()

    def test_get_empty_sched(self):
        self.assertEqual(self.sched.get_appointments(), "Appointment list for Today:\n")
    
    def test_add_one_appointment(self):
        self.sched.create_appointment("Online",self.patients[0],self.doctors[0],(datetime.time(9),datetime.time(9,30)))
        self.assertEqual(self.sched.get_appointments(),"Appointment list for Today:\nMeeting type: Online, Patient: Bob, Doctor: Jim, Time: 09:00:00-09:30:00\n")

    def test_add_multiple_appointments(self):
        self.sched.create_appointment("Online",self.patients[0],self.doctors[0],(datetime.time(9),datetime.time(9,30)))
        self.sched.create_appointment("Office",self.patients[1],self.doctors[1],(datetime.time(10),datetime.time(11)))
        self.assertEqual(self.sched.get_appointments(),"Appointment list for Today:\nMeeting type: Online, Patient: Bob, Doctor: Jim, Time: 09:00:00-09:30:00\nMeeting type: Office, Patient: Tom, Doctor: Pam, Time: 10:00:00-11:00:00\n")

    def test_cancel_appointment(self):
        self.sched.create_appointment("Online",self.patients[0],self.doctors[0],(datetime.time(9),datetime.time(9,30)))
        self.sched.cancel_appointment(self.sched.sched[0])
        self.assertEqual(self.sched.get_appointments(), "Appointment list for Today:\n")

    def test_clear_sched(self):
        self.sched.create_appointment("Online",self.patients[0],self.doctors[0],(datetime.time(9),datetime.time(9,30)))
        self.sched.create_appointment("Office",self.patients[1],self.doctors[1],(datetime.time(10),datetime.time(11)))
        self.sched.clear_sched()
        self.assertEqual(self.sched.get_appointments(), "Appointment list for Today:\n")

class TestPatient(unittest.TestCase):
    def setUp(self):
        self.patients = [pd.Patient("Bob"), pd.Patient("Tom"), pd.Patient("John")]
        self.doctors = [pd.Doctor("Jim"), pd.Doctor("Pam"), pd.Doctor("Sam")]
        self.sched = pd.Schedule()
    
    def test_get_empty_sched_patients(self):
        self.assertEqual(self.patients[0].get_appointments(), "Appointment list for Patient: Bob\n")
    
    def test_add_one_appointment_patients(self):
        self.sched.create_appointment("Online",self.patients[0],self.doctors[0],(datetime.time(9),datetime.time(9,30)))
        self.assertEqual(self.patients[0].get_appointments(),"Appointment list for Patient: Bob\nMeeting type: Online, Patient: Bob, Doctor: Jim, Time: 09:00:00-09:30:00\n")

    def test_add_multiple_appointments_patients(self):
        self.sched.create_appointment("Online",self.patients[0],self.doctors[0],(datetime.time(9),datetime.time(9,30)))
        self.sched.create_appointment("Office",self.patients[0],self.doctors[0],(datetime.time(10),datetime.time(11)))
        self.assertEqual(self.patients[0].get_appointments(),"Appointment list for Patient: Bob\nMeeting type: Online, Patient: Bob, Doctor: Jim, Time: 09:00:00-09:30:00\nMeeting type: Office, Patient: Bob, Doctor: Jim, Time: 10:00:00-11:00:00\n")
    
    def test_cancel_appointment_patients(self):
        self.sched.create_appointment("Online",self.patients[0],self.doctors[0],(datetime.time(9),datetime.time(9,30)))
        self.sched.cancel_appointment(self.sched.sched[0])
        self.assertEqual(self.patients[0].get_appointments(),"Appointment list for Patient: Bob\n")

class TestDoctor(unittest.TestCase):
    def setUp(self):
        self.patients = [pd.Patient("Bob"), pd.Patient("Tom"), pd.Patient("John")]
        self.doctors = [pd.Doctor("Jim"), pd.Doctor("Pam"), pd.Doctor("Sam")]
        self.sched = pd.Schedule()
    
    def test_get_empty_sched_doctors(self):
        self.assertEqual(self.doctors[0].get_appointments(), "Appointment list for Doctor: Jim\n")
    
    def test_add_one_appointment_doctors(self):
        self.sched.create_appointment("Online",self.patients[0],self.doctors[0],(datetime.time(9),datetime.time(9,30)))
        self.assertEqual(self.doctors[0].get_appointments(),"Appointment list for Doctor: Jim\nMeeting type: Online, Patient: Bob, Doctor: Jim, Time: 09:00:00-09:30:00\n")

    def test_add_multiple_appointments_doctors(self):
        self.sched.create_appointment("Online",self.patients[0],self.doctors[0],(datetime.time(9),datetime.time(9,30)))
        self.sched.create_appointment("Office",self.patients[0],self.doctors[0],(datetime.time(10),datetime.time(11)))
        self.assertEqual(self.doctors[0].get_appointments(),"Appointment list for Doctor: Jim\nMeeting type: Online, Patient: Bob, Doctor: Jim, Time: 09:00:00-09:30:00\nMeeting type: Office, Patient: Bob, Doctor: Jim, Time: 10:00:00-11:00:00\n")
    
    def test_cancel_appointment_doctors(self):
        self.sched.create_appointment("Online",self.patients[0],self.doctors[0],(datetime.time(9),datetime.time(9,30)))
        self.sched.cancel_appointment(self.sched.sched[0])
        self.assertEqual(self.doctors[0].get_appointments(),"Appointment list for Doctor: Jim\n")

def suite():
    """
        Gather all the tests from this module in a test suite.
    """
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestSched))
    test_suite.addTest(unittest.makeSuite(TestPatient))
    test_suite.addTest(unittest.makeSuite(TestDoctor))
    return test_suite

if __name__ == "__main__":
    mySuit=suite()
    runner=unittest.TextTestRunner()
    runner.run(mySuit)