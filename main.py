#Documentation for matplotlib: https://matplotlib.org/stable/users/explain/quick_start.html
#Documentation for os: https://docs.python.org/3/library/os.html (used for making directory for saving screenshots)
from file_reader import load_data_from_json, brain_type
from logic import run_simulation
from scenarios import scenario_binge_watch, scenario_rabbit_hole, scenario_high_goal_focus_vs_high_algorithim_reward, scenario_detox, scenario_base
import matplotlib.pyplot as plt
import os

def make_grid(results, brain, scenario_name):
    concept_names = ["Usage", "Enjoyment", "Dopamine", "Focus", "Attention", "Algorithim"]
    
    plt.figure(figsize=(10, 6))
    for i in range(results.shape[1]):
        plt.plot(results[:, i], label=concept_names[i], linewidth=2) #plot state vector 

    plt.title(f"Ran {brain} on {scenario_name} scenario", fontsize=14)
    plt.xlabel("Time Step (at time t)", fontsize=12)
    plt.ylabel("Activation Level (0.0 - 1.0)", fontsize=12)
    plt.ylim(-0.05, 1.05)

    #ensure that the formatting looks correct
    plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1))
    plt.grid(alpha=0.3)
    plt.tight_layout()

    #save file to plot_sim director
    file_name = f"plot_simulations/{brain}_{scenario_name}.png"
    plt.savefig(file_name)
    print(f"Saved {file_name}")
    
    plt.show() #show graph before saving 
    plt.close()


def start():
    # create directories to store screenshots
    os.makedirs("plot_simulations", exist_ok=True)
    # running 15 simulations...
    all_scenarios = [
        ("Baseline", scenario_base),
        ("BingeWatch", scenario_binge_watch),
        ("RabbitHole", scenario_rabbit_hole),
        ("Detox", scenario_detox),
        ("HighGoalVs.HighReward", scenario_high_goal_focus_vs_high_algorithim_reward)
    ]
    all_brain_types = [
        brain_type.disciplined, 
        brain_type.average, 
        brain_type.distracted
    ]
    for brain in all_brain_types:
        matrix, start_state = load_data_from_json(brain)
        for scenario_name, scenario_func in all_scenarios:
            print(f"Running: {brain} with {scenario_name}...")
            # Run simulation 
            result = run_simulation(matrix, start_state.copy(), 100, scenario_func)

            make_grid(result, brain, scenario_name)
    #return result

#start simulation
start()

