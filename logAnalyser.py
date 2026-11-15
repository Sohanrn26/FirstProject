import sys
try:
    total_lines = 0
    error_count = 0
    info_count = 0
    warning_count = 0

    if len(sys.argv)>= 2:
        with open (sys.argv[1],"r") as file:
            for line in file:
                total_lines+=1
                if "ERROR" in line:
                    part1 = line.split()
                    print("ERROR ->", end="")
                    print(" ".join(part1[1:]))
                    error_count+=1
                elif "INFO" in line:
                    part2 = line.split()
                    print("INFO ->", end="")
                    print(" ".join(part2[1:]))
                    info_count+=1
                elif "WARNING" in line:
                    print("WARNING ->", end="")
                    part3 = line.split()
                    print(" ".join(part3[1:]))
                    warning_count+=1
        print(f"Total number of lines: {total_lines}")
        print(f"\nTotal errors: {error_count}")
        print(f"Total infos: {info_count}")
        print(f"Total warnings: {warning_count}")
    else:
        print("File does not exist")

    
except FileNotFoundError:
    print("Log file not found!")