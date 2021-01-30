#The GDELT Program is an 'open source' web crawler of global news reporting translated from 65 core languages
##GDELT runs a deep learning algorithm on all news reports and gives the user geographic, cultural, religious, and identity information about news reporting globally
###GDELT uses CAMEO language as a means to allow researchers to decipher complex, granular new data
####CAMEO stands for "Conflict and Mediation Even Obsevervations," a language originally created by the NSF for open source use
#####The major issue GDELT faces now is that even though it is open source data and uses NSF-funded structured languages,
######...the program has become intrinsically tied to monetized data analytics--namely Google Big Query
#######This code allows you to append GDELT files together and structure them back into CAMEO language for Geographic Social Network Analysis
########The main advantage to using this code is that it is free and emancipates GDELT data from Google Big Query for use with your preferred GISystem
#########Psuedo code is important, please read it as you use this script :)
########################################################################################################################

#In order to turn your downloaded data into a usable, structured CAMEO language dataset, you must import the os, glob, csv, and pandas libraries
##Depending on your machine's specifications, you can install the libraries with the commands below
###$pip install os, glob, csv, pandas $pip3 install os, glob, csv, pandas  $conda install os, glob, csv, pandas

import os,glob,csv
import pandas as pd
########################################################################################################################

#The data you have dowloaded off of GDELT will come as a zipped csv file
##You should store the data you requested in the same folder and name them same format, followed by a number
###This will allow glob to understand there is a dynamic nature in your .csv list and run through the files in a similar manner to a for loop

path= "D:\Desktop\GDELT_DATA_RAW\GDELT_DATA_MED_RARE"
allfiles=glob.glob(os.path.join(path, "GDELT_Med_Rare_*.csv"))
########################################################################################################################

#Here are some variables we will run with pd pandas and csv libraries
##allcsvfiles is essentially telling pandas that these csv files are delimitted with a comma rather than a space
###dfmerged tells pd pandas to concatenate all the allcsvfiles variable vertically and that the file has no index yet
####finally, dfmerged.to_csv is where we tell the script to drop and name our cooked data
#####You can concatenate well over 100,000 unique CAMEO events with this script if you practice good data hygiene

allcsvfiles=((pd.read_csv(f,sep=',')) for f in allfiles)
dfmerged= pd.concat(allcsvfiles, ignore_index=True)
dfmerged.to_csv("D:\Desktop\GDELT_DATA_Cooked\cooked3.csv", index=False)
########################################################################################################################

#Outside of the Google Big Query Environment, GDELT data has no sturcture or index to it
##This explains why we redundantly tell the code that there is no index in our script above
###colnames is the variable that gives our cooked data a structure that is interpretable as CAMEO language and adds columns to the dataframe
####please see the codebook attached in your Breaking Down GDELT Folder for a detailed summary of each column and how it relates to CAMEO language

colnames=["Global_Event_ID", "Day", "YYYYMM", "YYYY", "Day_Time", "Actor_1_Country_Code", "Actor_1_Name",
            "Actor_1_Country_ABBR", "Actor_1_Known_Group_Code", "Actor_1_Ethnic_Code", "Actor_1_Religion_Code",
            "Actor_1_Religion_2_Code", "Actor_1_Role", "Actor_1_Role2", "Actor_1_Role3", "Actor_2_Country_Code",
            "Actor_2_Name", "Actor_2_Country_ABBR", "Actor_2_Know_Group_Code", "Actor_2_Ethnic_Code",
            "Actor_2_Religion_Code", "Actor_2_Religion_2_Code", "Actor_2_Role", "Actor_2_Role2", "Actor_2_Role3",
            "Is_Root_Event", "Event_Code", "Event_Base_Code", "Event_Root_Code", "Quad_Class", "Goldstein_Scale",
            "Num_Mentions", "Num_Sources", "Num_Articles", "AVG_TONE", "Actor_1_Geo_Type", "Actor_1_Geo_FullName",
            "Actor_1_Geo_Country_Code", "Actor1Geo_ADM1Code", "Actor1Geo_ADM2Code", "Actor1Geo_Lat", "Actor1Geo_Long",
            "Actor1Geo_FeatureID", "Actor_2_Geo_Type", "Actor_2_Geo_FullName", "Actor_2_Geo_Country_Code",
            "Actor2Geo_ADM1Code", "Actor2Geo_ADM2Code", "Actor2Geo_Lat", "Actor2Geo_Long", "Actor2Geo_FeatureID",
            "Mention_Type", "ST_PR_CNTRY", "Country", "ADM1Code_Extra", "ADM2Code_Extra", "Lat_Extra", "Long_Extra",
            "ActorGeo_FeaturID_Extra", "Date_Added", "Source_URL", "Start_X_ACT1toACT2", "End_X_ACT1toAct2",
            "Start_Y_Act1toAct2", "End_Y_Act1toAct2", "Start_X_Act2toAct1", "End_X_Act2toAct1", "Start_Y_Act2toAct1",
            "End_Y_Act2toAct1"]
