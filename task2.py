
# Dictionary to store the data for each runner
runner_data = {}

inpt = ""

# Read data from the stream one line at a time
while (inpt!="END"):
    inpt = input("Enter Runner Number and Time Separated by '::' : ")

    try:
        # Split the line into the runner number and time
        runner, time = inpt.strip().split('::')
    except:
        # Validator
        if (inpt == "END"):
            break
        else:
            print("Error in data stream. Ignorning. Carry on.")
            continue

    if runner not in runner_data:
        runner_data[runner] = int(time)
    else:
        runner_data[runner] = int(time)

total_time = 0
total_runners = len(runner_data)

# Calculating the statistics for each runner
for times in runner_data.values():
    total_time += times

avg_time = total_time / total_runners

a=int(min(runner_data.values()))/60
print(a)

# Print the statistics for the runner
# Write "END to end taking input from user and processed to output"
print(f'Total Runners: {total_runners}')
print(f'Average time: {int(avg_time)/60} minute')
print(f'Fastest time: {int(min(runner_data.values()))/60} minute')
print(f'Slowest time: {int(max(runner_data.values()))/60} minute')
print(f'\nBest Time Here : Runner #{[i for i in runner_data if runner_data[i]==min(runner_data.values())]}')