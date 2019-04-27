from typing import Dict
import pathlib


def _init(lint_data_dict: Dict, lintrc_path: pathlib.Path):
    for profile_name, profile_content in lint_data_dict.items():
        profile_path = lintrc_path / profile_name
        print(f"  Initializing {profile_name} ...")
        with open(profile_path, mode="w") as f_out:
            f_out.write(profile_content)
