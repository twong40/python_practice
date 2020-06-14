import datetime

class Appointment():
    
    def __init__(self, meeting_type, patient, doctor, timeframe):
        self.meeting_type = meeting_type
        self.patient = patient
        self.doctor = doctor
        self.timeframe = timeframe
    
    def __str__(self):
        return(f"Meeting type: {self.meeting_type}, Patient: {self.patient}, Doctor: {self.doctor}, Time: {self.timeframe[0]}-{self.timeframe[1]}\n")

class Patient():
    
    def __init__(self, name = "Patient"):
        self.name = name
        self.appointments = []
        self.previous_appointments = []
        
    def __str__(self):
        return f"{self.name}"
    def add_appointment(self, appointment):
        self.appointments.append(appointment)
    
    def complete_appointment(self, appointment):
        if(appointment in self.appointments):
            self.previous_appointments.append(appointment)
            self.appointments.remove(appointment)
    
    def cancel_appointment(self, appointment):
        if(appointment in self.appointments):
            self.appointments.remove(appointment)
    
    def get_appointments(self):
        app=""
        for appointment in self.appointments:
            app = app + str(appointment)
        return(f"Appointment list for Patient: {self.name}\n{app}")

class Doctor():
    def __init__(self, name = "Doctor"):
        self.name = name
        self.appointments = []
        self.unavailable = []
        self.previous_appointments = []
    
    def __str__(self):
        return f"{self.name}"
    def add_appointment(self, appointment):
        self.appointments.append(appointment)
    
    def complete_appointment(self, appointment):
        if(appointment in self.appointments):
            self.previous_appointments.append(appointment)
            self.appointments.remove(appointment)
    
    def cancel_appointment(self, appointment):
        if(appointment in self.appointments):
            self.appointments.remove(appointment)
            
    def get_appointments(self):
        app = ""
        for appointment in self.appointments:
            app = app + str(appointment)
        return(f"Appointment list for Doctor: {self.name}\n{app}")

class Schedule():
    
    def __init__(self):
        self.sched = []
    
    def create_appointment(self,meeting_type, patient, doctor, timeframe):
        appointment = Appointment(meeting_type, patient, doctor, timeframe)
        patient.add_appointment(appointment)
        doctor.add_appointment(appointment)
        self.sched.append(appointment)
        self.sched = sorted(self.sched, key = lambda t: t.timeframe[1])
    
    def cancel_appointment(self, appointment):
        if(appointment in self.sched):
            appointment.patient.cancel_appointment(appointment)
            appointment.doctor.cancel_appointment(appointment)
            self.sched.remove(appointment)
    def get_appointments(self):
        app = ""
        for appointment in self.sched:
                app = app + str(appointment)
        return(f"Appointment list for Today:\n{app}")
            
    def check_sched(self, timeframe):
        for app in self.sched:
            if(app.timeframe[0] == timeframe[0] or app.timeframe[1] == timeframe[0] or app.timeframe[0] == timeframe[1] or app.timeframe[1] == timeframe[1]):
                return False
        return True
    
    def clear_sched(self):
        self.sched = []