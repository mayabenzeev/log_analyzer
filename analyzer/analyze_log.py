from collections import Counter

class LogAnalyzer:
    def __init__(self, log_file_path: str, report_type: str):
        self.log_file_path = log_file_path
        self.report_type = report_type
        self.logs = []
    
    def generate_report(self):
        # print(f"Generating {self.report_type} report...")
        # Each log line is a single event, with the following format:
        # [YYYY-MM-DD HH:MM:SS] USER:LEVEL: Message

        with open(self.log_file_path, 'r') as file:
            self.logs = file.readlines()

        if self.report_type == 'summary':
            return self.generate_summary_report()
        elif self.report_type == 'top-user':
            return self.generate_top_user_report()
        elif self.report_type == 'common-error':
            return self.generate_common_error_report()
    
    def generate_summary_report(self):
        print(f"Total log entries = {len(self.logs)}")

    def generate_top_user_report(self):
        user_frequency = {user : count 
                          for user, count in Counter(log.split("] ")[1].split(":")[0].strip()
                                                    for log in self.logs).items()}
        print(f"Top user = {max(user_frequency, key=user_frequency.get)}")
        
    def generate_common_error_report(self):
        error_frequency = {error : count 
                          for error, count in Counter(log.split("ERROR: ")[1].strip() 
                                                    for log in self.logs if ":ERROR:" in log).items()}
        print(f"Common error = {max(error_frequency, key=error_frequency.get)}")
    
    