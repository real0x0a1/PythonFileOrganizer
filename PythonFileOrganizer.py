#!/bin/python3

# -*- Author: Ali -*-
# -*- Info: File Organizer -*-

import os
import shutil
from datetime import datetime

# Source directory where files are located
source_dir = '/path/to/source/directory'

# Destination directory where organized files will be placed
destination_dir = '/path/to/destination/directory'

# Iterate through files in the source directory
for filename in os.listdir(source_dir):
    file_path = os.path.join(source_dir, filename)
    if os.path.isfile(file_path):
        file_extension = os.path.splitext(filename)[1][1:]
        file_type_dir = os.path.join(destination_dir, file_extension)
        os.makedirs(file_type_dir, exist_ok=True)

        file_date = datetime.fromtimestamp(os.path.getmtime(file_path))
        year_dir = os.path.join(file_type_dir, str(file_date.year))
        month_dir = os.path.join(year_dir, f"{file_date.month:02d}")
        os.makedirs(month_dir, exist_ok=True)

        new_file_path = os.path.join(month_dir, filename)
        shutil.move(file_path, new_file_path)
