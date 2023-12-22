# Standard Library
import math
import numpy as np
from typing import List, Optional, Union, Tuple, Dict

from curobo.types.math import Pose
from curobo.util_file import (
    file_exists,
    get_assets_path,
    get_filename,
    get_files_from_dir,
    get_robot_configs_path,
    join_path,
    load_yaml,
)
from curobo.util.usd_helper import UsdHelper, get_world_transform_xform

def load_link_transforms(
        usd_path: str,
        link_names: List[str],
        robot_base_path: str = "/World/robot",
        ) -> Dict[str, Pose]:
    # load usd file
    usd_helper = UsdHelper()
    usd_helper.load_stage_from_file(usd_path)

    link_prims = {}
    link_poses = {}
    for link_name in link_names:
        prim_path = join_path(robot_base_path, link_name)
        # get world pose for each link in link_prims
        prim = usd_helper.stage.GetPrimAtPath(prim_path)
        link_poses[link_name], _ = get_world_transform_xform(prim)

    return link_poses

if __name__ == "__main__":
    # Load USD file
    usd_path = "/home/xuehan/Desktop/TestCuRobo/iiwa_allegro_example5.usd"
    usd_helper = UsdHelper()
    usd_helper.load_stage_from_file(usd_path)

    # Get all links
    link_poses = load_link_transforms(usd_path,
                            ["palm_link", "index_link_3", "middle_link_3",
                             "ring_link_3",  "thumb_link_3"],
                            "/Root/Root/World/iiwa_allegro")
    # save link poses to .npz file
    output_path = "/home/xuehan/Desktop/TestCuRobo/allegro_ee_grasp_poses_5.npz"
    np.savez(output_path, **link_poses)
    print("Saved link poses to: ", output_path)