########################################################################################################################

#As redundant as this step may seem, it is necessary to to see if the cooked data now has column names in the pd pandas environment in our script
##The columns will now print in your python interpreter
###if the columns look well-structured, you can then know that where you export this dataframe will have an index and CAMEO language structure to it

dataframe=pd.read_csv("D:\Desktop\GDELT_DATA_Cooked\cooked3.csv", names=colnames, header=0, index_col=False)
dataframe.columns=colnames
#print(dataframe.columns)
dataframe.to_csv("D:\Desktop\GDELT_DATA_Cooked\cooked_columns3.csv")



########################################################################################################################

#One of the largest critiques of GDELT data and its use of CAMEO language is that it is not well-structured for actual geographic and social network analysis
##If you have already famiiarized yourself with the codebook, you will likely realize that this dataframe is not yet well-suited to create a graph for meaningful analysis outside of Google Big Query
###We will now make separate files of our cooked dataframe and use it as a "legacy table"
####Open your other python documents to complete the network build



#######################################################################################################################

#Use pd pandas reader to open your cooked file from the CSV_Concactenate_GDELT.py file as a dataframe
##Then make a dataframe with uscols= clause to grab columns for your actor1 nodes
###export the dataframe as Actor1Nodes
dataframeactor1= pd.read_csv("D:\Desktop\GDELT_DATA_Cooked\cooked_columns3.csv", usecols = ["Global_Event_ID", "Day", "YYYYMM", "YYYY", "Day_Time", "Actor_1_Country_Code", "Actor_1_Name",
            "Actor_1_Country_ABBR", "Actor_1_Known_Group_Code", "Actor_1_Ethnic_Code", "Actor_1_Religion_Code",
            "Actor_1_Religion_2_Code", "Actor_1_Role", "Actor_1_Role2", "Actor_1_Role3", "Is_Root_Event", "Event_Code", "Event_Base_Code", "Event_Root_Code", "Quad_Class", "Goldstein_Scale",
            "Num_Mentions", "Num_Sources", "Num_Articles", "AVG_TONE", "Actor_1_Geo_Type", "Actor_1_Geo_FullName",
            "Actor_1_Geo_Country_Code", "Actor1Geo_ADM1Code", "Actor1Geo_ADM2Code", "Actor1Geo_Lat", "Actor1Geo_Long",
            "Actor1Geo_FeatureID"])
dataframeactor1.to_csv("D:\Desktop\GDELT_DATA_Cooked\Actor1Nodes.csv", index=True)
########################################################################################################################

#Use pd pandas reader to open your cooked file from the CSV_Concactenate_GDELT.py file as a dataframe
##Then make a dataframe with uscols= clause to grab columns for your actor1 nodes
###export the dataframe as Actor2Nodes
dataframeactor2= pd.read_csv("D:\Desktop\GDELT_DATA_Cooked\cooked_columns3.csv", usecols = ["Global_Event_ID", "Day", "YYYYMM", "YYYY", "Day_Time", "Actor_2_Country_Code",
            "Actor_2_Name", "Actor_2_Country_ABBR", "Actor_2_Know_Group_Code", "Actor_2_Ethnic_Code",
            "Actor_2_Religion_Code", "Actor_2_Religion_2_Code", "Actor_2_Role", "Actor_2_Role2", "Actor_2_Role3",
            "Is_Root_Event", "Event_Code", "Event_Base_Code", "Event_Root_Code", "Quad_Class", "Goldstein_Scale",
            "Num_Mentions", "Num_Sources", "Num_Articles", "AVG_TONE", "Actor_2_Geo_Type", "Actor_2_Geo_FullName", "Actor_2_Geo_Country_Code",
            "Actor2Geo_ADM1Code", "Actor2Geo_ADM2Code", "Actor2Geo_Lat", "Actor2Geo_Long", "Actor2Geo_FeatureID"])
