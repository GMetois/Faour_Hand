import subprocess
from itertools import product

# the command that will be kept the same for all runs
base_command = "python3 train.py task=Hand_sphere_axis wandb_activate=True wandb_group=srl_ethz wandb_project=rwr-6 capture_video=True force_render=False"



direction = [1.0,
             -1.0]


axis_value = [#"x",
              "y",
              #"z"
              ]
axis = {}
axis["x"] = "rottask_obj_xrotvel"
axis["y"] = "rottask_obj_yrotvel"
axis["z"] = "rottask_obj_zrotvel"


inclination = [#"0",
               #"5",
               #"10",
               "15"
               #"30"
               ]
angle = {}
angle["0"] = [0,0,0,1]
angle["5"] = [0,0.0436194,0,0.9990482]
angle["10"] = [0,0.0871557,0,0.9961947]
angle["15"] = [0,0.1305262,0,0.9914449]
angle["30"] = [0,0.258819,0,0.9659258]

action_cost = [-0.002,
               0.,
               -0.01]

trq_cost = [-0.002,
            0.,
            -0.01]

list_params = [direction, axis_value, inclination, action_cost, trq_cost]

for elements in product(*list_params):

    string_angle = str(angle[elements[2]]).replace(" ", "")

    wandb_name = f"{elements[0]}_{elements[1]}_{elements[2]}_{elements[3]}_{elements[4]}"
    env = f"task.env.x_rotation_dir={elements[0]} task.env.hand_start_r={string_angle}"
    rew = f"++task.rewards.scales.{axis[elements[1]]}=0.01 task.rewards.scales.action_penalty={elements[3]} task.rewards.scales.dof_trq_penalty={elements[4]}"
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