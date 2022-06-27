def Test_Basic_Open_Close_App_Via_Keyword_Template():
    #Replaces the current indicator text with the specified one.
    Indicator.PushText("Test_Basic_Open_Close_App_Via_Keyword_Template")
    #Creates a log folder and makes it the current folder to which messages will be posted. This folder can contain messages of different types as well as subfolders.
    Log.AppendFolder("Test_Basic_Open_Close_App_Via_Keyword_Template", "This is a test template to be used as a seed for new tests", pmNormal, Project.Variables.LogAtrribTestTitle)
    #Runs a keyword test.
    KeywordTests.Mod_Start_TestedApp.Run()
    #Runs a keyword test.
    KeywordTests.Mod_Close_TestedApp.Run()
    #Pops the folder that is currently at the top of the folder stack out of the stack. This makes the folder that will become the top of the stack the default folder of the test log.
    Log.PopLogFolder()
    #Restores the previous indicator text.
    Indicator.PopText()

def Test_Basic_Open_Close_App_Via_Scripts_Template():
    import Mods_Sanity
    #Replaces the current indicator text with the specified one.
    Indicator.PushText("Test_Basic_Open_Close_App_Via_Scripts_Template")
    #Creates a log folder and makes it the current folder to which messages will be posted. This folder can contain messages of different types as well as subfolders.
    Log.AppendFolder("Test_Basic_Open_Close_App_Via_Scripts_Template", "This is a test template to be used as a seed for new tests", pmNormal, Project.Variables.LogAtrribTestTitle)
    #Runs a script routine.
    Mods_Sanity.Mod_Start_TestedApp()
    #Runs a script routine.
    Mods_Sanity.Mod_Close_TestedApp()
    #Pops the folder that is currently at the top of the folder stack out of the stack. This makes the folder that will become the top of the stack the default folder of the test log.
    Log.PopLogFolder()
    #Restores the previous indicator text.
    Indicator.PopText()
