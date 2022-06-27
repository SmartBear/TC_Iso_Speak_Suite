def Test_Copy_File():
    #Replaces the current indicator text with the specified one.
    Indicator.PushText("Test_Copy_File")
    #Creates a log folder and makes it the current folder to which messages will be posted. This folder can contain messages of different types as well as subfolders.
    Log.AppendFolder("Test_Copy_File", "This is a test template to be used as a seed for new tests", pmNormal, Project.Variables.LogAtrribTestTitle)
    #The beginning of the Test_Copy_File group
    #Executes the specified code snippet.
    aqFileSystem.CopyFile("C:\\Temp\\IsoPlexis\\Contact_List.csv", "C:\\Shared_TC_Projects\\Iso_Speak_Suite\Iso_Speak_Desktop_Training_Project\\Data_Files\\Contact_List.csv")
    #Posts an information message to the test log.
    Log.Message("File C:\\\\Shared_TC_Projects\\\\Iso_Speak_Suite\\Iso_Speak_Desktop_Training_Project\\\\Data_Files\\\\Contact_List.csv should have been copied", 'aqFileSystem.CopyFile(\"C:\\\\Temp\\\\IsoPlexis\\\\Contact_List.csv\", \"C:\\\\Shared_TC_Projects\\\\Iso_Speak_Suite\\Iso_Speak_Desktop_Training_Project\\\\Data_Files\\\\Contact_List.csv\")  was executed', pmNormal, Project.Variables.LogAtrribInformation)
    #The end of the Test_Copy_File group
    #Pops the folder that is currently at the top of the folder stack out of the stack. This makes the folder that will become the top of the stack the default folder of the test log.
    Log.PopLogFolder()
    #Restores the previous indicator text.
    Indicator.PopText()
