"""
This file handles the argument parsing, and is the entry point of the app
"""

import argparse
import os
import sys

## these are the commands passed into function_switcher.py
run_notebook_command = "run_notebook"
list_notebooks_command="list_notebooks"
search_notebooks_command="search_notebooks"
open_notebook_command="open_notebook"
history_command="history"
next_notebook_command="next_notebook"
new_scene_command = "new_scene"
end_scene_command="end_scene"
change_scene_command="change_scene"
resume_scene_command="resume_scene"
delete_scene_command="delete_scene"
list_scene_command="list_scene"
add_library_command="add_library"
list_library_command="list_library"
remove_library_command="remove_library"
load_library_command="load_library"
set_env_command="set_env"
delete_env_command="delete_env"
list_env_command="list_env"
search_env_command="search_env"
## notebook help strings
run_notebook_help="run notebook"
run_notebook_notebook_help="notebook to run"
run_notebook_environment_help="html flag for opening in web"
open_notebook_help="open notebook in Azure Data Studio"
open_notebook_notebook_help="notebook to open"
list_notebooks_help="list notebooks to run, by ordinal."
search_notebooks_help="search for notebooks matching search term"
search_notebooks_term_help ="search term for notebooks"
next_notebook_help="model based prediction of what to do next in the current scene"
## scene help strings 
new_scene_help="new scene"
new_scene_name_help="name of new scene"
end_scene_help="end scene"
end_scene_name_help="name of scene to end"
change_scene_help="change scene"
change_scene_environment_help="environment for scene"
change_scene_name_help="name of scene to change to"
resume_scene_help="resume scene"
resume_scene_name_help="name of scene to resume"
delete_scene_help="delete scene"
delete_scene_name_help="name of scene to delete"
list_scene_help="list scenes"
## environment help strings
set_env_help="set environment variable for current scene"
set_env_name_help="name of the environment variable to set"
set_env_value_help="value of the environment variable to set"
delete_env_help="delete environment variable for current scene"
delete_env_name_help="name of the environment variable to delete"
search_env_help="search for environment variable names"
search_env_term_help="search term for environment variable"
list_env_help="list environment variables"
## library help strings
add_library_help="install library of notebooks to mtool"
add_library_path_help="the path to the library you want to add"
remove_library_help="remove library of notebooks mtool"
remove_library_path_help="path of the library you want to remove"
list_libraries_help="list libraries currently installed"
load_library_help="load libraries into mtool. Default loads from predefined library path"
load_library_path_help="load library from a specific directory into mtool"
## misc help strings
history_help="history of what you've done in the current scene"


def main(command_line=None):
    """creates all of the argparse parsers and returns the args passed in"""

    parser = argparse.ArgumentParser('mtool')
    subparsers = parser.add_subparsers(dest='command')
    
    run_notebook = subparsers.add_parser('run', aliases=["r"], help=run_notebook_help)
    run_notebook.add_argument('notebook', help=run_notebook_notebook_help)
    run_notebook.add_argument('html', nargs="?", help=run_notebook_environment_help)
    run_notebook.set_defaults(which=run_notebook_command)

    open_notebook = subparsers.add_parser('open', aliases=["o"], help=open_notebook_help)
    open_notebook.add_argument('notebook', help=open_notebook_notebook_help)
    open_notebook.set_defaults(which=open_notebook_command)
    
    search_notebooks = subparsers.add_parser('search', aliases=["sn"], help=search_notebooks_help)
    search_notebooks.add_argument('term', help=search_notebooks_term_help)
    search_notebooks.set_defaults(which=search_notebooks_command)

    list_notebooks = subparsers.add_parser('list', aliases=["l"], help=list_notebooks_help)
    list_notebooks.set_defaults(which=list_notebooks_command)

    history = subparsers.add_parser('history', aliases=["h"], help=history_help)
    history.set_defaults(which=history_command)

    next_notebook = subparsers.add_parser('whatnext', aliases=["n"], help=next_notebook_help)
    next_notebook.set_defaults(which=next_notebook_command)

    new_scene = subparsers.add_parser('newscene', aliases=["ns"], help=new_scene_help)
    new_scene.add_argument('name', help=new_scene_name_help)
    new_scene.set_defaults(which=new_scene_command)

    end_scene = subparsers.add_parser('endscene', aliases=["es"], help=end_scene_help)
    end_scene.add_argument('name', nargs="?", help=end_scene_name_help)
    end_scene.set_defaults(which=end_scene_command)

    change_scene = subparsers.add_parser('changescene', aliases=["cs"], help=change_scene_help)
    change_scene.add_argument('name', help=change_scene_name_help)
    change_scene.add_argument('environment', nargs="?", help=change_scene_environment_help)
    change_scene.set_defaults(which=change_scene_command)

    resume_scene = subparsers.add_parser('resumescene', aliases=["rs"], help=resume_scene_help)
    resume_scene.add_argument('name', help=resume_scene_name_help)
    resume_scene.set_defaults(which=resume_scene_command)

    delete_scene = subparsers.add_parser('deletescene', aliases=["ds"], help=delete_scene_help)
    delete_scene.add_argument('name', help=delete_scene_name_help)
    delete_scene.set_defaults(which=delete_scene_command)

    list_scene = subparsers.add_parser('listscenes', aliases=["ls"], help=list_scene_help)
    list_scene.set_defaults(which=list_scene_command)

    add_library = subparsers.add_parser('addlibrary', aliases=["al"], help=add_library_help)
    add_library.add_argument('path', help=add_library_path_help)
    add_library.set_defaults(which=add_library_command)

    remove_library = subparsers.add_parser('removelibrary', aliases=["rl"], help=remove_library_help)
    remove_library.add_argument('path', help=remove_library_path_help)
    remove_library.set_defaults(which=remove_library_command)

    list_libraries = subparsers.add_parser('listlibrary', aliases=["ll"], help=list_libraries_help)
    list_libraries.set_defaults(which=list_library_command)

    load_library = subparsers.add_parser('loadlibrary', aliases=["lo"], help=load_library_help)
    load_library.add_argument('path', nargs="?", help=load_library_path_help)
    load_library.set_defaults(which=load_library_command)


    set_env = subparsers.add_parser('setenv', aliases=["se"], help=set_env_help)
    set_env.add_argument('name', help=set_env_name_help)
    set_env.add_argument('value', help=set_env_value_help)
    set_env.set_defaults(which=set_env_command)

    search_env = subparsers.add_parser('searchenv', aliases=["s"], help=search_env_help)
    search_env.add_argument('term', help=search_env_term_help)
    search_env.set_defaults(which=search_env_command)

    delete_env = subparsers.add_parser('deleteenv', aliases=["de"], help=delete_env_help)
    delete_env.add_argument('name', help=delete_env_name_help)
    delete_env.set_defaults(which=delete_env_command)

    list_env = subparsers.add_parser('listenv', aliases=["le"], help=list_env_help)
    list_env.set_defaults(which=list_env_command)

    args = parser.parse_args(command_line)
    
    if len(sys.argv[1:])==0:
        parser.print_help()
    
    return args

if __name__ == "__main__":
    """the runner of mtool. makes a call to the switcher with the output of main"""
    from src.mtool.cli import function_switcher
    function_switcher.command(main())
