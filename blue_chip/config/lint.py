from typing import Dict, Union
import pathlib


def _init(lint_data_dict: Dict, lintrc_path: Union[pathlib.Path, str]):
    lintrc_path = pathlib.Path(lintrc_path)
    lintrc_path.mkdir(exist_ok=False)
    for profile_name, profile_content in lint_data_dict.items():
        profile_path = lintrc_path / profile_name
        print(f"  Initializing {profile_name} ...")
        with open(profile_path, mode="w") as f_out:
            f_out.write(profile_content)
