#File:          fileFormatConversion.py
#Name:          Jacob Strickland
#Date Created:  Feb 9, 2020
#Date Modified: Feb 9, 2020
#Description:   The program takes a csv file and changes the format to be useable
#               with a KNN model

#import libraries
import csv
import os
import time

start_time = time.time() #to track how long the program takes to run

csv_path = os.path.join(r'D:\Python', 'anime-planet-ranking-020920.csv')
csv_path1 = os.path.join(r'D:\Python', 'anime-planet-ranking-KNN2.csv')
with open(csv_path, 'r', newline='', encoding='utf-8') as input_file:
    with open(csv_path1, 'w', newline='', encoding="utf-8") as output_file:
        data_writer = csv.writer(output_file)

        #finds and creates all the headers
        next(input_file) #skip the headings

        header = []

        header.append("Title")
        header.append("Rank")
        header.append("Year")
        header.append("Rating")
        header.append("Votes")

        raw_anime_data = []
        for line in input_file.readlines():
            data_row = line.strip().split(',')
            while not data_row[1].isdigit():                #prevents titles with commas to get split up
                data_row[0] = data_row[0] + data_row[1]
                data_row.pop(1)

            data_row[3] = (float(data_row[3]))/2000
            data_row[5] = (float(data_row[5]))/10
            data_row[6] = (float(data_row[6]))/10000
            
            raw_anime_data.append(data_row)
            

        for media in raw_anime_data:
            if media[2] not in header:
                header.append(media[2])

        for studio in raw_anime_data:
            if studio[4] not in header:
                header.append(studio[4])

        for tag in raw_anime_data:
            for i in range(7, len(tag)):
                if tag[i] not in header:
                    header.append(tag[i])



        #print the headers to the new file
        data_writer.writerow(header)
            
        for anime in raw_anime_data:
            anime_info = []

            anime_info.append(anime[0]) #Title
            anime_info.append(anime[1]) #Rank
            anime_info.append(anime[3]) #Year
            anime_info.append(anime[5]) #Rating
            anime_info.append(anime[6]) #Votes

            for item in header[5:]:
                if item in anime:
                    anime_info.append('1')
                else:
                    anime_info.append('0')

            data_writer.writerow(anime_info)


print((time.time()-start_time), "seconds") #output how long the program took to run
