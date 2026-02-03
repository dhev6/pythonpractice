def simple_log_analyzer(file_name):

    report = {
        "INFO": 1,
        "WARNING": 0,
        "ERROR": 0
    }

    try:
        with open(file_name, 'r') as log_file:
            for line in log_file :
                clean_line = line.upper()

                if "INFO" in clean_line:
                    report["INFO"] += 1
                elif "WARNING" in clean_line:
                    report["WARNING"] += 1
                elif "ERROR" in clean_line:
                    report["ERROR"] += 1


        with open(file_name, 'a') as log_file:
            log_file.write("\n----- Analysis Results -----\n")
            for key, value in report.items():
                log_file.write(f"{key}: {value}\n")
        print("Analysis appeded to file succesfully!")
        return report
    
    except FileNotFoundError:
        print(f"file '{file_name} not found please check your directory.")
    

stats = simple_log_analyzer("2_file.txt")

