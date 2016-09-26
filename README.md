CSV to Gource
Python Scipting by Brian Evans

--------
Contents
========
1. Purpose/Description
2. Requirements
3. Using CSV for Gource
4. Copyright Info

--------------
1. Description
==============
CSV for Gource will convert Load_History date exported from SQL Server Management studio
into a format readable by the Gource 3D Visualization application.

---------------
2. Requirements
===============
- Python 2.x.x
- Gource
- SQL Server Management Studio
- Access to IFP2 and SG2 Load History

-----------------------
3. Using CSV for Gource
=======================

The first step in using CSV for Gource is to export a TAB delimited CSV file from SQL Server Management Studio.
To do so you will want to use a script such as the one that follows:

 SELECT TOP 20000 loadTaskCompleteDateTime, loadRequestedBy, loadEnvironmentDesc, periodid, carrierIDs, RemovedcarrierIDs FROM IFP2..vwLoadHistory
 WHERE loadTaskCompleteDateTime is not NULL

Notice that the select is done to a limited set. I cannot stress enough that the entire dataset of the load history is far too large to be either useful or processable in any timely manner. I used 20k in my example, but larger is possible, smaller is faster.
It is important that the columns listed as viewable are left in that order and are not added to.
The where clause can be anything you'd like, but I recommend keeping the 'isnotNull' for completion date in there, as a NULL value will not illicit a response from Gource anyway, and may cause trouble down the line.
After running your query, export/output the results as a tab delimited CSV.
TAB delimited CSV will likely not be the default behavior and will require action on your part. 

 Run CSV-to-Gorse.py
 Click ‘Format CSV for Gource’. Select the file you saved (the one with the SQL tab delimited data). 

If all went well, you should be able to click on ‘Run CSV In Gource’. That will take you to a console command prompt at which you can enter any run-time parameters for gource, or just type ‘none’ and hit enter.

 Gource will run your data. Hit ESC to close out of Gource and click ‘Quit’ to leave CSVtoGource.

----------------
5. Copyleft Info
================
Created by Brian Evans, with helpful input from Matthew Smithson and Andrew Kaplan 09/23/16
 GNU GPL-3 Copyleft. Basically: you are free to sue and modify this software on the condition that the result is also freely useable by others and that attribution of the original developers is given.