dataframeactor2.to_csv("D:\Desktop\GDELT_DATA_Cooked\Actor22Nodes.csv", index=True)
########################################################################################################################

# We will now make lines for our network analysis
##Sometimes, network analysis calls for different directions on line paths for more robust analaysis
###For this reason, we will make 2 line files
####The two line files can connote an active and passive role between actor 1 and actor 2 and we want to be able to travel both ways in our analysis
########################################################################################################################

#In this section, we will make the actor 1 to actor 2 lines for our dataset
##This connotes that actor 1 in the news heading is taking the active role in our CAMEO language onto actor 2
###We added extra empty columns for this very reason e.g. stat_X_act1toact2
####We will use simple expressions to load in the coordinated for our line data
dataframeactor1toactor2=pd.read_csv("D:\Desktop\GDELT_DATA_Cooked\cooked_columns3.csv", usecols =["Global_Event_ID", "Day", "YYYYMM", "YYYY", "Day_Time", "Actor1Geo_Lat", "Actor1Geo_Long", "Actor2Geo_Lat", "Actor2Geo_Long", "Start_X_ACT1toACT2", "End_X_ACT1toAct2",
            "Start_Y_Act1toAct2", "End_Y_Act1toAct2"])
dataframeactor1toactor2['Start_X_ACT1toACT2'] = dataframeactor1toactor2['Actor1Geo_Lat']
dataframeactor1toactor2['End_X_ACT1toAct2'] = dataframeactor1toactor2['Actor2Geo_Long']
dataframeactor1toactor2['Start_Y_Act1toAct2'] = dataframeactor1toactor2['Actor1Geo_Lat']
dataframeactor1toactor2['End_Y_Act1toAct2'] = dataframeactor1toactor2['Actor2Geo_Long']
dataframeactor1toactor2.to_csv("D:\Desktop\GDELT_DATA_Cooked\Actor1toActor2Lines.csv", index=False)
########################################################################################################################
#In this section, we will make the actor 1 to actor 2 lines for our dataset
##This connotes that actor 1 in the news heading is taking the active role in our CAMEO language onto actor 2
###We added extra empty columns for this very reason e.g. stat_X_act1toact2
####We will use simple expressions to load in the coordinated for our line data
dataframeactor2toactor1=pd.read_csv("D:\Desktop\GDELT_DATA_Cooked\cooked_columns3.csv", usecols =["Global_Event_ID", "Day", "YYYYMM", "YYYY", "Day_Time", "Actor1Geo_Lat", "Actor1Geo_Long", "Actor2Geo_Lat", "Actor2Geo_Long", "Start_X_Act2toAct1", "End_X_Act2toAct1", "Start_Y_Act2toAct1",
            "End_Y_Act2toAct1"])
dataframeactor2toactor1['Start_X_Act2toAct1'] = dataframeactor2toactor1['Actor2Geo_Lat']
dataframeactor2toactor1['End_X_Act2toAct1'] = dataframeactor2toactor1['Actor1Geo_Long']
dataframeactor2toactor1['Start_Y_Act2toAct1'] = dataframeactor2toactor1['Actor2Geo_Lat']
dataframeactor2toactor1['End_Y_Act2toAct1'] = dataframeactor2toactor1['Actor1Geo_Long']
dataframeactor2toactor1.to_csv("D:\Desktop\GDELT_DATA_Cooked\Actor2toActor1Lines.csv", index=False)

########################################################################################################################

#You should now have 5 pretty files that put the CAMEO language into what a GIS Analyst might prefer to work with
##You will have one master cooked table, 2 nodes, and 2 lines with inverse directions of one another
###The next steps are on you as the analyst to decide what to do with potentially spatially coincident data
####The best thing you can do now is geocode your csv files into a working network in a GISystem
#####Do no let GDELT force your hand into paying for Google Big Query as you can turn GDELT data into a stable file for use elsewhere free of charge
######CAMEO language has been summarized in the codebook for your use :)
#######Use your dataset as a means to take GDELT back into the open source realm, Big Query and Google Cloud can become costly
########...and with the amount of data you can use on GDELT, you will rack up a bill sooner than you might think!

















