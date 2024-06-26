import shutil, os
from pathlib import Path


def create_user_folders() -> None:
    """Creates user folders with module materials

    For all the names in the 'user.txt' file, creates a new folder in the user
    folder with the user's name. The modules folder is then copied across. If the
    users folder already exists, then no new folder is created or files / folders
    copied across.
    """
    with open("users.txt", "r") as file:
        for line in file:
            username = line.strip()
            username = username.replace(" ", "_")
            username = username.lower()
            folder_path = Path("users") / username
            if folder_path.exists():
                print(f"The folder {folder_path} already exists.")
            else:
                folder_path.mkdir(parents=True)
                print(f"The folder {folder_path} has been created.")
                shutil.copytree(
                    Path("programming_in_healthcare"),
                    folder_path,
                    dirs_exist_ok=True,
                )
                for folder in os.listdir(folder_path):
                    os.rename(
                        folder_path / folder,
                        folder_path / Path(username + "_" + folder),
                    )

    return


if __name__ == "__main__":
    create_user_folders()
