import subprocess
from itertools import product

# the command that will be kept the same for all runs
base_command = "python3 train.py task=Hand_sphere wandb_activate=True wandb_group=srl_ethz wandb_project=rwr-6 capture_video=True force_render=False"

direction = [1.0,
             -1.0]

item = ["sphere", 
        "big_sphere", 
        "small_sphere"]

action_cost = [-0.002,
               0.,
               -0.01]

drop_cost = [-1.,
             -5.]

inclination = ["0",
               "5",
               "10",
               "15"]

angle = {}
angle["0"] = [0,0,0,1]
angle["5"] = [0,0.0436194,0,0.9990482]
angle["10"] = [0,0.0871557,0,0.9961947]
angle["15"] = [0,0.1305262,0,0.9914449]

relative_control = [True,
                     False]

list_params = [item, action_cost, drop_cost, inclination, relative_control, direction]

for elements in product(*list_params):
    
    string_angle = str(angle[elements[3]]).replace(" ", "")

    wandb_name = f"{elements[0]}_{elements[1]}_{elements[2]}_{elements[3]}_{elements[4]}_{elements[5]}"
    env = f"task.env.use_relative_control={elements[4]} task.env.object_type=[\"{elements[0]}\"] task.env.hand_start_r={string_angle} task.env.x_rotation_dir={elements[5]}"
    rew = f"task.rewards.scales.action_penalty={elements[1]} task.rewards.scales.drop_penalty={elements[2]}"
    command = f"{base_command} {env} {rew} wandb_name={wandb_name}"

    print(command)
    subprocess.run(command, shell=True)
    # save the weights so that it can be tested later
    subprocess.run(f"cp runs/FaiveHand/nn/FaiveHand.pth runs/Hand/nn/{wandb_name}.pth", shell=True)

## create a for loop iterating through each condition you want to compare
#for rel_ctrl in [True, False]:
#    wandb_name = f"relctrl_{rel_ctrl}"
#
#    command = f"{base_command} task.env.use_relative_control={rel_ctrl} wandb_name={wandb_name}"
#
#    print(command)
#    subprocess.run(command, shell=True)
#    # save the weights so that it can be tested later
#    #subprocess.run(f"cp runs/FaiveHand/nn/FaiveHand.pth {wandb_name}.pth", shell=True)