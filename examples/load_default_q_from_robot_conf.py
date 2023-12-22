import yaml
import numpy as np

if __name__ == "__main__":
    # Load robot config file
    robot_config_path = "/home/xuehan/Desktop/TestCuRobo/iiwa_allegro_example5.yaml"
    with open(robot_config_path) as f:
        robot_config = yaml.load(f, Loader=yaml.FullLoader)
    # Get default joint values (key name: "default_q")
    default_q = robot_config["default_q"]
    print(default_q)
    # Save default joint values to .npz file
    output_path = "/home/xuehan/Desktop/TestCuRobo/iiwa_allegro_target_q_example5.npz"
    np.savez(output_path, default_q=default_q)
