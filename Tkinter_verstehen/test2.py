def start_test_time(self):
    def count():
        global tt_counter
         
        #Manage initial delay:
        if tt_counter == 0:
            display = "Starting"
        else:
            startTime = datetime.fromtimestampt(tt_counter)
            startTime = startTime.replace(hour=0)
            ttStr = startTime.strftime("%H:%M:%S")
            display = ttStr
 
    self.LabelTestTime.config(text=display)
 
    #Trigger after 1 second delay
    self.LabelTestTime.after(1000, count)
 
    tt_counter += 1
 
    #Trigger the start of counter
    count()
 
 
def stop_test_time(self):
    #I tried samples online but none worked.
 
 
def on_btn_start(self):
    #Trigger the test time
    self.start_test_timer()
 
 
def on_btn_stop(self):
    self.stop_test_time()