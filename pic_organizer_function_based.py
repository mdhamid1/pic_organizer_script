#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 22:44:39 2020

@author: daniyalhamid
"""


import os
from PIL import Image
#import numpy.core.multiarray
import cv2



def file_profile_name_list_appender(files, file_name_list, profile_list):

    """
    Appends the file name and profile folder name located in the specified "filesdirectory" to an
    initially empty list called file_name_list and profile_list.

    Attributes:
        files (list) - list of contents in the filesdirectory. file_name_list (list) - empty list 
        profile_list - empty list

    Returns:
        file_name_list, profile_list
    """

    for name in files:
        if ".jpg" in name or ".mp4" in name:
            file_name_list.append(name)
        else:
            profile_list.append(name)

    return file_name_list, profile_list


def duplicate_file_remover(file_name):

    """
    Takes as input file_name, which is an item in the file_name_list and checks if duplicates 
    are present by checking the file_name

    Attributes:
        file_name (string)

    Returns:
        None
    """

    for i in range(100): #determine number of files outside this function and pass this number of files in and include in range function
        if "(" + str(i) + ")" in file_name:
            os.remove(file_name)


def image_checker(profile_folder_name, file_name, jpeg_list):

    """
    Extracts the width and height from the image file and appends the name of that file
    to an empty jpeg_list. If the file is not a jpeg file then the file is not analyzed. 

    Attributes:
        profile_folder_name (list), file_name (string), jpeg_list (empty list)

    Returns:
        Tuple containing width, height, jpeg_list
    """

    try:
        image = Image.open(file_name)
        width, height = image.size
        jpeg_list.append(file_name)
        return width, height, jpeg_list
    except OSError:
        print("Not an image file")
        return None


def file_directory_updater(filesdirectory, file_name):

    """
    Creates a new variable named file_directory containing the location of the file 
    on the particular iteration. 

    Attributes:
        filesdirectory (string), file_name in particular iteration of file_name_list

    Returns:
        file_directory (string)
    """

    file_directory = filesdirectory + "/" + file_name

    return file_directory


def sub_directory_updater(filesdirectory, profile_folder_name, file_name):

    """
    Creates a new variable named sub_directory containing the string location in directory for 
    the profile_folder_name, which is the particular item in iteration of profile_list. 
    Creates another variable named sub_file_directory containing the string location in 
    directory where the file in current iteration is to be placed. Updates the files1 
    variable which is an updated list of contents within the sub_directory folder.

    Attributes:
        filesdirectory (string), profile_folder_name (string), file_name (string)

    Returns:
        sub_directory (string), sub_file_directory (string), files1 (list)
    """

    sub_directory = filesdirectory + "/" + profile_folder_name
    sub_file_directory = sub_directory + "/Stories" + "/" + file_name
    files1 = os.listdir(sub_directory)

    return sub_directory, sub_file_directory, files1


def story_checker(files1, file_directory, sub_directory, sub_file_directory):

    if "Stories" in files1:
        os.replace(file_directory, sub_file_directory)
    elif "Stories" not in files1:
        os.mkdir(sub_directory + "/Stories")
        os.replace(file_directory, sub_file_directory)


def jpeg_res_checker(file_name, jpeg_list, width, height, filesdirectory, profile_folder_name):

    if file_name in jpeg_list and (width == 480 and height <= 854) or (width == 640 and height <= 1136) or (width == 656 and height <= 1166) or (width == 720 and height == 1280) or (width == 750 and height <= 1333) or (width == 828 and height == 1472) or (width == 1024 and height == 1820) or (width == 1080 and height >=1919):
        #consider creating a data structure here that holds these values and iterates through to check. maybe a dictionary containing a list of tuples
        file_directory = file_directory_updater(filesdirectory, file_name)
        sub_directory, sub_file_directory, files1 = sub_directory_updater(filesdirectory, profile_folder_name, file_name)
        story_checker(files1, file_directory, sub_directory, sub_file_directory)
    else:
        os.replace(filesdirectory + "/" + file_name, filesdirectory + "/" + profile_folder_name + "/" + file_name)


def mp4_checker(file_name):
    if ".mp4" in file_name:
        file_path = file_name
        vid = cv2.VideoCapture(file_path)
        height_mp4 = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
        width_mp4 = vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        print("MP4_Res", width_mp4, height_mp4, file_name)
        return width_mp4, height_mp4
    else:
        return None


def mp4_res_checker(file_name, width_mp4, height_mp4, filesdirectory, profile_folder_name):
    if (width_mp4 == 480 and height_mp4 <= 854) or (width_mp4 == 640 and height_mp4 <= 1136) or (width_mp4 == 656 and height_mp4 <= 1166) or (width_mp4 == 720 and height_mp4 == 1280) or (width_mp4 == 750 and height_mp4 <= 1333) or (width_mp4 == 828 and height_mp4 == 1472) or (width_mp4 == 1024 and height_mp4 == 1820) or (width_mp4 == 1080 and height_mp4 >=1919):
        file_directory = file_directory_updater(filesdirectory, file_name)
        sub_directory, sub_file_directory, files1 = sub_directory_updater(filesdirectory, profile_folder_name, file_name)
        story_checker(files1, file_directory, sub_directory, sub_file_directory)
    else:
        os.replace(filesdirectory + "/" + file_name, filesdirectory + "/" + profile_folder_name + "/" + file_name)


def unmatched_folder_creator(files, filesdirectory, file_directory, unmatched_file_directory):

    if "1_Unmatched" in files:
        os.replace(file_directory, unmatched_file_directory)
    elif "1_Unmatched" not in files:
        os.mkdir(filesdirectory + "/1_Unmatched")
        os.replace(file_directory, unmatched_file_directory)



def main():

    filesdirectory = r'/Users/daniyalhamid/Documents/Programming/Python_Scripts_Data_Processing/Instagram/ig_photo_test_trial'
    files = os.listdir(filesdirectory)
    os.chdir(filesdirectory)

    profile_list = []
    file_name_list = []
    jpeg_list = []

    file_name_list, profile_list = file_profile_name_list_appender(files, file_name_list, profile_list)

    for file_name in file_name_list:
        duplicate_file_remover(file_name)

    profile_list = []
    file_name_list = []
    files = os.listdir(filesdirectory)
    file_name_list, profile_list = file_profile_name_list_appender(files, file_name_list, profile_list) #instead of calling this function 
    #create another function to pop the duplicate file name from the list.



    for profile_folder_name in profile_list:
        for file_name in file_name_list:
            if profile_folder_name in file_name:
                image_info_tuple = image_checker(profile_folder_name, file_name, jpeg_list)
                if image_info_tuple:
                    width, height, jpeg_list = image_info_tuple
                    jpeg_res_checker(file_name, jpeg_list, width, height, filesdirectory, profile_folder_name)

                mp4_info_tuple = mp4_checker(file_name)
                if mp4_info_tuple:
                    width_mp4, height_mp4 = mp4_info_tuple
                    mp4_res_checker(file_name, width_mp4, height_mp4, filesdirectory, profile_folder_name)


    file_name_list = []
    files = os.listdir(filesdirectory)
    file_name_list, profile_list = file_profile_name_list_appender(files, file_name_list, profile_list)


    for file_name in file_name_list:
        file_directory = file_directory_updater(filesdirectory, file_name)
        unmatched_file_directory = filesdirectory + "/1_Unmatched" + "/" + file_name
        unmatched_folder_creator(files, filesdirectory, file_directory, unmatched_file_directory)
        files = os.listdir(filesdirectory)

#consider creating a yaml or json file to read in info and automatically create folders based on what is writtein in 
#json or yaml file. also read filesdirectory link from there instead of hardcoding it. 

if __name__ == '__main__':
    main()