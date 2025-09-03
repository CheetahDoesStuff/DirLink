# DirLink

## Installation

You can install DirLink manually (which i will not provide a guide for, but the files are in the latest release) or through the AUR, where its called dirlink and can be installed manually or with an AUR Helper like `yay`

## Usage

The command of the program (`dirlink`) has 4 options:

`dirlink new link_name /path/to/folder` - Creates a new link with the name link_name

`dirlink load link_name` - It will load the link and following this example it would copy `cd /path/to/folder` to your clipboard

`dirlink remove my_link` - It will delete the link

`dirlink getdata` - logs the path of the data file in the terminal

# Errors

heres a table of all error codes:

| Code | Description |
|------|-------------|
| 1 | Error: Link Does Not Exist / Was Not Found In Saved Data |
| 2 | Error : Link Already Exists / Was Found In Saved Data |
