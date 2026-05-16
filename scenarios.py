# Implementation of 5 different scenarios
# These functions are called after a specific time t to add change into the system

def scenario_base(state, t):
    # No new modifications to the system 
    return state

def scenario_binge_watch(state, t):
    # In this scenario, we are on a binge watch, we complete this binge for t = 75 (75 steps in the system)
    if t < 75:
        state[0] = 1.0 # state[0] is content usage, keep it at max till t = 75
    return state

def scenario_detox(state, t):
    if t < 35:
        state[0] = 0.8
    else:
        state[0] = 0.0
    # this will stop all usage after 35 steps 
    return state

def scenario_high_goal_focus_vs_high_algorithim_reward(state, t):
    state[0] = 1.0
    state[3] = 1.0 
    #Usage and Goal Focus both at 1.0
    return state


def scenario_rabbit_hole(state, t):
    # Usage increase over time
    ramp = 0.2 + (t * 0.05) # start at 0.2, then increase by 5% per step 
    if ramp > 1.0:
        ramp = 1.0 #ensure value doesn't exceed t
        state[0] = ramp
        return state 
    state[0] = ramp
    return state
