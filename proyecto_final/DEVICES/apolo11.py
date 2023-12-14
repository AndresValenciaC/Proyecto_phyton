import datetime
import os
import random

from project_dummy_data import project_missions,devices_status,hash_format,date_format

class Apolo11:

   mission_list = project_missions


   def generate_mission_files(missions,num_files):
     output_directory = "SIMULACIONES/folder1"

     if not os.path.exists(output_directory):
        os.makedirs(output_directory)

     all_files_data = []

     for mission in missions:
         name = mission["name"]
         components = mission["components"]

         status_components = {component : random.choice(['good', 'excellent', 'faulty', 'warning']) for component in components}

         component_data = [{"mission": name, "component": component, "status": status} for component, status in status_components.items()]
         all_files_data.extend(component_data)

     selected_files_data = selected_files_data = random.choices(all_files_data, k=num_files)

     for file_data in selected_files_data:
         name = file_data["mission"]
         component = file_data["component"]
         status = file_data["status"]
         date_time = date_format()
         file_name = f"Mission_{name}_{component}_{date_time}_{random.randint(1, 100)}.txt"
         file_path = os.path.join(output_directory, file_name)

         with open(file_path, 'w') as file:
            hash_m = hash_format(date_time,name,component,status)
            file.write("Date: " + date_time + "\n")
            file.write("Mission: " + name + "\n")
            file.write("Device Type: " + component + "\n")
            file.write("Device Status: " + status + "\n")
            file.write("Hash: " + hash_m + "\n")


   generate_mission_files(mission_list,7)








