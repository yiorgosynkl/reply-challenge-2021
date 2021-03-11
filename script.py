import subprocess

program_name = 'main.py'
datasets = ['data_scenarios_a_example', 'data_scenarios_b_mumbai', 'data_scenarios_c_metropolis', 'data_scenarios_d_polynesia', 'data_scenarios_e_sanfrancisco', 'data_scenarios_f_tokyo']

for i, s in enumerate(datasets):
    data_in = s + '.in'
    data_out = s + '_out.txt'
    subprocess.check_output(f'python3 {program_name} < {data_in} > {data_out}', shell=True)[:-1].decode("utf-8")
